#!/usr/bin/env python3
"""Rule linter for one clip (rule-48). Lints the clip spec (+ script, plan, MP4, post) against rules/video-rules.md.

  check-rules.py content/clips/<clip>/            # gate 1: spec + script + post (if any) + plan validation
  check-rules.py content/clips/<clip>/ --final    # gate 2: also the rendered MP4 (ffprobe, loudness) + post.md required
  check-rules.py ... --stt                        # also STT every voice line and compare with the text (slow, ~1 min)
  check-rules.py ... --out report.txt
  check-rules.py --subjects draft.md [more.md]   # L-087 only: spoken text must not use school subjects as examples
  check-rules.py --l088 draft.md [more.md]       # L-088 only: evidence cited + spoken, hook/CTA not copied from earlier clips, trend link
  check-rules.py --trend draft.md [more.md]      # L-090 only: trend_id/hook_pattern from research/trends, trend spoken in b01–b02, not saturated, example_evidence
  check-rules.py --flow draft.md [more.md]       # L-089 only (⚠): narrator switches, beat openers with no link, «X, mà càng X» stitching, listy evidence, tacked-on maxim
  check-rules.py --fresh draft.md [--against old.md …]  # L-095: hook / beat chain similarity ≥0.5 vs every other script-v*.md of the clip (incl. git history) → ✖
  check-rules.py --link draft.md [more.md]       # L-094 (⚠): adjacent sentence pair (within or across beats) sharing no content word and not opening with a connector / back-reference
  check-rules.py --repeat draft.md [more.md]     # L-093: content word >5% of words (✖), repeated 3-word phrase (⚠), ≥3 sentences opening with the same connector (⚠)
  check-rules.py --clarity draft.md [more.md]    # L-091 only (⚠): b01–b03 question before situation, sentence >25 words, vague words, «cũng thấy vậy» generalisation
  check-rules.py content/clips/<clip>/ --prosody final/prosody-measure-v16b.json   # voice-only mode: L-070 + E1 + L-027 on a voice-only preview measure
  (every mode also runs E1 + L-027 on the newest final/prosody-measure-*.json when one exists; see check_e1 / check_l027_voice)

Source: <clip>/final/spec.json (format: see skills/make-video/SKILL.md). Exit 1 if any ✖ error. Also runs the lessons gate (rule-49, logs/lessons.md): checks named L-NNN.
"""
import json, os, re, subprocess, sys, difflib, unicodedata, glob, math, tempfile

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
REPO = str(P.ROOT)
NODE_BIN = os.environ.get("NODE22_BIN", "/workspace/tools/node-v22.20.0-linux-x64/bin")
ASR_PY = os.environ.get("ASR_PYTHON", "/workspace/asr-venv/bin/python")
res = []
def ok(rule, msg): res.append(("✔", rule, msg))
def warn(rule, msg): res.append(("⚠", rule, msg))
def err(rule, msg): res.append(("✖", rule, msg))
def info(rule, msg): res.append(("ℹ", rule, msg))  # not counted as error/warning (skips, coverage notes)

VI_CHARS = re.compile(r"[ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\U0001F000-\U0001F2FF]")
AI_TELLS = ["bạn có biết", "hãy cùng", "bí quyết", "thay đổi cuộc đời", "chìa khoá vàng", "chìa khóa vàng", "đỉnh cao", "và đó chính là", "không phải là", "hành trình"]
PARTICLES = ["nha", "á", "hông", "nè", "hen", "ha", "đó", "luôn", "thôi"]
EN_EXEMPT = {"toeic", "messenger", "oneup", "omi", "tiktok", "ios", "app", "laptop", "comment", "ok", "okay"}
EN_MIX = {"code", "listening", "deadline", "work", "focus", "ship", "plan", "lock", "in", "productive", "goal", "habit", "check", "level", "mindset", "skip", "reset"}
SFX_OK = {"pop", "ding", "whoosh", "tick", "click", "whoosh-soft", "swish", "ambience", "snap", "pen", "stamp", "rise"}

def norm(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", s.replace("đ", "d")).split()

def lines(spec):
    for p in spec["parts"]:
        for s in p.get("scenes", []) + p.get("sections", []):
            for l in s["lines"]:
                yield p, s, l

def ffprobe(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name,profile,width,height,r_frame_rate,pix_fmt,color_space,sample_rate:format=duration",
                        "-of", "json", path], capture_output=True, text=True).stdout
    return json.loads(o)

def theme_map(clip_no):
    tm = open(os.path.join(REPO, "content/theme-map.md")).read()
    for row in tm.splitlines():
        c = [x.strip() for x in row.strip("|").split("|")]
        if len(c) >= 8 and c[0] == str(clip_no):
            week = int(c[1]) if c[1].isdigit() else None
            theme = "light" if "LIGHT" in c[-1].upper() else "dark" if "DARK" in c[-1].upper() else None
            return week, theme
    return None, None

def _fold(s):  # per-char: strip Vietnamese marks (keeps length), đ→d
    return "".join(unicodedata.normalize("NFD", c)[0] for c in s).replace("đ", "d").replace("Đ", "D")

def display_texts(spec, fdir):
    """L-067: every Vietnamese string drawn on screen (not the spoken/caption lines themselves)."""
    out = []
    for p in spec.get("parts", []):
        for s in p.get("scenes", []) + p.get("sections", []):
            if s.get("narration"): out.append((f"{s['id']}.narration", s["narration"]))
            for i, pr in enumerate(s.get("props", [])):
                for k in ("text", "sub", "stamp"):
                    if pr.get(k): out.append((f"{s['id']}.props[{i}].{k}", pr[k]))
                for k in ("words", "pages"):
                    for w in pr.get(k) or []: out.append((f"{s['id']}.props[{i}].{k}", w))
    if (spec.get("hook") or {}).get("text"): out.append(("hook.text", spec["hook"]["text"]))
    covs = [("spec.cover", spec.get("cover") or {})] + [(os.path.relpath(f, fdir), json.load(open(f))) for f in sorted(glob.glob(os.path.join(fdir, "cover", "*.props.json")))]
    for src, cv in covs:
        for w in cv.get("hero") or []: out.append((f"{src}.hero", w))
        if cv.get("series"): out.append((f"{src}.series", cv["series"]))
    for f in sorted(glob.glob(os.path.join(fdir, "explainer", "compositions", "*.html.tpl")) + glob.glob(os.path.join(fdir, "explainer", "index.html.tpl"))):
        h = re.sub(r"(?is)<(script|style)\b.*?</\1>|<!--.*?-->", " ", open(f).read())
        for m in re.findall(r">([^<>{}]+)<", h):
            if m.strip(): out.append((os.path.relpath(f, fdir), m.strip()))
    for f in sorted(glob.glob(os.path.join(fdir, "endcard*.txt")) + glob.glob(os.path.join(fdir, "out", "endcard*.txt"))):
        out.append((os.path.relpath(f, fdir), open(f).read()))
    return out

def check_diacritics(spec, fdir, L):
    """L-067: on-screen Vietnamese text must keep its marks. Reference = locked spoken lines + latest script-vNN.md."""
    ref = " ".join(re.sub(r"\{[^}]*\}|\*", "", l["text"]) for _, _, l in L)
    sv = sorted(glob.glob(os.path.join(fdir, "script-v*.md")), key=lambda x: int(re.findall(r"v(\d+)", os.path.basename(x))[0]))
    if sv: ref += " " + open(sv[-1]).read()
    forms = {}
    for w in re.findall(r"\w+", ref.lower()): forms.setdefault(_fold(w), set()).add(w)
    bad = []
    for src, s in display_texts(spec, fdir):
        toks = [w for w in re.findall(r"\w+", s.lower()) if not w.isdigit()]
        if not toks: continue
        viet = VI_CHARS.search(s) or sum(_fold(w) in forms for w in toks) / len(toks) >= 0.6  # English strings (explainer labels) are not Vietnamese → skip
        lost = [w for w in toks if _fold(w) == w and w in forms and w not in forms[w]]
        if viet and lost: bad.append(f"{src} “{s.strip()[:60]}” (mất dấu: {', '.join(sorted(set(lost))[:6])})")
    (ok if not bad else err)("L-067", "on-screen Vietnamese text keeps diacritics vs locked script" + (": " + "; ".join(bad) if bad else ""))

def check_prosody_file(pm, fdir):
    """L-070 on an explicit measure json (voice-only previews, e.g. final/prosody-measure-v16b.json from voice-delivery-f5.py measure):
    no spec voice_prefix to match; every flag (pause vs delivery mark, comma ≥0.15 and < sentence pause, >0.5s, break inside a phrase,
    stress <2 dB vs sentence or neighbours, question not rising ≥0.5 st, STT <0.8, total >58s) blocks; warnings (>5 syll/s, pause off plan) only listed."""
    if not os.path.exists(pm): err("L-070", f"{os.path.relpath(pm, REPO)} missing"); return
    j = json.load(open(pm)); fl = j.get("flags", []); wn = j.get("warnings", [])
    dl = glob.glob(os.path.join(fdir, "script-*-delivery.md"))
    (ok if dl else err)("L-070", "delivery plan present (" + ", ".join(sorted(os.path.basename(d) for d in dl)) + ")")
    info = f"voice {j.get('voice_prefix')} plan {j.get('plan')}: {j.get('total_s')}s total, {len(j.get('sentences', []))} sentences, {len(j.get('pauses', []))} marks measured"
    (ok if not fl else err)("L-070", info + f", {len(fl)} blocking flags" + (": " + "; ".join(fl[:12]) if fl else ""))
    if wn: warn("L-070", f"{len(wn)} warnings: " + "; ".join(wn[:12]))

# ---- voice-only checks on prosody-measure-*.json (E1, L-027) ------------------------------------------------------------
# E1 mid-phrase-pause (Kokoro Voice, research/agents/kokoro-voice-tiktok-prosody-vi.md §E1; Rule Reviewer R8 20/10/2026, W-17).
# PROVISIONAL thresholds: taken from Northern-voice / slow-reading TTS research (~0.14s already heard as a phrase boundary);
# to be recalibrated on the F5 · Thái Sơn voice with the v18 measure data. Change them only here.
E1_WARN_S = 0.12      # silence ≥ this where there is no delivery mark → ⚠
E1_BLOCK_S = 0.25     # silence ≥ this where there is no delivery mark → ✖
E1_CLUSTER_S = 0.12   # silence ≥ this inside a forbidden cluster (cụm cấm ngắt) → ✖
L027_GAP_S = 0.1      # L-027: joins between clauses/lines inside the hook must be ≤ this
E1_DEFAULT_CLUSTERS = {"clip-04": ["ngay thì", "nhỏ thì", "kiểm tra lại nhớ", "cần là sáng", "gấp sách lại thì"]}  # script-v18-delivery.md R4/R9 + R8
MARK_AT = {"/": "comma", "//": "sentence", "//beat": "beat", "///": "beat"}  # voice-delivery-f5.py marks → at_mark ("///" = deliberate pause, counted as a mark)
"""Silence schema read by E1 (optional top-level key `silences` in prosody-measure-*.json, one entry per measured silence ≥ ~0.05s
between two spoken words, whole voice-only file):
  {"chunk_id": "c07",            # chunk / sentence id the silence sits in (or after)
   "t_start": 12.41, "t_end": 12.60, "dur_s": 0.19,   # seconds in the delivered wav
   "at_mark": "none",            # none | comma | sentence | beat  (delivery mark at that word boundary; none = no mark)
   "context_before": "nếu kiểm tra ngay",   # a few words before the silence (≥ 2 recommended)
   "context_after": "thì nhớ được"}         # a few words after the silence
Until voice-delivery-f5.py measure writes `silences`, E1 derives them from the existing keys: `pauses[]` (sid, after, mark, pause →
at_mark from MARK_AT, no context_after) and `sentences[].mid_breaks` ("«a b» 0.27s" → at_mark none). The current measure only records
mid_breaks > 0.25s, so in derived mode 0.12–0.25s mid-phrase silences are invisible (E1 says so with a ⚠ coverage line)."""

def _vkey(path):
    m = re.search(r"v(\d+)([a-z]*)", os.path.basename(path))
    return (int(m.group(1)), m.group(2), os.path.getmtime(path)) if m else (-1, "", os.path.getmtime(path))

def latest_measure(fdir):
    ms = glob.glob(os.path.join(fdir, "prosody-measure-*.json"))
    return max(ms, key=_vkey) if ms else None

def _words(s): return re.sub(r"[^\w\s]", " ", unicodedata.normalize("NFC", (s or "").lower())).split()

def measure_silences(j):
    """→ (silences in the E1 schema, 'silences' | 'derived')."""
    if isinstance(j.get("silences"), list):
        return [dict(x, dur_s=float(x.get("dur_s", x.get("t_end", 0) - x.get("t_start", 0)))) for x in j["silences"]], "silences"
    out = []
    for p in j.get("pauses", []):
        out.append({"chunk_id": p.get("sid"), "t_start": None, "t_end": None, "dur_s": float(p.get("pause", 0)), "at_mark": MARK_AT.get(p.get("mark"), "none" if not p.get("mark") else "beat"),
                    "context_before": p.get("after", ""), "context_after": ""})
    for s in j.get("sentences", []):
        for mb in s.get("mid_breaks") or []:
            m = re.match(r"«(.+?)\s+(\S+)»\s*([\d.]+)s", mb)
            if m: out.append({"chunk_id": s.get("id"), "t_start": None, "t_end": None, "dur_s": float(m.group(3)), "at_mark": "none", "context_before": m.group(1), "context_after": m.group(2)})
    return out, "derived"

def delivery_clusters(fdir, clip):
    """Forbidden clusters: «…» items after 'cụm cấm ngắt' (up to the sentence end) in the newest script-v*-delivery.md; else the clip default."""
    dl = sorted(glob.glob(os.path.join(fdir, "script-v*-delivery.md")), key=_vkey)
    if dl:
        for ln in open(dl[-1], encoding="utf8").read().splitlines():
            i = ln.lower().find("cụm cấm ngắt")
            if i < 0: continue
            seg = re.split(r"\.(?:\s|$)", ln[i:], maxsplit=1)[0]
            cl = [c.strip() for c in re.findall(r"«([^»]+)»", seg) if len(_words(c)) >= 2]
            if cl: return cl, os.path.basename(dl[-1])
    for k, v in E1_DEFAULT_CLUSTERS.items():
        if k in clip: return v, f"default {k} list"
    return [], None

def cluster_hit(before, after, cluster):
    """True when the silence splits `cluster`: context_before ends with its first part and context_after starts with the rest.
    Contexts shorter than the part are compared on the words available (≥ 1 word each side)."""
    bw, aw, cw = _words(before), _words(after), _words(cluster)
    if not bw or not aw: return False
    for k in range(1, len(cw)):
        left, right = cw[:k], cw[k:]; n1 = min(len(bw), len(left)); n2 = min(len(aw), len(right))
        if bw[-n1:] == left[-n1:] and aw[:n2] == right[:n2]: return True
    return False

def check_e1(j, fdir, clip, src, soft=False):
    """E1 mid-phrase-pause. ✖ silence ≥ E1_CLUSTER_S inside a forbidden cluster; at_mark none: ⚠ ≥ E1_WARN_S, ✖ ≥ E1_BLOCK_S.
    soft=True (measure is not for the spec's voice) turns ✖ into ⚠."""
    E = warn if soft else err
    sil, mode = measure_silences(j); cl, csrc = delivery_clusters(fdir, clip)
    blk, wrn = [], []
    for x in sil:
        d = x["dur_s"]; where = f"{x.get('chunk_id')} «{' '.join(_words(x.get('context_before'))[-3:])} | {' '.join(_words(x.get('context_after'))[:3])}» {d:.2f}s"
        hit = next((c for c in cl if cluster_hit(x.get("context_before"), x.get("context_after"), c)), None)
        if hit and d >= E1_CLUSTER_S: blk.append(f"{where} trong cụm cấm ngắt «{hit}»")
        elif x.get("at_mark", "none") == "none":
            if d >= E1_BLOCK_S: blk.append(f"{where} không có ký hiệu ngắt (≥{E1_BLOCK_S}s)")
            elif d >= E1_WARN_S: wrn.append(f"{where} không có ký hiệu ngắt (≥{E1_WARN_S}s)")
    tag = f"{src}: {len(sil)} silences ({mode}), clusters {cl or 'none'} ({csrc or 'no list'}); thresholds provisional"
    (E if blk else ok)("E1", f"mid-phrase pauses — {tag}" + (f"; {len(blk)} blocking: " + "; ".join(blk[:10]) if blk else ""))
    if wrn: warn("E1", f"{len(wrn)} silence(s) ≥{E1_WARN_S}s at no mark: " + "; ".join(wrn[:10]))
    if mode == "derived": warn("E1", f"{src} has no `silences` list → only mid_breaks >0.25s are visible; 0.12–0.25s mid-phrase silences unmeasured (measure must write `silences`)")
    if not cl: info("E1", "no forbidden-cluster list in the delivery plan and no default for this clip → cluster check skipped")

def hook_beats(spec):
    if not spec: return {"b01"}
    ids = set((spec.get("hook") or {}).get("scenes") or (spec.get("structure") or {}).get("hook") or [])
    bt = {s["id"]: s.get("beat", "").split(".")[-1] for p in spec.get("parts", []) for s in p.get("scenes", []) + p.get("sections", [])}
    return {bt.get(i) or i for i in ids} or {"b01"}

def check_l027_voice(j, spec, src, soft=False):
    """L-027 on a voice-only measure: every measured join (pauses[], i.e. the gap at each delivery mark between assembled pieces/chunks)
    whose both sides are hook sentences must be ≤ L027_GAP_S. Hook = sentences with part=='hook' or beat in the spec's hook beats
    (default b01). The hook→body join is not counted. Natural silences inside one F5 chunk are not joins and are left to E1."""
    E = warn if soft else err
    ss = j.get("sentences", []); hb = hook_beats(spec)
    hook = [s["id"] for s in ss if s.get("part") == "hook" or s.get("beat") in hb]
    if not hook: info("L-027", f"{src}: no hook sentences found (hook beats {sorted(hb)}) → voice-only hook-gap check skipped"); return
    order = [s["id"] for s in ss]; hs = set(hook); gaps = []
    for p in j.get("pauses", []):
        sid = p.get("sid")
        if sid not in hs: continue
        if p.get("mark") == "/": nxt = sid
        else: k = order.index(sid) if sid in order else -1; nxt = order[k + 1] if 0 <= k < len(order) - 1 else None
        if nxt in hs: gaps.append((sid, nxt, p.get("after"), float(p.get("pause", 0))))
    bad = [f"{a if a == b else a + '→' + b} sau «{w}» {g:.2f}s" for a, b, w, g in gaps if g > L027_GAP_S]
    (E if bad else ok)("L-027", f"voice-only {src}: hook {hook}, {len(gaps)} join(s)" + (f", gaps > {L027_GAP_S}s: {bad[:8]}" if bad else f" all ≤ {L027_GAP_S}s"))

def voice_only_checks(pm, fdir, clip, spec, explicit):
    """E1 + L-027 on a measure json. explicit = --prosody mode (full severity). In spec mode a measure for another voice than
    spec.voice_prefix is a preview: findings are reported as ⚠, not ✖."""
    if not pm or not os.path.exists(pm):
        info("E1", "no final/prosody-measure-*.json → E1 mid-phrase-pause skipped"); info("L-027", "no prosody-measure json → voice-only hook gaps skipped"); return
    j = json.load(open(pm, encoding="utf8")); src = os.path.basename(pm)
    soft = (not explicit) and spec is not None and j.get("voice_prefix") != spec.get("voice_prefix")
    if soft: info("E1", f"{src} is voice {j.get('voice_prefix')}, spec uses {spec.get('voice_prefix')} → preview: E1/L-027 findings reported as ⚠ (run --prosody for the gate)")
    check_e1(j, fdir, clip, src, soft); check_l027_voice(j, spec, src, soft)

def check_prosody(spec, fdir, final):
    """L-070: pauses/phrasing measured on the real voice (pipeline/scripts/prosody-check.py measure → final/prosody-measure.json).
    Blocks: pause >0.8s inside/between lines (beat change allows +0.35s), pause <0.1s at a period, break >0.25s at a word boundary
    without punctuation (= ngắt giữa cụm từ), question not rising at the end."""
    pm = os.path.join(fdir, "prosody-measure.json"); pp = os.path.join(fdir, "prosody-plan.md")
    if not os.path.exists(pm):
        (err if final else warn)("L-070", "prosody-measure.json missing (run prosody-check.py voice + measure after generating the voice)"); return
    j = json.load(open(pm))
    if j.get("voice_prefix") != spec.get("voice_prefix"): err("L-070", f"prosody-measure.json is for voice {j.get('voice_prefix')}, spec uses {spec.get('voice_prefix')} → re-measure"); return
    dl = sorted(glob.glob(os.path.join(fdir, "script-*-delivery.md")))  # the approved delivery plan (/, //, //|, ///, **nhấn**) is the prosody plan
    vm = re.search(r"(v\d+\w*)$", spec.get("voice_prefix") or "")  # pick the plan of THIS voice (c04v18 → script-v18-delivery.md), not the first glob hit
    dv = [d for d in dl if vm and os.path.basename(d) == f"script-{vm.group(1)}-delivery.md"]
    (ok if (dv or os.path.exists(pp)) else err)("L-070", "delivery/prosody plan present (" + (os.path.basename(dv[0]) if dv else "prosody-plan.md" if os.path.exists(pp) else f"none for voice {spec.get('voice_prefix')}") + ")")
    fl = j.get("flags", []); n = len(j.get("lines") or j.get("sentences") or [])
    (ok if not fl else err)("L-070", f"prosody: {n} sentences measured (voice {j.get('voice_prefix')}, {os.path.basename(dv[0]) if dv else 'plan'}), {len(fl)} blocking pause/phrasing flags" + (": " + "; ".join(fl[:8]) if fl else ""))

# ---- L-087 (Hiệp 26/10): ví dụ lấy từ đời thường, cấm lấy môn học (Sinh/Toán/Lý/Hóa/Sử/Địa/Văn…) làm ví dụ ----
_SUBJ = r"(?:sinh|toán|lý|lí|hóa|hoá|sử|địa|văn|anh|gdcd|tin)"
_SUBJ_P = r"(?:sinh|toán|lý|lí|hóa|hoá|sử|địa|văn|gdcd)"  # sau sách/bài/đề…: bỏ «anh» (đại từ), «tin» (tin nhắn)
_SUBJ_NOT = r"(?!\s+(?:viên|hoạt|nhật|ra|con|tồn|động|mệnh|khí|sản|lý|học sinh|thuyết|do|lẽ|tưởng|trí|phòng|bản|hóa|hoá|đơn|dụng|chỉ|điểm|minh|chương|nghệ|học viên|ấy|nhắn|tức|tưởng))"
L087_SPOKEN = [  # error: lời đọc gọi tên môn học hoặc dùng kiến thức môn học làm ví dụ
    (r"(?<!\w)môn\s+" + _SUBJ + r"(?!\w)" + _SUBJ_NOT, "tên môn (môn + Sinh/Toán/Lý/Hóa/Sử/Địa/Văn/Anh…)"),
    (r"(?<!\w)(?:sách|vở|bài|đề|chương|tiết|giờ|điểm|lớp|thi|ôn|học)\s+" + _SUBJ_P + r"(?!\w)" + _SUBJ_NOT, "tên môn sau sách/bài/đề/chương/thi/ôn/học…"),
    (r"(?<!\w)(?:sinh học|hóa học|hoá học|vật lý|vật lí|toán học|ngữ văn|địa lý|địa lí|tin học|môn lịch sử|lịch sử lớp|giáo dục công dân)(?!\w)", "tên môn học"),
    (r"(?<!\w)(?:di truyền|tính trạng|nhiễm sắc thể|gen trội|gen lặn|quang hợp|tế bào học|punnett|phương trình bậc|đạo hàm|tích phân|lượng giác|hình học|định luật newton|bảng tuần hoàn|nguyên tử khối|hóa trị|hoá trị|phản ứng hóa học|phản ứng hoá học)(?!\w)", "kiến thức môn học"),
]
L087_EXEMPT = [r"(?<!\w)học sinh(?!\w)", r"(?<!\w)bài toán(?!\w)", r"(?<!\w)tính toán(?!\w)"]
L087_VISUAL = r"(?<!\w)(?:genetics|biology|chemistry|physics|math(?:s|ematics)? (?:book|textbook|class|problem)|algebra|calculus|geometry|punnett|dna|periodic table|history (?:book|class)|literature (?:book|class)|textbook|sách (?:sinh|toán|lý|lí|hóa|hoá|sử|địa|văn)|sinh học|di truyền|adn)(?!\w)"
_L087_SPOKEN_RE = [(re.compile(pat, re.I), why) for pat, why in L087_SPOKEN]

def _plain(t):  # bỏ markup **…** và {nhấn: …} trước khi soi
    t = unicodedata.normalize("NFC", t or ""); t = re.sub(r"\{[^:{}]*:\s*([^{}]*)\}", r"\1", t); return t.replace("**", "")

def subject_hits(text):
    """L-087: [(cụm khớp, lý do)] cho một câu lời đọc. Cụm đời thường (học sinh, bài toán, tính toán) không tính."""
    t = _plain(text); out = []
    for ex in L087_EXEMPT: t = re.sub(ex, lambda m: "_" * len(m.group(0)), t, flags=re.I)
    for rx, why in _L087_SPOKEN_RE:
        for m in rx.finditer(t): out.append((m.group(0), why))
    return out

def check_l087(spec, L, fdir, clip_dir):
    _cn = re.search(r"clip-(\d+)", clip_dir); e87 = err if (_cn and int(_cn.group(1)) >= 6) else warn  # clip-05 đã Chốt trước L-087 → cảnh báo
    hits = []
    for _, s, l in L:
        seen = set()
        for k in ("text", "say"):
            for h, why in subject_hits(l.get(k)):
                if h.lower() not in seen: seen.add(h.lower()); hits.append(f"{s['id']}: «{h}» ({why})")
    (e87 if hits else ok)("L-087", ("lời đọc lấy môn học làm ví dụ (phải lấy từ đời thường): " + "; ".join(hits)) if hits else "lời đọc không lấy môn học làm ví dụ")
    vis = []
    for p in spec["parts"]:
        for sc in p.get("scenes", []) + p.get("sections", []):
            blob = json.dumps({k: v for k, v in sc.items() if k != "lines"}, ensure_ascii=False)
            for m in sorted({m.group(0).lower() for m in re.finditer(L087_VISUAL, blob, re.I)}): vis.append(f"{sc['id']}:{m}")
    for vp in sorted(glob.glob(os.path.join(fdir, "visual-plan*.md")))[-1:]:
        for m in sorted({m.group(0).lower() for m in re.finditer(L087_VISUAL, open(vp, encoding="utf8").read(), re.I)}): vis.append(f"{os.path.basename(vp)}:{m}")
    (warn if vis else ok)("L-087", ("hình/prop gắn môn học (đổi sang vật đời thường): " + ", ".join(vis[:20])) if vis else "hình/prop không gắn môn học")

def check_subjects_file(path):  # --subjects FILE: soi bản nháp script (.md/.txt) trước khi có spec
    n = 0
    for i, ln in enumerate(open(path, encoding="utf8"), 1):
        for h, why in subject_hits(ln): err("L-087", f"{os.path.basename(path)}:{i}: «{h}» ({why})"); n += 1
    if not n: ok("L-087", f"{os.path.basename(path)}: không gọi tên môn học / kiến thức môn học")

# ---- L-088 (Hiệp 26/10 21:44): có dẫn chứng trong clip, lồng vào mạch chuyện; hook/CTA không rập khuôn; vẫn theo trend ----
# Đo được: (a) có nguồn truy được (tác giả + năm / PMID / doi) ✖ nếu không có; lời đọc có nhắc dẫn chứng (✖ từ clip-06, ⚠ ≤05);
# câu mở dẫn chứng kiểu chèn trích dẫn («Một nghiên cứu cho…», «các nhà nghiên cứu thấy…») ⚠ để soát tay «liền mạch».
# (b) hook/CTA giống hook/CTA clip trước (difflib trên chữ bỏ dấu: 6 chữ đầu hoặc từng câu ≥4 chữ, > L088_SIM) ⚠; mở đầu 2 chữ trùng ≥2 clip trước ⚠.
# (c) trend-signals.md có link nguồn ⚠. «Liền mạch» và «sáng tạo» thật sự = soát tay (manual gate).
L088_SIM = 0.7          # ngưỡng giống nhau (difflib ratio trên token bỏ dấu); hiệu chỉnh trên clip 02–05: cặp khác clip ≤0,29 ở hook
L088_MIN_TOK = 4        # câu ngắn hơn không so (tránh trùng giả «Comment nha»)
_CITE_RE = re.compile(r"(?<![\w@-])(?:[A-Z][a-z'\-]+(?:\s*(?:&|và|and)\s*[A-Z][a-z'\-]+)?(?:\s+(?:et al\.?|và cộng sự|và cs\.?))?,?\s*\(?(?:19[5-9]\d|20[01]\d|202[0-5])\)?(?!\d)"
                      r"|PMID:?\s*\d{6,}|doi\.org/\S+|(?<!\w)doi:\s*10\.\S+|pubmed\.ncbi\.nlm\.nih\.gov/\d+)")
_CITE_STOP = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
              "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Sept", "Oct", "Nov", "Dec", "Clip", "Trend", "Rule", "News", "Hook", "Since", "From", "In", "The"}
L088_EVID_SPOKEN = r"(?<!\w)(?:nghiên cứu|thí nghiệm|khảo sát|phân tích gộp|nhà tâm lý|nhà khoa học|giáo sư|tiến sĩ|các nhà|người tham gia|gộp \d[\d.,]*)(?!\w)"
L088_DRY = r"(?<!\w)(?:một nghiên cứu (?:cho|chỉ|thấy|nói|của|ở|năm)|nghiên cứu (?:cho thấy|chỉ ra|nói rằng|nói là|đã chứng minh|chứng minh)|theo (?:một |các |nhiều )?nghiên cứu|các nhà (?:nghiên cứu|khoa học) (?:thấy|phát hiện|chỉ ra|chứng minh|kết luận)|khoa học (?:đã )?(?:chứng minh|nói)|(?:chuyện này )?có (?:một |hẳn )?nghiên cứu(?: hẳn hoi)?|bằng chứng là)(?!\w)"

def citations(text):
    """L-088: nguồn truy được trong một đoạn chữ → [chuỗi]. Tên tác giả chữ Latin + năm 1950–2025, hoặc PMID/doi/PubMed."""
    out = []
    for m in _CITE_RE.finditer(text or ""):
        s = re.sub(r"\s+", " ", m.group(0)).strip()
        if s.endswith(")") and "(" not in s: s = s[:-1].rstrip()
        if s.split()[0].rstrip(",") in _CITE_STOP: continue
        out.append(s)
    return out

def _l088_clean(t):  # bỏ markup {nhấn: x} → x, **, …, | (ngắt delivery) trước khi so
    t = _plain(t); return re.sub(r"\s+", " ", t.replace("…", " ").replace("\\|", " ").replace("|", " ")).strip()

def _sents(t): return [x for x in re.split(r"(?<=[.!?])\s+", _l088_clean(t)) if len(norm(x)) >= 1]

def similar_to(new, olds):
    """→ [(nhãn, chỉ số, ratio, câu cũ)] khi `new` giống một text cũ: 6 chữ đầu, hoặc một câu (≥ L088_MIN_TOK chữ) giống một câu cũ."""
    hits = []; nn = norm(_l088_clean(new))
    if not nn: return hits
    for lab, old in olds:
        on = norm(_l088_clean(old))
        if not on: continue
        best = (difflib.SequenceMatcher(None, nn[:6], on[:6]).ratio(), "6 chữ đầu", " ".join(on[:6]))
        for a in _sents(new):
            for b in _sents(old):
                na, nb = norm(a), norm(b)
                if len(na) < L088_MIN_TOK or len(nb) < L088_MIN_TOK: continue
                r = difflib.SequenceMatcher(None, na, nb).ratio()
                if r > best[0]: best = (r, f"câu «{a[:50]}»", b)
        if best[0] > L088_SIM: hits.append((lab, best[1], best[0], best[2]))
    return hits

def opener_reuse(new, olds, k=2, n=2):
    """→ [nhãn] khi k chữ đầu của `new` trùng k chữ đầu của ≥ n text cũ (vd CTA «Còn bạn, …» lần thứ 3)."""
    o = norm(_l088_clean(new))[:k]
    if len(o) < k: return []
    labs = [lab for lab, old in olds if norm(_l088_clean(old))[:k] == o]
    return labs if len(labs) >= n else []

def _spec_beats(spec): return [x for p in spec.get("parts", []) for x in p.get("scenes", []) + p.get("sections", [])]

def _spec_sel(spec, ids):
    ids = set(ids or []); return [x for x in _spec_beats(spec) if x["id"] in ids or x.get("beat", "").split(".")[-1] in ids]

def spec_hook_cta(spec):
    """(hook text, CTA text) đọc từ spec: structure.hook / hook.scenes; structure.cta → beat part=='cta' → beat cuối."""
    st = spec.get("structure") or {}; bs = _spec_beats(spec)
    hk = _spec_sel(spec, st.get("hook") or (spec.get("hook") or {}).get("scenes")) or bs[:1]
    ct = _spec_sel(spec, st.get("cta")) or [x for x in bs if x.get("part") == "cta"] or bs[-1:]
    j = lambda xs: " ".join(l.get("text", "") for x in xs for l in x.get("lines", []))
    return j(hk), j(ct)

def draft_parts(md):
    """Bản nháp script (.md, khung «N. **[Nhãn]** lời»): → (hook, cta, toàn bộ lời đọc). Hook = mục có nhãn «Hook» (không có thì mục 1);
    CTA = mục có nhãn «CTA» (không có thì mục cuối). Lời đọc = các mục đánh số + gạch đầu dòng con, dừng ở «**End card» hoặc heading «## »."""
    items = []; spoken = []; inside = False
    for ln in md.splitlines():
        m = re.match(r"^\s*(\d+)\.\s*\*\*\[([^\]]+)\]\*\*\s*(.*)$", ln)
        if m: items.append((m.group(2), m.group(3))); spoken.append(m.group(3)); inside = True; continue
        if inside and (ln.startswith("## ") or ln.lstrip().startswith("**End card")): inside = False
        if inside and re.match(r"^\s+[-*]\s+", ln): spoken.append(re.sub(r"^\s+[-*]\s+(\*\*[^*]+\*\*\s*)?", "", ln))
    if not items: return "", "", ""
    hk = next((t for lab, t in items if re.search(r"hook", lab, re.I)), items[0][1])
    ct = next((t for lab, t in items if re.search(r"\bcta\b", lab, re.I)), items[-1][1])
    return hk, ct, " ".join(spoken)

def _clip_no(path):
    m = re.search(r"clip-(\d+)", path or ""); return int(m.group(1)) if m else None

def previous_hooks_ctas(cur_clip_no, exclude_file=None, same_clip_ok=False):
    """Hook/CTA đã khoá của các clip trước (spec.json trong content/clips + content/archive; thêm script-v*-LOCKED.md).
    same_clip_ok=True (soi bản nháp): lấy cả spec/bản LOCKED cũ của chính clip đó (bản làm lại không được bê nguyên hook cũ)."""
    hooks, ctas, seen = [], [], set()
    for f in sorted(glob.glob(os.path.join(REPO, "content/clips/*/final/spec.json")) + glob.glob(os.path.join(REPO, "content/archive/*/final/spec.json"))):
        n = _clip_no(f)
        if n is None or (cur_clip_no is not None and (n > cur_clip_no or (n == cur_clip_no and not same_clip_ok))): continue
        try: h, c = spec_hook_cta(json.load(open(f, encoding="utf8")))
        except Exception: continue
        lab = f"clip-{n:02d}" + (" (bản cũ cùng clip)" if n == cur_clip_no else "")
        for lst, t in ((hooks, h), (ctas, c)):
            key = (lab, tuple(norm(t)[:12]))
            if t.strip() and key not in seen: seen.add(key); lst.append((lab, t))
    for f in sorted(glob.glob(os.path.join(REPO, "content/clips/*/*-LOCKED.md")) + glob.glob(os.path.join(REPO, "content/clips/*/final/*-LOCKED.md")) + glob.glob(os.path.join(REPO, "content/archive/*/*-LOCKED.md"))):
        n = _clip_no(f)
        if n is None or (exclude_file and os.path.abspath(f) == os.path.abspath(exclude_file)): continue
        if cur_clip_no is not None and (n > cur_clip_no or (n == cur_clip_no and not same_clip_ok)): continue
        h, c, _ = draft_parts(open(f, encoding="utf8").read())
        lab = f"clip-{n:02d} {os.path.basename(f)}"
        for lst, t in ((hooks, h), (ctas, c)):
            if t.strip() and not any(norm(_l088_clean(t)) == norm(_l088_clean(o)) for _, o in lst): lst.append((lab, t))
    return hooks, ctas

def _l088_novelty(hook, cta, cur_clip_no, exclude_file=None, same_clip_ok=False):
    ph, pc = previous_hooks_ctas(cur_clip_no, exclude_file, same_clip_ok)
    for what, new, olds in (("hook", hook, ph), ("CTA", cta, pc)):
        if not new.strip(): warn("L-088", f"không tìm thấy {what} để so"); continue
        sim = similar_to(new, olds); op = opener_reuse(new, olds)
        if sim: warn("L-088", f"{what} rập khuôn, giống {what} clip trước: " + "; ".join(f"{lab} ({how} ≈ «{old[:60]}» {r:.2f})" for lab, how, r, old in sim))
        if op: warn("L-088", f"{what} mở bằng «{' '.join(_l088_clean(new).split()[:2])}» như {len(op)} clip trước ({', '.join(op)}) → đổi cách mở")
        if not sim and not op: ok("L-088", f"{what} không trùng mẫu {len(olds)} {what} clip trước (ngưỡng {L088_SIM})")

def _l088_evidence(cites, spoken, cur_clip_no, where):
    (ok if cites else err)("L-088", f"có nguồn truy được ({where}): " + ", ".join(sorted(set(cites))[:6]) if cites else f"không có nguồn truy được (tác giả + năm / PMID / doi) trong {where} → clip phải có dẫn chứng")
    sur = {w for c in cites for w in re.findall(r"[A-Z][a-z'\-]{2,}", c) if w not in ("PMID",)}
    sp = _l088_clean(spoken)
    said = re.search(L088_EVID_SPOKEN, sp, re.I) or any(re.search(rf"(?<!\w){re.escape(s)}(?!\w)", sp) for s in sur)
    e = err if (cur_clip_no or 0) >= 6 else warn
    (ok if said else e)("L-088", "lời đọc có nói dẫn chứng (nghiên cứu / tên tác giả)" if said else "lời đọc không nhắc dẫn chứng nào — nguồn chỉ nằm ở end card/fact lock; dẫn chứng phải có trong clip")
    dry = sorted({m.group(0).lower() for m in re.finditer(L088_DRY, sp, re.I)})
    if dry: warn("L-088", "dẫn chứng mở kiểu chèn trích dẫn: " + ", ".join(f"«{d}»" for d in dry) + " → soát tay liền mạch: lồng nghiên cứu vào việc nhân vật đang làm / trả lời câu hỏi hook")

def _l088_trend(clip_dir):
    """L-088 (1) (Hiệp 21:47 qua News): clip có file trend của Social Research có link nguồn — final/trend-signals.md (hoặc ở gốc clip)
    hoặc research/trends/<ngày>/clip-NN-*trend*.md. Thiếu: ✖ từ clip-06, ⚠ clip ≤05."""
    n = _clip_no(clip_dir); e = err if (n or 0) >= 6 else warn
    cands = [p for p in (os.path.join(clip_dir, "final", "trend-signals.md"), os.path.join(clip_dir, "trend-signals.md")) if os.path.exists(p)]
    if n is not None: cands += sorted(glob.glob(os.path.join(REPO, f"research/trends/*/clip-{n:02d}-*trend*.md")))
    linked = [p for p in cands if re.search(r"https?://\S+", open(p, encoding="utf8").read())]
    if linked: ok("L-088", "file trend (Social Research) có link nguồn: " + ", ".join(os.path.relpath(p, REPO) for p in linked))
    elif cands: e("L-088", "file trend không có link nguồn: " + ", ".join(os.path.relpath(p, REPO) for p in cands))
    else: e("L-088", f"chưa có file trend của Social Research cho clip (final/trend-signals.md hoặc research/trends/<ngày>/clip-{(n or 0):02d}-*trend*.md, có link nguồn)")

def _l088_facts(clip_dir, extra=()):
    """L-088 (2) (Hiệp 21:47 qua News): clip có ràng buộc/kiểm fact của Deep Research — fact-package*/fact-check* trong thư mục clip
    (gốc hoặc final/), research/fact-packages/*clip-NN*, hoặc file mà `fact_lock:` của bản nháp trỏ tới. Thiếu: ✖ từ clip-06, ⚠ ≤05."""
    n = _clip_no(clip_dir); e = err if (n or 0) >= 6 else warn
    fs = []
    for d in (clip_dir, os.path.join(clip_dir, "final")):
        for pat in ("fact-package*.md", "fact-check*.md", "*fact-lock*.md", "dr-*.md"): fs += glob.glob(os.path.join(d, pat))
    if n is not None: fs += glob.glob(os.path.join(REPO, f"research/fact-packages/*clip-{n:02d}*.md"))
    fs += [p for p in extra if os.path.exists(p)]
    fs = sorted(set(os.path.abspath(p) for p in fs))
    (ok if fs else e)("L-088", ("ràng buộc/kiểm fact Deep Research: " + ", ".join(os.path.relpath(p, REPO) for p in fs)) if fs else
        "chưa có file ràng buộc/kiểm fact của Deep Research cho clip (fact-package*.md / fact-check*.md trong thư mục clip hoặc research/fact-packages/*clip-NN*)")

L088_MANUAL = ("manual gate: (a) liền mạch: dẫn chứng là một bước trong chuyện, không phải khối «nghiên cứu nói…»; (b) sáng tạo: kiểu hook khác 2 clip trước, "
               "chuyển ý tự nhiên trong khung W-16; (c) trend chỉ là cái móc, thông điệp bám trục kênh: truyền cảm hứng, motivation, sống tốt hơn mỗi ngày +1")

def check_l088(spec, L, fdir, clip_dir):
    n = _clip_no(clip_dir)
    sf = os.path.join(fdir, "script-final.md"); stx = open(sf, encoding="utf8").read() if os.path.exists(sf) else ""
    cites = citations(stx) + citations(json.dumps(spec, ensure_ascii=False))
    _l088_evidence(cites, " ".join((l.get("text") or "") for _, _, l in L), n, "script-final.md + spec")
    hook, cta = spec_hook_cta(spec); _l088_novelty(hook, cta, n)
    _l088_trend(clip_dir); _l088_facts(clip_dir)
    info("L-088", L088_MANUAL)

def check_l088_file(path):  # --l088 FILE: soi bản nháp script trước khi có spec
    md = open(path, encoding="utf8").read(); n = _clip_no(os.path.abspath(path))
    hook, cta, spoken = draft_parts(md)
    if not spoken: err("L-088", f"{os.path.basename(path)}: không đọc được lời theo beat (khung «N. **[Nhãn]** lời»)"); return
    _l088_evidence(citations(md), spoken, n, os.path.basename(path))
    _l088_novelty(hook, cta, n, exclude_file=path, same_clip_ok=not path.endswith("-LOCKED.md"))  # bản đã khoá không so với spec của chính nó
    m = re.search(r"content/(?:clips|archive)/[^/]+", os.path.abspath(path).replace(os.sep, "/"))
    fl = [os.path.join(REPO, x.strip()) for x in re.findall(r"(?m)^fact_lock:\s*(\S+\.md)", md)]  # frontmatter fact_lock: <path> (…)
    if m: cd = os.path.join(REPO, m.group(0)); _l088_trend(cd); _l088_facts(cd, fl)
    else: warn("L-088", "bản nháp không nằm trong thư mục clip → không tìm được file trend / fact của clip")
    info("L-088", L088_MANUAL)

# ---- L-089 (Hiệp 27/10 02:37 «Xàm quá… đọc k thấy nó rời rạc à»): --flow <draft.md> — cờ hỗ trợ cổng đọc to liền mạch (chỉ ⚠, quyết định cuối manual)
L089_CONN = ("vì", "tại vì", "bởi vì", "nên", "cho nên", "thế nên", "vậy", "vậy nên", "vậy là", "thế là", "mà", "nhưng", "còn", "rồi", "xong",
             "hóa ra", "hoá ra", "thì ra", "giống", "cũng", "chính vì", "nhờ", "từ đó", "sau đó", "bởi vậy", "ủa", "mà khoan", "tức là", "nghĩa là", "đó là", "kết quả")
L089_REF = r"(?<!\w)(đó|ấy|vậy|thế|y chang|cũng)(?!\w)"
L089_STOP = set("mình bạn họ thì là mà và với của cho có không được một các những này đó rồi cũng nha nè á thôi luôn lại ra vào lên xuống".split())
L089_MAXIM = r"(?<!\w)(chỉ cần|mỗi ngày một|mỗi ngày mình|nhích|một chút|từng chút|\+1|sống tốt hơn)(?!\w)"
L089_MANUAL = ("manual gate (làm TRƯỚC khi chấm luật): đọc to b01→CTA một mạch như người nói chuyện — một ngôi kể xuyên suốt, mỗi beat mở bằng mối nối "
               "với beat trước, không câu mồ côi/gắn thêm, dẫn chứng nảy ra từ chuyện, không đổi liền mạch lấy số chữ (bỏ ý chứ không ép câu)")

def _l089_tok(t): return re.findall(r"[\wÀ-ỹ]+", t.lower())
def _l089_sents(t): return [x.strip() for x in re.split(r"(?<=[.?!…])\s+", re.sub(r"\{[^}:]*:\s*([^}]*)\}", r"\1", t).replace("**", "")) if x.strip()]
def _l089_starts_conn(sent):  # từ nối trong 3 chữ đầu («Có thể vì…», «Mà…», «Vậy nên…»)
    tw = _l089_tok(sent)[:4]
    return any(" ".join(tw[k:k + len(c.split())]) == c for c in L089_CONN for k in range(0, min(3, len(tw))))
def _l089_person(t):
    tw = _l089_tok(t); b = tw.count("bạn")
    m = sum(1 for i, w in enumerate(tw) if w == "mình" and not (i and tw[i - 1] in ("kể", "cho", "với", "giúp", "hỏi", "nhắn", "chỉ")))
    return "bạn" if b > m else "mình" if m > b else ("lẫn" if b else "-")
def _l089_bigrams(t):
    tw = [w for w in _l089_tok(t)]; return {(a, b) for a, b in zip(tw, tw[1:]) if a not in L089_STOP or b not in L089_STOP}

def draft_beats(md):
    items = []
    for ln in md.splitlines():
        m = re.match(r"^\s*(\d+)\.\s*\*\*\[([^\]]+)\]\*\*\s*(.*)$", ln)
        if m: items.append((int(m.group(1)), m.group(2), m.group(3)))
        elif ln.startswith("## ") and items: break
    return items

def check_flow_beats(items, where="draft"):
    if not items: err("L-089", f"{where}: không đọc được lời theo beat (khung «N. **[Nhãn]** lời»)"); return
    n = len(items)
    hk = next((i for i, (_, lab, _) in enumerate(items) if re.search(r"hook", lab, re.I)), 0)
    ct = next((i for i, (_, lab, _) in enumerate(items) if re.search(r"\bcta\b", lab, re.I)), n - 1)
    pers = [_l089_person(t) for _, _, t in items]
    # (1) ngôi kể
    narr = {pers[i] for i in range(n) if i not in (hk, ct) and pers[i] in ("bạn", "mình")}
    seq = [p for p in pers if p in ("bạn", "mình")]; sw = sum(1 for a, b in zip(seq, seq[1:]) if a != b)
    shown = " → ".join(f"b{i+1:02d} {p}" for i, p in enumerate(pers))
    if len(narr) > 1: warn("L-089", f"đổi ngôi kể giữa các beat thân bài ({shown}) → một người kể xuyên suốt")
    elif sw >= 2: warn("L-089", f"ngôi kể đổi qua lại {sw} lần ({shown}) → hook/CTA chỉ gọi «bạn» khi khung chuyện tự nhiên, soát tay")
    elif sw == 1: info("L-089", f"ngôi kể đổi 1 lần ({shown}) → soát tay khung chuyện")
    else: ok("L-089", f"ngôi kể nhất quán ({shown})")
    # (2) khâu lặp kiểu «X, mà càng X»
    stitched = []
    for i, (_, _, t) in enumerate(items):
        for s_ in _l089_sents(t):
            m = re.search(r"((?:[\wÀ-ỹ]+\s+){1,3}[\wÀ-ỹ]+)\s*,?\s*(?:mà|thì|nên|là)\s+(?:càng\s+)?\1(?![\wÀ-ỹ])", s_, re.I)
            tw = _l089_tok(s_); tri = [tuple(tw[k:k + 3]) for k in range(len(tw) - 2)]
            dup = next((g for k, g in enumerate(tri) if g in tri[k + 1:k + 11]), None)
            if m or dup: stitched.append(f"b{i+1:02d} «{(m.group(0) if m else ' '.join(dup))}»")
    (warn if stitched else ok)("L-089", ("khâu câu bằng cụm lặp: " + "; ".join(stitched) + " → nối bằng ý, không lặp chữ để gượng nối") if stitched else "không có cụm lặp khâu câu")
    # (3) mở beat không có mối nối / tham chiếu beat trước
    cold = []
    for i in range(1, n):
        if i in (hk, ct): continue  # CTA: mối nối kiểm ở rule-56 (loop) + đọc to
        ss = _l089_sents(items[i][2]);
        if not ss: continue
        first = ss[0]; prev = _l089_sents(items[i - 1][2]); prev_last = prev[-1] if prev else ""
        head = " ".join(_l089_tok(first)[:8])
        linked = _l089_starts_conn(first) or re.search(L089_REF, head) or (_l089_bigrams(first) & _l089_bigrams(prev_last))
        if not linked: cold.append(f"b{i+1:02d} «{' '.join(first.split()[:6])}…»")
    (warn if cold else ok)("L-089", ("beat mở không nối với beat trước: " + "; ".join(cold) + " → mở bằng từ nối/chữ gọi lại ý vừa nói") if cold else "beat nào cũng mở bằng mối nối với beat trước")
    # (4) liệt kê song song (đọc như danh sách) + câu chốt gắn thêm
    lists, tacked = [], []
    for i, (_, _, t) in enumerate(items):
        ss = _l089_sents(t); heads = []
        for s_ in ss:
            tw = _l089_tok(s_)
            while tw and tw[0] in ("còn", "nhưng", "mà", "rồi", "và"): tw = tw[1:]
            heads.append(tuple(tw[:2]))
        dup = {h for h in heads if len(h) == 2 and heads.count(h) >= 2}
        if dup: lists.append(f"b{i+1:02d} ({', '.join('«' + ' '.join(h) + '…»' for h in dup)})")
        if i not in (hk, ct) and len(ss) >= 2 and not _l089_starts_conn(ss[-1]) and re.search(L089_MAXIM, ss[-1].lower()) and len(_l089_tok(ss[-1])) <= 12:
            tacked.append(f"b{i+1:02d} «{ss[-1]}»")
    (warn if lists else ok)("L-089", ("câu cùng mở bằng một cụm, đọc như danh sách: " + "; ".join(lists) + " → kể thành chuyện, không liệt kê nhóm") if lists else "không có đoạn liệt kê song song")
    (warn if tacked else ok)("L-089", ("câu chốt/motivation đứng trơ cuối beat: " + "; ".join(tacked) + " → nối vào ý trước hoặc bỏ") if tacked else "không có câu chốt gắn thêm")
    info("L-089", L089_MANUAL)

def check_flow_file(path):  # --flow FILE: cờ liền mạch cho bản nháp (L-089)
    check_flow_beats(draft_beats(open(path, encoding="utf8").read()), os.path.basename(path))

# ---- L-091 (Hiệp 29/10 11:51 «Trong 3 ý đầu hơi lòng vòng chưa rõ nghĩa và khó hiểu»): --clarity <draft.md> — cờ hỗ trợ cổng «nghe một lần là hiểu» (chỉ ⚠)
L091_CUES = ("hỏi", "kể lại", "gặp")  # cảnh nỗi đau cụ thể; «đọc» quá rộng (bb480a6 bỏ sót r6.5)
L091_VAGUE = ("trôi", "bay màu", "chắc được", "cũng thấy vậy", "lòng vòng")
L091_MANUAL = "manual gate: đọc b01–b03 như người lần đầu nghe, tóm ý trong 1 câu; không được → CHƯA ĐẠT"
def _l091_has(text, phrase): return re.search(r"(?<![\wÀ-ỹ])" + re.escape(phrase) + r"(?![\wÀ-ỹ])", text.lower()) is not None
def check_clarity_beats(items, where="draft"):
    if not items: err("L-091", f"{where}: không đọc được lời theo beat (khung «N. **[Nhãn]** lời»)"); return
    head = items[:3]
    # (1) câu hỏi trước câu tình huống đầu tiên
    q = sit = None
    for i, (_, _, t) in enumerate(head):
        for k, s_ in enumerate(_l089_sents(t)):
            isq = s_.rstrip().endswith("?")
            if isq and q is None: q = (i, k, s_)
            if not isq and sit is None and any(_l091_has(s_, c) for c in L091_CUES): sit = (i, k, s_)
    if q and (sit is None or q[:2] < sit[:2]):
        warn("L-091", f"câu hỏi b{q[0]+1:02d} «{q[2]}» đến trước câu tình huống cụ thể" + (f" (b{sit[0]+1:02d} «{' '.join(sit[2].split()[:6])}…»)" if sit else " (b01–b03 không có câu tình huống)") + " → tình huống → câu hỏi → trả lời")
    else: ok("L-091", "tình huống cụ thể đến trước câu hỏi (b01–b03)")
    # (2) câu > 25 chữ (cả bài)
    longs = [f"b{i+1:02d} ({len(_l089_tok(s_))} chữ) «{' '.join(s_.split()[:6])}…»" for i, (_, _, t) in enumerate(items) for s_ in _l089_sents(t) if len(_l089_tok(s_)) > 25]
    (warn if longs else ok)("L-091", ("câu dài >25 chữ: " + "; ".join(longs) + " → mỗi câu một ý") if longs else "không câu nào >25 chữ")
    # (3) chữ mơ hồ trong lời b01–b03
    vague = [f"b{i+1:02d} «{w}»" for i, (_, _, t) in enumerate(head) for w in L091_VAGUE if _l091_has(_l088_clean(t), w)]
    (warn if vague else ok)("L-091", ("chữ mơ hồ thay nghĩa thẳng: " + "; ".join(vague) + " → nói thẳng (vd «trôi» → «quên»)") if vague else "không chữ mơ hồ trong b01–b03")
    # (4) b03 mở bằng câu khái quát rồi «cũng thấy vậy»
    if len(items) >= 3:
        ss = _l089_sents(items[2][2]); hit = next((k for k, s_ in enumerate(ss) if _l091_has(s_, "cũng thấy vậy")), None)
        if hit is not None and hit >= 1:
            warn("L-091", f"b03 mở bằng câu khái quát «{ss[0]}» rồi «{ss[hit]}» → nói thẳng một phép so sánh (làm A thì…, làm B thì…)")
        else: ok("L-091", "b03 không mở bằng câu khái quát + «cũng thấy vậy»")
    info("L-091", L091_MANUAL)

def check_clarity_file(path):  # --clarity FILE (L-091)
    check_clarity_beats(draft_beats(open(path, encoding="utf8").read()), os.path.basename(path))

# ---- L-093 (Hiệp 29/10 14:00 «Các câu nói chưa có chiều sâu còn lủng củng lặp từ quá nhiều»): --repeat <draft.md> — lặp từ/cụm, từ nối lặp
L093_STOP = set("bạn mình và thì là mà có không được một hai rồi cho của với trong khi lại vẫn còn những các này đó nha nghe cũng đã sẽ đang ra vào lên để như hơn sau trước".split())
L093_CONNECT = ("nhưng", "rồi", "còn", "mà", "và", "vậy")
L093_MANUAL = ("manual gate: (a) chiều sâu — mỗi beat cho người xem một điều mới (vì sao/cảm giác/hệ quả cụ thể), không nói lại ý cũ bằng chữ khác; "
               "(b) đọc to nghe trơn, không câu cụt nối bằng «Nhưng/Và/Rồi» liên tiếp; (c) thay từ lặp bằng đại từ/chữ khác hoặc bỏ hẳn")
def check_repeat_beats(items, where="draft"):
    if not items: err("L-093", f"{where}: không đọc được lời theo beat"); return
    sents = [s_ for _, _, t in items for s_ in _l089_sents(t)]
    toks = [w for s_ in sents for w in _l089_tok(s_)]
    n = max(len(toks), 1)
    from collections import Counter
    c = Counter(w for w in toks if w not in L093_STOP and len(w) > 1)
    heavy = [(w, k) for w, k in c.most_common() if k / n > 0.05 and k >= 5]
    (err if heavy else ok)("L-093", ("từ lặp dày (>5% lời): " + ", ".join(f"«{w}» ×{k}" for w, k in heavy) + " → thay chữ/đại từ hoặc bỏ ý") if heavy else "không từ nội dung nào lặp >5% lời")
    tri = Counter(" ".join(t_[i:i+3]) for t_ in (_l089_tok(s_) for s_ in sents) for i in range(len(t_) - 2))  # per sentence, no cross-boundary trigrams
    rep = [(g, k) for g, k in tri.items() if k >= 2 and not set(g.split()) <= L093_STOP]
    (warn if rep else ok)("L-093", ("cụm 3 chữ lặp: " + "; ".join(f"«{g}» ×{k}" for g, k in rep[:8])) if rep else "không cụm 3 chữ nào lặp")
    opens = Counter(_l089_tok(s_)[0] for s_ in sents if _l089_tok(s_) and _l089_tok(s_)[0] in L093_CONNECT)
    many = [(w, k) for w, k in opens.items() if k >= 3]
    (warn if many else ok)("L-093", ("câu mở bằng cùng từ nối: " + ", ".join(f"«{w}» ×{k}" for w, k in many) + " → câu cụt nối nhau, lủng củng") if many else "từ nối mở câu không lặp ≥3")
    info("L-093", L093_MANUAL)

def check_repeat_file(path):  # --repeat FILE (L-093)
    check_repeat_beats(draft_beats(open(path, encoding="utf8").read()), os.path.basename(path))

# ---- L-095 (Hiệp 30/10 18:00 «Tệ quá làm lại từ đầu toàn bộ script với sáng tạo hơn»): --fresh <draft.md> [--against f.md…] — bản mới không được giữ hook/khung của bản bị bác cùng clip
L095_LIMIT = 0.5
L095_MANUAL = ("manual gate (chặn): 3 ý tưởng một dòng trước khi viết lời; review ghi vì sao ý được chọn khác bản bị bác; "
               "người xem có dừng lướt ở 3 giây đầu không, có hình ảnh/khoảnh khắc đáng nhớ không")
def _l095_words(t):
    return [w for w in _l089_tok(" ".join(_l089_sents(t))) if len(w) > 1 and w not in L089_STOP and w not in L093_STOP]
def _l095_sim(a, b):
    from difflib import SequenceMatcher
    sa, sb = set(a), set(b)
    jac = len(sa & sb) / max(len(sa | sb), 1)
    return max(jac, SequenceMatcher(None, a, b, autojunk=False).ratio())
def _l095_scores(new, old):
    hook = _l095_sim(_l095_words(new[0][2]), _l095_words(old[0][2]))
    m = min(len(new), len(old))
    chain = sum(_l095_sim(_l095_words(new[i][2]), _l095_words(old[i][2])) for i in range(m)) / max(len(new), len(old), 1)
    return hook, chain
def _l095_rejected(path, extra):
    import subprocess, glob
    d = os.path.dirname(os.path.abspath(path)); me = os.path.abspath(path); out = []
    files = [f for f in sorted(glob.glob(os.path.join(d, "script-v*.md"))) if os.path.abspath(f) != me]
    for f in files:
        out.append((os.path.basename(f), open(f, encoding="utf8").read()))
        try:
            shas = subprocess.run(["git", "log", "--format=%h", "--", f], cwd=d, capture_output=True, text=True).stdout.split()
            rel = subprocess.run(["git", "ls-files", "--full-name", f], cwd=d, capture_output=True, text=True).stdout.strip()
            for h in shas[1:]:
                r = subprocess.run(["git", "show", f"{h}:{rel}"], cwd=d, capture_output=True, text=True)
                if r.returncode == 0: out.append((f"{os.path.basename(f)}@{h}", r.stdout))
        except Exception: pass
    for f in extra: out.append((os.path.basename(f), open(f, encoding="utf8").read()))
    return out
def check_fresh_file(path, extra=()):
    new = draft_beats(open(path, encoding="utf8").read())
    if not new: err("L-095", f"{os.path.basename(path)}: không đọc được lời theo beat"); return
    rows = []
    for name, md in _l095_rejected(path, extra):
        old = draft_beats(md)
        if old: rows.append((name,) + _l095_scores(new, old))
    if not rows: warn("L-095", "không tìm thấy bản cũ cùng clip để so"); return
    bh = max(rows, key=lambda r: r[1]); bc = max(rows, key=lambda r: r[2])
    (err if bh[1] >= L095_LIMIT else ok)("L-095", f"hook giống nhất {bh[1]:.2f} với {bh[0]} (ngưỡng {L095_LIMIT}, so {len(rows)} bản)" + (" → đổi hook/tình huống mở" if bh[1] >= L095_LIMIT else ""))
    (err if bc[2] >= L095_LIMIT else ok)("L-095", f"chuỗi beat giống nhất {bc[2]:.2f} với {bc[0]}" + (" → đổi khung dẫn dắt, không chỉ đổi chữ" if bc[2] >= L095_LIMIT else ""))
    info("L-095", L095_MANUAL)

# ---- L-094 (Rule Reviewer 29/10 15:14, Hiệp «Quá lộn xộn các câu thiếu liên kết»): --link <draft.md> — cặp câu liền nhau không có mối nối (chỉ ⚠, cổng tay chặn)
L094_REF = r"(?<!\w)(đó|ấy|vậy|thế|này|nó|họ|y chang|cũng|lúc đó|khi đó|chuyện này|điều này|cách này)(?!\w)"
L094_MANUAL = ("manual gate (chặn): bảng cặp câu trong review — câu N+1 trả lời/giải thích/đối chiếu/hệ quả của câu N nhờ chữ nào; "
               "không đưa nhân vật/nhóm/mốc/hành động chưa nhắc; câu hỏi hook được trả lời ngay sau; lời khuyên dùng đúng mốc của dẫn chứng")
def _l094_content(sent):
    return {w for w in _l089_tok(sent) if len(w) > 1 and w not in L089_STOP and w not in L093_STOP}
def check_link_beats(items, where="draft"):
    if not items: err("L-094", f"{where}: không đọc được lời theo beat"); return
    seq = [(i + 1, s_) for i, (_, _, t) in enumerate(items) for s_ in _l089_sents(t)]
    loose = []
    for (ba, a), (bb, b) in zip(seq, seq[1:]):
        head = " ".join(_l089_tok(b)[:6])
        if _l094_content(a) & _l094_content(b) or _l089_starts_conn(b) or re.search(L094_REF, head): continue
        loose.append(f"b{ba:02d}→b{bb:02d} «{' '.join(a.split()[-5:])}» | «{' '.join(b.split()[:6])}…»")
    (warn if loose else ok)("L-094", (f"{len(loose)}/{max(len(seq)-1,1)} cặp câu không chung từ nội dung, không từ nối/đại từ gọi lại: " + "; ".join(loose) + " → viết câu nối hoặc gọi lại ý câu trước")
                            if loose else f"{len(seq)-1} cặp câu liền nhau đều có từ chung, từ nối hoặc đại từ gọi lại")
    info("L-094", L094_MANUAL)

def check_link_file(path):  # --link FILE (L-094)
    check_link_beats(draft_beats(open(path, encoding="utf8").read()), os.path.basename(path))

# ---- L-090 (Hiệp 28/10 23:46 + 23:48): --trend <draft.md> — trend phải nằm trong LỜI hook theo nghiên cứu trend đã lưu, không chỉ ở end card/hình
L090_MANUAL = ("manual gate: (1) đối chiếu hook/format với research/trends/patterns.md (P/F active) + digest 3 ngày gần nhất + file trend của clip; "
               "(2) ví dụ chính phải là nỗi đau người xem kênh thật sự có (bằng chứng comment/trend), minh hoạ ĐÚNG điểm cốt lõi của nguồn, "
               "và lời khuyên làm được trong chính tình huống đó; ví dụ gượng/hiếm gặp → CHƯA ĐẠT dù luật khác đạt")
def _l090_norm(s): return " ".join(re.findall(r"[\wÀ-ỹ]+", (s or "").lower()))
def _frontmatter(md):
    m = re.match(r"^---\n(.*?)\n---", md, re.S); fm = {}
    for ln in (m.group(1).splitlines() if m else []):
        k = re.match(r"^([A-Za-z_]+):\s*(.*)$", ln)
        if k: fm[k.group(1)] = k.group(2).strip()
    return fm
def check_trend_file(path):  # --trend FILE
    md = open(path, encoding="utf8").read(); fm = _frontmatter(md); where = os.path.basename(path)
    items = draft_beats(md)
    if not items: err("L-090", f"{where}: không đọc được lời theo beat"); return
    hook_spoken = _l090_norm(" ".join(t for _, _, t in items[:2])); spoken = _l090_norm(" ".join(t for _, _, t in items))
    tdir = os.path.join(REPO, "research", "trends")
    days = sorted(d for d in os.listdir(tdir) if re.match(r"\d{4}-\d{2}-\d{2}$", d))
    corpus = {}
    for f in [os.path.join(tdir, "ingest.md")] + glob.glob(os.path.join(tdir, "*", "digest.md")) + glob.glob(os.path.join(tdir, "*", "*trend*.md")):
        if os.path.exists(f): corpus[f] = open(f, encoding="utf8").read()
    pat = open(os.path.join(tdir, "patterns.md"), encoding="utf8").read()
    tid = fm.get("trend_id", "").split()[0] if fm.get("trend_id") else ""
    if not tid: err("L-090", f"{where}: thiếu `trend_id:` (id bridge B-… / id trend trong research/trends/ingest.md hoặc digest) → script không khai trend nào từ nghiên cứu đã lưu")
    else:
        hits = sorted(f for f, t in corpus.items() if tid in t)
        (ok if hits else err)("L-090", f"trend_id {tid} " + (f"có trong {len(hits)} file trend đã lưu (mới nhất {os.path.relpath(hits[-1], REPO)})" if hits else "không có trong research/trends/** → không phải trend đã nghiên cứu"))
        seen_days = [d for d in days if any(tid in corpus.get(os.path.join(tdir, d, x), "") for x in ("digest.md",))]
        import datetime as _dt
        if seen_days and (_dt.date.today() - _dt.date.fromisoformat(seen_days[-1])).days > 7:
            warn("L-090", f"trend {tid} thấy lần cuối {seen_days[-1]} (>7 ngày) → không còn nóng, hỏi Social Research trend mới")
    hp = re.findall(r"\b([PF]\d{2})\b", fm.get("hook_pattern", ""))
    if not hp: err("L-090", f"{where}: thiếu `hook_pattern:` (id P../F.. trong research/trends/patterns.md) → hook không theo khuôn trend đã nghiên cứu")
    for p in hp:
        row = re.search(rf"(?m)^\| {p} \|.*$", pat)
        if not row: err("L-090", f"hook_pattern {p} không có trong patterns.md")
        elif "| tired |" in row.group(0): err("L-090", f"hook_pattern {p} đã «tired» → đổi khuôn")
        else: ok("L-090", f"hook_pattern {p} active trong patterns.md")
    tb = re.findall(r"b\d{2}", fm.get("trend_beats", ""))
    if not tb: err("L-090", "thiếu `trend_beats:` (beat nào dùng trend, phải có b01 hoặc b02)")
    elif not set(tb) & {"b01", "b02"}: err("L-090", f"trend_beats {', '.join(tb)} không có b01/b02 → trend không nằm ở hook (L-084)")
    else: ok("L-090", f"trend_beats {', '.join(tb)}")
    ts = _l090_norm(fm.get("trend_spoken", "").strip("\"'«»"))
    if not ts: err("L-090", "thiếu `trend_spoken:` (cụm/khoảnh khắc trend NÓI THÀNH LỜI ở b01–b02)")
    else: (ok if ts in hook_spoken else err)("L-090", f"trend_spoken «{ts}» " + ("có trong lời b01–b02" if ts in hook_spoken else "KHÔNG có trong lời b01–b02 → trend chỉ ở hình/end card"))
    name = _l090_norm(re.split(r"[(\[—]", fm.get("trend", ""))[0])
    if name:
        rest = md[md.find(items[-1][2]) + len(items[-1][2]):] if items else md
        if name not in spoken and _l090_norm(rest).find(name) >= 0:
            err("L-090", f"trend «{name}» chỉ xuất hiện ở end card/nguồn/ghi chú, không có trong lời → người xem không nghe/thấy trend")
        recent = days[-3:]; sat = []
        for d in recent:
            for ln in corpus.get(os.path.join(tdir, d, "digest.md"), "").splitlines():
                k = re.search(r"bão ho[àa]|saturat", ln, re.I)
                if k and name in _l090_norm(ln[k.start():]) or (name in _l090_norm(ln) and re.search(r"bão ho[àa]\)", ln, re.I)): sat.append(d); break
        for m_ in re.finditer(r"(?m)^- (\d{4}-\d{2}-\d{2})[^\n]*", pat):
            ln = m_.group(0)
            k = re.search(r"bão ho[àa] nên tránh|saturated", ln, re.I)
            if m_.group(1) in recent and k and name in _l090_norm(ln[k.start():].split(". ")[0]) and m_.group(1) not in sat: sat.append(m_.group(1))
        if sat: (warn if fm.get("trend_saturation_ok") else err)("L-090", f"trend «{name}» bị ghi bão hoà/nên tránh trong {', '.join(sorted(set(sat)))} → chọn trend khác" + (" (có trend_saturation_ok: Hiệp duyệt dùng kiểu lật)" if fm.get("trend_saturation_ok") else ""))
    ev = fm.get("example_evidence", "")
    if not ev: warn("L-090", "thiếu `example_evidence:` (link comment/trend/file chứng minh người xem kênh thật sự gặp tình huống ví dụ)")
    else:
        pth = ev.split()[0]
        (ok if pth.startswith("http") or os.path.exists(os.path.join(REPO, pth)) else warn)("L-090", f"example_evidence {pth}")
    info("L-090", L090_MANUAL)

def main():
    a = sys.argv[1:]
    outp = a[a.index("--out") + 1] if "--out" in a else None
    if a and a[0] == "--subjects":  # L-087 on draft script files
        for f in a[1:]:
            if f != "--out" and f != outp: check_subjects_file(f)
        return report(outp)
    if a and a[0] == "--l088":  # L-088 on draft script files (dẫn chứng + hook/CTA không rập khuôn + trend)
        for f in a[1:]:
            if f != "--out" and f != outp: check_l088_file(f)
        return report(outp)
    if a and a[0] == "--trend":  # L-090 on draft script files (trend từ nghiên cứu đã lưu phải nằm trong lời hook, không bão hoà, có hook_pattern)
        for f in a[1:]:
            if f != "--out" and f != outp: check_trend_file(f)
        return report(outp)
    if a and a[0] == "--fresh":  # L-095: bản làm lại phải khác hook/khung các bản bị bác cùng clip
        rest = [f for f in a[1:] if f not in ("--out", outp)]
        extra = rest[rest.index("--against") + 1:] if "--against" in rest else []
        for f in (rest[:rest.index("--against")] if "--against" in rest else rest): check_fresh_file(f, extra)
        return report(outp)
    if a and a[0] == "--link":  # L-094 on draft script files (cặp câu liền nhau có mối nối)
        for f in a[1:]:
            if f != "--out" and f != outp: check_link_file(f)
        return report(outp)
    if a and a[0] == "--repeat":  # L-093 on draft script files (lặp từ/cụm, từ nối mở câu)
        for f in a[1:]:
            if f != "--out" and f != outp: check_repeat_file(f)
        return report(outp)
    if a and a[0] == "--clarity":  # L-091 on draft script files (nghe một lần là hiểu: b01–b03)
        for f in a[1:]:
            if f != "--out" and f != outp: check_clarity_file(f)
        return report(outp)
    if a and a[0] == "--flow":  # L-089 on draft script files (đọc to liền mạch: ngôi kể, mối nối beat, cụm lặp khâu câu, liệt kê, câu gắn thêm)
        for f in a[1:]:
            if f != "--out" and f != outp: check_flow_file(f)
        return report(outp)
    clip_dir = os.path.abspath(a[0]); final = "--final" in a; do_stt = "--stt" in a
    specp = os.path.join(clip_dir, "final", "spec.json")
    if not os.path.exists(specp) and os.path.exists(os.path.join(clip_dir, "spec.json")): specp = os.path.join(clip_dir, "spec.json")  # samples
    if not os.path.exists(specp): err("rule-48", f"missing {os.path.relpath(specp, REPO)} (source of truth for the clip)"); return report(outp)
    if "/content/archive/" in os.path.abspath(specp).replace(os.sep, "/") + "/":
        print(f"skip: {specp} is archived (rule-66); check-assets verifies its post package"); sys.exit(0)
    if "--prosody" in a:  # L-070 only, on an explicit measure json (voice-only preview; no render/spec involved)
        pmp = a[a.index("--prosody") + 1]; pmp = pmp if os.path.exists(pmp) else os.path.join(clip_dir, pmp)
        check_prosody_file(os.path.abspath(pmp), os.path.dirname(specp))
        try: spec_ = json.load(open(specp))
        except Exception: spec_ = None
        voice_only_checks(os.path.abspath(pmp), os.path.dirname(specp), clip_dir, spec_, True); return report(outp)
    spec = json.load(open(specp)); fdir = os.path.dirname(specp)
    prof = {}
    for f in glob.glob(os.path.join(REPO, "video-engine/src/characters/profiles/*.json")):
        j = json.load(open(f)); prof[j["id"]] = j
    L = list(lines(spec))
    clip_no = int(re.findall(r"\d+", spec.get("clip", "clip-0"))[0])
    tm_week, tm_theme = theme_map(clip_no)

    # rule-4 / rule-9 length + pacing
    tpath = os.path.join(fdir, "timing.json")
    _en = {l.get("en") for _, _, l in L}
    def _fresh(tp):  # DL-062: timing from an older script version is stale → skip its audio checks
        if not (tp and os.path.exists(tp)): return False
        st_ = [x.get("en") for x in json.load(open(tp)).get("lines", []) if x.get("en") not in _en]
        if st_: warn("timing", f"{os.path.relpath(tp, REPO)} is stale ({len(st_)} lines not in current spec) → re-voice; audio checks skipped")
        return not st_
    LT = spec.get("length_target") or [55, 60.5]
    if not _fresh(tpath): tpath = None
    if tpath and os.path.exists(tpath):
        t = json.load(open(tpath)); total = t.get("total", 0)
        LX = spec.get("length_exception")  # DL-041: Hiệp-approved info-dense exception, ≤70s, flagged as warning
        (ok if LT[0] <= total <= LT[1] else (warn if total > LT[1] else err))("rule-4", f"planned length {total:.1f}s (target {LT[0]}–{LT[1]}s)" + (f" · exception {LX}" if LX and total > 60.5 else ""))
        bt = {}
        for l in t["lines"]: bt.setdefault(l["scene"], []).append(l)
        for sid, ls in bt.items():
            span = ls[-1]["local"] + ls[-1]["dur"] - ls[0]["local"]
            if span > 8.5: warn("rule-9", f"{sid}: voice spans {span:.1f}s in one shot (max ~8s per scene)")
    else:
        est = sum(len(l["text"].split()) for _, _, l in L) / 2.9
        (ok if LT[0] - 3 <= est <= LT[1] + 2 else warn)("rule-4", f"no fresh timing.json; estimated {est:.0f}s from word count (target {LT[0]}–{LT[1]}s)")
    words = sum(len((l.get("say") or l["text"]).split()) for _, _, l in L)
    WT = spec.get("word_target") or [140, 175]
    (ok if WT[0] <= words <= WT[1] else warn)("rule-7", f"{words} VI words (target {WT[0]}–{WT[1]})")
    # hook in 0-3s: first line starts < 1s and the first beat is tagged hook
    first = spec["parts"][0].get("scenes", spec["parts"][0].get("sections"))[0]
    (ok if first.get("part") == "hook" else warn)("rule-7", f"first beat {first['id']} part='{first.get('part')}' (hook expected in 0–3s)")
    last = spec["parts"][-1].get("scenes", spec["parts"][-1].get("sections"))[-1]
    (ok if last.get("part") == "cta" else warn)("rule-8", f"last beat {last['id']} part='{last.get('part')}' (CTA question expected)")
    if not any("?" in l["text"] or "comment" in l["text"].lower() for _, s, l in L if s.get("part") == "cta"): warn("rule-8", "CTA has no question / comment prompt")

    # rule-11 Omi week
    omi_used = any(l["speaker"] == "omi" for _, _, l in L) or any(c["id"] == "omi" for p in spec["parts"] for s in p.get("scenes", []) for c in s.get("cast", []))
    week = spec.get("week")
    if omi_used:
        if not week or week < 5: err("rule-11", f"Omi appears but spec week={week} (< 5)")
        elif tm_week and tm_week < 5: warn("rule-11", f"DEMO: Omi + week {week} in spec, but theme-map schedules clip {clip_no} in week {tm_week} → cannot post as-is in week {tm_week}")
        else: ok("rule-11", f"Omi allowed (week {week})")
    else: ok("rule-11", "no Omi")
    # rule-17 theme
    if tm_theme: (ok if spec.get("theme") == tm_theme else err)("rule-17", f"theme {spec.get('theme')} vs theme-map {tm_theme.upper()}")
    # beat ids
    for p in spec["parts"]:
        for s in p.get("scenes", []) + p.get("sections", []):
            if not re.fullmatch(rf"{spec['clip']}\.b\d\d", s.get("beat", "")): err("ids", f"{s['id']}: beat id '{s.get('beat')}' must be {spec['clip']}.bNN")
    # rule-42 engines
    for p in spec["parts"]:
        if p["engine"] == "remotion":
            for s in p["scenes"]:
                if s.get("mg"):  # clip-04 v18: evidence beat = HyperFrames motion-graphic plate (final/<mg>/index.html) composited under the Remotion caption layer
                    hp = os.path.join(fdir, s["mg"], "index.html"); pl = [x for x in s.get("props", []) if x.get("kind") == "plate"]
                    mp = os.path.join(REPO, "video-engine/public", pl[0]["src"]) if pl else ""
                    (ok if os.path.exists(hp) and pl and os.path.exists(mp) else err)("rule-42", f"{s['id']}: HyperFrames plate {s['mg']} → {pl[0]['src'] if pl else 'NO plate prop'}")
                elif s.get("part") in ("evidence",): warn("rule-42", f"{s['id']}: evidence beat in comic; should be motion graphics")
        elif p["engine"] != "hyperframes": err("rule-25", f"part {p['id']}: unknown engine {p['engine']}")
    # rule-16 / rule-1 captions EN, bubbles VI, no emoji
    for _, s, l in L:
        if not l.get("en"): err("rule-1", f"{s['id']}: line without EN caption")
        elif VI_CHARS.search(l["en"]): err("rule-16", f"{s['id']}: EN caption contains Vietnamese: “{l['en']}”")
        n = len(l.get("en", "").split())
        for h in l.get("hl", []):
            if h >= n: err("rule-1", f"{s['id']}: highlight index {h} out of range for “{l['en']}”")
        if not l.get("hl"): warn("rule-1", f"{s['id']}: EN caption without highlighted keyword")
        if EMOJI.search(l["text"] + l.get("en", "")): err("rule-14", f"{s['id']}: emoji in on-screen text")
    # rule-15 fonts in HyperFrames html + engine
    for p in spec["parts"]:
        if p["engine"] == "hyperframes":
            for f in glob.glob(os.path.join(fdir, p["dir"], "*.html")) + glob.glob(os.path.join(fdir, p["dir"], "*.tpl")):
                h = open(f).read()
                fams = set(re.findall(r"font-family:\s*\"?([^;\"}]+)", h))
                bad = [x for x in fams if x.strip() not in ("BVP", "Be Vietnam Pro", "inherit")]
                srcs = re.findall(r"@font-face\{[^}]*src:url\(([^)]+)\)", h)
                if bad: err("rule-15", f"{os.path.basename(f)}: non-brand font-family {bad}")
                elif srcs and all("BeVietnamPro" in x for x in srcs): ok("rule-15", f"{p['dir']}/{os.path.basename(f)}: Be Vietnam Pro embedded")
                else: err("rule-15", f"{os.path.basename(f)}: @font-face not Be Vietnam Pro: {srcs}")
                if re.search(r"https?://(cdn|fonts\.googleapis|unpkg|cdnjs)", h): err("rule-25", f"{os.path.basename(f)}: loads from CDN (GSAP/fonts must be local)")
                if re.search(r"(text-shadow|filter:\s*drop-shadow|box-shadow:[^;]*\d+px\s+\d+px\s+[1-9]\d*px)", h): warn("rule-14", f"{os.path.basename(f)}: blurred shadow/glow found")
    fts = open(os.path.join(REPO, "video-engine/src/composition/fonts.ts")).read()
    (ok if "Be Vietnam Pro" in fts or "BeVietnamPro" in fts else err)("rule-15", "video-engine fonts.ts uses Be Vietnam Pro")
    # rule-21 / 22 audio
    if any(k in json.dumps(spec).lower() for k in ('"music"', "bgm")): err("rule-21", "spec mentions music; no music in file")
    else: ok("rule-21", "no music")
    src = open(os.path.join(REPO, "assets/sfx/SOURCES.md")).read()
    for p in spec["parts"]:
        for s in p.get("scenes", []):
            for x in s.get("sfx", []):
                if x["name"] not in SFX_OK: err("rule-22", f"{s['id']}: sfx '{x['name']}' not in allowed set {sorted(SFX_OK)}")
                elif x["name"] not in src: err("rule-22", f"sfx '{x['name']}' missing in assets/sfx/SOURCES.md")
    # rule-40/41 voice
    texts = [(s["id"], l) for _, s, l in L]
    for sid, l in texts:
        low = l["text"].lower()
        for tell in AI_TELLS:
            if tell in low: warn("rule-40", f"{sid}: AI-tell phrase “{tell}”")
    allv = " ".join(l["text"].lower() for _, l in texts)
    part_lines = sum(1 for _, l in texts if any(re.search(rf"(?<!\w){p}(?!\w)", l["text"].lower()) for p in PARTICLES))
    (ok if part_lines >= 3 else warn)("rule-41", f"Southern particles in {part_lines}/{len(texts)} lines")
    if part_lines > 0.8 * len(texts): warn("rule-41", "particles on almost every line (profile: not on every line)")
    (ok if re.search(r"(?<!\w)bạn(?!\w)", allv) else warn)("rule-41", "addresses viewer as “bạn”")
    en_mix = sorted({w for w in re.findall(r"[a-z]+", " ".join(re.sub(r"\*\*", "", l["text"]) for _, l in texts).lower()) if w in EN_MIX})
    (ok if 1 <= len(en_mix) <= 3 else warn)("rule-41", f"English mix words: {en_mix or 'none'} (profile: 1–3 per clip; proper nouns exempt)")
    script = os.path.join(fdir, "script-final.md") if os.path.exists(os.path.join(fdir, "script-final.md")) else os.path.join(clip_dir, "script.md")
    if os.path.exists(script):
        st = open(script).read()
        n = st.count("[CẦN HIỆP XÁC NHẬN]") + len(re.findall(r"^\d+\. ", st.split("CẦN HIỆP XÁC NHẬN]")[-1], re.M)) if "CẦN HIỆP XÁC NHẬN" in st else 0
        (warn if n else ok)("rule-41", f"{os.path.relpath(script, REPO)}: {'has unconfirmed story items → Hiệp must confirm before posting' if n else 'no unconfirmed story items'}")
        if "Fact lock" not in st: warn("rule-40", "script has no Fact lock section")
    else: err("rule-35", "no script-final.md / script.md")
    # rule-46 voices
    voiced = set()
    for _, s, l in L:
        v = prof.get(l["speaker"], {}).get("voice")
        if not v: err("rule-46", f"{s['id']}: speaker {l['speaker']} has no voice preset in its profile")
        else: voiced.add(f"{prof[l['speaker']]['name']}={v['preset']}")
        if "ref_audio" in json.dumps(l): err("rule-46", "ref_audio (voice cloning) is forbidden")
    if voiced: ok("rule-46", "AI voices: " + ", ".join(sorted(voiced)))
    # DL-035: F5-TTS voices with synthetic VieNeu references
    VOICES = {"omi": ("f5-tts", "F5 · Mỹ Duyên", "assets/voice-refs/my-duyen.wav"), "hiep": ("f5-tts", "F5 · Thái Sơn", "assets/voice-refs/thai-son.wav")}
    for cid, (eng, pre, ref) in VOICES.items():
        pv = prof.get(cid, {}).get("voice", {})
        if cid == "omi" and not omi_used: continue
        if (pv.get("engine"), pv.get("preset"), pv.get("ref")) != (eng, pre, ref):
            (err if cid == "omi" else warn)("rule-46", f"{cid} voice {pv.get('engine')}/{pv.get('preset')} differs from DL-035 ({pre}); log a DL")
        elif not os.path.exists(os.path.join(REPO, ref)): err("rule-46", f"{cid} F5 reference missing: {ref}")
        else: ok("rule-46", f"{cid} voice = {pre} (F5-TTS, CC-BY-NC-SA risk accepted DL-035)")
    # rule-13 / 46 / 32 post package
    post = os.path.join(fdir, "post.md")
    if os.path.exists(post):
        pt = open(post).read()
        for need, rule, label in [("HowToLiveBetter", "rule-13", "credit HowToLiveBetter"), ("CC BY 4.0", "rule-13", "license name"), ("creativecommons.org/licenses/by/4.0", "rule-13", "license link"),
                                  ("chuyển thể", "rule-13", "'đã chuyển thể / adapted'")]:
            (ok if need in pt else err)(rule, f"post.md {label}")
        if voiced:
            (ok if "AI-generated content" in pt else err)("rule-46", "post.md: TikTok 'AI-generated content' toggle")
            (ok if "giọng AI" in pt else err)("rule-46", "post.md: AI-voice disclosure line in caption")
            if "giọng AI" in pt: (ok if "F5-TTS" in pt else err)("rule-46", "post.md: disclosure names the engine (F5-TTS, DL-035)")
        (ok if "#" in pt else warn)("rule-32", "post.md hashtags")
    else: (err if final else warn)("rule-32", "post.md missing")
    # rule-45 plans validate
    plans = sorted(glob.glob(os.path.join(fdir, "plan-*.voiced.json")))
    if plans:
        env = dict(os.environ, PATH=NODE_BIN + ":" + os.environ["PATH"])
        r = subprocess.run(["npx", "tsx", "src/cli.ts", "validate", *plans], cwd=os.path.join(REPO, "video-engine"), capture_output=True, text=True, env=env)
        (ok if r.returncode == 0 else err)("rule-45", "video-engine validate: " + (" | ".join(x.strip() for x in (r.stdout + r.stderr).splitlines() if x.strip().startswith(("✔", "✖", "error", "⚠")))[:400] or r.stderr[-300:]))
    elif final: err("rule-45", "no plan-*.voiced.json")
    # L-033 layout collisions: bubble ∩ prop/sign/character, prop over a character's head
    _ids = {p_["id"] for p_ in (spec.get("parts") or []) if p_.get("engine") == "remotion"} if isinstance(spec, dict) else set()
    plans_main = [x for x in plans if "-preview" not in x and (not _ids or os.path.basename(x)[5:-12] in _ids)]
    if plans_main:
        r = subprocess.run(["npx", "tsx", "src/layoutCheck.ts", *plans_main], cwd=os.path.join(REPO, "video-engine"), capture_output=True, text=True, env=dict(os.environ, PATH=NODE_BIN + ":" + os.environ["PATH"]))
        bad = [x.strip() for x in r.stdout.splitlines() if x.strip().startswith("✖")]
        (ok if r.returncode == 0 else err)("L-033", "layout collisions: " + ("none" if not bad else " | ".join(bad))[:500])
    # L-033 Reels (RR round 2, 3d8f43d): the Reels plan has its own caption box (x 60–648 incl. shadow, y 1000–1056+68·lines) + frame edge x 1046.
    # layoutCheck boxes are estimates; the per-frame pixel scan (scan-reels-clearance.py → out/reels-clearance.txt) is the authority when present.
    reels_plans = sorted(x for x in glob.glob(os.path.join(fdir, "out", "plan-reels*.json")) if "nocap" not in x)
    scan = os.path.join(fdir, "out", "reels-clearance.txt"); scan_txt = open(scan).read() if os.path.exists(scan) else ""
    scan_ok = bool(re.search(r"^PASS:", scan_txt, re.M)); rm_ = sorted(glob.glob(os.path.join(fdir, "*-reels.mp4")))
    if scan_txt and rm_ and os.path.getmtime(scan) < max(os.path.getmtime(x) for x in rm_): scan_ok = False; err("L-033", "reels clearance scan is older than the Reels MP4 → rerun scan-reels-clearance.py")
    if reels_plans:
        r = subprocess.run(["npx", "tsx", "src/layoutCheck.ts", *reels_plans], cwd=os.path.join(REPO, "video-engine"), capture_output=True, text=True, env=dict(os.environ, PATH=NODE_BIN + ":" + os.environ["PATH"]))
        bad = [x.strip() for x in r.stdout.splitlines() if x.strip().startswith("✖")]
        (ok if not bad else warn if scan_ok else err)("L-033", "reels plan layout (estimated boxes): " + ("none" if not bad else " | ".join(bad))[:500] + (" — pixel scan passes, estimates only" if bad and scan_ok else ""))
    elif final and rm_: err("L-033", "Reels MP4 present but no out/plan-reels*.json to check")
    if final and rm_:
        if not scan_txt: err("L-033", "no per-frame Reels clearance scan (out/reels-clearance.txt from scan-reels-clearance.py)")
        else: (ok if scan_ok else err)("L-033", "reels per-frame scan: " + " · ".join(x.strip() for x in scan_txt.splitlines() if x.startswith(("caption clearance min", "right edge clearance min", "PASS", "FAIL")))[:400])
    # final MP4
    mp4 = os.path.join(fdir, "out", spec["id"] + ".mp4")
    if not os.path.exists(mp4) and glob.glob(os.path.join(fdir, "*-tiktok.mp4")): mp4 = sorted(glob.glob(os.path.join(fdir, "*-tiktok.mp4")))[-1]  # out/ is gitignored and can vanish on resync → check the delivered TikTok file
    if final:
        if not os.path.exists(mp4): err("rule-4", f"missing {os.path.relpath(mp4, REPO)}")
        else:
            j = ffprobe(mp4); v = [s for s in j["streams"] if s["codec_type"] == "video"][0]; au = [s for s in j["streams"] if s["codec_type"] == "audio"]
            d = float(j["format"]["duration"])
            LX = spec.get("length_exception")
            (ok if LT[0] <= d <= LT[1] else warn)("rule-4", f"MP4 {d:.2f}s (target {LT[0]}–{LT[1]}s; L-080 length is content-driven → warn only)" + (f" · exception {LX}" if LX and d > 60.5 else ""))
            spec_ok = v["width"] == 1080 and v["height"] == 1920 and v["r_frame_rate"] == "30/1" and v["codec_name"] == "h264" and v.get("profile") == "High" and v["pix_fmt"] == "yuv420p" and v.get("color_space") == "bt709"
            (ok if spec_ok else err)("rule-4", f"video {v['width']}×{v['height']} {v['r_frame_rate']} {v['codec_name']} {v.get('profile')} {v['pix_fmt']} {v.get('color_space')}")
            if not au: err("rule-46", "MP4 has no audio track")
            else:
                m = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
                li = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", m)[-1]); pk = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)[-1])
                (ok if abs(li + 14) <= 1.0 and pk <= -0.5 else err)("rule-4", f"audio {au[0]['codec_name']} {au[0]['sample_rate']} Hz, {li} LUFS, peak {pk} dBFS (target −14 ±1, peak ≤ −0.5)")
            (ok if os.path.exists(os.path.join(fdir, "contact-sheet.png")) else err)("rule-34", "contact-sheet.png for frame review")
    # L-083 (Hiệp 21/10/2026): reels file opens on the template-A cover (frame 0 == cover.png, ≤0.5s); TikTok file has no cover frame.
    if final:
        cpng = os.path.join(fdir, "cover.png")
        def _ssim(mp4, n):
            r = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-i", cpng, "-filter_complex",
                f"[0:v]trim=start_frame={n}:end_frame={n+1},setpts=PTS-STARTPTS[a];[1:v]scale=1080:1920[b];[a][b]ssim=stats_file=-", "-f", "null", "-"], capture_output=True, text=True)
            m = re.findall(r"All:([\d.]+)", r.stdout + r.stderr); return float(m[0]) if m else 0.0
        reels = sorted(glob.glob(os.path.join(fdir, "*-reels.mp4"))); tiks = sorted(glob.glob(os.path.join(fdir, "*-tiktok.mp4")))
        if os.path.exists(cpng):
            for rm in reels:
                if _ssim(rm, 0) < 0.98: err("L-083", f"{os.path.basename(rm)} frame 0 is not cover.png (put template-A cover as first frame, ≤0.5s)"); continue
                n = 0
                while n < 20 and _ssim(rm, n) >= 0.98: n += 1
                (ok if n <= 15 else err)("L-083", f"{os.path.basename(rm)} opens on cover.png for {n} frame(s) = {n/30:.2f}s (≤0.50s)")
            for tk in tiks:
                (ok if _ssim(tk, 0) < 0.98 else err)("L-083", f"{os.path.basename(tk)} has no cover frame (TikTok takes cover.png separately)")
    # STT
    if do_stt and tpath and os.path.exists(tpath):
        t = json.load(open(tpath)); wavs = [os.path.join(REPO, "video-engine/public/voice", l["key"] + ".wav") for l in t["lines"]]
        # RR round 2 (3d8f43d, T2): when the clip uses an approved voice track, STT hears THAT file (what is delivered), not public/voice/*.wav
        # (can be stale: c05v4-c18.wav was not rev5). With a voice-only timing (sentence spans) each SENTENCE is cut at its real speech span ±0.15 s
        # and compared with the joined `say` of its lines (sub-sentence lines of 0.6 s make whisper hallucinate «đăng ký kênh»); else lines at timing ±0.2 s.
        vt = json.load(open(os.path.join(fdir, "spec.json"))).get("voice_track") if os.path.exists(os.path.join(fdir, "spec.json")) else None
        groups = None
        if vt and os.path.exists(os.path.join(fdir, vt)):
            sd = tempfile.mkdtemp(prefix="stt-slices-"); wavs = []
            cut = lambda o, ss, du: (subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{max(0.0, ss):.3f}", "-t", f"{du:.3f}", "-i", os.path.join(fdir, vt), "-ac", "1", "-ar", "16000", o]), wavs.append(o))
            vo = sorted(glob.glob(os.path.join(fdir, "voice-only-*.timing.json")))
            spans = {x["id"]: (x["pieces"][0]["start"], x["pieces"][-1]["end"]) for x in json.load(open(vo[-1]))["sentences"]} if vo else {}
            sid = lambda k: (re.search(r"-(c\d+)[a-z]?$", k) or [None, None])[1]
            if spans and all(sid(l["key"]) in spans for l in t["lines"]):
                groups = {}
                for l in t["lines"]: groups.setdefault(sid(l["key"]), []).append(l)
                for g_, ls in groups.items():
                    st_, en_ = spans[g_]; cut(os.path.join(sd, g_ + ".wav"), st_ - 0.15, en_ - st_ + 0.3)
                ok("rule-46", f"STT source: {vt}, {len(groups)} sentences cut at voice-only spans ±0.15s ({os.path.basename(vo[-1])})")
            else:
                for l in t["lines"]: cut(os.path.join(sd, l["key"] + ".wav"), l["t"] - 0.2, l["dur"] + 0.4)
                ok("rule-46", f"STT source: {vt} sliced at timing.json ±0.2s ({len(wavs)} lines)")
        r = subprocess.run([ASR_PY, os.path.join(REPO, "pipeline/tts/stt_check.py"), *wavs], capture_output=True, text=True)
        got = {x.split(" | ")[0]: x.split(" | ", 1)[1] for x in r.stdout.splitlines() if " | " in x}
        if groups:
            for g_, ls in groups.items():
                hyp = got.get(g_ + ".wav", ""); ref = " ".join(l["say"] for l in ls); sim = difflib.SequenceMatcher(None, norm(ref), norm(hyp)).ratio()
                (ok if sim >= 0.75 else warn if sim >= 0.55 else err)("rule-46", f"STT {g_} ({'/'.join(l['scene'] for l in ls)}) {sim:.2f}: “{hyp}”")
        for l in ([] if groups else t["lines"]):
            hyp = got.get(l["key"] + ".wav", ""); sim = difflib.SequenceMatcher(None, norm(l["say"]), norm(hyp)).ratio()
            (ok if sim >= 0.75 else warn if sim >= 0.55 else err)("rule-46", f"STT {l['scene']} {sim:.2f}: “{hyp}”")
    # rule-50 (DL-042): every transition has an SFX + continuous ambience bed
    if final and tpath and os.path.exists(tpath):
        tj = json.load(open(tpath)); tr = tj.get("transitions"); mixs = tj.get("sfx_mix", [])
        if not tr: err("rule-50", "timing.json has no transitions list (build-final ≥ DL-042 writes it)")
        else:
            src = open(os.path.join(REPO, "assets/sfx/SOURCES.md")).read()
            miss = [t for t in tr if not any(m["name"] == t["sfx"] and abs(m["at"] - t["at"]) <= 0.3 for m in mixs)]
            (ok if not miss else err)("rule-50", f"{len(tr)} transitions, {len(tr) - len(miss)} with SFX" + (f"; missing at {[t['at'] for t in miss]}" if miss else ""))
            (ok if any(m["name"] == "ambience" for m in mixs) else err)("rule-50", "ambience bed under whole clip")
            for n in sorted({m["name"] for m in mixs}):
                if n not in src: err("rule-22", f"sfx '{n}' missing in assets/sfx/SOURCES.md")
    # rule-53 (DL-045): complete TikTok post package (template v1), each field in its own code block
    pm = os.path.join(fdir, "post.md")
    if final:
        pt = open(pm).read() if os.path.exists(pm) else ""
        secs = {m.group(1).strip(): m.group(2) for m in re.finditer(r"^## \d+\. ([^\n]+)\n(.*?)(?=^## |\Z)", pt, re.S | re.M)}
        need = ["File video", "Chữ trên cover", "Caption", "Hashtag", "Từ khoá SEO", "Bình luận ghim", "Giờ đăng", "Âm thanh", "Checklist cài đặt", "Ghi nguồn", "Series", "Nhãn AI"]
        def blk(k):
            for h, b in secs.items():
                if h.startswith(k):
                    m = re.search(r"```\n(.*?)\n```", b, re.S); return m.group(1).strip() if m else ""
            return None
        miss = [k for k in need if not blk(k)]
        (ok if not miss else err)("rule-53", "post.md has all 12 fields with code blocks" + (f" — missing/empty: {miss}" if miss else ""))
        cv = blk("Chữ trên cover") or ""; (ok if 0 < len(cv) <= 40 else err)("rule-53", f"cover text {len(cv)} chars (≤ 40)")
        (ok if os.path.exists(os.path.join(fdir, "cover.png")) else err)("rule-53", "cover.png exported")
        (ok if re.search(r"Frame cover: \*\*[\d.]+s\*\*", pt) else err)("rule-53", "cover frame timestamp given")
        cap = blk("Caption") or ""; (ok if 0 < len(cap) <= 2200 else err)("rule-53", f"caption {len(cap)} chars (≤ 2200)")
        tags = re.findall(r"#\w+", blk("Hashtag") or ""); (ok if 3 <= len(tags) <= 5 else err)("rule-53", f"{len(tags)} hashtags (3–5)")
        spam = [t for t in tags if t.lower() in ("#fyp", "#foryou", "#foryoupage", "#viral", "#xuhuong", "#trending", "#lenxuhuong")]
        (ok if not spam else err)("rule-53", "no spammy hashtags" + (f": {spam}" if spam else ""))
        (ok if all(t in cap for t in tags) else warn)("rule-53", "hashtags appended to caption")
        st = blk("Checklist cài đặt") or ""; (ok if all(k in st for k in ("AI", "Duet", "Stitch", "Vị trí")) else err)("rule-53", "settings checklist: AI toggle, duet/stitch, location")
        (ok if os.path.exists(os.path.join(fdir, "post-checklist.md")) else err)("rule-53", "post-checklist.md present")
    # L-020 (DL-046): cover comes from the Cover template (props json), never a video frame grab
    if final:
        import hashlib
        cdir = os.path.join(fdir, "cover"); cpng = os.path.join(fdir, "cover.png")
        props = glob.glob(os.path.join(cdir, "cover-*.props.json"))
        rend = {hashlib.md5(open(f, "rb").read()).hexdigest() for f in glob.glob(os.path.join(cdir, "cover-*.png")) if "grid" not in f}
        okc = os.path.exists(cpng) and hashlib.md5(open(cpng, "rb").read()).hexdigest() in rend
        cv = spec.get("cover") or {}
        (ok if cv.get("direction") == "a" and cv.get("hero") and cv.get("series") and cv.get("ep") else err)("rule-54", f"spec.cover props (template A) {'present' if cv else 'MISSING'}")
        (ok if props and okc else err)("L-020", "cover.png rendered from Cover template (props json present)" if okc else
            f"cover.png is not a Cover-template render ({len(props)} template direction(s) in cover/ — render cover from template A: npx remotion still src/index.ts Cover final/cover.png --props=spec.cover)")
    check_diacritics(spec, fdir, L)
    check_prosody(spec, fdir, final)
    voice_only_checks(latest_measure(fdir), fdir, clip_dir, spec, False)  # E1 + L-027 on the newest voice-only measure, if any
    # rule-55 (DL-051): hook 0–3s rapid, dramatic, emotion-dense (clips before 02 are legacy → warn)
    e55 = warn if "clip-01" in clip_dir else err
    hk = spec.get("hook") or {}; A0 = spec["parts"][0]; scs = A0.get("scenes", [])
    hsc = [x for x in scs if x["id"] in hk.get("scenes", [])]
    (ok if hk.get("text") and scs and scs[0].get("narration") == hk["text"] else e55)("rule-55", "on-screen hook text on frame 0 (first scene narration = spec.hook.text)")
    if hsc:
        fw = len(re.sub(r"\{[^}]*\}|\*", "", hsc[0]["lines"][0]["text"]).split())
        (ok if fw <= 6 else e55)("rule-55", f"first spoken clause {fw} words (≤ 6, punchy)")
        t = 0.12; ev = []; first_sp = 0.12
        tl_ = {}
        if tpath and os.path.exists(tpath):
            for l in json.load(open(tpath)).get("lines", []): tl_.setdefault(l["scene"], []).append(l)
        for k, x in enumerate(hsc):
            if k: ev.append(("cut", t)); t += 0.06
            st = t
            for x2 in x.get("sfx", []): ev.append(("hit", st + x2.get("offset", 0)))
            d = sum((tl_[x["id"]][i]["dur"] if x["id"] in tl_ and i < len(tl_[x["id"]]) else len(re.sub(r"\{[^}]*\}|\*", "", l["text"]).split()) * 0.27 + 0.3) for i, l in enumerate(x["lines"]))
            t = st + d + 0.15
        if tl_ and hsc[0]["id"] in tl_: first_sp = tl_[hsc[0]["id"]][0]["t"]
        in3 = [e for e in ev if e[1] <= 3.0]; fv = min([e[1] for e in ev] or [99])
        (ok if first_sp <= 0.3 else e55)("rule-55", f"first spoken word at {first_sp:.2f}s (≤ 0.3)")
        (ok if fv <= 1.0 else e55)("rule-55", f"first visual change/hit at {fv:.2f}s (≤ 1.0)")
        nc = sum(1 for e in in3 if e[0] == "cut")
        (ok if len(in3) >= 2 and nc >= 1 else e55)("rule-55", f"0–3s: {nc} cut(s) + {len(in3) - nc} hit(s) (need ≥ 2 total, ≥ 1 cut)" + ("" if tpath and os.path.exists(tpath) else " · estimated"))
        emo = [l["emotion"] for x in hsc for l in x["lines"]]
        (ok if any(e in ("sad", "surprised", "angry", "scared", "confused") for e in emo) else warn)("rule-55", f"hook voice emotions {emo} (dramatic)")
    else: e55("rule-55", "spec.hook.scenes missing")
    # rule-56 (DL-052): subtle engagement devices, no begging
    eng = spec.get("engagement") or []; types = {e.get("type") for e in eng}
    btxt = {x["id"]: " ".join(l["text"] for l in x["lines"]) for p_ in spec["parts"] for x in p_.get("scenes", p_.get("sections", []))}
    def _n(x): return re.sub(r"[^\w\s]", "", x.lower())
    (ok if len(types & {"comment-challenge", "save-prompt", "relatable-question", "loop"}) >= 3 and {"comment-challenge", "loop"} <= types else e55)("rule-56", f"engagement devices {sorted(t for t in types if t)} (≥3 incl. comment-challenge + loop)")
    for e in eng:
        if _n(e.get("text", "")) not in _n(btxt.get(e.get("beat"), "")): e55("rule-56", f"{e.get('type')} text not in beat {e.get('beat')}: “{e.get('text')}”")
        if e.get("type") == "loop" and hsc and _n(e.get("hook_word", "")) not in _n(" ".join(btxt.get(x["id"], "") for x in hsc)): e55("rule-56", "loop hook_word not in hook")
    beg = [k for k, v in btxt.items() if re.search(r"(like|follow|thả tim|share|chia sẻ) (đi|nha|giùm|giúp)|nhớ (like|follow|thả tim)|xin (like|follow)", v.lower())]
    (ok if not beg else e55)("rule-56", "no begging for likes/follows" + (f": {beg}" if beg else ""))
    # rule-57 (DL-053): TikTok-native trend signals
    tsp = os.path.join(clip_dir, "final", "trend-signals.md")
    if "clip-01" in clip_dir: pass
    elif not os.path.exists(tsp): err("L-084", "final/trend-signals.md missing (trend must be in the clip, Hiệp 21/10)")
    else:
        ts = open(tsp, encoding="utf8").read()
        _cn = re.search(r"clip-(\d+)", clip_dir); _e84 = err if (_cn and int(_cn.group(1)) >= 5) else warn  # L-084 from clip-05 on
        m = re.search(r"Trend trong clip:\s*(b\d+[a-z]?)\s*[·|-]\s*(.+)", ts)
        if not m: _e84("L-084", "trend-signals.md lacks line «Trend trong clip: bNN · <câu/format/hình>» (trend must be visible in hook/b01–b02)")
        else:
            bid = m.group(1); hook_ok = bid in ("b01", "b01a", "b01b", "b02", "b02a")
            (ok if hook_ok else _e84)("L-084", f"trend shown at {bid}: {m.group(2)[:80]}" + ("" if hook_ok else " → must be in hook (b01–b02)"))
        (ok if re.search(r"http\S+.*\d[\d.,]*\s*(M\s*)?view", ts) else warn)("rule-57", "trend-signals.md has clip URLs with view counts")
        if "proxy" in ts.lower() and "tiktok.com/@" not in ts: warn("rule-57", "only proxy signals, no TikTok clip URL yet → verify in app before posting")
    # rule-58 (DL-059, L-022): one continuous story, precise words, no vague phrases
    VAGUE = [r"\b(điện thoại|não|cảm xúc|nó|lười|việc)\s+thắng\b", r"\bthắng\s*[.!]?$", r"điều gì đó", r"cái gì đó", r"nhiều thứ", r"mọi thứ", r"kiểu như", r"theo một cách nào đó", r"vân vân", r"\bthật sự rất\b", r"\brất là\b", r"một cảm giác\b"]
    CONN = r"^(thế là|rồi|nhưng|mà|hóa ra|tức là|nói gọn|vì|tại vì|nên|vậy|bằng chứng|lý do|nếu|còn|ngược lại|lưu ý|phần mình|thành|sau đó|cuối cùng|thay vào đó|đó là|kết quả|chính vì|giờ|kiểu|nói thiệt|xong|haizz|ủa|trời ơi|thôi|hả|ê|khoan)\b|^\S+( \S+)? hả\?"
    beats_ = [x for p_ in spec["parts"] for x in p_.get("scenes", p_.get("sections", []))]
    hookset = set((spec.get("hook") or {}).get("scenes", []))
    vg = [(x["id"], m.group(0)) for x in beats_ for l in x["lines"] for pat in VAGUE for m in [re.search(pat, re.sub(r"\{[^}]*\}", "", l["text"]).lower())] if m]
    (e55 if False else (warn if "clip-01" in clip_dir else err))("rule-58", "no vague phrases" + (f": {vg}" if vg else "")) if vg else ok("rule-58", "no vague phrases (‘X thắng’, ‘điều gì đó’, ‘mọi thứ’…)")
    nc_ = [x["id"] for i_, x in enumerate(beats_) if i_ and x["id"] not in hookset and not x.get("link") and sum(len(l["text"].split()) for l in x["lines"]) > 4 and not re.search(CONN, re.sub(r"\{[^}]*\}|[\"“”]", "", x["lines"][0]["text"]).strip().lower())]
    ((warn if "clip-01" in clip_dir else err) if nc_ else ok)("rule-58", "every non-hook beat opens with a connector/callback" + (f"; missing: {nc_}" if nc_ else ""))
    lw = [x["id"] for x in beats_ for l in x["lines"] if max(len(c.split()) for c in re.split(r"[.,?!:;]", re.sub(r"\{[^}]*\}", "", l["text"])) if c.strip()) > 12]
    (warn if lw else ok)("rule-58", "clauses ≤ 12 words (punchy)" + (f"; long: {lw}" if lw else ""))
    # rule-60 (DL-061, L-024): spoken Southern style + every beat interleaves action + emotion + dialogue
    WRITTEN = [r"\btức là\b", r"\bngược lại\b", r"\bbằng chứng\b", r"hệ số", r"tương quan", r"\blưu ý\b", r"\bdo đó\b", r"\bvì vậy\b", r"\btuy nhiên\b", r"\bbởi vì\b", r"\bnhằm\b", r"\bđiều này\b", r"\bhơn nữa\b", r"\bmặt khác\b", r"\bđồng thời\b", r"\bcụ thể là\b", r"\bkết quả là\b", r"\bnói gọn\b", r"phân tích gộp", r"\bcơ chế\b", r"\bnhư vậy\b"]
    INTERJ = r"(?<!\w)(trời ơi|trời|haizz|hả|ủa|thôi xong|ê|khoan|nè|nha|hà|hông|lận|á|ơ|ồ|thiệt)(?!\w)"
    lax = "clip-01" in clip_dir
    wr = [(x["id"], m.group(0)) for x in beats_ for l in x["lines"] for pat in WRITTEN for m in [re.search(pat, re.sub(r"\{[^}]*\}", "", l["text"]).lower())] if m]
    ((warn if lax else err) if wr else ok)("rule-60", "spoken style, no written/academic connectors" + (f": {wr}" if wr else ""))
    na = [x["id"] for x in beats_ if len(((x.get("stage") or {}).get("action") or "")) < 8]
    ((warn if lax else err) if na else ok)("rule-60", "every beat has a stage action (stage.action)" + (f"; missing: {na}" if na else ""))
    ne = [x["id"] for x in beats_ if not (x.get("stage") or {}).get("react") and not re.search(INTERJ, " ".join(l["text"] for l in x["lines"]).lower())]
    ((warn if lax else err) if ne else ok)("rule-60", "every beat has an emotion cue (interjection in line or stage.react)" + (f"; missing: {ne}" if ne else ""))
    ni = [x["id"] for x in beats_ if not re.search(INTERJ, " ".join(l["text"] for l in x["lines"]).lower())]
    (warn if len(ni) > len(beats_) // 2 else ok)("rule-60", f"spoken interjections/particles in {len(beats_) - len(ni)}/{len(beats_)} beats (≥ half)")
    # rule-61 (DL-062, L-029): dialogue never narrates what the visual/action shows; no filler; tight word budget
    def _bg(t): w = re.findall(r"\w+", t.lower()); return {" ".join(w[i:i + 2]) for i in range(len(w) - 1)}
    nar = [(x["id"], sorted(_bg(l["text"]) & _bg(" | ".join(w for w in re.sub(r"'[^']*'|‘[^’]*’|“[^”]*”", " | ", (x.get("stage") or {}).get("action", "")).split() if not (w.isupper() and len(w) > 1))))) for x in beats_ for l in x["lines"]]
    nar = [(i, o) for i, o in nar if len(o) >= 2]
    ((warn if lax else err) if nar else ok)("rule-61", "dialogue does not narrate the stage action" + (f": {nar}" if nar else ""))
    FILL = [r"\bmở code\b", r"\bgõ (được )?hai dòng\b", r"\bthôi thì\b", r"\bnói chung\b", r"\bthật ra thì\b", r"\bcái việc\b", r"\bkiểu vậy\b", r"\bnhư mình đã nói\b", r"\bnhìn nè\b", r"\bnhư bạn thấy\b", r"\bđây là\b"]
    fl = [(x["id"], m.group(0)) for x in beats_ for l in x["lines"] for pat in FILL for m in [re.search(pat, l["text"].lower())] if m and not (x["id"] in hookset and "của cái việc" in l["text"].lower())]  # L-036 meme stem exempt in hook
    ((warn if lax else err) if fl else ok)("rule-61", "no filler / visual-describing phrases" + (f": {fl}" if fl else ""))
    if spec.get("word_target"):
        bw = [x["id"] for x in beats_ if sum(len(l["text"].split()) for l in x["lines"]) > 20]
        (err if bw else ok)("rule-61", "every beat ≤ 20 words" + (f"; over: {bw}" if bw else ""))
    # rule-62 (DL-063, L-030): one ABT throughline, every beat states its contextual link, callbacks to prior clips, ≤2 literal nhưng/nên
    e62 = warn if lax else err
    tl = spec.get("throughline", "")
    (ok if tl and re.search(r"NHƯNG", tl) and re.search(r"VÌ VẬY|NÊN", tl) else e62)("rule-62", "spec.throughline present in ABT form (… VÀ … NHƯNG … VÌ VẬY …)" if tl else "spec.throughline MISSING")
    nl = [x["id"] for i_, x in enumerate(beats_) if i_ and len(x.get("link", "")) < 8]
    (e62 if nl else ok)("rule-62", "every beat after the first has a contextual `link` (why it follows)" + (f"; missing: {nl}" if nl else ""))
    lit = sum(len(re.findall(r"(?<!\w)(nhưng|nên)(?!\w)", re.sub(r"\{[^}]*\}", "", l["text"]).lower())) for x in beats_ for l in x["lines"])
    (e62 if lit > 2 else ok)("rule-62", f"literal ‘nhưng/nên’ in dialogue: {lit} (≤ 2; links come from context)")
    hq = spec.get("hook_question") or {}
    (ok if hq.get("asked") and hq.get("answered") and hq.get("answered") != hq.get("asked") else e62)("rule-62", "hook_question asked + answered later (open loop closed)")
    cno = int(re.search(r"clip-(\d+)", clip_dir).group(1)) if re.search(r"clip-(\d+)", clip_dir) else 1
    if cno > 1: ((ok if spec.get("callbacks") is not None else e62))("rule-62", f"callbacks to prior clips declared ({len(spec.get('callbacks') or [])}); use [] if none overlap")
    # rule-64 (DL-065, L-032): hook→intro→body→summary→one CTA; typed hook ≤ 2 sentences; no generic opener; alt hook
    e64 = warn if lax else err
    stc = spec.get("structure") or {}
    need = ["hook", "intro", "body", "summary", "cta"]
    (ok if all(stc.get(k) for k in need) else e64)("rule-64", "spec.structure has hook/intro/body/summary/cta" + ("" if all(stc.get(k) for k in need) else f"; missing {[k for k in need if not stc.get(k)]}"))
    if stc.get("hook"):
        ht = " ".join(l["text"] for x in beats_ if x["id"] in stc["hook"] for l in x["lines"])
        ns = len([z for z in re.split(r"(?<=[.!?])\s+", ht) if z.strip()])
        (ok if ns <= 2 else e64)("rule-64", f"hook {ns} sentence(s) (≤ 2)")
        gen = re.search(r"^(hôm nay mình sẽ|bạn có biết|xin chào|chào các bạn|trong video này)", ht.strip().lower())
        (e64 if gen else ok)("rule-64", "hook is not a generic opener")
    if stc.get("cta"):
        ct = " ".join(l["text"] for x in beats_ if x["id"] in stc["cta"] for l in x["lines"]).lower()
        nct = len(re.findall(r"comment|follow|lưu lại|share|bấm|theo dõi", ct))
        (ok if nct == 1 else e64)("rule-64", f"exactly one CTA ({nct})")
    (ok if (spec.get("hook_alt") or {}).get("type") in ("direct", "controversy", "negative") else warn)("rule-64", "hook_alt of another type proposed")
    # rule-52 / L-019 (DL-044): effects planned at script stage (gate 1) — blocks pre-render too
    ts = spec.get("transition_sfx") or {}
    TRN = {"whoosh-soft", "swish", "whoosh"}
    (ok if ts.get("part") in TRN and ts.get("scene") in TRN else err)("rule-52", f"transition_sfx planned: {ts or 'missing'}")
    def _norm(x): return re.sub(r"[^\w\s]", "", x.lower())
    for p_ in spec["parts"]:
        for x in p_.get("scenes", p_.get("sections", [])):
            fx = x.get("fx") or {}; txt = _norm(" ".join(l["text"] for l in x["lines"]))
            (ok if len(fx.get("visual", "")) >= 15 else err)("rule-52", f"{x['id']}: motion/visual described" + ("" if fx.get("visual") else " — MISSING fx.visual"))
            w = fx.get("word", ""); (ok if w and _norm(w) in txt else err)("rule-52", f"{x['id']}: effect tied to spoken word “{w}”" + ("" if w and _norm(w) in txt else " — not in line text"))
            accs = [h for h in x.get("hits", []) if h.get("sfx")] + [{"sfx": y["name"], "word": y.get("word")} for y in x.get("sfx", [])]
            for h in accs:
                if not h.get("word") or _norm(h["word"]) not in txt: err("rule-52", f"{x['id']}: accent `{h['sfx']}` hit word “{h.get('word')}” not in line text")
            if p_["engine"] == "hyperframes": (ok if any(h.get("sfx") for h in x.get("hits", [])) else err)("rule-52", f"{x['id']}: explainer has ≥1 planned hit + SFX")
    sfm = os.path.join(fdir, "script-final.md"); stx = open(sfm).read() if os.path.exists(sfm) else ""
    tab = stx.split("## Bảng hiệu ứng", 1)[1] if "## Bảng hiệu ứng" in stx else ""
    ids = [x["id"] for p_ in spec["parts"] for x in p_.get("scenes", p_.get("sections", []))]
    miss = [i for i in ids if f"| {i} |" not in tab]
    (ok if tab and not miss else err)("rule-52", "script-final.md effects table covers every beat" + (f" — missing {miss or 'table'} (run pipeline/scripts/fx-table.py --write)" if (miss or not tab) else ""))
    (ok if not tab or "**THIẾU**" not in tab else err)("rule-52", "effects table has no **THIẾU** cells")
    # L-044: script lines flow as connected speech — ≤ 5 phrases per beat, ≤ 1 fragment under 3 words
    chop = []
    for row in stx.split("## Kịch bản", 1)[-1].split("\n") if "## Kịch bản" in stx else []:
        cc = row.split(" | ")
        if not row.startswith("| b") or len(cc) < 5: continue
        ph = [re.sub(r"\{nhấn: |\{kéo: |\}|[«»…:;,.?!]", " ", x).split() for x in cc[3].split("\\|")]
        if len(ph) > 5 or sum(1 for x in ph if 0 < len(x) < 3) >= 2 or (len(ph) >= 4 and sum(map(len, ph)) / len(ph) < 4.5): chop.append(f"{cc[0][2:].split()[0]}:{len(ph)}ph")
    (warn if chop else ok)("L-044", "script beats flow (≤ 5 phrases, ≤ 1 fragment < 3 words, ≥ 4 phrases need avg ≥ 4.5 words)" + (f"; choppy: {chop}" if chop else ""))
    # rule-51 (DL-043): every explainer section has ≥1 marked hit with an accent SFX, mixed at the hit time
    if final and tpath and os.path.exists(tpath):
        tj = json.load(open(tpath)); hits = tj.get("hits", []); mixs = tj.get("sfx_mix", [])
        for p_ in spec["parts"]:
            for sec in p_.get("sections", []):
                hs = [h for h in hits if h.get("section") == sec["id"] and h.get("sfx")]
                bad = [h["id"] for h in hs if not any(m["name"] == h["sfx"] and abs(m["at"] - h["t"]) <= 0.05 for m in mixs)]
                (ok if hs and not bad else err)("rule-51", f"{sec['id']}: {len(hs)} accent hit(s) " + (f"[{', '.join(h['sfx'] for h in hs)}]" if hs else "— none") + (f"; not in mix: {bad}" if bad else ""))
                if len(hs) > 3: warn("rule-51", f"{sec['id']}: {len(hs)} accent SFX (> 3 → clutter)")
        acc = sorted(m["at"] for m in mixs if m["name"] not in ("ambience", "whoosh-soft", "swish", "roomtone"))
        close = [round(b, 2) for a, b in zip(acc, acc[1:]) if b - a < 0.25]
        (ok if not close else warn)("rule-51", f"{len(acc)} accent SFX, spacing ≥ 0.25s" + (f"; too close at {close}" if close else ""))
    check_l087(spec, L, fdir, clip_dir)
    check_l088(spec, L, fdir, clip_dir)
    lessons(spec, fdir, L, final, tpath)
    return report(outp)

# ---- rule-49: lessons gate (logs/lessons.md). Every measurable lesson = a check named after its id. ----
KEY_TERMS = {"toeic": "tô ích", "ok": "ô kê", "okay": "ô kê"}   # L-010: Latin terms TTS misreads → required phonetic
FUNC_WORDS = {"a", "an", "the", "to", "of", "and", "or", "is", "are", "my", "your", "it", "in", "on", "at", "for"}

def wav_read(path):
    import wave, array
    with wave.open(path) as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth(); b = w.readframes(n); sr = w.getframerate()
    a = array.array("h", b)[::ch] if sw == 2 else array.array("h")
    return [x / 32768 for x in a], sr

def audio_cuts(path, meta):
    """L-008: clicks (sample jump > 0.35 of peak) and phrase edges that start/end loud (cut mid-syllable)."""
    x, sr = wav_read(path)
    if not x: return [], []
    import numpy as np
    a = np.asarray(x, np.float32); pk = float(np.abs(a).max()) or 1; probs = []
    # Generic click scan is a WARNING heuristic only: on natural F5/VieNeu takes plosives reach 2nd-diff/median
    # ratios up to ~160, overlapping real splices (~14), so it cannot block. Blocking = edit-point checks below.
    d2 = np.abs(np.diff(a, 2)); f = int(sr / 1000); n = len(d2) // f; clicks = []
    if n > 60:
        e = d2[:n * f].reshape(n, f).mean(1)
        med = np.array([np.median(e[max(0, i - 25):i + 25]) for i in range(n)]) + 1e-9
        clicks = [round(i / 1000, 2) for i in np.where((e > 200 * med) & (e > e.max() * 0.1))[0]]
    def rdb(a, b):
        seg = x[max(0, int(a * sr)):max(0, int(b * sr))]
        return 20 * math.log10((sum(v * v for v in seg) / max(1, len(seg))) ** 0.5 / pk + 1e-9) if seg else -99
    ph = meta.get("phrases") or []
    for k, p in enumerate(ph):
        if p.get("merged") and k + 1 < len(ph) and ph[k + 1].get("merged") and abs(ph[k + 1]["start"] - p["end"]) < 0.005: continue  # inside one natural segment
        if k > 0 and abs(p["start"] - ph[k - 1]["end"]) > 0.05 and rdb(p["start"], p["start"] + 0.008) > -20: probs.append(f"phrase {k} starts loud (mid-syllable cut)")
        if k + 1 < len(ph) and abs(ph[k + 1]["start"] - p["end"]) > 0.05 and rdb(p["end"] - 0.008, p["end"]) > -20: probs.append(f"phrase {k} ends loud (mid-syllable cut)")
    return probs, clicks

def lessons(spec, fdir, L, final, tpath):
    lp = os.path.join(REPO, "logs/lessons.md")
    if not os.path.exists(lp): err("rule-49", "logs/lessons.md missing"); return
    ids = re.findall(r"^\| (L-\d{3}) ", open(lp).read(), re.M); ok("rule-49", f"lessons.md: {len(ids)} lessons loaded")
    # L-001 contact sheet (frame review)
    (ok if os.path.exists(os.path.join(fdir, "contact-sheet.png")) else (err if final else warn))("L-001", "contact-sheet.png present for self-review")
    # L-004 highlight index
    bad = [f"{s['id']}:{l['en']!r} hl={l.get('hl')}" for _, s, l in L if l.get("en") and any((not isinstance(i, int)) or i >= len(l["en"].split()) for i in l.get("hl", []))]
    fw = [f"{s['id']}:{l['en'].split()[i]}" for _, s, l in L if l.get("en") for i in l.get("hl", []) if isinstance(i, int) and i < len(l["en"].split()) and re.sub(r"\W", "", l["en"].split()[i].lower()) in FUNC_WORDS]
    (err if bad else ok)("L-004", f"highlight indexes out of range: {bad}" if bad else "highlight indexes within EN caption")
    if fw: err("L-004", f"function word highlighted: {fw}")
    # L-005 TTS tags spoken as words
    tg = [s["id"] for _, s, l in L if any(re.search(r"\[[^\]]+\]", t or "") for t in [l.get("text"), l.get("say")] + [p.get("t", "") + p.get("tag", "") for p in l.get("phrases", [])])]
    (err if tg else ok)("L-005", f"non-verbal [tags] in spoken text: {tg}" if tg else "no [tags] in spoken text")
    # L-006 robotic tempo
    tp = [f"{s['id']}:{p.get('tempo')}" for _, s, l in L for p in l.get("phrases", []) if not 0.85 <= p.get("tempo", 1.0) <= 1.15]
    nop = [s["id"] for _, s, l in L if not l.get("phrases")]
    (err if tp else ok)("L-006", f"phrase tempo outside 0.85–1.15: {tp}" if tp else "phrase tempos within 0.85–1.15")
    if nop: warn("L-006", f"lines without `phrases` (no prosody shaping): {nop}")
    # L-010 key terms
    kt = []
    for _, s, l in L:
        spoken = (" ".join(p.get("t", "") for p in l["phrases"]) if l.get("phrases") else l.get("say") or l.get("text", "")).lower()
        for term, ph in KEY_TERMS.items():
            if re.search(rf"(?<!\w){term}(?!\w)", spoken): kt.append(f"{s['id']}: '{term}' spoken raw (use '{ph}')")
    (err if kt else ok)("L-010", "; ".join(kt) if kt else "key terms use phonetic spelling")
    # L-025 English/brand words must be respelled in the spoken part (display text keeps the real word)
    br = [f"{s['id']}: '{m}'" for _, s, l in L for m in re.findall(r"(?<!\w)(POV|Omi|TikTok|Haizz|code)(?!\w)", re.sub(r"\{[^}]*\}", "", " ".join(p.get("t", "") for p in l.get("phrases", []))), re.I)]
    (warn if br else ok)("L-025", f"raw English/brand words in spoken text (respell: POV→Pi ô vi, Omi→Ô mi, TikTok→Tíc Tóc, Haizz→Hầy..., code→cốt): {br}" if br else "spoken text respelled")
    vd = os.path.join(REPO, "video-engine/public/voice"); tl = []
    _en = {l.get("en") for _, _, l in L}
    _tps = [tp for tp in [tpath, os.path.join(fdir, "preview", "timing-preview.json")] if tp and os.path.exists(tp) and all(x.get("en") in _en for x in json.load(open(tp)).get("lines", []))]
    for tp_ in _tps:
        if tp_ and os.path.exists(tp_):
            for x in json.load(open(tp_)).get("lines", []):
                vj = os.path.join(vd, x["key"] + ".json")
                if os.path.exists(vj):
                    sm = json.load(open(vj)).get("stt_sim", 1)
                    if sm < 0.8: tl.append(f"{x['scene']}:{x['key']} {sm}")
    (err if tl else ok)("L-025", f"line STT < 0.8: {tl}" if tl else "all rendered lines STT ≥ 0.8")
    # L-027 hook voice gaps (choppy): clause gaps inside a line + line-to-line gaps in hook scenes ≤ 0.1 s
    hg = []
    for tp_ in _tps:
        if not (tp_ and os.path.exists(tp_)): continue
        hook_ids = {s["id"] for _, s, _ in L if s.get("part") == "hook"}
        ls_ = [x for x in json.load(open(tp_)).get("lines", []) if x["scene"] in hook_ids]
        for x in ls_:
            vj = os.path.join(vd, x["key"] + ".json")
            if os.path.exists(vj):
                for u in json.load(open(vj)).get("units", [])[:-1]:
                    if u.get("gap_after", 0) > 0.1: hg.append(f"{x['scene']}: clause gap {u['gap_after']}s")
        for a, b in zip(ls_, ls_[1:]):
            g = round(b["t"] - (a["t"] + a["dur"]), 3)
            if g > 0.1: hg.append(f"{a['scene']}→{b['scene']}: line gap {g}s")
    (err if hg else ok)("L-027", f"hook gaps > 0.1s: {hg[:8]}" if hg else "hook voice gaps ≤ 0.1s")
    # L-028 self-blame lines must be punchy (!) with post emphasis on the key word
    sb = [s["id"] for _, s, l in L if re.search(r"đồ lười|ghét bản thân|tội lỗi", " ".join(p.get("t", "") for p in l.get("phrases", [])).lower()) and s.get("part") == "hook" and not ("!" in " ".join(p.get("t", "") for p in l["phrases"]) and (l.get("emph_tail") or l.get("emph_head") or "{nhấn:" in " ".join(p.get("t", "") for p in l["phrases"])))]
    (err if sb else ok)("L-028", f"self-blame hook line without '!' + emph_tail/emph_head: {sb}" if sb else "self-blame lines punchy + emphasized")
    # L-036 meme-stem delivery: a line using the 'bản chất / Thứ nhất / Thứ hai / Và cuối cùng' stem must not be one flat
    # whole-line F5 take: needs ≥2 clause phrases (stem | payload) and a {nhấn:}/{kéo:}/emph mark on the payload slot
    ms = [s["id"] for _, s, l in L if re.match(r"\s*(thì cái bản chất|thứ nhất là|thứ hai là|và cuối cùng là)", re.sub(r"\*", "", l.get("text", "")).lower())
          and not (len(l.get("phrases", [])) >= 2 and any(p.get("emph") or "{nhấn:" in p.get("t", "") or "{kéo:" in p.get("t", "") for p in l["phrases"]))]
    (err if ms else ok)("L-036", f"meme-stem lines voiced flat (need stem|payload phrases + payload emphasis): {ms}" if ms else "meme-stem lines split + payload emphasized")
    # L-031 / rule-63: every hook sentence has one {nhấn: …} word; hook should carry Southern particles
    import re as _re
    ne = []; npart = True
    for _, s_, l in L:
        if s_.get("part") != "hook": continue
        sp_ = " ".join(p.get("t", "") for p in l.get("phrases", []))
        for sent in [x for x in _re.split(r"(?<=[.!?])\s+", sp_) if _re.search(r"\w", _re.sub(r"\{[^}]*\}", "", x)) and len(_re.sub(r"\{[^}]*\}", "", x).split()) > 3]:
            if "{nhấn:" not in sent: ne.append(f"{s_['id']}: {sent[:40]}")
        if _re.search(r"(?<!\w)(luôn|á|nhỉ|nha|nè|hông|ha|đó)(?!\w)", sp_.lower()): npart = False
    (err if ne else ok)("L-031", f"hook sentence without {{nhấn:}} word: {ne}" if ne else "each hook sentence has an emphasis word")
    if npart: warn("L-031", "hook has no Southern sentence-final particle")
    # L-026 despair lines must not use a smiling/neutral face
    dz = [s["id"] for _, s, l in L if re.search(r"trời ơi|tuyệt vọng", (l.get("text") or "").lower()) and ((l.get("set") or {}).get(l["speaker"], {}).get("expression") or next((c.get("expression") for c in s.get("cast", []) if c["id"] == l["speaker"]), "")) not in ("sad", "despair")]
    (err if dz else ok)("L-026", f"despair line without sad/despair face: {dz}" if dz else "despair lines use sad/despair face")
    # L-017 voice markup (fillers / particles / hesitation) valid + density caps (voice-profile §3c)
    sys.path.insert(0, os.path.join(REPO, "pipeline/tts")); import markup as MK
    srcs = [(s["id"], " ".join(p.get("t", "") for p in l.get("phrases", [])) or l.get("say") or "") for _, s, l in L]
    badm = [f"{sid}: {b}" for sid, t in srcs for b in MK.validate(t)]
    (err if badm else ok)("L-017", f"invalid voice markup: {badm}" if badm else "voice markup valid")
    nob = []
    for _, s_, l in L:
        for f in re.findall(r"\{bank:\s*([^}]+)\}", " ".join(p.get("t", "") for p in l.get("phrases", []))):
            if not glob.glob(os.path.join(REPO, "pipeline/tts/filler-bank", l["speaker"], f.strip() + "-*.wav")): nob.append(f"{s_['id']}:{l['speaker']}/{f}")
    (err if nob else ok)("L-017", f"filler not in bank (F5 failed it for that voice; use inline {{…}} or another filler): {nob}" if nob else "bank fillers available")
    nk = sum(len(re.findall(r"\{kéo:", t)) for _, t in srcs)
    (warn if nk > 1 else ok)("L-018", f"{{kéo:}} used {nk}× (plain particles preferred by Hiệp; ≤ 1/clip)")
    per = [(sid, MK.count_fillers(t)) for sid, t in srcs]; tot = sum(n for _, n in per); cap = max(2, len(srcs) // 4)
    over = [f"{sid}:{n}" for sid, n in per if n > MK.MAX_FILLERS_LINE]
    (err if over or tot > cap else ok)("L-017", f"fillers {tot}/clip (cap {cap}), per line ≤ {MK.MAX_FILLERS_LINE}" + (f"; over: {over}" if over else ""))
    vis = [f"{s['id']}" for _, s, l in L if "{" in l.get("text", "") or "{" in l.get("en", "")]
    (err if vis else ok)("L-017", f"markup leaked into on-screen text/caption: {vis}" if vis else "no markup in on-screen text")
    raw_fill = [s["id"] for _, s, l in L if re.search(r"(?<!\w)(ừm|ờ|hừm|hmm)(?!\w)", " ".join(p.get("t", "") for p in l.get("phrases", [])).replace("{", " {"))
                and not re.search(r"\{(ừm|ờ|hừm|hmm|bank:[^}]+)\}", " ".join(p.get("t", "") for p in l.get("phrases", [])))]
    if raw_fill: warn("L-017", f"bare filler words (use {{ừm}} markup so they are counted/capped): {raw_fill}")
    # L-011 Omi week
    omi = any(l.get("speaker") == "omi" for _, _, l in L) or "\"omi\"" in json.dumps(spec)
    if omi and spec.get("week", 0) < 5: err("L-011", f"Omi present but week={spec.get('week')} < 5 (rule-11)")
    else: ok("L-011", "Omi/week consistent")
    # L-003 caption overlap (time); face-box overlap is fixed by layout, verified on contact sheet
    ov = []
    for pp in glob.glob(os.path.join(fdir, "plan-*.voiced.json")):
        for sc in json.load(open(pp))["scenes"]:
            segs = sorted((sc.get("caption") or {}).get("segments", []), key=lambda g: g["start"])
            ov += [f"{sc['id']}:{a['text'][:20]}|{b['text'][:20]}" for a, b in zip(segs, segs[1:]) if b["start"] < a["end"] - 0.01]
    (err if ov else ok)("L-003", f"caption segments overlap in time: {ov}" if ov else "caption segments never overlap")
    # L-014 HyperFrames lint evidence
    if any(p["engine"] == "hyperframes" for p in spec["parts"]):
        hf = os.path.join(fdir, "hf-check.txt"); txt = open(hf).read() if os.path.exists(hf) else ""
        (ok if re.search(r"\b0 errors?\b", txt) else (err if final else warn))("L-014", "hf-check.txt shows hyperframes lint 0 errors" if txt else "hf-check.txt missing (run build-final lint gate)")
    # L-007/L-008/L-009 voice audio per line
    if tpath and os.path.exists(tpath):
        vd = os.path.join(REPO, "video-engine/public/voice")
        for l in json.load(open(tpath))["lines"]:
            jp = os.path.join(vd, l["key"] + ".json"); wp = os.path.join(vd, l["key"] + ".wav")
            if not os.path.exists(jp): err("L-007", f"{l['scene']}: voice cache {l['key']} missing"); continue
            m = json.load(open(jp)); tag = f"{l['scene']}/{l['key']}"
            am = m
            if "F5" in m.get("engine", ""):
                pf = "per-phrase F5" in m["engine"] and m.get("emphasis_edits") is True and m.get("units")  # L-016 exception: voice-phrase-f5.py, one F5 call per '|' phrase, only {nhấn:} word stretch/pitch + stem end fall edits
                if pf:
                    ok("L-016", f"{tag}: per-phrase F5 units, cuts only for {{nhấn:}} emphasis edits (exception)"); ok("L-007", f"{tag}: F5 per-phrase generation")
                    am = m
                    continue
                v4 = re.search(r"voice-prosody v[45]", m["engine"]) and m.get("intra_output_cuts") == 0 and m.get("units")
                (ok if v4 else err)("L-016", f"{tag}: " + ("sentence/clause units, no cut inside any F5 output" if v4 else "F5 audio cut inside a model output (v2 collage / v3 word-cut) → rebuild with voice-prosody v4"))
                (ok if re.search(r"voice-prosody v[45]", m["engine"]) else err)("L-007", f"{tag}: F5 per-unit generation (whole clause per call)")
                if v4:
                    us = m["units"]
                    badu = [u["text"] for u in us[:-1] if not re.search(r"(\.\.\.|[.,?!…;:—)”\"])$", u["text"].strip())]
                    shortu = [u["text"] for u in us if len(norm(u["text"])) < 4 and len(us) > 1]
                    (err if badu or shortu else ok)("L-016", f"{tag}: {len(us)} unit(s)" + (f", split not at punctuation {badu}" if badu else "") + (f", unit < 4 syllables {shortu}" if shortu else ""))
                    f0 = [u["f0"] for u in us if u.get("f0")]
                    if len(f0) > 1:
                        spread = 12 * math.log2(max(f0) / min(f0)); (ok if spread <= 2.5 else err)("L-008", f"{tag}: timbre/F0 spread across units {spread:.1f} st (≤ 2.5)")
                    am = {"phrases": us}
            probs, clicks = audio_cuts(wp, am) if os.path.exists(wp) else (["wav missing"], [])
            (err if probs else ok)("L-008", f"{tag}: " + ("; ".join(probs) if probs else "edit points clean (no loud/mid-syllable cuts)"))
            if clicks: warn("L-008", f"{tag}: possible click(s) at {clicks[:5]}s — listen")
            hyp, ref = norm(m.get("stt", "")), norm(re.sub(r"\b[Oo]mi\b", "Ô mi", l.get("say", "")))  # Omi = 2 spoken syllables (O-mi)
            if hyp and ref:
                extra = (len(hyp) - len(ref)) / len(ref); rep = [hyp[i] for i in range(1, len(hyp)) if hyp[i] == hyp[i - 1] and not any(ref[k] == ref[k - 1] == hyp[i] for k in range(1, len(ref)))]
                bad = extra > 0.2 or extra < -0.25 or rep
                (err if bad else ok)("L-009", f"{tag}: STT {len(hyp)} vs {len(ref)} syllables" + (f", repeated {rep}" if rep else "") + ("" if not bad else " → re-roll/rewrite"))
    # L-013 push pending (warning only)
    r = subprocess.run(["git", "rev-list", "--count", "origin/main..HEAD"], cwd=REPO, capture_output=True, text=True)
    n = int(r.stdout.strip() or 0) if r.returncode == 0 else 0
    (warn if n else ok)("L-013", f"{n} commit(s) not pushed to origin (tell Hiệp; push when Mac online)" if n else "nothing pending push")

def report(outp):
    lines_ = [f"{a} {b:8} {c}" for a, b, c in res]
    ne = sum(1 for r in res if r[0] == "✖"); nw = sum(1 for r in res if r[0] == "⚠")
    lines_.append(f"\n{len(res)} checks · {ne} error(s) · {nw} warning(s) → {'FAIL' if ne else 'PASS'}")
    txt = "\n".join(lines_); print(txt)
    if outp: open(outp, "w").write(txt + "\n")
    return 1 if ne else 0

if __name__ == "__main__":
    sys.exit(main())
