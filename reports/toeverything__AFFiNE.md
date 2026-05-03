# Valkey Integration Analysis: toeverything/AFFiNE

**GitHub:** https://github.com/toeverything/AFFiNE
**Analyzed:** 2026-05-02T01:40:32.864949+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, ioredis. 1 related issue(s)/PR(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** ioredis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, Cargo.toml

**Redis dependencies:**
- `redis` (redis-client)
- `ioredis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 10 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #11220](https://github.com/toeverything/AFFiNE/issues/11220): [Feature Request]: Self-hosting with Redis alternative (closed)

## Phase 5: Ecosystem

**Related repos in org (45 total org repos):**
- [AFFiNE-Community](https://github.com/toeverything/AFFiNE-Community): None

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (228 occurrences)
- `ioredis` (11 occurrences)
