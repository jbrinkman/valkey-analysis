# Valkey Integration Analysis: pinpoint-apm/pinpoint

**GitHub:** https://github.com/pinpoint-apm/pinpoint
**Analyzed:** 2026-05-02T01:40:32.835633+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** cache, time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (6 occurrences)
- `jedis` (1 occurrences)
- `lettuce` (2 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 47 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (392 occurrences)
- `jedis` (1 occurrences)
- `lettuce` (7 occurrences)
