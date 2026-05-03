# Valkey Integration Analysis: kataras/iris

**GitHub:** https://github.com/kataras/iris
**Analyzed:** 2026-05-02T01:40:32.791469+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 1 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (35 occurrences)
