# ty User Guide

!!! TIP
    Official documentation for ty is available at [https://github.com/astral-sh/ty](https://github.com/astral-sh/ty)

## What is ty?

ty is a fast type checker for Python built by Astral (the creators of uv and Ruff). It provides static type checking to catch type errors before runtime.

## How to use ty

If you want to run ty to manually check types in your Python code, run the following command:
```sh
uv run ty check
```

## Running ty via nox

You can also run ty through the nox lint session:
```sh
# Run only ty
uv run nox -s lint -- --ty

# Run both Ruff and ty
uv run nox -s lint -- --ruff --ty
```

## ty Configuration

If you want to configure ty, visit the [Configuration for ty](../configurations/ty.md) page.

## Integration with Development Workflow

ty is integrated into the development workflow in multiple ways:

### Pre-commit Hooks
ty runs automatically before each commit when pre-commit hooks are installed:
```sh
uv run pre-commit install
```

### CI/CD
GitHub Actions runs ty on every push and pull request to the main branch. See the workflow configuration in `.github/workflows/lint.yml`.

### VSCode Integration
VSCode uses ty for type checking when `python.languageServer` is set to `"None"` in `.vscode/settings.json`.
