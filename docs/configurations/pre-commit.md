# pre-commit Configurations

!!! TIP
    If you do not want to use the pre-commit hook, run this command:
    ```sh
    uv run pre-commit uninstall
    ```

## Hook List
- [https://github.com/pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    - End of file fixer, Trailing whitespace
    - Check JSON / TOML / XML / YAML
    - Detect private key
- [https://github.com/astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
    - Python Format (`ruff format`)
    - Python Lint (`ruff check --fix`)
- ty (local hook: `uv run ty check`)
    - Python Type Check
- [https://github.com/rhysd/actionlint](https://github.com/rhysd/actionlint)
    - GitHub Actions Lint
- [https://github.com/hadolint/hadolint](https://github.com/hadolint/hadolint)
    - Dockerfile Lint (requires `hadolint` on your `PATH`)
- [sqruff](https://github.com/quarylabs/sqruff) (local hooks: `uv run sqruff fix` / `uv run sqruff lint`)
    - SQL Format
    - SQL Lint

## Overview
```{.yaml title=".pre-commit-config.yaml"}
--8<-- ".pre-commit-config.yaml"
```
