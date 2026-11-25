#!/usr/bin/env python3
"""Print the next free DL-NNN or L-NNN id across local working tree and origin/main.

Usage:
  python3 pipeline/scripts/next-id.py DL
  python3 pipeline/scripts/next-id.py L
  python3 pipeline/scripts/next-id.py          # prints both
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGETS = {
    "DL": ("logs/decision-log.md", re.compile(r"(?:^\|\s*|^#{2,3}\s+)DL-(\d{3})\b", re.M)),
    "L": ("logs/lessons.md", re.compile(r"(?:^\|\s*|^#{2,3}\s+)L-(\d{3})\b", re.M)),
}


def max_id(kind: str) -> int:
    rel, pat = TARGETS[kind]
    nums = [int(m) for m in pat.findall((ROOT / rel).read_text(encoding="utf-8", errors="ignore"))]
    # Also inspect origin/main if present so parallel branches don't collide
    r = subprocess.run(["git", "show", f"origin/main:{rel}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0 and r.stdout:
        nums += [int(m) for m in pat.findall(r.stdout)]
    return max(nums, default=0)


def main() -> int:
    kinds = [sys.argv[1].upper()] if len(sys.argv) > 1 else ["DL", "L"]
    for k in kinds:
        if k not in TARGETS:
            sys.stderr.write(f"Unknown kind {k!r} (expected DL or L)\n")
            return 2
        nxt = max_id(k) + 1
        print(f"{k}-{nxt:03d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
