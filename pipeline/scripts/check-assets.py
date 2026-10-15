#!/usr/bin/env python3
"""rule-59 / L-023: fail if @hi.oneup project files live outside the repo.
Scans known external dirs on the box; a file passes only if an identical copy (sha256)
is tracked in the repo or listed in media/MANIFEST.json. Usage: check-assets.py [--list]"""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
EXTERNAL = [Path("/workspace/oneup-studio-sync"), Path("/workspace/hi-oneup")]
WS_MD = ["hi-oneup*", "howtolivebetter*", "make-video*", "oneup-*", "trend-digest*", "trend-routine*"]
SKIP = {"node_modules", ".git", ".bundle-cache", "__pycache__"}
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
known = set()
files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True).stdout.split("\0")
for f in files:
    p = ROOT / f
    if f and p.is_file(): known.add(sha(p))
m = ROOT / "media/MANIFEST.json"
if m.exists(): known |= {e["sha256"] for e in json.loads(m.read_text())}
cands = []
for d in EXTERNAL:
    if d.exists(): cands += [p for p in d.rglob("*") if p.is_file() and not SKIP & set(p.parts)]
for g in WS_MD: cands += [p for p in Path("/workspace").glob(g) if p.is_file() and p.suffix == ".md"]
bad = [p for p in cands if sha(p) not in known]
if bad:
    print(f"FAIL rule-59: {len(bad)} project file(s) outside repo {ROOT} not committed/manifested:")
    for p in bad[: (None if "--list" in sys.argv else 20)]: print("  ", p)
    sys.exit(1)
print(f"PASS rule-59: {len(cands)} external file(s) all mirrored in repo")
