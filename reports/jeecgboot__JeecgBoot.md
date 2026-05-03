# Valkey Integration Analysis: jeecgboot/JeecgBoot

**GitHub:** https://github.com/jeecgboot/JeecgBoot
**Analyzed:** 2026-05-02T01:40:32.787431+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (3 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 13 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (933 occurrences)
- `jedis` (7 occurrences)
- `lettuce` (20 occurrences)

**Redis module mentions:** ['redistimeseries', 'redisjson']
