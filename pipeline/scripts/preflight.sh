#!/usr/bin/env bash
# preflight.sh — the one gate every agent runs before committing (Claude, Antigravity, Cursor, Grok, humans).
# Single source of truth for the checks: .githooks/pre-commit just calls this script, so agents without
# a native hook system (Grok) get exactly the same gate by running it by hand.
#
#   bash pipeline/scripts/preflight.sh            # all checks (video-engine too when node_modules exists)
#   bash pipeline/scripts/preflight.sh --staged   # pre-commit mode: video-engine only if staged files touch it
#
# Runs every check, prints a summary, exits 1 if any check failed. No absolute paths: the repo root comes
# from git, the Node toolchain from pipeline/paths.py (NODE22_BIN / PATH / nvm).
set -uo pipefail
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT"
MODE="${1:-all}"
FAILED=()
run() { local name="$1"; shift; echo "[preflight] $name"; if "$@"; then echo "[preflight] ok: $name"; else echo "[preflight] FAIL: $name"; FAILED+=("$name"); fi; }

run "check-assets.py" python3 pipeline/scripts/check-assets.py
run "unittest tests/" python3 -m unittest discover -s tests
run "unittest pipeline/tests/" python3 -m unittest discover -s pipeline/tests

want_ve=1
if [ "$MODE" = "--staged" ]; then
  git diff --cached --name-only | grep -q '^video-engine/' || want_ve=0
fi
if [ "$want_ve" = 1 ]; then
  NODE_DIR="$(python3 -c 'import sys; sys.path.insert(0, "pipeline"); import paths; print(paths.NODE_BIN)')"
  export PATH="$NODE_DIR:$PATH"
  if [ -d video-engine/node_modules ]; then
    run "video-engine typecheck" bash -c 'cd video-engine && npm run --silent typecheck'
    run "video-engine vitest" bash -c 'cd video-engine && npm test --silent'
  else
    echo "[preflight] skip video-engine: no video-engine/node_modules (run: cd video-engine && npm ci)"
    [ "$MODE" = "--staged" ] && FAILED+=("video-engine (node_modules missing)")
  fi
else
  echo "[preflight] skip video-engine: no staged changes under video-engine/"
fi

if [ "${#FAILED[@]}" -gt 0 ]; then
  echo "[preflight] FAILED (${#FAILED[@]}): ${FAILED[*]}"
  exit 1
fi
echo "[preflight] all checks passed"
