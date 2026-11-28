#!/usr/bin/env python3
"""rule-59 / L-023: fail if @hi.oneup project files live outside the repo.
Scans external dirs listed in ONEUP_EXTERNAL_DIRS (os.pathsep-separated; empty by default, the old agent-box
sync dirs are gone); a file passes only if an identical copy (sha256) is tracked in the repo or
listed in media/MANIFEST.json. No agent-specific path is hardcoded. Usage: check-assets.py [--list]"""
import hashlib, json, os, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
EXTERNAL = [Path(d).expanduser() for d in os.environ.get("ONEUP_EXTERNAL_DIRS", "").split(os.pathsep) if d.strip()]
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
for d in EXTERNAL:
    if d.is_dir():
        for g in WS_MD: cands += [p for p in d.glob(g) if p.is_file() and p.suffix == ".md"]
bad = [p for p in cands if sha(p) not in known]
if bad:
    print(f"FAIL rule-59: {len(bad)} project file(s) outside repo {ROOT} not committed/manifested:")
    for p in bad[: (None if "--list" in sys.argv else 20)]: print("  ", p)
    sys.exit(1)
else:
    print(f"PASS rule-59: {len(cands)} external file(s) all mirrored in repo")

# ---- rule-65 / L-034: storage convention (docs/conventions/storage.md) ----
sys.path.insert(0, str(ROOT / "pipeline")); import paths as P
DUP_EXEMPT = ("skills/", "video-engine/public/voice/", "brand/omi-exports/", "refs/", "resources/refs/")
DUP_EXEMPT_NAMES = {"package.json", "package-lock.json", "hyperframes.json", ".gitignore", "README.md", "AGENTS.md", "CLAUDE.md", "tokens.css"}
import re as _re
DUP_EXEMPT_RE = _re.compile(r"(\.tpl$|^logs/runs/|/final/cover\.png$|/v\d+/|/qa-v\d+-render/|/apify/comments-merged\.json$)")  # templates, run logs, L-020 cover, versioned snapshots, QA frames, single-batch merged comments
# Historical duplicate DL-069 (2026-11-08 @vanhiep.tech & 2026-11-25 clip-05 archive) is frozen and must NOT be renumbered.
HIST_DUP_DL = {"DL-069"}
MEDIA_EXT = {".mp4", ".mov", ".wav", ".m4a", ".mp3", ".webm", ".mkv"}
MAX_TRACKED_MEDIA_BYTES = 2 * 1024 * 1024
# Pre-existing legacy >2MB media already in git history (grandfathered; all NEW >2MB media in content/ or channels/ must go to media/ + MANIFEST.json)
LEGACY_LARGE_MEDIA = {
    "content/archive/clip-05-hoc-mot-dem/archive/v4-final/voice-only-c05v4.wav",
    "content/archive/clip-02-procrastination-discomfort/final/preview/clip-02-final-preview.mp4",
    "content/archive/clip-02-procrastination-discomfort/final/preview/clip-02-hook-preview.mp4",
    "content/archive/clip-04-gap-sach-tu-kiem/final/voice-only-c04v16c.wav",
    "content/archive/clip-04-gap-sach-tu-kiem/final/voice-only-c04v18.wav",
    "content/archive/clip-04-gap-sach-tu-kiem/final/voice-track-c04v18.wav",
    "content/samples/lab/motion-100/preview/01-hook-breath.mp4",
    "content/samples/lab/motion-100/preview/01-hook-on-aroll.mp4",
    "content/samples/lab/motion-100/preview/01-hook-padded.mp4",
    "content/samples/lab/motion-100/preview/01-hook-scrim-plus-aroll-blur.mp4",
    "content/samples/lab/motion-100/preview/01-hook-scrim.mp4",
    "content/samples/lab/motion-100/preview/02-d01-on-aroll.mp4",
    "content/samples/lab/motion-100/preview/03-l3-on-aroll.mp4",
    "content/samples/lab/motion-100/preview/04-q-on-aroll.mp4",
    "content/samples/lab/motion-100/preview/05-l3-on-aroll.mp4",
    "content/samples/lab/sample-f5/ab-v3.wav",
    "content/samples/lab/sample-f5/ab-v4.wav",
    "content/samples/lab/sample-f5/ab.wav",
    "content/samples/lab/sample-f5/filler-bank.wav",
    "content/samples/lab/sample-full/sample-full-w5-story.mp4",
    "content/samples/lab/sample-full/sample-full-w5.mp4",
    "content/samples/lab/sample-natural/old-vs-new-AB.wav",
    "content/samples/lab/video-engine/clip-01-story-b01-b03.mp4",
    "content/samples/lab/video-engine/debugging-story.mp4",
    "content/samples/lab/video-engine/sample-script.mp4",
}
tracked = [f for f in subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True).stdout.split("\0") if f and (ROOT / f).is_file()]
errs = []
final_drafts = {}
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
        final_drafts.setdefault("/".join(parts[:3]), []).append(f)
    if f.startswith(("content/", "samples/")) and (Path(f).suffix.lower() in P.SHARED_EXT or name in P.SHARED_NAMES):
        errs.append(f"shared-type file inside a clip/sample folder (use brand/ or assets/, synced by sync-shared.py): {f}")
    if f.startswith(("content/", "channels/")) and f not in LEGACY_LARGE_MEDIA and Path(f).suffix.lower() in MEDIA_EXT and (ROOT / f).stat().st_size > MAX_TRACKED_MEDIA_BYTES:
        errs.append(f"large media (>2MB) tracked in git (move to media/ + MANIFEST.json): {f}")
for clip, fs in sorted(final_drafts.items()):
    if len(fs) > 1:
        errs.append(f"more than one draft inside {clip}/final/ (keep the working draft, move the rest to archive/): {', '.join(fs)}")
# Guard against duplicate DL-NNN / L-NNN IDs (use pipeline/scripts/next-id.py before adding)
from collections import Counter
for log_rel, pat, allow in [
    ("logs/decision-log.md", r"(?:^\|\s*|^#{2,3}\s+)(DL-\d{3})\b", HIST_DUP_DL),
    ("logs/lessons.md", r"(?:^\|\s*|^#{2,3}\s+)(L-\d{3})\b", set()),
]:
    lp = ROOT / log_rel
    if lp.is_file():
        counts = Counter(re.findall(pat, lp.read_text(encoding="utf-8", errors="ignore"), re.M))
        for k, v in sorted(counts.items()):
            if v > 1 and k not in allow:
                errs.append(f"duplicate ID in {log_rel}: {k} appears {v}× (use pipeline/scripts/next-id.py)")
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
# front-matter (content-bot prompt): title, date, type, tags, status, source on every content .md
_fm = subprocess.run([sys.executable, str(ROOT / "pipeline/scripts/fm-backfill.py"), "--dry"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
errs += [f"front-matter missing {l.split(' ', 1)[1]}: {l.split(' ', 1)[0]} (run fm-backfill.py, then fill real values)" for l in _fm if l and not l[0].isdigit()]
for f in tracked + subprocess.run(["git", "ls-files", "-o", "--exclude-standard"], cwd=ROOT, capture_output=True, text=True).stdout.split():
    if f.endswith(".md") and (f.startswith(P.FM_STRICT_STATUS) or (f.startswith("content/clips/") and f.endswith("/final/script-final.md"))) and (ROOT / f).is_file():
        m = re.search(r"^status:\s*(\S+)", (ROOT / f).read_text().split("\n---", 1)[0], re.M)
        if not m or m.group(1).strip('"').rstrip(",") not in P.FM_STATUS: errs.append(f"front-matter status must be draft|ready|published: {f}")
if subprocess.run([sys.executable, str(ROOT / "pipeline/scripts/build-index.py"), "--check"], cwd=ROOT, capture_output=True).returncode:
    errs.append("INDEX.md/index.json stale: run python3 pipeline/scripts/build-index.py")
if errs:
    print(f"FAIL rule-65: {len(errs)} storage violation(s):"); [print("  ", e) for e in errs[: (None if "--list" in sys.argv else 40)]]; sys.exit(1)
print(f"PASS rule-65: {len(tracked)} tracked files follow docs/conventions/storage.md (no shared files in clips, no duplicates)")
