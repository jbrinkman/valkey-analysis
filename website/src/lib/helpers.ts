import type { RepoEntry } from '../types/index.ts';

/**
 * Formats an array of use case strings as a comma-separated list.
 * Returns "—" for empty arrays.
 */
export function formatUseCases(useCases: string[]): string {
  if (useCases.length === 0) {
    return '—';
  }
  return useCases.join(', ');
}

/**
 * Generates a URL slug from an owner and repository name.
 * Returns the format `{owner}/{repoName}`.
 */
export function generateSlug(owner: string, repoName: string): string {
  return `${owner}/${repoName}`;
}

/**
 * Filters repositories by Valkey support status.
 * Returns all repositories when status is "all".
 */
export function filterRepos(repos: RepoEntry[], status: string): RepoEntry[] {
  if (status === 'all') {
    return repos;
  }
  return repos.filter((repo) => repo.valkey_support === status);
}
