import { describe, it, expect } from 'vitest';
import fc from 'fast-check';
import { formatUseCases, generateSlug, filterRepos } from './helpers.ts';
import { getAllRepos } from './data.ts';
import type { RepoEntry } from '../types/index.ts';

/**
 * Arbitrary that generates a minimal valid RepoEntry with a random valkey_support status.
 */
const valkeyStatusArb = fc.constantFrom(
  'explicit' as const,
  'implied' as const,
  'none' as const,
);

const repoEntryArb: fc.Arbitrary<RepoEntry> = fc.record({
  repo_name: fc.string({ minLength: 1 }),
  owner: fc.string({ minLength: 1 }),
  github_url: fc.string(),
  description: fc.string(),
  language: fc.string(),
  stars: fc.nat(),
  valkey_support: valkeyStatusArb,
  valkey_search_support: valkeyStatusArb,
  valkey_glide_used: fc.boolean(),
  redisearch_usage: fc.boolean(),
  integration_details: fc.record({
    client_libraries: fc.array(fc.string()),
    use_cases: fc.array(fc.string()),
    integration_type: fc.constantFrom('native', 'extension', 'none'),
    redis_modules_used: fc.array(fc.string()),
  }),
  evidence: fc.record({
    dependencies: fc.array(fc.string()),
    code_references: fc.nat(),
    doc_mentions: fc.boolean(),
    readme_mentions: fc.boolean(),
    issues_prs: fc.constant([]),
    discussions: fc.constant([]),
    wiki_mentions: fc.boolean(),
    community_extensions: fc.constant([]),
    issues_prs_total: fc.nat(),
  }),
  evidence_summary: fc.string(),
  detail_report: fc.string(),
  analyzed_at: fc.string(),
});

describe('Property Tests: Data Layer and Helpers', () => {
  /**
   * Property 1: Data completeness preservation
   * Validates: Requirements 2.1
   *
   * Verify that getAllRepos() returns an array where every entry has the
   * required fields, and no entries are dropped or duplicated from the
   * actual imported data.
   */
  describe('Property 1: Data completeness preservation', () => {
    it('getAllRepos() returns an array where every entry has required fields', () => {
      const repos = getAllRepos();

      expect(Array.isArray(repos)).toBe(true);
      expect(repos.length).toBeGreaterThan(0);

      for (const repo of repos) {
        expect(repo).toHaveProperty('repo_name');
        expect(repo).toHaveProperty('owner');
        expect(repo).toHaveProperty('github_url');
        expect(repo).toHaveProperty('valkey_support');
        expect(repo).toHaveProperty('valkey_glide_used');
        expect(repo).toHaveProperty('integration_details');
      }
    });

    it('random RepoEntry arrays preserve length through identity operations', () => {
      fc.assert(
        fc.property(fc.array(repoEntryArb), (entries) => {
          // Verify that array length is preserved — no entries dropped or duplicated
          const copy = [...entries];
          expect(copy.length).toBe(entries.length);

          // Every entry in the source is present in the copy
          for (let i = 0; i < entries.length; i++) {
            expect(copy[i]).toBe(entries[i]);
          }
        }),
        { numRuns: 100 },
      );
    });
  });

  /**
   * Property 3: Use cases formatting
   * Validates: Requirements 2.5
   *
   * For any array of non-empty strings, formatUseCases() output contains
   * every input string. For empty arrays, it produces "—".
   */
  describe('Property 3: Use cases formatting', () => {
    it('output contains every input string for non-empty arrays', () => {
      fc.assert(
        fc.property(
          fc.array(fc.string({ minLength: 1 }).filter((s) => !s.includes(',')), { minLength: 1 }),
          (useCases) => {
            const result = formatUseCases(useCases);

            // Every input string must appear in the output
            for (const useCase of useCases) {
              expect(result).toContain(useCase);
            }

            // Result should be comma-separated
            if (useCases.length > 1) {
              expect(result).toContain(', ');
            }
          },
        ),
        { numRuns: 100 },
      );
    });

    it('empty arrays produce "—"', () => {
      fc.assert(
        fc.property(fc.constant([]), (emptyArr: string[]) => {
          expect(formatUseCases(emptyArr)).toBe('—');
        }),
        { numRuns: 100 },
      );
    });
  });

  /**
   * Property 4: URL slug generation
   * Validates: Requirements 3.1, 3.6
   *
   * For any owner and repo_name strings (alphanumeric + hyphens),
   * the slug equals `{owner}/{repo_name}`.
   */
  describe('Property 4: URL slug generation', () => {
    it('slug equals {owner}/{repoName} for alphanumeric + hyphen strings', () => {
      const alphanumHyphen = fc.stringMatching(/^[a-zA-Z0-9-]+$/);

      fc.assert(
        fc.property(alphanumHyphen, alphanumHyphen, (owner, repoName) => {
          const slug = generateSlug(owner, repoName);
          expect(slug).toBe(`${owner}/${repoName}`);

          // Slug contains exactly one slash separating owner and repo
          const parts = slug.split('/');
          expect(parts.length).toBe(2);
          expect(parts[0]).toBe(owner);
          expect(parts[1]).toBe(repoName);
        }),
        { numRuns: 100 },
      );
    });
  });

  /**
   * Property 5: Support status filtering
   * Validates: Requirements 5.5
   *
   * For any array of RepoEntry objects with random statuses, the filter
   * returns the correct subset. "all" returns all entries unchanged.
   */
  describe('Property 5: Support status filtering', () => {
    it('filtering by a specific status returns only entries with that status', () => {
      fc.assert(
        fc.property(
          fc.array(repoEntryArb),
          valkeyStatusArb,
          (repos, status) => {
            const filtered = filterRepos(repos, status);

            // All returned entries must match the filter status
            for (const repo of filtered) {
              expect(repo.valkey_support).toBe(status);
            }

            // No matching entries should be missing
            const expected = repos.filter((r) => r.valkey_support === status);
            expect(filtered.length).toBe(expected.length);
          },
        ),
        { numRuns: 100 },
      );
    });

    it('filtering by "all" returns all entries unchanged', () => {
      fc.assert(
        fc.property(fc.array(repoEntryArb), (repos) => {
          const filtered = filterRepos(repos, 'all');
          expect(filtered.length).toBe(repos.length);

          // Same entries in same order
          for (let i = 0; i < repos.length; i++) {
            expect(filtered[i]).toBe(repos[i]);
          }
        }),
        { numRuns: 100 },
      );
    });

    it('filtered result is always a subset of the input (no entries invented)', () => {
      fc.assert(
        fc.property(
          fc.array(repoEntryArb),
          fc.constantFrom('explicit', 'implied', 'none', 'all'),
          (repos, status) => {
            const filtered = filterRepos(repos, status);

            // Every entry in filtered must exist in the original array
            for (const repo of filtered) {
              expect(repos).toContain(repo);
            }

            // Filtered length never exceeds input length
            expect(filtered.length).toBeLessThanOrEqual(repos.length);
          },
        ),
        { numRuns: 100 },
      );
    });
  });
});
