# VSCode Dev Container: Python Development with uv and Ruff

<div align="center">

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![Versions](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11%20|%203.12%20-green.svg)](https://github.com/a5chin/python-uv)

[![Ruff](https://github.com/a5chin/python-uv/actions/workflows/ruff.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/ruff.yml)
[![Test](https://github.com/a5chin/python-uv/actions/workflows/test.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/test.yml)
[![Docker](https://github.com/a5chin/python-uv/actions/workflows/docker.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/docker.yml)

</div>

## Overview
This repository contains configurations to set up a Python development environment using VSCode's Dev Container feature.
The environment includes uv, and Ruff.

![demo](assets/gif/ruff.gif)

If the Ruff format does not work, try reloading the VS Code window.
Specifically, you can solve this problem by following the steps below.

1. Type `⌘+⇧+P` to open the command palette
2. Type `Developer: Reload Window` in the command palette to reload the window

### Contents
- [VSCode Dev Container: Python Development with uv and Ruff](#vscode-dev-container-python-development-with-uv-and-ruff)
  - [Overview](#overview)
    - [Contents](#contents)
  - [Branches](#branches)
  - [Dev Container](#dev-container)
  - [GitHub Actions](#github-actions)
  - [Ruff](#ruff)
  - [pre-commit](#pre-commit)
  - [Appendix](#appendix)
    - [Install libraries](#install-libraries)
    - [The structure of this repository](#the-structure-of-this-repository)

## Branches
- [main](https://github.com/a5chin/python-uv/tree/main)
- [jupyter](https://github.com/a5chin/python-uv/tree/jupyter)
- [rye](https://github.com/a5chin/python-uv/tree/rye)（Archived）

## Dev Container
- `devcontainer.json`
  - settings
    - formatOnSave by Ruff
  - features
    - pre-commit
  - extentions
    - [charliermarsh.ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
    - [codezombiech.gitignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)
    - [eamodio.gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
    - [kevinrose.vsc-python-indent](https://marketplace.visualstudio.com/items?itemName=kevinrose.vsc-python-indent)
    - [mosapride.zenkaku](https://marketplace.visualstudio.com/items?itemName=mosapride.zenkaku)
    - [ms-azuretools.vscode-docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
    - [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [njpwerner.autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    - [oderwat.indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
    - [pkief.material-icon-theme](https://marketplace.visualstudio.com/items?itemName=pkief.material-icon-theme)
    - [shardulm94.trailing-spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)
    - [usernamehw.errorlens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
    - [yzhang.markdown-all-in-one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- `Dockerfile`
  - Only Dev dependencies
    - `pre-commit`
    - `pytest`
    - `ruff`

## GitHub Actions
- `docker.yml`
  - Workflow to check if you can build with Docker
- `test.yml`
  - Workflow to check if all the described tests can be passed with pytest
- `ruff.yml`
  - Workflow to check if you can go through Formatter and Linter with Ruff

## Ruff
Ruff can be used to replace Flake8, Black, isort, pydocstyle, pyupgrade, autoflake, etc., and yet run tens to hundreds of times faster than the individual tools.

To change the configuration, it is necessary to rewrite ruff.toml, and [it is recommended](https://docs.astral.sh/ruff/formatter/#conflicting-lint-rules) to set it to ignore conflicts such as the following:
```toml
ignore = [
    "COM812", "COM819",
    "D100", "D203", "D213", "D300",
    "E111", "E114", "E117",
    "ISC001", "ISC002",
    "Q000", "Q001", "Q002", "Q003",
    "W191",
]
```

## pre-commit
The `.pre-commit-config.yaml` file can contain scripts to be executed before commit.

```sh
# Python Formatter
uv run ruff format .

# Python Linter
uv run ruff check . --fix

# Docker Linter
hodolint Dockerfile
```

## Appendix

### Install libraries
Only sync based on the production lockfile (`requirements.lock`) instead of the development lockfile (`requirements-dev.lock`).

```sh
# Install also include develop dependencies
uv sync

# If you do not want dev dependencies to be installed
uv sync --no-dev

# Use the add command to add dependencies to your project
uv add {libraries}
```

### The structure of this repository
```
.
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── Dockerfile
├── .github
│   ├── actions
│   │   └── setup-python-with-uv
│   │       └── action.yml
│   ├── dependabot.yml
│   └── workflows
│       ├── docker.yml
│       ├── ruff.yml
│       └── test.yml
├── .gitignore
├── LICENSE
├── .pre-commit-config.yaml
├── pyproject.toml
├── .python-version
├── README.md
├── requirements-dev.lock
├── requirements.lock
├── ruff.toml
└── .vscode
    ├── extensions.json
    └── settings.json
```
