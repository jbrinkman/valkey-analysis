# Valkey Integration Analysis: spiceai/spiceai

**GitHub:** https://github.com/spiceai/spiceai
**Analyzed:** 2026-05-02T01:40:32.855409+00:00

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
- `redistimeseries` / `ts.add`: 7 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (109 total org repos):**
- [data-components-contrib](https://github.com/spiceai/data-components-contrib): Community built data connectors and processors for Spice.ai

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
