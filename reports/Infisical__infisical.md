# Valkey Integration Analysis: Infisical/infisical

**GitHub:** https://github.com/Infisical/infisical
**Analyzed:** 2026-05-02T01:40:32.618154+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 8 file(s)
  - [docs/documentation/platform/pam/getting-started/resources/redis.mdx](https://github.com/Infisical/infisical/blob/3567c8c5d14c495d189ca5d0dff0b4731930ebb6/docs/documentation/platform/pam/getting-started/resources/redis.mdx)
  - [frontend/src/hooks/api/secretApproval/queries.tsx](https://github.com/Infisical/infisical/blob/3567c8c5d14c495d189ca5d0dff0b4731930ebb6/frontend/src/hooks/api/secretApproval/queries.tsx)
  - [frontend/src/hooks/api/secretApproval/mutation.tsx](https://github.com/Infisical/infisical/blob/3567c8c5d14c495d189ca5d0dff0b4731930ebb6/frontend/src/hooks/api/secretApproval/mutation.tsx)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 6 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #5133](https://github.com/Infisical/infisical/pull/5133): docs: add redis PAM document (closed)

## Phase 5: Ecosystem

**Related repos in org (70 total org repos):**
- [sigstore-kms-infisical](https://github.com/Infisical/sigstore-kms-infisical): Infisical KMS provider for Sigstore
- [community-operators](https://github.com/Infisical/community-operators): The canonical source for Kubernetes Operators that are published on OperatorHub.io and part of the default catalog of the Operator Lifecycle Manager.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (165 occurrences)
- `ioredis` (4 occurrences)
