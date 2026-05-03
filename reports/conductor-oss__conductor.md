# Valkey Integration Analysis: conductor-oss/conductor

**GitHub:** https://github.com/conductor-oss/conductor
**Analyzed:** 2026-05-02T01:40:32.736696+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: requirements.txt, build.gradle

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (9 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 11 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (32 total org repos):**
- [conductor-community](https://github.com/conductor-oss/conductor-community): None

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (402 occurrences)
- `jedis` (14 occurrences)
