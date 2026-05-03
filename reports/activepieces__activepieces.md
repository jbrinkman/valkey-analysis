# Valkey Integration Analysis: activepieces/activepieces

**GitHub:** https://github.com/activepieces/activepieces
**Analyzed:** 2026-05-02T01:40:32.703459+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redisai, redistimeseries. Redis dependencies: redis, ioredis. 2 related issue(s)/PR(s) found. Redis modules used: redisai, redistimeseries.

## Integration Details

- **Client Libraries:** ioredis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisai, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

**Redis dependencies:**
- `redis` (redis-client)
- `ioredis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)
- `redisai` / `redisai`: 6 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #10795](https://github.com/activepieces/activepieces/issues/10795): [BUG]: Helm installation - chart dependencies postgresql and redis refer to commercial bitnami images (open)
- [ISSUE #5005](https://github.com/activepieces/activepieces/issues/5005): Replace Redis with Valkey? (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (264 occurrences)
- `ioredis` (1 occurrences)
