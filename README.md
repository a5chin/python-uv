# Python Development with uv and Ruff

<div align="center">

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13%20|%203.14%20-green.svg)](https://github.com/a5chin/python-uv)
![code coverage](https://raw.githubusercontent.com/a5chin/python-uv/coverage-badge/coverage.svg?raw=true)

[![Docker](https://github.com/a5chin/python-uv/actions/workflows/docker.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/docker.yml)
[![Format](https://github.com/a5chin/python-uv/actions/workflows/format.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/format.yml)
[![Lint](https://github.com/a5chin/python-uv/actions/workflows/lint.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/lint.yml)
[![Test](https://github.com/a5chin/python-uv/actions/workflows/test.yml/badge.svg)](https://github.com/a5chin/python-uv/actions/workflows/test.yml)

</div>

A production-ready Python development environment template using modern tools: **uv** for blazing-fast package management, **Ruff** for lightning-fast linting and formatting, and **VSCode Dev Containers** for reproducible development environments.

<div align="center">
<img src="docs/img/ruff.gif" width="49%"> <img src="docs/img/jupyter.gif" width="49%">
</div>

## ✨ Features

- 🚀 **Ultra-fast package management** with [uv](https://github.com/astral-sh/uv) (10-100x faster than pip)
- ⚡ **Lightning-fast linting & formatting** with [Ruff](https://github.com/astral-sh/ruff) (replacing Black, isort, Flake8, and more)
- 🐳 **Dev Container ready** - Consistent development environment across all machines
- 🔍 **Type checking** with Pyright
- ✅ **Pre-configured testing** with pytest (75% coverage requirement)
- 🔄 **Automated CI/CD** with GitHub Actions
- 📦 **Reusable utilities** - Logger, configuration management, and performance tracing tools
- 🎯 **Task automation** with nox
- 🪝 **Pre-commit hooks** for automatic code quality checks

## 🚀 Quick Start

### Using Dev Container (Recommended)

1. **Prerequisites**: Install [Docker](https://www.docker.com/) and [VSCode](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in container**:
   ```bash
   git clone https://github.com/a5chin/python-uv.git
   cd python-uv
   code .
   ```
   When prompted, click "Reopen in Container"

3. **Start developing**:
   ```bash
   # Install dependencies
   uv sync

   # Run tests
   uv run nox -s test

   # Format and lint
   uv run nox -s fmt
   uv run nox -s lint -- --pyright --ruff
   ```

### Using Docker Only

```bash
# Build the image
docker build -t python-uv .

# Run container
docker run -it --rm -v $(pwd):/workspace python-uv
```

### Local Setup (Without Docker)

**Prerequisites**: Python 3.10+ and [uv](https://github.com/astral-sh/uv)

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/a5chin/python-uv.git
cd python-uv

# Install dependencies
uv sync

# Install pre-commit hooks (optional)
uv run pre-commit install
```

## 📚 Getting Started

### Installing Dependencies

```bash
# Install all dependencies (including dev dependencies)
uv sync

# Install without dev dependencies
uv sync --no-dev

# Add new dependencies
uv add requests pandas

# Add dev dependencies
uv add --dev pytest-mock
```

### Development Workflow

This project uses **nox** for task automation. All common development tasks are available as nox sessions:

```bash
# Format code with Ruff
uv run nox -s fmt

# Run linters (Pyright + Ruff)
uv run nox -s lint -- --pyright --ruff

# Run only Pyright
uv run nox -s lint -- --pyright

# Run only Ruff linter
uv run nox -s lint -- --ruff

# Run tests with coverage (75% minimum required)
uv run nox -s test

# Run tests with JUnit XML output (for CI)
uv run nox -s test -- --junitxml=results.xml
```

You can also run tools directly:

```bash
# Run pytest directly
uv run pytest

# Run specific test file
uv run pytest tests/tools/test__logger.py

# Format with Ruff
uv run ruff format .

# Lint with Ruff
uv run ruff check . --fix

# Type check with Pyright
uv run pyright
```

### Pre-commit Hooks

Pre-commit hooks automatically run code quality checks before each commit:

```bash
# Install hooks
uv run pre-commit install

# Run manually on all files
uv run pre-commit run --all-files
```

Configured hooks:
- Ruff formatting and linting
- JSON, YAML, TOML validation
- Trailing whitespace removal
- End-of-file fixer
- Private key detection
- Dockerfile linting with hadolint

### Documentation

Generate and serve documentation with MkDocs:

```bash
# Serve locally at http://127.0.0.1:8000
uv run mkdocs serve

# Build static site
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy
```

## 🏗️ Project Structure

```
.
├── tools/                    # Reusable utility modules
│   ├── config/              # Configuration management (Settings, FastAPI config)
│   ├── logger/              # Logging utilities (Local & Google Cloud formatters)
│   └── tracer/              # Performance tracing (Timer decorator/context manager)
├── tests/                   # Test suite mirroring tools/ structure
├── docs/                    # MkDocs documentation
├── .devcontainer/           # Dev Container configuration
├── .github/                 # GitHub Actions workflows and reusable actions
├── noxfile.py              # Task automation configuration
├── pyproject.toml          # Project metadata and dependencies
├── ruff.toml               # Ruff configuration
├── pyrightconfig.json      # Pyright type checking configuration
└── pytest.ini              # Pytest configuration
```

### Built-in Utility Modules

The `tools/` package provides production-ready utilities:

#### **Logger** - Dual-mode logging system
```python
from tools.logger import Logger, LogType

# Local development (colored console output)
logger = Logger(__name__, log_type=LogType.LOCAL)

# Google Cloud (structured JSON logging)
logger = Logger(__name__, log_type=LogType.GOOGLE_CLOUD, project="my-project")

logger.info("Application started")
```

#### **Configuration** - Environment-based settings
```python
from tools.config import Settings

settings = Settings()  # Loads from .env and .env.local
api_url = settings.api_prefix_v1
```

#### **Timer** - Performance monitoring
```python
from tools.tracer import Timer

# As context manager
with Timer("database_query"):
    result = db.query()  # Logs execution time automatically

# As decorator
@Timer("process_data")
def process_data(data):
    # Logs execution time when function completes
    return transform(data)
```

## ⚙️ Configuration

### Ruff Configuration

Ruff replaces multiple tools (Black, isort, Flake8, pydocstyle, pyupgrade, autoflake) with a single, fast tool.

Key settings in `ruff.toml`:
- **Line length**: 88 (Black-compatible)
- **Target Python**: 3.14
- **Rules**: ALL enabled by default with specific exclusions
- **Test files**: Exempt from `INP001` (namespace packages) and `S101` (assert usage)

See [Ruff documentation](https://docs.astral.sh/ruff/) for customization options.

### Pyright Configuration

Type checking configured in `pyrightconfig.json`:
- **Python version**: 3.14
- **Mode**: Standard type checking
- **Include**: `tools/` package
- **Virtual environment**: `.venv`

### Pytest Configuration

Testing configured in `pytest.ini`:
- **Coverage requirement**: 75% minimum (including branch coverage)
- **Test file pattern**: `test__*.py`
- **Coverage reports**: HTML and terminal
- **Import mode**: importlib

## 🔄 CI/CD

Automated workflows in `.github/workflows/`:

| Workflow | Purpose |
|----------|---------|
| `docker.yml` | Validate Docker build |
| `devcontainer.yml` | Validate Dev Container configuration |
| `format.yml` | Check code formatting with Ruff |
| `lint.yml` | Run Pyright and Ruff linting |
| `test.yml` | Run test suite with coverage |
| `gh-deploy.yml` | Deploy documentation to GitHub Pages |
| `pr-agent.yml` | Automated PR reviews |
| `publish-devcontainer.yml` | Publish Dev Container image |

## 🎨 VSCode Configuration

The Dev Container includes these pre-configured extensions:

**Python Development**:
- Ruff, Pyright, Python, autodocstring, python-indent

**Code Quality**:
- GitLens, Error Lens, indent-rainbow, trailing-spaces

**File Support**:
- YAML, TOML, Markdown, Docker, Material Icon Theme

**Editor Settings**:
- Format on save (Python, JSON, YAML, TOML, Dockerfile)
- Auto-trim trailing whitespace
- Auto-insert final newline

> **Note**: If Ruff formatting doesn't work, reload the window: `Cmd+Shift+P` → "Developer: Reload Window"

## 🍪 Cookiecutter Templates

Use this repository as a base to generate project-specific templates:

```bash
uv run cookiecutter <template-url>
```

**Recommended templates**:

- **Data Science**: [cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science)
- **FastAPI**: [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)
- **Django**: [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
- **Flask**: [cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)

## 📖 Documentation

Comprehensive documentation is available at [https://a5chin.github.io/python-uv](https://a5chin.github.io/python-uv)

Topics covered:
- Getting started guides (Docker, VSCode, Dev Containers)
- Tool configurations (uv, Ruff, Pyright, pre-commit)
- Testing strategies
- Using the `tools/` utilities (config, logger, tracer)
- Use cases (Jupyter, FastAPI, OpenCV)

## 🌿 Branches

- **[main](https://github.com/a5chin/python-uv/tree/main)** - Current production-ready template
- **[jupyter](https://github.com/a5chin/python-uv/tree/jupyter)** - Archived Jupyter-specific configuration
- **[rye](https://github.com/a5chin/python-uv/tree/rye)** - Archived Rye package manager version

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This template leverages these excellent tools:
- [uv](https://github.com/astral-sh/uv) by Astral
- [Ruff](https://github.com/astral-sh/ruff) by Astral
- [Pyright](https://github.com/microsoft/pyright) by Microsoft
- [nox](https://nox.thea.codes/) for task automation
- [pytest](https://pytest.org/) for testing
