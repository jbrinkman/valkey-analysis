"""Phase 2: Scan README and documentation sites for Valkey/Redis mentions."""

import asyncio
import base64
import json
import logging
import re
import sys
from urllib.parse import urlparse

import httpx

from config import (
    DATA_DIR,
    VALKEY_EXPLICIT_KEYWORDS,
    VALKEY_GLIDE_KEYWORDS,
    REDIS_KEYWORDS,
    REDIS_MODULE_KEYWORDS,
    CONCURRENT_REQUESTS,
)
from github_client import github_get, log_rate_status

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

sem = asyncio.Semaphore(CONCURRENT_REQUESTS)

# Patterns to extract docs URLs from README
DOCS_URL_PATTERNS = [
    r'https?://docs\.[a-zA-Z0-9\-]+\.[a-z]+[^\s\)\"\']*',
    r'https?://[a-zA-Z0-9\-]+\.readthedocs\.io[^\s\)\"\']*',
    r'https?://[a-zA-Z0-9\-]+\.gitbook\.io[^\s\)\"\']*',
    r'https?://[a-zA-Z0-9\-]+\.github\.io[^\s\)\"\']*',
]


def find_keyword_matches(text: str, keywords: list[str]) -> list[dict]:
    """Find keyword occurrences in text with surrounding context."""
    matches = []
    text_lower = text.lower()
    lines = text.split("\n")
    for kw in keywords:
        kw_lower = kw.lower()
        if kw_lower not in text_lower:
            continue
        # Find lines containing the keyword for context
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


def extract_docs_urls(text: str, homepage: str | None = None) -> list[str]:
    """Extract documentation site URLs from README text and repo homepage."""
    urls = set()
    for pattern in DOCS_URL_PATTERNS:
        for match in re.findall(pattern, text):
            clean = match.rstrip(".,;:!?)")
            urls.add(clean)
    if homepage and homepage.startswith("http"):
        urls.add(homepage)
    return list(urls)


async def fetch_readme(client: httpx.AsyncClient, owner: str, repo: str) -> str | None:
    """Fetch README content via GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    data = await github_get(client, url)
    if not data or not data.get("content"):
        return None
    try:
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    except Exception:
        return None


async def fetch_repo_metadata(client: httpx.AsyncClient, owner: str, repo: str) -> dict | None:
    """Fetch repo metadata for homepage URL."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    return await github_get(client, url)


async def fetch_docs_page(client: httpx.AsyncClient, url: str) -> str | None:
    """Fetch a documentation page and return text content."""
    async with sem:
        try:
            resp = await client.get(url, follow_redirects=True, timeout=15)
            if resp.status_code != 200:
                return None
            content_type = resp.headers.get("content-type", "")
            if "html" in content_type or "text" in content_type:
                return resp.text
            return None
        except Exception as e:
            log.debug("Error fetching docs page %s: %s", url, e)
            return None


async def analyze_repo(client: httpx.AsyncClient, repo: dict) -> dict:
    """Analyze a single repo's documentation for Valkey/Redis mentions."""
    url = repo["github_url"]
    parts = url.rstrip("/").split("/")
    owner, name = parts[-2], parts[-1]

    result = {
        "owner": owner,
        "repo_name": name,
        "github_url": url,
        "readme_found": False,
        "valkey_mentions": [],
        "valkey_glide_mentions": [],
        "redis_mentions": [],
        "redis_module_mentions": {},
        "docs_urls_found": [],
        "docs_valkey_mentions": [],
        "docs_redis_mentions": [],
        "has_valkey_signal": False,
        "has_redis_signal": False,
    }

    # Fetch README and metadata concurrently
    readme_task = fetch_readme(client, owner, name)
    meta_task = fetch_repo_metadata(client, owner, name)
    readme_content, metadata = await asyncio.gather(readme_task, meta_task)

    homepage = metadata.get("homepage", "") if metadata else ""

    if readme_content:
        result["readme_found"] = True
        result["valkey_mentions"] = find_keyword_matches(readme_content, VALKEY_EXPLICIT_KEYWORDS)
        result["valkey_glide_mentions"] = find_keyword_matches(readme_content, VALKEY_GLIDE_KEYWORDS)
        result["redis_mentions"] = find_keyword_matches(readme_content, REDIS_KEYWORDS)
        result["redis_module_mentions"] = find_module_matches(readme_content)
        result["docs_urls_found"] = extract_docs_urls(readme_content, homepage)
    elif homepage:
        result["docs_urls_found"] = [homepage]

    # Scan up to 3 docs pages for keyword mentions
    for docs_url in result["docs_urls_found"][:3]:
        page_content = await fetch_docs_page(client, docs_url)
        if not page_content:
            continue
        valkey_hits = find_keyword_matches(page_content, VALKEY_EXPLICIT_KEYWORDS)
        redis_hits = find_keyword_matches(page_content, REDIS_KEYWORDS)
        if valkey_hits:
            result["docs_valkey_mentions"].append({"url": docs_url, "matches": valkey_hits})
        if redis_hits:
            result["docs_redis_mentions"].append({"url": docs_url, "matches": redis_hits})

    # Set signal flags
    result["has_valkey_signal"] = bool(result["valkey_mentions"] or result["valkey_glide_mentions"] or result["docs_valkey_mentions"])
    result["has_redis_signal"] = bool(result["redis_mentions"] or result["docs_redis_mentions"])

    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 2 analysis."""
    repos_file = DATA_DIR / "repos.json"
    if not repos_file.exists():
        log.error("repos.json not found — run Phase 1 first to fetch repo list")
        sys.exit(1)

    repos = json.loads(repos_file.read_text())["repos"]
    log.info("Loaded %d repos", len(repos))

    if repo_filter:
        repos = [r for r in repos if f"{r['github_url'].rstrip('/').split('/')[-2]}/{r['github_url'].rstrip('/').split('/')[-1]}" in repo_filter]
        log.info("Filtered to %d repos", len(repos))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            log.info("[%d/%d] Scanning docs for %s", i + 1, len(repos), repo["github_url"])
            result = await analyze_repo(client, repo)
            results.append(result)

    valkey_count = sum(1 for r in results if r["has_valkey_signal"])
    redis_count = sum(1 for r in results if r["has_redis_signal"])
    log.info("Phase 2 complete: %d valkey signals, %d redis signals", valkey_count, redis_count)

    output = DATA_DIR / "phase2_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
