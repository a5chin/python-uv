ARG VARIANT=3.12
FROM python:${VARIANT} AS builder

ENV PYTHONDONTWRITEBYTECODE=True
ENV UV_LINK_MODE=copy

WORKDIR /opt

COPY pyproject.toml uv.lock ./

# hadolint ignore=DL3013,DL3042
RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync --frozen


FROM python:${VARIANT}-slim
COPY --from=builder /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages

ENV PYTHONUNBUFFERED=True

WORKDIR /
