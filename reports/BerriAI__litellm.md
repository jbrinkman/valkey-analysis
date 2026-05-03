# Valkey Integration Analysis: BerriAI/litellm

**GitHub:** https://github.com/BerriAI/litellm
**Analyzed:** 2026-05-02T01:40:32.459797+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 4 related issue(s)/PR(s) found. 2 related discussion(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** redis, redisvl
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, package.json

**Redis dependencies:**
- `redis` (redis-client)
- `redisvl` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 2 file(s)
  - [litellm/caching/redis_cache.py](https://github.com/BerriAI/litellm/blob/eab0075353abba12428a3712c6bfce5704576e67/litellm/caching/redis_cache.py)
  - [tests/test_litellm/caching/test_redis_cache.py](https://github.com/BerriAI/litellm/blob/eab0075353abba12428a3712c6bfce5704576e67/tests/test_litellm/caching/test_redis_cache.py)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #20734](https://github.com/BerriAI/litellm/issues/20734): [Bug]: Redis Sentinel auth fails because Sentinel() uses password=sentinel_password instead of sentinel_kwargs (open)
- [ISSUE #11243](https://github.com/BerriAI/litellm/issues/11243): Regression: Redis/Valkey cache backend not initializing, `/cache/ping` endpoint 404, no cache health in Docker (v1.71.x+) (closed)
- [ISSUE #14683](https://github.com/BerriAI/litellm/issues/14683): [Bug]: TPM/RPM not working (closed)
- [PR #16207](https://github.com/BerriAI/litellm/pull/16207): fix(redis): handle float redis_version from AWS ElastiCache Valkey (closed)

**Discussions:**
- [Discussion #18562](https://github.com/BerriAI/litellm/discussions/18562): Open WebUI + LiteLLM Stack – Production-Ready* with Observability (LGTM), Qdrant, Traefik
- [Discussion #2032](https://github.com/BerriAI/litellm/discussions/2032): Multiple LiteLLM instances

## Phase 5: Ecosystem

**Related repos in org (44 total org repos):**
- [litellm-pgvector](https://github.com/BerriAI/litellm-pgvector): None

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (335 occurrences)
