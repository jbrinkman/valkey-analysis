"""Phase 6: Deep dive & evidence synthesis — classify Valkey support and generate reports."""

import asyncio
import json
import logging
import sys
from datetime import datetime, timezone

import httpx

from config import (
    DATA_DIR,
    REPORTS_DIR,
    DEEPWIKI_BASE_URL,
    GITHUB_HEADERS,
    GITHUB_API_BASE,
    CONCURRENT_REQUESTS,
    USE_CASES,
    REDIS_MODULE_KEYWORDS,
    VALKEY_INCOMPATIBLE_MODULES,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

sem = asyncio.Semaphore(CONCURRENT_REQUESTS)


def load_phase_data() -> dict:
    """Load all phase results into a unified lookup keyed by owner/repo."""
    merged = {}

    for phase, filename in [
        ("phase1", "phase1_results.json"),
        ("phase2", "phase2_results.json"),
        ("phase2b", "phase2b_results.json"),
        ("phase3", "phase3_results.json"),
        ("phase4", "phase4_results.json"),
        ("phase5", "phase5_results.json"),
    ]:
        path = DATA_DIR / filename
        if not path.exists():
            log.warning("%s not found, skipping", filename)
            continue
        data = json.loads(path.read_text())
        for entry in data:
            key = f"{entry['owner']}/{entry['repo_name']}"
            if key not in merged:
                merged[key] = {}
            merged[key][phase] = entry

    return merged


def load_repo_metadata() -> dict:
    """Load original repo metadata from repos.json."""
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


async def fetch_deepwiki(client: httpx.AsyncClient, owner: str, repo: str) -> str | None:
    """Fetch DeepWiki summary for a repo."""
    url = f"{DEEPWIKI_BASE_URL}/{owner}/{repo}"
    async with sem:
        try:
            resp = await client.get(url, follow_redirects=True, timeout=20)
            if resp.status_code == 200:
                return resp.text
            return None
        except Exception as e:
            log.debug("DeepWiki fetch error for %s/%s: %s", owner, repo, e)
            return None


def is_negative_valkey_mention(title: str) -> bool:
    """Check if an issue/PR title indicates Valkey is NOT supported."""
    title_lower = title.lower()
    negative_patterns = [
        "not supported", "not compatible", "incompatible", "doesn't work",
        "does not work", "doesn't support", "does not support", "not working",
        "won't work", "will not work", "cannot use", "can't use",
        "unable to", "fails with", "broken with", "issue with",
        "not available", "unsupported", "no support",
    ]
    return any(p in title_lower for p in negative_patterns)


async def collect_valkey_mentions(phases: dict) -> list[dict]:
    """Collect all Valkey mentions across phases with their context for sentiment analysis."""
    mentions = []

    # Phase 2: README mentions
    p2 = phases.get("phase2", {})
    for m in p2.get("valkey_mentions", []):
        for ctx in m.get("contexts", []):
            mentions.append({
                "text": ctx.get("text", ""),
                "context": f"README keyword '{m['keyword']}' match",
                "source": "readme",
            })

    # Phase 2: docs site mentions
    for doc in p2.get("docs_valkey_mentions", []):
        for m in doc.get("matches", []):
            for ctx in m.get("contexts", []):
                mentions.append({
                    "text": ctx.get("text", ""),
                    "context": f"Docs site {doc.get('url', '')} keyword '{m['keyword']}' match",
                    "source": "docs",
                })

    # Phase 2b: DeepWiki mentions
    p2b = phases.get("phase2b", {})
    for m in p2b.get("valkey_mentions", []):
        for ctx in m.get("contexts", []):
            mentions.append({
                "text": ctx.get("text", ""),
                "context": f"DeepWiki keyword '{m['keyword']}' match",
                "source": "deepwiki",
            })

    # Phase 4: issue/PR titles
    p4 = phases.get("phase4", {})
    for ip in p4.get("issues_prs", []):
        mentions.append({
            "text": ip.get("title", ""),
            "context": f"{ip.get('type', 'issue').upper()} #{ip.get('number', '')} ({ip.get('state', '')})",
            "source": "issue_pr",
        })

    # Phase 5: extension repo README mentions
    p5 = phases.get("phase5", {})
    for ext in p5.get("related_repos", []):
        if ext.get("valkey_mentioned"):
            mentions.append({
                "text": ext.get("details", f"Extension repo {ext.get('repo_name', '')} mentions Valkey"),
                "context": f"Extension repo {ext.get('url', '')}",
                "source": "extension",
            })

    return mentions


async def analyze_valkey_sentiment(client: httpx.AsyncClient, phases: dict) -> dict:
    """Run sentiment analysis on all Valkey mentions. Returns summary."""
    from sentiment import classify_mention

    mentions = await collect_valkey_mentions(phases)
    if not mentions:
        return {"positive": [], "negative": [], "neutral": [], "total": 0}

    results = {"positive": [], "negative": [], "neutral": [], "total": len(mentions)}

    for mention in mentions:
        sentiment = await classify_mention(client, mention["text"], mention["context"])
        entry = {**mention, "sentiment": sentiment["sentiment"], "reason": sentiment["reason"]}
        bucket = sentiment["sentiment"].lower()
        if bucket in results:
            results[bucket].append(entry)
        else:
            results["neutral"].append(entry)

    return results


def classify_valkey_support(phases: dict, sentiment_results: dict | None = None) -> str:
    """Classify valkey_support as explicit, implied, or none.

    Uses LLM sentiment analysis results when available to determine
    whether Valkey mentions are actually positive signals.
    """
    p1 = phases.get("phase1", {})
    p3 = phases.get("phase3", {})
    p5 = phases.get("phase5", {})

    # Check for incompatible modules upfront
    modules_used = detect_redis_modules(phases)
    incompatible = [m for m in modules_used if m in VALKEY_INCOMPATIBLE_MODULES]

    # Hard explicit: Valkey dependency in package manifest
    if p1.get("valkey_deps"):
        return "explicit"

    # Soft signals below — incompatible modules disqualify
    if incompatible:
        return "none"

    # Code references: require multiple files
    if p3.get("has_valkey_code") and p3.get("valkey_total_files", 0) >= 3:
        return "explicit"

    # LLM sentiment-based classification
    if sentiment_results and sentiment_results.get("positive"):
        # Only count as explicit if there are genuinely positive mentions
        positive_sources = {m["source"] for m in sentiment_results["positive"]}
        # Strong positive: code-adjacent sources (readme, docs, extension)
        if positive_sources & {"readme", "docs", "extension"}:
            return "explicit"

    # Implied: Redis dependency with compatible use case
    p2 = phases.get("phase2", {})
    p2b = phases.get("phase2b", {})
    has_strong_redis_signal = p1.get("redis_deps") or p2.get("has_redis_signal") or p5.get("has_redis_extension")
    has_deepwiki_redis = p2b.get("has_redis_signal")
    if has_strong_redis_signal or (has_deepwiki_redis and (p1.get("redis_deps") or p2.get("has_redis_signal"))):
        return "implied"

    return "none"


def classify_valkey_search_support(phases: dict) -> str:
    """Classify valkey_search_support. Conservative — RediSearch alone is NOT enough."""
    p2 = phases.get("phase2", {})
    p3 = phases.get("phase3", {})

    # Explicit: direct valkey-search mentions in code or docs
    valkey_mentions = p2.get("valkey_mentions", [])
    for m in valkey_mentions:
        if "valkey-search" in m.get("keyword", "").lower():
            return "explicit"

    if p3.get("has_valkey_code"):
        for hit in p3.get("valkey_code_hits", []):
            if "valkey-search" in hit.get("keyword", "").lower():
                return "explicit"

    # NOT implied from RediSearch alone — per project requirements
    return "none"


def detect_valkey_glide(phases: dict) -> bool:
    """Check if Valkey-Glide is used."""
    p1 = phases.get("phase1", {})
    p2 = phases.get("phase2", {})
    p3 = phases.get("phase3", {})

    if p1.get("valkey_glide_found"):
        return True
    if p2.get("valkey_glide_mentions"):
        return True
    if p3.get("has_valkey_glide_code"):
        return True
    return False


def detect_redisearch_usage(phases: dict) -> bool:
    """Check if RediSearch is used."""
    p2 = phases.get("phase2", {})
    p2b = phases.get("phase2b", {})
    p3 = phases.get("phase3", {})

    modules = p2.get("redis_module_mentions", {})
    if "redisearch" in modules:
        return True
    if "redisearch" in p2b.get("redis_module_mentions", {}):
        return True
    if p3.get("redis_module_code_hits", {}).get("redisearch"):
        return True
    return False


def detect_redis_modules(phases: dict) -> list[str]:
    """Detect which Redis modules are used."""
    modules_found = set()
    p2 = phases.get("phase2", {})
    p2b = phases.get("phase2b", {})
    p3 = phases.get("phase3", {})

    for module in REDIS_MODULE_KEYWORDS:
        if module in p2.get("redis_module_mentions", {}):
            modules_found.add(module)
        if module in p2b.get("redis_module_mentions", {}):
            modules_found.add(module)
        if module in p3.get("redis_module_code_hits", {}):
            modules_found.add(module)

    return sorted(modules_found)


def collect_client_libraries(phases: dict) -> list[str]:
    """Collect all detected client libraries."""
    libs = set()
    p1 = phases.get("phase1", {})
    for dep in p1.get("valkey_deps", []):
        libs.add(dep["name"])
    for dep in p1.get("redis_deps", []):
        libs.add(dep["name"])
    return sorted(libs)


def infer_use_cases(phases: dict) -> list[str]:
    """Infer use cases from evidence."""
    cases = set()
    p2 = phases.get("phase2", {})
    p3 = phases.get("phase3", {})

    # Check README and docs for use case keywords
    all_text = ""
    for mention in p2.get("valkey_mentions", []) + p2.get("redis_mentions", []):
        for ctx in mention.get("contexts", []):
            all_text += " " + ctx.get("text", "").lower()

    use_case_signals = {
        "vector_store": ["vector", "embedding", "similarity", "semantic search", "vectorstore", "vector_store"],
        "cache": ["cache", "caching", "llm cache", "prompt cache", "semantic cache"],
        "memory": ["memory", "conversation history", "chat history", "long-term memory", "agent memory"],
        "message_broker": ["pubsub", "pub/sub", "message queue", "task queue", "celery", "stream"],
        "session_store": ["session", "session store"],
        "rate_limiting": ["rate limit", "throttl"],
        "general_datastore": ["key-value", "key value", "data store", "datastore"],
        "time_series": ["time series", "timeseries", "ts.add"],
    }

    for use_case, signals in use_case_signals.items():
        for signal in signals:
            if signal in all_text:
                cases.add(use_case)
                break

    # Redis modules imply use cases
    modules = detect_redis_modules(phases)
    if "redisearch" in modules:
        cases.add("vector_store")
    if "redistimeseries" in modules:
        cases.add("time_series")

    return sorted(cases)


def infer_integration_type(phases: dict) -> str:
    """Infer how the integration works."""
    p1 = phases.get("phase1", {})
    p5 = phases.get("phase5", {})

    if p5.get("has_valkey_extension") or p5.get("has_redis_extension"):
        if p5.get("related_repos"):
            return "extension"

    if p1.get("valkey_deps") or p1.get("redis_deps"):
        return "native"

    return "none"


def build_evidence(phases: dict, sentiment_results: dict | None = None) -> dict:
    """Build the evidence object from all phase data."""
    p1 = phases.get("phase1", {})
    p2 = phases.get("phase2", {})
    p3 = phases.get("phase3", {})
    p4 = phases.get("phase4", {})
    p5 = phases.get("phase5", {})

    deps = [d["name"] for d in p1.get("valkey_deps", [])] + [d["name"] for d in p1.get("redis_deps", [])]

    code_refs = p3.get("valkey_total_files", 0) + p3.get("redis_module_total_files", 0)

    doc_mentions = p2.get("has_valkey_signal", False) or p2.get("has_redis_signal", False)
    readme_mentions = bool(p2.get("valkey_mentions") or p2.get("redis_mentions"))

    # Tag issues/PRs with LLM sentiment if available, else use source-based heuristic
    issue_sentiments = {}
    if sentiment_results:
        for bucket in ("positive", "negative", "neutral"):
            for m in sentiment_results.get(bucket, []):
                if m.get("source") == "issue_pr":
                    # Match by title text
                    issue_sentiments[m["text"]] = {
                        "sentiment": bucket,
                        "reason": m.get("reason", ""),
                    }

    issues_prs = []
    for ip in p4.get("issues_prs", []):
        tagged = dict(ip)
        title = ip.get("title", "")
        if title in issue_sentiments:
            tagged["sentiment"] = issue_sentiments[title]["sentiment"]
            tagged["sentiment_reason"] = issue_sentiments[title]["reason"]
        else:
            tagged["sentiment"] = "neutral"
            tagged["sentiment_reason"] = "No LLM analysis available"
        issues_prs.append(tagged)

    discussions = p4.get("discussions", [])
    wiki_mentions = p4.get("has_valkey_wiki", False)

    community_extensions = []
    for ext in p5.get("related_repos", []):
        ext_entry = {
            "repo_url": ext.get("url", ""),
            "description": ext.get("description", ""),
            "valkey_mentioned": ext.get("valkey_mentioned", False),
            "redis_mentioned": ext.get("redis_mentioned", False),
        }
        # Add LLM sentiment for extension mentions
        if sentiment_results and ext.get("valkey_mentioned"):
            ext_url = ext.get("url", "")
            for m in sentiment_results.get("positive", []) + sentiment_results.get("negative", []) + sentiment_results.get("neutral", []):
                if m.get("source") == "extension" and ext_url in m.get("context", ""):
                    ext_entry["sentiment"] = m["sentiment"]
                    ext_entry["sentiment_reason"] = m.get("reason", "")
                    break
        community_extensions.append(ext_entry)

    # Include full sentiment summary
    sentiment_summary = None
    if sentiment_results:
        sentiment_summary = {
            "total": sentiment_results["total"],
            "positive": len(sentiment_results["positive"]),
            "negative": len(sentiment_results["negative"]),
            "neutral": len(sentiment_results["neutral"]),
            "details": [
                {**m, "text": m["text"][:200]} for bucket in ("positive", "negative", "neutral")
                for m in sentiment_results.get(bucket, [])
            ],
        }

    return {
        "dependencies": deps,
        "code_references": code_refs,
        "doc_mentions": doc_mentions,
        "readme_mentions": readme_mentions,
        "issues_prs": issues_prs,
        "discussions": discussions,
        "wiki_mentions": wiki_mentions,
        "community_extensions": community_extensions,
        "sentiment_analysis": sentiment_summary,
    }


def build_evidence_summary(valkey_support: str, valkey_search_support: str,
                           valkey_glide: bool, evidence: dict, phases: dict,
                           sentiment_results: dict | None = None) -> str:
    """Build a human-readable evidence summary."""
    parts = []

    if valkey_support == "explicit":
        parts.append("Explicit Valkey support detected.")
        if evidence["dependencies"]:
            valkey_deps = [d["name"] for d in phases.get("phase1", {}).get("valkey_deps", [])]
            if valkey_deps:
                parts.append(f"Valkey dependencies: {', '.join(valkey_deps)}.")
    elif valkey_support == "implied":
        parts.append("Implied Valkey compatibility via Redis integration.")
        redis_deps = [d["name"] for d in phases.get("phase1", {}).get("redis_deps", [])]
        if redis_deps:
            parts.append(f"Redis dependencies: {', '.join(redis_deps)}.")
    else:
        # Check if this is a "none" due to incompatible modules
        modules = detect_redis_modules(phases)
        incompatible = [m for m in modules if m in VALKEY_INCOMPATIBLE_MODULES]
        p1 = phases.get("phase1", {})
        has_redis = p1.get("redis_deps") or phases.get("phase2", {}).get("has_redis_signal")
        if has_redis and incompatible:
            parts.append(f"Redis integration detected but uses Valkey-incompatible module(s): {', '.join(incompatible)}.")
            redis_deps = [d["name"] for d in p1.get("redis_deps", [])]
            if redis_deps:
                parts.append(f"Redis dependencies: {', '.join(redis_deps)}.")
        else:
            parts.append("No Valkey or Redis integration detected.")

    if valkey_glide:
        parts.append("Valkey-Glide client library detected.")

    if valkey_search_support == "explicit":
        parts.append("Explicit Valkey-Search support detected.")

    if evidence["issues_prs"]:
        total = len(evidence["issues_prs"])
        negative = sum(1 for ip in evidence["issues_prs"] if ip.get("sentiment") == "negative")
        neutral = sum(1 for ip in evidence["issues_prs"] if ip.get("sentiment") == "neutral")
        positive = sum(1 for ip in evidence["issues_prs"] if ip.get("sentiment") == "positive")
        qualifiers = []
        if positive:
            qualifiers.append(f"{positive} positive")
        if negative:
            qualifiers.append(f"{negative} negative")
        if neutral:
            qualifiers.append(f"{neutral} neutral")
        parts.append(f"{total} related issue(s)/PR(s) found ({', '.join(qualifiers)}).")

    if evidence["discussions"]:
        count = len(evidence["discussions"])
        parts.append(f"{count} related discussion(s) found.")

    if evidence["community_extensions"]:
        count = len(evidence["community_extensions"])
        valkey_exts = sum(1 for e in evidence["community_extensions"] if e["valkey_mentioned"])
        parts.append(f"{count} related extension repo(s) found ({valkey_exts} mention Valkey).")

    modules = detect_redis_modules(phases)
    if modules:
        parts.append(f"Redis modules used: {', '.join(modules)}.")

    return " ".join(parts)


def generate_markdown_report(repo_key: str, result: dict, phases: dict, deepwiki_available: bool) -> str:
    """Generate a detailed markdown evidence report for a single repo."""
    owner, repo_name = repo_key.split("/")
    lines = [
        f"# Valkey Integration Analysis: {owner}/{repo_name}",
        "",
        f"**GitHub:** https://github.com/{owner}/{repo_name}",
        f"**Analyzed:** {result['analyzed_at']}",
        "",
        "## Classification",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Valkey Support | **{result['valkey_support']}** |",
        f"| Valkey-Search Support | **{result['valkey_search_support']}** |",
        f"| Valkey-Glide Used | {result['valkey_glide_used']} |",
        f"| RediSearch Usage | {result['redisearch_usage']} |",
        "",
        "## Summary",
        "",
        result["evidence_summary"],
        "",
        "## Integration Details",
        "",
        f"- **Client Libraries:** {', '.join(result['integration_details']['client_libraries']) or 'None detected'}",
        f"- **Use Cases:** {', '.join(result['integration_details']['use_cases']) or 'None detected'}",
        f"- **Integration Type:** {result['integration_details']['integration_type']}",
        f"- **Redis Modules:** {', '.join(result['integration_details']['redis_modules_used']) or 'None detected'}",
        "",
    ]

    # Phase 1: Dependencies
    p1 = phases.get("phase1", {})
    lines.extend([
        "## Phase 1: Dependency Scan",
        "",
        f"Manifests checked: {', '.join(p1.get('manifests_checked', [])) or 'None found'}",
        "",
    ])
    if p1.get("valkey_deps"):
        lines.append("**Valkey dependencies:**")
        for dep in p1["valkey_deps"]:
            lines.append(f"- `{dep['name']}` ({dep['category']})")
        lines.append("")
    if p1.get("redis_deps"):
        lines.append("**Redis dependencies:**")
        for dep in p1["redis_deps"]:
            lines.append(f"- `{dep['name']}` ({dep['category']})")
        lines.append("")

    # Phase 2: Documentation
    p2 = phases.get("phase2", {})
    lines.extend(["## Phase 2: Documentation Scan", ""])
    if p2.get("valkey_mentions"):
        lines.append("**Valkey mentions in README:**")
        for m in p2["valkey_mentions"]:
            lines.append(f"- `{m['keyword']}` ({m['count']} occurrences)")
            for ctx in m.get("contexts", []):
                lines.append(f"  - Line {ctx['line']}: `{ctx['text']}`")
        lines.append("")
    if p2.get("redis_mentions"):
        lines.append("**Redis mentions in README:**")
        for m in p2["redis_mentions"][:5]:  # limit output
            lines.append(f"- `{m['keyword']}` ({m['count']} occurrences)")
        lines.append("")
    if p2.get("docs_valkey_mentions"):
        lines.append("**Valkey mentions in docs:**")
        for doc in p2["docs_valkey_mentions"]:
            lines.append(f"- {doc['url']}")
        lines.append("")

    # Phase 3: Code Search
    p3 = phases.get("phase3", {})
    lines.extend(["## Phase 3: Code Search", ""])
    if p3.get("valkey_code_hits"):
        lines.append("**Valkey code references:**")
        for hit in p3["valkey_code_hits"]:
            lines.append(f"- `{hit['keyword']}`: {hit['total_count']} file(s)")
            for f in hit.get("files", [])[:3]:
                lines.append(f"  - [{f['file']}]({f['url']})")
        lines.append("")
    if p3.get("valkey_glide_code_hits"):
        lines.append("**Valkey-Glide code references:**")
        for hit in p3["valkey_glide_code_hits"]:
            lines.append(f"- `{hit['keyword']}`: {hit['total_count']} file(s)")
        lines.append("")
    if p3.get("redis_module_code_hits"):
        lines.append("**Redis module code references:**")
        for module, hits in p3["redis_module_code_hits"].items():
            for hit in hits:
                lines.append(f"- `{module}` / `{hit['keyword']}`: {hit['total_count']} file(s)")
        lines.append("")

    # Phase 4: Community Signals
    p4 = phases.get("phase4", {})
    lines.extend(["## Phase 4: Community Signals", ""])
    if result.get("evidence", {}).get("issues_prs"):
        lines.append("**Issues/PRs:**")
        sentiment_icons = {"negative": "⛔", "neutral": "➖", "positive": "✅"}
        for ip in result["evidence"]["issues_prs"]:
            icon = sentiment_icons.get(ip.get("sentiment", ""), "➖")
            reason = f" — _{ip['sentiment_reason']}_" if ip.get("sentiment_reason") else ""
            lines.append(f"- {icon} [{ip['type'].upper()} #{ip['number']}]({ip['url']}): {ip['title']} ({ip['state']}){reason}")
        lines.append("")
    if p4.get("discussions"):
        lines.append("**Discussions:**")
        for d in p4["discussions"]:
            lines.append(f"- [Discussion #{d['number']}]({d['url']}): {d['title']}")
        lines.append("")
    if p4.get("wiki", {}).get("valkey_mentions"):
        lines.append("**Wiki mentions:**")
        for w in p4["wiki"]["valkey_mentions"]:
            lines.append(f"- Page: {w['page_title']} (keyword: {w['keyword']})")
        lines.append("")

    # Phase 5: Ecosystem
    p5 = phases.get("phase5", {})
    lines.extend(["## Phase 5: Ecosystem", ""])
    if p5.get("related_repos"):
        lines.append(f"**Related repos in org ({p5.get('org_repos_checked', 0)} total org repos):**")
        for ext in p5["related_repos"]:
            valkey_flag = " ✅ Valkey" if ext.get("valkey_mentioned") else ""
            redis_flag = " 🔴 Redis" if ext.get("redis_mentioned") else ""
            lines.append(f"- [{ext['repo_name']}]({ext['url']}): {ext.get('description', '')}{valkey_flag}{redis_flag}")
        lines.append("")
    else:
        lines.append("No related extension repos found in the org.")
        lines.append("")

    # Sentiment Analysis
    sa = result.get("evidence", {}).get("sentiment_analysis")
    if sa and sa["total"] > 0:
        lines.extend([
            "## Sentiment Analysis",
            "",
            f"**{sa['total']} Valkey mention(s) analyzed:** {sa['positive']} positive, {sa['negative']} negative, {sa['neutral']} neutral",
            "",
        ])
        sentiment_icons = {"positive": "✅", "negative": "⛔", "neutral": "➖"}
        for detail in sa.get("details", []):
            icon = sentiment_icons.get(detail.get("sentiment", ""), "")
            source = detail.get("source", "")
            reason = detail.get("reason", "")
            text = detail.get("text", "")[:150]
            lines.append(f"- {icon} **[{source}]** \"{text}\"")
            if reason:
                lines.append(f"    - Reason: {reason}")
        lines.append("")

    # DeepWiki
    p2b = phases.get("phase2b", {})
    if p2b.get("deepwiki_available"):
        lines.extend([
            "## DeepWiki Analysis",
            "",
        ])
        if p2b.get("valkey_mentions"):
            lines.append("**Valkey mentions:**")
            for m in p2b["valkey_mentions"]:
                lines.append(f"- `{m['keyword']}` ({m['count']} occurrences)")
                for ctx in m.get("contexts", []):
                    lines.append(f"  - `{ctx['text']}`")
            lines.append("")
        if p2b.get("redis_mentions"):
            lines.append(f"**Redis mentions:** {len(p2b['redis_mentions'])} keyword(s) found")
            for m in p2b["redis_mentions"][:5]:
                lines.append(f"- `{m['keyword']}` ({m['count']} occurrences)")
            lines.append("")
        if p2b.get("redis_module_mentions"):
            lines.append(f"**Redis module mentions:** {list(p2b['redis_module_mentions'].keys())}")
            lines.append("")
        if not p2b.get("valkey_mentions") and not p2b.get("redis_mentions"):
            lines.append("No Valkey or Redis mentions found in DeepWiki content.")
            lines.append("")
    else:
        lines.extend(["## DeepWiki Analysis", "", "DeepWiki content not available for this repo.", ""])

    return "\n".join(lines)


async def synthesize_repo(client: httpx.AsyncClient, repo_key: str, phases: dict, metadata: dict) -> dict:
    """Synthesize all phase data for a single repo into a final result."""
    owner, repo_name = repo_key.split("/")
    meta = metadata.get(repo_key, {})

    # DeepWiki data is now collected in Phase 2b — check if it was available
    deepwiki_available = phases.get("phase2b", {}).get("deepwiki_available", False)

    # Run LLM sentiment analysis on all Valkey mentions
    sentiment_results = await analyze_valkey_sentiment(client, phases)

    # Classify using sentiment results
    valkey_support = classify_valkey_support(phases, sentiment_results)
    valkey_search_support = classify_valkey_search_support(phases)
    valkey_glide = detect_valkey_glide(phases)
    redisearch = detect_redisearch_usage(phases)

    # Build result
    evidence = build_evidence(phases, sentiment_results)
    evidence_summary = build_evidence_summary(valkey_support, valkey_search_support, valkey_glide, evidence, phases, sentiment_results)

    report_filename = f"{owner}__{repo_name}.md"

    result = {
        "repo_name": repo_name,
        "owner": owner,
        "github_url": f"https://github.com/{owner}/{repo_name}",
        "description": meta.get("description", ""),
        "language": meta.get("language", ""),
        "stars": int(meta.get("stars", 0)),
        "valkey_support": valkey_support,
        "valkey_search_support": valkey_search_support,
        "valkey_glide_used": valkey_glide,
        "redisearch_usage": redisearch,
        "integration_details": {
            "client_libraries": collect_client_libraries(phases),
            "use_cases": infer_use_cases(phases),
            "integration_type": infer_integration_type(phases),
            "redis_modules_used": detect_redis_modules(phases),
        },
        "evidence": evidence,
        "evidence_summary": evidence_summary,
        "detail_report": f"reports/{report_filename}",
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
    }

    # Generate markdown report
    report = generate_markdown_report(repo_key, result, phases, deepwiki_available)
    (REPORTS_DIR / report_filename).write_text(report)

    return result


async def main(repo_filter: list[str] | None = None):
    """Run Phase 6 synthesis."""
    phase_data = load_phase_data()
    metadata = load_repo_metadata()

    if not phase_data:
        log.error("No phase data found — run phases 1-5 first")
        sys.exit(1)

    if repo_filter:
        keys = [k for k in phase_data if k in repo_filter]
    else:
        # Include all repos from metadata, even those without phase data
        keys = set(phase_data.keys())
        for k in metadata:
            keys.add(k)
        keys = sorted(keys)

    log.info("Phase 6: synthesizing %d repos", len(keys))

    results = []
    async with httpx.AsyncClient(timeout=30) as client:
        for i, key in enumerate(keys):
            log.info("[%d/%d] Synthesizing %s", i + 1, len(keys), key)
            phases = phase_data.get(key, {})
            result = await synthesize_repo(client, key, phases, metadata)
            results.append(result)

    # Summary
    explicit = sum(1 for r in results if r["valkey_support"] == "explicit")
    implied = sum(1 for r in results if r["valkey_support"] == "implied")
    none_count = sum(1 for r in results if r["valkey_support"] == "none")
    glide = sum(1 for r in results if r["valkey_glide_used"])
    log.info("Phase 6 complete: %d explicit, %d implied, %d none, %d glide", explicit, implied, none_count, glide)

    output = DATA_DIR / "phase6_results.json"
    output.write_text(json.dumps(results, indent=2))
    log.info("Results written to %s", output)
    return results


if __name__ == "__main__":
    repo_filter = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(repo_filter))
