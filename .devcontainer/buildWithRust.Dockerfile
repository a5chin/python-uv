FROM debian:bookworm-slim AS builder

ENV CARGO_HOME="/opt/.cargo"
ENV RUSTUP_HOME="/opt/.rustup"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

WORKDIR /opt

# The installer requires curl (and certificates) to download the release archive
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl

# Run uv and rustup installer
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

ENV CARGO_HOME="/opt/.cargo"
ENV RUSTUP_HOME="/opt/.rustup"
ENV PATH="$CARGO_HOME/bin/:$PATH"
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /opt

COPY --from=builder --chown=vscode: $CARGO_HOME $CARGO_HOME
COPY --from=builder $RUSTUP_HOME $RUSTUP_HOME
