#!/usr/bin/env python3
"""Rule linter for one clip (rule-48). Lints the clip spec (+ script, plan, MP4, post) against rules/video-rules.md.

  check-rules.py content/clips/<clip>/            # gate 1: spec + script + post (if any) + plan validation
  check-rules.py content/clips/<clip>/ --final    # gate 2: also the rendered MP4 (ffprobe, loudness) + post.md required
  check-rules.py ... --stt                        # also STT every voice line and compare with the text (slow, ~1 min)
  check-rules.py ... --out report.txt

Source: <clip>/final/spec.json (format: see skills/make-video/SKILL.md). Exit 1 if any ✖ error. Also runs the lessons gate (rule-49, logs/lessons.md): checks named L-NNN.
"""
import json, os, re, subprocess, sys, difflib, unicodedata, glob, math

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
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
    spec = json.load(open(specp)); fdir = os.path.dirname(specp)
    prof = {}
    for f in glob.glob(os.path.join(REPO, "video-engine/src/characters/profiles/*.json")):
        j = json.load(open(f)); prof[j["id"]] = j
    L = list(lines(spec))
    clip_no = int(re.findall(r"\d+", spec.get("clip", "clip-0"))[0])
    tm_week, tm_theme = theme_map(clip_no)

    # rule-4 / rule-9 length + pacing
    tpath = os.path.join(fdir, "timing.json")
    if os.path.exists(tpath):
        t = json.load(open(tpath)); total = t.get("total", 0)
        LX = spec.get("length_exception")  # DL-041: Hiệp-approved info-dense exception, ≤70s, flagged as warning
        (ok if 55 <= total <= 60.5 else (warn if LX and total <= 70 else err))("rule-4", f"planned length {total:.1f}s (target 55–60s)" + (f" · exception {LX}" if LX and total > 60.5 else ""))
        bt = {}
        for l in t["lines"]: bt.setdefault(l["scene"], []).append(l)
        for sid, ls in bt.items():
            span = ls[-1]["local"] + ls[-1]["dur"] - ls[0]["local"]
            if span > 8.5: warn("rule-9", f"{sid}: voice spans {span:.1f}s in one shot (max ~8s per scene)")
    else:
        est = sum(len(l["text"].split()) for _, _, l in L) / 2.9
        (ok if 52 <= est <= 62 else warn)("rule-4", f"no timing.json yet; estimated {est:.0f}s from word count")
    words = sum(len((l.get("say") or l["text"]).split()) for _, _, l in L)
    (ok if 140 <= words <= 175 else warn)("rule-7", f"{words} VI words (target ~150–170)")
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
    VOICES = {"omi": ("f5-tts", "F5 · Mỹ Duyên", "pipeline/tts/f5-refs/my-duyen.wav"), "hiep": ("f5-tts", "F5 · Thái Sơn", "pipeline/tts/f5-refs/thai-son.wav")}
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
    # final MP4
    mp4 = os.path.join(fdir, "out", spec["id"] + ".mp4")
    if final:
        if not os.path.exists(mp4): err("rule-4", f"missing {os.path.relpath(mp4, REPO)}")
        else:
            j = ffprobe(mp4); v = [s for s in j["streams"] if s["codec_type"] == "video"][0]; au = [s for s in j["streams"] if s["codec_type"] == "audio"]
            d = float(j["format"]["duration"])
            LX = spec.get("length_exception")
            (ok if 55 <= d <= 60.5 else (warn if LX and d <= 70 else err))("rule-4", f"MP4 {d:.2f}s" + (f" · exception {LX}" if LX and d > 60.5 else ""))
            spec_ok = v["width"] == 1080 and v["height"] == 1920 and v["r_frame_rate"] == "30/1" and v["codec_name"] == "h264" and v.get("profile") == "High" and v["pix_fmt"] == "yuv420p" and v.get("color_space") == "bt709"
            (ok if spec_ok else err)("rule-4", f"video {v['width']}×{v['height']} {v['r_frame_rate']} {v['codec_name']} {v.get('profile')} {v['pix_fmt']} {v.get('color_space')}")
            if not au: err("rule-46", "MP4 has no audio track")
            else:
                m = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
                li = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", m)[-1]); pk = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", m)[-1])
                (ok if abs(li + 14) <= 1.0 and pk <= -0.5 else err)("rule-4", f"audio {au[0]['codec_name']} {au[0]['sample_rate']} Hz, {li} LUFS, peak {pk} dBFS (target −14 ±1, peak ≤ −0.5)")
            (ok if os.path.exists(os.path.join(fdir, "contact-sheet.png")) else err)("rule-34", "contact-sheet.png for frame review")
    # STT
    if do_stt and os.path.exists(tpath):
        t = json.load(open(tpath)); wavs = [os.path.join(REPO, "video-engine/public/voice", l["key"] + ".wav") for l in t["lines"]]
        r = subprocess.run([ASR_PY, os.path.join(REPO, "pipeline/tts/stt_check.py"), *wavs], capture_output=True, text=True)
        got = {x.split(" | ")[0]: x.split(" | ", 1)[1] for x in r.stdout.splitlines() if " | " in x}
        for l in t["lines"]:
            hyp = got.get(l["key"] + ".wav", ""); sim = difflib.SequenceMatcher(None, norm(l["say"]), norm(hyp)).ratio()
            (ok if sim >= 0.75 else warn if sim >= 0.55 else err)("rule-46", f"STT {l['scene']} {sim:.2f}: “{hyp}”")
    # rule-50 (DL-042): every transition has an SFX + continuous ambience bed
    if final and os.path.exists(tpath):
        tj = json.load(open(tpath)); tr = tj.get("transitions"); mixs = tj.get("sfx_mix", [])
        if not tr: err("rule-50", "timing.json has no transitions list (build-final ≥ DL-042 writes it)")
        else:
            src = open(os.path.join(REPO, "assets/sfx/SOURCES.md")).read()
            miss = [t for t in tr if not any(m["name"] == t["sfx"] and abs(m["at"] - t["at"]) <= 0.3 for m in mixs)]
            (ok if not miss else err)("rule-50", f"{len(tr)} transitions, {len(tr) - len(miss)} with SFX" + (f"; missing at {[t['at'] for t in miss]}" if miss else ""))
            (ok if any(m["name"] == "ambience" for m in mixs) else err)("rule-50", "ambience bed under whole clip")
            for n in sorted({m["name"] for m in mixs}):
                if n not in src: err("rule-22", f"sfx '{n}' missing in assets/sfx/SOURCES.md")
    # rule-51 (DL-043): every explainer section has ≥1 marked hit with an accent SFX, mixed at the hit time
    if final and os.path.exists(tpath):
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
    if os.path.exists(tpath):
        vd = os.path.join(REPO, "video-engine/public/voice")
        for l in json.load(open(tpath))["lines"]:
            jp = os.path.join(vd, l["key"] + ".json"); wp = os.path.join(vd, l["key"] + ".wav")
            if not os.path.exists(jp): err("L-007", f"{l['scene']}: voice cache {l['key']} missing"); continue
            m = json.load(open(jp)); tag = f"{l['scene']}/{l['key']}"
            am = m
            if "F5" in m.get("engine", ""):
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
            hyp, ref = norm(m.get("stt", "")), norm(l.get("say", ""))
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
