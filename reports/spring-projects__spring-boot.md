# Valkey Integration Analysis: spring-projects/spring-boot

**GitHub:** https://github.com/spring-projects/spring-boot
**Analyzed:** 2026-05-02T01:40:32.856108+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 3 related extension repo(s) found (1 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: build.gradle

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 81 file(s)
- `redisjson` / `rejson`: 24 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (80 total org repos):**
- [spring-data-redis](https://github.com/spring-projects/spring-data-redis): Provides support to increase developer productivity in Java when using Redis, a key-value store. Uses familiar Spring concepts such as a template classes for core API usage and lightweight repository style data access. ✅ Valkey 🔴 Redis
- [spring-integration-extensions](https://github.com/spring-projects/spring-integration-extensions): The Spring Integration Extensions project provides extension components for Spring Integration
- [spring-batch-extensions](https://github.com/spring-projects/spring-batch-extensions): Spring Batch Extensions

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (162 occurrences)
- `jedis` (6 occurrences)
- `lettuce` (6 occurrences)
