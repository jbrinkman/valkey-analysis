# Valkey Integration Analysis: gnachman/iTerm2

**GitHub:** https://github.com/gnachman/iTerm2
**Analyzed:** 2026-05-02T01:40:32.765416+00:00

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

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 2 file(s)
  - [sources/DataStructuresAlgorithms/IntervalTree.m](https://github.com/gnachman/iTerm2/blob/7d11b982d3101650247b2bcb0c826fe90a2d8bb3/sources/DataStructuresAlgorithms/IntervalTree.m)
  - [sources/StatusBar/Components/iTermStatusBarGitComponent.m](https://github.com/gnachman/iTerm2/blob/7d11b982d3101650247b2bcb0c826fe90a2d8bb3/sources/StatusBar/Components/iTermStatusBarGitComponent.m)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 6 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
