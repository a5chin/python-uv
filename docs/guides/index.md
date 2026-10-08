# Development Guides

This section provides guides for using the tools and utilities included in this template, and for contributing to it.

## Task Automation with nox

**nox** is the primary way to run development tasks in this repository. Every session runs with `python=False` (it relies on `uv run`), and `fmt` / `lint` only run the tools whose flags you pass: `uv run nox -s fmt` without flags does nothing.

### Available Sessions

```bash
# Format code
uv run nox -s fmt -- --ruff --sqruff  # Format both
uv run nox -s fmt -- --ruff           # Format Python code
uv run nox -s fmt -- --sqruff         # Format SQL code

# Run linters (you can specify which ones)
uv run nox -s lint -- --ruff --sqruff --ty  # All linters
uv run nox -s lint -- --ruff --ty           # Python only
uv run nox -s lint -- --ruff                # Ruff only
uv run nox -s lint -- --sqruff              # SQL only
uv run nox -s lint -- --ty                  # ty only

# Run tests with coverage (75% minimum required)
uv run nox -s test

# Run tests with JUnit XML output (for CI)
uv run nox -s test -- --cov_report xml --junitxml junit.xml
```

Before opening a pull request, run `fmt`, `lint`, and `test` above, then `uv run pre-commit run --all-files`.

## Tools

| Guide | What it covers |
|---|---|
| [uv](uv.md) | Adding / removing dependencies, development dependencies, pinning the Python version |
| [Ruff](ruff.md) | Formatting and linting Python code |
| [ty](ty.md) | Type checking |
| [pre-commit](pre-commit.md) | Hooks that run before every commit |
| [Test](test.md) | Running pytest with coverage |
| [cookiecutter](cookiecutter.md) | Bootstrapping new projects from templates |
| [Tools Package](tools/index.md) | Built-in `Logger`, `Settings`, and `Timer` utilities |

## Contributing

| Guide | What it covers |
|---|---|
| [Code Standards](code-standards.md) | Coding rules, writing tests, documentation rules, common issues |
| [Branch Strategy & Release Flow](branch-strategy.md) | GitHub Flow, branch naming, Draft Release → Publish → Production |
| [CI/CD Workflows](ci-cd.md) | What each GitHub Actions workflow does and when it runs |

For configuration details, see the [Configuration Reference](../configurations/index.md).
