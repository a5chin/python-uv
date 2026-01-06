# Configuration Reference

This section provides detailed information about how each tool in this template is configured. Understanding these configurations will help you customize the environment to match your project's specific needs.

## Overview

The development environment includes configuration files for:

- **uv** - Package management and Python version
- **Ruff** - Linting and formatting rules
- **ty** - Type checking strictness
- **pytest** - Testing and coverage
- **pre-commit** - Automated quality checks

Each tool is configured through dedicated configuration files in the repository root.

## Configuration Files

| File | Tool | Purpose |
|------|------|---------|
| `pyproject.toml` | uv, Project | Dependencies and project metadata |
| `ruff.toml` | Ruff | Linting and formatting rules |
| `ty.toml` | ty | Type checking configuration |
| `pytest.ini` | pytest | Testing and coverage settings |
| `.pre-commit-config.yaml` | pre-commit | Hook definitions |
| `noxfile.py` | nox | Task automation |

## Quick Links

Jump to detailed configuration guides:

### [uv Configuration](uv.md)
Learn how uv manages dependencies and Python versions:
- Dependency groups (production vs development)
- Lock file management
- Python version pinning
- Virtual environment handling

**Key file**: `pyproject.toml`

[→ Read full uv configuration guide](uv.md)

### [Ruff Configuration](ruff.md)
Understand Ruff's linting and formatting rules:
- Rule selection (ALL enabled by default)
- Specific rule exclusions
- Per-file rule overrides
- Line length and formatting style

**Key file**: `ruff.toml`

[→ Read full Ruff configuration guide](ruff.md)

### [ty Configuration](ty.md)
Configure type checking behavior:
- Include/exclude patterns
- Source directories
- Cache exclusions

**Key file**: `ty.toml`

[→ Read full ty configuration guide](ty.md)

### [pytest Configuration](test.md)
Set up testing and coverage:
- Coverage requirements (75% minimum)
- Test discovery patterns
- Coverage reports (HTML + terminal)
- pytest plugins and options

**Key file**: `pytest.ini`

[→ Read full pytest configuration guide](test.md)

### [pre-commit Configuration](pre-commit.md)
Configure automated hooks:
- Ruff formatting and linting hooks
- File validation hooks
- Dockerfile linting
- Hook execution order

**Key file**: `.pre-commit-config.yaml`

[→ Read full pre-commit configuration guide](pre-commit.md)

## Common Configuration Tasks

### Adjusting Code Quality Standards

**Make linting more strict:**
```toml
# ruff.toml
[lint]
select = ["ALL"]
ignore = []  # Remove exclusions to enable all rules
```

**Increase coverage requirements:**
```ini
# pytest.ini
[pytest]
addopts = --cov-fail-under=90  # Increase from 75% to 90%
```

**Configure type checking:**
```toml
# ty.toml
[src]
include = ["tools", "tests", "your_package"]
exclude = ["**/__pycache__", ".pytest_cache", ".ruff_cache", ".venv"]
```

### Adding New Dependencies

**Add production dependency:**
```bash
uv add requests
```

**Add development dependency:**
```bash
uv add --dev pytest-mock
```

Both commands automatically update `pyproject.toml` and `uv.lock`.

### Customizing for Your Project

**Update project metadata:**
```toml
# pyproject.toml
[project]
name = "your-project-name"
version = "1.0.0"
description = "Your project description"
requires-python = ">=3.11"
```

**Configure FastAPI settings:**
```bash
# .env.local
DEBUG=true
TITLE=Your API Name
VERSION=1.0.0
API_PREFIX_V1=/api/v1
```

## Configuration Best Practices

### 1. Start with Defaults

The default configurations are production-tested. Only modify when you have a specific need.

### 2. Document Changes

If you modify configurations, document why:

```toml
# ruff.toml
[lint]
ignore = [
    "D100",  # Exclude module docstring (team decision 2024-01-15)
]
```

### 3. Keep Configurations Consistent

Ensure configurations work together:
- Ruff's line length should match your formatting preferences
- Type checking directories in `ty.toml` should match your project structure
- Test patterns should align with your file structure

### 4. Version Control

Commit configuration files to git:
```bash
git add pyproject.toml ruff.toml ty.toml pytest.ini .pre-commit-config.yaml
git commit -m "Update project configurations"
```

**Exception**: Never commit `.env.local` (contains local secrets)

### 5. Team Alignment

Configuration changes affect the entire team. Discuss before making major changes:
- Changing coverage requirements
- Modifying linting rules
- Updating Python version requirements

## Troubleshooting

### Conflicts Between Tools

**Ruff and other formatters:**
The template is configured to avoid conflicts. If you add other formatters, they may conflict with Ruff.

**Solution**: Use Ruff exclusively (it replaces Black, isort, etc.)

### VSCode Not Picking Up Changes

After modifying configurations:

1. Reload the VSCode window: `Cmd/Ctrl+Shift+P` → "Developer: Reload Window"
2. Ensure the Dev Container rebuilt if you changed `devcontainer.json`

### Pre-commit Hooks Failing

If hooks fail after configuration changes:

```bash
# Update pre-commit hooks
uv run pre-commit autoupdate

# Reinstall hooks
uv run pre-commit uninstall
uv run pre-commit install
```

## Advanced Configuration

### Multi-Environment Setup

Use different configurations for different environments:

```python
# Load config based on environment
from tools.config import Settings

settings = Settings()

if settings.IS_LOCAL:
    # Use local database
    DATABASE_URL = "sqlite:///./dev.db"
else:
    # Use production database
    DATABASE_URL = settings.PRODUCTION_DATABASE_URL
```

### CI/CD Configuration

GitHub Actions workflows use the same configurations:

```yaml
# .github/workflows/test.yml
- name: Run tests
  run: uv run nox -s test
```

Ensure CI and local environments use identical configurations.

## Migration Guide

### From pip to uv

If migrating from pip:

```bash
# Export current dependencies
pip freeze > requirements.txt

# Add to pyproject.toml
uv add $(cat requirements.txt)

# Remove old files
rm requirements.txt
```

### From Black/isort to Ruff

Ruff replaces both. Remove old configs:

```bash
# Remove old configuration files
rm .black.toml setup.cfg .isort.cfg

# Configure Ruff in ruff.toml (already done in template)
```

## Next Steps

- **Customize your setup**: Read the detailed configuration guides
- **Understand the tools**: Check the [Development Guides](../guides/index.md)
- **See it in action**: Browse [Use Cases](../usecases/index.md)

## Getting Help

- **uv**: [Official Documentation](https://docs.astral.sh/uv)
- **Ruff**: [Official Documentation](https://docs.astral.sh/ruff)
- **ty**: [Official Documentation](https://github.com/astral-sh/ty)
- **pytest**: [Official Documentation](https://docs.pytest.org)
- **pre-commit**: [Official Documentation](https://pre-commit.com)
