# pre-commit Configurations

!!! TIP
    If you do not want to use the pre-commit hook, run this command:
    ```sh
    pre-commit uninstall
    ```

## Hook List
- [https://github.com/astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
    - Ruff Lint
    - Ruff Format
- [https://github.com/quarylabs/sqruff](https://github.com/quarylabs/sqruff)
    - sqruff Lint
    - sqruff Fix
- [https://github.com/rhysd/actionlint](https://github.com/rhysd/actionlint)
    - actionlint
- [https://github.com/hadolint/hadolint](https://github.com/hadolint/hadolint)
    - Hadolint

## Overview
```{.yaml title=".pre-commit-config.yaml"}
default_stages: [pre-commit]

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: end-of-file-fixer
        name: End of file fixer
        description: Ensure files end with a newline

      - id: check-json
        name: Check JSON
        description: Check that JSON files are valid

      - id: check-toml
        name: Check TOML
        description: Check that TOML files are valid

      - id: check-xml
        name: Check XML
        description: Check that XML files are valid

      - id: check-yaml
        name: Check YAML
        description: Check that YAML files are valid

      - id: detect-private-key
        name: Detect private key
        description: Detect private keys in files

      - id: trailing-whitespace
        name: Trailing whitespace
        description: Remove trailing whitespace from files

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.8
    hooks:
      - id: ruff-format
        name: Python Format
        description: Run 'ruff format' for extremely fast Python formatting

      - id: ruff-lint
        name: Python Lint
        description: Run 'ruff check' for extremely fast Python linting
        args: [--fix]

  - repo: local
    hooks:
      - id: ty
        name: Python Type Check
        description: Run 'ty check' for Python type checking
        entry: uv run ty check
        language: python
        types: [python]

  - repo: https://github.com/rhysd/actionlint
    rev: v1.7.10
    hooks:
      - id: actionlint
        name: GitHub Actions Lint
        description: Lint GitHub Actions workflows

  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint
        name: Dockerfile Lint
        description: Runs hadolint to lint Dockerfiles
        language: system
        types: ["dockerfile"]
        entry: hadolint

  - repo: local
    hooks:
      - id: sqruff-fix
        name: SQL Format
        description: Run 'sqruff fix' for SQL formatting
        entry: uv run sqruff fix
        language: python
        types: [python]

      - id: sqruff-lint
        name: SQL Lint
        description: Run 'sqruff lint' for SQL linting
        entry: uv run sqruff lint
        language: python
        types: [python]

ci:
  autoupdate_schedule: weekly
```
