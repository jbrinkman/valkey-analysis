# Valkey Integration Analysis: HumanSignal/label-studio

**GitHub:** https://github.com/HumanSignal/label-studio
**Analyzed:** 2026-05-02T01:40:32.616914+00:00

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

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (50 total org repos):**
- [label-studio-plugins](https://github.com/HumanSignal/label-studio-plugins): Plugins to extend Label Studio with custom workflows, integrations, and UI components.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (399 occurrences)
- `redis-py` (2 occurrences)
