"""Phase 4: Search issues, PRs, discussions, and wiki for Valkey/Redis mentions."""

import asyncio
import json
import logging
import sys

import httpx

from config import (
    DATA_DIR,
    GITHUB_API_BASE,
    GITHUB_HEADERS,
    VALKEY_EXPLICIT_KEYWORDS,
    VALKEY_GLIDE_KEYWORDS,
    CONCURRENT_REQUESTS,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

sem = asyncio.Semaphore(CONCURRENT_REQUESTS)

# Focused search terms for issues/PRs/discussions
SEARCH_TERMS = ["valkey", "valkey-glide", "valkey-search"]


async def github_get(client: httpx.AsyncClient, url: str, params: dict | None = None) -> dict | None:
    """Make a rate-limit-aware GitHub API GET request."""
    async with sem:
        try:
            resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
            if resp.status_code == 403 and "rate limit" in resp.text.lower():
                retry_after = int(resp.headers.get("Retry-After", "60"))
                log.warning("Rate limited, sleeping %ds", retry_after)
                await asyncio.sleep(retry_after)
                resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
            if resp.status_code == 404:
                return None
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            log.debug("GitHub API error for %s: %s", url, e)
            return None


async def search_issues_prs(client: httpx.AsyncClient, owner: str, repo: str, term: str) -> list[dict]:
    """Search issues and PRs for a keyword using GitHub search API."""
    results = []
    url = f"{GITHUB_API_BASE}/search/issues"
    params = {"q": f'"{term}" repo:{owner}/{repo}', "per_page": 10, "sort": "updated"}

    data = await github_get(client, url, params)
    if not data or "items" not in data:
        return results

    for item in data["items"]:
        is_pr = "pull_request" in item
        results.append({
            "type": "pr" if is_pr else "issue",
            "number": item["number"],
            "title": item["title"],
            "state": item["state"],
            "url": item["html_url"],
            "created_at": item.get("created_at", ""),
            "updated_at": item.get("updated_at", ""),
            "labels": [l["name"] for l in item.get("labels", [])],
            "search_term": term,
        })

    return results


async def search_discussions(client: httpx.AsyncClient, owner: str, repo: str, term: str) -> list[dict]:
    """Search discussions using GitHub GraphQL API."""
    results = []
    query = """
    query($queryStr: String!) {
      search(query: $queryStr, type: DISCUSSION, first: 10) {
        nodes {
          ... on Discussion {
            number
            title
            url
            createdAt
            updatedAt
            category { name }
            answer { id }
          }
        }
      }
    }
    """
    variables = {"queryStr": f'"{term}" repo:{owner}/{repo}'}

    async with sem:
        try:
            resp = await client.post(
                "https://api.github.com/graphql",
                headers=GITHUB_HEADERS,
                json={"query": query, "variables": variables},
            )
            if resp.status_code == 403 and "rate limit" in resp.text.lower():
                retry_after = int(resp.headers.get("Retry-After", "60"))
                log.warning("Rate limited, sleeping %ds", retry_after)
                await asyncio.sleep(retry_after)
                resp = await client.post(
                    "https://api.github.com/graphql",
                    headers=GITHUB_HEADERS,
                    json={"query": query, "variables": variables},
                )
            resp.raise_for_status()
            data = resp.json()

            nodes = data.get("data", {}).get("search", {}).get("nodes", [])
            for node in nodes:
                if not node:
                    continue
                results.append({
                    "type": "discussion",
                    "number": node.get("number"),
                    "title": node.get("title", ""),
                    "url": node.get("url", ""),
                    "created_at": node.get("createdAt", ""),
                    "updated_at": node.get("updatedAt", ""),
                    "category": node.get("category", {}).get("name", ""),
                    "has_answer": node.get("answer") is not None,
                    "search_term": term,
                })
        except Exception as e:
            log.debug("Discussions search error for %s/%s: %s", owner, repo, e)

    return results


async def check_wiki(client: httpx.AsyncClient, owner: str, repo: str) -> dict:
    """Check if wiki exists and search for Valkey mentions via wiki pages API."""
    result = {"has_wiki": False, "valkey_mentions": []}

    # Check if repo has wiki enabled
    repo_data = await github_get(client, f"{GITHUB_API_BASE}/repos/{owner}/{repo}")
    if not repo_data or not repo_data.get("has_wiki"):
        return result

    result["has_wiki"] = True

    # Fetch wiki pages list
    pages_data = await github_get(client, f"{GITHUB_API_BASE}/repos/{owner}/{repo}/wiki/pages")
    if not pages_data:
        return result

    # Check page titles for Valkey/Redis mentions
    pages = pages_data if isinstance(pages_data, list) else []
    for page in pages[:20]:  # limit to first 20 pages
        title = page.get("title", "").lower() if isinstance(page, dict) else ""
        for kw in VALKEY_EXPLICIT_KEYWORDS:
            if kw.lower() in title:
                result["valkey_mentions"].append({
                    "page_title": page.get("title", ""),
                    "keyword": kw,
                })

    return result


async def analyze_repo(client: httpx.AsyncClient, owner: str, repo: str) -> dict:
    """Analyze a single repo's community signals."""
    result = {
        "owner": owner,
        "repo_name": repo,
        "github_url": f"https://github.com/{owner}/{repo}",
        "issues_prs": [],
        "discussions": [],
        "wiki": {"has_wiki": False, "valkey_mentions": []},
        "has_valkey_issues_prs": False,
        "has_valkey_discussions": False,
        "has_valkey_wiki": False,
    }

    # Search issues/PRs and discussions for each term
    for term in SEARCH_TERMS:
        issues_prs = await search_issues_prs(client, owner, repo, term)
        result["issues_prs"].extend(issues_prs)

        discussions = await search_discussions(client, owner, repo, term)
        result["discussions"].extend(discussions)

    # Deduplicate by URL
    seen_urls = set()
    deduped_ip = []
    for item in result["issues_prs"]:
        if item["url"] not in seen_urls:
            seen_urls.add(item["url"])
            deduped_ip.append(item)
    result["issues_prs"] = deduped_ip

    seen_urls = set()
    deduped_disc = []
    for item in result["discussions"]:
        if item["url"] not in seen_urls:
            seen_urls.add(item["url"])
            deduped_disc.append(item)
    result["discussions"] = deduped_disc

    # Check wiki
    result["wiki"] = await check_wiki(client, owner, repo)

    # Set flags
    result["has_valkey_issues_prs"] = len(result["issues_prs"]) > 0
    result["has_valkey_discussions"] = len(result["discussions"]) > 0
    result["has_valkey_wiki"] = len(result["wiki"]["valkey_mentions"]) > 0

    return result


def select_repos(repo_filter: list[str] | None) -> list[dict]:
    """Select repos to analyze based on prior phases or CLI filter."""
    if repo_filter:
        return [{"owner": r.split("/")[0], "repo_name": r.split("/")[1]} for r in repo_filter]

    # Load all repos from the master list — we search all for community signals
    # since issues/PRs about Valkey could exist even without code/dep signals
    repos_file = DATA_DIR / "repos.json"
    if not repos_file.exists():
        log.error("repos.json not found — run Phase 1 first")
        sys.exit(1)

    all_repos = json.loads(repos_file.read_text())["repos"]
    result = []

    # Prioritize repos with signals from earlier phases, but include all
    signaled = set()
    for phase_file in ["phase1_results.json", "phase2_results.json", "phase3_results.json"]:
        path = DATA_DIR / phase_file
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        for r in data:
            key = f"{r['owner']}/{r['repo_name']}"
            if phase_file == "phase1_results.json" and r.get("triage") != "no_dep_signal":
                signaled.add(key)
            elif phase_file == "phase2_results.json" and (r.get("has_valkey_signal") or r.get("has_redis_signal")):
                signaled.add(key)
            elif phase_file == "phase3_results.json" and (r.get("has_valkey_code") or r.get("has_redis_module_code")):
                signaled.add(key)

    # Return signaled repos first, then the rest
    for repo in all_repos:
        parts = repo["github_url"].rstrip("/").split("/")
        owner, name = parts[-2], parts[-1]
        key = f"{owner}/{name}"
        result.append({"owner": owner, "repo_name": name, "priority": key in signaled})

    result.sort(key=lambda x: not x["priority"])
    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 4 analysis."""
    repos = select_repos(repo_filter)
    log.info("Phase 4: scanning community signals for %d repos", len(repos))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, repo in enumerate(repos):
            owner, name = repo["owner"], repo["repo_name"]
            log.info("[%d/%d] Scanning issues/PRs/discussions for %s/%s", i + 1, len(repos), owner, name)
            result = await analyze_repo(client, owner, name)
            results.append(result)

    ip_count = sum(1 for r in results if r["has_valkey_issues_prs"])
    disc_count = sum(1 for r in results if r["has_valkey_discussions"])
    wiki_count = sum(1 for r in results if r["has_valkey_wiki"])
    log.info("Phase 4 complete: %d with issues/PRs, %d with discussions, %d with wiki mentions",
             ip_count, disc_count, wiki_count)

    output = DATA_DIR / "phase4_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
