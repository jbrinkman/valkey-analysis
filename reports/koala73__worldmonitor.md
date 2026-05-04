# Valkey Integration Analysis: koala73/worldmonitor

**GitHub:** https://github.com/koala73/worldmonitor
**Analyzed:** 2026-05-04T02:04:36.753301+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redisai. Redis dependencies: redis. 1 related issue(s)/PR(s) found (1 positive). Redis modules used: redisai.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** cache
- **Integration Type:** native
- **Redis Modules:** redisai

## Phase 1: Dependency Scan

Manifests checked: package.json

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ✅ [PR #1966](https://github.com/koala73/worldmonitor/pull/1966): fix(consumer-prices): restore seed script + fix publish job writing to wrong Redis (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (218 occurrences)

**Redis module mentions:** ['redisai']
