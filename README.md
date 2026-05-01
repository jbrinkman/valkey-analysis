# Valkey Integration Analysis

Automated analysis of 899 AI/LLM agent framework repos to determine Valkey and Valkey-Search integration support levels with evidence-backed conclusions.

## Overview

This project scans GitHub repositories for signals of Valkey and Redis integration, classifying each as:
- **Explicit** — Direct Valkey client library usage or documentation
- **Implied** — Redis compatibility that could work with Valkey
- **None** — No evidence found

## Setup

1. Copy `example.env` to `.env` and add your GitHub PAT:
   ```
   cp example.env .env
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Phases

| Phase | Script | Description |
|-------|--------|-------------|
| 1 | `phase1_dependencies.py` | Scan package manifests for Valkey/Redis client libraries |
| 2 | `phase2_documentation.py` | Scan README and docs sites for keyword mentions |
| 3 | `phase3_code_search.py` | GitHub code search for Valkey/Redis references |
| 4 | `phase4_community_signals.py` | Search issues, PRs, discussions, and wiki |
| 5 | `phase5_ecosystem.py` | Check org repos for community extensions/plugins |
| 6 | `phase6_synthesize.py` | Deep dive with DeepWiki + evidence synthesis |
| 7 | `phase7_assemble.py` | Assemble final results.json and per-project reports |

## Output

- `results/results.json` — Dashboard-consumable JSON
- `reports/{owner}__{repo}.md` — Detailed evidence report per project

## Classification Rules

- **Explicit Valkey**: Direct Valkey client library in dependencies, OR Valkey mentioned in code/docs as a supported backend
- **Explicit Valkey-Search**: Direct Valkey-Search references in code or docs
- **Implied Valkey**: Redis client library used with configurable connection, AND use case compatible with Valkey core
- **Implied Valkey-Search**: NOT automatically inferred from RediSearch — requires evidence of abstraction layer
- **None**: No evidence, or ambiguous evidence only

RediSearch usage is flagged separately and does not imply Valkey-Search compatibility.
TimeSeries module usage is flagged but does not imply Valkey compatibility.
