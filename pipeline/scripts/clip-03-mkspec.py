"""clip-03 v8 spec generator (script locked 16/10) (HTB 4.7, Thầy monologue, meme 'bản chất' stems, L-039/L-040).
Meta (cover, pacing, transition_sfx) modelled on clip-02; voice via build-final --stage voice-phrase (prefix c03v3)."""
import json, re
D = '/workspace/oneup-studio/content/clips/clip-03-big-task-chunking/final/'
P = 'c03v8'
# key, display text, spoken phrases ('|' split, {nhấn:}), en, highlight words
RAW = [
("b01", "Có việc gì bạn hứa **cuối tuần** làm…", "Có việc gì bạn hứa {nhấn: cuối tuần} làm...", "Got a task you promised for \"this weekend\"…", ["weekend\"…"]),
("b01b", "…mà để **cả năm** rồi chưa đụng tới không?", "mà để {nhấn: cả năm} rồi chưa đụng tới không?", "…that's sat untouched for a year?", ["year?"]),
("b02", "Như dọn cái phòng, hay ôn thi chẳng hạn. Tuần nào cũng tự nhủ **cuối tuần làm**, rồi một năm trôi qua lúc nào không hay.", "Như dọn cái phòng, hay ôn thi chẳng hạn.|Tuần nào cũng tự nhủ {nhấn: cuối tuần làm},|rồi một năm trôi qua lúc nào không hay.", "Cleaning your room, studying for exams. \"This weekend\" every week… and a year slips by.", ["room,", "year"]),
("b03", "Lý do là việc đó chỉ có **một cái tên to đùng**. Nhìn vô là **ngợp**, không biết bắt đầu từ đâu, thế là cứ để đó.", "Lý do là việc đó|chỉ có {nhấn: một cái tên to đùng}.|Nhìn vô là {nhấn: ngợp},|không biết bắt đầu từ đâu,|thế là cứ để đó.", "Because it's just one huge name. Overwhelming, no idea where to start, so it sits.", ["huge", "Overwhelming,"]),
("b04", "Chuyện này có nghiên cứu hẳn hoi. Hai nhà tâm lý học Kruger và Evans thấy: nhìn mỗi cái tên việc, mình hay nghĩ **chút xíu là xong**. Phải **ghi ra từng bước nhỏ**, mình mới thấy **nó đâu có ít**.", "Chuyện này có nghiên cứu hẳn hoi.|Hai nhà tâm lý học Cru gơ và Ê vần thấy:|nhìn mỗi cái tên việc,|mình hay nghĩ {nhấn: chút xíu là xong}.|Phải {nhấn: ghi ra từng bước nhỏ},|mình mới thấy {nhấn: nó đâu có ít}.", "Psychologists Kruger & Evans found: from the name alone we think it's quick. List the small steps, and it's not so little.", ["quick.", "steps,"]),
("b05", "Còn giáo sư Steel thì gom **rất nhiều** nghiên cứu về chuyện trì hoãn lại và thấy một điều: việc nào mình càng **ngại đụng vô**, mình càng dễ **để mai tính**. Mà việc càng to thì mình càng ngại, nên nó mới **nằm đó cả năm**.", "Còn giáo sư Xtiu thì gom {nhấn: rất nhiều} nghiên cứu về chuyện trì hoãn lại|và thấy một điều:|việc nào mình càng {nhấn: ngại đụng vô},|mình càng dễ {nhấn: để mai tính}.|Mà việc càng to thì mình càng ngại,|nên nó mới {nhấn: nằm đó cả năm}.", "Professor Steel pooled many procrastination studies: the more we dread a task, the more we put it off. Big tasks feel worse, so they sit all year.", ["dread", "off."]),
("b06", "Vậy nên: việc gì to quá thì **chia nhỏ ra** trước, rồi mới tính coi mất bao lâu, xong mới bắt tay vô làm.", "Vậy nên:|việc gì to quá thì {nhấn: chia nhỏ ra} trước,|rồi mới tính coi mất bao lâu,|xong mới bắt tay vô làm.", "In short: split big tasks first, then estimate, then start.", ["split", "start."]),
("b07", "Như mình đây, thay vì ghi «dọn phòng», mình ghi ra ba việc: **dọn đống đồ** trên ghế, lau cái bàn, đổ sọt rác. Mỗi việc chừng **mười lăm phút**, tối nay làm một việc là xong.", "Như mình đây,|thay vì ghi dọn phòng,|mình ghi ra ba việc:|{nhấn: dọn đống đồ} trên ghế, lau cái bàn, đổ sọt rác.|Mỗi việc chừng {nhấn: mười lăm phút},|tối nay làm một việc là xong.", "Me: not \"clean room\" but three tasks: clear the chair, wipe the desk, empty the trash. About 15 minutes each, one tonight.", ["three", "15"]),
("b08", "Ôn thi cũng vậy: đừng ghi «ôn thi», ghi «làm **một đề** chương hai». Cộng thời gian từng việc lại là biết **chừng nào xong** thật.", "Ôn thi cũng vậy:|đừng ghi ôn thi,|ghi làm {nhấn: một đề} chương hai.|Cộng thời gian từng việc lại|là biết {nhấn: chừng nào xong} thật.", "Same for exams: not \"study\" but \"one practice test, chapter 2\". Add them up: a real finish date.", ["practice", "real"]),
("b09", "Như clip trước mình nói, rối thì **chia nhỏ**. Còn clip đầu tiên: chín giờ tối, ngồi vào bàn, làm **việc nhỏ đầu tiên**.", "Như clíp trước mình nói,|rối thì {nhấn: chia nhỏ}.|Còn clíp đầu tiên:|chín giờ tối, ngồi vào bàn,|làm {nhấn: việc nhỏ đầu tiên}.", "Last clip: messy? Split it. First clip: 9 p.m., at the desk, do the first small task.", ["Split", "first"]),
("b10", "Bạn thấy đó, không phải mình lười, mà là việc **to quá** thôi. Việc bạn để **cả năm** chưa làm là gì? Comment một chữ cho mình biết nha!", "Bạn thấy đó,|không phải mình lười,|mà là việc {nhấn: to quá} thôi.|Việc bạn để {nhấn: cả năm} chưa làm là gì?|Com men một chữ cho mình biết nha!", "Not lazy, the task's just too big. What's yours? Comment one word!", ["big.", "Comment"]),
]
LN = {k: (t, s, en, hw) for k, t, s, en, hw in RAW}
def line(k, emo):
    t, s, en, hw = LN[k]; ws = en.split(); hl = []
    for w in hw:
        i = [j for j, x in enumerate(ws) if x.lower() == w.lower() and j not in hl]; assert i, (w, en); hl.append(i[0])
    return {"speaker": "hiep", "emotion": emo, "text": t, "say": re.sub(r"\{nhấn: ([^}]*)\}", r"\1", s.replace("|", " ")), "en": en, "hl": hl,
            "phrases": [dict({"t": p.strip()}, **({"emph": True} if "{nhấn:" in p else {})) for p in s.split("|")],
            "voice_file": f"voice/{P}-{k}.wav", "voice_role": "Thầy"}
def C(x, facing, pose, act, ex): return {"id": "hiep", "x": x, "facing": facing, "pose": pose, "action": act, "expression": ex}
def SC(id, part, bg, tr, cast, ln, fx, sfx, props, narr=None, push=0.06):
    d = {"id": id, "beat": f"clip-03.{id}", "part": part, "role": "Thầy", "background": bg, "framing": "medium", "push": push,
         "transition": tr, "cast": [cast], "fx": {"visual": fx[0], "word": fx[1]}, "sfx": sfx, "props": props, "lines": [ln]}
    if narr: d["narration"] = narr
    return d
S = lambda n, off, w: {"name": n, "atLine": 0, "offset": off, "word": w}
A = [
 SC("b01", "hook", "grid", "cut", C(0.72, "left", "standing", "talking", "surprised"), line("b01", "surprised"),
    ("mmx-oversize-land: sticky CUỐI TUẦN LÀM treo móc đập frame 0", "cuối tuần"), [S("stamp", 0.0, "cuối tuần"), S("pop", 0.9, "cuối tuần")],
    [], narr="CUỐI TUẦN LÀM", push=0.14),
 SC("b01b", "hook", "bed", "cut", C(0.72, "left", "sitting", "idle", "despair"), line("b01b", "sad"),
    ("Cắt cứng: lịch lật T1→T12 (mmx-accel-exit), sticky vẫn treo", "cả năm"), [S("swish", 0.0, "mà để"), S("stamp", 0.6, "cả năm")],
    [{"kind": "calendar", "x": 260, "y": 1000, "s": 0.6, "pages": ["T1", "T4", "T8", "T12"], "tearAt": [0.5, 1.0, 1.5]}], push=0.14),
 SC("b02", "struggle", "bed", "cut", C(0.72, "left", "sitting", "idle", "despair"), line("b02", "focused"),
    ("mmx-glide: 2 thẻ treo DỌN PHÒNG · ÔN THI đung đưa", "cuối tuần làm"), [S("pop", 0.6, "dọn cái phòng"), S("tick", 3.0, "cuối tuần làm")],
    [{"kind": "words", "x": 280, "y": 900, "s": 0.55, "words": ["DỌN PHÒNG", "ÔN THI"], "dropAt": [0.5, 1.5]}]),
 SC("b03", "struggle", "bed", "cut", C(0.72, "left", "standing", "talking", "confused"), line("b03", "confused"),
    ("mmx-snap-settle: thẻ DỌN PHÒNG phình to đùng, Hiệp lùi lại", "ngợp"), [S("stamp", 1.4, "to đùng"), S("snap", 3.2, "ngợp")],
    [{"kind": "sign", "x": 540, "y": 340, "s": 0.75, "rot": -3, "text": "DỌN PHÒNG", "at": 1.2}]),
 SC("b04", "evidence", "paper", "mmx-soft-land", C(0.78, "left", "standing", "talking", "surprised"), line("b04", "focused"),
    ("motion graphic: KRUGER & EVANS 2004; tên việc bung ra danh sách bước (tdev-stagger), không số", "ghi ra từng bước nhỏ"), [S("ding", 2.0, "Kruger"), S("pop", 7.5, "ghi ra"), S("stamp", 9.5, "đâu có ít")],
    [{"kind": "sign", "x": 280, "y": 860, "s": 0.5, "rot": -3, "text": "KRUGER & EVANS 2004", "at": 1.8},
     {"kind": "words", "x": 280, "y": 1150, "s": 0.5, "words": ["BƯỚC 1", "BƯỚC 2", "BƯỚC 3", "BƯỚC 4"], "dropAt": [7.4, 7.7, 8.0, 8.3]}]),
 SC("b05", "evidence", "paper", "tdev-panel", C(0.78, "left", "standing", "talking", "focused"), line("b05", "focused"),
    ("motion graphic: STEEL 2007 · TỔNG HỢP NGHIÊN CỨU; NGẠI ↑ → ĐỂ MAI; không số", "để mai tính"), [S("ding", 1.0, "Steel"), S("tick", 7.0, "để mai tính"), S("stamp", 11.0, "cả năm")],
    [{"kind": "sign", "x": 280, "y": 860, "s": 0.5, "rot": 2, "text": "STEEL 2007", "at": 0.8},
     {"kind": "words", "x": 280, "y": 1150, "s": 0.5, "words": ["NGẠI ↑", "ĐỂ MAI ↑"], "dropAt": [5.0, 6.8]}]),
 SC("b06", "payoff", "grid", "tdev-stagger", C(0.74, "left", "standing", "talking", "happy"), line("b06", "focused"),
    ("Thầy cắt sợi dây treo, thẻ to vỡ thành thẻ nhỏ (tdev-stagger)", "chia nhỏ ra"), [S("snap", 1.2, "chia nhỏ ra"), S("pop", 2.0, "chia nhỏ ra")],
    [{"kind": "words", "x": 280, "y": 900, "s": 0.55, "words": ["CHIA NHỎ", "TÍNH GIỜ", "BẮT TAY"], "dropAt": [1.2, 3.0, 4.6]}]),
 SC("b07", "payoff", "bed", "mmx-snap-settle", C(0.74, "left", "standing", "talking", "happy"), line("b07", "focused"),
    ("chibi Hiệp làm mẫu: tick 3 thẻ, mỗi thẻ 15'", "dọn đống đồ"), [S("tick", 3.6, "dọn đống đồ"), S("tick", 5.0, "lau cái bàn"), S("tick", 6.2, "đổ sọt rác")],
    [{"kind": "words", "x": 280, "y": 880, "s": 0.5, "words": ["DỌN GHẾ ✓", "LAU BÀN ✓", "ĐỔ RÁC ✓"], "dropAt": [3.5, 4.9, 6.1]},
     {"kind": "sign", "x": 280, "y": 1260, "s": 0.45, "rot": 2, "text": "~15' / VIỆC", "at": 7.2}]),
 SC("b08", "payoff", "desk", "tdev-text-swap", C(0.74, "left", "sitting", "typing", "focused"), line("b08", "focused"),
    ("chibi Hiệp: tdev-text-swap ÔN THI → ĐỀ CHƯƠNG 2, cộng lên lịch", "một đề"), [S("pop", 2.4, "một đề"), S("ding", 5.5, "chừng nào xong")],
    [{"kind": "sign", "x": 280, "y": 900, "s": 0.5, "rot": -2, "text": "ĐỀ CHƯƠNG 2", "at": 2.2},
     {"kind": "calendar", "x": 280, "y": 1260, "s": 0.5, "pages": ["XONG: T6"], "tearAt": []}]),
 SC("b09", "payoff", "desk", "tdev-modal", C(0.74, "left", "standing", "talking", "happy"), line("b09", "focused"),
    ("tdev-modal: callback clip-02 RỐI → CHIA NHỎ, clip-01 NẾU 21:00", "chia nhỏ"), [S("pop", 1.4, "chia nhỏ"), S("tick", 3.6, "chín giờ tối")],
    [{"kind": "sign", "x": 280, "y": 900, "s": 0.5, "rot": -2, "text": "RỐI → CHIA NHỎ", "at": 1.2},
     {"kind": "sign", "x": 280, "y": 1200, "s": 0.45, "rot": 3, "text": "21:00 → VIỆC 1", "at": 3.4}]),
 SC("b10", "cta", "grid", "cut", C(0.74, "left", "standing", "talking", "happy"), line("b10", "happy"),
    ("mmx-pop-over (spring duy nhất): sticky CUỐI TUẦN LÀM rớt khỏi móc (loop hook), COMMENT 1 CHỮ", "Comment"), [S("swish", 0.4, "Bạn thấy đó"), S("pop", 6.0, "Comment")],
    [{"kind": "words", "x": 280, "y": 900, "s": 0.6, "words": ["COMMENT 1 CHỮ"], "dropAt": [5.8]}]),
]
ST = {
 "b01": ("Sticky CUỐI TUẦN LÀM treo lủng lẳng trên móc", "nhướng mày", None),
 "b01b": ("Lịch lật vèo mười hai tháng, sticky vẫn treo", "ngán ngẩm", "vế sau câu hỏi: treo cả năm"),
 "b02": ("Hiệp ngồi nhìn hai thẻ treo, thở dài", "ngán ngẩm", "nỗi đau cụ thể: dọn phòng, ôn thi"),
 "b03": ("Thẻ to đùng phình ra, Hiệp lùi lại", "bối rối", "nguyên nhân: chỉ có một cái tên to"),
 "b04": ("Thầy chỉ thước vào bảng Kruger & Evans", "ngạc nhiên", "bằng chứng 1 cho nguyên nhân"),
 "b05": ("Thầy lật bảng sang Steel, mũi tên vọt lên", "nghiêm túc", "bằng chứng 2: ngại thì để mai"),
 "b06": ("Thầy cắt phăng sợi dây treo thẻ", "dứt khoát", "rút thông điệp HTB 4.7"),
 "b07": ("Hiệp tick từng thẻ, ghế trống dần", "hào hứng", "làm mẫu với ví dụ dọn phòng"),
 "b08": ("Hiệp gạch thẻ ÔN THI, viết ĐỀ CHƯƠNG 2", "tự tin", "áp sang ví dụ ôn thi"),
 "b09": ("Hai thẻ callback bật ra cạnh Thầy", "thân thiện", "nối clip 1-2"),
 "b10": ("Sticky rớt khỏi móc, Thầy chìa tay mời", "ấm áp", "chốt và mời comment, loop về hook"),
}
for n, sc in enumerate(A, 1):
    a, r, lk = ST[sc["id"]]; sc["stage"] = {"action": a, "react": r}; sc["beat"] = f"clip-03.b{n:02d}"
    if lk: sc["link"] = lk
base = json.load(open('/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/spec.json'))
s = {k: base[k] for k in ("transition_sfx", "pacing")}
s.update({"id": "clip-03-final", "clip": "clip-03", "title": "Việc hứa cuối tuần mà để cả năm: chia việc lớn thành việc con (HTB 4.7)",
  "week": 1, "theme": "dark", "pillar": "1 Làm ít, xong nhiều", "story": "monologue Thầy (L-039), dọn phòng + ôn thi (L-040), hook câu hỏi mở (L-043)",
  "trend": "comment Apify 16/10 (final/trend-signals.md)", "voice_prefix": P,
  "revisions": [{"v": 3, "date": "2026-10-16", "note": "script v3 (Hiệp: không hay)"}, {"v": 8, "date": "2026-10-16", "note": "script v8 Hiệp chốt: hook câu hỏi mở, bằng chứng cụ thể, b04 «nó đâu có ít», b05 «để mai tính»"}, {"v": 9, "date": "2026-10-17", "note": "script v9: chỉ đổi b06 «Nói gọn lại là:» → «Vậy nên:» (rule-60); hook b01 giữ nguyên (rule-55 waived by Hiệp)"}],
  "cover": {"direction": "a", "theme": "dark", "series": "Làm ít, xong nhiều", "ep": 3, "hero": ["ĐỂ CẢ NĂM?", "CHIA NHỎ!"], "accent": 1, "strike": 0, "expression": "despair", "action": "reacting", "emote": "!", "tilt": -5},
  "hook": {"text": "CUỐI TUẦN LÀM", "scenes": ["b01", "b01b"], "format": "câu hỏi mở về nỗi đau (L-043)"},
  "engagement": [{"type": "relatable-question", "beat": "b01", "text": "Có việc gì bạn hứa cuối tuần làm"}, {"type": "comment-challenge", "beat": "b10", "text": "Comment một chữ cho mình biết nha!"},
                 {"type": "loop", "beat": "b10", "text": "cả năm", "hook_word": "cả năm"}],
  "voices": {"Thầy": "F5 · Thái Sơn speed 0.9"},
  "throughline": "Ai cũng hứa cuối tuần làm VÀ ghi việc bằng một cái tên to đùng, NHƯNG nhìn tên thì tưởng ít nên ngợp, ngại rồi để cả năm, VÌ VẬY chia nhỏ ra trước rồi mới tính giờ, mới bắt tay",
  "hook_question": {"asked": "có việc gì bạn hứa cuối tuần mà để cả năm chưa đụng tới?", "answered": "không phải lười, việc to quá: chia nhỏ ra trước"},
  "structure": {"hook": ["b01", "b01b"], "intro": ["b02", "b03"], "body": ["b04", "b05", "b06", "b07", "b08", "b09"], "summary": ["b10"], "cta": ["b10"]},
  "hook_alt": {"type": "direct", "text": "Việc để cả năm không phải vì bạn lười."},
  "callbacks": ["clip-01 (4.1 nếu-thì 21:00)", "clip-02 (4.9 rối thì chia nhỏ)"],
  "parts": [{"id": "A", "engine": "remotion", "scenes": A}]})
json.dump(s, open(D + 'spec.json', 'w'), ensure_ascii=False, indent=2)
print("VI words", sum(len(re.sub(r"\*", "", l["text"]).split()) for sc in A for l in sc["lines"]))
