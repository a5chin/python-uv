# CI/CD Workflows

All workflows live in [`.github/workflows/`](https://github.com/a5chin/python-uv/tree/main/.github/workflows). Quality checks run on pull requests, using the same nox sessions as local development (see [Task Automation with nox](index.md#task-automation-with-nox)).

## Quality Checks

| Workflow | Runs on | What it does |
|---|---|---|
| `format.yml` | PRs changing Python / SQL files or their configs | `nox -s fmt -- --ruff` and `nox -s fmt -- --sqruff` |
| `lint.yml` | PRs changing Python / SQL files or their configs | `nox -s lint -- --ruff`, `-- --sqruff`, and `-- --ty` |
| `test.yml` | PRs and pushes to `main` changing Python files or test configs | `nox -s test -- --cov_report xml --junitxml junit.xml`, then uploads results to Codecov |
| `actionlint.yml` | PRs changing `.github/workflows/*.yml` | Lints workflows with actionlint (reviewdog) |
| `docker.yml` | PRs changing Python files, `pyproject.toml`, `uv.lock`, ... | Validates the `Dockerfile` build |
| `devcontainer.yml` | PRs changing `.devcontainer/` or `.python-version` | Validates the Dev Container build |

## Pull Request Automation

| Workflow | Runs on | What it does |
|---|---|---|
| `labeler.yml` | PRs opened / updated | Adds labels from the branch prefix (see [Branches](branch-strategy.md#branches)) |
| `assign.yml` | PRs opened by humans without an assignee | Assigns the PR author |
| `approve.yml` | PRs opened by bots (e.g. Renovate) | Approves the PR |
| `pr-agent.yml` | PRs opened / updated and PR comments (non-bot) | Automated review with Qodo PR Agent |

## Release & Deployment

| Workflow | Runs on | What it does |
|---|---|---|
| `release.yml` | Pushes to `main` and published releases | Builds and pushes the `app` / `devcontainer` images to GHCR and updates the Draft Release. See [Branch Strategy & Release Flow](branch-strategy.md) |
| `gh-deploy.yml` | PRs changing `docs/` or `mkdocs.yml`, and manual runs | Deploys this documentation site to GitHub Pages (`mkdocs gh-deploy`) |

## Repository Settings

| Workflow | Runs on | What it does |
|---|---|---|
| `setting.yml` | Daily, manual runs, and PRs changing it or `.github/{environments,protection}.json` | Applies the default branch, environments and their deployment policies, GitHub Pages source, workflow permissions, and branch protection |
