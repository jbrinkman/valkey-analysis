# Valkey Integration Analysis: gravitational/teleport

**GitHub:** https://github.com/gravitational/teleport
**Analyzed:** 2026-05-02T01:40:32.774237+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 13 related issue(s)/PR(s) found. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, go.mod, Cargo.toml

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 30 file(s)
  - [lib/cloud/aws/aws.go](https://github.com/gravitational/teleport/blob/5bde21eafe0ea4e9a9f313d0af710f6a827bdc5c/lib/cloud/aws/aws.go)
  - [docs/pages/includes/discovery/aws-db-discovery-config.mdx](https://github.com/gravitational/teleport/blob/5bde21eafe0ea4e9a9f313d0af710f6a827bdc5c/docs/pages/includes/discovery/aws-db-discovery-config.mdx)
  - [lib/config/database.go](https://github.com/gravitational/teleport/blob/5bde21eafe0ea4e9a9f313d0af710f6a827bdc5c/lib/config/database.go)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 30 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #64628](https://github.com/gravitational/teleport/issues/64628): FY27 Q1 Teleport Test Plan (open)
- [ISSUE #47507](https://github.com/gravitational/teleport/issues/47507): AWS ElastiCache/MemoryDB for Valkey support (closed)
- [ISSUE #40225](https://github.com/gravitational/teleport/issues/40225): Support ElastiCache Serverless (closed)
- [ISSUE #55231](https://github.com/gravitational/teleport/issues/55231): Teleport 18 test plan (closed)
- [ISSUE #48003](https://github.com/gravitational/teleport/issues/48003): Teleport 17 Test Plan (closed)
- [ISSUE #47514](https://github.com/gravitational/teleport/issues/47514): Database guides for Valkey (open)
- [PR #59395](https://github.com/gravitational/teleport/pull/59395): Release 18.2.2 (closed)
- [PR #58891](https://github.com/gravitational/teleport/pull/58891): [v18] Add ElastiCache Serverless docs (closed)
- [PR #58473](https://github.com/gravitational/teleport/pull/58473): Add ElastiCache Serverless docs (closed)
- [PR #58335](https://github.com/gravitational/teleport/pull/58335): Add ElastiCache Serverless config (closed)
- [PR #55725](https://github.com/gravitational/teleport/pull/55725): [v18][docs] break ElastiCache and MemoryDB guide and add Valkey (closed)
- [PR #55563](https://github.com/gravitational/teleport/pull/55563): [docs] break ElastiCache and MemoryDB guide and add Valkey (closed)
- [PR #51050](https://github.com/gravitational/teleport/pull/51050): Migrate AWS ElastiCache clients to AWS SDK v2 (closed)

## Phase 5: Ecosystem

**Related repos in org (194 total org repos):**
- [teleport-plugins](https://github.com/gravitational/teleport-plugins): Set of plugins for Teleport
- [redis](https://github.com/gravitational/redis): Teleport fork of redis/go-redis: Type-safe Redis client for Golang 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (34 occurrences)
- `go-redis` (3 occurrences)
