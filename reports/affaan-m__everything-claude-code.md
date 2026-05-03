# Valkey Integration Analysis: affaan-m/everything-claude-code

**GitHub:** https://github.com/affaan-m/everything-claude-code
**Analyzed:** 2026-05-02T01:40:32.704156+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis modules used: redisearch, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, package.json

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 1 file(s)
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
