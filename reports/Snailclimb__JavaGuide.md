# Valkey Integration Analysis: Snailclimb/JavaGuide

**GitHub:** https://github.com/Snailclimb/JavaGuide
**Analyzed:** 2026-05-02T01:40:32.691454+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redisai, redistimeseries. Redis modules used: redisai, redisbloom, redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisai, redisbloom, redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (29 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)
- `redisbloom` / `bf.add`: 1 file(s)
- `redisai` / `redisai`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (375 occurrences)

**Redis module mentions:** ['redisearch', 'redisjson']
