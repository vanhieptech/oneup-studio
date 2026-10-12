#!/usr/bin/env bash
# Sync trend research produced on the box into this repo, commit, push (rule-38).
# Flow: agent packs /workspace/oneup-studio-sync -> CopyFromBox to <repo>/../.oneup-sync/trends.tgz -> run this on the Mac.
# Usage: pipeline/scripts/sync-trends.sh [--no-push]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"; INBOX="$REPO/../.oneup-sync"; PKG="$INBOX/trends.tgz"
[ -f "$PKG" ] || { echo "no package at $PKG"; exit 0; }
TMP="$(mktemp -d)"; tar xzf "$PKG" -C "$TMP"
[ -d "$TMP/research/trends" ] || { echo "package has no research/trends"; exit 1; }
mkdir -p "$REPO/research/trends"
# daily folders: add only, never overwrite an existing day; ingest.md: box version wins (it is the rolling library)
for d in "$TMP"/research/trends/20*/; do day=$(basename "$d"); [ -e "$REPO/research/trends/$day" ] || cp -R "$d" "$REPO/research/trends/$day"; done
[ -f "$TMP/research/trends/ingest.md" ] && cp "$TMP/research/trends/ingest.md" "$REPO/research/trends/ingest.md"
rm -rf "$TMP"; mv "$PKG" "$PKG.done-$(date +%Y%m%d%H%M)"
cd "$REPO"; git add research/trends
if git diff --cached --quiet; then echo "nothing new"; exit 0; fi
git commit -qm "trends: sync $(ls -d research/trends/20* | tail -1 | xargs basename) digest(s) from box"
[ "${1:-}" = "--no-push" ] || git push origin main
git log --oneline -1
