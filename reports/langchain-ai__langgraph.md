# Valkey Integration Analysis: langchain-ai/langgraph

**GitHub:** https://github.com/langchain-ai/langgraph
**Analyzed:** 2026-05-02T01:40:32.797637+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

**Valkey mentions in docs:**
- https://docs.langchain.com/oss/python/learn
- https://docs.langchain.com/langsmith/home
- https://docs.langchain.com/oss/python/langchain/overview

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #6987](https://github.com/langchain-ai/langgraph/issues/6987): LangGraph API 0.7.60: Redis TLS cluster PubSub fails with port 0 (go-redis v9.18.0 regression) (open)

## Phase 5: Ecosystem

**Related repos in org (238 total org repos):**
- [langchain-redis](https://github.com/langchain-ai/langchain-redis): None 🔴 Redis
- [langgraph-messaging-integrations](https://github.com/langchain-ai/langgraph-messaging-integrations): Event server integrations with Slack and other messaging platforms.
- [langchain-community](https://github.com/langchain-ai/langchain-community): Community-maintained LangChain integrations
- [langsmith-claude-code-plugins](https://github.com/langchain-ai/langsmith-claude-code-plugins): LangSmith plugins for Claude Code
- [langchainjs-community](https://github.com/langchain-ai/langchainjs-community): Community-maintained LangChainJS integrations

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (56 occurrences)
