# Development Guides

This section provides comprehensive guides for using the tools and utilities included in this template. Whether you're managing dependencies, formatting code, or building production applications, these guides will help you work efficiently.

## Overview

This template includes several modern Python development tools, each serving a specific purpose:

- **uv** - Ultra-fast package management (10-100x faster than pip)
- **Ruff** - Lightning-fast linting and formatting
- **ty** - Advanced type checking
- **SQLFluff** - SQL linting and formatting
- **actionlint** - GitHub Actions workflow linting
- **pytest** - Comprehensive testing framework
- **nox** - Task automation and workflow management
- **pre-commit** - Automated code quality checks
- **Built-in utilities** - Production-ready modules for logging, configuration, and monitoring

## Task Automation with nox

**nox** is the primary way to run development tasks in this repository. It provides a consistent interface for common operations and handles dependency management automatically.

### Available Sessions

```bash
# Format code
uv run nox -s fmt -- --ruff             # Format Python code
uv run nox -s fmt -- --sqlfluff         # Format SQL code
uv run nox -s fmt -- --ruff --sqlfluff  # Format both

# Run linters (you can specify which ones)
uv run nox -s lint -- --ruff --sqlfluff --ty  # All linters
uv run nox -s lint -- --ruff --ty             # Python only
uv run nox -s lint -- --ruff                  # Ruff only
uv run nox -s lint -- --sqlfluff              # SQL only
uv run nox -s lint -- --ty                    # ty only

# Run tests with coverage (75% minimum required)
uv run nox -s test

# Run tests with JUnit XML output (for CI)
uv run nox -s test -- --cov_report xml --junitxml junit.xml
```

### Why nox?

- **Consistent workflow** - Same commands work for all developers
- **Isolated environments** - Each session runs in isolation
- **Customizable** - Easy to add new sessions for your needs
- **CI/CD friendly** - Integrates seamlessly with GitHub Actions

## Package Management

### [uv Guide](uv.md)

Learn how to manage Python packages with uv, the blazing-fast package manager:

- Adding and removing dependencies
- Managing development dependencies
- Pinning Python versions
- Understanding the lock file

**Quick reference:**

```bash
# Add a package
uv add requests

# Add a dev dependency
uv add --dev pytest-mock

# Install all dependencies
uv sync

# Remove a package
uv remove requests
```

[→ Read the full uv guide](uv.md)

## Code Quality

### [Ruff Guide](ruff.md)

Master Ruff, the all-in-one linter and formatter that replaces Black, isort, Flake8, and more:

- Formatting code automatically
- Running linting checks
- Understanding Ruff rules
- Customizing for your project

**Quick reference:**

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Auto-fix issues
uv run ruff check . --fix
```

[→ Read the full Ruff guide](ruff.md)

### [ty Guide](ty.md)

Use ty for comprehensive type checking:

- Running type checks
- Understanding type errors
- Configuring type checking
- Integrating with your editor

**Quick reference:**

```bash
# Run type checker
uv run ty check

# Check via nox
uv run nox -s lint -- --ty
```

[→ Read the full ty guide](ty.md)

## Testing

### [Testing Guide](test.md)

Learn how to write and run tests with pytest:

- Writing test cases
- Running tests with coverage
- Understanding coverage reports
- Testing best practices

**Quick reference:**

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/tools/test__logger.py

# Run with coverage report
uv run pytest --cov=tools --cov-report=html
```

[→ Read the full testing guide](test.md)

## Automation

### [Pre-commit Guide](pre-commit.md)

Set up automated code quality checks that run before every commit:

- Installing pre-commit hooks
- Running hooks manually
- Understanding hook failures
- Customizing hooks

**Quick reference:**

```bash
# Install hooks
uv run pre-commit install

# Run all hooks manually
uv run pre-commit run --all-files

# Run specific hook
uv run pre-commit run ruff-format
```

[→ Read the full pre-commit guide](pre-commit.md)

## Built-in Utilities

### [Tools Package](tools/index.md)

Explore the production-ready utility modules included in this template:

#### [Logger](tools/logger.md)
Flexible logging system with support for both local development and Google Cloud:

```python
from tools.logger import Logger, LogType

logger = Logger(__name__, log_type=LogType.LOCAL)
logger.info("Application started")
```

#### [Configuration](tools/config.md)
Environment-based configuration management:

```python
from tools.config import Settings

settings = Settings()  # Loads from .env and .env.local
api_url = settings.api_prefix_v1
```

#### [Performance Tracer](tools/tracer.md)
Timer decorator and context manager for performance monitoring:

```python
from tools.tracer import Timer

with Timer("database_query"):
    result = db.query()  # Logs execution time
```

[→ Explore all built-in utilities](tools/index.md)

## Project Templates

### [Cookiecutter Guide](cookiecutter.md)

Learn how to use cookiecutter templates to bootstrap new projects:

- Data Science projects
- FastAPI applications
- Django web apps
- Flask microservices

**Quick reference:**

```bash
# Use a template
uv run cookiecutter https://github.com/fastapi/full-stack-fastapi-template
```

[→ Read the full cookiecutter guide](cookiecutter.md)

## Next Steps

1. **Start with basics**: Read the [uv guide](uv.md) to understand package management
2. **Ensure quality**: Set up [pre-commit hooks](pre-commit.md) for automatic checks
3. **Explore utilities**: Check out the [built-in tools](tools/index.md) for common tasks
4. **See examples**: Browse [use cases](../usecases/index.md) for real-world applications

## Need More Details?

For in-depth configuration information, see the [Configuration Reference](../configurations/index.md) section.
