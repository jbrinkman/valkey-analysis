# Valkey Integration Analysis: 9001/copyparty

**GitHub:** https://github.com/9001/copyparty
**Analyzed:** 2026-05-02T01:40:32.409118+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, setup.py

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 3 file(s)
  - [docs/examples/docker/idp-authelia-traefik/README.md](https://github.com/9001/copyparty/blob/6e25d648a900f65a4546a1b17a9761c0f1e9e3cb/docs/examples/docker/idp-authelia-traefik/README.md)
  - [docs/examples/docker/idp-authelia-traefik/docker-compose.yml](https://github.com/9001/copyparty/blob/6e25d648a900f65a4546a1b17a9761c0f1e9e3cb/docs/examples/docker/idp-authelia-traefik/docker-compose.yml)
  - [docs/examples/docker/idp-authelia-traefik/authelia/configuration.yml](https://github.com/9001/copyparty/blob/6e25d648a900f65a4546a1b17a9761c0f1e9e3cb/docs/examples/docker/idp-authelia-traefik/authelia/configuration.yml)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #377](https://github.com/9001/copyparty/pull/377): chore: updated authelia docker-compose.yml (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
