# Valkey Integration Analysis: PostHog/posthog

**GitHub:** https://github.com/PostHog/posthog
**Analyzed:** 2026-05-02T01:40:32.682767+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 2 related issue(s)/PR(s) found. 6 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, package.json

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [frontend/src/lib/components/IntervalFilter/intervals.ts](https://github.com/PostHog/posthog/blob/a72cf32c9da6196e587956d58763e47676c486d5/frontend/src/lib/components/IntervalFilter/intervals.ts)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 44 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #43538](https://github.com/PostHog/posthog/pull/43538): feat: increment issue buckets in cymbal (closed)
- [PR #47936](https://github.com/PostHog/posthog/pull/47936): feat: migrate query cache to dedicated cluster (closed)

## Phase 5: Ecosystem

**Related repos in org (320 total org repos):**
- [plugin-contrib](https://github.com/PostHog/plugin-contrib): Contributed utilities for plugin authors
- [contributions-bot](https://github.com/PostHog/contributions-bot): A bot for automating the handling of open source contributions to PostHog.
- [integrations-repository](https://github.com/PostHog/integrations-repository): A repository for hosting a list of PostHog integrations, both official and community ones.
- [raycast-extensions](https://github.com/PostHog/raycast-extensions): Everything you need to extend Raycast.
- [claude-plugins-official](https://github.com/PostHog/claude-plugins-official): Official, Anthropic-managed directory of high quality Claude Code Plugins.
- [community-extensions](https://github.com/PostHog/community-extensions): None

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (124 occurrences)
- `ioredis` (1 occurrences)
- `go-redis` (1 occurrences)
