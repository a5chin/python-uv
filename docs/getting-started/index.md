# Getting Started

Welcome! This guide will help you set up your development environment using this Python template. You'll be up and running in just a few minutes.

## Prerequisites

Before you begin, you'll need to install the following tools on your machine:

1. **[Docker Desktop](docker.md)** - Container platform for running the development environment
2. **[Visual Studio Code](vscode.md)** - Code editor with excellent Python support
3. **[Dev Containers Extension](devcontainer.md)** - VSCode extension for container-based development

## Setup Options

You have three ways to set up your development environment. Choose the one that best fits your workflow:

### Option 1: Dev Container (Recommended)

The **Dev Container** approach provides a fully configured, consistent development environment that works the same on any machine.

**Pros:**

- ✅ Zero configuration - everything is pre-configured
- ✅ Consistent across all team members
- ✅ Isolated from your host system
- ✅ All dependencies included
- ✅ Pre-installed VSCode extensions

**Setup steps:**

1. Install [Docker Desktop](docker.md)
2. Install [VSCode](vscode.md) and the [Dev Containers extension](devcontainer.md)
3. Clone this repository
4. Open the folder in VSCode
5. Click "Reopen in Container" when prompted

That's it! Your environment is ready to use.

### Option 2: Docker Only

If you prefer to use Docker without VSCode integration, you can use the standalone Docker setup.

**Pros:**

- ✅ Works with any editor
- ✅ Consistent environment
- ✅ Easy to integrate with CI/CD

**Setup steps:**

```bash
# Clone the repository
git clone https://github.com/a5chin/python-uv.git
cd python-uv

# Build the Docker image
docker build -t python-uv .

# Run the container with the source mounted at /app (the image's WORKDIR).
# The extra volume keeps the virtual environment that was installed in the image.
docker run -it --rm -v "$(pwd)":/app -v /app/.venv python-uv bash

# Inside the container, dependencies are already installed
uv run nox -s test
```

### Option 3: Local Installation

For advanced users who prefer to work directly on their host machine.

**Pros:**

- ✅ No Docker overhead
- ✅ Direct access to system resources
- ✅ Faster startup times

**Requirements:**

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager

**Setup steps:**

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/a5chin/python-uv.git
cd python-uv

# Install dependencies
uv sync

# Install pre-commit hooks (optional but recommended)
uv run pre-commit install
```

## Verify Your Setup

Once your environment is set up, verify that everything is working:

```bash
# Check uv is available
uv --version

# Install dependencies
uv sync

# Run tests
uv run nox -s test

# Format code
uv run nox -s fmt -- --ruff

# Run linters
uv run nox -s lint -- --ruff --ty
```

If all commands complete successfully, you're ready to start developing! 🎉 See [Task Automation with nox](../guides/index.md#task-automation-with-nox) for all sessions and flags.

## Detailed Setup Guides

For step-by-step instructions with screenshots, see the detailed guides:

- **[Docker Setup Guide](docker.md)** - Install Docker Desktop on your platform
- **[VSCode Setup Guide](vscode.md)** - Configure Visual Studio Code
- **[Dev Container Guide](devcontainer.md)** - Set up the Dev Container extension

## Troubleshooting

### Ruff formatting not working in VSCode

If Ruff formatting doesn't activate automatically:

1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Developer: Reload Window"
3. Press Enter

This reloads the VSCode window and should activate the Ruff extension.

### Docker container won't start

Make sure Docker Desktop is running:

- **macOS**: Check for the Docker icon in your menu bar
- **Windows**: Check for the Docker icon in your system tray
- **Linux**: Run `sudo systemctl status docker`

### Permission errors with Docker

On Linux, you may need to add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in for the changes to take effect.

## Using as a Template

When you start a new project from this template:

1. Update the project name and description in `pyproject.toml` (see [Customizing for Your Project](../configurations/index.md#customizing-for-your-project)).
2. Add project-specific configuration by extending `Settings` (see [Extending Settings](../guides/tools/config.md#extending-settings)).
3. Use the utilities in `tools/`, or remove them if you do not need them. If you remove or add packages, update `include` in `ty.toml` (see [ty Configurations](../configurations/ty.md)).
4. Put shared defaults in `.env.local` (committed) and secrets in `.env` (not committed) (see [Environment Files](../guides/tools/config.md#environment-files)).
5. Customize Ruff rules in `ruff.toml` only when needed (see [Ruff Configurations](../configurations/ruff.md)).

## Next Steps

Now that your environment is set up, explore the guides to learn how to use the tools:

- **[Development Guides](../guides/index.md)** - Learn how to use uv, Ruff, pytest, and more
- **[Built-in Utilities](../guides/tools/index.md)** - Explore the logger, config, and tracer modules
- **[Configuration Reference](../configurations/index.md)** - Understand tool configurations
- **[Use Cases](../usecases/index.md)** - See practical examples (Jupyter, FastAPI, OpenCV)
