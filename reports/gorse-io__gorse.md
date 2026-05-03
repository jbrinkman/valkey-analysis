# Valkey Integration Analysis: gorse-io/gorse

**GitHub:** https://github.com/gorse-io/gorse
**Analyzed:** 2026-05-03T00:56:44.341623+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis. 1 related issue(s)/PR(s) found (1 positive). Redis modules used: redisearch, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** cache, time_series, vector_store
- **Integration Type:** native
- **Redis Modules:** redisearch, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ✅ [ISSUE #1260](https://github.com/gorse-io/gorse/issues/1260): Add Valkey as a cache storage backend (open)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (191 occurrences)

**Redis module mentions:** ['redisearch', 'redistimeseries']
