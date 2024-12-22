# uv Configations

!!! TIP
    Official documentation for uv is available at [https://docs.astral.sh/uv](https://docs.astral.sh/uv)

## Virtual Environment
Set the `UV_PROJECT_ENVIRONMENT` not to create a virtual environment in the project directory.

```{.dockerfile title=".devcontainer/Dockerfile" hl_lines="34"}
{
    "name": "uv",
    "build": {
        "context": "..",
        "dockerfile": "Dockerfile",
        "args": {
            "UV_VERSION": "0.5.11",
            "DEBIAN_VERSION": "bookworm"
        }
    },
    "features": {
        "ghcr.io/dhoeric/features/hadolint:1": {}
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "charliermarsh.ruff",
                "exiasr.hadolint",
                "kevinrose.vsc-python-indent",
                "mosapride.zenkaku",
                "ms-azuretools.vscode-docker",
                "ms-python.python",
                "njpwerner.autodocstring",
                "redhat.vscode-yaml",
                "shardulm94.trailing-spaces",
                "tamasfe.even-better-toml"
            ]
        }
    },
    "containerEnv": {
        "DISPLAY": "dummy",
        "PYTHONUNBUFFERED": "True",
        "UV_LINK_MODE": "copy",
        "UV_PROJECT_ENVIRONMENT": "/home/vscode/.venv"
    },
    "postCreateCommand": "uv sync --frozen",
    "postStartCommand": "uv run pre-commit install",
    "remoteUser": "vscode"
}

```
