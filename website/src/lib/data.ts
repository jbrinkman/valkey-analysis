import fs from 'node:fs';
import path from 'node:path';
import { marked } from 'marked';
import type {
  ResultsData,
  ResultsMetadata,
  ResultsSummary,
  RepoEntry,
} from '../types/index.ts';

import resultsData from '../../results/results.json';

const data = resultsData as ResultsData;

export function getAllRepos(): RepoEntry[] {
  return data.repos;
}

export function getSummary(): ResultsSummary {
  return data.summary;
}

export function getMetadata(): ResultsMetadata {
  return data.metadata;
}

export function getRepoBySlug(
  owner: string,
  repoName: string,
): RepoEntry | undefined {
  return data.repos.find(
    (r) => r.owner === owner && r.repo_name === repoName,
  );
}

export async function getReportHtml(
  owner: string,
  repoName: string,
): Promise<string> {
  const reportPath = path.resolve(
    process.cwd(),
    '..',
    'reports',
    `${owner}__${repoName}.md`,
  );
  const markdown = fs.readFileSync(reportPath, 'utf-8');
  return marked(markdown);
}
