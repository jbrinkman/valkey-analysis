# Valkey Integration Analysis: netbirdio/netbird

**GitHub:** https://github.com/netbirdio/netbird
**Analyzed:** 2026-05-02T01:40:32.825220+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis. 4 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 10 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (47 total org repos):**
- [example-public-integrations](https://github.com/netbirdio/example-public-integrations): None
- [management-integrations](https://github.com/netbirdio/management-integrations): None
- [OPNsensePlugins](https://github.com/netbirdio/OPNsensePlugins): OPNsense plugin collection 🔴 Redis
- [plugins](https://github.com/netbirdio/plugins): OPNsense plugin collection 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (5 occurrences)

**Redis module mentions:** ['redistimeseries']
