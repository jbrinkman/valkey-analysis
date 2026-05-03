# Valkey Integration Analysis: rails/rails

**GitHub:** https://github.com/rails/rails
**Analyzed:** 2026-05-02T01:40:32.841420+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 2 related issue(s)/PR(s) found. 1 related discussion(s) found. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, Gemfile

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 8 file(s)
  - [railties/lib/rails/generators/rails/app/templates/github/ci.yml.tt](https://github.com/rails/rails/blob/c0eeb1fafbb3beb374c1bc17e75a8352e56abbb0/railties/lib/rails/generators/rails/app/templates/github/ci.yml.tt)
  - [.devcontainer/compose.yaml](https://github.com/rails/rails/blob/c0eeb1fafbb3beb374c1bc17e75a8352e56abbb0/.devcontainer/compose.yaml)
  - [railties/lib/rails/generators/rails/app/templates/config/deploy.yml.tt](https://github.com/rails/rails/blob/c0eeb1fafbb3beb374c1bc17e75a8352e56abbb0/railties/lib/rails/generators/rails/app/templates/config/deploy.yml.tt)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #56769](https://github.com/rails/rails/pull/56769): Bump Valkey Redis Image version to 9 (closed)
- [PR #53864](https://github.com/rails/rails/pull/53864): Switch Redis image to Valkey in rails generators and devcontainers (closed)

**Discussions:**
- [Discussion #55026](https://github.com/rails/rails/discussions/55026): Rails compatibility with Redis and Valkey

## Phase 5: Ecosystem

**Related repos in org (127 total org repos):**
- [rails-contributors](https://github.com/rails/rails-contributors): The web application that runs https://contributors.rubyonrails.org
- [kredis](https://github.com/rails/kredis): Higher-level data structures built on Redis 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (51 occurrences)
