#!/bin/bash

set -e

timezone_setup() {
    local TZ=${TZ}

    if [ -z "$TZ" ]; then
        echo "==> Timezone not set"
        return
    fi

    echo "==> Setting timezone to: $TZ"
    sudo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
    sudo dpkg-reconfigure -f noninteractive tzdata
}

echo "==> Working directory: $(pwd)"

# Load environment variables from .env file
#
echo "==> Load environment variables from .env file"
if [ -f ".env" ]; then
    set -o allexport
    source ./.env
    set +o allexport
fi

# Timezone setup
#
timezone_setup

echo "==> Customize git user configuration"
git config --global core.eol lf
git config --global core.autocrlf false
git config --global http.sslVerify false
git config --global core.editor "code --wait"
git config --global --add safe.directory /workspace

echo "==> Setting git user.name: '${GIT_USER_EMAIL}'"
git config --global user.email "${GIT_USER_EMAIL}"

echo "==> Setting git user.email: '${GIT_USER_NAME}'"
git config --global user.name "${GIT_USER_NAME}"

echo "==> uv sync --frozen"
uv sync --frozen
