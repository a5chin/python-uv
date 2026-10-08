# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. It only holds agent-specific rules and the minimum commands; everything else is in `docs/` (see [Documentation Map](#documentation-map)).

## Project Overview

A Python development environment template using **uv** (package manager), **Ruff** (linter/formatter), and **ty** (type checker). It also ships a reusable `tools/` package (`Logger`, `Settings`, `Timer`).

## Essential Commands

```bash
uv sync                                     # Install dependencies
uv add <package>                            # Add a dependency (--dev for dev dependencies); never use pip
uv run nox -s fmt -- --ruff --sqruff        # Format (without flags, nothing runs)
uv run nox -s lint -- --ruff --sqruff --ty  # Lint and type check (without flags, nothing runs)
uv run nox -s test                          # Tests with coverage (75% minimum)
uv run pre-commit run --all-files           # All pre-commit hooks
```

Run all of the above before opening a PR. Other options: [Task Automation with nox](docs/guides/index.md#task-automation-with-nox).

## Rules for Claude Code

### Code and tests

- Follow [Code Standards](docs/guides/code-standards.md): type hints and docstrings on public APIs, line length 88.
- Name test files `test__*.py` (double underscore) and mirror `tools/` in `tests/`. Coverage must stay at 75% or above (branch coverage included).
- When adding a utility to `tools/`, add or update its page in `docs/guides/tools/`.

### Documentation

- Each topic has exactly one source of truth under `docs/` (see [Documentation Map](#documentation-map)). Edit only that page.
- Never copy documentation content into `README.md`, `CONTRIBUTING.md`, or this file; link to the `docs/` page instead.
- Configuration pages include the real config files with `--8<--` snippets; do not paste config contents into docs.
- After changing docs, run `uv run mkdocs build --strict`. Register new pages in the `nav` of `mkdocs.yml`.

### Branches and pull requests

The flow is described in [Branch Strategy & Release Flow](docs/guides/branch-strategy.md) (GitHub Flow, no `develop` branch).

- Always open PRs against `main`; never push directly to `main`.
- Use a branch prefix from [Branches](docs/guides/branch-strategy.md#branches) (`feature/`, `fix/`, `hotfix/`, `refactor/`).
- Commit or push only when the user asks.

### Releases

- To release, edit the **existing** Draft Release; never create a new release or tag (`gh release create`, `git tag`).
- The tag must start with `v` (e.g. `v1.3.0`); changing the proposed tag is allowed.
- Publishing deploys to Production: always confirm with the user before publishing.

Release procedure (e.g. the user asks "release v1.3.0" and the Draft proposes `v1.2.4`):

```bash
# 1. Find the Draft: the row marked "Draft"; its proposed tag (here v1.2.4) identifies it
gh release list
gh release view v1.2.4              # check the change list and the target commit

# 2. Ask the user for confirmation, showing the new tag (v1.3.0) and the change list.
#    Do not edit anything until the user approves.

# 3. After approval, change the tag and publish immediately, without waiting in between
#    (a merge into main in between makes release-drafter overwrite the tag again)
gh release edit v1.2.4 --tag v1.3.0 --title v1.3.0 --prerelease=false
gh release edit v1.3.0 --draft=false   # from here on, the release is addressed by the new tag
```

`gh` runs with the user's own credentials, so publishing with it triggers the Production deployment. The "`GITHUB_TOKEN` does not trigger workflows" caveat only applies to releases published from inside a GitHub Actions workflow.

## Documentation Map

| Topic | Source of truth |
|---|---|
| Setup, using this repository as a template | [docs/getting-started/index.md](docs/getting-started/index.md) |
| nox sessions and flags | [docs/guides/index.md](docs/guides/index.md#task-automation-with-nox) |
| uv / Ruff / ty / pre-commit / pytest usage | [docs/guides/](docs/guides/index.md) |
| Configuration files (`ruff.toml`, `ty.toml`, `pytest.ini`, `.sqruff`, `.pre-commit-config.yaml`, ...) | [docs/configurations/](docs/configurations/index.md) |
| `tools/` package (`Logger`, `Settings`, `Timer`) and environment variables | [docs/guides/tools/](docs/guides/tools/index.md) |
| Code standards, writing tests, common issues | [docs/guides/code-standards.md](docs/guides/code-standards.md) |
| Branch strategy and release flow | [docs/guides/branch-strategy.md](docs/guides/branch-strategy.md) |
| GitHub Actions workflows | [docs/guides/ci-cd.md](docs/guides/ci-cd.md) |
| Project structure | [docs/index.md](docs/index.md) |
| Pull request process | [CONTRIBUTING.md](CONTRIBUTING.md) |

All contributors must follow the [Code of Conduct](CODE_OF_CONDUCT.md).
