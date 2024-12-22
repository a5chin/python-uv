This repository provides jupyter branch for Jupyter Notebook.
What a surprise! You can use it with just the following commands!
```sh
git switch jupyter
```

## devcontainer.json
```{.json title=".devcontainer/devcontainer.json" hl_lines=23}
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
                "ms-toolsai.jupyter",
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

## settings.json
```{.json title=".vscode/settings.json" hl_lines=2-6}
{
    "notebook.codeActionsOnSave": {
        "notebook.source.fixAll": "explicit",
        "notebook.source.organizeImports": "explicit"
    },
    "notebook.formatOnSave.enabled": true,
    "python.defaultInterpreterPath": "/home/vscode/.venv/bin/python",
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.tabSize": 4
    }
}
```
