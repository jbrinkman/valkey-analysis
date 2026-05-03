# Valkey Integration Analysis: GetStream/Vision-Agents

**GitHub:** https://github.com/GetStream/Vision-Agents
**Analyzed:** 2026-05-02T01:40:32.585036+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 4 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (478 total org repos):**
- [redis](https://github.com/GetStream/redis): Type-safe Redis client for Golang 🔴 Redis
- [combase-plugins](https://github.com/GetStream/combase-plugins): None
- [stream-firebase-extensions](https://github.com/GetStream/stream-firebase-extensions): Stream firebase extensions
- [firebase-extensions-iOS-demo](https://github.com/GetStream/firebase-extensions-iOS-demo): Demonstration of the Firebase Extensions that Stream offers. Concretely, an iOS app that uses the Auth extensions to sync users and avoid having to build our own server.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
