# Valkey Integration Analysis: openai/openai-agents-python

**GitHub:** https://github.com/openai/openai-agents-python
**Analyzed:** 2026-05-02T01:40:32.831289+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 2 related issue(s)/PR(s) found. 3 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** session_store, time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (6 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #3017](https://github.com/openai/openai-agents-python/issues/3017): Add ValkeySession provider for session memory (open)
- [PR #3018](https://github.com/openai/openai-agents-python/pull/3018): feat: #3017 add ValkeySession provider for session memory (open)

## Phase 5: Ecosystem

**Related repos in org (244 total org repos):**
- [scheduler-plugins](https://github.com/openai/scheduler-plugins): Repository for out-of-tree scheduler plugins based on scheduler framework.
- [plugins-quickstart](https://github.com/openai/plugins-quickstart): Get a ChatGPT plugin up and running in under 5 minutes!
- [plugins](https://github.com/openai/plugins): OpenAI Plugins

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (75 occurrences)
