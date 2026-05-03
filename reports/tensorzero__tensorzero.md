# Valkey Integration Analysis: tensorzero/tensorzero

**GitHub:** https://github.com/tensorzero/tensorzero
**Analyzed:** 2026-05-02T01:40:32.862223+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 20 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 81 file(s)
  - [docs/deployment/valkey-redis.mdx](https://github.com/tensorzero/tensorzero/blob/7cd83f2255cccf87ebf43f2fa2a1c6cb1749c5bf/docs/deployment/valkey-redis.mdx)
  - [crates/tensorzero-core/src/db/valkey/mod.rs](https://github.com/tensorzero/tensorzero/blob/7cd83f2255cccf87ebf43f2fa2a1c6cb1749c5bf/crates/tensorzero-core/src/db/valkey/mod.rs)
  - [crates/tensorzero-core/src/db/valkey/cache.rs](https://github.com/tensorzero/tensorzero/blob/7cd83f2255cccf87ebf43f2fa2a1c6cb1749c5bf/crates/tensorzero-core/src/db/valkey/cache.rs)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #7232](https://github.com/tensorzero/tensorzero/issues/7232): Reinitialize runtime dependencies after full config apply (closed)
- [ISSUE #7012](https://github.com/tensorzero/tensorzero/issues/7012): CI/Merge Queue Performance: Analysis & Recommendations (open)
- [ISSUE #6994](https://github.com/tensorzero/tensorzero/issues/6994): Investigate flaky e2e tests in daily CI runs (open)
- [ISSUE #6755](https://github.com/tensorzero/tensorzero/issues/6755): Add tests using Redis instead of Valkey (closed)
- [ISSUE #6751](https://github.com/tensorzero/tensorzero/issues/6751): Add examples for caching with CH, Valkey (open)
- [ISSUE #6274](https://github.com/tensorzero/tensorzero/issues/6274): Run the entire client test suite with Postgres + Valkey in CI (closed)
- [ISSUE #6750](https://github.com/tensorzero/tensorzero/issues/6750): Hide unused dependencies from `/health` (open)
- [ISSUE #5691](https://github.com/tensorzero/tensorzero/issues/5691): Support Postgres-only TensorZero deployments (closed)
- [ISSUE #6138](https://github.com/tensorzero/tensorzero/issues/6138): Update valkey docs to note that we support `valkey://` and `valkeys://` urls (closed)
- [ISSUE #6161](https://github.com/tensorzero/tensorzero/issues/6161): Add Valkey-based inference caching (closed)
- [PR #6769](https://github.com/tensorzero/tensorzero/pull/6769): fix: only show enabled backends in /health response (open)
- [PR #7254](https://github.com/tensorzero/tensorzero/pull/7254): Make e2e tests deterministic for provider-proxy cache (closed)
- [PR #7278](https://github.com/tensorzero/tensorzero/pull/7278): Support hotswapping database connections (closed)
- [PR #7251](https://github.com/tensorzero/tensorzero/pull/7251): Hotswap gateway runtime dependencies after config apply (closed)
- [PR #7248](https://github.com/tensorzero/tensorzero/pull/7248): Make e2e tests deterministic for provider-proxy cache (closed)
- [PR #6794](https://github.com/tensorzero/tensorzero/pull/6794): Also run tests against redis in addition to valkey (closed)
- [PR #6924](https://github.com/tensorzero/tensorzero/pull/6924): Migrate core docs from CH to PG (closed)
- [PR #6752](https://github.com/tensorzero/tensorzero/pull/6752): Switch valkey namespace to redis for compatibility (closed)
- [PR #6585](https://github.com/tensorzero/tensorzero/pull/6585): Add cache.enabled and cache.backend config fields (closed)
- [PR #6425](https://github.com/tensorzero/tensorzero/pull/6425): Fix valkey TLS support and add a test (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (117 occurrences)
  - `docs/deployment/valkey-redis.mdx`
  - `Storage  Code Entity / Context  Purpose       PostgreSQL    TENSORZERO_POSTGRES_URL   Transactional data: API keys, authentication, and rate limit state       docs/gateway/configuration-reference.mdx `
  - `Caching:  If enabled, the system checks Valkey for a cached response       docs/gateway/api-reference/inference.mdx  141-149`

**Redis mentions:** 1 keyword(s) found
- `redis` (37 occurrences)
