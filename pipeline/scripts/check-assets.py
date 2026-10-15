#!/usr/bin/env python3
"""rule-59 / L-023: fail if @hi.oneup project files live outside the repo.
Scans known external dirs on the box; a file passes only if an identical copy (sha256)
is tracked in the repo or listed in media/MANIFEST.json. Usage: check-assets.py [--list]"""
import hashlib, json, re, subprocess, sys
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
else:
    print(f"PASS rule-59: {len(cands)} external file(s) all mirrored in repo")

# ---- rule-65 / L-034: storage convention (docs/conventions/storage.md) ----
sys.path.insert(0, str(ROOT / "pipeline")); import paths as P
DUP_EXEMPT = ("skills/", "video-engine/public/voice/", "brand/omi-exports/", "refs/")
DUP_EXEMPT_NAMES = {"package.json", "package-lock.json", "hyperframes.json", ".gitignore", "README.md", "AGENTS.md", "CLAUDE.md"}
import re as _re
DUP_EXEMPT_RE = _re.compile(r"(\.tpl$|^logs/runs/|/final/cover\.png$|/v\d+/)")  # templates, run logs, L-020 cover = template render, versioned snapshots
tracked = [f for f in subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True).stdout.split("\0") if f and (ROOT / f).is_file()]
errs = []
for f in tracked:
    top = f.split("/")[0]
    if top not in P.TOP_ALLOWED and not top.startswith("."): errs.append(f"outside allowed top-level dirs: {f}")
    name = f.rsplit("/", 1)[-1]
    parts = f.split("/")
    if f.startswith(("content/clips/", "content/archive/")) and len(parts) >= 4 and parts[3] not in P.CLIP_TOP_ALLOWED:
        errs.append(f"clip layout: only final/, archive/, README.md allowed in {parts[2]}/ (drafts → archive/): {f}")
    if f.startswith("content/clips/") and len(parts) == 3:
        errs.append(f"stray file directly in content/clips/: {f}")
    if f.startswith("content/clips/") and "/final/" in f and re.search(r"(-draft|-v\d+(\.\d+)?-draft)\.md$", name):
        errs.append(f"draft inside final/ (move to archive/): {f}")
    if f.startswith(("content/", "samples/")) and (Path(f).suffix.lower() in P.SHARED_EXT or name in P.SHARED_NAMES):
        errs.append(f"shared-type file inside a clip/sample folder (use brand/ or assets/, synced by sync-shared.py): {f}")
by = {}
for f in tracked:
    if f.startswith(DUP_EXEMPT) or f.rsplit("/", 1)[-1] in DUP_EXEMPT_NAMES or DUP_EXEMPT_RE.search(f) or (ROOT / f).stat().st_size < 64: continue
    by.setdefault(sha(ROOT / f), []).append(f)
for h, fs in by.items():
    if len(fs) > 1: errs.append(f"duplicate content ({h[:10]}): {', '.join(fs)}")
# rule-66: archived clips must carry a complete post package; active clips may be incomplete
man = {e["path"]: e for e in json.loads((ROOT / "media/MANIFEST.json").read_text())}
for cd in sorted(P.ARCHIVE.glob("*/")) if P.ARCHIVE.exists() else []:
    rel = cd.relative_to(ROOT).as_posix()
    for need in P.POST_PACKAGE:
        if not (cd / need).is_file(): errs.append(f"rule-66 archived {rel}: missing {need}")
    ap = cd / "final/approved.json"
    if ap.is_file():
        a = json.loads(ap.read_text())
        if a.get("approved") != "duyệt": errs.append(f"rule-66 archived {rel}: approved.json needs \"approved\": \"duyệt\" (Hiệp's word)")
        for k in ("title", "video_full", "video_720"):
            if not a.get(k): errs.append(f"rule-66 archived {rel}: approved.json missing {k}")
        for k in ("video_full", "video_720"):
            if a.get(k) and a[k] not in man: errs.append(f"rule-66 archived {rel}: {k} {a[k]} not in media/MANIFEST.json")
    post = cd / "final/post.md"
    if post.is_file():
        t = post.read_text()
        if "caption" not in t.lower() or not re.search(r"#\w", t): errs.append(f"rule-66 archived {rel}: post.md needs caption + hashtags")
if errs:
    print(f"FAIL rule-65: {len(errs)} storage violation(s):"); [print("  ", e) for e in errs[: (None if "--list" in sys.argv else 40)]]; sys.exit(1)
print(f"PASS rule-65: {len(tracked)} tracked files follow docs/conventions/storage.md (no shared files in clips, no duplicates)")
