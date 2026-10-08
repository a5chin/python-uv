# Configuration Reference

This section provides detailed information about how each tool in this template is configured. Understanding these configurations will help you customize the environment to match your project's specific needs.

## Configuration Files

| File | Tool | Purpose | Reference |
| --- | --- | --- | --- |
| `pyproject.toml`, `.devcontainer/devcontainer.json` | uv, Project | Dependencies, project metadata, Dev Container and VS Code settings | [uv](uv.md) |
| `ruff.toml` | Ruff | Linting and formatting rules | [Ruff](ruff.md) |
| `ty.toml` | ty | Type checking configuration | [ty](ty.md) |
| `.sqruff` | sqruff | SQL linting and formatting rules | [sqruff](sqruff.md) |
| `pytest.ini` | pytest | Testing and coverage settings | [Test](test.md) |
| `.pre-commit-config.yaml` | pre-commit | Hook definitions | [pre-commit](pre-commit.md) |
| `noxfile.py` | nox | Task automation | [Task Automation with nox](../guides/index.md#task-automation-with-nox) |
| `.env`, `.env.local` | `Settings` | Environment variables | [Configuration Management](../guides/tools/config.md) |

## Customizing for Your Project

**Update project metadata:**
```toml
# pyproject.toml
[project]
name = "your-project-name"
version = "1.0.0"
description = "Your project description"
requires-python = ">=3.11"
```

To change linting rules, coverage requirements, or type checking targets, edit the file listed above; each reference page explains its options.

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

Commit configuration files to git. `.env` is ignored by git, so put secrets there; `.env.local` is committed (see [Configuration Management](../guides/tools/config.md)).

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
