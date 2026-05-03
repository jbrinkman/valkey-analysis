# Valkey Integration Analysis: cube-js/cube

**GitHub:** https://github.com/cube-js/cube
**Analyzed:** 2026-05-02T01:40:32.739286+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [packages/cubejs-schema-compiler/src/adapter/Granularity.ts](https://github.com/cube-js/cube/blob/98128afd15bc7e4bb0b85eaafc9520b967837d4d/packages/cubejs-schema-compiler/src/adapter/Granularity.ts)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (16 occurrences)
- `ioredis` (1 occurrences)
