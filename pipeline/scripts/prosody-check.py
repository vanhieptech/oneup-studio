#!/usr/bin/env python3
"""Prosody plan + measurement (clip-04 v14b, Hiệp 20/10: "ngắt nghỉ, nhấn nhá không hợp lý").
  python3 pipeline/scripts/prosody-check.py plan    <spec.json>   # final/prosody-plan.md (+.json): cụm theo ý, nghỉ mục tiêu, 1 từ nhấn/câu, câu hỏi lên giọng
  /workspace/asr-venv/bin/python pipeline/scripts/prosody-check.py measure <spec.json>  # final/prosody-measure.json/.md from the real voice wavs + timing.json
Targets: comma 0.15–0.25s, period/?/! 0.35–0.5s, colon 0.2–0.35s, between beats ≈0.5s (0.4–0.8), no pause >0.8s, no pause <0.1s at a period,
no break >0.25s at a boundary without punctuation (= ngắt giữa cụm từ). Pauses = silence runs (energy) between aligned words, so whisper's fuzzy
word edges only locate the boundary. Question rise = median F0 of the last word vs. the rest of the sentence (numpy autocorrelation)."""
import json, os, re, sys, subprocess, unicodedata, difflib
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TGT = {",": (0.15, 0.25), ".": (0.35, 0.5), "?": (0.35, 0.5), "!": (0.35, 0.5), ":": (0.2, 0.35), "line": (0.3, 0.6), "beat": (0.4, 0.8)}
MAX_PAUSE, MIN_PERIOD, MID_BREAK = 0.8, 0.1, 0.25
# one stressed word per sentence; {nhấn:} in the locked script wins, otherwise this map (key words chosen by meaning, not stretched by DSP)
STRESS = {"Ví dụ học từ tiếng Anh để đi du lịch.": "du lịch", "Tối đọc đi đọc lại.": "đọc đi đọc lại", "Tưởng mai nhớ hết.": "nhớ hết",
          "Sáng dậy, gấp sách viết lại.": "gấp sách", "airport, hotel, ticket, passport.": "passport", "Tới từ thứ năm, hành lý.": "hành lý",
          "Không nhớ từ tiếng Anh.": "Không nhớ", "Mình chột dạ.": "chột dạ", "Sau passport.": "passport", "Dừng ở đó.": "Dừng",
          "Gấp lại, viết tiếp.": "viết tiếp", "Hơn 48 ngàn học sinh.": "48 ngàn", "Lớp có kiểm nhỏ.": "kiểm nhỏ", "Điểm cao hơn mức vừa.": "mức vừa",
          "Dunlosky xếp mười cách.": "mười cách", "Đọc lại, gạch chân nằm nhóm thấp nhất.": "thấp nhất", "Vẫn có ích.": "có ích", "Tác dụng hẹp.": "hẹp",
          "Mỗi chồng mười thẻ.": "mười thẻ", "Học xong chồng đầu.": "chồng đầu", "Gấp sách, viết lại đúng chồng đó.": "đúng chồng đó",
          "Sáng hôm sau, quay lại giấy đó.": "giấy đó", "Sách vẫn gấp.": "vẫn gấp", "Sáng hôm sau tự viết được, không cần sách.": "không cần sách",
          "Bạn viết lại được mấy từ?": "mấy từ", "Comment con số đó nha.": "con số", "Không nhìn sách, bạn có thể nhớ được những gì?": "Không nhìn sách"}

# script-v14-delivery.md rev3: '/' phẩy/hai chấm 0.15–0.2 · '//' chấm/hỏi trong beat 0.35 · '//|' hết beat 0.4 · '///' lặng có chủ ý 0.4 (trước «Bút dừng»)
PLANS = {"A": {"/": 0.18, "//": 0.35, "//beat": 0.4, "///": 0.4}, "B": {"/": 0.15, "//": 0.3, "//beat": 0.4, "///": 0.4}, "C": {"/": 0.12, "//": 0.25, "//beat": 0.35, "///": 0.4}}
DELIV_GAP = {"/": (0.15, 0.2), "//": (0.35, 0.35), "//beat": (0.4, 0.4), "///": (0.4, 0.4)}
RESPELL = [("hai trăm hai mươi hai", "222"), ("bốn mươi tám ngàn", "48 ngàn"), ("Đun lốt ki", "Dunlosky"), ("Giang", "Yang"), ("Com men", "Comment"),
           ("Lắc ghịt", "Luggage"), ("lắc ghịt", "luggage"), ("e pọt", "airport"), ("hô ten", "hotel"), ("tích kịt", "ticket"), ("pát pọt", "passport")]
def unrespell(s):
    for a, b in RESPELL: s = s.replace(a, b)
    return s
def delivery_stream(fd):
    """[(word, mark_after)] over the whole clip from final/script-v14-delivery.md; mark in '', '/', '//', '//beat', '///'."""
    f = os.path.join(fd, "script-v14-delivery.md")
    if not os.path.exists(f): return None
    out = []
    for row in open(f).read().splitlines():
        if not re.match(r"\| b\d\d \|", row): continue
        cell = [x.strip() for x in row.replace("\\|", "¦").strip("|").split("|")][1].replace("**", "").replace("↗", " ").replace("↘", " ")
        for tok in re.findall(r"/{1,3}¦?|[\wÀ-ỹ]+", cell):
            if tok.startswith("/"):
                if out: out[-1] = (out[-1][0], "//beat" if tok.endswith("¦") else tok)
            else: out.append((tok, ""))
        if out and out[-1][1] == "//": out[-1] = (out[-1][0], "//beat")
    return out

def delivery_bold(fd):
    """bool per word of delivery_stream(): True if the word is inside **…** (the 1 stressed chunk per sentence)."""
    f = os.path.join(fd, "script-v14-delivery.md"); out = []
    for row in open(f).read().splitlines():
        if not re.match(r"\| b\d\d \|", row): continue
        cell = [x.strip() for x in row.replace("\\|", "¦").strip("|").split("|")][1]
        for i, part in enumerate(cell.split("**")):
            out += [i % 2 == 1] * len(re.findall(r"[\wÀ-ỹ]+", part.replace("↗", " ").replace("↘", " ")))
    return out

def fold(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn").replace("đ", "d")
def toks(s): return re.findall(r"[\wÀ-ỹ]+|[,.?!:]", s)
def sentences(text):
    t = re.sub(r"\*\*", "", text); return [x.strip() for x in re.findall(r"[^.?!]+[.?!]?", t) if x.strip()]
def all_lines(spec):
    for p in spec["parts"]:
        for s in p.get("scenes", []) + p.get("sections", []):
            for l in s["lines"]: yield p, s, l

def plan(specp):
    spec = json.load(open(specp)); fd = os.path.dirname(specp); rows = []; out = []
    for p, s, l in all_lines(spec):
        units = [re.sub(r"\{nhấn: ([^}]*)\}", r"\1", ph["t"]) for ph in l["phrases"]]
        nh = re.findall(r"\*\*([^*]+)\*\*", l["text"])
        for sen in sentences(l["text"]):
            st = next((w for w in nh if w in sen), None) or STRESS.get(sen) or next((v for k, v in STRESS.items() if sen in k or k in sen), "")
            rows.append({"scene": s["id"], "voice": l.get("voice_file", ""), "sentence": sen, "units": units, "stress": st,
                         "question_rise": sen.endswith("?"), "end_pause": "period .35–.5s" if sen[-1:] in ".?!" else "comma .15–.25s"})
    json.dump(rows, open(os.path.join(fd, "prosody-plan.json"), "w"), ensure_ascii=False, indent=1)
    md = ["# Prosody plan — " + spec["id"] + " (voice " + spec.get("voice_prefix", "") + ")", "",
          "Lời giữ nguyên script chốt. F5 không có SSML: nhấn = tách cụm (unit riêng) + nghỉ trước từ nhấn (+0.08s) + {nhấn:} giãn nhẹ; câu hỏi = nâng ~1.5 st từ cuối.",
          "Nghỉ mục tiêu: phẩy 0.15–0.25s · chấm/hỏi 0.35–0.5s · hai chấm 0.2–0.35s · giữa câu (dòng) 0.3–0.6s · giữa beat ~0.5s (0.4–0.8) · không nghỉ >0.8s · không ngắt giữa cụm (>0.25s ở chỗ không có dấu).", "",
          "| Beat | Câu | Cụm F5 (unit) | Từ nhấn | Câu hỏi lên giọng | Nghỉ cuối câu |", "|---|---|---|---|---|---|"]
    for r in rows: md.append(f"| {r['scene']} | {r['sentence']} | {' ‖ '.join(r['units'])} | **{r['stress']}** | {'có' if r['question_rise'] else '—'} | {r['end_pause']} |")
    open(os.path.join(fd, "prosody-plan.md"), "w").write("\n".join(md) + "\n"); print(f"{len(rows)} sentences → prosody-plan.md")

def arg(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d

def measure(specp):
    import numpy as np
    from faster_whisper import WhisperModel
    spec = json.load(open(specp)); fd = os.path.dirname(specp); T = json.load(open(arg("--timing", os.path.join(fd, "timing.json"))))
    od = arg("--out", fd); os.makedirs(od, exist_ok=True); DS = delivery_stream(fd); dpos = 0; DB = delivery_bold(fd) if DS else None
    FWD = [(b, a) for a, b in RESPELL]
    def respell(s):
        for a, b in FWD: s = re.sub(rf"\b{re.escape(a)}\b", b, s)
        return s
    m = WhisperModel("small", device="cpu", compute_type="int8"); SR = 16000; VO = os.path.join(REPO, "video-engine", "public", "voice")
    def pcm(f): return np.frombuffer(subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, dtype="float32")
    def silmask(x):
        hop = int(0.01 * SR); e = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)]); thr = max(0.012, 0.06 * np.percentile(e, 95)); return e < thr
    def longest_sil(mask, a, b):
        a, b = max(0, int(a * 100)), min(len(mask), int(b * 100)); best = cur = 0
        for v in mask[a:b]: cur = cur + 1 if v else 0; best = max(best, cur)
        return best / 100
    def edge(mask):
        i = 0
        while i < len(mask) and mask[i]: i += 1
        j = 0
        while j < len(mask) and mask[len(mask) - 1 - j]: j += 1
        return i / 100, j / 100
    def f0(x):
        hop = int(0.02 * SR); win = int(0.04 * SR); out = []
        for i in range(0, len(x) - win, hop):
            fr = x[i:i + win] - x[i:i + win].mean()
            if np.sqrt(np.mean(fr ** 2)) < 0.02: out.append(0); continue
            ac = np.correlate(fr, fr, "full")[win - 1:]; lo, hi = int(SR / 350), int(SR / 70); k = lo + int(np.argmax(ac[lo:hi]))
            out.append(SR / k if ac[k] > 0.3 * ac[0] else 0)
        return np.array(out)
    lines = T["lines"]; rows = []; flags = []
    for i, L in enumerate(lines):
        f = os.path.join(VO, L["key"] + ".wav"); x = pcm(f); mask = silmask(x); lead, trail = edge(mask)
        segs, _ = m.transcribe(x, language="vi", beam_size=5, word_timestamps=True, condition_on_previous_text=False)
        hw = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()]
        tt = toks(L["say"]); words = [t for t in tt if t not in ",.?!:"]; punct_after = {}
        ow = re.findall(r"[\wÀ-ỹ]+", unrespell(L["say"])); marks = None; bold = None
        if DS and dpos + len(ow) <= len(DS) and [fold(w) for w, _ in DS[dpos:dpos + len(ow)]] == [fold(w) for w in ow]:
            marks = [m_ for _, m_ in DS[dpos:dpos + len(ow)]]; bold = DB[dpos:dpos + len(ow)]; dpos += len(ow)
        elif DS: print("delivery alignment lost at", L["key"], flush=True); DS = None
        # orig word i -> respelled token range [cnt[i], cnt[i+1]) (e.g. «222» -> 5 tokens)
        cnt = [len(re.findall(r"[\wÀ-ỹ]+", respell(" ".join(ow[:i])))) for i in range(len(ow) + 1)]
        end2orig = {cnt[i + 1] - 1: i for i in range(len(ow)) if cnt[i + 1] > cnt[i]}
        wi = -1
        for t in tt:
            if t in ",.?!:": punct_after[wi] = t
            else: wi += 1
        sm = difflib.SequenceMatcher(None, [fold(re.sub(r"[^\w]", "", w[0])) for w in hw], [fold(w) for w in words], autojunk=False)
        mp = {}
        for a, b, n in sm.get_matching_blocks():
            for k in range(n): mp[b + k] = a + k
        bnds = []
        for k in range(len(words) - 1):
            if k in mp and k + 1 in mp:
                e0 = hw[mp[k]][2]; s1 = hw[mp[k + 1]][1]; mid0 = (hw[mp[k]][1] + e0) / 2; mid1 = (s1 + hw[mp[k + 1]][2]) / 2
                pz = longest_sil(mask, mid0, mid1); pu = punct_after.get(k)
                lo, hi = TGT.get(pu, (0, MID_BREAK)); st = "ok"
                if marks:  # delivery plan wins over punctuation (boundary inside a respelled word = no mark)
                    mk = marks[end2orig[k]] if k in end2orig else ""; pu = mk or None; lo, hi = DELIV_GAP.get(mk, (0, MID_BREAK))
                    if words[k + 1:k + 2] and L["key"].endswith("b03b") and mk == "/": lo, hi = 0.15, 0.22
                if pz > MAX_PAUSE: st = "✖ >0.8s"
                elif pu in (".", "//", "//beat", "///") and pz < MIN_PERIOD: st = "✖ chấm <0.1s"
                elif pu in (",", "/", ":") and pz < 0.12: st = "✖ phẩy dính (<0.12s)"
                elif pu in (",", "/") and pz > 0.27: st = "✖ phẩy dài hơn chấm (>0.27s)"
                elif not pu and pz > MID_BREAK: st = "✖ ngắt giữa cụm"
                elif pu and not (lo - 0.05 <= pz <= hi + 0.1): st = "⚠ lệch mục tiêu"
                bnds.append({"after": words[k], "punct": pu or "", "pause": round(pz, 2), "target": f"{lo}-{hi}" if pu else f"<{MID_BREAK}", "status": st})
        # pitch at question end
        rise = None
        if L["say"].rstrip().endswith("?") and hw:
            F = f0(x); t0 = hw[-1][1]; a = F[: int(t0 / 0.02)]; b = F[int(t0 / 0.02):]
            a, b = a[a > 0], b[b > 0]
            if len(a) and len(b): rise = round(float(12 * np.log2(np.median(b) / np.median(a))), 2)
        # emphasis (bold of delivery): mean dB of the stressed chunk vs the rest of the sentence (final syllable excluded)
        def dbr(a, b):
            seg = x[int(max(0, a) * SR):int(max(0, b) * SR)]; return 20 * np.log10(max(1e-5, float(np.sqrt(np.mean(seg ** 2))))) if len(seg) else None
        emph = []
        if bold and any(bold) and hw:
            toks_b = sorted({j for i_, b_ in enumerate(bold) if b_ for j in range(cnt[i_], cnt[i_ + 1])})
            ks = [k for k in toks_b if k in mp]
            if ks:
                a_, b_ = hw[mp[ks[0]]][1], hw[mp[ks[-1]]][2]; last = hw[-1][1]
                e_db = dbr(a_, b_); parts = [x[:int(a_ * SR)], x[int(b_ * SR):int(min(last, len(x) / SR) * SR)]] if b_ < last else [x[:int(a_ * SR)]]
                rest = np.concatenate(parts) if sum(len(z) for z in parts) else None
                r_db = 20 * np.log10(max(1e-5, float(np.sqrt(np.mean(rest ** 2))))) if rest is not None and len(rest) > SR * 0.1 else None
                emph.append({"words": " ".join(ow[i_] for i_, b_ in enumerate(bold) if b_), "delta_db": None if (e_db is None or r_db is None) else round(e_db - r_db, 1)})
        voiced_s = max(0.3, float((~mask[int(hw[0][1] * 100):int(hw[-1][2] * 100)]).sum()) * 0.01) if hw else None
        rate = round(len(words) / voiced_s, 2) if voiced_s else None
        nxt = lines[i + 1] if i + 1 < len(lines) else None
        gap = None
        if nxt:
            xn = pcm(os.path.join(VO, nxt["key"] + ".wav")); ln_, _ = edge(silmask(xn))
            gap = round(nxt["t"] - (L["t"] + L["dur"]) + trail + ln_, 2)
        kind = "beat" if nxt and nxt["scene"] != L["scene"] else "line"
        lmark = marks[-1] if marks else None
        TGT_ = {"line": DELIV_GAP[lmark], "beat": DELIV_GAP[lmark]} if lmark in DELIV_GAP else TGT
        gst = "ok" if gap is None else ("✖ >0.8s" if gap > MAX_PAUSE + (0.35 if kind == "beat" else 0) else "⚠ lệch mục tiêu" if not (TGT_[kind][0] - 0.05 <= gap <= TGT_[kind][1] + 0.1) else "ok")
        r = {"key": L["key"], "scene": L["scene"], "say": L["say"], "t": round(L["t"], 2), "dur": L["dur"], "stt": " ".join(w[0] for w in hw), "boundaries": bnds,
             "gap_after": gap, "gap_kind": kind, "gap_target": list(TGT_[kind]), "plan_mark": lmark, "gap_status": gst, "question_rise_st": rise,
             "rise_status": None if rise is None else ("ok" if rise >= 0.5 else "✖ không lên giọng")}
        r["emphasis"] = emph; r["syll_per_s"] = rate
        for e_ in emph:
            if e_["delta_db"] is not None and e_["delta_db"] < 2.0: flags.append(f"{L['key']}: nhấn «{e_['words']}» chỉ +{e_['delta_db']} dB (<2 dB)")
        if rate and rate > 5.0: flags.append(f"{L['key']}: {rate} âm tiết/s (>5)")
        r["stt_sim"] = round(difflib.SequenceMatcher(None, [fold(w) for w in re.findall(r"[\wÀ-ỹ]+", r["stt"])], [fold(w) for w in words]).ratio(), 2)
        rows.append(r)
        for b_ in bnds:
            if b_["status"].startswith("✖"): flags.append(f"{L['key']}: sau «{b_['after']}{b_['punct']}» nghỉ {b_['pause']}s ({b_['status']})")
        if gst.startswith("✖"): flags.append(f"{L['key']}→{nxt['key']}: nghỉ {gap}s ({gst})")
        if r["rise_status"] and r["rise_status"].startswith("✖"): flags.append(f"{L['key']}: câu hỏi cuối {rise} st ({r['rise_status']})")
        print(L["key"], gap, [(b_["after"], b_["pause"], b_["status"]) for b_ in bnds if b_["punct"] or b_["status"] != "ok"], rise, flush=True)
    res = {"voice_prefix": spec.get("voice_prefix"), "targets": TGT, "limits": {"max": MAX_PAUSE, "min_period": MIN_PERIOD, "mid_break": MID_BREAK}, "lines": rows, "flags": flags}
    json.dump(res, open(os.path.join(od, "prosody-measure.json"), "w"), ensure_ascii=False, indent=1)
    md = [f"# Prosody đo thật — {spec['id']} (voice {spec.get('voice_prefix')})", "", "Nghỉ = đoạn lặng dài nhất (năng lượng) giữa hai từ khớp; giữa câu/beat = khoảng lặng thật giữa hai file giọng theo timing.json. Lên giọng = trung vị F0 từ cuối so với phần trước (semitone).", "",
          "| Câu (key) | bắt đầu–kết thúc (s) | Chỗ ngắt theo plan: đo / mục tiêu | Ngắt giữa cụm | Nghỉ sau câu: đo / mục tiêu | Nhấn (đậm): dB so phần còn lại | Âm tiết/s | Câu hỏi lên giọng (st) | STT (sim) | Kết luận |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        pb = "; ".join(f"«{b['after']}{b['punct']}» {b['pause']}/{b['target']}{'' if b['status'] == 'ok' else ' ' + b['status']}" for b in r["boundaries"] if b["punct"]) or "—"
        mb = "; ".join(f"«{b['after']}» {b['pause']}s" for b in r["boundaries"] if not b["punct"] and b["status"] != "ok") or "không"
        g = "—" if r["gap_after"] is None else f"{r['gap_after']}/{r['gap_target'][0]}–{r['gap_target'][1]} ({'giữa beat' if r['gap_kind'] == 'beat' else 'giữa câu'}){'' if r['gap_status'] == 'ok' else ' ' + r['gap_status']}"
        bad = any(b["status"].startswith("✖") for b in r["boundaries"]) or r["gap_status"].startswith("✖") or (r["rise_status"] or "").startswith("✖")
        bad = bad or any((e_["delta_db"] or 9) < 2.0 for e_ in r["emphasis"]) or (r["syll_per_s"] or 0) > 5.0
        em = "; ".join(f"«{e_['words']}» {'+' if (e_['delta_db'] or 0) >= 0 else ''}{e_['delta_db']}" for e_ in r["emphasis"]) or "—"
        md.append(f"| {unrespell(r['say'])} ({r['key']}) | {r['t']}–{round(r['t'] + r['dur'], 2)} | {pb} | {mb} | {g} | {em} | {r['syll_per_s']} | {'—' if r['question_rise_st'] is None else r['question_rise_st']} | {r['stt']} ({r['stt_sim']}) | {'**ĐỌC LẠI**' if bad else 'ok'} |")
    md += ["", f"Cờ chặn: {len(flags)}"] + [f"- {x}" for x in flags]
    open(os.path.join(od, "prosody-measure.md"), "w").write("\n".join(md) + "\n"); print("flags", len(flags))

def voice(specp):
    """Assemble ONE voice-only file from picked F5 units (W/<unit>.npy, 48k) with the delivery-plan pauses: final/voice-only-<prefix>.wav (-14 LUFS),
    final/voice-only-<prefix>.timing.json (timing.json line format, feeds measure --timing) and --m4a (AAC mono 96k)."""
    import numpy as np
    spec = json.load(open(specp)); fd = os.path.dirname(specp); W = arg("--work"); SR = 48000; pre = spec.get("voice_prefix")
    U = json.load(open(os.path.join(W, "units.json"))); DS = delivery_stream(fd); dpos = 0; marks = []
    USTT = json.load(open(os.path.join(W, "units-stt.json"))) if os.path.exists(os.path.join(W, "units-stt.json")) else {}
    if not DS: sys.exit("script-v14-delivery.md missing: the plan defines the pauses")
    def edges(x, thr=0.01):
        i = np.where(np.abs(x) > thr)[0]; return (i[0] / SR, (len(x) - i[-1]) / SR) if len(i) else (0, 0)
    sid = {}
    for p in spec["parts"]:
        for s in p.get("scenes", []) + p.get("sections", []):
            for li, l in enumerate(s["lines"]): sid[s["id"] + ("abcdef"[li] if len(s["lines"]) > 1 else "")] = (s["id"], l)
    out = []; t = 0.0; lines = {}; prev_tail = 0.0; prev_key = ""
    for u in U:
        x = np.load(os.path.join(W, u["key"] + ".npy")).astype("float32"); lead, tail = edges(x)
        ug = USTT.get(u["key"], {}).get("unit_gain_db", 0.0)
        if ug: x = x * np.float32(10 ** (ug / 20))  # stressed chunk = whole unit (e.g. «Bút dừng», «không cần sách»): gain vs the rest of its sentence
        ow = re.findall(r"[\wÀ-ỹ]+", unrespell(u["t"])); seg = DS[dpos:dpos + len(ow)]
        if [fold(w) for w, _ in seg] != [fold(w) for w in ow]: sys.exit(f"delivery/unit mismatch at {u['key']}: {ow} vs {[w for w, _ in seg]}")
        dpos += len(ow)
        if out:
            g = PLANS[arg("--plan", "A")].get(marks[-1], 0.0)
            if marks[-1] == "/" and prev_key.startswith("b03b"): g = 0.2  # 4 EN words: clear 0.2s each (pacing-v14.md #4)  # no mark = inside one clause: butt-join (only F5's own edge silence)
            pad = max(0.0, g - prev_tail - lead); out.append(np.zeros(int(pad * SR), "float32")); t += pad
        st = t; out.append(x); t += len(x) / SR; prev_tail = tail; marks.append(seg[-1][1]); prev_key = u["key"]
        ln = u["line"]; sc, l = sid[ln]
        L = lines.setdefault(ln, {"key": f"{pre}-{ln}", "scene": sc, "say": l["say"], "t": round(st + lead, 3), "units": []})
        L["dur"] = round(t - tail - L["t"], 3); L["units"].append({"key": u["key"], "t": round(st + lead, 3), "end": round(t - tail, 3), "mark_after": seg[-1][1]})
    y = np.concatenate(out); raw = os.path.join(W, "voice-only-raw.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", raw], input=y.tobytes(), check=True)
    wav = os.path.join(fd, f"voice-only-{pre}.wav"); m4a = arg("--m4a", f"/workspace/{spec['clip']}-v14-voice-only.m4a")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "1", wav], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "aac", "-b:a", "96k", "-ac", "1", "-movflags", "+faststart", m4a], check=True)
    for L in lines.values():  # per-line wav cut from the assembled file so measure() reads it like a normal voice line
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-ss", str(max(0, L["t"] - 0.06)), "-t", str(L["dur"] + 0.16), os.path.join(REPO, "video-engine/public/voice", L["key"] + ".wav")], check=True)
        L["t"] = round(L["t"] - 0.06, 3); L["dur"] = round(L["dur"] + 0.16, 3)
    json.dump({"total": round(len(y) / SR, 3), "lines": list(lines.values())}, open(os.path.join(fd, f"voice-only-{pre}.timing.json"), "w"), ensure_ascii=False, indent=1)
    print("voice-only", round(len(y) / SR, 2), "s ->", wav, m4a)

if __name__ == "__main__":
    {"plan": plan, "measure": measure, "voice": voice}[sys.argv[1]](os.path.abspath(sys.argv[2]))
