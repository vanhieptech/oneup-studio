#!/usr/bin/env python3
"""Rule linter for one clip (rule-48). Lints the clip spec (+ script, plan, MP4, post) against rules/video-rules.md.

  check-rules.py content/clips/<clip>/            # gate 1: spec + script + post (if any) + plan validation
  check-rules.py content/clips/<clip>/ --final    # gate 2: also the rendered MP4 (ffprobe, loudness) + post.md required
  check-rules.py ... --stt                        # also STT every voice line and compare with the text (slow, ~1 min)
  check-rules.py ... --out report.txt

Source: <clip>/final/spec.json (format: see skills/make-video/SKILL.md). Exit 1 if any ✖ error.
"""
import json, os, re, subprocess, sys, difflib, unicodedata, glob

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
SFX_OK = {"pop", "ding", "whoosh", "tick", "click"}

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
        (ok if 55 <= total <= 60.5 else err)("rule-4", f"planned length {total:.1f}s (target 55–60s)")
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
            (ok if 55 <= d <= 60.5 else err)("rule-4", f"MP4 {d:.2f}s")
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
    return report(outp)

def report(outp):
    lines_ = [f"{a} {b:8} {c}" for a, b, c in res]
    ne = sum(1 for r in res if r[0] == "✖"); nw = sum(1 for r in res if r[0] == "⚠")
    lines_.append(f"\n{len(res)} checks · {ne} error(s) · {nw} warning(s) → {'FAIL' if ne else 'PASS'}")
    txt = "\n".join(lines_); print(txt)
    if outp: open(outp, "w").write(txt + "\n")
    return 1 if ne else 0

if __name__ == "__main__":
    sys.exit(main())
