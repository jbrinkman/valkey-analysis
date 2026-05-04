import { describe, it, expect } from 'vitest';
import { getAllRepos, getSummary, getRepoBySlug } from './data.ts';
import { formatUseCases, filterRepos } from './helpers.ts';

describe('Data Layer', () => {
  describe('getAllRepos()', () => {
    it('returns an array of 899 repos', () => {
      const repos = getAllRepos();
      expect(Array.isArray(repos)).toBe(true);
      expect(repos.length).toBe(899);
    });

    it('every repo has required fields', () => {
      const repos = getAllRepos();
      for (const repo of repos) {
        expect(repo).toHaveProperty('repo_name');
        expect(repo).toHaveProperty('owner');
        expect(repo).toHaveProperty('github_url');
        expect(repo).toHaveProperty('valkey_support');
        expect(repo).toHaveProperty('integration_details');
      }
    });

    it('contains known repos from the dataset', () => {
      const repos = getAllRepos();
      const n8n = repos.find(
        (r) => r.owner === 'n8n-io' && r.repo_name === 'n8n',
      );
      expect(n8n).toBeDefined();
      expect(n8n!.valkey_support).toBe('explicit');
    });
  });

  describe('getSummary()', () => {
    it('returns the expected summary object', () => {
      const summary = getSummary();
      expect(summary.total_repos).toBe(899);
      expect(summary.valkey_support).toEqual({
        explicit: 100,
        implied: 120,
        none: 679,
      });
      expect(summary.valkey_search_support).toEqual({
        explicit: 0,
        implied: 0,
        none: 899,
      });
      expect(summary.valkey_glide_used).toBe(2);
      expect(summary.redisearch_usage).toBe(21);
      expect(summary.reports_generated).toBe(899);
    });
  });

  describe('getRepoBySlug()', () => {
    it('returns the correct repo for a known explicit-support pair', () => {
      const repo = getRepoBySlug('n8n-io', 'n8n');
      expect(repo).toBeDefined();
      expect(repo!.owner).toBe('n8n-io');
      expect(repo!.repo_name).toBe('n8n');
      expect(repo!.valkey_support).toBe('explicit');
      expect(repo!.stars).toBe(186290);
    });

    it('returns the correct repo for a known implied-support pair', () => {
      const repo = getRepoBySlug('vinta', 'awesome-python');
      expect(repo).toBeDefined();
      expect(repo!.owner).toBe('vinta');
      expect(repo!.repo_name).toBe('awesome-python');
      expect(repo!.valkey_support).toBe('implied');
    });

    it('returns the correct repo for a known none-support pair', () => {
      const repo = getRepoBySlug('sindresorhus', 'awesome');
      expect(repo).toBeDefined();
      expect(repo!.owner).toBe('sindresorhus');
      expect(repo!.repo_name).toBe('awesome');
      expect(repo!.valkey_support).toBe('none');
    });

    it('returns undefined for a non-existent owner/repo pair', () => {
      const repo = getRepoBySlug('nonexistent-owner', 'nonexistent-repo');
      expect(repo).toBeUndefined();
    });

    it('returns undefined when owner matches but repo does not', () => {
      const repo = getRepoBySlug('n8n-io', 'nonexistent-repo');
      expect(repo).toBeUndefined();
    });
  });
});

describe('Helpers', () => {
  describe('formatUseCases()', () => {
    it('formats a known use case array as comma-separated string', () => {
      const result = formatUseCases(['time_series', 'vector_store']);
      expect(result).toBe('time_series, vector_store');
    });

    it('formats a single-element array without comma', () => {
      const result = formatUseCases(['cache']);
      expect(result).toBe('cache');
    });

    it('returns "—" for an empty array', () => {
      const result = formatUseCases([]);
      expect(result).toBe('—');
    });
  });

  describe('filterRepos()', () => {
    const repos = getAllRepos();

    it('returns all repos when status is "all"', () => {
      const filtered = filterRepos(repos, 'all');
      expect(filtered.length).toBe(899);
      expect(filtered).toBe(repos);
    });

    it('returns only explicit repos when status is "explicit"', () => {
      const filtered = filterRepos(repos, 'explicit');
      expect(filtered.length).toBe(100);
      for (const repo of filtered) {
        expect(repo.valkey_support).toBe('explicit');
      }
    });

    it('returns only implied repos when status is "implied"', () => {
      const filtered = filterRepos(repos, 'implied');
      expect(filtered.length).toBe(120);
      for (const repo of filtered) {
        expect(repo.valkey_support).toBe('implied');
      }
    });

    it('returns only none repos when status is "none"', () => {
      const filtered = filterRepos(repos, 'none');
      expect(filtered.length).toBe(679);
      for (const repo of filtered) {
        expect(repo.valkey_support).toBe('none');
      }
    });
  });
});
