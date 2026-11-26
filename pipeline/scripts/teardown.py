#!/usr/bin/env python3
"""Video teardown with Gemini CLI: watch + listen to a clip, extract hook / pacing / spine / audio / ending as JSON.

  teardown.py VIDEO.mp4 | --url <tiktok/youtube link> [--engine auto|agy|gemini] [--id ID] [--model gemini-2.5-pro] [--out-dir research/trends/<date>/teardowns]
               [--clip-json row.json] [--timing final/timing.json] [--queue-id trends-YYYY-MM-DD-NN] [--no-arc]
  teardown.py --rerender research/trends/<date>/teardowns/<id>.json     # re-render the 6-block .md + ARC/idea-bank from a saved JSON (no model call)

- Prompt: docs/prompts/gemini-teardown.md (between <<<PROMPT and PROMPT>>>). Output: <out-dir>/<id>.json + <id>.md
  (sections 2, 3, 5, 6, 7 of templates/clip-teardown.md; the rest is filled from Apify / by Claude).
- Engine: `agy` (Antigravity CLI, Google sign-in, default when installed; models e.g. gemini-4-hydrogen-high,
  gemini-4-carbon-high — `agy models`) or Gemini CLI. Gemini CLI auth: `export GEMINI_API_KEY=…` in ~/oneup-tools/env.sh (outside git; key from Google AI Studio). "Sign in with
  Google" is refused for individual accounts since 2026-11 ("no longer supported for Gemini Code Assist for individuals").
  Without a key this exits 3 with the CLI's message.
- --timing: our own clip's timing.json → report how far Gemini's cut times are from the real scene starts (accuracy check).
- --url: yt-dlp downloads to media/tmp/teardown/ (gitignored), the clip is analysed, and the file is deleted in a finally
  block even when Gemini fails; the link is stored in the JSON. Hiệp OK'd analysing competitor clips (26/11); never reuse them.
- Output = Viral DNA card, 6 blocks (templates/clip-teardown.md): hook · beat map · winning points · algorithmic triggers ·
  reusable arc ARC-NNN · dual-channel angle. Khối 0 metadata comes from --clip-json, else the clip's row in
  research/trends/*/apify/clips.json (matched by URL / TikTok id).
- Each run upserts Khối 5 into the ARC library (pipeline/arc_library.py: similar ≥ 0.6 → add evidence, else new ARC-NNN),
  pushes Khối 6 to content/idea-bank.md, rebuilds the ARC table in research/trends/patterns.md, and with --queue-id marks the
  teardown-queue row done (trend-streams.py). Old JSON (spine/pacing/formula) is mapped to the new blocks.
"""
import datetime as dt, json, os, re, subprocess, sys
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
import arc_library as ARC

PROMPT_MD = P.ROOT / "docs/prompts/gemini-teardown.md"

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
    guesses = [mmss(x.get("t")) for x in ((data.get("winning_points") or {}).get("interrupts") or data.get("pacing", {}).get("interrupts", []))] + [mmss(x.get("from")) for x in (data.get("beats") or data.get("spine") or [])]
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

def normalize(data):
    """Map an old teardown JSON (spine / pacing / formula, before the 7-block prompt) onto the 7 blocks. Idempotent."""
    d = dict(data)
    if not d.get("beats") and d.get("spine"):
        d["beats"] = [{"from": x.get("from"), "to": x.get("to"), "seconds": (lambda a, b: round(b - a, 1) if a is not None and b is not None else None)(mmss(x.get("from")), mmss(x.get("to"))),
                       "role": x.get("role"), "retention_function": None, "summary": x.get("summary"), "transition": x.get("transition")} for x in d["spine"]]
    if d.get("beats") and d["beats"] and d["beats"][0].get("role") != "hook" and mmss(d["beats"][0].get("from")) == 0:
        pass  # Gemini may call the opening «dẫn dắt»; keep its word
    wp = d.setdefault("winning_points", {})
    if not wp.get("interrupts") and d.get("pacing", {}).get("interrupts"): wp["interrupts"] = d["pacing"]["interrupts"]
    if wp.get("interrupts_per_10s") is None and d.get("pacing", {}).get("avg_seconds_per_change"):
        wp["interrupts_per_10s"] = round(10 / float(d["pacing"]["avg_seconds_per_change"]), 1)
    d.setdefault("algorithmic_triggers", {})
    arc = d.setdefault("arc", {})
    if not arc.get("skeleton") and d.get("formula"): arc["skeleton"] = d["formula"]
    if not arc.get("hook_mechanism"): arc["hook_mechanism"] = (d.get("hook") or {}).get("mechanism") or ""
    arc["beats"] = [{"role": b.get("role"), "function": b.get("retention_function"), "seconds": b.get("seconds"), "transition": b.get("transition")}
                    for b in d.get("beats", [])]
    d.setdefault("angles", {})
    ct = d.setdefault("craft_transfer", {})
    if isinstance(ct, dict):
        ct.setdefault("metaphor_transfer", "")
        ct.setdefault("sentence_rhythm", "")
        ct.setdefault("pacing_3_5s", "")
        ct.setdefault("audience_pains", [])
    return d

def find_clip(source):
    """Khối 0 metadata: the clip's row in research/trends/*/{apify/clips.json, radar-raw.json} (by TikTok/YT id or URL), newest first."""
    vid = re.search(r"/video/(\d+)", source or "") or re.search(r"/shorts/([A-Za-z0-9_-]{8,})", source or "") or re.search(r"(\d{15,})", source or "")
    for pat in ("research/trends/20??-??-??/apify/clips.json", "research/trends/20??-??-??/radar-raw.json"):
        for f in sorted(P.ROOT.glob(pat), reverse=True):
            try: doc = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError: continue
            for c in (doc if isinstance(doc, list) else doc.get("clips", [])):
                if (vid and vid.group(1) in (c.get("url") or "")) or (source and source == c.get("url")): return c
    return None

PAIN_BANK = P.ROOT / "resources/vn-spoken/audience-pain-bank.md"

def push_audience_pains(cid, data, date, bank_path=None):
    """Append deduplicated audience questions/pains from Block 7 / top_comments into resources/vn-spoken/audience-pain-bank.md."""
    p = Path(bank_path or PAIN_BANK)
    ct = data.get("craft_transfer") if isinstance(data.get("craft_transfer"), dict) else {}
    ap = data.get("apify") if isinstance(data.get("apify"), dict) else {}
    raw_pains = []
    for x in (ct.get("audience_pains") or []):
        if isinstance(x, str) and x.strip():
            raw_pains.append(x.strip())
    for cm in (ap.get("top_comments") or [])[:5]:
        t = cm.get("text", "").strip() if isinstance(cm, dict) else str(cm).strip()
        if len(t) >= 8:
            raw_pains.append(t)
    if not raw_pains:
        return 0
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            f"---\ntitle: \"Kho Nỗi Đau & Câu Hỏi Khán Giả Thật (Audience Pain Bank)\"\ndate: {date}\n"
            f"id: resources.vn-spoken.audience-pain-bank\ntype: resource\nstatus: ready\nupdated: {date}\n"
            f"tags: [audience, pain-bank, comments, vn-spoken, teardown]\n"
            f"source: \"pipeline/scripts/teardown.py\"\n---\n# Kho Nỗi Đau & Câu Hỏi Khán Giả Thật\n\n"
            f"## Bảng nỗi đau & câu hỏi từ comment\n\n"
            f"| ngày | nguồn teardown / video | chủ đề | câu hỏi / nỗi đau khán giả (ẩn danh) | ghi chú dùng cho hook |\n"
            f"|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    existing = p.read_text(encoding="utf-8")
    existing_low = existing.lower()
    topic = ", ".join((ap.get("channel_niche") or [])[:2]) or (data.get("arc") or {}).get("name") or "chung"
    topic = topic.replace("|", "/").strip()
    added_lines = []
    for pain in raw_pains:
        clean = re.sub(r"\s+", " ", pain).replace("|", "/").strip(" «»\"")
        if len(clean) < 8 or clean.lower() in existing_low:
            continue
        existing_low += "\n" + clean.lower()
        added_lines.append(f"| {date} | {cid} | {topic} | «{clean[:220]}» | Tự động trích từ Khối 7 / comment |")
    if added_lines:
        p.write_text(existing.rstrip("\n") + "\n" + "\n".join(added_lines) + "\n", encoding="utf-8")
    return len(added_lines)

def _v(x, k="text"):
    return (x or {}).get(k) if isinstance(x, dict) else x

def render_md(cid, data, meta):
    d = normalize(data); h, L = d.get("hook", {}), []
    c = d.get("apify") or {}
    fans = (c.get("author") or {}).get("fans"); views = c.get("play_count")
    ratio = round(views / fans, 2) if fans and views else None
    L += ["---", f'title: "Teardown {cid}"', f"date: {meta['date']}", f"id: teardown.{cid}", "type: teardown", "status: draft",
          f"updated: {meta['date']}", "tags: [teardown, trend, viral-dna]", f'source: "{meta.get("source") or meta["video"]} · {meta["cli"]} · model {meta["model"]}"', "---",
          f"# Viral DNA Card `{cid}`", "", "Theo `templates/clip-teardown.md` (6 khối). Khối 1–6 do model xem + nghe video điền (quan sát / suy đoán); Khối 0 từ Apify. Không chép câu, hình, âm thanh vào clip của mình.", "",
          "## Khối 0 — Số liệu", "| link | creator | follower | view | view/follower | comment | share | độ dài | ngày đăng |", "|---|---|---|---|---|---|---|---|---|",
          f"| {meta.get('source') or ''} | {(c.get('author') or {}).get('name', '')} | {fans or ''} | {views or ''} | {str(ratio) + 'x' if ratio else ''} | {c.get('comment_count', '')} | {c.get('share_count', '')} | {c.get('duration_s', '')} | {(c.get('create_time') or '')[:10]} |", "",
          "## Khối 1 — Hook Mechanics (0–3 giây)", f"- Câu mở đầu: {h.get('spoken')} (nguyên văn: {h.get('verbatim')})", f"- Chữ trên màn hình: {h.get('on_screen_text')}",
          f"- Hình / hành động: {h.get('visual_action')}", f"- Cơ chế tâm lý: **{h.get('mechanism')}** — {h.get('mechanism_note')}", f"- Lời hứa ngầm: {h.get('implied_promise')}", "",
          "## Khối 2 — Story Arc & Beat Map", "| mốc | giây | vai trò | chức năng giữ chân | tóm ý | chuyển ý sang beat sau |", "|---|---|---|---|---|---|"]
    L += [f"| {b.get('from')}–{b.get('to')} | {b.get('seconds')} | {b.get('role')} | {b.get('retention_function') or '—'} | {b.get('summary')} | {b.get('transition')} |" for b in d.get("beats", [])]
    wp = d.get("winning_points", {})
    L += [f"- Trả lời lời hứa của hook ở: {d.get('promise_answered_at')}", "", "## Khối 3 — Winning Points",
          f"- Ẩn dụ / ví dụ đắt nhất: {_v(wp.get('best_metaphor')) or '—'} ({_v(wp.get('best_metaphor'), 't') or '—'})",
          f"- Câu đáng lưu / share: {_v(wp.get('quotable_line')) or '—'} ({_v(wp.get('quotable_line'), 't') or '—'})",
          f"- Ngắt nhịp: {wp.get('interrupts_per_10s') if wp.get('interrupts_per_10s') is not None else '—'} lần / 10 giây"]
    L += [f"  - {x.get('t')} {x.get('what')} ({x.get('kind')})" for x in wp.get("interrupts", [])]
    a = d.get("audio", {}); e = d.get("ending", {})
    L += [f"- Âm thanh: nhịp {a.get('speech_pace')} · tone {a.get('tone')} · nhạc {a.get('music')} (luật 21: clip mình không có nhạc)",
          f"- Kết: {e.get('type')} · CTA: {e.get('cta')}", "", "## Khối 4 — Algorithmic Triggers"]
    at = d.get("algorithmic_triggers", {})
    L += [f"- Bình luận: {x.get('what')} ({x.get('why')}, {x.get('kind')})" for x in at.get("comment", [])] or ["- Bình luận: — (bổ sung từ Apify comments)"]
    L += [f"- Lưu / chia sẻ: {x.get('what')} ({x.get('why')}, {x.get('kind')})" for x in at.get("save_share", [])] or ["- Lưu / chia sẻ: —"]
    if at.get("_source"): L.append(f"- Nguồn khối: {at['_source']}")
    arc = d.get("arc", {})
    L += ["", f"## Khối 5 — Reusable Story Arc ({meta.get('arc') or 'ARC chưa gộp'})", f"- Tên: {arc.get('name') or '—'} · cơ chế hook: {arc.get('hook_mechanism') or '—'}"]
    L += [f"{k}. {x}" for k, x in enumerate(arc.get("skeleton", []), 1)]
    if arc.get("_source"): L.append(f"- Nguồn khối: {arc['_source']}")
    if meta.get("arc"): L += [f"- {'Mạch mới' if meta.get('arc_new') else 'Trùng mạch đã có, cộng bằng chứng'}: xem `research/trends/patterns.md` › Story arcs."]
    ang = d.get("angles", {})
    L += ["", "## Khối 6 — Dual-Channel Angle (suy đoán, Hiệp chọn ở Gate 0)"]
    for ch, lab in (("hi_oneup", "@hi.oneup (comic + motion, 120–180s)"), ("vanhiep_tech", "@vanhiep.tech (talking-head + overlay, 45–90s)")):
        x = ang.get(ch) or {}
        L.append(f"- **{lab}:** {x.get('idea') or '— (chưa có: teardown cũ, Claude bổ sung hoặc chạy lại)'}" + (f" · hook: «{x.get('hook')}» · ~{x.get('length_s')}s" if x.get("idea") else ""))
    if ang.get("_source"): L.append(f"- Nguồn khối: {ang['_source']}")
    ct = d.get("craft_transfer") if isinstance(d.get("craft_transfer"), dict) else {}
    pains = ct.get("audience_pains") or []
    L += ["", "## Khối 7 — Craft & Voice Transfer (Kỹ thuật ngôn ngữ & Nhịp cắt học được)",
          f"- Ẩn dụ chuyển hóa khái niệm khó → đời thường: {ct.get('metaphor_transfer') or _v(wp.get('best_metaphor')) or '—'}",
          f"- Cách ngắt câu & nhịp nói: {ct.get('sentence_rhythm') or a.get('speech_pace') or '—'}",
          f"- Kỹ thuật giữ nhịp mỗi 3–5s: {ct.get('pacing_3_5s') or (str(wp.get('interrupts_per_10s')) + ' ngắt nhịp/10s' if wp.get('interrupts_per_10s') is not None else '—')}",
          f"- Câu hỏi / nỗi đau khán giả (→ `resources/vn-spoken/audience-pain-bank.md`): {('; '.join(pains[:5]) if pains else '—')}"]
    L += ["", "## Vì sao nó chạy (suy đoán)"] + [f"- {x.get('claim')} ({x.get('evidence')})" for x in d.get("why_it_works", [])]
    if meta.get("accuracy"): L += ["", "## Kiểm độ chính xác mốc cắt (so với timing.json)", f"- {meta['accuracy']}"]
    return "\n".join(L) + "\n"

def finish(cid, data, meta, outd, opt_queue=None, arc=True):
    """Write JSON + 7-block md, upsert ARC, push angles to idea-bank, push audience pains, rebuild generated tables, close the queue row."""
    data = normalize(data)
    if data.get("apify") is None: data["apify"] = find_clip(meta.get("source"))
    md_path = Path(outd) / f"{cid}.md"
    rel = str(md_path.resolve().relative_to(P.ROOT)) if P.ROOT in md_path.resolve().parents else str(md_path)
    if arc:
        c = data.get("apify") or {}; fans = (c.get("author") or {}).get("fans"); views = c.get("play_count")
        meta["arc"], meta["arc_new"] = ARC.upsert_arc(data["arc"], {"source": meta.get("source"), "creator": (c.get("author") or {}).get("name"),
                                                                     "ratio": round(views / fans, 2) if fans and views else None, "views": views,
                                                                     "followers": fans, "date": meta["date"], "teardown": rel})
        if meta["arc"]:
            ARC.push_ideas(meta["arc"], data.get("angles"), rel, meta["date"])
            ARC.render_patterns(); ARC.render_ideas()
        push_audience_pains(cid, data, meta["date"])
    data["_meta"] = meta
    os.makedirs(outd, exist_ok=True)
    open(os.path.join(outd, f"{cid}.json"), "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    md_path.write_text(render_md(cid, data, meta), encoding="utf-8")
    if opt_queue:
        import importlib.util
        sp = importlib.util.spec_from_file_location("trend_streams", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trend-streams.py"))
        ts = importlib.util.module_from_spec(sp); sp.loader.exec_module(ts); ts.mark_done(opt_queue, rel)
    return rel

def rerender(json_path):
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    meta = dict(data.get("_meta") or {}); meta.setdefault("date", dt.date.today().isoformat())
    meta.setdefault("video", ""); meta.setdefault("cli", "?"); meta.setdefault("model", "?")
    meta.pop("blueprint", None)
    cid = Path(json_path).stem
    rel = finish(cid, data, meta, str(Path(json_path).parent))
    print(f"rerender → {rel} · {meta.get('arc')}{' (mới)' if meta.get('arc_new') else ''}")
    return 0

def main():
    a = sys.argv[1:]
    def opt(n, d=None): return a[a.index(n) + 1] if n in a else d
    if opt("--rerender"): return rerender(opt("--rerender"))
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
    rel = finish(cid, data, meta, outd, opt("--queue-id"), arc=not ({"--no-arc", "--no-blueprint"} & set(sys.argv)) and not opt("--timing"))  # --timing = self-test on our own clip, not evidence
    print(f"teardown → {rel} · model {used} · {meta.get('arc') or 'no arc'}" + (f" · accuracy {meta['accuracy']}" if meta.get("accuracy") else ""))
    return 0

if __name__ == "__main__":
    sys.exit(main())
