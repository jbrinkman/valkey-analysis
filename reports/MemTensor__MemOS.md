# Valkey Integration Analysis: MemTensor/MemOS

**GitHub:** https://github.com/MemTensor/MemOS
**Analyzed:** 2026-05-02T01:40:32.659732+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** memory, message_broker, time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (2 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)
- `redisjson` / `rejson`: 18 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (192 occurrences)
