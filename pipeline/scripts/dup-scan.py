#!/usr/bin/env python3
"""Reuse-first duplicate scan (content-bot prompt step 4-5): filenames, titles, hooks, hashtag sets, topics (HowToLiveBetter items).
Reports only; never deletes. Usage: dup-scan.py [out.md]"""
import re, sys, json, subprocess, difflib, unicodedata
from pathlib import Path
from collections import defaultdict
R = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(R / "pipeline")); import paths as P
fs = [f for f in subprocess.run(["git", "ls-files", "-z"], cwd=R, capture_output=True, text=True).stdout.split("\0") if f and not f.startswith(P.FM_EXEMPT) and "node_modules" not in f]
md = [f for f in fs if f.endswith(".md")]
def norm(s): s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d"); return re.sub(r"[^a-z0-9 ]+", " ", s).split()
out = ["---", 'title: "Dup scan"', f"date: 2026-10-15", "type: log", "tags: [duplicates, reuse-first]", "status: ready", 'source: "pipeline/scripts/dup-scan.py"', "---", "# Dup scan (chỉ báo, không xoá)", ""]
# 1 filenames
byname = defaultdict(list)
for f in fs:
    n = Path(f).name
    if n.lower() in ("readme.md", "spec.json", "post.md", "script-final.md", "post-checklist.md", "digest.md", "raw.json", "collect.json", "patterns.md", "approved.json", "cover.png", "timing.json", ".gitkeep") or f.startswith(("video-engine/public/voice/", "media/", "pipeline/tts/filler-bank/", "content/samples/lab/voice-audition/work/")) or "/explainer/" in f or n.endswith((".wav", ".png", ".txt", ".log")): continue
    byname[n].append(f)
out += ["## 1. Tên file trùng (ngoài tên chuẩn theo layout)", "| tên | các file |", "|---|---|"] + [f"| {n} | {'<br>'.join(v)} |" for n, v in sorted(byname.items()) if len(v) > 1] + [""]
# 2 titles
def fm(f):
    s = (R / f).read_text(errors="ignore"); h = s.split("\n---", 1)[0] if s.startswith("---") else ""
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', h, re.M); return m.group(1) if m else ""
tt = defaultdict(list)
for f in md: tt[" ".join(norm(fm(f)))].append(f)
out += ["## 2. Tiêu đề trùng", "| tiêu đề | file |", "|---|---|"] + [f"| {k} | {'<br>'.join(v)} |" for k, v in tt.items() if k and len(v) > 1] + [""]
# 3 hooks: quoted lines next to 'hook' / 'Hook' + spec hook text
hooks = []
for f in md:
    for ln in (R / f).read_text(errors="ignore").splitlines():
        if re.search(r"hook", ln, re.I) or "Script hooks" in ln:
            for q in re.findall(r"[\"“]([^\"”]{12,140})[\"”]", ln): hooks.append((q, f))
for f in fs:
    if f.endswith("spec.json"):
        try:
            h = json.loads((R / f).read_text()).get("hook", {}); t = h.get("text") if isinstance(h, dict) else None
            if t: hooks.append((t, f))
        except Exception: pass
pairs = []
for i in range(len(hooks)):
    for j in range(i + 1, len(hooks)):
        a, b = hooks[i], hooks[j]
        if a[1] == b[1]: continue
        r = difflib.SequenceMatcher(None, " ".join(norm(a[0])), " ".join(norm(b[0]))).ratio()
        if r >= 0.8: pairs.append((r, a, b))
seen = set(); out += ["## 3. Hook giống nhau (≥ 0.8)", "| sim | hook | file A | file B |", "|---|---|---|---|"]
for r, a, b in sorted(pairs, reverse=True):
    k = (" ".join(norm(a[0])), a[1], b[1])
    if k in seen: continue
    seen.add(k); out.append(f"| {r:.2f} | {a[0][:90]} | `{a[1]}` | `{b[1]}` |")
out.append("")
# 4 hashtags
hs = {}
for f in md:
    if "post" in Path(f).name or "script" in Path(f).name:
        t = set(re.findall(r"(?<![\w&])#([A-Za-zÀ-ỹ][\wÀ-ỹ]{2,})", (R / f).read_text(errors="ignore")))
        if t: hs[f] = t
out += ["## 4. Bộ hashtag trùng / gần trùng (Jaccard ≥ 0.6)", "| jaccard | file A | file B | chung |", "|---|---|---|---|"]
ks = sorted(hs)
for i in range(len(ks)):
    for j in range(i + 1, len(ks)):
        a, b = hs[ks[i]], hs[ks[j]]; jac = len(a & b) / len(a | b)
        if jac >= 0.6: out.append(f"| {jac:.2f} | `{ks[i]}` | `{ks[j]}` | {' '.join('#' + x for x in sorted(a & b)[:8])} |")
out.append("")
# 5 topics: HowToLiveBetter item refs used by >1 clip/plan/idea
top = defaultdict(set)
for f in md:
    if not (f.startswith("content/") or f.endswith(("digest.md", "idea-bank.md"))): continue
    for ln in (R / f).read_text(errors="ignore").splitlines():
        if "|" not in ln and "mục" not in ln: continue
        for a, b in re.findall(r"(?<![\d.,])([1-9]|[12]\d|3[0-4])\.([1-9]\d?)(?![\d.,%]|\s?(?:s|giây|h|M|k)\b)", ln): top[f"{a}.{b}"].add(f)
out += ["## 5. Chủ đề (mục HowToLiveBetter) dùng ở nhiều nơi", "| mục | số file | file |", "|---|---|---|"] + [f"| {k} | {len(v)} | {'<br>'.join(sorted(v)[:6])}{' …' if len(v) > 6 else ''} |" for k, v in sorted(top.items(), key=lambda x: -len(x[1])) if len(v) > 2]
o = sys.argv[1] if len(sys.argv) > 1 else None
T = "\n".join(out) + "\n"
(Path(o).write_text(T) if o else print(T))
