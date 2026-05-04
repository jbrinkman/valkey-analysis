# Valkey Integration Analysis: n8n-io/n8n

**GitHub:** https://github.com/n8n-io/n8n
**Analyzed:** 2026-05-04T12:56:14.012601+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **implied** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Implied Valkey compatibility via Redis integration. 7 related issue(s)/PR(s) found (2 negative, 5 neutral). 1 related extension repo(s) found (0 mention Valkey).

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** None detected
- **Integration Type:** extension
- **Redis Modules:** None detected

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ➖ [ISSUE #27753](https://github.com/n8n-io/n8n/issues/27753): Redis connection sometimes not recovered (closed) — _The text discusses a Redis connection issue and does not mention Valkey or its support status._
- ➖ [ISSUE #26144](https://github.com/n8n-io/n8n/issues/26144): n8n pods restart after a valkey rolling update (closed) — _The text describes an operational issue regarding pod restarts during an update, not the project's level of support or integration for Valkey._
- ⛔ [ISSUE #21361](https://github.com/n8n-io/n8n/issues/21361): Redis Vector Store node incompatible with AWS ElastiCache Valkey - TEXT field not supported (closed) — _The text explicitly states that the node is incompatible with AWS ElastiCache Valkey due to a lack of support for the TEXT field._
- ➖ [ISSUE #20906](https://github.com/n8n-io/n8n/issues/20906): worker http server not listening on 5679 (closed) — _The text describes a technical issue with an HTTP server port and does not mention Valkey or its support status._
- ⛔ [ISSUE #16590](https://github.com/n8n-io/n8n/issues/16590): Bug: AWS ElastiCache Serverless not supported (closed) — _The text explicitly states that a specific Valkey-compatible service (AWS ElastiCache Serverless) is not supported._
- ➖ [PR #16592](https://github.com/n8n-io/n8n/pull/16592): fix(Redis): Allow for using AWS ElastiCache Serverless in Queue Mode (closed) — _The text mentions Redis and AWS ElastiCache, but there is no mention of Valkey._
- ➖ [PR #16591](https://github.com/n8n-io/n8n/pull/16591): fix(Redis): Allow for using AWS ElastiCache Serverless in Queue Mode (closed) — _The text mentions Redis and AWS ElastiCache, but there is no mention of Valkey._

## Phase 5: Ecosystem

**Related repos in org (40 total org repos):**
- [terraform-azurerm-avm-res-cache-redis](https://github.com/n8n-io/terraform-azurerm-avm-res-cache-redis): None 🔴 Redis

## Sentiment Analysis

**7 Valkey mention(s) analyzed:** 0 positive, 2 negative, 5 neutral

-  **[issue_pr]** "Redis Vector Store node incompatible with AWS ElastiCache Valkey - TEXT field not supported"
  - Reason: The text explicitly states that the node is incompatible with AWS ElastiCache Valkey due to a lack of support for the TEXT field.
-  **[issue_pr]** "Bug: AWS ElastiCache Serverless not supported"
  - Reason: The text explicitly states that a specific Valkey-compatible service (AWS ElastiCache Serverless) is not supported.
-  **[issue_pr]** "Redis connection sometimes not recovered"
  - Reason: The text discusses a Redis connection issue and does not mention Valkey or its support status.
-  **[issue_pr]** "n8n pods restart after a valkey rolling update"
  - Reason: The text describes an operational issue regarding pod restarts during an update, not the project's level of support or integration for Valkey.
-  **[issue_pr]** "worker http server not listening on 5679"
  - Reason: The text describes a technical issue with an HTTP server port and does not mention Valkey or its support status.
-  **[issue_pr]** "fix(Redis): Allow for using AWS ElastiCache Serverless in Queue Mode"
  - Reason: The text mentions Redis and AWS ElastiCache, but does not mention Valkey or its support status.
-  **[issue_pr]** "fix(Redis): Allow for using AWS ElastiCache Serverless in Queue Mode"
  - Reason: The text mentions Redis and AWS ElastiCache, but there is no mention of Valkey.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (97 occurrences)
