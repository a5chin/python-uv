ARG VARIANT=3.12
FROM python:${VARIANT} AS builder

ENV PYTHONDONTWRITEBYTECODE=True

WORKDIR /opt
COPY pyproject.toml requirements.lock ./

# hadolint ignore=DL3013,DL3042
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock


FROM python:${VARIANT}-slim
COPY --from=builder /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages

ENV PYTHONUNBUFFERED=True

WORKDIR /
