"""Phase 7: Assemble final results.json from Phase 6 synthesis output."""

import json
import logging
import sys
from datetime import datetime, timezone

from config import DATA_DIR, RESULTS_DIR, REPORTS_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def load_repo_metadata() -> dict:
    """Load original repo metadata keyed by owner/repo."""
    path = DATA_DIR / "repos.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    meta = {}
    for r in data["repos"]:
        parts = r["github_url"].rstrip("/").split("/")
        key = f"{parts[-2]}/{parts[-1]}"
        meta[key] = r
    return meta


def main():
    """Assemble final results."""
    p6_file = DATA_DIR / "phase6_results.json"
    if not p6_file.exists():
        log.error("phase6_results.json not found — run Phase 6 first")
        sys.exit(1)

    repos = json.loads(p6_file.read_text())
    metadata = load_repo_metadata()
    log.info("Assembling results for %d repos", len(repos))

    # Ensure all repos from the master list are represented
    covered = {f"{r['owner']}/{r['repo_name']}" for r in repos}
    for key, meta in metadata.items():
        if key in covered:
            continue
        owner, repo_name = key.split("/")
        repos.append({
            "repo_name": repo_name,
            "owner": owner,
            "github_url": f"https://github.com/{key}",
            "description": meta.get("description", ""),
            "language": meta.get("language", ""),
            "stars": int(meta.get("stars", 0)),
            "valkey_support": "none",
            "valkey_search_support": "none",
            "valkey_glide_used": False,
            "redisearch_usage": False,
            "integration_details": {
                "client_libraries": [],
                "use_cases": [],
                "integration_type": "none",
                "redis_modules_used": [],
            },
            "evidence": {
                "dependencies": [],
                "code_references": 0,
                "doc_mentions": False,
                "readme_mentions": False,
                "issues_prs": [],
                "discussions": [],
                "wiki_mentions": False,
                "community_extensions": [],
            },
            "evidence_summary": "No Valkey or Redis integration detected.",
            "detail_report": f"reports/{owner}__{repo_name}.md",
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
        })

    # Sort by valkey_support (explicit first), then stars descending
    support_order = {"explicit": 0, "implied": 1, "none": 2}
    repos.sort(key=lambda r: (support_order.get(r["valkey_support"], 3), -r.get("stars", 0)))

    # Build summary stats
    stats = {
        "total_repos": len(repos),
        "valkey_support": {
            "explicit": sum(1 for r in repos if r["valkey_support"] == "explicit"),
            "implied": sum(1 for r in repos if r["valkey_support"] == "implied"),
            "none": sum(1 for r in repos if r["valkey_support"] == "none"),
        },
        "valkey_search_support": {
            "explicit": sum(1 for r in repos if r["valkey_search_support"] == "explicit"),
            "implied": sum(1 for r in repos if r["valkey_search_support"] == "implied"),
            "none": sum(1 for r in repos if r["valkey_search_support"] == "none"),
        },
        "valkey_glide_used": sum(1 for r in repos if r["valkey_glide_used"]),
        "redisearch_usage": sum(1 for r in repos if r["redisearch_usage"]),
        "reports_generated": sum(1 for r in repos if (REPORTS_DIR / f"{r['owner']}__{r['repo_name']}.md").exists()),
    }

    # Strip heavy evidence detail from the main JSON to keep it dashboard-friendly
    # Full evidence is in the per-repo markdown reports
    dashboard_repos = []
    for r in repos:
        dr = dict(r)
        # Slim down issues_prs and discussions to counts + top items
        evidence = dict(dr["evidence"])
        if len(evidence.get("issues_prs", [])) > 5:
            evidence["issues_prs_total"] = len(evidence["issues_prs"])
            evidence["issues_prs"] = evidence["issues_prs"][:5]
        if len(evidence.get("discussions", [])) > 5:
            evidence["discussions_total"] = len(evidence["discussions"])
            evidence["discussions"] = evidence["discussions"][:5]
        if len(evidence.get("community_extensions", [])) > 5:
            evidence["community_extensions_total"] = len(evidence["community_extensions"])
            evidence["community_extensions"] = evidence["community_extensions"][:5]
        dr["evidence"] = evidence
        dashboard_repos.append(dr)

    output = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_repos": len(repos),
            "analysis_version": "1.0",
        },
        "summary": stats,
        "repos": dashboard_repos,
    }

    output_path = RESULTS_DIR / "results.json"
    output_path.write_text(json.dumps(output, indent=2))
    log.info("Final results written to %s", output_path)

    # Print summary
    log.info("=== Summary ===")
    log.info("Total repos: %d", stats["total_repos"])
    log.info("Valkey support — explicit: %d, implied: %d, none: %d",
             stats["valkey_support"]["explicit"],
             stats["valkey_support"]["implied"],
             stats["valkey_support"]["none"])
    log.info("Valkey-Search support — explicit: %d, implied: %d, none: %d",
             stats["valkey_search_support"]["explicit"],
             stats["valkey_search_support"]["implied"],
             stats["valkey_search_support"]["none"])
    log.info("Valkey-Glide used: %d", stats["valkey_glide_used"])
    log.info("RediSearch usage: %d", stats["redisearch_usage"])
    log.info("Reports generated: %d", stats["reports_generated"])


if __name__ == "__main__":
    main()
