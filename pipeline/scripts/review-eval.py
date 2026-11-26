#!/usr/bin/env python3
"""Measure the independent script reviewer against Hiệp's real verdicts (research/review-golden/).

  review-eval.py [--model sonnet] [--limit N] [--only id,id] [--jobs 3] [--dry-run] [--out research/review-golden/eval-<date>.json]

For each golden sample that has words (rejected: the "Lời bản bị bác" section of rejected/<id>.md; approved: the
`text` lines of content/archive/<clip>/final/spec.json), build a neutral draft in a temp folder, build a
leave-one-out copy of the golden set without that sample (so the reviewer cannot look up the answer), and run
`claude -p` with docs/prompts/reviewer-script.md (read-only tools, cwd = repo). The verdict is recomputed by
review_tiers.py from the answer's HARD_FAILS/SCORE block (DL-074 two tiers); the model's own VERDICT line is kept as
`verdict_llm` for comparison. A usage-limit answer is recorded as `error` (not a verdict) and stops new launches.

Metrics: rejected caught = verdict is not ĐẠT/ĐẠT VỀ ĐIỂM (target ≥ 14/15); approved passed = ĐẠT or ĐẠT VỀ ĐIỂM (target all).
Writes per-sample results + metrics to --out and prints a table. Never edits the golden set.
"""
import datetime as dt, json, os, re, shutil, subprocess, sys, tempfile, threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
from review_tiers import parse_block, tier_verdict

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

def strip_markup(text):
    """Same footing for drafts and approved specs: drop voice/emphasis markup so the reviewer judges the words only."""
    t = re.sub(r"\{[^{}:]*:\s*([^{}]*)\}", r"\1", text or "")
    t = re.sub(r"\{[^{}]*\}", "", t)
    labels = []
    t = re.sub(r"\*\*\[[^\]]*\]\*\*", lambda m: labels.append(m.group(0)) or f"\x00{len(labels) - 1}\x00", t)  # keep `**[bNN]**` beat labels
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t).replace(" | ", " ").replace(" / ", " ")
    t = re.sub(r"  +", " ", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: labels[int(m.group(1))], t)

def words_for(s):
    w = rejected_words(s) if s["verdict"] == "rejected" else approved_words(s)
    return strip_markup(w) if w else w

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
    """Two-tier verdict from the block (review_tiers); falls back to the model's last VERDICT line when the block is missing."""
    tv = tier_verdict(parse_block(text))
    if tv: return tv[0]
    hits = re.findall(r"VERDICT:\s*(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|ĐẠT)", text or "")
    return hits[-1] if hits else None

LIMIT_RE = re.compile(r"hit your (?:\d+-hour |weekly )?limit|usage limit|rate limit", re.I)
STOP = threading.Event()

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
    if LIMIT_RE.search(text or r.stderr or "") and "VERDICT" not in (text or ""):
        STOP.set()
        return {"id": s["id"], "verdict_hiep": s["verdict"], "error": "usage limit", "tail": (text or r.stderr)[-200:]}
    b = parse_block(text); v = parse_verdict(text)
    return {"id": s["id"], "verdict_hiep": s["verdict"], "verdict_reviewer": v, "verdict_llm": (b or {}).get("verdict_llm"),
            "score": (b or {}).get("score"), "parts": (b or {}).get("parts"), "hard_fails": (b or {}).get("hard_fails"),
            "soft_warnings": (b or {}).get("soft"), "block": b is not None, "cost_usd": out.get("total_cost_usd"),
            "ok": (v not in ("ĐẠT", "ĐẠT VỀ ĐIỂM")) if s["verdict"] == "rejected" else (v in ("ĐẠT", "ĐẠT VỀ ĐIỂM")),
            "tail": (text or r.stderr)[-600:]}

def metrics(rows):
    rej = [r for r in rows if r["verdict_hiep"] == "rejected" and not r.get("skipped") and r.get("verdict_reviewer")]
    app = [r for r in rows if r["verdict_hiep"] == "approved" and not r.get("skipped") and r.get("verdict_reviewer")]
    caught = sum(1 for x in rej if x["ok"]); passed = sum(1 for x in app if x["ok"])
    pct = lambda xs: round(100 * sum(1 for x in xs if x["ok"]) / len(xs), 1) if xs else None
    return {"rejected_caught": f"{caught}/{len(rej)}", "approved_passed": f"{passed}/{len(app)}",
            "rejected_caught_pct": pct(rej), "rejected_n": len(rej), "approved_passed_pct": pct(app), "approved_n": len(app),
            "no_verdict": sum(1 for r in rows if not r.get("skipped") and not r.get("verdict_reviewer") and not r.get("error")),
            "errors": sum(1 for r in rows if r.get("error")),
            "skipped": sum(1 for r in rows if r.get("skipped")), "target": "rejected ≥ 14/15, approved all",
            "verdict_source": "review_tiers (DL-074)",
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
    tpl = load_prompt(); jobs = int(opt("--jobs", "1"))
    def one(s):
        if STOP.is_set(): return {"id": s["id"], "verdict_hiep": s["verdict"], "error": "not run (usage limit hit earlier)"}
        r = run_one(s, model, tpl)
        print(f"{r['id']:14} Hiệp={r['verdict_hiep']:9} reviewer={r.get('verdict_reviewer') or r.get('skipped') or r.get('error')}"
              f" score={r.get('score')} llm={r.get('verdict_llm')}  {'✔' if r.get('ok') else ('–' if r.get('skipped') or r.get('error') else '✖')}", flush=True)
        return r
    with ThreadPoolExecutor(max_workers=max(1, jobs)) as ex: rows = list(ex.map(one, ss))
    m = metrics(rows)
    out = Path(opt("--out", str(GOLDEN / f"eval-{dt.date.today().isoformat()}.json")))
    out.write_text(json.dumps({"date": dt.date.today().isoformat(), "model": model, "prompt": str(PROMPT_MD.relative_to(P.ROOT)),
                               "metrics": m, "rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(m, ensure_ascii=False)); print(f"→ {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
