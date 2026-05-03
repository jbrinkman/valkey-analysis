# Valkey Integration Analysis: yt-dlp/yt-dlp

**GitHub:** https://github.com/yt-dlp/yt-dlp
**Analyzed:** 2026-05-02T01:40:32.893691+00:00

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

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (3 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (14 total org repos):**
- [yt-dlp-sample-plugins](https://github.com/yt-dlp/yt-dlp-sample-plugins): Sample plugin package for yt-dlp

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
