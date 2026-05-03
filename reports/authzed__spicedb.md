# Valkey Integration Analysis: authzed/spicedb

**GitHub:** https://github.com/authzed/spicedb
**Analyzed:** 2026-05-02T01:40:32.716921+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

No Valkey or Redis integration detected. Redis modules used: redisbloom, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisbloom, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)
- `redisbloom` / `bf.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (6 occurrences)
