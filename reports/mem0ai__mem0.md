# Valkey Integration Analysis: mem0ai/mem0

**GitHub:** https://github.com/mem0ai/mem0
**Analyzed:** 2026-05-04T02:04:35.759433+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. Valkey dependencies: valkey. 17 related issue(s)/PR(s) found (2 inconclusive, 15 positive). 1 related discussion(s) found. Redis modules used: redisearch.

## Integration Details

- **Client Libraries:** redis, redisvl, valkey
- **Use Cases:** vector_store
- **Integration Type:** native
- **Redis Modules:** redisearch

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Valkey dependencies:**
- `valkey` (valkey-client)

**Redis dependencies:**
- `redis` (redis-client)
- `redisvl` (redis-client)

## Phase 2: Documentation Scan

**Valkey mentions in docs:**
- https://docs.mem0.ai/open-source/overview
- https://docs.mem0.ai/open-source/setup#upgrade-notes
- https://docs.mem0.ai/integrations/langgraph

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ✅ [ISSUE #5006](https://github.com/mem0ai/mem0/issues/5006): Valkey vector store: memory field should use TEXT index type instead of TAG (open)
- ✅ [ISSUE #3948](https://github.com/mem0ai/mem0/issues/3948): Mem0 Vector Search Returns Zero Results on AWS ElastiCache Valkey (open)
- ✅ [ISSUE #4453](https://github.com/mem0ai/mem0/issues/4453): fix: threshold filtering broken for distance-based vector stores (open)
- ❓ [ISSUE #3788](https://github.com/mem0ai/mem0/issues/3788): using LMStudio, search returns no results (closed)
- ❓ [ISSUE #4336](https://github.com/mem0ai/mem0/issues/4336): Mem0 with Valkey: update() corrupts embeddings when called with vector=None (closed)
- ✅ [PR #5021](https://github.com/mem0ai/mem0/pull/5021): fix: keep Valkey hashes aligned with index schema (open)
- ✅ [PR #5014](https://github.com/mem0ai/mem0/pull/5014): fix(vector-stores): index Valkey memory as text (open)
- ✅ [PR #4842](https://github.com/mem0ai/mem0/pull/4842): docs: add Neon vector database guide (open)
- ✅ [PR #4815](https://github.com/mem0ai/mem0/pull/4815): test: update valkey cluster search test to use top_k parameter (closed)
- ✅ [PR #4759](https://github.com/mem0ai/mem0/pull/4759): feat(valkey): add cluster mode enabled (CME) support (closed)
- ✅ [PR #4656](https://github.com/mem0ai/mem0/pull/4656): fix(configs): add missing ConfigDict to vector store configs (closed)
- ✅ [PR #4652](https://github.com/mem0ai/mem0/pull/4652): fix: normalize vector store scores to similarity for consistent threshold filtering (open)
- ✅ [PR #4427](https://github.com/mem0ai/mem0/pull/4427): fix: handle vector=None in Qdrant adapter update() to prevent validation error (closed)
- ✅ [PR #4426](https://github.com/mem0ai/mem0/pull/4426): fix: skip embedding update when vector is None in Valkey adapter (closed)
- ✅ [PR #3653](https://github.com/mem0ai/mem0/pull/3653): fix: Prevent PointStruct validation error when updating metadata for event='NONE' (closed)
- ✅ [PR #3824](https://github.com/mem0ai/mem0/pull/3824): Add Strands agent (with AWS ElastiCache and Neptune) example mention in Joint blog post by Mem0 and AWS (closed)
- ✅ [PR #3272](https://github.com/mem0ai/mem0/pull/3272): feat(vector-store): Add Valkey vector store support (closed)

**Discussions:**
- [Discussion #3657](https://github.com/mem0ai/mem0/discussions/3657): PRs to come from me on openmemory - Roadmap

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (45 occurrences)
  - `See  Installation and Setup  for detailed guides and  System Architecture  for a deep dive into the internal components.                 Dismiss   Refresh this wiki  This wiki was recently refreshed. `

**Redis mentions:** 1 keyword(s) found
- `redis` (49 occurrences)

**Redis module mentions:** ['redisearch']
