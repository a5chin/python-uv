ARG DEBIAN_VERSION=bookwork
ARG VARIANT=3.12


FROM python:$VARIANT-slim-$DEBIAN_VERSION
LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

ARG UV_VERSION=0.5.4

ENV PYTHONDONTWRITEBYTECODE=True
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:$UV_VERSION /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project
