# Valkey Integration Analysis: FlowiseAI/Flowise

**GitHub:** https://github.com/FlowiseAI/Flowise
**Analyzed:** 2026-05-02T01:40:32.567813+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redisgraph, redistimeseries. 1 related issue(s)/PR(s) found. Redis modules used: redisearch, redisgraph, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redisgraph, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 1 file(s)
- `redistimeseries` / `ts.add`: 1 file(s)
- `redisgraph` / `graph.query`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #6218](https://github.com/FlowiseAI/Flowise/issues/6218): Add Valkey Vector Store Node (open)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (259 occurrences)
- `ioredis` (3 occurrences)
