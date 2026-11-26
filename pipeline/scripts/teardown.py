#!/usr/bin/env python3
"""Video teardown with Gemini CLI: watch + listen to a clip, extract hook / pacing / spine / audio / ending as JSON.

  teardown.py VIDEO.mp4 [--id ID] [--model gemini-2.5-pro] [--out-dir research/trends/<date>/teardowns]
               [--clip-json row.json] [--timing final/timing.json]

- Prompt: docs/prompts/gemini-teardown.md (between <<<PROMPT and PROMPT>>>). Output: <out-dir>/<id>.json + <id>.md
  (sections 2, 3, 5, 6, 7 of templates/clip-teardown.md; the rest is filled from Apify / by Claude).
- Gemini CLI auth: the CLI must be signed in once (`gemini` interactively → "Login with Google") or GEMINI_API_KEY set
  outside the repo. Without it this exits 3 with the CLI's message.
- --timing: our own clip's timing.json → report how far Gemini's cut times are from the real scene starts (accuracy check).
- Competitor videos: download only with Hiệp's OK, analyse, then delete (the script never keeps or reuses the video).
"""
import datetime as dt, json, os, re, subprocess, sys

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

PROMPT_MD = P.ROOT / "docs/prompts/gemini-teardown.md"

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

def run_gemini(video, model):
    if not P.GEMINI_BIN: raise SystemExit("gemini CLI not found (GEMINI_BIN)")
    prompt = load_prompt() + f"\n\n@{os.path.abspath(video)}"
    args = [P.GEMINI_BIN, "-p", prompt, "-o", "json", "--approval-mode", "plan", "--include-directories", os.path.dirname(os.path.abspath(video))]
    if model: args += ["-m", model]
    r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=os.path.dirname(os.path.abspath(video)))
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
    if not a or a[0].startswith("-"): print(__doc__); return 2
    video = a[0]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    date = dt.date.today().isoformat()
    cid = opt("--id", os.path.splitext(os.path.basename(video))[0])
    outd = opt("--out-dir", str(P.ROOT / f"research/trends/{date}/teardowns"))
    model = opt("--model")
    out = run_gemini(video, model)
    data = extract_json(out.get("response", ""))
    cli = subprocess.run([P.GEMINI_BIN, "--version"], capture_output=True, text=True).stdout.strip()
    used = model or next(iter((out.get("stats", {}).get("models") or {}).keys()), "default")
    meta = {"date": date, "video": os.path.basename(video), "cli": cli, "model": used}
    if opt("--timing"): meta["accuracy"] = cut_accuracy(data, opt("--timing"))
    if opt("--clip-json"): data["apify"] = json.load(open(opt("--clip-json"), encoding="utf-8"))
    data["_meta"] = meta
    os.makedirs(outd, exist_ok=True)
    open(os.path.join(outd, f"{cid}.json"), "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    open(os.path.join(outd, f"{cid}.md"), "w", encoding="utf-8").write(render_md(cid, data, meta))
    print(f"teardown → {outd}/{cid}.{{json,md}} · model {used}" + (f" · accuracy {meta['accuracy']}" if meta.get("accuracy") else ""))
    return 0

if __name__ == "__main__":
    sys.exit(main())
