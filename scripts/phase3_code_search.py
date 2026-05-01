"""Phase 3: GitHub code search for Valkey/Redis references in repo source code."""

import asyncio
import json
import logging
import sys

import httpx

from config import (
    DATA_DIR,
    REDIS_MODULE_KEYWORDS,
)
from github_client import github_search, log_rate_status

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

# Focused keyword sets — one query each to minimize API calls
# Valkey: single query for "valkey" catches valkey-py, valkey-glide, valkey-search etc.
# Glide: single query for "valkey-glide"
# Modules: one representative keyword per module (most distinctive)
MODULE_SEARCH_KEYWORDS = {
    "redisearch": "ft.search",
    "redistimeseries": "ts.add",
    "redisjson": "rejson",
    "redisbloom": "bf.add",
    "redisgraph": "graph.query",
    "redisai": "redisai",
}


async def code_search(client: httpx.AsyncClient, keyword: str, owner: str, repo: str) -> dict | None:
    """Run a single code search query."""
    params = {"q": f'"{keyword}" repo:{owner}/{repo}', "per_page": 10}
    return await github_search(client, "search/code", params, resource="code_search")


def extract_hits(response: dict) -> list[dict]:
    if not response or "items" not in response:
        return []
    return [
        {"file": item.get("path", ""), "url": item.get("html_url", "")}
        for item in response["items"]
    ]


async def analyze_repo(client: httpx.AsyncClient, owner: str, repo: str) -> dict:
    """Run code searches for a single repo. 8 queries total."""
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

    # Query 1: "valkey" — catches valkey, valkey-py, valkey-search, etc.
    resp = await code_search(client, "valkey", owner, repo)
    if resp and resp.get("total_count", 0) > 0:
        result["valkey_code_hits"].append({
            "keyword": "valkey",
            "total_count": resp["total_count"],
            "files": extract_hits(resp),
        })

    # Query 2: "valkey-glide" — specific glide check
    resp = await code_search(client, "valkey-glide", owner, repo)
    if resp and resp.get("total_count", 0) > 0:
        result["valkey_glide_code_hits"].append({
            "keyword": "valkey-glide",
            "total_count": resp["total_count"],
            "files": extract_hits(resp),
        })

    # Queries 3-8: one per Redis module
    for module, keyword in MODULE_SEARCH_KEYWORDS.items():
        resp = await code_search(client, keyword, owner, repo)
        if resp and resp.get("total_count", 0) > 0:
            result["redis_module_code_hits"][module] = [{
                "keyword": keyword,
                "total_count": resp["total_count"],
                "files": extract_hits(resp),
            }]

    # Summarize
    result["valkey_total_files"] = sum(h["total_count"] for h in result["valkey_code_hits"])
    result["redis_module_total_files"] = sum(
        h["total_count"] for hits in result["redis_module_code_hits"].values() for h in hits
    )
    result["has_valkey_code"] = result["valkey_total_files"] > 0
    result["has_valkey_glide_code"] = len(result["valkey_glide_code_hits"]) > 0
    result["has_redis_module_code"] = result["redis_module_total_files"] > 0

    return result


def select_repos_for_search() -> list[dict]:
    """Select repos to search based on prior phase signals."""
    repos_to_search = {}

    for phase_file, check_fn in [
        ("phase1_results.json", lambda r: r.get("triage") in ("has_valkey_dep", "has_redis_dep")),
        ("phase2_results.json", lambda r: r.get("has_valkey_signal") or r.get("has_redis_signal")),
        ("phase2b_results.json", lambda r: r.get("has_valkey_signal") or r.get("has_redis_signal")),
    ]:
        path = DATA_DIR / phase_file
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        for r in data:
            if check_fn(r):
                key = f"{r['owner']}/{r['repo_name']}"
                repos_to_search[key] = {"owner": r["owner"], "repo_name": r["repo_name"]}

    return list(repos_to_search.values())


async def main(repo_filter: list[str] | None = None):
    """Run Phase 3 analysis."""
    if repo_filter:
        repos = [{"owner": r.split("/")[0], "repo_name": r.split("/")[1]} for r in repo_filter]
    else:
        repos = select_repos_for_search()
        if not repos:
            log.error("No prior phase results found and no repo filter specified")
            sys.exit(1)

    # 8 queries per repo, 10 queries/min limit = ~1.25 repos/min
    est_minutes = len(repos) * 8 / 10
    log.info("Phase 3: searching code in %d repos (~8 queries each, est. %.0f min)", len(repos), est_minutes)

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            owner, name = repo["owner"], repo["repo_name"]
            log.info("[%d/%d] Code search for %s/%s", i + 1, len(repos), owner, name)
            result = await analyze_repo(client, owner, name)
            results.append(result)
            if (i + 1) % 10 == 0:
                log_rate_status()

    valkey_count = sum(1 for r in results if r["has_valkey_code"])
    glide_count = sum(1 for r in results if r["has_valkey_glide_code"])
    module_count = sum(1 for r in results if r["has_redis_module_code"])
    log.info("Phase 3 complete: %d valkey code, %d glide code, %d redis module code",
             valkey_count, glide_count, module_count)

    output = DATA_DIR / "phase3_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
