## Dockerfile
```{.dockerfile title=".devcontainer/Dockerfile" hl_lines=15}
ARG UV_VERSION=0.5.11
ARG DEBIAN_VERSION=bookworm


FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv


FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VERSION
LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # For OpenCV etc...
    libgl1 libglib2.0-0 \
    # To remove the image size, it is recommended refresh the package cache as follows
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv --chown=vscode: /uv /uvx /bin/
```

## uv command
```sh
uv add opencv-python
```

## pyproject.toml
```{.toml title="pyproject.toml" hl_lines=3}
[project]
dependencies = [
    "opencv-python>=4.10.0.84",
]
```
