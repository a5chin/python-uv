ARG UV_VERSION=0.5.4
ARG TAG=bookworm


FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv


FROM mcr.microsoft.com/vscode/devcontainers/base:$TAG
LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

COPY --from=uv --chown=vscode: /uv /uvx /bin/
