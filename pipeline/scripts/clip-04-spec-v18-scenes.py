"""clip-04 v18 scenes → final/spec.json (imported by clip-04-mkspec-v18.py spec). Follows final/script-v18-table.md,
final/visual-plan-v18.md (FLUX 6770a3f) and research/agents/short-factory-clip04-v18-review-vi.md. Times are scene-local seconds,
taken from the measured word times of the approved voice (slices.json)."""
import json, os, re, importlib
MK = importlib.import_module("clip-04-mkspec-v18")
D, WORK, P = MK.D, MK.WORK, MK.P
S = json.load(open(WORK + "slices.json")); LN = {L[0]: L for L in MK.LINES}

# ---------- scene table ----------
SC = []  # filled below
def line(lid, anchor=None):
    L = LN[lid]; s = S[lid]
    say = re.sub(r"\*\*", "", L[3])
    ph = re.sub(r"\*\*([^*]+)\*\*", r"{nhấn: \1}", L[3])
    d = {"speaker": "hiep", "emotion": L[6], "text": L[3], "say": say, "en": L[4], "hl": L[5], "bubble": L[7], "voice_role": "Thầy",
         "voice_file": f"voice/{s['key']}.wav", "cap": s["cap"], "chunk": L[1]}
    if lid != "c01a": d["phrases"] = [{"t": ph}]  # c01a = first clause of chunk c01 (one F5 take); phrases on c01b carry the chunk's {nhấn:}
    if anchor: d["anchor"] = anchor
    return d

class Scene:
    def __init__(s, id, beat, part, lids, bg, framing="medium"):
        s.id, s.beat, s.part, s.lids, s.bg, s.framing = id, beat, part, lids, bg, framing
        s.off = {}; t = 0
        for l in lids: s.off[l] = t; t += S[l]["dur"]
        s.dur = round(t, 4)
    def W(s, lid, word, n=1, end=False):
        """scene-local time of the n-th token `word` (STT spelling) in line lid"""
        k = 0
        for w, a, b in S[lid]["tok"]:
            if w == word:
                k += 1
                if k == n: return round(s.off[lid] + max(0.0, b if end else a), 3)
        raise KeyError((lid, word, n))
    def L0(s, lid): return s.off[lid]

# ---------- shared objects (design px) ----------
def WIN(sky, cu=False, **kw): return {"kind": "window", "x": 0, "y": 0, "sky": sky, **({"wx": 70, "wy": 560, "ww": 220, "wh": 200} if cu else {"wx": 660, "wy": 250, "ww": 300, "wh": 250}), **kw}
TABLE = {"kind": "table", "x": 0, "y": 0, "top": 1395}
def TOME(keys, room=True, flips=None, **kw):
    open_ = keys[0][1] == "open"
    pos = {"x": 205, "y": 1300, "s": 0.55, "closedDy": 160} if room else {"x": 200, "y": 1405, "s": 0.6}  # closedDy: a shut book lies flat on the table top
    return {"kind": "tome", **pos, "keys": keys, **({"flips": flips} if flips else {}), **kw}
def SHEET(rows=(), cu=False, **kw):
    return {"kind": "paper", **({"x": 600, "y": 1070, "s": 1.1} if cu else {"x": 480, "y": 1265, "s": 0.45}), "rows": [list(r) for r in rows], **kw}
def ROWY(i, cu=False): return (1070 + 1.1 * (-232 + 50 * i)) if cu else (1265 + 0.45 * (-232 + 50 * i))
def ROWX(cu=False): return (437, 760) if cu else (413, 540)
def PEN(keys, rot=24, cu=False): return {"kind": "pen", "x": 0, "y": 0, "s": 1, "rot": rot, "len": 230 if cu else 150, "keys": keys}
PEN_REST = PEN([[0, 585, 1420]], rot=8)
PEN_REST_CU = PEN([[0, 790, 1330]], rot=28, cu=True)
def CARD(**kw): return dict({"kind": "card", "x": 905, "y": ROWY(4, True), "s": 0.6, "shadow": 0.3}, **kw)  # light theme: suitcase shadow boosted for contrast
def C(ex="focused", act="talking", facing="left"): return {"id": "hiep", "x": 0.76, "facing": facing, "pose": "sitting", "action": act, "expression": ex}
def SFX(n, lid, word, sc, nn=1, off=0.0):
    li = sc.lids.index(lid); return {"name": n, "atLine": li, "offset": round(sc.W(lid, word, nn) - sc.L0(lid) + off, 3), "word": WORDS.get((lid, word), word)}
WORDS = {("c13", "giang"): "Yang", ("c16a", "lắc"): "luggage", ("c17b", "com"): "Comment"}
def TAG(text, x, y, at, until=None, **kw): return dict({"kind": "tag", "text": text, "x": x, "y": y, "at": at}, **({"until": until} if until is not None else {}), **kw)
CU_ANCHOR = [600, 560]

def build():
    out = []
    def add(sc, cast, props, sfx, fx, stage, link=None, push=0.04, narration=None, mg=None):
        lines = [line(l, CU_ANCHOR if (not cast and LN[l][7]) else None) for l in sc.lids]
        if cast:
            for l in lines: l["set"] = {"hiep": {"expression": {"neutral": "neutral"}.get(l["emotion"], l["emotion"])}}
        d = {"id": sc.id, "beat": f"clip-04.{sc.beat}", "part": sc.part, "role": "Thầy", "background": sc.bg, "framing": sc.framing, "push": push, "transition": "cut",
             "cast": cast, "fx": {"visual": fx[0], "word": fx[1]}, "sfx": sfx, "props": props, "lines": lines, "stage": {"action": stage[0], "react": stage[1]}, "dur": sc.dur}
        if link: d["link"] = link
        if narration: d["narration"] = narration
        if mg: d["mg"] = mg; d["push"] = 0
        out.append(d)

    # b01 hook, shot 1: close-up blank sheet, night→sun, faint rows of last night evaporate, pen drops + snap
    s = Scene("b01a", "b01", "hook", ["c01a", "c01b"], "paper", "closeup")
    add(s, [], [WIN([[0, "night"], [s.W("c01b", "sáng"), "day"]], cu=True), TOME([[0, "closed"]], room=False),
                SHEET([(0, -1), (1, -1), (2, -1)], cu=True, dimRows=True, fadeAt=s.W("c01b", "quên")),
                PEN([[0, 760, 520], [0.08, 760, 520], [0.34, 772, 1300]], rot=28, cu=True)],
        [{"name": "snap", "atLine": 0, "offset": 0.34, "word": "Học thuộc"}],
        ("mmx-cut-on-motion: pen drops onto the blank sheet + snap; last night's faint rows evaporate at 'quên sạch'; window moon→sun", "quên sạch"),
        ("Pen drops on a blank 10-row sheet; faint rows fade; moon in the window becomes a rising sun", "shock, direct pain"), push=0.08,
        narration="HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?")
    # b01 hook, shot 2: medium, morning, book closed, blank sheet; tick at 'không nhìn sách' (book slides away)
    s = Scene("b01b", "b01", "hook", ["c02"], "room")
    tk = s.W("c02", "không")
    add(s, [C("surprised", "reacting")], [WIN([[0, "day"]]), TABLE, dict(TOME([[0, "closed"]]), mv=[[0, 205, 1300], [tk, 205, 1300], [tk + 0.35, 140, 1312]]), SHEET(), PEN_REST],
        [SFX("tick", "c02", "không", s)],
        ("mmx-snap: closed book slides away from the blank sheet at 'không nhìn sách', face turns to the camera asking", "không nhìn sách"),
        ("Book pushed aside, blank sheet in front, morning sun in window", "unsure, asking the viewer"), link="hook question right after the pain line (same morning)")

    # b02 example: night, book open, pages flip back and forth twice
    s = Scene("b02a", "b02", "struggle", ["c03"], "room")
    add(s, [C("happy", "talking")], [WIN([[0, "night"]]), TABLE, TOME([[0, "open"]], flips=[s.W("c03", "đọc", 1), s.W("c03", "đọc", 2)])],
        [SFX("swish", "c03", "đọc", s, 1, -0.02)],
        ("mmx-cruise: at night (moon) the open book flips back and forth twice, confident nod", "thuộc làu"),
        ("Rereads the open book at night, pages flip twice", "confident"), link="the hook's 'last night' told as my own example")
    # b02 morning: cut on motion, sun rises, book closes, pen writes 4 rows
    s = Scene("b02b", "b02", "struggle", ["c04"], "room")
    vt = s.W("c04", "viết"); x0, x1 = ROWX()
    pk = [[0, 585, 1420], [vt - 0.25, 585, 1420], [vt, x0, ROWY(0)]]
    for i in range(4): pk += [[vt + i * 0.17 + 0.15, x1, ROWY(i)], [vt + i * 0.17 + 0.17, x0, ROWY(i + 1)]]
    add(s, [C("focused", "typing")], [WIN([[0, "night"], [0.05, "day"]]), TABLE, TOME([[0, "open"], [s.W("c04", "gấp"), "closed"]]),
                                       SHEET([(i, vt + i * 0.17) for i in range(4)]), PEN(pk[:-1], rot=20)],
        [SFX("pen", "c04", "viết", s)],
        ("mmx-cut-on-motion: sun rises, book snaps shut at 'gấp sách', pen writes four rows on the sheet", "viết thử"),
        ("Closes the book and writes from memory", "focused"), link="next morning of the same night, the closed-book test")
    # b02 stuck: close-up, pen stops at row 5, face-down card with a faint suitcase shadow
    s = Scene("b02c", "b02", "struggle", ["c05"], "paper", "closeup")
    x0, x1 = ROWX(True); stop = s.W("c05", "thứ")
    add(s, [], [WIN([[0, "day"]], cu=True), TOME([[0, "closed"]], room=False), SHEET([(i, -1) for i in range(4)], cu=True, focus={"row": 4, "at": stop}),
                CARD(at=s.W("c05", "hành"), shakeAt=s.W("c05", "bí")), PEN([[0, x1, ROWY(3, True) + 20], [stop, x0 + 8, ROWY(4, True) + 4]], rot=26, cu=True)],
        [SFX("pen", "c05", "tới", s, 1, 0.05), SFX("tick", "c05", "bí", s)],
        ("mmx-snap-settle: close-up, pen stops dead on empty row 5; a face-down card with a faded suitcase shadow appears, shakes at 'bí'", "bí"),
        ("Pen stops at row 5; face-down card shows only a faint suitcase shadow", "stuck, deflated"), push=0.06, link="the exact word where that morning test broke")

    # b03 cause + evidence → HyperFrames motion-graphic plate (rule-42): final/mg-b03 (pipeline/scripts/clip-04-mg-v18.py),
    # rendered to video-engine/public/mg/c04v18-b03.mp4; Remotion only overlays captions + the study credit + «+2 ngày» tag.
    MG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content/clips/clip-04-gap-sach-tu-kiem/final/mg-v18.json")))
    PL = lambda name, frm: {"kind": "plate", "x": 0, "y": 0, "src": f"mg/c04v18-{name}.mp4", "from": round(frm, 4)}
    CR = lambda at: TAG("Roediger & Karpicke 2006", 540, 1330, at)
    s = Scene("b03a", "b03", "evidence", ["c06"], "plate"); t3 = 0.0
    add(s, [], [PL("b03", t3), CR(s.W("c06", "thí"))],
        [SFX("ding", "c06", "năm", s, 1)],
        ("hf-motion-graphic: split frame, reread book left vs closed-book sheet right, baseline draws; study credit tag", "2006"),
        ("Two columns: open book vs closed-book sheet", "curious"), link="why the morning test broke: a 2006 experiment", mg="mg-b03")
    t3 += s.dur
    s = Scene("b03b", "b03", "evidence", ["c07"], "plate")
    add(s, [], [PL("b03", t3), CR(-1)],
        [SFX("pop", "c07", "tốt", s)],
        ("hf-motion-graphic: two bars rise at 'kiểm tra ngay', reread bar a bit taller, thumbs-up pops on it at 'tốt hơn'", "kiểm tra ngay"),
        ("Bars: reread a bit taller when tested at once", "fair, admits rereading helps first"), link="the experiment's first result", mg="mg-b03")
    t3 += s.dur
    s = Scene("b03c", "b03", "evidence", ["c08"], "plate")
    r2 = MG["mg-b03"]["rise2"] - t3
    add(s, [], [PL("b03", t3), CR(-1), TAG("+2 ngày", 830, 300, r2, style="word", size=52)],
        [SFX("rise", "c08", "tự", s, 1, -0.17)],
        ("hf-motion-graphic: window moon → sunrise → sunset → 2nd sunrise; at the 2nd sunrise «+2 ngày» tag and the bars swap (self-test clearly taller), thumbs-up droops", "hai ngày sau"),
        ("Two sunrises; reread bar shrinks, self-test bar grows past it; no numbers", "surprised reversal"), link="but two days later the result flips", mg="mg-b03")

    # b04 goal: back to the sheet, push into empty row 5 with a dotted suitcase outline
    s = Scene("b04", "b04", "intro", ["c09"], "paper", "closeup")
    add(s, [], [WIN([[0, "night"], [s.W("c09", "sáng"), "day"]], cu=True), TOME([[0, "closed"]], room=False),
                SHEET([(i, -1) for i in range(4)], cu=True, focus={"row": 4, "at": s.W("c09", "sáng")}, ghost={"row": 4, "at": s.W("c09", "viết")}), PEN_REST_CU],
        [SFX("tick", "c09", "viết", s)],
        ("mmx-push-in: slow push into empty row 5 of the same sheet; sun rises; dotted suitcase outline appears at 'viết ra được'", "sáng hôm sau"),
        ("Same sheet, empty row 5 gets a dotted suitcase outline", "calm, clear goal"), push=0.18, link="goal set right on the empty row that broke")

    # b05 how-to: 30 cards → 3 stacks, write each part with the book closed, open only when stuck
    DK = {"kind": "deck", "x": 390, "y": 1350, "s": 0.5}
    BK5 = {"x": 140, "y": 1362, "s": 0.45, "closedDy": 84}
    s = Scene("b05a", "b05", "payoff", ["c10"], "room")
    add(s, [C("focused", "talking")], [WIN([[0, "day"]]), TABLE, TOME([[0, "closed"]], **BK5), dict(DK, spillAt=s.W("c10", "ba", 1), splitAt=s.W("c10", "ba", 2))],
        [SFX("pop", "c10", "ba", s, 2)],
        ("tdev-stagger: 30 blank cards spill as one pile, then pop into three neat stacks of ten (no bow)", "ba phần"),
        ("Splits 30 blank cards into 3 stacks", "methodical"), link="so the fix starts from the same 30 words")
    s = Scene("b05b", "b05", "payoff", ["c11"], "room")
    vl = s.W("c11", "viết")
    add(s, [C("focused", "typing")], [WIN([[0, "day"]]), TABLE, TOME([[0, "open"], [s.W("c11", "gấp"), "closed"]], **BK5),
                dict(DK, spillAt=-5, splitAt=-2, tickAt=s.W("c11", "đó")),
                PEN([[0, 560, 1420], [vl, 238, 1300], [vl + 0.2, 292, 1300], [vl + 0.3, 238, 1306], [vl + 0.5, 292, 1306], [vl + 0.6, 238, 1312], [vl + 0.8, 290, 1312]], rot=18)],
        [SFX("snap", "c11", "gấp", s), SFX("pen", "c11", "viết", s)],
        ("mmx-snap: book snaps shut at 'gấp sách', pen writes the part on the sheet, tick on the first stack at 'phần đó'", "gấp sách"),
        ("Closes the book, writes one stack from memory, ticks it", "steady"), link="what to do with each stack")
    s = Scene("b05c", "b05", "payoff", ["c12"], "room")
    mo = s.W("c12", "mở")
    add(s, [C("confused", "thinking")], [WIN([[0, "day"]]), TABLE, TOME([[0, "closed"], [mo, "open"], [mo + 0.75, "closed"]], **BK5),
                dict(DK, spillAt=-5, splitAt=-2, tickAt=-1), PEN([[0, 560, 1420]], rot=12)],
        [SFX("pop", "c12", "mở", s)],
        ("mmx-snap-settle: book opens once at 'mở sách' for a glance, then shuts again", "mở sách"),
        ("Opens the book once only where stuck, closes it again", "small doubt, then sure"), link="the only moment the book opens")

    # b06 evidence → HyperFrames motion-graphic plate (rule-42): final/mg-b06 → public/mg/c04v18-b06.mp4
    YC = lambda at: TAG("Yang et al. 2021", 540, 1330, at)
    s = Scene("b06a", "b06", "evidence", ["c13"], "plate"); t6 = 0.0
    add(s, [], [PL("b06", t6), YC(s.W("c13", "giang"))],
        [SFX("ding", "c13", "giang", s)],
        ("hf-motion-graphic: research papers drop one by one into a pile, squared up at 'nghiên cứu'; study credit at 'Yang'", "222 nghiên cứu"),
        ("Research papers pile up and merge", "solid, sure"), link="bigger evidence for the same closed-book habit", mg="mg-b06")
    t6 += s.dur
    s = Scene("b06b", "b06", "evidence", ["c14"], "plate")
    add(s, [], [PL("b06", t6), YC(-1)],
        [SFX("rise", "c14", "cao", s, 1, -0.05)],
        ("hf-motion-graphic: two class bars, quiz sheet + tick on the quiz class, bars rise at 'điểm cao hơn', hand points at the TALL bar, dashed line + bracket marks a moderate gap at 'ở mức vừa'", "cao hơn"),
        ("Two class bars, the quiz class a moderate step higher; no numbers", "measured, not hyped"), link="what those studies found", mg="mg-b06")

    # b07 result: same frames as b02, card flips to a clear suitcase + tick; hold ~1s
    s = Scene("b07a", "b07", "payoff", ["c15"], "room")
    add(s, [C("neutral", "idle")], [WIN([[0, "night"], [s.W("c15", "sáng"), "day"]]), TABLE, TOME([[0, "closed"]]), SHEET(), PEN_REST],
        [SFX("rise", "c15", "sáng", s, 1, -0.05)],
        ("mmx-cruise: same desk as b02, sun rises again, the book stays closed", "sách vẫn gấp"),
        ("Next morning, book still closed beside the blank sheet", "calm"), link="the next morning after doing the method")
    s = Scene("b07b", "b07", "payoff", ["c16a", "c16b"], "paper", "closeup")
    x0, x1 = ROWX(True); tv = s.W("c16a", "tự"); fl = s.W("c16a", "lắc")
    add(s, [], [WIN([[0, "day"]], cu=True), TOME([[0, "closed"]], room=False), SHEET([(i, -1) for i in range(4)] + [(4, tv)], cu=True),
                CARD(flipAt=fl), PEN([[0, x0, ROWY(4, True)], [tv, x0, ROWY(4, True)], [tv + 0.35, x1 - 40, ROWY(4, True) + 4], [tv + 0.5, x1 - 20, ROWY(4, True) + 60]], rot=26, cu=True),
                TAG("luggage", 790, 880, fl + 0.3, style="word", font="en", tick=True)],
        [SFX("pen", "c16a", "tự", s), SFX("pop", "c16a", "lắc", s, 1, 0.3)],
        ("mmx-soft-land: same close-up as b02, pen fills row 5, the face-down card flips to a clear suitcase + tick, word tag 'luggage', hold 1s", "luggage"),
        ("Writes row 5; the stuck card flips to a clear suitcase with a tick", "relieved smile"), push=0.06, link="payoff on the exact word stuck in b02")

    # b08 CTA: cut on motion, faces the viewer, ends on the frame-0 set (closed book, blank sheet, pen)
    s = Scene("b08a", "b08", "cta", ["c17a"], "room")
    add(s, [C("happy", "talking", "right")], [WIN([[0, "day"]]), TABLE, TOME([[0, "open"], [s.W("c17a", "gấp"), "closed"]]), SHEET(), PEN_REST],
        [SFX("snap", "c17a", "gấp", s)],
        ("mmx-cut-on-motion: turns to the viewer and snaps the book shut at 'gấp sách lại'", "mấy từ"),
        ("Turns to the camera and shuts the book", "warm, inviting"), link="hands the same closed-book test to the viewer")
    s = Scene("b08b", "b08", "cta", ["c17b"], "room")
    add(s, [C("happy", "talking", "right")], [WIN([[0, "day"]]), TABLE, TOME([[0, "closed"]]), SHEET(), PEN_REST,
                {"kind": "icon", "name": "chat", "x": 205, "y": 1010, "size": 120, "at": s.W("c17b", "com"), "plate": True},
                {"kind": "icon", "name": "hand", "x": 205, "y": 1190, "size": 92, "rot": 180, "at": s.W("c17b", "com") + 0.12, "bob": True}],
        [SFX("tick", "c17b", "số", s)],
        ("mmx-soft-land: comment bubble icon pops, hand points down; frame returns to the frame-0 set (closed book, blank sheet, pen)", "con số"),
        ("Points down to the comments; desk looks like frame 0 again", "warm"), link="the reply the viewer leaves")
    return out

def write():
    sc = build()
    for x in sc:
        x["lines"][-1].pop("cap_hold", None)
    # hold b07: caption of the held line stays through the 1s hold
    for x in sc:
        for l in x["lines"]:
            if l["voice_file"].endswith(f"{MK.HOLD_AFTER}.wav"): l["cap"] = [l["cap"][0], S[MK.HOLD_AFTER]["dur"]]
    base = json.load(open(D + "spec.json"))
    spec = {"id": "clip-04-final", "clip": "clip-04", "title": "Gấp sách tự kiểm (HTB 23.14) - script v18 locked", "week": 1, "theme": "light", "pillar": "Học đúng cách",
        "story": "monologue Thầy (L-039); ví dụ 30 từ tiếng Anh (luggage); L-050 nghĩa bằng vật + hành động, không chữ trong hình; visual-plan-v18 (FLUX 6770a3f) + short-factory review",
        "trend": base.get("trend"), "voice_prefix": P, "voice_track": "voice-track-c04v18.wav", "mix": "linear", "layout": "tiktok",
        "length_target": [40, 60.5], "length_note": "L-080 (Hiệp 21/10 00:33): độ dài theo nội dung, không ép 55s; giọng 46.1s + giữ b07 1s + đuôi 0.3s + end card 1.5s",
        "pacing": {"exact": True, "swish": "beat"}, "transition_sfx": base["transition_sfx"],
        "endcard": {"duration": 1.5, "y": 560, "safety": "Thông tin tham khảo, không thay thế tư vấn chuyên gia",
                    "sources": "Roediger & Karpicke 2006 · Yang et al. 2021",
                    "credit": "Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/"},
        "revisions": [{"v": "v18", "date": "2026-10-21", "note": "Stage 2 render: approved voice c0ec507 (Rule Reviewer PASS), script-v18-LOCKED, visual-plan-v18 + short-factory review; one Remotion part, lines = frame-aligned slices of the approved wav"}],
        "cover": base.get("cover"),
        "hook": {"text": "HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?", "scenes": ["b01a", "b01b"], "format": "pain point + câu hỏi (Hiệp chốt v18); 2 shot, cắt ở ~1.8s"},
        "engagement": [{"type": "relatable-question", "beat": "b01b", "text": "bạn còn nhớ được những gì?"},
                       {"type": "comment-challenge", "beat": "b08b", "text": "Comment con số nha."},
                       {"type": "loop", "beat": "b08a", "text": "thử gấp sách lại", "hook_word": "sách"}],
        "voices": {"Thầy": "F5 · Thái Sơn speed 1.0 (approved voice-only-c04v18.wav)"},
        "throughline": "Học thuộc tối qua VÀ sáng dậy quên sạch, NHƯNG đọc lại chỉ thắng lúc kiểm tra ngay, còn hai ngày sau nhóm tự kiểm tra nhớ hơn, VÌ VẬY chia 30 từ thành 3 phần và gấp sách viết lại từng phần",
        "hook_question": {"asked": "Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì?", "answered": "b07: sáng hôm sau sách vẫn gấp, tự viết được luggage"},
        "structure": {"hook": ["b01a", "b01b"], "intro": ["b02a", "b02b", "b02c", "b03a", "b03b", "b03c", "b04"], "body": ["b05a", "b05b", "b05c", "b06a", "b06b"], "summary": ["b07a", "b07b"], "cta": ["b08a", "b08b"]},
        "hook_alt": {"type": "direct", "text": "(giữ nguyên hook Hiệp chốt, không dùng hook_alt)"}, "callbacks": [],
        "parts": [{"id": "A", "engine": "remotion", "scenes": sc}]}
    json.dump(spec, open(D + "spec.json", "w"), ensure_ascii=False, indent=1)
    print("spec written:", len(sc), "scenes,", round(sum(x["dur"] for x in sc), 3), "s + end card", spec["endcard"]["duration"])
