"""Phase 5: Check org repos for community extensions, plugins, and integrations."""

import asyncio
import base64
import json
import logging
import sys

import httpx

from config import (
    DATA_DIR,
    ECOSYSTEM_REPO_KEYWORDS,
    VALKEY_EXPLICIT_KEYWORDS,
    CONCURRENT_REQUESTS,
)
from github_client import github_get, log_rate_status

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


async def list_org_repos(client: httpx.AsyncClient, owner: str) -> list[dict]:
    """List all public repos for an org/user, paginated."""
    all_repos = []
    for endpoint in [f"https://api.github.com/orgs/{owner}/repos", f"https://api.github.com/users/{owner}/repos"]:
        page = 1
        while page <= 5:
            data = await github_get(client, endpoint, {"per_page": 100, "page": page})
            if data is None:
                break
            if not isinstance(data, list) or len(data) == 0:
                break
            all_repos.extend(data)
            if len(data) < 100:
                break
            page += 1
        if all_repos:
            break
    return all_repos


def is_relevant_repo(repo: dict, source_repo_name: str) -> bool:
    """Check if an org repo name suggests it's an integration/extension repo."""
    name = repo.get("name", "").lower()
    desc = (repo.get("description") or "").lower()
    topics = repo.get("topics", [])

    # Skip the source repo itself
    if name == source_repo_name.lower():
        return False

    # Check name for ecosystem keywords
    for kw in ECOSYSTEM_REPO_KEYWORDS:
        if kw in name:
            return True

    # Check if repo name contains the source project name (e.g., langchain-redis)
    source_lower = source_repo_name.lower().replace("-", "").replace("_", "")
    name_clean = name.replace("-", "").replace("_", "")
    if source_lower in name_clean and any(kw in name for kw in ["redis", "valkey", "cache", "vector", "store"]):
        return True

    # Check description
    for kw in VALKEY_EXPLICIT_KEYWORDS:
        if kw in desc:
            return True
    if "redis" in desc and source_repo_name.lower() in desc:
        return True

    # Check topics
    topic_str = " ".join(topics).lower()
    if "valkey" in topic_str or ("redis" in topic_str and "integration" in topic_str):
        return True

    return False


async def quick_scan_repo(client: httpx.AsyncClient, owner: str, repo_name: str) -> dict:
    """Quick scan of a related repo's README for Valkey mentions."""
    result = {
        "repo_name": repo_name,
        "url": f"https://github.com/{owner}/{repo_name}",
        "valkey_mentioned": False,
        "redis_mentioned": False,
        "details": "",
    }

    url = f"https://api.github.com/repos/{owner}/{repo_name}/readme"
    data = await github_get(client, url)
    if not data or not data.get("content"):
        return result

    try:
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace").lower()
    except Exception:
        return result

    for kw in VALKEY_EXPLICIT_KEYWORDS:
        if kw.lower() in content:
            result["valkey_mentioned"] = True
            result["details"] += f"README mentions '{kw}'. "
            break

    if "redis" in content:
        result["redis_mentioned"] = True

    return result


async def analyze_repo(client: httpx.AsyncClient, owner: str, repo_name: str) -> dict:
    """Find and analyze related repos in the same org."""
    result = {
        "owner": owner,
        "repo_name": repo_name,
        "github_url": f"https://github.com/{owner}/{repo_name}",
        "org_repos_checked": 0,
        "related_repos": [],
        "has_valkey_extension": False,
        "has_redis_extension": False,
    }

    # List all repos in the org
    org_repos = await list_org_repos(client, owner)
    result["org_repos_checked"] = len(org_repos)

    # Filter for relevant repos
    relevant = [r for r in org_repos if is_relevant_repo(r, repo_name)]

    # Quick scan each relevant repo
    for repo in relevant[:10]:  # cap at 10 related repos
        scan = await quick_scan_repo(client, owner, repo["name"])
        scan["description"] = repo.get("description", "")
        scan["stars"] = repo.get("stargazers_count", 0)
        result["related_repos"].append(scan)

        if scan["valkey_mentioned"]:
            result["has_valkey_extension"] = True
        if scan["redis_mentioned"]:
            result["has_redis_extension"] = True

    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 5 analysis."""
    repos_file = DATA_DIR / "repos.json"
    if not repos_file.exists():
        log.error("repos.json not found — run Phase 1 first")
        sys.exit(1)

    all_repos = json.loads(repos_file.read_text())["repos"]

    if repo_filter:
        repos = [{"owner": r.split("/")[0], "repo_name": r.split("/")[1]}
                 for r in repo_filter]
    else:
        repos = []
        for r in all_repos:
            parts = r["github_url"].rstrip("/").split("/")
            repos.append({"owner": parts[-2], "repo_name": parts[-1]})

    # Deduplicate by org — only need to list org repos once per org
    seen_orgs = {}
    for repo in repos:
        org = repo["owner"]
        if org not in seen_orgs:
            seen_orgs[org] = []
        seen_orgs[org].append(repo["repo_name"])

    log.info("Phase 5: checking ecosystem repos for %d orgs (%d repos)", len(seen_orgs), len(repos))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        i = 0
        for org, repo_names in seen_orgs.items():
            # Fetch org repos once
            org_repos = await list_org_repos(client, org)

            for repo_name in repo_names:
                i += 1
                log.info("[%d/%d] Checking ecosystem for %s/%s", i, len(repos), org, repo_name)

                result = {
                    "owner": org,
                    "repo_name": repo_name,
                    "github_url": f"https://github.com/{org}/{repo_name}",
                    "org_repos_checked": len(org_repos),
                    "related_repos": [],
                    "has_valkey_extension": False,
                    "has_redis_extension": False,
                }

                relevant = [r for r in org_repos if is_relevant_repo(r, repo_name)]

                for repo in relevant[:10]:
                    scan = await quick_scan_repo(client, org, repo["name"])
                    scan["description"] = repo.get("description", "")
                    scan["stars"] = repo.get("stargazers_count", 0)
                    result["related_repos"].append(scan)

                    if scan["valkey_mentioned"]:
                        result["has_valkey_extension"] = True
                    if scan["redis_mentioned"]:
                        result["has_redis_extension"] = True

                results.append(result)

    valkey_ext = sum(1 for r in results if r["has_valkey_extension"])
    redis_ext = sum(1 for r in results if r["has_redis_extension"])
    log.info("Phase 5 complete: %d with valkey extensions, %d with redis extensions", valkey_ext, redis_ext)

    output = DATA_DIR / "phase5_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
