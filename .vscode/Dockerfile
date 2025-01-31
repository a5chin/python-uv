FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye

WORKDIR /opt

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl && \
    rm -rf /var/lib/apt/lists/*

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

COPY ./.python-version ./pyproject.toml ./requirements* ./
RUN rye pin "$(cat .python-version)" && \
    rye sync

RUN chown -R vscode $RYE_HOME
