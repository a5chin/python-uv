# uv Configurations

!!! TIP
    Official documentation for uv is available at [https://docs.astral.sh/uv](https://docs.astral.sh/uv)

## Virtual Environment
Set the `UV_PROJECT_ENVIRONMENT` not to create a virtual environment in the project directory.

```json title=".devcontainer/devcontainer.json" hl_lines="10-24 53 55"
{
    "name": "uv",
    "dockerComposeFile": "../.devcontainer/docker-compose.yml",
    "service": "vscode",
    "runServices": [
        "vscode"
    ],
    "workspaceFolder": "/workspace",
    "mounts": [
        {
            "source": "cache-${devcontainerId}",
            "target": "/home/${remoteUser}/.cache",
            "type": "volume"
        },
        {
            "source": "${localEnv:HOME}/.ssh",
            "target": "/home/${remoteUser}/.ssh",
            "type": "bind"
        },
        {
            "source": "venv-${devcontainerId}",
            "target": "${containerWorkspaceFolder}/.venv",
            "type": "volume"
        }
    ],
    "features": {
        "ghcr.io/dhoeric/features/hadolint:1": {}
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "astral-sh.ty",
                "charliermarsh.ruff",
                "dorzey.vscode-sqlfluff",
                "exiasr.hadolint",
                "kevinrose.vsc-python-indent",
                "mosapride.zenkaku",
                "ms-azuretools.vscode-docker",
                "ms-python.python",
                "ms-python.vscode-pylance",
                "ms-toolsai.jupyter",
                "njpwerner.autodocstring",
                "redhat.vscode-yaml",
                "shardulm94.trailing-spaces",
                "streetsidesoftware.code-spell-checker",
                "tamasfe.even-better-toml",
                "yzhang.markdown-all-in-one"
            ]
        }
    },
    "containerEnv": {
        "DISPLAY": "dummy",
        "UV_PROJECT_ENVIRONMENT": "${containerWorkspaceFolder}/.venv"
    },
    "updateContentCommand": "sudo chown -R vscode ${containerWorkspaceFolder}/.venv /home/${remoteUser}/.ssh",
    "postCreateCommand": "uv sync --frozen",
    "postStartCommand": "uv run pre-commit install",
    "remoteUser": "vscode"
}
```

### Key Configuration Details

**Mounts Section:**
- The `.venv` directory is stored in a Docker named volume (`venv-${devcontainerId}`) for better performance and isolation
- SSH keys from the host (`${localEnv:HOME}/.ssh`) are bind-mounted to enable git operations with SSH authentication

**Environment Variables:**
- `UV_PROJECT_ENVIRONMENT` is set to `${containerWorkspaceFolder}/.venv` to ensure uv uses the mounted volume

**Update Content Command:**
- `updateContentCommand` sets proper ownership of `.venv` and `.ssh` directories to the `vscode` user after container updates

This configuration eliminates the need for volume definitions in `docker-compose.yml`, as volumes are managed directly through the devcontainer `mounts` section.
