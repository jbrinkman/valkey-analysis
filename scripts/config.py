"""Shared configuration for Valkey integration analysis."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"
RESULTS_DIR = PROJECT_ROOT / "results"

for d in (DATA_DIR, REPORTS_DIR, RESULTS_DIR):
    d.mkdir(exist_ok=True)

# Load .env
load_dotenv(PROJECT_ROOT / ".env")
GITHUB_PAT = os.getenv("GITHUB_PAT", "")

# API endpoints
REPOS_API_URL = "https://b3lpst6208.execute-api.us-west-2.amazonaws.com/repos"

# GitHub API
GITHUB_API_BASE = "https://api.github.com"
GITHUB_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_PAT:
    GITHUB_HEADERS["Authorization"] = f"Bearer {GITHUB_PAT}"

# Rate limiting
GITHUB_REST_RPM = 5000  # authenticated requests per hour
GITHUB_SEARCH_RPM = 30  # code search requests per minute
CONCURRENT_REQUESTS = 10

# --- Keywords ---

VALKEY_EXPLICIT_KEYWORDS = [
    "valkey",
    "valkey-py",
    "valkey-java",
    "valkey-go",
    "valkey-rb",
    "iovalkey",
    "valkey-glide",
    "valkey-search",
]

VALKEY_GLIDE_KEYWORDS = [
    "valkey-glide",
    "glide-for-redis",
    "valkey-glide-py",
    "valkey-glide-node",
    "valkey-glide-java",
    "valkey-glide-rs",
]

REDIS_KEYWORDS = [
    "redis",
    "redis-py",
    "ioredis",
    "jedis",
    "redis-rs",
    "go-redis",
    "node-redis",
    "stackexchange.redis",
    "lettuce",
    "hiredis",
    "predis",
    "phpredis",
    "aioredis",
    "redis-om",
]

REDIS_MODULE_KEYWORDS = {
    "redisearch": ["redisearch", "redis.commands.search", "ft.search", "ft.create"],
    "redistimeseries": ["redistimeseries", "redis.commands.timeseries", "ts.add", "ts.range"],
    "redisjson": ["redisjson", "redis.commands.json", "json.set", "json.get", "rejson"],
    "redisbloom": ["redisbloom", "redis.commands.bf", "bf.add", "bf.exists"],
    "redisgraph": ["redisgraph", "redis.commands.graph", "graph.query"],
    "redisai": ["redisai", "redis.commands.ai"],
}

# Redis modules with NO Valkey equivalent — their presence disqualifies implied Valkey support
VALKEY_INCOMPATIBLE_MODULES = [
    "redistimeseries",
    "redisgraph",
    "redisai",
]

# --- Dependency patterns per package manager ---

MANIFEST_FILES = [
    "requirements.txt",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "Pipfile",
    "package.json",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "Gemfile",
    "composer.json",
]

# Map of dependency names to their category
VALKEY_DEPENDENCIES = {
    # Python
    "valkey": "valkey-client",
    "valkey-py": "valkey-client",
    "valkey-glide": "valkey-glide",
    # Node.js
    "iovalkey": "valkey-client",
    "@valkey/valkey-glide": "valkey-glide",
    # Java
    "io.valkey:valkey-java": "valkey-client",
    "io.valkey:valkey-glide": "valkey-glide",
    # Go
    "github.com/valkey-io/valkey-go": "valkey-client",
    "github.com/valkey-io/valkey-glide": "valkey-glide",
    # Rust
    "valkey": "valkey-client",
}

REDIS_DEPENDENCIES = {
    # Python
    "redis": "redis-client",
    "redis-py": "redis-client",
    "aioredis": "redis-client",
    "redis-om": "redis-client",
    "redisvl": "redis-client",
    # Node.js
    "redis": "redis-client",
    "ioredis": "redis-client",
    # Java
    "redis.clients:jedis": "redis-client",
    "io.lettuce:lettuce-core": "redis-client",
    "org.redisson:redisson": "redis-client",
    # Go
    "github.com/redis/go-redis": "redis-client",
    "github.com/go-redis/redis": "redis-client",
    "github.com/gomodule/redigo": "redis-client",
    # Rust
    "redis": "redis-client",
    # PHP
    "predis/predis": "redis-client",
    # Ruby
    "redis": "redis-client",
    # .NET
    "StackExchange.Redis": "redis-client",
}

# --- Use case vocabulary ---

USE_CASES = [
    "vector_store",
    "cache",
    "memory",
    "message_broker",
    "session_store",
    "rate_limiting",
    "general_datastore",
    "time_series",
]

# --- Integration types ---

INTEGRATION_TYPES = [
    "native",
    "plugin",
    "extension",
    "configurable_backend",
    "none",
]

# --- Ecosystem search terms for Phase 5 ---

ECOSYSTEM_REPO_KEYWORDS = [
    "valkey",
    "redis",
    "integrations",
    "plugins",
    "contrib",
    "community",
    "extensions",
]

# --- DeepWiki ---

DEEPWIKI_BASE_URL = "https://deepwiki.com"

# --- OpenRouter (LLM sentiment analysis) ---

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "google/gemma-4-26b-a4b-it"
