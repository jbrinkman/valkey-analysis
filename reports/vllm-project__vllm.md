# Valkey Integration Analysis: vllm-project/vllm

**GitHub:** https://github.com/vllm-project/vllm
**Analyzed:** 2026-05-02T01:40:32.886198+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 10 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, setup.py

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 20 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #10818](https://github.com/vllm-project/vllm/issues/10818): [RFC]: Disaggregated prefilling and KV cache transfer roadmap (closed)
- [PR #30913](https://github.com/vllm-project/vllm/pull/30913): [docker] install cuda13 version of lmcache and nixl (closed)
- [PR #16159](https://github.com/vllm-project/vllm/pull/16159): [V1][Core] Add async kv cache offload (closed)
- [PR #8018](https://github.com/vllm-project/vllm/pull/8018): [Core][Kernel][Misc] Support external swapper for vllm (closed)
- [PR #12957](https://github.com/vllm-project/vllm/pull/12957): [Feature][Disaggregated] Support XpYd disaggregated prefill with MooncakeStore (closed)
- [PR #11480](https://github.com/vllm-project/vllm/pull/11480): [Misc] Allow initializing KV cache transfer agent when `kv_parallel_size==1` (closed)
- [PR #8694](https://github.com/vllm-project/vllm/pull/8694): [Core] Enable Memory Tiering for vLLM (closed)
- [PR #8498](https://github.com/vllm-project/vllm/pull/8498): [Core] Implementing disaggregated prefilling, and caching KV cache in CPU/disk/database. (closed)
- [PR #9537](https://github.com/vllm-project/vllm/pull/9537): [WIP] Disaggregated prefilling support X prefill + Y decode (closed)
- [PR #8724](https://github.com/vllm-project/vllm/pull/8724): [Core] Disaggregated prefilling supports valkey (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (1 occurrences)
