ARG VARIANT=3.12
ARG BASE=slim-bookwork


FROM python:$VARIANT-$BASE AS builder
LABEL maintainer="a5chin <a5chin.origin+contact@gmain.com>"

ENV PYTHONDONTWRITEBYTECODE=True
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.5.4 /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project
