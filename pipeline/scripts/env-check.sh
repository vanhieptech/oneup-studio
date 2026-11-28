#!/usr/bin/env bash
# env-check.sh — print the local toolchain this repo resolves (via pipeline/paths.py) and what is missing.
# Works for every agent and for non-interactive remote shells (no nvm/venv activation needed).
# Secrets are reported only as set/missing, never printed.
#   bash pipeline/scripts/env-check.sh            # report, exit 0
#   bash pipeline/scripts/env-check.sh --strict   # exit 1 if a required tool is missing
set -uo pipefail
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT"
exec python3 - "$@" <<'PY'
import os, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, "pipeline"); import paths as P
strict = "--strict" in sys.argv
rows, missing_required = [], []
def ver(cmd):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip().splitlines()[0][:60]
    except Exception: return ""
def check(name, path, required=False, version=None):
    ok = bool(path) and (Path(path).exists() or bool(shutil.which(str(path))))
    v = ver(version) if (ok and version) else ""
    rows.append((("ok  " if ok else ("MISS" if required else "--  ")), name, str(path or "-"), v))
    if required and not ok: missing_required.append(name)
node = Path(P.NODE_BIN) / "node"
check("repo root", str(P.ROOT), True)
check("ONEUP_TOOLS_DIR", str(P.TOOLS_DIR), False)
check("python3", sys.executable, True, [sys.executable, "--version"])
check("git", shutil.which("git"), True, ["git", "--version"])
check("node (NODE_BIN)", str(node), True, [str(node), "--version"])
check("npm", str(Path(P.NODE_BIN) / "npm"), False)
check("video-engine/node_modules", str(P.VE / "node_modules"), False)
check("ffmpeg", P.FFMPEG_BIN, True, [P.FFMPEG_BIN, "-version"])
check("ffprobe", P.FFPROBE_BIN, False)
check("F5_PYTHON", P.F5_PYTHON, False)
check("ASR_PYTHON", P.ASR_PYTHON, False)
check("VIENEU_PYTHON", P.VIENEU_PYTHON, False)
check("F5_CKPT_DIR", P.F5_CKPT_DIR, False)
check("F5_VOCODER_DIR", P.F5_VOCODER_DIR, False)
check("VOICE_WORK_DIR", str(P.VOICE_WORK_DIR), False)
check("agy (Antigravity CLI)", P.AGY_BIN, False)
check("gemini CLI", P.GEMINI_BIN, False)
check("tinyfish", P.TINYFISH_BIN, False)
check("ego-browser", P.EGO_BROWSER_BIN, False)
for tool in ("gh", "rg", "xerj", "claude", "cursor-agent"):
    check(tool, shutil.which(tool) or "", False)
w = max(len(r[1]) for r in rows)
print(f"oneup-studio env-check (root: {P.ROOT})")
for s, n, p, v in rows: print(f"  {s} {n:<{w}}  {p}{('  [' + v + ']') if v else ''}")
print("secrets (set/missing only, values never printed):")
for k in ("APIFY_TOKEN", "GEMINI_API_KEY"):
    print(f"  {'set ' if P.tools_env(k) else '--  '} {k}")
xk = Path.home() / "xerj-data/admin.key"
print(f"  {'set ' if (os.environ.get('XERJ_API_KEY') or xk.exists()) else '--  '} XERJ_API_KEY (env or ~/xerj-data/admin.key)")
hp = subprocess.run(["git", "config", "core.hooksPath"], capture_output=True, text=True).stdout.strip()
print(f"git hooks: core.hooksPath={hp or '(unset)'}" + ("" if hp == ".githooks" else "  -> pre-commit not installed; run checks by hand: bash pipeline/scripts/preflight.sh"))
if missing_required:
    print("MISSING required: " + ", ".join(missing_required))
    sys.exit(1 if strict else 0)
print("required tools: all present")
PY
