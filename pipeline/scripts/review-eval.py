#!/usr/bin/env python3
"""Measure the independent script reviewer against Hiệp's real verdicts (research/review-golden/).

  review-eval.py [--model sonnet] [--limit N] [--only id,id] [--dry-run] [--out research/review-golden/eval-<date>.json]

For each golden sample that has words (rejected: the "Lời bản bị bác" section of rejected/<id>.md; approved: the
`text` lines of content/archive/<clip>/final/spec.json), build a neutral draft in a temp folder, build a
leave-one-out copy of the golden set without that sample (so the reviewer cannot look up the answer), and run
`claude -p` with docs/prompts/reviewer-script.md (read-only tools, cwd = repo). Parse the last `VERDICT:` line.

Metrics: rejected caught = reviewer did not say ĐẠT (target ≥ 90%); approved passed = ĐẠT or ĐẠT VỀ ĐIỂM.
Writes per-sample results + metrics to --out and prints a table. Never edits the golden set.
"""
import datetime as dt, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

GOLDEN = P.ROOT / "research/review-golden"
PROMPT_MD = P.ROOT / "docs/prompts/reviewer-script.md"
CLAUDE = shutil.which("claude") or str(Path.home() / ".local/bin/claude")

def load_prompt():
    m = re.search(r"<<<PROMPT\n(.*?)\nPROMPT>>>", PROMPT_MD.read_text(encoding="utf-8"), re.S)
    if not m: raise SystemExit(f"no prompt block in {PROMPT_MD}")
    return m.group(1)

def samples():
    d = json.loads((GOLDEN / "index.json").read_text(encoding="utf-8"))
    return d["samples"] if isinstance(d, dict) else d

def rejected_words(s):
    f = GOLDEN / (s.get("excerpt_file") or f"rejected/{s['id']}.md")
    if not f.exists(): return None
    t = f.read_text(encoding="utf-8")
    m = re.search(r"^## Lời bản bị bác[^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    if not m: return None
    body = "\n".join(l for l in m.group(1).splitlines() if not l.startswith("Nguồn:")).strip()
    return body if re.search(r"^\s*\d+\.\s*\*\*\[", body, re.M) else None

def approved_words(s):
    clipdir = P.ROOT / Path(s["source"]).parent.parent  # content/archive/<clip>/final/script-final.md → content/archive/<clip>
    spec = clipdir / "final/spec.json"
    if not spec.exists(): return None
    sp = json.loads(spec.read_text(encoding="utf-8")); out, n = [], 0
    for p in sp.get("parts", []):
        for sc in p.get("scenes", []) + p.get("sections", []):
            words = " ".join((l.get("text") or "").strip() for l in sc.get("lines", []) if l.get("text"))
            if words: n += 1; out.append(f"{n}. **[{sc.get('id', f'b{n:02d}')}]** {words}")
    return "\n".join(out) or None

def words_for(s):
    return rejected_words(s) if s["verdict"] == "rejected" else approved_words(s)

def leave_one_out(tmp, sid):
    g = tmp / "golden"; (g / "rejected").mkdir(parents=True)
    d = json.loads((GOLDEN / "index.json").read_text(encoding="utf-8"))
    keep = [x for x in (d["samples"] if isinstance(d, dict) else d) if x["id"] != sid]
    for x in keep:
        if x.get("excerpt_file") and (GOLDEN / x["excerpt_file"]).exists():
            shutil.copy(GOLDEN / x["excerpt_file"], g / x["excerpt_file"])
    (g / "index.json").write_text(json.dumps({"samples": keep}, ensure_ascii=False, indent=1), encoding="utf-8")
    return g

def parse_verdict(text):
    hits = re.findall(r"VERDICT:\s*(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|ĐẠT)", text or "")
    return hits[-1] if hits else None

def run_one(s, model, prompt_tpl):
    words = words_for(s)
    if not words: return {"id": s["id"], "verdict_hiep": s["verdict"], "skipped": "no words"}
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td); draft = tmp / "draft.md"
        draft.write_text("# Nháp cần review\n\n" + words + "\n", encoding="utf-8")
        g = leave_one_out(tmp, s["id"])
        prompt = (prompt_tpl.replace("{DRAFT}", str(draft)).replace("{CLIP_DIR}", str(tmp / "noclip")).replace("{GOLDEN}", str(g))
                  + f"\n\n(Chế độ đo: không mở thư mục research/review-golden/ gốc và không mở content/archive/{s.get('clip', '')}/; chỉ dùng {g}.)")
        args = [CLAUDE, "-p", prompt, "--model", model, "--output-format", "json", "--allowedTools", "Read", "Grep", "Glob",
                "--add-dir", str(tmp)]
        r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=str(P.ROOT))
    try: out = json.loads(r.stdout); text = out.get("result", "")
    except json.JSONDecodeError: out, text = {}, r.stdout
    v = parse_verdict(text)
    return {"id": s["id"], "verdict_hiep": s["verdict"], "verdict_reviewer": v, "cost_usd": out.get("total_cost_usd"),
            "ok": (v != "ĐẠT") if s["verdict"] == "rejected" else (v in ("ĐẠT", "ĐẠT VỀ ĐIỂM")),
            "tail": (text or r.stderr)[-400:]}

def metrics(rows):
    rej = [r for r in rows if r["verdict_hiep"] == "rejected" and not r.get("skipped") and r.get("verdict_reviewer")]
    app = [r for r in rows if r["verdict_hiep"] == "approved" and not r.get("skipped") and r.get("verdict_reviewer")]
    pct = lambda xs: round(100 * sum(1 for x in xs if x["ok"]) / len(xs), 1) if xs else None
    return {"rejected_caught_pct": pct(rej), "rejected_n": len(rej), "approved_passed_pct": pct(app), "approved_n": len(app),
            "no_verdict": sum(1 for r in rows if not r.get("skipped") and not r.get("verdict_reviewer")),
            "skipped": sum(1 for r in rows if r.get("skipped")), "target_rejected_caught_pct": 90,
            "cost_usd": round(sum(r.get("cost_usd") or 0 for r in rows), 4)}

def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    model = opt("--model", "sonnet"); ss = samples()
    if opt("--only"): ss = [s for s in ss if s["id"] in opt("--only").split(",")]
    if opt("--limit"): ss = ss[: int(opt("--limit"))]
    if "--dry-run" in a:
        for s in ss:
            w = words_for(s); print(f"{s['id']:14} {s['verdict']:9} {'words ' + str(len(w.splitlines())) + ' beats' if w else 'SKIP (no words)'}")
        print(f"{sum(1 for s in ss if words_for(s))} with words / {len(ss)}"); return 0
    tpl = load_prompt(); rows = []
    for s in ss:
        r = run_one(s, model, tpl); rows.append(r)
        print(f"{r['id']:14} Hiệp={r['verdict_hiep']:9} reviewer={r.get('verdict_reviewer') or r.get('skipped')}  {'✔' if r.get('ok') else ('–' if r.get('skipped') else '✖')}", flush=True)
    m = metrics(rows)
    out = Path(opt("--out", str(GOLDEN / f"eval-{dt.date.today().isoformat()}.json")))
    out.write_text(json.dumps({"date": dt.date.today().isoformat(), "model": model, "prompt": str(PROMPT_MD.relative_to(P.ROOT)),
                               "metrics": m, "rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(m, ensure_ascii=False)); print(f"→ {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
