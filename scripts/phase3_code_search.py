"""Phase 3: GitHub code search for Valkey/Redis references in repo source code."""

import asyncio
import json
import logging
import sys
import time

import httpx

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    GITHUB_HEADERS,
    VALKEY_EXPLICIT_KEYWORDS,
    VALKEY_GLIDE_KEYWORDS,
    REDIS_MODULE_KEYWORDS,
    GITHUB_SEARCH_RPM,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

# Code search rate limit: 30 req/min authenticated
SEARCH_INTERVAL = 60.0 / GITHUB_SEARCH_RPM + 0.1  # seconds between requests

# Keywords to search in code (kept focused to stay within rate limits)
CODE_SEARCH_KEYWORDS = {
    "valkey": VALKEY_EXPLICIT_KEYWORDS,
    "valkey_glide": VALKEY_GLIDE_KEYWORDS,
    "redis_modules": [kw for kws in REDIS_MODULE_KEYWORDS.values() for kw in kws if "." not in kw],
}


async def search_code(client: httpx.AsyncClient, query: str, last_request_time: list[float]) -> dict | None:
    """Execute a GitHub code search with rate limiting. Returns API response or None."""
    # Enforce rate limit
    elapsed = time.time() - last_request_time[0]
    if elapsed < SEARCH_INTERVAL:
        await asyncio.sleep(SEARCH_INTERVAL - elapsed)

    url = f"{GITHUB_API_BASE}/search/code"
    params = {"q": query, "per_page": 10}

    try:
        resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
        last_request_time[0] = time.time()

        if resp.status_code == 403:
            retry_after = int(resp.headers.get("Retry-After", "60"))
            log.warning("Code search rate limited, sleeping %ds", retry_after)
            await asyncio.sleep(retry_after)
            resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
            last_request_time[0] = time.time()

        if resp.status_code == 422:
            log.debug("Search query validation error for: %s", query)
            return None

        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        log.warning("Code search error for query '%s': %s", query, e)
        return None


def extract_search_hits(response: dict) -> list[dict]:
    """Extract relevant info from code search results."""
    if not response or "items" not in response:
        return []
    hits = []
    for item in response["items"]:
        hits.append({
            "file": item.get("path", ""),
            "url": item.get("html_url", ""),
            "score": item.get("score", 0),
        })
    return hits


async def analyze_repo(client: httpx.AsyncClient, owner: str, repo: str, last_request_time: list[float]) -> dict:
    """Run code searches for a single repo."""
    result = {
        "owner": owner,
        "repo_name": repo,
        "github_url": f"https://github.com/{owner}/{repo}",
        "valkey_code_hits": [],
        "valkey_glide_code_hits": [],
        "redis_module_code_hits": {},
        "valkey_total_files": 0,
        "redis_module_total_files": 0,
        "has_valkey_code": False,
        "has_valkey_glide_code": False,
        "has_redis_module_code": False,
    }

    # Search for Valkey keywords
    for kw in CODE_SEARCH_KEYWORDS["valkey"]:
        query = f'"{kw}" repo:{owner}/{repo}'
        resp = await search_code(client, query, last_request_time)
        if resp and resp.get("total_count", 0) > 0:
            hits = extract_search_hits(resp)
            result["valkey_code_hits"].append({
                "keyword": kw,
                "total_count": resp["total_count"],
                "files": hits,
            })

    # Search for Valkey-Glide keywords
    for kw in CODE_SEARCH_KEYWORDS["valkey_glide"]:
        query = f'"{kw}" repo:{owner}/{repo}'
        resp = await search_code(client, query, last_request_time)
        if resp and resp.get("total_count", 0) > 0:
            hits = extract_search_hits(resp)
            result["valkey_glide_code_hits"].append({
                "keyword": kw,
                "total_count": resp["total_count"],
                "files": hits,
            })

    # Search for Redis module keywords including command prefixes (FT., TS., etc.)
    for module, keywords in REDIS_MODULE_KEYWORDS.items():
        module_hits = []
        for kw in keywords:
            query = f'"{kw}" repo:{owner}/{repo}'
            resp = await search_code(client, query, last_request_time)
            if resp and resp.get("total_count", 0) > 0:
                hits = extract_search_hits(resp)
                module_hits.append({
                    "keyword": kw,
                    "total_count": resp["total_count"],
                    "files": hits,
                })
        if module_hits:
            result["redis_module_code_hits"][module] = module_hits

    # Summarize
    result["valkey_total_files"] = sum(h["total_count"] for h in result["valkey_code_hits"])
    result["redis_module_total_files"] = sum(
        h["total_count"] for hits in result["redis_module_code_hits"].values() for h in hits
    )
    result["has_valkey_code"] = result["valkey_total_files"] > 0
    result["has_valkey_glide_code"] = len(result["valkey_glide_code_hits"]) > 0
    result["has_redis_module_code"] = result["redis_module_total_files"] > 0

    return result


def select_repos_for_search(phase1_path: str | None, phase2_path: str | None) -> list[dict]:
    """Select repos to search based on prior phase signals. Returns list of {owner, repo_name}."""
    repos_to_search = {}

    # All repos with any signal from Phase 1
    if phase1_path:
        p1 = json.loads(phase1_path)
        for r in p1:
            if r["triage"] in ("has_valkey_dep", "has_redis_dep"):
                key = f"{r['owner']}/{r['repo_name']}"
                repos_to_search[key] = {"owner": r["owner"], "repo_name": r["repo_name"]}

    # All repos with any signal from Phase 2
    if phase2_path:
        p2 = json.loads(phase2_path)
        for r in p2:
            if r["has_valkey_signal"] or r["has_redis_signal"]:
                key = f"{r['owner']}/{r['repo_name']}"
                repos_to_search[key] = {"owner": r["owner"], "repo_name": r["repo_name"]}

    return list(repos_to_search.values())


async def main(repo_filter: list[str] | None = None):
    """Run Phase 3 analysis."""
    # Load prior phase results to determine scope
    p1_file = DATA_DIR / "phase1_results.json"
    p2_file = DATA_DIR / "phase2_results.json"

    p1_data = p1_file.read_text() if p1_file.exists() else None
    p2_data = p2_file.read_text() if p2_file.exists() else None

    if repo_filter:
        repos = [{"owner": r.split("/")[0], "repo_name": r.split("/")[1]} for r in repo_filter]
    elif p1_data or p2_data:
        repos = select_repos_for_search(p1_data, p2_data)
    else:
        log.error("No prior phase results found and no repo filter specified")
        sys.exit(1)

    log.info("Phase 3: searching code in %d repos", len(repos))

    results = []
    last_request_time = [0.0]

    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            owner, name = repo["owner"], repo["repo_name"]
            log.info("[%d/%d] Code search for %s/%s", i + 1, len(repos), owner, name)
            result = await analyze_repo(client, owner, name, last_request_time)
            results.append(result)

    valkey_count = sum(1 for r in results if r["has_valkey_code"])
    glide_count = sum(1 for r in results if r["has_valkey_glide_code"])
    module_count = sum(1 for r in results if r["has_redis_module_code"])
    log.info("Phase 3 complete: %d valkey code, %d glide code, %d redis module code", valkey_count, glide_count, module_count)

    output = DATA_DIR / "phase3_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
