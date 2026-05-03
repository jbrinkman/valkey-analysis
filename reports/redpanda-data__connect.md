# Valkey Integration Analysis: redpanda-data/connect

**GitHub:** https://github.com/redpanda-data/connect
**Analyzed:** 2026-05-02T01:40:32.843374+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis. 4 related extension repo(s) found (0 mention Valkey). Redis modules used: redisbloom, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** message_broker, time_series
- **Integration Type:** native
- **Redis Modules:** redisbloom, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (2 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 13 file(s)
- `redisbloom` / `bf.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (127 total org repos):**
- [integrations-extras](https://github.com/redpanda-data/integrations-extras): Community developed integrations and plugins for the Datadog Agent.
- [community-program](https://github.com/redpanda-data/community-program): For all community events, programs and more. 
- [docs-extensions-and-macros](https://github.com/redpanda-data/docs-extensions-and-macros): Extensions and macros developed for Redpanda documentation.
- [oxla-clang-tidy-custom-plugins](https://github.com/redpanda-data/oxla-clang-tidy-custom-plugins): Class member order plugin plus examples of other custom clang-tidy plugins

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (89 occurrences)
