# Requirements Document

## Introduction

A static website built with Astro that presents Valkey integration analysis data from a multi-stage research pipeline. The site reads from a pre-generated `results/results.json` file (899 repositories) and per-repo markdown reports in `reports/`. It provides a landing page with a sortable/filterable project list and a detail page per project showing the full analysis report.

## Glossary

- **Dashboard**: The Astro-based static website that presents Valkey analysis data
- **Project_List**: The landing page component that displays all analyzed repositories in a tabular format
- **Detail_Page**: A per-repository page that shows the complete analysis report for a single project
- **Results_Data**: The JSON file at `results/results.json` containing metadata, summary statistics, and an array of 899 repository analysis objects
- **Report_File**: A markdown file in the `reports/` directory named `{owner}__{repo_name}.md` containing the detailed multi-phase analysis for a single repository
- **Valkey_Support_Status**: A classification value of "explicit", "implied", or "none" indicating the level of Valkey compatibility detected for a repository
- **Valkey_Glide_Status**: A boolean indicating whether a repository uses the Valkey Glide client library
- **Use_Cases**: An array of detected integration use cases for a repository (e.g., "time_series", "vector_store")
- **Build_Process**: The Astro static site generation step that reads source data and produces deployable HTML/CSS/JS files
- **Color_Mode**: The active visual theme of the Dashboard, one of "light", "dark", or "system" (auto-detect from OS preference)
- **Theme_Toggle**: A persistent UI control displayed on every page that allows the user to switch between the three supported Color_Mode values
- **Deployment_Workflow**: A GitHub Actions workflow file (`.github/workflows/deploy.yml`) that builds the Astro site and deploys the output to GitHub Pages on pushes to the main branch
- **Taskfile**: A YAML configuration file (`Taskfile.yml`) at the workspace root that defines named tasks using the [Task](https://taskfile.dev) runner, providing standardized commands for common development workflows
- **Task_Runner**: The `task` CLI tool that reads the Taskfile and executes the defined tasks

## Requirements

### Requirement 1: Static Site Generation from Analysis Data

**User Story:** As a researcher, I want the website to be statically generated from the analysis data at build time, so that the site loads quickly and can be hosted on any static file server.

#### Acceptance Criteria

1. THE Build_Process SHALL read Results_Data from `results/results.json` at build time and generate static HTML pages for all repositories
2. THE Build_Process SHALL read each Report_File from the `reports/` directory at build time and generate a corresponding Detail_Page
3. WHEN the Build_Process completes successfully, THE Dashboard SHALL consist entirely of static HTML, CSS, and JavaScript files requiring no server-side runtime
4. IF Results_Data is missing or malformed, THEN THE Build_Process SHALL fail with a descriptive error message indicating the problem

### Requirement 2: Project List Landing Page

**User Story:** As a researcher, I want to see all analyzed projects in a list on the landing page, so that I can quickly scan and compare Valkey support across repositories.

#### Acceptance Criteria

1. THE Project_List SHALL display every repository from Results_Data in a tabular layout
2. THE Project_List SHALL display the following columns for each repository: project name (formatted as `owner/repo_name`), Valkey_Support_Status, Valkey_Glide_Status, and Use_Cases
3. WHEN a user views the Project_List, THE Dashboard SHALL display the total number of repositories analyzed
4. THE Project_List SHALL display Valkey_Support_Status using visually distinct indicators for "explicit", "implied", and "none" values
5. THE Project_List SHALL display Use_Cases as a comma-separated list of detected use cases, or indicate when no use cases are detected

### Requirement 3: Project Detail Page

**User Story:** As a researcher, I want to click on a project name and see the complete analysis details, so that I can review the full evidence and findings for that repository.

#### Acceptance Criteria

1. WHEN a user clicks a project name in the Project_List, THE Dashboard SHALL navigate to the Detail_Page for that repository
2. THE Detail_Page SHALL display the repository metadata including project name, GitHub URL, description, primary language, and star count
3. THE Detail_Page SHALL display the classification table showing Valkey_Support_Status, Valkey Search support, Valkey_Glide_Status, and RediSearch usage
4. THE Detail_Page SHALL render the full content of the corresponding Report_File as formatted HTML
5. THE Detail_Page SHALL include a navigation link back to the Project_List
6. THE Detail_Page SHALL have a URL path derived from the repository owner and name (e.g., `/projects/owner/repo_name`)

### Requirement 4: Summary Statistics Display

**User Story:** As a researcher, I want to see aggregate statistics on the landing page, so that I can understand the overall landscape of Valkey adoption at a glance.

#### Acceptance Criteria

1. THE Project_List page SHALL display summary statistics from Results_Data including: total repositories analyzed, count of explicit Valkey support, count of implied Valkey support, count of no Valkey support, count of Valkey Glide users, and count of RediSearch users
2. THE Dashboard SHALL display summary statistics in a visually grouped format that is distinct from the project table

### Requirement 5: Navigation and Usability

**User Story:** As a researcher, I want the website to be easy to navigate and visually clean, so that I can efficiently review the analysis data.

#### Acceptance Criteria

1. THE Dashboard SHALL use a consistent page layout with a site header identifying the dashboard purpose
2. THE Dashboard SHALL be responsive and render correctly on screen widths from 768 pixels to 1920 pixels
3. WHEN a user is on a Detail_Page, THE Dashboard SHALL provide a visible link to return to the Project_List
4. THE Dashboard SHALL use semantic HTML elements for accessibility compliance
5. THE Project_List SHALL support client-side filtering by Valkey_Support_Status so users can narrow the displayed repositories

### Requirement 6: Visual Status Indicators

**User Story:** As a researcher, I want Valkey support levels to be visually distinct, so that I can quickly identify the support classification of each project.

#### Acceptance Criteria

1. THE Dashboard SHALL render Valkey_Support_Status "explicit" with a green color-coded badge
2. THE Dashboard SHALL render Valkey_Support_Status "implied" with a yellow or amber color-coded badge
3. THE Dashboard SHALL render Valkey_Support_Status "none" with a gray color-coded badge
4. THE Dashboard SHALL render Valkey_Glide_Status as a boolean indicator distinguishing true from false
5. THE Dashboard SHALL ensure all color-coded indicators have sufficient contrast to meet WCAG 2.1 AA contrast requirements

### Requirement 7: Theme and Color Mode Support

**User Story:** As a user with a visual sensitivity condition such as vertigo, I want the dashboard to support light, dark, and system color modes, so that I can reduce visual strain and use the site comfortably.

#### Acceptance Criteria

1. THE Dashboard SHALL support three color modes: light mode, dark mode, and system mode
2. WHILE system mode is active, THE Dashboard SHALL detect and apply the operating system color scheme preference using the `prefers-color-scheme` media query
3. THE Dashboard SHALL default to system mode when no user preference has been previously stored
4. THE Dashboard SHALL display a visible theme toggle control on every page that allows the user to switch between light mode, dark mode, and system mode
5. WHEN a user selects a color mode via the theme toggle, THE Dashboard SHALL persist the selection in localStorage and apply the selected mode immediately without a page reload
6. WHEN a user navigates between pages, THE Dashboard SHALL apply the persisted color mode preference from localStorage before rendering visible content to prevent a flash of incorrect theme
7. WHILE dark mode is active, THE Dashboard SHALL use low-contrast, muted background and text colors to reduce visual strain
8. WHILE dark mode is active, THE Dashboard SHALL render all visual elements including status badges, summary statistics cards, and data tables with colors adapted for dark backgrounds while maintaining WCAG 2.1 AA contrast requirements
9. WHILE light mode is active, THE Dashboard SHALL render all visual elements with colors adapted for light backgrounds while maintaining WCAG 2.1 AA contrast requirements
10. WHEN the operating system color scheme preference changes and system mode is active, THE Dashboard SHALL update the applied color scheme in real time without requiring a page reload

### Requirement 8: GitHub Pages Deployment

**User Story:** As a researcher, I want the dashboard to be automatically built and deployed to GitHub Pages when I push to the main branch, so that the latest analysis data is always publicly accessible without manual deployment steps.

#### Acceptance Criteria

1. THE Deployment_Workflow SHALL trigger automatically on pushes to the `main` branch
2. WHEN the Deployment_Workflow is triggered, THE Deployment_Workflow SHALL build the Astro site using the Build_Process and deploy the output to GitHub Pages using the official `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages` actions
3. THE Build_Process SHALL configure the Astro site with a `base` path matching the repository name so that all asset and navigation URLs resolve correctly on GitHub Pages
4. THE Deployment_Workflow SHALL set the GitHub Pages source to GitHub Actions deployment (not branch-based deployment)
5. THE Deployment_Workflow SHALL set the GitHub Pages site visibility to public
6. IF the Build_Process fails during the Deployment_Workflow, THEN THE Deployment_Workflow SHALL fail the workflow run and report the build error in the GitHub Actions log
7. WHEN the Deployment_Workflow completes successfully, THE Dashboard SHALL be accessible at `https://jbrinkman.github.io/{repository_name}/`

### Requirement 9: Taskfile Support for Development Workflows

**User Story:** As a developer, I want a Taskfile at the workspace root that provides standardized commands for common development workflows, so that I can run tasks without remembering complex command-line parameters or changing directories.

#### Acceptance Criteria

1. THE Taskfile SHALL be located at the workspace root as `Taskfile.yml` and be readable by the Task_Runner
2. THE Taskfile SHALL define a task named `install` that installs the Dashboard dependencies in the `website/` directory
3. THE Taskfile SHALL define a task named `dev` that starts the Astro development server for the Dashboard in the `website/` directory
4. THE Taskfile SHALL define a task named `build` that runs the Astro production build for the Dashboard in the `website/` directory
5. THE Taskfile SHALL define a task named `preview` that serves the production build of the Dashboard locally from the `website/` directory
6. THE Taskfile SHALL define a task named `clean` that removes build artifacts from the `website/` directory
7. WHEN a user runs any task from the workspace root, THE Task_Runner SHALL execute the command in the `website/` working directory without requiring the user to change directories manually
8. THE Taskfile SHALL include a `desc` field for every defined task so that running `task --list` displays a self-documenting summary of all available tasks
