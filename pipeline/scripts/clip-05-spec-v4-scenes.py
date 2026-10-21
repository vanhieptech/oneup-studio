"""clip-05 v4 scenes → final/spec.json (imported by clip-05-mkspec-v4.py spec). Follows script-v4-LOCKED.md (91848a3) and
final/visual-plan-v4.md (FLUX, b03 constraint 97a50af). Times are scene-local seconds from the measured word times of the approved
voice (slices.json). Cuts every ~1.5–3.4 s (23 shots). DARK theme. L-050: meaning by objects; words only as overlays (tag/counter)."""
import json, os, re, importlib
MK = importlib.import_module("clip-05-mkspec-v4")
D, WORK, P = MK.D, MK.WORK, MK.P
S = json.load(open(WORK + "slices.json")); LN = {L[0]: L for L in MK.LINES}
NOBUB = {"c09", "c11a", "c15"}  # lines in scenes without the character → voice + caption only

def line(lid):
    L = LN[lid]; s = S[lid]
    say = re.sub(r"\*\*", "", L[3]); ph = re.sub(r"\*\*([^*]+)\*\*", r"{nhấn: \1}", L[3])
    d = {"speaker": "hiep", "emotion": L[6], "text": L[3], "say": say, "en": L[4], "hl": L[5], "bubble": L[7] and lid not in NOBUB, "voice_role": "Thầy",
         "voice_file": f"voice/{s['key']}.wav", "cap": s["cap"], "chunk": L[1]}
    if lid not in ("c01b", "c01c"): d["phrases"] = [{"t": ph}]  # c01a/c01b/c01c = one F5 take (chunk c01); its {nhấn: một đêm} rides on c01a (own words, so rule-46 STT compares each slice with its own text)
    return d

class Scene:
    def __init__(s, id, beat, part, lids, bg, framing="medium"):
        s.id, s.beat, s.part, s.lids, s.bg, s.framing = id, beat, part, lids, bg, framing
        s.off = {}; t = 0
        for l in lids: s.off[l] = t; t += S[l]["dur"]
        s.dur = round(t, 4)
    def W(s, lid, word, n=1, end=False):
        k = 0
        for w, a, b in S[lid]["tok"]:
            if w == word:
                k += 1
                if k == n: return round(s.off[lid] + max(0.0, b if end else a), 3)
        raise KeyError((lid, word, n))
    def L0(s, lid): return s.off[lid]

# ---------- shared objects (design px) ----------
def WIN(sky, **kw): return {"kind": "window", "x": 0, "y": 0, "sky": sky, **{"wx": 660, "wy": 250, "ww": 300, "wh": 250, **kw}}
TABLE = {"kind": "table", "x": 0, "y": 0, "top": 1395}
def BIO(keys=(("closed",),), x=205, y=1240, s=0.5, **kw): return {"kind": "biobook", "x": x, "y": y, "s": s, "keys": [[0, keys[0][0]]] + [list(k) for k in keys[1:]], **kw}
def BIOK(keys, x=205, y=1240, s=0.5, **kw): return {"kind": "biobook", "x": x, "y": y, "s": s, "keys": keys, **kw}
def PEN(keys, rot=24, ln=150): return {"kind": "pen", "x": 0, "y": 0, "s": 1, "rot": rot, "len": ln, "keys": keys}
def C(ex="focused", act="talking", facing="left", x=0.76): return {"id": "hiep", "x": x, "facing": facing, "pose": "sitting", "action": act, "expression": ex}
WORDS = {("c18", "com"): "Comment", ("c03", "di"): "Di truyền"}
def SFX(n, lid, word, sc, nn=1, off=0.0):
    li = sc.lids.index(lid); return {"name": n, "atLine": li, "offset": round(max(0.0, sc.W(lid, word, nn) - sc.L0(lid) + off), 3), "word": WORDS.get((lid, word), word)}
def TAG(text, x, y, at, until=None, **kw): return dict({"kind": "tag", "text": text, "x": x, "y": y, "at": at}, **({"until": until} if until is not None else {}), **kw)
EXAM_PUN = {"kind": "punnett", "x": 330, "y": 1130, "s": 0.82, "tilt": -3}
EXAM_CLOCK = {"kind": "wallclock", "x": 190, "y": 760, "s": 0.9, "h": 2.6}
NUM = lambda n, at: TAG(n, 150, 300, at, style="word", size=190)  # «1» / «2» kinetic overlay (template, not drawn in the image)

def build():
    out = []
    def add(sc, cast, props, sfx, fx, stage, link=None, push=0.04, narration=None):
        lines = [line(l) for l in sc.lids]
        if cast:
            for l in lines: l["set"] = {"hiep": {"expression": l["emotion"] if l["emotion"] != "neutral" else "neutral"}}
        d = {"id": sc.id, "beat": f"clip-05.{sc.beat}", "part": sc.part, "role": "Thầy", "background": sc.bg, "framing": sc.framing, "push": push, "transition": "cut",
             "cast": cast, "fx": {"visual": fx[0], "word": fx[1]}, "sfx": sfx, "props": props, "lines": lines, "stage": {"action": stage[0], "react": stage[1]}, "dur": sc.dur}
        if link: d["link"] = link
        if narration: d["narration"] = narration
        out.append(d)

    # ---- b01 hook (L-084 trend at b01a) ----
    s = Scene("b01a", "b01", "hook", ["c01a", "c01b"], "room")
    add(s, [], [WIN([[0, "night"]], wx=560, wy=330, ww=280, wh=240), {"kind": "table", "x": 0, "y": 0, "top": 1250},
                {"kind": "wallclock", "x": 220, "y": 330, "s": 0.8, "h": 2.92}, {"kind": "textbooks", "x": 380, "y": 1228, "s": 0.95, "n": 6},
                {"kind": "lamp", "x": 690, "y": 1236, "s": 0.85}, {"kind": "ttframe", "x": 0, "y": 0, "shareAt": 0.3, "likeAt": 0.18, "barDur": 14},
                {"kind": "counter", "x": 958, "y": 1236, "at": 0.3, "to": 55.3, "suffix": "K", "dur": 0.6},
                TAG("@ng__phanh · TikTok", 300, 1312, 0.0, font="en", size=30),
                TAG("Học 1 đêm mới hiểu sao…", 380, 1388, 0.0, style="word", size=46)],
        [{"name": "pop", "atLine": 0, "offset": 0.3, "word": "một đêm"}],
        ("mmx-cut-on-motion: TikTok-style vertical feed rebuilt from objects (brand-new textbook pile, desk lamp, moon, clock near 3), share button pulses and counts up to 55,3K", "một đêm"),
        ("Night desk shown as a vertical feed frame: untouched textbooks, lamp on, share count climbs", "shock, relatable pain"), push=0.05,
        narration="HỌC DỒN 1 ĐÊM? 1 TUẦN SAU CÒN GÌ?")
    s = Scene("b01b", "b01", "hook", ["c01c"], "room")
    pd = s.W("c01c", "làm")
    add(s, [C("happy", "reacting")], [WIN([[0, "day"]]), TABLE, BIO(), {"kind": "exam", "x": 470, "y": 1250, "s": 0.62, "tilt": -4},
                {"kind": "icon", "name": "tick", "x": 545, "y": 1135, "size": 70, "at": pd + 0.1},
                PEN([[0, 640, 1150], [pd - 0.05, 640, 1150], [pd + 0.2, 585, 1420]], rot=10)],
        [SFX("snap", "c01c", "làm", s, 1, 0.2)],
        ("mmx-cut-on-motion: morning sun, pen set down beside the exam sheet, tick pops, relieved exhale", "làm được đề"),
        ("Morning: puts the pen down next to a ticked exam sheet", "relieved"), link="the morning right after the cram night")
    s = Scene("b01c", "b01", "hook", ["c02"], "room")
    t0 = s.W("c02", "tuần")
    add(s, [C("confused", "thinking")], [WIN([[0, "day"]]), TABLE, {"kind": "tearpad", "x": 330, "y": 1150, "s": 0.85, "n": 9, "tears": [round(t0 + i * 0.12, 3) for i in range(7)]}],
        [SFX("swish", "c02", "tuần", s)],
        ("mmx-stagger: number-less tear-off calendar sheds 7 pages fast, a blank page left; head tilt", "một tuần sau"),
        ("Seven calendar pages fly off; stares at the blank page, head tilted", "unsure, asks the viewer"), link="one week after that exam")

    # ---- b02 example ----
    s = Scene("b02a", "b02", "struggle", ["c03"], "room")
    add(s, [C("focused", "talking")], [WIN([[0, "night"]]), TABLE, {"kind": "hourglass", "x": 470, "y": 1210, "s": 0.8, "flow": [0, s.dur]},
                BIOK([[0, "open"]], x=205, y=1300, s=0.5, flips=[s.W("c03", "ôn"), s.W("c03", "tiếng"), s.W("c03", "hôm")])],
        [SFX("swish", "c03", "ôn", s), SFX("tick", "c03", "liền", s)],
        ("mmx-cruise: night, one big hourglass pours non-stop beside the open genetics book (DNA sticker); pages flip fast", "ba tiếng liền"),
        ("Night: flips the genetics book fast while the big hourglass pours", "determined, cramming"), link="my own example of that cram night")
    s = Scene("b02b", "b02", "struggle", ["c04"], "grid")
    kq = s.W("c04", "không")
    add(s, [C("confused", "thinking")], [EXAM_CLOCK, TABLE, dict(EXAM_PUN), PEN([[0, 520, 1010], [0.4, 470, 960]], rot=30, ln=170),
                {"kind": "qmark", "x": 680, "y": 770, "s": 0.8, "at": kq}],
        [SFX("tick", "c04", "không", s)],
        ("mmx-snap-settle: finals room, empty 4x4 Punnett grid, pen frozen mid-air, small '?' pops", "không nhớ"),
        ("Finals exam: empty Punnett grid, pen frozen above it", "puzzled, not dumb"), link="the same chapter comes back at finals")

    # ---- b03 cause + evidence (each bar compared only with the grey bar) ----
    G, O, B = 210, 320, 216  # Rule Reviewer final F2 (bb7423c): +2-day third bar just above grey (target 215–227px as RR measures it; 216 renders ≈222–224 incl. outline), well under the immediate orange
    LAB = lambda at: [TAG("Đọc 1 lần", 210, 1330, at, size=30), TAG("Đọc 2 lần liền", 540, 1330, at, size=30), TAG("Lần 2 cách 1 tuần", 870, 1330, at, size=30)]
    CR = lambda at: TAG("Rawson & Kintsch 2005", 540, 1410, at, font="en", size=26)
    GR = lambda keys, focus, ref=None: {"kind": "groups3", "x": 540, "y": 1000, "s": 1, "keys": keys, "focus": focus, **({"refAt": ref} if ref is not None else {})}
    s = Scene("b03a", "b03", "evidence", ["c05"], "paper")
    add(s, [], [{"kind": "paper", "x": 540, "y": 560, "s": 0.6, "tilt": -3, "rows": [[i, 0.05 + i * 0.06] for i in range(7)]}, GR([[0, 0, 0, 0]], [[0, [0, 1, 2]]]), *LAB(0.0), CR(s.W("c05", "nghiên"))],
        [SFX("pop", "c05", "hai", s)],
        ("mmx-stagger: the one text page they all read sits on top; three faceless groups with their books: grey reads once, orange reads twice back-to-back, ink reads again a week later (7 sheets between books)", "hai lần liền"),
        ("Three groups, one book each, the orange group has two books stacked tight", "curious"), link="why the cram night fades: a 2005 reading study")
    s = Scene("b03b", "b03", "evidence", ["c06"], "paper")
    ng = s.W("c06", "ngay"); hi = s.W("c06", "cao")
    add(s, [], [GR([[0, 0, 0, 0], [ng, G, 0, 0], [hi, G, O, 0]], [[0, [0, 1]]], ref=ng + 0.35), {"kind": "lamp", "x": 860, "y": 560, "s": 0.6, "flip": True}, *LAB(0.0), CR(0.0)],
        [SFX("rise", "c06", "cao", s, 1, -0.1)],
        ("mmx-snap-settle: desk lamp = tested right away; grey bar rises, dashed grey reference line; orange bar rises above it", "cao hơn"),
        ("Tested at once: orange bar taller than the grey reference", "fair, admits it helps first"), link="first result of that study")
    s = Scene("b03c", "b03", "evidence", ["c07"], "paper")
    d2 = s.W("c07", "sau"); kc = s.W("c07", "không")
    add(s, [], [GR([[0, G, O, 0], [kc, G, G, 0]], [[0, [0, 1]]], ref=-1), WIN([[0, "night"], [0.25, "day"], [0.55, "night"], [0.85, "day"]], wx=780, wy=330, ww=220, wh=190),
                TAG("+2 ngày", 890, 260, d2, style="word", size=46), *LAB(0.0), CR(0.0)],
        [SFX("tick", "c07", "sau", s), SFX("snap", "c07", "không", s, 1, 0.1)],
        ("mmx-snap-settle: window sun rises twice (+2 ngày), orange bar sinks onto the grey reference line", "hai ngày sau"),
        ("Two sunrises; orange bar drops level with grey", "surprised reversal"), link="but two days later that lead is gone")
    s = Scene("b03d", "b03", "evidence", ["c08a"], "paper")
    add(s, [], [GR([[0, G, G, 0]], [[0, [0, 2]]], ref=-1), WIN([[0, "day"]], wx=780, wy=330, ww=220, wh=190), TAG("+2 ngày", 890, 260, -1, style="word", size=46), *LAB(0.0), CR(0.0)],
        [SFX("swish", "c08a", "tuần", s)],
        ("mmx-push-in: spotlight moves to the ink group, its two books separated by seven calendar sheets", "cách một tuần"),
        ("Focus on the group whose second read came a week later", "interested"), link="the third group in the same study")
    s = Scene("b03e", "b03", "evidence", ["c08b"], "paper")
    vh = s.W("c08b", "hơn")
    add(s, [], [GR([[0, G, G, 0], [vh - 0.2, G, G, B]], [[0, [0, 1, 2]]], ref=-1), WIN([[0, "day"]], wx=780, wy=330, ww=220, wh=190), TAG("+2 ngày", 890, 260, -1, style="word", size=46), *LAB(0.0), CR(0.0)],
        [SFX("rise", "c08b", "hơn", s, 1, -0.25)],
        ("mmx-snap-settle: at +2 days the ink bar rises above the grey reference line (no numbers, orange stays level with grey)", "vẫn hơn"),
        ("Ink bar ends above the grey reference two days later", "convinced"), link="what that week-apart group kept two days later")

    # ---- b04 goal ----
    s = Scene("b04", "b04", "intro", ["c09"], "paper")
    add(s, [], [{"kind": "exam", "x": 250, "y": 930, "s": 1.0, "tilt": -5}, {"kind": "exam", "x": 830, "y": 930, "s": 1.0, "tilt": 4, "head": "accent"},
                {"kind": "rope", "x": 0, "y": 0, "a": [350, 960], "b": [730, 960], "sag": 110, "at": s.W("c09", "tới")},
                BIOK([[0, "closed"]], x=830, y=1250, s=0.5, glowAt=s.W("c09", "vẫn"))],
        [SFX("rise", "c09", "vẫn", s)],
        ("mmx-draw-on: a string runs from the midterm sheet to the finals sheet; the genetics book glows at the finals end", "vẫn nhớ"),
        ("String from midterm sheet to finals sheet, book glowing at the finals end", "calm, clear goal"), push=0.08, link="goal set against that finals gap")

    # ---- b05 how-to (counted: 1 / 2) ----
    s = Scene("b05a", "b05", "payoff", ["c10"], "room")
    ba = s.W("c10", "ba")
    add(s, [C("focused", "talking")], [WIN([[0, "night"]]), TABLE, BIO(),
                dict({"kind": "hourglass", "x": 470, "y": 1210, "s": 0.8, "level": 0.0}, mv=[[0, 470, 1210], [ba, 470, 1210], [ba + 0.45, 450, 1120]])],
        [SFX("swish", "c10", "ba", s)],
        ("mmx-cut-on-motion: the same big hourglass is pulled to centre, refilled", "ba tiếng"),
        ("Pulls the same big hourglass to the middle of the desk", "planning"), link="same three hours, spent differently")
    s = Scene("b05b", "b05", "payoff", ["c11a"], "paper")
    ch = s.W("c11a", "chia")
    add(s, [], [NUM("1", 0.02), *[{"kind": "tearpad", "x": x, "y": 1190, "s": 0.6, "n": 4, "at": ch + 0.25 + i * 0.07} for i, x in enumerate((230, 540, 850))],
                *[{"kind": "moondot", "x": x, "y": 960, "s": 0.9, "at": ch + 0.55 + i * 0.1} for i, x in enumerate((230, 540, 850))],
                {"kind": "hourglass", "x": 540, "y": 700, "s": 1.0, "level": 0.0, "breakAt": ch, "to": [[-310, 400], [0, 400], [310, 400]], "smallSize": 0.5}],
        [SFX("snap", "c11a", "chia", s), SFX("pop", "c11a", "ba", s, 1, 0.1)],
        ("mmx-stagger: big «1»; the big hourglass breaks into three small ones that land on three calendar pages, one moon each", "ba ngày"),
        ("Hourglass splits into three small ones on three calendar pages", "neat, decisive"), link="step one of that plan")
    s = Scene("b05c", "b05", "payoff", ["c11b"], "room")
    cm = s.W("c11b", "cẩm")
    add(s, [C("focused", "idle")], [WIN([[0, "night"]]), TABLE, NUM("1", -5), {"kind": "hourglass", "x": 470, "y": 1280, "s": 0.5, "flow": [0.1, cm - 0.2]},
                BIOK([[0, "open"], [cm, "closed"]], x=205, y=1300, s=0.5, flips=[s.W("c11b", "tiếng")])],
        [SFX("snap", "c11b", "cẩm", s)],
        ("mmx-cruise: one small hourglass runs out during one study hour, then the book snaps shut", "một tiếng"),
        ("Studies one hour by a small hourglass, closes the book when it runs out", "steady"), link="what one of those three days looks like")
    s = Scene("b05d", "b05", "payoff", ["c12"], "room")
    gp = s.W("c12", "gấp"); tk = s.W("c12", "kiểm"); cp = s.W("c12", "clip")
    rows = [(i, gp + 0.25 + i * 0.16) for i in range(3)]
    pk = [[0, 585, 1420], [gp + 0.1, 585, 1420]] + [k for i in range(3) for k in ([gp + 0.25 + i * 0.16, 413, 1265 + 0.45 * (-232 + 50 * i)], [gp + 0.39 + i * 0.16, 540, 1265 + 0.45 * (-232 + 50 * i)])] + [[cp, 585, 1420]]
    add(s, [C("focused", "talking")], [WIN([[0, "night"]]), TABLE, NUM("2", 0.02), BIOK([[0, "open"], [gp, "closed"], [tk + 0.2, "open"]], x=205, y=1300, s=0.5),
                {"kind": "paper", "x": 480, "y": 1265, "s": 0.45, "rows": [list(r) for r in rows]},
                {"kind": "ring", "x": 470, "y": 1265 + 0.45 * (-232 + 50 * 1), "rx": 80, "ry": 22, "at": cp}, PEN(pk, rot=20)],
        [SFX("snap", "c12", "gấp", s), SFX("pen", "c12", "tự", s), SFX("tick", "c12", "clip", s)],
        ("mmx-snap: big «2»; quick clip-04 callback: book shut, pen writes from memory, book opens, red ring circles one row", "tự kiểm"),
        ("Closes the book, writes from memory, opens it, circles the wrong row in red", "focused"), link="step two, the closed-book check from the last clip")

    # ---- b06 evidence ----
    CP = lambda at: TAG("Cepeda et al. 2006", 540, 1410, at, font="en", size=26)
    s = Scene("b06a", "b06", "evidence", ["c13"], "paper")
    add(s, [], [{"kind": "papers", "x": 540, "y": 1150, "s": 1.25, "n": 18, "at": 0.05, "stagger": 0.08}, CP(s.W("c13", "gom"))],
        [SFX("ding", "c13", "thí", s)],
        ("mmx-stagger: research papers drop one by one into a tall pile (many experiments, not counted)", "317 thí nghiệm"),
        ("Papers pile up higher and higher", "solid, sure"), link="bigger evidence for spacing the hours")
    s = Scene("b06b", "b06", "evidence", ["c14a"], "paper")
    nh = s.W("c14a", "nhớ"); la = s.W("c14a", "lâu")
    add(s, [], [{"kind": "strip", "x": 540, "y": 960, "s": 1.0, "flagKeys": [[0, 0.32], [nh - 0.2, 0.62], [la - 0.1, 0.95]], "dotsAt": 0.05}, CP(0.0)],
        [SFX("swish", "c14a", "nhớ", s)],
        ("mmx-drag: a long number-less calendar strip; the hand drags the 'remember until' flag far right; the accent review dots spread with it", "nhớ càng lâu"),
        ("Drags the remember-until flag further along the strip; review dots follow", "lightbulb"), link="what those experiments found")
    s = Scene("b06c", "b06", "evidence", ["c14b"], "paper")
    da = s.W("c14b", "dài")
    add(s, [], [{"kind": "strip", "x": 540, "y": 960, "s": 0.9, "flagKeys": [[0, 0.95]], "dots": [0, 0.16, 0.42, 0.78]}, CP(0.0)],
        [SFX("tick", "c14b", "dài", s)],
        ("mmx-push-in: close on the strip, gaps between the accent dots stay wide (longer memory = wider gaps)", "càng phải dài"),
        ("The review dots sit far apart along the strip", "sure"), push=0.06, link="the rule behind those spreading dots")

    # ---- b07 fast redo + payoff on the exact b02 frame ----
    s = Scene("b07a", "b07", "summary", ["c15"], "paper")
    xs = (230, 540, 850); st = [0.05 + i * 0.4 for i in range(3)]
    pr = []
    for x, a in zip(xs, st):
        pr += [{"kind": "tearpad", "x": x, "y": 1160, "s": 0.6, "n": 3, "at": a},
               {"kind": "hourglass", "x": x - 70, "y": 870, "s": 0.32, "at": a + 0.05, "flow": [a + 0.1, 0.3]},
               {"kind": "biobook", "x": x + 70, "y": 880, "s": 0.22, "keys": [[0, "closed"]], "from": a + 0.15},
               {"kind": "ring", "x": x, "y": 1210, "rx": 70, "ry": 22, "at": a + 0.3}]
    add(s, [], pr, [SFX("pop", "c15", "làm", s), SFX("pop", "c15", "bước", s)],
        ("mmx-stagger fast-forward: three days flip in, each with a small hourglass, the closed book and a red ring", "hai bước"),
        ("Three days in a row, each with both steps", "brisk"), link="doing both steps over the same three hours")
    s = Scene("b07b", "b07", "summary", ["c16a"], "grid")
    add(s, [C("focused", "thinking")], [EXAM_CLOCK, TABLE, dict(EXAM_PUN), PEN([[0, 520, 1010], [0.6, 470, 960], [1.6, 380, 1060]], rot=30, ln=170)],
        [SFX("swish", "c16a", "lai", s)],
        ("mmx-match-cut: the exact b02 finals frame (same angle, same empty Punnett grid), pen moves in this time", "dạng lai"),
        ("Back in the same finals seat facing the same empty grid; the pen moves", "calm"), link="same finals problem as in b02")
    s = Scene("b07c", "b07", "summary", ["c16b"], "grid")
    add(s, [C("happy", "talking")], [EXAM_CLOCK, TABLE, dict(EXAM_PUN, fillAt=0.05, tickAt=s.W("c16b", "hơn")), PEN([[0, 380, 1060], [1.2, 300, 1230]], rot=30, ln=170)],
        [SFX("pen", "c16b", "nhớ", s), SFX("ding", "c16b", "hơn", s)],
        ("mmx-soft-land: same angle, the Punnett grid fills with coloured dots cell by cell, small tick, light nod", "dễ nhớ ra"),
        ("Fills the whole grid, small nod", "relieved, not cheering"), push=0.06, link="payoff on the exact grid that was empty in b02")

    # ---- b08 CTA ----
    s = Scene("b08", "b08", "cta", ["c17", "c18"], "room")
    cm = s.W("c18", "com")
    add(s, [C("happy", "talking", "right")], [WIN([[0, "day"]]), TABLE,
                dict({"kind": "tearpad", "x": 430, "y": 1050, "s": 0.7, "n": 6, "holdUp": True}, mv=[[0, 330, 1210], [0.35, 430, 1000]]),
                {"kind": "icon", "name": "chat", "x": 190, "y": 1060, "size": 120, "at": cm, "plate": True},
                {"kind": "icon", "name": "hand", "x": 190, "y": 1270, "size": 96, "rot": 180, "at": cm + 0.12, "bob": True}],
        [SFX("swish", "c17", "môn", s), SFX("tick", "c18", "số", s)],
        ("mmx-soft-land: lifts a number-less calendar page toward the viewer, comment bubble pops, hand points down", "mấy hôm"),
        ("Holds up a calendar page, points down to the comments", "warm, curious"), link="hands the same question to the viewer")
    return out

def write():
    sc = build()
    spec = {"id": "clip-05-final", "clip": "clip-05", "title": "Học dồn một đêm (HTB 23.15) - script v4 locked", "week": 1, "theme": "dark", "pillar": "Học & đầu tư bản thân",
        "story": "monologue Thầy; ví dụ chương Di truyền / dạng lai hai cặp tính trạng (ô Punnett 4×4 trống b02, điền b07); L-050 nghĩa bằng vật + hành động; visual-plan-v4 (FLUX 0a6738b, b03 97a50af)",
        "trend": {"source": "https://www.tiktok.com/@ng__phanh/video/7532553338664045831", "where": "b01a (TikTok-style frame rebuilt from objects + overlay caption + 55,3K share counter)", "file": "final/trend-signals.md"},
        "voice_prefix": P, "voice_track": "voice-track-c05v4.wav", "mix": "linear", "layout": "tiktok", "caption_accent": True,
        "length_target": [50, 60.5], "length_note": "L-080: độ dài theo nội dung; giọng 52.7s (approved 5b12e22) + đuôi 0.3s (bỏ giữ b07c, Rule Reviewer F3) + end card 2.0s",
        "pacing": {"exact": True, "swish": "beat"}, "transition_sfx": {"part": "whoosh-soft", "scene": "swish"},
        "endcard": {"duration": 2.0, "y": 520, "safety": "Thông tin tham khảo, không thay thế tư vấn chuyên gia",
                    "sources": "Nguồn: Rawson & Kintsch 2005 · Cepeda et al. 2006 · Yang et al. 2021 · Dunlosky et al. 2013 · Trend: @ng__phanh · TikTok",
                    "credit": "Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/"},
        "revisions": [{"v": "v4", "date": "2026-10-21", "note": "Render stage: approved voice c05v4 (Rule Reviewer PASS 5b12e22; c18 /s/ rev5 764c16d), script-v4-LOCKED (91848a3), visual-plan-v4 (97a50af); one Remotion part, lines = frame-aligned slices of the approved wav; caption keyword accent #FF5A36 = open choice for Hiệp"}],
        "cover": {"direction": "a", "theme": "dark", "series": "Học đúng cách", "ep": 5, "hero": ["HỌC DỒN 1 ĐÊM?", "1 TUẦN SAU CÒN GÌ?"], "accent": 1, "strike": -1,
                  "expression": "confused", "action": "thinking", "tilt": -4},
        "hook": {"text": "HỌC DỒN 1 ĐÊM? 1 TUẦN SAU CÒN GÌ?", "scenes": ["b01a", "b01b", "b01c"], "format": "nỗi đau + câu hỏi; trend @ng__phanh chỉ ở hình/chữ b01a (L-084); 3 shot, cắt ở 1.57s và 2.93s"},
        "engagement": [{"type": "relatable-question", "beat": "b01c", "text": "bạn còn nhớ bao nhiêu?"},
                       {"type": "comment-challenge", "beat": "b08", "text": "Comment số hôm nha."},
                       {"type": "loop", "beat": "b08", "text": "Còn bạn, môn sắp thi còn cách mấy hôm?", "hook_word": "bạn"}],
        "voices": {"Thầy": "F5 · Thái Sơn speed 1.0 (approved voice-only-c05v4.wav, 5b12e22 + c18 rev5 764c16d)"},
        "throughline": "Học dồn một đêm VÀ sáng ra vẫn làm được đề, NHƯNG một tuần sau quên nhanh (đọc liền chỉ hơn lúc kiểm tra ngay), VÌ VẬY cùng ba tiếng đó chia ra ba ngày và mỗi buổi gấp sách tự kiểm",
        "hook_question": {"asked": "Một tuần sau, bạn còn nhớ bao nhiêu?", "answered": "b07: làm đủ hai bước, tới cuối kỳ dễ nhớ ra cách giải dạng lai hai cặp tính trạng hơn"},
        "structure": {"hook": ["b01a", "b01b", "b01c"], "intro": ["b02a", "b02b", "b03a", "b03b", "b03c", "b03d", "b03e", "b04"], "body": ["b05a", "b05b", "b05c", "b05d", "b06a", "b06b", "b06c"],
                      "summary": ["b07a", "b07b", "b07c"], "cta": ["b08"]},
        "hook_alt": {"type": "direct", "text": "(giữ nguyên hook v4 đã Chốt, không dùng hook_alt)"},
        "callbacks": [{"clip": "clip-04", "beat": "b05d", "what": "gấp sách tự kiểm (bước Hai) — gọi lại, không giải thích lại"}],
        "parts": [{"id": "A", "engine": "remotion", "scenes": sc}]}
    json.dump(spec, open(D + "spec.json", "w"), ensure_ascii=False, indent=1)
    print("spec written:", len(sc), "scenes,", round(sum(x["dur"] for x in sc), 3), "s + end card", spec["endcard"]["duration"])
    for x in sc: print(f"  {x['id']:5} {x['dur']:.2f}s")
