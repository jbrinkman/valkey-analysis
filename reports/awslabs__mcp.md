# Valkey Integration Analysis: awslabs/mcp

**GitHub:** https://github.com/awslabs/mcp
**Analyzed:** 2026-05-02T01:40:32.719194+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 15 related issue(s)/PR(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisgraph.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** cache, memory
- **Integration Type:** none
- **Redis Modules:** redisgraph

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

**Valkey mentions in README:**
- `valkey` (28 occurrences)
  - Line 232: `| [Amazon ElastiCache / MemoryDB for Valkey MCP Server](src/valkey-mcp-server) | Advanced data structures and caching with Valkey | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=f`
  - Line 386: `| [Amazon ElastiCache / MemoryDB for Valkey MCP Server](src/valkey-mcp-server) | Advanced data structures and caching with Valkey | [![Install](https://img.shields.io/badge/Install-Kiro-9046FF?style=f`
  - Line 447: `For example, you can use the **AWS Documentation MCP Server** to help your AI assistant research and generate up-to-date code for any AWS service, like Amazon Bedrock Inline agents. Alternatively, you`

**Redis mentions in README:**
- `redis` (1 occurrences)

**Valkey mentions in docs:**
- https://awslabs.github.io/mcp/

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 65 file(s)
  - [docusaurus/docs/servers/valkey-mcp-server.md](https://github.com/awslabs/mcp/blob/8aef8704c70f684c0dc7c1ece2409b7c5a99d9f5/docusaurus/docs/servers/valkey-mcp-server.md)
  - [src/valkey-mcp-server/README.md](https://github.com/awslabs/mcp/blob/8aef8704c70f684c0dc7c1ece2409b7c5a99d9f5/src/valkey-mcp-server/README.md)
  - [src/valkey-mcp-server/NOTICE](https://github.com/awslabs/mcp/blob/8aef8704c70f684c0dc7c1ece2409b7c5a99d9f5/src/valkey-mcp-server/NOTICE)

**Redis module code references:**
- `redisgraph` / `graph.query`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #2884](https://github.com/awslabs/mcp/issues/2884): Security scan: valkey-mcp-server scored 0/100 (F) with 2 CRITICALs across 105 tools (open)
- [ISSUE #424](https://github.com/awslabs/mcp/issues/424): ElastiCache for Valkey, DocumentDB, RDS: Support for accessing private subnet nodes (closed)
- [ISSUE #290](https://github.com/awslabs/mcp/issues/290): RFC: Amazon ElastiCache/MemoryDB Valkey MCP Server (closed)
- [PR #3276](https://github.com/awslabs/mcp/pull/3276): feat(valkey-mcp-server): V2 — GLIDE migration, Focused Search + JSON + Command Runner Tools (open)
- [PR #1862](https://github.com/awslabs/mcp/pull/1862): feat(api): VSS and Semantic Search MCPs for Valkey (closed)
- [PR #3167](https://github.com/awslabs/mcp/pull/3167): chore(deps): update docker images: bump the docker-version-updates group across 50 directories with 1 update (closed)
- [PR #2652](https://github.com/awslabs/mcp/pull/2652): chore(deps): update docker images: bump the docker-version-updates group across 52 directories with 1 update (closed)
- [PR #3041](https://github.com/awslabs/mcp/pull/3041): chore(deps): update uv: bump pytest from 8.3.5 to 9.0.3 in /src/valkey-mcp-server (open)
- [PR #3231](https://github.com/awslabs/mcp/pull/3231): chore(deps): update uv: bump python-dotenv from 1.1.0 to 1.2.2 in /src/valkey-mcp-server (open)
- [PR #3196](https://github.com/awslabs/mcp/pull/3196): chore: release/2026.04.20260421081720 (closed)
- [PR #2715](https://github.com/awslabs/mcp/pull/2715): chore(deps): update docker images: bump the docker-version-updates group across 51 directories with 1 update (closed)
- [PR #2999](https://github.com/awslabs/mcp/pull/2999): chore(deps): update uv: bump uv from 0.9.24 to 0.11.6 in /src/valkey-mcp-server (closed)
- [PR #3180](https://github.com/awslabs/mcp/pull/3180): chore(deps): update docker images: bump the docker-version-updates group across 42 directories with 1 update (closed)
- [PR #1830](https://github.com/awslabs/mcp/pull/1830): feat(api): Introduce VSS MCP tool (closed)
- [PR #291](https://github.com/awslabs/mcp/pull/291): feat(server): Amazon ElastiCache/MemoryDB Valkey MCP Server (closed)

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [aws-powershell-extensions](https://github.com/awslabs/aws-powershell-extensions): The extensions for AWS Tools for PowerShell provide workflow enhancements on top of the core AWSPowerShell module.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (51 occurrences)
  - `src/valkey-mcp-server/ELASTICACHECONNECT.md`
  - `Used by:  postgres-mcp-server  (PostgreSQL wire protocol),  valkey-mcp-server  (RESP3 protocol)`
  - `Sources:       .github/CODEOWNERS  1-95         README.md  60-82                   Dismiss   Refresh this wiki  Enter email to refresh    On this page    Overview    Purpose and Scope    Model Context`

**Redis mentions:** 1 keyword(s) found
- `redis` (6 occurrences)
