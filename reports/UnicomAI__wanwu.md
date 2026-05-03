# Valkey Integration Analysis: UnicomAI/wanwu

**GitHub:** https://github.com/UnicomAI/wanwu
**Analyzed:** 2026-05-02T01:40:32.697055+00:00

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

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [configs/microservice/bff-service/configs/agent-skills/minimax/fullstack-dev/references/technology-selection.md](https://github.com/UnicomAI/wanwu/blob/2b42bb911e3ff6ecfec3b49312742fde4408765d/configs/microservice/bff-service/configs/agent-skills/minimax/fullstack-dev/references/technology-selection.md)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (173 occurrences)
