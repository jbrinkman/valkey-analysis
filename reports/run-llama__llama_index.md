# Valkey Integration Analysis: run-llama/llama_index

**GitHub:** https://github.com/run-llama/llama_index
**Analyzed:** 2026-05-02T01:40:32.846486+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 2 related issue(s)/PR(s) found. Redis modules used: redisgraph, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisgraph, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 6 file(s)
- `redisgraph` / `graph.query`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #20785](https://github.com/run-llama/llama_index/issues/20785): [Feature Request]: Add Valkey Vector Store support (open)
- [PR #20889](https://github.com/run-llama/llama_index/pull/20889): Feature/valkey vector store (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (11 occurrences)
