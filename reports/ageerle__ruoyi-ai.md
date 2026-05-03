# Valkey Integration Analysis: ageerle/ruoyi-ai

**GitHub:** https://github.com/ageerle/ruoyi-ai
**Analyzed:** 2026-05-02T01:40:32.704933+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redisgraph, redistimeseries. Redis dependencies: redis. Redis modules used: redisgraph, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisgraph, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (4 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 15 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (383 occurrences)

**Redis module mentions:** ['redistimeseries', 'redisgraph']
