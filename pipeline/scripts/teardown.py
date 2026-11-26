#!/usr/bin/env python3
"""Video teardown with Gemini CLI: watch + listen to a clip, extract hook / pacing / spine / audio / ending as JSON.

  teardown.py VIDEO.mp4 | --url <tiktok/youtube link> [--engine auto|agy|gemini] [--id ID] [--model gemini-2.5-pro] [--out-dir research/trends/<date>/teardowns]
               [--clip-json row.json] [--timing final/timing.json]

- Prompt: docs/prompts/gemini-teardown.md (between <<<PROMPT and PROMPT>>>). Output: <out-dir>/<id>.json + <id>.md
  (sections 2, 3, 5, 6, 7 of templates/clip-teardown.md; the rest is filled from Apify / by Claude).
- Engine: `agy` (Antigravity CLI, Google sign-in, default when installed; models e.g. gemini-4-hydrogen-high,
  gemini-4-carbon-high — `agy models`) or Gemini CLI. Gemini CLI auth: `export GEMINI_API_KEY=…` in ~/oneup-tools/env.sh (outside git; key from Google AI Studio). "Sign in with
  Google" is refused for individual accounts since 2026-11 ("no longer supported for Gemini Code Assist for individuals").
  Without a key this exits 3 with the CLI's message.
- --timing: our own clip's timing.json → report how far Gemini's cut times are from the real scene starts (accuracy check).
- --url: yt-dlp downloads to media/tmp/teardown/ (gitignored), the clip is analysed, and the file is deleted in a finally
  block even when Gemini fails; the link is stored in the JSON. Hiệp OK'd analysing competitor clips (26/11); never reuse them.
- Each run merges `formula` into research/blueprints/index.json (similar ≥ 0.6 → seen+1, else a new script mode).
"""
import datetime as dt, json, os, re, subprocess, sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

PROMPT_MD = P.ROOT / "docs/prompts/gemini-teardown.md"

BLUEPRINTS = P.ROOT / "research/blueprints/index.json"
TMP_DIR = P.ROOT / "media/tmp/teardown"

def download(url):
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    out = TMP_DIR / "%(id)s.%(ext)s"  # -S res:480: ≤480p is enough for analysis, smaller and faster
    import shutil
    ytdlp = [shutil.which("yt-dlp")] if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]  # Homebrew binary first (python3.14 has no yt_dlp module)
    r = subprocess.run([*ytdlp, "-S", "res:480,ext:mp4", "-o", str(out), "--no-playlist", "--print", "after_move:filepath", url],
                       capture_output=True, text=True, timeout=300)
    path = (r.stdout.strip().splitlines() or [""])[-1]
    if r.returncode or not path or not os.path.exists(path):
        raise SystemExit(f"yt-dlp failed for {url}: {r.stderr.strip()[-300:]}")
    return path

def _sim(a, b):
    import difflib
    return difflib.SequenceMatcher(None, " ".join(a).lower(), " ".join(b).lower()).ratio()

def merge_blueprint(formula, source, path=None, threshold=0.6):
    """Add a teardown formula to the script-mode library: similar (≥ threshold) → seen+1 + source, else a new id."""
    path = Path(path or BLUEPRINTS)
    lib = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"modes": []}
    if not formula: return None
    best = max(lib["modes"], key=lambda m: _sim(m["formula"], formula), default=None)
    if best and _sim(best["formula"], formula) >= threshold:
        best["seen"] += 1
        if source not in best["sources"]: best["sources"].append(source)
        mode = best
    else:
        mode = {"id": f"SM{len(lib['modes']) + 1:02d}", "formula": formula, "seen": 1, "uses": 0, "wins": 0, "sources": [source]}
        lib["modes"].append(mode)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(lib, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return mode["id"]

def load_prompt():
    t = PROMPT_MD.read_text(encoding="utf-8")
    m = re.search(r"<<<PROMPT\n(.*?)\nPROMPT>>>", t, re.S)
    if not m: raise SystemExit(f"no <<<PROMPT … PROMPT>>> block in {PROMPT_MD}")
    return m.group(1)

def extract_json(text):
    """Gemini sometimes wraps JSON in ``` fences or adds a sentence; take the outermost {...} block."""
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.M)
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j <= i: raise ValueError("no JSON object in Gemini response")
    return json.loads(t[i:j + 1])

def mmss(v):
    if not v or not isinstance(v, str): return None
    m = re.match(r"^(\d+):(\d{1,2})(?:\.(\d+))?$", v.strip())
    return int(m.group(1)) * 60 + int(m.group(2)) + (float("0." + m.group(3)) if m.group(3) else 0) if m else None

def cut_accuracy(data, timing_path):
    """Distance from each Gemini interrupt/spine boundary to the nearest real scene start in our timing.json."""
    tj = json.load(open(timing_path, encoding="utf-8"))
    starts, off = [], 0.0
    for part in tj.get("parts", []):  # build-final timing.json: parts[].scene_starts are relative to the part; _off/dur place the part
        base = float(part.get("_off", off))
        starts += [round(base + float(x), 2) for x in part.get("scene_starts", [])]
        off = base + float(part.get("dur", 0))
    starts = sorted(set(starts))
    guesses = [mmss(x.get("t")) for x in data.get("pacing", {}).get("interrupts", [])] + [mmss(x.get("from")) for x in data.get("spine", [])]
    guesses = [g for g in guesses if g is not None]
    if not starts or not guesses: return {"n": 0}
    d = [min(abs(g - s) for s in starts) for g in guesses]
    return {"n": len(d), "mean_s": round(sum(d) / len(d), 2), "max_s": round(max(d), 2), "within_1s": sum(1 for x in d if x <= 1.0)}

def run_agy(video, model):
    """Antigravity CLI (`agy -p`, Google sign-in). Returns the same shape as run_gemini: {"response": text, "stats": {...}}."""
    prompt = load_prompt() + f"\n\nVideo cần phân tích: @{os.path.abspath(video)}"
    args = [P.AGY_BIN, "-p", prompt, "--output-format", "json", "--mode", "plan", "--add-dir", os.path.dirname(os.path.abspath(video)),
            "--print-timeout", "900s"]
    if model: args += ["--model", model]
    r = subprocess.run(args, capture_output=True, text=True, timeout=960, cwd=os.path.dirname(os.path.abspath(video)))
    try: out = json.loads(r.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError): out = {"status": "ERROR", "error": (r.stderr or r.stdout).strip()[-500:]}
    if out.get("status") == "ERROR" or out.get("error"):
        print(f"agy error: {out.get('error')}", file=sys.stderr); sys.exit(3)
    return {"response": out.get("response", ""), "stats": {"models": {out.get("model") or model or "agy-default": out.get("usage", {})}},
            "engine": "agy"}

def run_engine(video, model, engine):
    if engine == "agy" or (engine == "auto" and P.AGY_BIN and os.path.exists(P.AGY_BIN)):
        return run_agy(video, model)
    return run_gemini(video, model)

def run_gemini(video, model):
    if not P.GEMINI_BIN: raise SystemExit("gemini CLI not found (GEMINI_BIN)")
    prompt = load_prompt() + f"\n\n@{os.path.abspath(video)}"
    args = [P.GEMINI_BIN, "-p", prompt, "-o", "json", "--approval-mode", "plan", "--include-directories", os.path.dirname(os.path.abspath(video))]
    if model: args += ["-m", model]
    env = dict(os.environ)
    key = P.tools_env("GEMINI_API_KEY")  # Google sign-in no longer works for individual accounts (26/11): API key from ~/oneup-tools/env.sh
    if key: env["GEMINI_API_KEY"] = key
    r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=os.path.dirname(os.path.abspath(video)), env=env)
    try: out = json.loads(r.stdout)
    except json.JSONDecodeError: out = {"response": r.stdout, "error": {"message": r.stderr.strip()[:500]} if r.returncode else None}
    if out.get("error"):
        print(f"gemini error: {out['error'].get('message', out['error'])}", file=sys.stderr); sys.exit(3)
    return out

def render_md(cid, data, meta):
    h, L = data.get("hook", {}), []
    L += ["---", f'title: "Teardown {cid}"', f"date: {meta['date']}", f"id: teardown.{cid}", "type: teardown", "status: draft",
          f"updated: {meta['date']}", "tags: [teardown, trend]", f'source: "{meta["video"]} · Gemini CLI {meta["cli"]} · model {meta["model"]}"', "---",
          f"# Teardown `{cid}`", "", "Theo `templates/clip-teardown.md`. Mục 2, 3, 5, 6, 7 do Gemini điền (quan sát/suy đoán ghi trong JSON); mục 0, 1, 4, 8 từ Apify; 9–11 Claude tổng hợp.", "",
          "## 2. Hook 0–3 giây", f"- Lời: {h.get('spoken')} (nguyên văn: {h.get('verbatim')})", f"- Chữ trên màn hình: {h.get('on_screen_text')}",
          f"- Hình / hành động: {h.get('visual_action')}", f"- Cơ chế: {h.get('mechanism')} — {h.get('mechanism_note')}", f"- Lời hứa ngầm: {h.get('implied_promise')}", "",
          "## 3. Xương sống", "| mốc | vai trò | tóm ý | chuyển ý |", "|---|---|---|---|"]
    L += [f"| {x.get('from')}–{x.get('to')} | {x.get('role')} | {x.get('summary')} | {x.get('transition')} |" for x in data.get("spine", [])]
    L += [f"- Trả lời lời hứa ở: {data.get('promise_answered_at')}", "", "## 5. Nhịp & ngắt nhịp",
          f"- Trung bình mỗi lần đổi: {data.get('pacing', {}).get('avg_seconds_per_change')} giây"]
    L += [f"- {x.get('t')} {x.get('what')} ({x.get('kind')})" for x in data.get("pacing", {}).get("interrupts", [])]
    a = data.get("audio", {})
    L += ["", "## 6. Âm thanh & năng lượng", f"- Nhịp nói: {a.get('speech_pace')} · tone: {a.get('tone')} · nhạc: {a.get('music')}"]
    L += [f"- nhấn {x.get('t')}: {x.get('what')}" for x in a.get("emphasis", [])] + [f"- SFX {x.get('t')}: {x.get('what')}" for x in a.get("sfx", [])]
    e = data.get("ending", {})
    L += ["", "## 7. Kết & CTA", f"- Kiểu: {e.get('type')} · CTA: {e.get('cta')}", "", "## 9. Vì sao nó chạy (Gemini, suy đoán)"]
    L += [f"- {x.get('claim')} ({x.get('evidence')})" for x in data.get("why_it_works", [])]
    L += ["", "## 11. Công thức khung"] + [f"{k}. {x}" for k, x in enumerate(data.get("formula", []), 1)]
    if meta.get("accuracy"): L += ["", f"## Kiểm độ chính xác mốc cắt (so với timing.json)", f"- {meta['accuracy']}"]
    return "\n".join(L) + "\n"

def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    url = opt("--url")
    if not url and (not a or a[0].startswith("-")): print(__doc__); return 2
    video = download(url) if url else a[0]
    try:
        return analyse(video, url, opt)
    finally:
        if url and os.path.exists(video): os.remove(video)  # never keep someone else's clip

def analyse(video, url, opt):
    date = dt.date.today().isoformat()
    cid = opt("--id", os.path.splitext(os.path.basename(video))[0])
    source = url or os.path.basename(video)
    outd = opt("--out-dir", str(P.ROOT / f"research/trends/{date}/teardowns"))
    model = opt("--model")
    engine = opt("--engine", "auto")  # auto = agy (Antigravity) when installed, else gemini CLI
    out = run_engine(video, model, engine)
    try:
        data = extract_json(out.get("response", ""))
    except ValueError:
        raw = TMP_DIR / f"{cid}.raw.txt"; TMP_DIR.mkdir(parents=True, exist_ok=True)
        raw.write_text(out.get("response", ""), encoding="utf-8")
        print(f"no JSON in model response; raw saved to {raw}:\n{out.get('response', '')[:800]}", file=sys.stderr); sys.exit(4)
    cli = ("agy " if out.get("engine") == "agy" else "gemini ") + subprocess.run([P.AGY_BIN if out.get("engine") == "agy" else P.GEMINI_BIN, "--version"], capture_output=True, text=True).stdout.strip()[:40]
    used = model or next(iter((out.get("stats", {}).get("models") or {}).keys()), "default")
    meta = {"date": date, "video": os.path.basename(video), "cli": cli, "model": used}
    if opt("--timing"): meta["accuracy"] = cut_accuracy(data, opt("--timing"))
    if opt("--clip-json"): data["apify"] = json.load(open(opt("--clip-json"), encoding="utf-8"))
    meta["source"] = source
    meta["blueprint"] = merge_blueprint(data.get("formula") or [], source) if "--no-blueprint" not in sys.argv else None
    data["_meta"] = meta
    os.makedirs(outd, exist_ok=True)
    open(os.path.join(outd, f"{cid}.json"), "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    open(os.path.join(outd, f"{cid}.md"), "w", encoding="utf-8").write(render_md(cid, data, meta))
    print(f"teardown → {outd}/{cid}.{{json,md}} · model {used}" + (f" · accuracy {meta['accuracy']}" if meta.get("accuracy") else ""))
    return 0

if __name__ == "__main__":
    sys.exit(main())
