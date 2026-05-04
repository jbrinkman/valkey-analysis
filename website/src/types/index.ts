/** Top-level structure of results/results.json */
export interface ResultsData {
  metadata: ResultsMetadata;
  summary: ResultsSummary;
  repos: RepoEntry[];
}

export interface ResultsMetadata {
  generated_at: string; // ISO 8601 timestamp
  total_repos: number;
  analysis_version: string;
}

export interface ResultsSummary {
  total_repos: number;
  valkey_support: {
    explicit: number;
    implied: number;
    none: number;
  };
  valkey_search_support: {
    explicit: number;
    implied: number;
    none: number;
  };
  valkey_glide_used: number;
  redisearch_usage: number;
  reports_generated: number;
}

export interface RepoEntry {
  repo_name: string;
  owner: string;
  github_url: string;
  description: string;
  language: string;
  stars: number;
  valkey_support: 'explicit' | 'implied' | 'none';
  valkey_search_support: 'explicit' | 'implied' | 'none';
  valkey_glide_used: boolean;
  redisearch_usage: boolean;
  integration_details: IntegrationDetails;
  evidence: Evidence;
  evidence_summary: string;
  detail_report: string; // e.g. "reports/n8n-io__n8n.md"
  analyzed_at: string; // ISO 8601 timestamp
}

export interface IntegrationDetails {
  client_libraries: string[];
  use_cases: string[];
  integration_type: string; // "native" | "extension" | "none"
  redis_modules_used: string[];
}

export interface Evidence {
  dependencies: string[];
  code_references: number;
  doc_mentions: boolean;
  readme_mentions: boolean;
  issues_prs: IssuePr[];
  discussions: unknown[];
  wiki_mentions: boolean;
  community_extensions: CommunityExtension[];
  issues_prs_total: number;
}

export interface IssuePr {
  type: 'issue' | 'pr';
  number: number;
  title: string;
  state: string;
  url: string;
  created_at: string;
  updated_at: string;
  labels: string[];
  search_term: string;
}

export interface CommunityExtension {
  repo_url: string;
  description: string | null;
  valkey_mentioned: boolean;
  redis_mentioned: boolean;
}
