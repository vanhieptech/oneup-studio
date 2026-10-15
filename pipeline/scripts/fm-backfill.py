#!/usr/bin/env python3
"""Add missing front-matter keys (title, date, type, tags, status, source) to content .md files. Never overwrites an existing key.
Usage: fm-backfill.py [--dry]   (scope = paths.FM_EXEMPT excluded; see docs/conventions/storage.md)"""
import re, sys, json, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); import paths as P
R = P.ROOT
def scope():
    fs = subprocess.run(["git", "ls-files", "*.md"], cwd=R, capture_output=True, text=True).stdout.split()
    fs += subprocess.run(["git", "ls-files", "-o", "--exclude-standard", "*.md"], cwd=R, capture_output=True, text=True).stdout.split()
    return sorted({f for f in fs if not f.startswith(P.FM_EXEMPT) and "node_modules" not in f})
def split(s):
    if s.startswith("---\n") and "\n---" in s[4:]:
        head, body = s[4:].split("\n---", 1); return head.splitlines(), body.lstrip("\n")
    return None, s
def keys(lines): return {l.split(":", 1)[0].strip(): l.split(":", 1)[1].strip() for l in lines if ":" in l and not l.startswith((" ", "-"))}
def q(v): return json.dumps(v, ensure_ascii=False)
def derive(f, k, body):
    top = f.split("/")[0]; name = Path(f).name
    h = re.search(r"^# (.+)$", body, re.M)
    d = subprocess.run(["git", "log", "--diff-filter=A", "--follow", "--format=%cs", "--", f], cwd=R, capture_output=True, text=True).stdout.split()
    typ = ("readme" if name.lower() == "readme.md" else "script" if "script" in name else "research" if top == "research" or "/research/" in f
           else "plan" if "/plans/" in f else "log" if top == "logs" else "brand" if top == "brand" else "doc")
    return {"title": q(h.group(1).strip() if h else Path(f).stem), "date": k.get("updated") or k.get("date") or (d[-1] if d else "2026-10-15"),
            "type": typ, "tags": f"[{top}]", "status": "ready" if typ in ("readme", "brand", "log", "doc") else "draft",
            "source": q(k["collector"] if "collector" in k else "oneup-studio (soạn trong repo)")}
def missing(f):
    lines, body = split((R / f).read_text(errors="ignore")); k = keys(lines or [])
    return [x for x in P.FM_REQUIRED if x not in k], lines, body, k
if __name__ == "__main__":
    n = 0
    for f in scope():
        miss, lines, body, k = missing(f)
        if not miss: continue
        dv = derive(f, k, body); add = [f"{x}: {dv[x]}" for x in miss]; n += 1
        if "--dry" in sys.argv: print(f, miss); continue
        (R / f).write_text("---\n" + "\n".join(add + (lines or [])) + "\n---\n" + ("\n" if lines is None else "") + body)
    print(f"{n} file(s) {'need' if '--dry' in sys.argv else 'got'} front-matter keys")
