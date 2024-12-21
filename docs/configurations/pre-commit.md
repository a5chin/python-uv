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
- [https://github.com/hadolint/hadolint](https://github.com/hadolint/hadolint)
    - Hadolint

## Overview
```{.yaml hl_lines=42-57 title=".pre-commit-config.yaml"}
default_stages: [pre-commit]

repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.3
    hooks:
      - id: ruff
        name: Ruff check
        description: "Run 'ruff check' for extremely fast Python linting"
        args: [--fix]

      - id: ruff-format
        name: Ruff format
        description: "Run 'ruff format' for extremely fast Python formatting"

  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint
        name: Lint Dockerfiles
        description: Runs hadolint to lint Dockerfiles
        language: system
        types: ["dockerfile"]
        entry: hadolint

ci:
  autoupdate_schedule: weekly
```
