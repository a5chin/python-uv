ARG UV_VERSION=latest
ARG DEBIAN_VERSION=bookworm

FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv
FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VERSION

LABEL maintainer="Bob Tanner <tanner@real-time.com>"

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libonig-dev \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=uv --chown=vscode: /uv /uvx /bin/

EXPOSE 8000
