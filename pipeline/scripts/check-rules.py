#!/usr/bin/env python3
"""Rule linter for one clip (rule-48). Lints the clip spec (+ script, plan, MP4, post) against rules/video-rules.md.

  check-rules.py content/clips/<clip>/            # gate 1: spec + script + post (if any) + plan validation
  check-rules.py content/clips/<clip>/ --final    # gate 2: also the rendered MP4 (ffprobe, loudness) + post.md required
  check-rules.py ... --stt                        # also STT every voice line and compare with the text (slow, ~1 min)
  check-rules.py ... --out report.txt

Source: <clip>/final/spec.json (format: see skills/make-video/SKILL.md). Exit 1 if any ✖ error. Also runs the lessons gate (rule-49, logs/lessons.md): checks named L-NNN.
"""
import json, os, re, subprocess, sys, difflib, unicodedata, glob, math

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65
REPO = str(P.ROOT)
NODE_BIN = os.environ.get("NODE22_BIN", "/workspace/tools/node-v22.20.0-linux-x64/bin")
ASR_PY = os.environ.get("ASR_PYTHON", "/workspace/asr-venv/bin/python")
res = []
def ok(rule, msg): res.append(("✔", rule, msg))
def warn(rule, msg): res.append(("⚠", rule, msg))
def err(rule, msg): res.append(("✖", rule, msg))

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

def main():
    a = sys.argv[1:]; clip_dir = os.path.abspath(a[0]); final = "--final" in a; do_stt = "--stt" in a
    outp = a[a.index("--out") + 1] if "--out" in a else None
    specp = os.path.join(clip_dir, "final", "spec.json")
    if not os.path.exists(specp) and os.path.exists(os.path.join(clip_dir, "spec.json")): specp = os.path.join(clip_dir, "spec.json")  # samples
    if not os.path.exists(specp): err("rule-48", f"missing {os.path.relpath(specp, REPO)} (source of truth for the clip)"); return report(outp)
    if "/content/archive/" in os.path.abspath(specp).replace(os.sep, "/") + "/":
        print(f"skip: {specp} is archived (rule-66); check-assets verifies its post package"); sys.exit(0)
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
                if s.get("part") in ("evidence",): warn("rule-42", f"{s['id']}: evidence beat in comic; should be motion graphics")
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
    # final MP4
    mp4 = os.path.join(fdir, "out", spec["id"] + ".mp4")
    if final:
        if not os.path.exists(mp4): err("rule-4", f"missing {os.path.relpath(mp4, REPO)}")
        else:
            j = ffprobe(mp4); v = [s for s in j["streams"] if s["codec_type"] == "video"][0]; au = [s for s in j["streams"] if s["codec_type"] == "audio"]
            d = float(j["format"]["duration"])
            LX = spec.get("length_exception")
            (ok if 55 <= d <= 60.5 else (warn if d > 60.5 else err))("rule-4", f"MP4 {d:.2f}s" + (f" · exception {LX}" if LX and d > 60.5 else ""))
            spec_ok = v["width"] == 1080 and v["height"] == 1920 and v["r_frame_rate"] == "30/1" and v["codec_name"] == "h264" and v.get("profile") == "High" and v["pix_fmt"] == "yuv420p" and v.get("color_space") == "bt709"
            (ok if spec_ok else err)("rule-4", f"video {v['width']}×{v['height']} {v['r_frame_rate']} {v['codec_name']} {v.get('profile')} {v['pix_fmt']} {v.get('color_space')}")
            if not au: err("rule-46", "MP4 has no audio track")
            else:
                m = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
                li = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", m)[-1]); pk = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)[-1])
                (ok if abs(li + 14) <= 1.0 and pk <= -0.5 else err)("rule-4", f"audio {au[0]['codec_name']} {au[0]['sample_rate']} Hz, {li} LUFS, peak {pk} dBFS (target −14 ±1, peak ≤ −0.5)")
            (ok if os.path.exists(os.path.join(fdir, "contact-sheet.png")) else err)("rule-34", "contact-sheet.png for frame review")
    # STT
    if do_stt and tpath and os.path.exists(tpath):
        t = json.load(open(tpath)); wavs = [os.path.join(REPO, "video-engine/public/voice", l["key"] + ".wav") for l in t["lines"]]
        r = subprocess.run([ASR_PY, os.path.join(REPO, "pipeline/tts/stt_check.py"), *wavs], capture_output=True, text=True)
        got = {x.split(" | ")[0]: x.split(" | ", 1)[1] for x in r.stdout.splitlines() if " | " in x}
        for l in t["lines"]:
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
    elif not os.path.exists(tsp): warn("rule-57", "final/trend-signals.md missing")
    else:
        ts = open(tsp, encoding="utf8").read()
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
