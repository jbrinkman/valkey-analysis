# Valkey Integration Analysis: anthropics/claude-plugins-official

**GitHub:** https://github.com/anthropics/claude-plugins-official
**Analyzed:** 2026-05-02T01:40:32.712030+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 4 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (79 total org repos):**
- [redis-py](https://github.com/anthropics/redis-py): None 🔴 Redis
- [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins): Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork
- [financial-services-plugins](https://github.com/anthropics/financial-services-plugins): None
- [claude-plugins-community](https://github.com/anthropics/claude-plugins-community): Community plugin marketplace for Claude Cowork and Claude Code. Read-only mirror — submit plugins at clau.de/plugin-directory-submission.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
