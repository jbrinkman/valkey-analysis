# Valkey Integration Analysis: letta-ai/letta

**GitHub:** https://github.com/letta-ai/letta
**Analyzed:** 2026-05-02T01:40:32.800045+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 1 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #3065](https://github.com/letta-ai/letta/issues/3065): Use Valkey as an Alternative for Redis Caching in docker-compose.yml (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (60 occurrences)
- `lettuce` (19 occurrences)
