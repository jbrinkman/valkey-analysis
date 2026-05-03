# Valkey Integration Analysis: Unstructured-IO/unstructured

**GitHub:** https://github.com/Unstructured-IO/unstructured
**Analyzed:** 2026-05-02T01:40:32.697548+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 3 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (41 total org repos):**
- [community](https://github.com/Unstructured-IO/community): Open source libraries and APIs to build custom preprocessing pipelines for labeling, training, or production machine learning pipelines.
- [prometheus-community-helm-charts](https://github.com/Unstructured-IO/prometheus-community-helm-charts): Prometheus community Helm charts
- [unstructured-platform-plugins](https://github.com/Unstructured-IO/unstructured-platform-plugins): None

## DeepWiki Analysis

**Redis module mentions:** ['redisjson']

No Valkey or Redis mentions found in DeepWiki content.
