# Implementation Plan: Valkey Analysis Dashboard

## Overview

Build a static Astro website in the `website/` subdirectory that reads pre-generated analysis data (`results/results.json` and `reports/*.md`) and produces a landing page with filterable project list, summary statistics, and 899 detail pages — one per analyzed repository. The site supports light/dark/system themes, deploys to GitHub Pages via GitHub Actions, and uses a Taskfile for developer workflows.

## Tasks

- [x] 1. Scaffold Astro project and configure build tooling
  - [x] 1.1 Initialize Astro project in `website/` directory
    - Run `npm create astro@latest` in `website/` with an empty template, targeting **Astro 6.x**
    - Configure `astro.config.mjs` with `site` set to `https://jbrinkman.github.io`, `base` set to `/valkey-analysis` (matching the repo name), and `output: 'static'`
    - Verify `package.json` has `astro` pinned to `^6.0.0` (reject any 5.x or 4.x version)
    - Add `marked` as a dependency for markdown rendering
    - Add `vitest` and `fast-check` as dev dependencies for testing
    - Configure `tsconfig.json` with strict mode enabled
    - _Requirements: 1.1, 1.3, 8.3_

  - [x] 1.2 Create Taskfile.yml at workspace root
    - Define `install` task: `npm install` with `dir: website`
    - Define `dev` task: `npm run dev` with `dir: website`
    - Define `build` task: `npm run build` with `dir: website`
    - Define `preview` task: `npm run preview` with `dir: website`
    - Define `clean` task: `rm -rf dist .astro` with `dir: website`
    - Include `desc` field for every task
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8_

  - [x] 1.3 Configure Vitest for the Astro project
    - Add a `vitest.config.ts` in `website/` with TypeScript support
    - Add a `test` script to `package.json`
    - Verify Vitest runs with a trivial placeholder test
    - _Requirements: (testing infrastructure)_

- [x] 2. Checkpoint - Verify project scaffolding
  - Ensure `task install` succeeds, `task build` produces output, and Vitest runs. Ask the user if questions arise.

- [x] 3. Define TypeScript types and implement data layer
  - [x] 3.1 Create TypeScript interfaces in `src/types/index.ts`
    - Define `ResultsData`, `ResultsMetadata`, `ResultsSummary`, `RepoEntry`, `IntegrationDetails`, `Evidence`, `IssuePr`, and `CommunityExtension` interfaces matching the `results/results.json` schema
    - Export all types for use across the project
    - _Requirements: 1.1, 2.1, 2.2_

  - [x] 3.2 Implement data loading module in `src/lib/data.ts`
    - Import `results/results.json` using a relative path (`../../results/results.json`)
    - Implement `getAllRepos()` returning typed `RepoEntry[]`
    - Implement `getSummary()` returning typed `ResultsSummary`
    - Implement `getMetadata()` returning typed `ResultsMetadata`
    - Implement `getRepoBySlug(owner, repoName)` returning `RepoEntry | undefined`
    - Implement `getReportHtml(owner, repoName)` that reads the markdown file from `../../reports/{owner}__{repoName}.md` and converts to HTML via `marked`
    - _Requirements: 1.1, 1.2, 1.4, 3.4_

  - [x] 3.3 Implement helper utilities in `src/lib/helpers.ts`
    - Implement `formatUseCases(useCases: string[]): string` — returns comma-separated list or "—" for empty arrays
    - Implement `generateSlug(owner: string, repoName: string): string` — returns `{owner}/{repoName}`
    - Implement `filterRepos(repos: RepoEntry[], status: string): RepoEntry[]` — filters by `valkey_support` or returns all for `"all"`
    - _Requirements: 2.5, 3.6, 5.5_

  - [x] 3.4 Write property tests for data layer and helpers
    - **Property 1: Data completeness preservation** — Generate random arrays of `RepoEntry` objects, verify `getAllRepos()` returns all entries with correct count
    - **Validates: Requirements 2.1**
    - **Property 3: Use cases formatting** — Generate random arrays of non-empty strings, verify `formatUseCases()` output contains every input string; verify empty arrays produce "—"
    - **Validates: Requirements 2.5**
    - **Property 4: URL slug generation** — Generate random `owner` and `repo_name` strings, verify slug equals `{owner}/{repo_name}`
    - **Validates: Requirements 3.1, 3.6**
    - **Property 5: Support status filtering** — Generate random arrays of `RepoEntry` with random statuses, verify filter returns correct subset
    - **Validates: Requirements 5.5**

  - [x] 3.5 Write unit tests for data layer
    - Test `getAllRepos()` returns expected array from fixture data
    - Test `getSummary()` returns expected summary object
    - Test `getRepoBySlug()` returns correct repo for known pairs and `undefined` for non-existent repos
    - Test `formatUseCases()` with known arrays and empty array
    - Test `filterRepos()` with each status value and `"all"`
    - _Requirements: 2.1, 2.5, 5.5_

- [x] 4. Implement theme system
  - [x] 4.1 Implement theme logic in `src/lib/theme.ts`
    - Implement `getTheme(): string` — reads from localStorage with try/catch, defaults to `"system"`
    - Implement `setTheme(theme: string): void` — writes to localStorage with try/catch
    - Implement `resolveTheme(theme: string): "light" | "dark"` — resolves `"system"` using `prefers-color-scheme` media query, returns `"light"` or `"dark"` for explicit values
    - _Requirements: 7.1, 7.2, 7.3, 7.5, 7.6_

  - [x] 4.2 Write property test for theme persistence
    - **Property 6: Theme persistence round-trip** — Generate random valid theme values from `["light", "dark", "system"]`, verify `setTheme` then `getTheme` returns the original value; verify `resolveTheme` never returns `"system"`
    - **Validates: Requirements 7.5**

  - [x] 4.3 Write unit tests for theme logic
    - Test default theme is `"system"` when localStorage is empty
    - Test `setTheme("dark")` writes to localStorage
    - Test `resolveTheme("system")` returns correct value based on media query
    - Test `resolveTheme("light")` always returns `"light"`
    - Test localStorage errors are caught gracefully
    - _Requirements: 7.1, 7.2, 7.3, 7.5_

- [x] 5. Create global styles and CSS theme variables
  - [x] 5.1 Create `src/styles/global.css` with theme custom properties
    - Define light theme variables on `:root` and `[data-theme="light"]`
    - Define dark theme variables on `[data-theme="dark"]`
    - Include base typography, layout resets, and responsive styles
    - Style summary stat cards, table, badges, header, and navigation
    - Ensure badge colors meet WCAG 2.1 AA contrast requirements in both themes
    - _Requirements: 5.2, 6.1, 6.2, 6.3, 6.5, 7.7, 7.8, 7.9_

- [x] 6. Build base layout and shared components
  - [x] 6.1 Create `src/layouts/BaseLayout.astro`
    - Accept `title` and optional `description` props
    - Render full HTML document shell with `<head>` (meta tags, global CSS import, favicon)
    - Inject inline theme-init script before `</head>` that reads localStorage and sets `document.documentElement.dataset.theme` to prevent flash of incorrect theme
    - Include `<Header />` component
    - Render page content via `<slot />`
    - _Requirements: 5.1, 7.3, 7.6_

  - [x] 6.2 Create `src/components/Header.astro`
    - Render site title "Valkey Analysis Dashboard" with link to home
    - Include `<ThemeToggle />` component aligned right
    - Use semantic `<header>` and `<nav>` elements
    - _Requirements: 5.1, 5.4, 7.4_

  - [x] 6.3 Create `src/components/ThemeToggle.astro`
    - Render three buttons: Light ☀️, Dark 🌙, System 💻
    - Include inline `<script>` that reads current theme, highlights active button, handles click events to call `setTheme()` and update `data-theme` attribute
    - Listen to `prefers-color-scheme` media query changes to update when in system mode
    - _Requirements: 7.1, 7.4, 7.5, 7.10_

  - [x] 6.4 Create `src/components/StatusBadge.astro`
    - Accept `status` prop of type `'explicit' | 'implied' | 'none'`
    - Render `<span>` with class `badge badge--{status}` and capitalized status text
    - CSS classes map to green (explicit), amber (implied), gray (none) via custom properties
    - _Requirements: 6.1, 6.2, 6.3_

  - [x] 6.5 Write property test for StatusBadge rendering
    - **Property 2: Status badge CSS class mapping** — Generate random valid status values, verify badge output contains CSS class including the status value
    - **Validates: Requirements 2.4, 6.1, 6.2, 6.3**

  - [x] 6.6 Create `src/components/BackLink.astro`
    - Render "← Back to Project List" link pointing to base path `/valkey-analysis/`
    - Use semantic `<nav>` element
    - _Requirements: 3.5, 5.3_

- [x] 7. Checkpoint - Verify components and theme system
  - Ensure all tests pass, verify theme toggle works in both modes. Ask the user if questions arise.

- [x] 8. Implement landing page
  - [x] 8.1 Create `src/components/SummaryStats.astro`
    - Accept `summary` prop of type `ResultsSummary`
    - Render stat cards in a grid: total repos, explicit support, implied support, no support, Valkey Glide users, RediSearch users
    - Style cards with CSS custom properties for theme adaptation
    - _Requirements: 4.1, 4.2_

  - [x] 8.2 Create `src/components/ProjectTable.astro`
    - Accept `repos` prop of type `RepoEntry[]`
    - Render filter bar with buttons: All, Explicit, Implied, None
    - Render `<table>` with columns: Project (`owner/repo_name` as link), Valkey Support (via `<StatusBadge>`), Valkey Glide (✓/✗), Use Cases (via `formatUseCases`)
    - Add `data-support` attribute on each `<tr>` for filtering
    - Include inline `<script>` for client-side filtering that toggles `hidden` attribute on rows
    - Use semantic `<table>`, `<thead>`, `<tbody>` elements
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 5.4, 5.5, 6.4_

  - [x] 8.3 Create `src/pages/index.astro`
    - Import `getAllRepos()` and `getSummary()` from data layer
    - Render `<BaseLayout>` with title "Valkey Analysis Dashboard"
    - Include `<SummaryStats>` and `<ProjectTable>` components
    - Display total repository count
    - _Requirements: 1.1, 2.1, 2.3, 4.1_

- [x] 9. Implement detail pages
  - [x] 9.1 Create `src/pages/projects/[...slug].astro`
    - Implement `getStaticPaths()` that enumerates all repos and returns `{ params: { slug: '{owner}/{repo_name}' }, props: { repo } }` for each
    - Fetch report HTML via `getReportHtml(owner, repoName)`
    - Render repo metadata: project name, GitHub URL, description, language, stars
    - Render classification table: Valkey support, Valkey Search support, Valkey Glide, RediSearch usage
    - Render report HTML content using `set:html`
    - Include `<BackLink>` component
    - Wrap in `<BaseLayout>` with project-specific title
    - _Requirements: 1.2, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6_

- [x] 10. Checkpoint - Verify full site build
  - Run `task build` and verify output contains `index.html` and detail page directories. Ensure all tests pass. Ask the user if questions arise.

- [x] 11. Create GitHub Actions deployment workflow
  - [x] 11.1 Create `.github/workflows/deploy.yml`
    - Trigger on push to `main` branch
    - Set permissions for `pages: write`, `id-token: write`, `contents: read`
    - Configure concurrency group for deployments
    - Job steps: checkout, setup Node.js, install dependencies in `website/`, run `astro build` in `website/`, configure pages with `actions/configure-pages`, upload artifact with `actions/upload-pages-artifact` pointing to `website/dist`, deploy with `actions/deploy-pages`
    - Set environment to `github-pages` with URL output
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7_

- [x] 12. Final checkpoint - Full build and deployment verification
  - Run `task build` to verify the complete site builds successfully. Verify `deploy.yml` is valid YAML with correct trigger, permissions, and action references. Ensure all tests pass. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation throughout the build
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- The site is deployed to `https://jbrinkman.github.io/valkey-analysis/`
- All Astro components and source files live under `website/src/`
- Data files (`results/results.json`, `reports/*.md`) are accessed via relative paths from the `website/` directory
