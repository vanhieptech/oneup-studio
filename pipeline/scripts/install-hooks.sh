#!/usr/bin/env bash
# Enable repo-managed git hooks (.githooks/pre-commit)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
chmod +x "$ROOT/.githooks/pre-commit"
git -C "$ROOT" config core.hooksPath .githooks
echo "Installed git hooks from .githooks/ (pre-commit active)"
