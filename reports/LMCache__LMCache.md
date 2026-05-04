# Valkey Integration Analysis: LMCache/LMCache

**GitHub:** https://github.com/LMCache/LMCache
**Analyzed:** 2026-05-04T02:04:35.702088+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 15 related issue(s)/PR(s) found (5 inconclusive, 10 positive). 10 related extension repo(s) found (0 mention Valkey).

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** cache
- **Integration Type:** extension
- **Redis Modules:** None detected

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, setup.py

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (3 occurrences)

**Valkey mentions in docs:**
- https://docs.lmcache.ai/getting_started/quickstart/
- https://docs.lmcache.ai/getting_started/installation

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ❓ [ISSUE #627](https://github.com/LMCache/LMCache/issues/627): [Onboarding] Welcoming contributors with good first issues! (closed)
- ❓ [ISSUE #1621](https://github.com/LMCache/LMCache/issues/1621): Support Valkey Backend (closed)
- ❓ [ISSUE #574](https://github.com/LMCache/LMCache/issues/574): LMCache Q2 Roadmap (closed)
- ❓ [ISSUE #1222](https://github.com/LMCache/LMCache/issues/1222): [Usage] Does LMCache support the RDMA feature of valkey? (closed)
- ❓ [ISSUE #481](https://github.com/LMCache/LMCache/issues/481): Introduce valkey as a remote backend of LMCache (closed)
- ✅ [PR #2311](https://github.com/LMCache/LMCache/pull/2311): Support TLS connection for Valkey (open)
- ✅ [PR #2967](https://github.com/LMCache/LMCache/pull/2967): [Operator] Add L2 RESP (Redis/Valkey) adapter support (closed)
- ✅ [PR #2949](https://github.com/LMCache/LMCache/pull/2949): [Security][Remote Connector]: Add env var auth config for RESP (closed)
- ✅ [PR #2790](https://github.com/LMCache/LMCache/pull/2790): feat: improve ValkeyConnector with cluster mode, TLS, and GLIDE optimizations (closed)
- ✅ [PR #2307](https://github.com/LMCache/LMCache/pull/2307): Support database option at Valkey connector  (closed)
- ✅ [PR #2316](https://github.com/LMCache/LMCache/pull/2316): init storage manager after register kv caches (closed)
- ✅ [PR #2315](https://github.com/LMCache/LMCache/pull/2315): [refactor] use shapes and dtypes in RemoteMetadata (closed)
- ✅ [PR #1888](https://github.com/LMCache/LMCache/pull/1888): [RFC][Core] v2. memory pool facade phase1 (closed)
- ✅ [PR #1743](https://github.com/LMCache/LMCache/pull/1743): Valkey connector (closed)
- ✅ [PR #482](https://github.com/LMCache/LMCache/pull/482): [#481] Add a simple valkey remote backend (closed)

## Phase 5: Ecosystem

**Related repos in org (20 total org repos):**
- [lmcache-server](https://github.com/LMCache/lmcache-server): None
- [lmcache-vllm](https://github.com/LMCache/lmcache-vllm): The driver for LMCache core to run in vLLM
- [lmcache-tests](https://github.com/LMCache/lmcache-tests): None 🔴 Redis
- [lmcache.github.io](https://github.com/LMCache/lmcache.github.io): LMCache official blog
- [LMCache-Examples](https://github.com/LMCache/LMCache-Examples): None
- [LMCache-Ascend](https://github.com/LMCache/LMCache-Ascend): LMCache on Ascend
- [lmcache_frontend](https://github.com/LMCache/lmcache_frontend): the frontend of lmcache
- [lmcache-agentic](https://github.com/LMCache/lmcache-agentic): None
- [lmcache-agent-trace](https://github.com/LMCache/lmcache-agent-trace): Agent application/benchmark/workload traces should be placed here.
- [lmcache_redis](https://github.com/LMCache/lmcache_redis): zero copy python sdk

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (36 occurrences)
  - `Sources:       README.md  66-80         docs/source/getting_started/installation.rst  21-33         docs/source/getting_started/installation.rst  161-177         docs/source/index.rst  135-136        `

**Redis mentions:** 1 keyword(s) found
- `redis` (80 occurrences)
