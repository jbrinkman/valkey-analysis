"""Phase 1: Scan package manifests for Valkey/Redis client library dependencies."""

import asyncio
import base64
import json
import logging
import sys

import httpx

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    MANIFEST_FILES,
    REPOS_API_URL,
    VALKEY_DEPENDENCIES,
    REDIS_DEPENDENCIES,
    VALKEY_GLIDE_KEYWORDS,
)
from github_client import github_get, log_rate_status

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


async def fetch_repo_list() -> list[dict]:
    """Fetch the master repo list from the API, or load from cache."""
    cache = DATA_DIR / "repos.json"
    if cache.exists():
        log.info("Loading cached repo list from %s", cache)
        return json.loads(cache.read_text())["repos"]

    log.info("Fetching repo list from %s", REPOS_API_URL)
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(REPOS_API_URL)
        resp.raise_for_status()
        data = resp.json()
    cache.write_text(json.dumps(data, indent=2))
    return data["repos"]


def scan_manifest(filename: str, content: str) -> dict:
    """Scan a manifest file for Valkey/Redis dependencies. Returns found deps."""
    found = {"valkey": [], "redis": [], "valkey_glide": False, "file": filename}
    text_lower = content.lower()

    for dep, category in VALKEY_DEPENDENCIES.items():
        if dep.lower() in text_lower:
            found["valkey"].append({"name": dep, "category": category})
            if category == "valkey-glide":
                found["valkey_glide"] = True

    for dep, category in REDIS_DEPENDENCIES.items():
        if dep.lower() in text_lower:
            found["redis"].append({"name": dep, "category": category})

    for kw in VALKEY_GLIDE_KEYWORDS:
        if kw.lower() in text_lower and not found["valkey_glide"]:
            found["valkey_glide"] = True

    return found


async def analyze_repo(client: httpx.AsyncClient, repo: dict) -> dict:
    """Analyze a single repo's dependencies using tree API to minimize calls."""
    url = repo["github_url"]
    parts = url.rstrip("/").split("/")
    owner, name = parts[-2], parts[-1]

    result = {
        "owner": owner,
        "repo_name": name,
        "github_url": url,
        "manifests_checked": [],
        "valkey_deps": [],
        "redis_deps": [],
        "valkey_glide_found": False,
        "triage": "no_dep_signal",
    }

    # Use tree API to list files — 1 call instead of 13
    tree_url = f"{GITHUB_API_BASE}/repos/{owner}/{name}/git/trees/HEAD"
    tree_data = await github_get(client, tree_url, {"recursive": "false"})

    if not tree_data or "tree" not in tree_data:
        return result

    # Find which manifest files exist in the repo root
    existing_files = {item["path"] for item in tree_data["tree"] if item["type"] == "blob"}
    manifests_to_fetch = [f for f in MANIFEST_FILES if f in existing_files]

    # Fetch only the manifests that exist
    for filename in manifests_to_fetch:
        content_url = f"{GITHUB_API_BASE}/repos/{owner}/{name}/contents/{filename}"
        data = await github_get(client, content_url)
        if not data or not data.get("content"):
            continue

        try:
            content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        except Exception:
            continue

        result["manifests_checked"].append(filename)
        scan = scan_manifest(filename, content)

        if scan["valkey"]:
            result["valkey_deps"].extend(scan["valkey"])
        if scan["redis"]:
            result["redis_deps"].extend(scan["redis"])
        if scan["valkey_glide"]:
            result["valkey_glide_found"] = True

    # Deduplicate
    seen_v = set()
    result["valkey_deps"] = [d for d in result["valkey_deps"] if d["name"] not in seen_v and not seen_v.add(d["name"])]
    seen_r = set()
    result["redis_deps"] = [d for d in result["redis_deps"] if d["name"] not in seen_r and not seen_r.add(d["name"])]

    # Triage
    if result["valkey_deps"]:
        result["triage"] = "has_valkey_dep"
    elif result["redis_deps"]:
        result["triage"] = "has_redis_dep"

    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 1 analysis."""
    repos = await fetch_repo_list()
    log.info("Loaded %d repos", len(repos))

    if repo_filter:
        repos = [r for r in repos if f"{r['github_url'].rstrip('/').split('/')[-2]}/{r['github_url'].rstrip('/').split('/')[-1]}" in repo_filter]
        log.info("Filtered to %d repos", len(repos))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            log.info("[%d/%d] Analyzing %s", i + 1, len(repos), repo["github_url"])
            result = await analyze_repo(client, repo)
            results.append(result)
            if (i + 1) % 100 == 0:
                log_rate_status()

    valkey_count = sum(1 for r in results if r["triage"] == "has_valkey_dep")
    redis_count = sum(1 for r in results if r["triage"] == "has_redis_dep")
    none_count = sum(1 for r in results if r["triage"] == "no_dep_signal")
    log.info("Phase 1 complete: %d valkey, %d redis, %d none", valkey_count, redis_count, none_count)

    output = DATA_DIR / "phase1_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
