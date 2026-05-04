# Valkey Integration Analysis: langfuse/langfuse

**GitHub:** https://github.com/langfuse/langfuse
**Analyzed:** 2026-05-04T02:04:36.535728+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

No Valkey or Redis integration detected. 15 related issue(s)/PR(s) found (1 negative, 7 inconclusive, 7 positive). 10 related discussion(s) found.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** None detected
- **Integration Type:** none
- **Redis Modules:** None detected

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ❓ [ISSUE #11603](https://github.com/langfuse/langfuse/issues/11603): bug: S3 will upload a large number of small json files, resulting in 100% inode usage. How should it be configured? (closed)
- ✅ [ISSUE #5959](https://github.com/langfuse/langfuse/issues/5959): bug: Pod for deploying web UI is not coming up (open)
- ✅ [ISSUE #6198](https://github.com/langfuse/langfuse/issues/6198): bug: Observations migration to Clickhouse failed to due due to deadlock (open)
- ❓ [ISSUE #9649](https://github.com/langfuse/langfuse/issues/9649): bug: failed prisma migrations (closed)
- ❓ [ISSUE #9443](https://github.com/langfuse/langfuse/issues/9443): bug: Redis KEYS command causes AWS Valkey Serverless compatibility issue (closed)
- ❓ [ISSUE #7150](https://github.com/langfuse/langfuse/issues/7150): bug: Failure in Helm upgrade in self-hosted Kubernetes environment (closed)
- ⛔ [ISSUE #6667](https://github.com/langfuse/langfuse/issues/6667): bug: Unable to do helm upgrade on self hosted installation (closed)
- ❓ [ISSUE #8731](https://github.com/langfuse/langfuse/issues/8731): bug: Self Hosted UI calls /api/trpc/prompt.create in stead of the /api/public/v2/prompts when creating prompt (closed)
- ❓ [ISSUE #7746](https://github.com/langfuse/langfuse/issues/7746): bug: otel trace metadata not being merged in self hosted langfuse (closed)
- ❓ [ISSUE #6765](https://github.com/langfuse/langfuse/issues/6765): bug: migration job "migrate_event_log_to_blob_storage" failed after upgrading from 3.30.0 to 3.54.0 (closed)
- ✅ [PR #9461](https://github.com/langfuse/langfuse/pull/9461): fix(model-cache): replace KEYS with SCAN for Valkey Serverless compatibility (closed)
- ✅ [PR #7355](https://github.com/langfuse/langfuse/pull/7355): docs: Update network diagram (closed)
- ✅ [PR #3688](https://github.com/langfuse/langfuse/pull/3688): chore(deps): bump @aws-sdk/s3-request-presigner from 3.614.0 to 3.668.0 (closed)
- ✅ [PR #3658](https://github.com/langfuse/langfuse/pull/3658): chore(deps): bump @aws-sdk/s3-request-presigner from 3.614.0 to 3.667.0 (closed)
- ✅ [PR #3661](https://github.com/langfuse/langfuse/pull/3661): chore(deps): bump @aws-sdk/lib-storage from 3.645.0 to 3.667.0 (closed)

**Discussions:**
- [Discussion #12848](https://github.com/orgs/langfuse/discussions/12848): Critical metadata eviction risk in Langfuse (Valkey allkeys-lru)
- [Discussion #13159](https://github.com/orgs/langfuse/discussions/13159): Timeout errors showing up
- [Discussion #11977](https://github.com/orgs/langfuse/discussions/11977): Langfuse Redis Primary Pod Terminated Due to AOF fsync Delays
- [Discussion #11933](https://github.com/orgs/langfuse/discussions/11933): Best practices to setup replication, backup/restore and Disaster recovery in Langfuse underlying storage
- [Discussion #12053](https://github.com/orgs/langfuse/discussions/12053): Performance Bottleneck: ECONNRESET / Socket Hang Up under moderate load (30 RPS)
- [Discussion #12054](https://github.com/orgs/langfuse/discussions/12054): Prompt cache keys never written to Redis on self-hosted prod (v3.133)
- [Discussion #11216](https://github.com/orgs/langfuse/discussions/11216): Langfuse +Docker+Pytest Self Hosting Issue
- [Discussion #11823](https://github.com/orgs/langfuse/discussions/11823): Langfuse not working
- [Discussion #11514](https://github.com/orgs/langfuse/discussions/11514): Add the ability to store traces locally instead of sending them to the backend
- [Discussion #11337](https://github.com/orgs/langfuse/discussions/11337): Self host Langfuse for prompt management only

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (441 occurrences)
- `ioredis` (16 occurrences)
