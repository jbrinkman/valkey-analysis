# Valkey Integration Analysis: qdrant/qdrant

**GitHub:** https://github.com/qdrant/qdrant
**Analyzed:** 2026-05-02T01:40:32.840444+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: Cargo.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 8 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (130 total org repos):**
- [qdrant-cloud-buf-plugins](https://github.com/qdrant/qdrant-cloud-buf-plugins): Collection of Buf plugins used by Qdrant Cloud APIs

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
