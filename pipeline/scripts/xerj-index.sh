#!/usr/bin/env bash
# Start the local XERJ node (if needed) and (re)index oneup-studio + reference repos.
# Usage: pipeline/scripts/xerj-index.sh [project|ref|all]   (default: all)
# Docs: docs/conventions/search-xerj.md
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
export XERJ_DISABLE_FEEDBACK=true          # no automatic field reports
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
REF="${XERJ_REF_DIR:-/workspace/reference-repos}"
DATA="${XERJ_DATA_DIR:-$HOME/xerj-data}"   # must stay OUTSIDE indexed folders
command -v xerj >/dev/null || { echo "xerj not installed: curl -fsSL https://xerj.org/get -o /tmp/get.sh && less /tmp/get.sh && sh /tmp/get.sh"; exit 1; }
if ! curl -s -m1 http://localhost:9200 >/dev/null; then
  mkdir -p "$DATA"; nohup xerj --insecure --data-dir "$DATA" >"$DATA.log" 2>&1 &
  for _ in $(seq 1 30); do curl -s -m1 http://localhost:9200 >/dev/null && break; sleep 1; done
fi
what="${1:-all}"
rc=0
if [[ $what == project || $what == all ]]; then
  xerj autoindex "$REPO" --prefix oneup --state-dir "$HOME/.xerj/state-oneup" --progress plain || rc=$?
  [[ $rc == 0 || $rc == 3 ]] || exit $rc   # exit 3 = completed-with-junk = OK
fi
if [[ $what == ref || $what == all ]] && [[ -d $REF ]]; then
  rc=0; xerj autoindex "$REF" --prefix ref --state-dir "$HOME/.xerj/state-ref" --progress plain || rc=$?
  [[ $rc == 0 || $rc == 3 ]] || exit $rc
fi
echo "done. search: xerj search --prefix oneup \"...\"  |  xerj search --prefix ref \"...\""
