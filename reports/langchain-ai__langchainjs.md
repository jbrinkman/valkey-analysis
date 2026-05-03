# Valkey Integration Analysis: langchain-ai/langchainjs

**GitHub:** https://github.com/langchain-ai/langchainjs
**Analyzed:** 2026-05-02T01:40:32.797402+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redisearch, redisgraph, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** extension
- **Redis Modules:** redisearch, redisgraph, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

**Valkey mentions in docs:**
- https://docs.langchain.com/oss/javascript/langchain/overview
- https://docs.langchain.com/oss/javascript/langgraph/overview
- https://docs.langchain.com/oss/javascript/learn

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 3 file(s)
- `redistimeseries` / `ts.add`: 1 file(s)
- `redisgraph` / `graph.query`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #9915](https://github.com/langchain-ai/langchainjs/pull/9915): Valkey vector store provider (open)

## Phase 5: Ecosystem

**Related repos in org (238 total org repos):**
- [langchain-redis](https://github.com/langchain-ai/langchain-redis): None 🔴 Redis
- [langgraph-messaging-integrations](https://github.com/langchain-ai/langgraph-messaging-integrations): Event server integrations with Slack and other messaging platforms.
- [langchain-community](https://github.com/langchain-ai/langchain-community): Community-maintained LangChain integrations
- [langsmith-claude-code-plugins](https://github.com/langchain-ai/langsmith-claude-code-plugins): LangSmith plugins for Claude Code
- [langchainjs-community](https://github.com/langchain-ai/langchainjs-community): Community-maintained LangChainJS integrations

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (69 occurrences)
- `ioredis` (1 occurrences)

**Redis module mentions:** ['redisearch']
