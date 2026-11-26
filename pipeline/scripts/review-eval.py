#!/usr/bin/env python3
"""Measure the independent script reviewer against Hiệp's real verdicts (research/review-golden/).

  review-eval.py [--mode pairwise|score] [--anchor auto|a-c05] [--engine agy|claude|cursor] [--model default|sonnet|grok-4.7-medium]
                 [--limit N] [--only id,id] [--jobs 3] [--dry-run]
                 [--out research/review-golden/eval-<date>.json]

Modes:
  pairwise (default): Pairwise A/B with Theme/Format-Matched Anchor Selection — automatically picks the
                      closest approved script from `research/review-golden/approved/` + `index.json` matching
                      the draft's channel (`@hi.oneup` vs `@vanhiep.tech`), format (`story_metaphor` vs
                      `instructional_list`), and theme (leave-one-out when evaluating an approved sample).
                      Also injects Hiệp's historical rejection blind-spots from `resources/feedback.md`.
                      Recomputes verdict via review_tiers.py (H1–H4 hard gate + WIN/TIE/LOSE).
  score:              Legacy absolute-score mode.

Samples with no words (`skipped: no words`) are skipped before launching worker calls.
Metrics: rejected caught = verdict is not ĐẠT/ĐẠT VỀ ĐIỂM (target ≥ 14/15); approved passed = ĐẠT or ĐẠT VỀ ĐIỂM.
Writes per-sample results + metrics to --out and prints a table. Never edits the golden set.
"""
import datetime as dt, json, os, re, shutil, subprocess, sys, tempfile, threading, unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
from review_tiers import parse_block, tier_verdict

GOLDEN = P.ROOT / "research/review-golden"
PROMPT_MD = P.ROOT / "docs/prompts/reviewer-script.md"
FEEDBACK_MD = P.ROOT / "resources/feedback.md"
CLAUDE = shutil.which("claude") or str(Path.home() / ".local/bin/claude")

LIST_FORMAT_RE = re.compile(
    r"(?<!\w)(?:thì cái bản chất|bản chất của cái|và cuối cùng|3 cách|ba cách|bước 1|bước 2)(?!\w)",
    re.I,
)
THEME_KEYWORDS = {
    "habit_procrastination": (
        "thói quen", "trì hoãn", "21 ngày", "mai học", "để mai", "cuối tuần", "cả năm",
        "dọn phòng", "chia nhỏ", "nếu thì", "đang né", "mình né", "khó chịu", "đi bộ", "hít đất", "lally", "steel", "gollwitzer",
    ),
    "memory_study": (
        "nhớ lâu", "quên sạch", "học thuộc", "đọc sách", "đọc lại", "gấp sách", "tự kiểm",
        "tự viết", "tự kể", "trả bài", "ôn thi", "chương sách", "sinh viên", "roediger", "yang", "từ tiếng anh",
        "tài liệu", "thí nghiệm", "nhớ hơn", "học một đêm",
    ),
    "tech_dev": (
        "code", "lập trình", "terminal", "api", "jwt", "token", "server", "bug", "deploy",
        "docker", "git", "capcut", "overlay", "prompt", "llm", "agent", "database",
    ),
}
STOP_WORDS = set(
    "và của là có cho một những các được với không thì mà này đó để khi người bạn mình rồi lại cũng như nào gì vì nên hay hơn vào ra lên về tới tại".split()
)


def _fold(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    return unicodedata.normalize("NFC", "".join(c for c in s if unicodedata.category(c) != "Mn")).replace("đ", "d")


def _content_tokens(text):
    return {w for w in re.findall(r"[a-z0-9]+", _fold(text)) if len(w) > 2 and w not in STOP_WORDS}


def load_prompt():
    m = re.search(r"<<<PROMPT\n(.*?)\nPROMPT>>>", PROMPT_MD.read_text(encoding="utf-8"), re.S)
    if not m:
        raise SystemExit(f"no prompt block in {PROMPT_MD}")
    return m.group(1)


def load_feedback_blindspots(path=FEEDBACK_MD):
    """Extract Hiệp's historical rejection notes from resources/feedback.md for Pairwise TIE-vs-LOSE calibration."""
    p = Path(path)
    if not p.exists():
        return "- (chưa có resources/feedback.md)"
    rows = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        if ln.startswith("|") and not re.match(r"^\|[-\s|:]+\|$", ln):
            c = [x.strip() for x in ln.strip("|").split("|")]
            if len(c) >= 4 and c[0].startswith("«"):
                rows.append(f"- {c[0]} → **{c[1]}** ({c[3]})")
    return "\n".join(rows) if rows else "- (chưa có mục chê nào trong resources/feedback.md)"


def samples():
    d = json.loads((GOLDEN / "index.json").read_text(encoding="utf-8"))
    return d["samples"] if isinstance(d, dict) else d


def rejected_words(s):
    f = GOLDEN / (s.get("excerpt_file") or f"rejected/{s['id']}.md")
    if not f.exists():
        return None
    t = f.read_text(encoding="utf-8")
    m = re.search(r"^## Lời bản bị bác[^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    if not m:
        return None
    body = "\n".join(l for l in m.group(1).splitlines() if not l.startswith("Nguồn:")).strip()
    return body if re.search(r"^\s*\d+\.\s*\*\*\[", body, re.M) else None


def approved_words(s):
    # Support explicit research/review-golden/approved/<id>.md if present, else content/archive/<clip>/final/spec.json
    direct = GOLDEN / "approved" / f"{s['id']}.md"
    if direct.exists():
        t = direct.read_text(encoding="utf-8")
        body = t.split("\n---", 1)[1].strip() if t.startswith("---") and "\n---" in t[3:] else t.strip()
        if re.search(r"^\s*\d+\.\s*\*\*\[", body, re.M):
            return body
    src = s.get("source") or ""
    if src and (P.ROOT / src).exists() and str(src).endswith(".md"):
        # For non-spec channels (e.g. @vanhiep.tech), allow numbered beats directly in the approved markdown
        clipdir = P.ROOT / Path(src).parent.parent
        spec = clipdir / "final/spec.json"
        if not spec.exists():
            t = (P.ROOT / src).read_text(encoding="utf-8")
            body = t.split("\n---", 1)[1].strip() if t.startswith("---") and "\n---" in t[3:] else t.strip()
            if re.search(r"^\s*\d+\.\s*\*\*\[", body, re.M):
                return body
            return None
    else:
        if not src:
            return None
        clipdir = P.ROOT / Path(src).parent.parent  # content/archive/<clip>/final/script-final.md → content/archive/<clip>
        spec = clipdir / "final/spec.json"
    if not spec.exists():
        return None
    sp = json.loads(spec.read_text(encoding="utf-8"))
    out, n = [], 0
    for p in sp.get("parts", []):
        for sc in p.get("scenes", []) + p.get("sections", []):
            words = " ".join((l.get("text") or "").strip() for l in sc.get("lines", []) if l.get("text"))
            if words:
                n += 1
                out.append(f"{n}. **[{sc.get('id', f'b{n:02d}')}]** {words}")
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
    if s.get("_words"):
        return strip_markup(s["_words"])
    w = rejected_words(s) if s["verdict"] == "rejected" else approved_words(s)
    return strip_markup(w) if w else w


def detect_channel(sample, text=""):
    """Identify channel: '@vanhiep.tech' vs '@hi.oneup'."""
    if sample and sample.get("channel"):
        ch = str(sample["channel"]).lower()
        return "@vanhiep.tech" if ("vht" in ch or "vanhiep" in ch) else "@hi.oneup"
    src = str((sample or {}).get("source") or "").lower()
    sid = str((sample or {}).get("id") or "").lower()
    if "vanhiep-tech" in src or "vht-" in src or sid.startswith(("vht-", "a-vht", "r-vht")):
        return "@vanhiep.tech"
    return "@hi.oneup"


def detect_format(sample, text=""):
    """Classify structure style: 'instructional_list' (hướng dẫn liệt kê / khung bản chất) vs 'story_metaphor' (kể chuyện ẩn dụ)."""
    if sample and sample.get("format"):
        return str(sample["format"])
    norm = unicodedata.normalize("NFC", text or "")
    hits = LIST_FORMAT_RE.findall(norm)
    has_list_triad = all(re.search(p, norm, re.I) for p in (r"(?<!\w)thứ nhất(?!\w)", r"(?<!\w)thứ hai(?!\w)", r"(?<!\w)cuối cùng(?!\w)"))
    if len(hits) >= 2 or has_list_triad:
        return "instructional_list"
    return "story_metaphor"


def detect_theme(sample, text=""):
    """Classify dominant topic theme from text + sample metadata using word-boundary matching."""
    if sample and sample.get("theme"):
        return str(sample["theme"])
    low = " " + " ".join(re.findall(r"[a-z0-9]+", _fold((text or "") + " " + str((sample or {}).get("source") or "")))) + " "
    best_theme, best_hits = "general", 0
    for theme, kws in THEME_KEYWORDS.items():
        hits = sum(1 for k in kws if f" {' '.join(re.findall(r'[a-z0-9]+', _fold(k)))} " in low)
        if hits > best_hits:
            best_theme, best_hits = theme, hits
    return best_theme


def load_approved_pool(all_samples, golden_dir=GOLDEN):
    """Merge approved entries from index.json and optional research/review-golden/approved/*.md files."""
    pool = [dict(x) for x in all_samples if x.get("verdict") == "approved"]
    known_ids = {x["id"] for x in pool}
    app_dir = Path(golden_dir) / "approved"
    if app_dir.exists():
        for f in sorted(app_dir.glob("*.md")):
            sid = f.stem
            if sid in known_ids:
                continue
            raw = f.read_text(encoding="utf-8")
            fm = {}
            if raw.startswith("---") and "\n---" in raw[3:]:
                head, body = raw[3:].split("\n---", 1)
                for ln in head.splitlines():
                    if ":" in ln:
                        k, v = ln.split(":", 1)
                        fm[k.strip()] = v.strip().strip('"')
            else:
                body = raw
            pool.append({
                "id": sid,
                "verdict": "approved",
                "channel": fm.get("channel"),
                "format": fm.get("format"),
                "theme": fm.get("theme"),
                "source": str(f.relative_to(P.ROOT)) if P.ROOT in f.resolve().parents else str(f),
                "_words": body.strip(),
            })
    return pool


SOUTHERN_MARKERS_RE = re.compile(r"(?<!\w)(?:nha|á|hông|nè|hen|ha|hà|nghen|vô|coi|ghê|đâu có|trời ơi|mắc cười|thiệt)(?!\w)", re.I)


def _anchor_craft_bonus(text):
    """Prefer anchors that demonstrate confirmed Southern spoken voice (>= 2 distinct markers) over minimal legacy scripts."""
    hits = {m.group(0).lower() for m in SOUTHERN_MARKERS_RE.finditer(unicodedata.normalize("NFC", text or ""))}
    return 2.5 if len(hits) >= 2 else 0.0


def select_anchor_with_meta(all_samples, sample_id, preferred_anchor=None, sample=None, draft_words=None, golden_dir=GOLDEN):
    """Theme/Format-Matched Anchor Selection (leave-one-out).

    Matches approved scripts by:
      1. Same channel (`@hi.oneup` vs `@vanhiep.tech`): +10.0
      2. Same theme (`habit_procrastination` / `memory_study` / `tech_dev`): +5.0
      3. Same structural format (`story_metaphor` vs `instructional_list`): +2.0
      4. Anchor spoken-voice craft quality (≥2 Southern spoken markers): +2.5
      5. Token Jaccard overlap: up to +1.0
      6. Newer approved script as tie-breaker: +0.5 * (idx / len)
    Returns `(anchor_id, anchor_words, match_meta)`.
    """
    pool = [x for x in load_approved_pool(all_samples, golden_dir=golden_dir) if x["id"] != sample_id]
    if preferred_anchor and preferred_anchor != "auto":
        cand = next((x for x in pool if x["id"] == preferred_anchor or x.get("clip") == preferred_anchor), None)
        if cand:
            w = words_for(cand)
            if w:
                return cand["id"], w, {"reason": "explicit --anchor", "anchor_channel": detect_channel(cand, w),
                                       "anchor_format": detect_format(cand, w), "anchor_theme": detect_theme(cand, w)}

    if sample is None:
        sample = next((x for x in all_samples if x["id"] == sample_id), {"id": sample_id})
    d_words = draft_words if draft_words is not None else (words_for(sample) if sample.get("verdict") else "")
    d_ch = detect_channel(sample, d_words)
    d_fmt = detect_format(sample, d_words)
    d_thm = detect_theme(sample, d_words)
    d_toks = _content_tokens(d_words)

    best = None
    n_pool = max(len(pool), 1)
    for idx, cand in enumerate(pool):
        w = words_for(cand)
        if not w:
            continue
        c_ch = detect_channel(cand, w)
        c_fmt = detect_format(cand, w)
        c_thm = detect_theme(cand, w)
        c_toks = _content_tokens(w)
        jac = (len(d_toks & c_toks) / max(len(d_toks | c_toks), 1)) if (d_toks and c_toks) else 0.0
        craft = _anchor_craft_bonus(w)

        score = 0.0
        reasons = []
        if c_ch == d_ch:
            score += 10.0
            reasons.append(f"kênh {c_ch}")
        if c_thm == d_thm and d_thm != "general":
            score += 5.0
            reasons.append(f"chủ đề {c_thm}")
        if c_fmt == d_fmt:
            score += 2.0
            reasons.append(f"format {c_fmt}")
        if craft > 0:
            score += craft
        score += 1.0 * jac + 0.5 * (idx / n_pool)
        meta = {
            "channel": d_ch,
            "format": d_fmt,
            "theme": d_thm,
            "anchor_channel": c_ch,
            "anchor_format": c_fmt,
            "anchor_theme": c_thm,
            "jaccard": round(jac, 3),
            "craft_bonus": craft,
            "score": round(score, 3),
            "reason": " + ".join(reasons) if reasons else "fallback mới nhất",
        }
        if best is None or score > best[0]:
            best = (score, cand["id"], w, meta)

    if not best:
        return None, None, {}
    return best[1], best[2], best[3]


def resolve_anchor(all_samples, sample_id, preferred_anchor=None, sample=None, draft_words=None):
    """Backward-compatible wrapper returning `(anchor_id, anchor_words)` via Theme/Format-Matched Selection."""
    aid, aw, _ = select_anchor_with_meta(
        all_samples, sample_id, preferred_anchor=preferred_anchor, sample=sample, draft_words=draft_words
    )
    return aid, aw


def leave_one_out(tmp, sid):
    g = tmp / "golden"
    (g / "rejected").mkdir(parents=True)
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
    if tv:
        return tv[0]
    hits = re.findall(r"VERDICT\**\s*:\s*\**(ĐẠT VỀ ĐIỂM|CHƯA ĐẠT|CẦN SỬA|ĐẠT)", text or "", re.I)
    return hits[-1].upper() if hits else None


LIMIT_RE = re.compile(r"hit your (?:\d+-hour |weekly )?limit|usage limit|rate limit", re.I)
STOP = threading.Event()


def _invoke_reviewer(prompt, tmp, model, engine="claude"):
    """Run reviewer via `claude -p`, `agy -p`, or `cursor-agent -p` (ask mode, when the other CLIs are out of quota)."""
    if engine == "cursor":
        agent = shutil.which("cursor-agent") or str(Path.home() / ".local/bin/cursor-agent")
        model_name = model if model and model not in ("sonnet", "default") else "grok-4.7-medium"
        args = [agent, "-p", "--mode", "ask", "--trust", "--model", model_name, "--output-format", "text", prompt]
        r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=str(P.ROOT))
        return {"result": r.stdout}, r.stdout, r.stderr, model_name
    if engine == "agy":
        if not P.AGY_BIN or not os.path.exists(P.AGY_BIN):
            raise SystemExit("agy CLI not found (AGY_BIN)")
        args = [P.AGY_BIN, "-p", prompt, "--output-format", "json", "--mode", "plan", "--add-dir", str(tmp),
                "--print-timeout", "300s"]
        if model and model not in ("sonnet", "default"):
            args += ["--model", model]
        r = subprocess.run(args, capture_output=True, text=True, timeout=360, cwd=str(P.ROOT))
        try:
            out = json.loads(r.stdout.strip().splitlines()[-1])
            text = out.get("response", "")
        except (json.JSONDecodeError, IndexError):
            out, text = {}, r.stdout
        return out, text, r.stderr, out.get("model") or model
    args = [CLAUDE, "-p", prompt, "--model", model, "--output-format", "json", "--allowedTools", "Read",
            "--add-dir", str(tmp)]
    r = subprocess.run(args, capture_output=True, text=True, timeout=900, cwd=str(P.ROOT))
    try:
        out = json.loads(r.stdout)
        text = out.get("result", "")
    except json.JSONDecodeError:
        out, text = {}, r.stdout
    return out, text, r.stderr, model


def run_one(s, model, prompt_tpl, mode="pairwise", anchor_pref=None, all_samples=None, engine="claude"):
    words = words_for(s)
    if not words:
        return {"id": s["id"], "verdict_hiep": s["verdict"], "skipped": "no words"}
    anchor_id, anchor_words, anchor_meta = (None, None, {})
    if mode == "pairwise":
        anchor_id, anchor_words, anchor_meta = select_anchor_with_meta(
            all_samples or samples(), s["id"], preferred_anchor=anchor_pref, sample=s, draft_words=words
        )
        if not anchor_words:
            return {"id": s["id"], "verdict_hiep": s["verdict"], "error": "no approved anchor available"}
    blindspots = load_feedback_blindspots()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        draft = tmp / "draft.md"
        draft.write_text("# Bản nháp cần review\n\n" + words + "\n", encoding="utf-8")
        anchor_file = tmp / "anchor.md"
        if anchor_words:
            anchor_file.write_text(f"# Bản chuẩn đã được Hiệp duyệt ({anchor_id})\n\n" + anchor_words + "\n", encoding="utf-8")
        g = leave_one_out(tmp, s["id"])
        prompt = (
            prompt_tpl
            .replace("{DRAFT}", str(draft))
            .replace("{ANCHOR}", str(anchor_file) if anchor_words else "(không có)")
            .replace("{ANCHOR_ID}", anchor_id or "(none)")
            .replace("{ANCHOR_MATCH}", anchor_meta.get("reason") or "mặc định")
            .replace("{FEEDBACK_BLINDSPOTS}", blindspots)
            .replace("{CLIP_DIR}", str(tmp / "noclip"))
            .replace("{GOLDEN}", str(g))
            + f"\n\n(Chế độ đo: không mở thư mục research/review-golden/ gốc và không mở content/archive/{s.get('clip', '')}/; chỉ đọc {draft}"
            + (f", {anchor_file}" if anchor_words else "")
            + ".)"
        )
        out, text, stderr, used_model = _invoke_reviewer(prompt, tmp, model, engine=engine)
    if LIMIT_RE.search(text or stderr or "") and "VERDICT" not in (text or ""):
        STOP.set()
        return {"id": s["id"], "verdict_hiep": s["verdict"], "error": "usage limit", "tail": (text or stderr)[-200:]}
    if out.get("status") == "ERROR" or out.get("error"):
        return {"id": s["id"], "verdict_hiep": s["verdict"], "error": str(out.get("error"))[:200], "tail": (text or stderr)[-200:]}
    b = parse_block(text)
    v = parse_verdict(text)
    row = {
        "id": s["id"],
        "verdict_hiep": s["verdict"],
        "mode": mode,
        "engine": engine,
        "model": used_model,
        "anchor_id": anchor_id,
        "anchor_match": anchor_meta,
        "verdict_reviewer": v,
        "verdict_llm": (b or {}).get("verdict_llm"),
        "pairwise": (b or {}).get("pairwise"),
        "top_fixes": (b or {}).get("top_fixes") or [],
        "score": (b or {}).get("score"),
        "parts": (b or {}).get("parts"),
        "hard_fails": (b or {}).get("hard_fails"),
        "soft_warnings": (b or {}).get("soft"),
        "block": b is not None,
        "cost_usd": out.get("total_cost_usd"),
        "ok": (v not in ("ĐẠT", "ĐẠT VỀ ĐIỂM")) if s["verdict"] == "rejected" else (v in ("ĐẠT", "ĐẠT VỀ ĐIỂM")),
        "tail": (text or stderr)[-600:],
    }
    return row


def metrics(rows, mode="pairwise"):
    rej = [r for r in rows if r["verdict_hiep"] == "rejected" and not r.get("skipped") and r.get("verdict_reviewer")]
    app = [r for r in rows if r["verdict_hiep"] == "approved" and not r.get("skipped") and r.get("verdict_reviewer")]
    caught = sum(1 for x in rej if x["ok"])
    passed = sum(1 for x in app if x["ok"])
    pct = lambda xs: round(100 * sum(1 for x in xs if x["ok"]) / len(xs), 1) if xs else None
    rc_pct = pct(rej)
    ap_pct = pct(app)
    bal_acc = round((rc_pct + ap_pct) / 2.0, 1) if (rc_pct is not None and ap_pct is not None) else None
    m = {
        "mode": mode,
        "rejected_caught": f"{caught}/{len(rej)}",
        "approved_passed": f"{passed}/{len(app)}",
        "rejected_caught_pct": rc_pct,
        "rejected_n": len(rej),
        "approved_passed_pct": ap_pct,
        "approved_n": len(app),
        "balanced_accuracy_pct": bal_acc,
        "no_verdict": sum(1 for r in rows if not r.get("skipped") and not r.get("verdict_reviewer") and not r.get("error")),
        "errors": sum(1 for r in rows if r.get("error")),
        "skipped": sum(1 for r in rows if r.get("skipped")),
        "target": "rejected ≥ 14/15, approved all",
        "verdict_source": "review_tiers (pairwise A/B theme-matched + H1–H4)" if mode == "pairwise" else "review_tiers (DL-074)",
        "cost_usd": round(sum(r.get("cost_usd") or 0 for r in rows), 4),
    }
    if mode == "pairwise":
        pw_counts = lambda xs: {k: sum(1 for x in xs if x.get("pairwise") == k) for k in ("WIN", "TIE", "LOSE")}
        m["pairwise_rejected"] = pw_counts(rej)
        m["pairwise_approved"] = pw_counts(app)
    return m


def main():
    a = sys.argv[1:]
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    mode = opt("--mode", "pairwise")
    if mode not in ("pairwise", "score"):
        raise SystemExit("--mode must be pairwise or score")
    engine = opt("--engine", "claude")
    if engine not in ("claude", "agy", "cursor"):
        raise SystemExit("--engine must be claude, agy, or cursor")
    anchor_pref = opt("--anchor")
    model = opt("--model", "sonnet" if engine == "claude" else ("grok-4.7-medium" if engine == "cursor" else "default"))
    all_ss = samples()
    ss = list(all_ss)
    if opt("--only"):
        ss = [s for s in ss if s["id"] in opt("--only").split(",")]
    if opt("--limit"):
        ss = ss[: int(opt("--limit"))]
    if "--dry-run" in a:
        for s in ss:
            w = words_for(s)
            if mode == "pairwise" and w:
                anc, _, meta = select_anchor_with_meta(all_ss, s["id"], preferred_anchor=anchor_pref, sample=s, draft_words=w)
                why = meta.get("reason", "")
            else:
                anc, why = "-", ""
            print(f"{s['id']:14} {s['verdict']:9} anchor={anc:6} ({why:42}) {'words ' + str(len(w.splitlines())) + ' beats' if w else 'SKIP (no words)'}")
        print(f"{sum(1 for s in ss if words_for(s))} with words / {len(ss)} (mode={mode}, engine={engine})")
        return 0
    tpl = load_prompt()
    jobs = int(opt("--jobs", "1"))
    # Skip samples without words up front so worker pool only runs real evaluations
    runnable = [s for s in ss if words_for(s)]
    skipped_rows = [{"id": s["id"], "verdict_hiep": s["verdict"], "skipped": "no words"} for s in ss if not words_for(s)]

    def one(s):
        if STOP.is_set():
            return {"id": s["id"], "verdict_hiep": s["verdict"], "error": "not run (usage limit hit earlier)"}
        r = run_one(s, model, tpl, mode=mode, anchor_pref=anchor_pref, all_samples=all_ss, engine=engine)
        detail = f"pw={r.get('pairwise')} vs {r.get('anchor_id')}" if mode == "pairwise" else f"score={r.get('score')}"
        print(f"{r['id']:14} Hiệp={r['verdict_hiep']:9} reviewer={r.get('verdict_reviewer') or r.get('skipped') or r.get('error')}"
              f" {detail} hf={len(r.get('hard_fails') or [])}  {'✔' if r.get('ok') else ('–' if r.get('skipped') or r.get('error') else '✖')}", flush=True)
        return r

    with ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
        ran_rows = list(ex.map(one, runnable))
    by_id = {r["id"]: r for r in ran_rows + skipped_rows}
    rows = [by_id[s["id"]] for s in ss]
    m = metrics(rows, mode=mode)
    out = Path(opt("--out", str(GOLDEN / f"eval-{dt.date.today().isoformat()}.json")))
    out.write_text(json.dumps({
        "date": dt.date.today().isoformat(),
        "engine": engine,
        "model": next((r.get("model") for r in ran_rows if r.get("model")), model),
        "mode": mode,
        "anchor": anchor_pref or "auto-theme-format-matched",
        "prompt": str(PROMPT_MD.relative_to(P.ROOT)),
        "metrics": m,
        "rows": rows,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(m, ensure_ascii=False))
    print(f"→ {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
