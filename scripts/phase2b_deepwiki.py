"""Phase 2b: DeepWiki scan for Valkey/Redis integration signals."""

import asyncio
import json
import logging
import re
import sys

import httpx

from config import (
    DATA_DIR,
    DEEPWIKI_BASE_URL,
    VALKEY_EXPLICIT_KEYWORDS,
    VALKEY_GLIDE_KEYWORDS,
    REDIS_KEYWORDS,
    REDIS_MODULE_KEYWORDS,
    CONCURRENT_REQUESTS,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

sem = asyncio.Semaphore(CONCURRENT_REQUESTS)


def find_keyword_matches(text: str, keywords: list[str]) -> list[dict]:
    """Find keyword occurrences in text with surrounding context."""
    matches = []
    text_lower = text.lower()
    lines = text.split("\n")
    for kw in keywords:
        kw_lower = kw.lower()
        if kw_lower not in text_lower:
            continue
        contexts = []
        for i, line in enumerate(lines):
            if kw_lower in line.lower():
                contexts.append({"line": i + 1, "text": line.strip()[:200]})
                if len(contexts) >= 3:
                    break
        matches.append({"keyword": kw, "count": text_lower.count(kw_lower), "contexts": contexts})
    return matches


def find_module_matches(text: str) -> dict[str, list[dict]]:
    """Find Redis module keyword matches."""
    results = {}
    for module, keywords in REDIS_MODULE_KEYWORDS.items():
        matches = find_keyword_matches(text, keywords)
        if matches:
            results[module] = matches
    return results


async def fetch_deepwiki(client: httpx.AsyncClient, owner: str, repo: str) -> str | None:
    """Fetch DeepWiki page for a repo."""
    url = f"{DEEPWIKI_BASE_URL}/{owner}/{repo}"
    async with sem:
        try:
            resp = await client.get(url, follow_redirects=True, timeout=20)
            if resp.status_code == 200:
                return resp.text
            return None
        except Exception as e:
            log.debug("DeepWiki error for %s/%s: %s", owner, repo, e)
            return None


async def analyze_repo(client: httpx.AsyncClient, owner: str, repo: str) -> dict:
    """Analyze a single repo via DeepWiki."""
    result = {
        "owner": owner,
        "repo_name": repo,
        "github_url": f"https://github.com/{owner}/{repo}",
        "deepwiki_available": False,
        "valkey_mentions": [],
        "valkey_glide_mentions": [],
        "redis_mentions": [],
        "redis_module_mentions": {},
        "has_valkey_signal": False,
        "has_redis_signal": False,
        "has_redis_module_signal": False,
    }

    content = await fetch_deepwiki(client, owner, repo)
    if not content:
        return result

    result["deepwiki_available"] = True

    # Strip HTML tags for cleaner text matching
    text = re.sub(r"<[^>]+>", " ", content)

    result["valkey_mentions"] = find_keyword_matches(text, VALKEY_EXPLICIT_KEYWORDS)
    result["valkey_glide_mentions"] = find_keyword_matches(text, VALKEY_GLIDE_KEYWORDS)
    result["redis_mentions"] = find_keyword_matches(text, REDIS_KEYWORDS)
    result["redis_module_mentions"] = find_module_matches(text)

    result["has_valkey_signal"] = bool(result["valkey_mentions"] or result["valkey_glide_mentions"])
    result["has_redis_signal"] = bool(result["redis_mentions"])
    result["has_redis_module_signal"] = bool(result["redis_module_mentions"])

    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 2b analysis."""
    repos_file = DATA_DIR / "repos.json"
    if not repos_file.exists():
        log.error("repos.json not found — run Phase 1 first to fetch repo list")
        sys.exit(1)

    all_repos = json.loads(repos_file.read_text())["repos"]
    log.info("Loaded %d repos", len(all_repos))

    if repo_filter:
        repos = [{"owner": r.split("/")[0], "repo_name": r.split("/")[1]} for r in repo_filter]
    else:
        repos = []
        for r in all_repos:
            parts = r["github_url"].rstrip("/").split("/")
            repos.append({"owner": parts[-2], "repo_name": parts[-1]})

    log.info("Phase 2b: scanning DeepWiki for %d repos", len(repos))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            log.info("[%d/%d] DeepWiki scan for %s/%s", i + 1, len(repos), repo["owner"], repo["repo_name"])
            result = await analyze_repo(client, repo["owner"], repo["repo_name"])
            results.append(result)

    available = sum(1 for r in results if r["deepwiki_available"])
    valkey_count = sum(1 for r in results if r["has_valkey_signal"])
    redis_count = sum(1 for r in results if r["has_redis_signal"])
    module_count = sum(1 for r in results if r["has_redis_module_signal"])
    log.info("Phase 2b complete: %d/%d available, %d valkey, %d redis, %d redis modules",
             available, len(results), valkey_count, redis_count, module_count)

    output = DATA_DIR / "phase2b_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
