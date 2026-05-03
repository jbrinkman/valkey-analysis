# Valkey Integration Analysis: zenml-io/zenml

**GitHub:** https://github.com/zenml-io/zenml
**Analyzed:** 2026-05-02T01:40:32.895735+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

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

**Related repos in org (81 total org repos):**
- [zenml-hub-plugins](https://github.com/zenml-io/zenml-hub-plugins): None
- [zenml-plugins](https://github.com/zenml-io/zenml-plugins): A repository of not officially supported ZenML plugins

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
