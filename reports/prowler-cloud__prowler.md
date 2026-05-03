# Valkey Integration Analysis: prowler-cloud/prowler

**GitHub:** https://github.com/prowler-cloud/prowler
**Analyzed:** 2026-05-02T01:40:32.838086+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. 22 related issue(s)/PR(s) found. 2 related discussion(s) found. Redis modules used: redisearch, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

**Valkey mentions in README:**
- `valkey` (1 occurrences)
  - Line 192: `docker compose up postgres valkey -d`

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 29 file(s)
  - [contrib/k8s/helm/prowler-app/templates/api/secret-valkey.yaml](https://github.com/prowler-cloud/prowler/blob/8db3a896697e3e5d79b8f5cef1c885a3f5f5b954/contrib/k8s/helm/prowler-app/templates/api/secret-valkey.yaml)
  - [api/README.md](https://github.com/prowler-cloud/prowler/blob/8db3a896697e3e5d79b8f5cef1c885a3f5f5b954/api/README.md)
  - [Makefile](https://github.com/prowler-cloud/prowler/blob/8db3a896697e3e5d79b8f5cef1c885a3f5f5b954/Makefile)

**Redis module code references:**
- `redisearch` / `ft.search`: 1 file(s)
- `redistimeseries` / `ts.add`: 8 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #10179](https://github.com/prowler-cloud/prowler/issues/10179): Network error or server unreachable (closed)
- [ISSUE #10225](https://github.com/prowler-cloud/prowler/issues/10225): UI 1st scan always stuck on the same place (aws codeartifact) (closed)
- [ISSUE #8832](https://github.com/prowler-cloud/prowler/issues/8832): Allow the connection scheme (redis or rediss) to be defined using an environment variable to support ElastiCache with Valkey and SSL. (closed)
- [ISSUE #7747](https://github.com/prowler-cloud/prowler/issues/7747): [via ECS] ALB has no health checks when trying to access the UI & Public IP not showing UI either (closed)
- [ISSUE #9337](https://github.com/prowler-cloud/prowler/issues/9337): Dashboard ,Complaince No data ! (closed)
- [ISSUE #9947](https://github.com/prowler-cloud/prowler/issues/9947): Can't Sign-Up: Network error or server is unreachable (closed)
- [ISSUE #9171](https://github.com/prowler-cloud/prowler/issues/9171): On clean OS install, user can sign up, but not log in. (closed)
- [ISSUE #10024](https://github.com/prowler-cloud/prowler/issues/10024): SAML SSO: Creating user without role causes frontend to crash / Edit user modal to freeze and blocks SSO login (closed)
- [ISSUE #8794](https://github.com/prowler-cloud/prowler/issues/8794): Permanent prowler-api hostname (closed)
- [ISSUE #6689](https://github.com/prowler-cloud/prowler/issues/6689): Build prowler container images for arm64 architecture as well (closed)
- [PR #10677](https://github.com/prowler-cloud/prowler/pull/10677): feat(api): Cloud Foundry deployment with UAA authentication (open)
- [PR #10729](https://github.com/prowler-cloud/prowler/pull/10729): perf(attack-paths): cleanup task prioritization, restore default batch sizes to 1000, upgrade Cartography to 0.135.0 (closed)
- [PR #10603](https://github.com/prowler-cloud/prowler/pull/10603): fix(beat): make it dependant from API service (closed)
- [PR #10420](https://github.com/prowler-cloud/prowler/pull/10420): feat(celery): `VALKEY_SCHEME` environment variable (closed)
- [PR #9835](https://github.com/prowler-cloud/prowler/pull/9835): feat(app): Helm chart for deploying prowler in k8s (closed)
- [PR #8207](https://github.com/prowler-cloud/prowler/pull/8207): feat: Add Lighthouse recommendations and caching (closed)
- [PR #8308](https://github.com/prowler-cloud/prowler/pull/8308): feat(api & ui): prwlr-7478 api key (closed)
- [PR #5909](https://github.com/prowler-cloud/prowler/pull/5909): feat(docker-compose): add Docker Compose YAMLs and `.env` (closed)
- [PR #5342](https://github.com/prowler-cloud/prowler/pull/5342): chore(deps): bump botocore from 1.35.35 to 1.35.36 (closed)
- [PR #10693](https://github.com/prowler-cloud/prowler/pull/10693): fix(api): self-heal finding-group summaries on /latest drift (open)
- [ISSUE #9919](https://github.com/prowler-cloud/prowler/issues/9919): Jira Integration Fails with INVALID_INPUT Error for Specific Findings (closed)
- [ISSUE #9011](https://github.com/prowler-cloud/prowler/issues/9011): Prowler UI login not working when hosted on AWS ECS (Fargate with awsvpc network mode) (closed)

**Discussions:**
- [Discussion #8039](https://github.com/prowler-cloud/prowler/discussions/8039): Locally running Prowler app on docker compose unable to locate credentials
- [Discussion #6017](https://github.com/prowler-cloud/prowler/discussions/6017): Prowler-App Login Error 502 Bad Gateway on Kubernetes

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (36 occurrences)
  - `Full Stack (App) : Deployed via Docker Compose, which orchestrates the API, UI, Postgres, Valkey, and Neo4j services.`
  - `Sources:       README.md  20-24         README.md  76-81         prowler/lib/cli/parser.py  91-92                   Dismiss   Refresh this wiki  Enter email to refresh    On this page    Overview    S`

**Redis mentions:** 1 keyword(s) found
- `redis` (4 occurrences)
