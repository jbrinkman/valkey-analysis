# Valkey Integration Analysis: spring-projects/spring-ai

**GitHub:** https://github.com/spring-projects/spring-ai
**Analyzed:** 2026-05-04T02:04:35.978346+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 3 related issue(s)/PR(s) found (1 negative, 2 positive). 3 related extension repo(s) found (1 mention Valkey).

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** vector_store
- **Integration Type:** extension
- **Redis Modules:** None detected

## Phase 1: Dependency Scan

Manifests checked: pom.xml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ⛔ [ISSUE #5709](https://github.com/spring-projects/spring-ai/issues/5709): RedisVectorStore.similaritySearch() fails on AWS ElastiCache Valkey 8.x due to unsupported FT.SEARCH SORTBY clause (open)
- ✅ [ISSUE #5215](https://github.com/spring-projects/spring-ai/issues/5215): Add Amazon ElastiCache / Valkey as a Vector Store (open)
- ✅ [PR #5471](https://github.com/spring-projects/spring-ai/pull/5471): GH-5215: Add Valkey Vector Store module (open)

## Phase 5: Ecosystem

**Related repos in org (80 total org repos):**
- [spring-data-redis](https://github.com/spring-projects/spring-data-redis): Provides support to increase developer productivity in Java when using Redis, a key-value store. Uses familiar Spring concepts such as a template classes for core API usage and lightweight repository style data access. ✅ Valkey 🔴 Redis
- [spring-integration-extensions](https://github.com/spring-projects/spring-integration-extensions): The Spring Integration Extensions project provides extension components for Spring Integration
- [spring-batch-extensions](https://github.com/spring-projects/spring-batch-extensions): Spring Batch Extensions

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (166 occurrences)
- `jedis` (3 occurrences)
