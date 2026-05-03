# Valkey Integration Analysis: Tencent/WeKnora

**GitHub:** https://github.com/Tencent/WeKnora
**Analyzed:** 2026-05-02T01:40:32.694018+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** rate_limiting, time_series, vector_store
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (2 occurrences)

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [internal/event/event.go](https://github.com/Tencent/WeKnora/blob/58a283effeac7ccfcb2b25063233695f600237e1/internal/event/event.go)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (257 total org repos):**
- [tencent-edgeone-agent-plugins](https://github.com/Tencent/tencent-edgeone-agent-plugins): None

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (2 occurrences)
  - `Sources:        VERSION  1         README.md  52-67         CHANGELOG.md  5-20                   Dismiss   Refresh this wiki  Enter email to refresh    On this page    WeKnora Overview    Purpose and `

**Redis mentions:** 2 keyword(s) found
- `redis` (222 occurrences)
- `go-redis` (1 occurrences)
