# Valkey Integration Analysis: servo/servo

**GitHub:** https://github.com/servo/servo
**Analyzed:** 2026-05-02T01:40:32.849975+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

No Valkey or Redis integration detected. Redis modules used: redisgraph, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisgraph, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, Cargo.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 191 file(s)
- `redisjson` / `rejson`: 1 file(s)
- `redisgraph` / `graph.query`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (4 occurrences)

**Redis module mentions:** ['redisjson']
