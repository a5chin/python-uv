ARG UV_VERSION=latest
ARG DEBIAN_VERSION=bookworm

ARG UBUNTU_VERSION=noble
ARG HADOLINT=v2.12.0

FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv
FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VERSION
# FROM ubuntu:$UBUNTU_VERSION

LABEL maintainer="Bob Tanner <tanner@real-time.com>"

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libonig-dev \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    curl \
    git \
    git-lfs \
    less \
    zip \
    unzip \
    vim-tiny \
    openssh-client \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG USERNAME=vscode
ARG USER_UID=3000
ARG USER_GID=3000

RUN echo "vscode ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vscode  \
    && if ! getent group vscode; then groupadd --gid 3000 vscode; fi \
    && if ! id -u vscode > /dev/null 2>&1; then useradd --uid 3000 --gid 3000 -m vscode; fi

COPY --from=uv --chown=vscode: /uv /uvx /bin/

EXPOSE 8000
