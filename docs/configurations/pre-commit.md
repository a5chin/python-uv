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
- [https://github.com/sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)
    - SQLFluff Lint
    - SQLFluff Fix
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
      - id: check-json
      - id: check-toml
      - id: check-xml
      - id: check-yaml
      - id: detect-private-key
      - id: trailing-whitespace

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.8
    hooks:
      - id: ruff
        name: Ruff check
        description: "Run 'ruff check' for extremely fast Python linting"
        args: [--fix]

      - id: ruff-format
        name: Ruff format
        description: "Run 'ruff format' for extremely fast Python formatting"

  - repo: https://github.com/rhysd/actionlint
    rev: v1.7.10
    hooks:
      - id: actionlint

  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.0
    hooks:
      - id: hadolint
        name: Lint Dockerfiles
        description: Runs hadolint to lint Dockerfiles
        language: system
        types: ["dockerfile"]
        entry: hadolint

  - repo: https://github.com/sqlfluff/sqlfluff
    rev: 3.5.0
    hooks:
      - id: sqlfluff-lint
        name: SQLFluff Lint
        description: "Lints sql files with `SQLFluff`"
        types: [sql]

      - id: sqlfluff-fix
        name: SQLFluff Fix
        description: "Fixes sql lint errors with `SQLFluff`"
        types: [sql]

ci:
  autoupdate_schedule: weekly
```
