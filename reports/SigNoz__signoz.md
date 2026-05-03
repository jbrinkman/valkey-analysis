# Valkey Integration Analysis: SigNoz/signoz

**GitHub:** https://github.com/SigNoz/signoz
**Analyzed:** 2026-05-02T01:40:32.689844+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis, github.com/go-redis/redis. 3 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/go-redis/redis, github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)
- `github.com/go-redis/redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)
- `redisjson` / `rejson`: 3 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (153 total org repos):**
- [opentelemetry-go-contrib](https://github.com/SigNoz/opentelemetry-go-contrib): Collection of extensions for OpenTelemetry-Go.
- [opentelemetry-collector-contrib](https://github.com/SigNoz/opentelemetry-collector-contrib): None
- [opentelemetry-collector-contrib-test](https://github.com/SigNoz/opentelemetry-collector-contrib-test): Contrib repository for the OpenTelemetry Collector

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (47 occurrences)
- `go-redis` (5 occurrences)
