# Valkey Integration Analysis: pytorch/executorch

**GitHub:** https://github.com/pytorch/executorch
**Analyzed:** 2026-05-02T01:40:32.840005+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, setup.py

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [backends/apple/coreml/runtime/delegate/serde_json.mm](https://github.com/pytorch/executorch/blob/3be45468bad401b09ec79e0627fbcb1142a8f6dc/backends/apple/coreml/runtime/delegate/serde_json.mm)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 15 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (69 total org repos):**
- [contrib](https://github.com/pytorch/contrib): Implementations of ideas from recent papers

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
