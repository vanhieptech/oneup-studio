"""clip-03 v3 spec generator (HTB 4.7, Thầy monologue, meme 'bản chất' stems, L-039/L-040).
Meta (cover, pacing, transition_sfx) modelled on clip-02; voice via build-final --stage voice-phrase (prefix c03v3)."""
import json, re
D = '/workspace/oneup-studio/content/clips/clip-03-big-task-chunking/final/'
P = 'c03v3'
# key, display text, spoken phrases ('|' split, {nhấn:}), en, highlight words
RAW = [
("b01", "Thì cái **bản chất**…", "Thì cái|{nhấn: bản chất}...", "So what's the essence…", ["essence…"]),
("b01b", "…của cái việc hứa «**cuối tuần** dọn phòng»… là gì?", "của cái việc hứa|{nhấn: cuối tuần} dọn phòng...|là gì?", "…of promising \"I'll clean my room this weekend\"?", ["clean"]),
("b03", "Thứ nhất là các bạn phải ghi **gọn** một chữ: «dọn phòng», **không** chia gì hết.", "Thứ nhất là|các bạn phải ghi {nhấn: gọn} một chữ:|dọn phòng,|{nhấn: không} chia gì hết.", "First: write just \"clean room\", no breakdown at all.", ["no"]),
("b04", "Thứ hai là đứng giữa phòng mà **không biết** bắt đầu từ đâu… thì nằm xuống **lướt** điện thoại.", "Thứ hai là|đứng giữa phòng|mà {nhấn: không biết} bắt đầu từ đâu...|thì nằm xuống {nhấn: lướt} điện thoại.", "Second: no idea where to start… so lie down and scroll.", ["scroll."]),
("b06", "Và cuối cùng là các bạn phải tự hứa «**cuối tuần** sau», rồi ba tháng sau… cái ghế vẫn là **tủ đồ**.", "Và cuối cùng là|các bạn phải tự hứa|{nhấn: cuối tuần} sau,|rồi ba tháng sau...|cái ghế vẫn là {nhấn: tủ đồ}.", "And finally: promise \"next weekend\"… three months later, the chair is still the closet.", ["closet."]),
("b07", "Nghe quen hông? Mà các nhà khoa học nói: Kruger và Evans thấy **liệt kê** việc con ra trước rồi mới ước giờ thì ước **bớt hụt**. Còn Steel thấy việc càng ngán càng bị **đẩy** về sau.", "Nghe quen hông?|Mà các nhà khoa học nói:|Cru gơ và Ê vần thấy|{nhấn: liệt kê} việc con ra trước|rồi mới ước giờ|thì ước {nhấn: bớt hụt}.|Còn Xtiu thấy|việc càng ngán|càng bị {nhấn: đẩy} về sau.", "Sound familiar? List subtasks first, then estimate: you underestimate less. And the more you dread it, the more it's pushed back.", ["List", "pushed"]),
("b08", "Vậy việc lớn phải **chia thành việc con** rồi mới ước giờ, mới bắt tay. Nghiên cứu mới thấy hướng thôi, chưa có con số. Mà «dọn phòng» hóa ra là **cả chục việc** đó.", "Vậy việc lớn|phải {nhấn: chia thành việc con}|rồi mới ước giờ,|mới bắt tay.|Nghiên cứu mới thấy hướng thôi,|chưa có con số.|Mà dọn phòng|hóa ra là {nhấn: cả chục việc} đó.", "Split big work into subtasks, then estimate, then start. Only the direction is known. \"Clean room\" is really a dozen tasks.", ["subtasks,", "dozen"]),
("b09", "Chuẩn chia: mỗi việc con xong trong **một lần làm**. Gom áo trên ghế. Dọn mặt bàn. Bỏ rác dưới gầm giường. Cộng giờ từng phần mới ra **hạn thật**. Chia vừa thôi, chia vụn quá cũng mệt.", "Chuẩn chia:|mỗi việc con xong|trong {nhấn: một lần làm}.|Gom áo trên ghế.|Dọn mặt bàn.|Bỏ rác dưới gầm giường.|Cộng giờ từng phần|mới ra {nhấn: hạn thật}.|Chia vừa thôi,|chia vụn quá cũng mệt.", "Each subtask fits one go: clear the chair, clean the desk, bag the trash. Add up the parts for a real deadline.", ["one", "real"]),
("b09c", "Ôn thi cũng vậy: không ghi «ôn thi», mà ghi «**làm một đề chương hai**». Như clip trước: rối thì **chia nhỏ**; clip đầu: chín giờ tối, ở đâu, làm **thẻ đầu tiên**.", "Ôn thi cũng vậy:|không ghi ôn thi,|mà ghi {nhấn: làm một đề chương hai}.|Như clíp trước: rối thì {nhấn: chia nhỏ};|clíp đầu: chín giờ tối, ở đâu,|làm {nhấn: thẻ đầu tiên}.", "Not \"study\", but \"one practice test, chapter 2\". Messy? Split it. 9 p.m., a set place, card one.", ["Split", "one."]),
("b10", "Vậy đó, không phải lười, việc **to quá** thôi. Việc to nhất bạn đang treo tên gì? Comment một chữ nha!", "Vậy đó,|không phải lười,|việc {nhấn: to quá} thôi.|Việc to nhất bạn đang treo|tên gì?|Com men một chữ nha!", "Not lazy, the task's just too big. Comment one word!", ["big.", "Comment"]),
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
 SC("b01", "hook", "grid", "cut", C(0.72, "left", "standing", "talking", "focused"), line("b01", "focused"),
    ("mmx-oversize-land: Thầy gõ thước, chữ hook đập frame 0", "bản chất"), [S("stamp", 0.0, "bản chất")], [], narr="BẢN CHẤT LÀ GÌ?", push=0.14),
 SC("b01b", "hook", "bed", "cut", C(0.72, "left", "sitting", "idle", "despair"), line("b01b", "focused"),
    ("Cắt cứng: phòng ngập đồ, lịch lật 3 cuối tuần (tdev-text-swap)", "cuối tuần"), [S("swish", 0.0, "của cái việc"), S("pop", 1.0, "cuối tuần")],
    [{"kind": "calendar", "x": 260, "y": 1000, "s": 0.6, "pages": ["T7", "T7 SAU", "T7 NỮA"], "tearAt": [1.2, 2.0]}], push=0.14),
 SC("b03", "struggle", "bed", "cut", C(0.72, "left", "standing", "talking", "focused"), line("b03", "focused"),
    ("mmx-snap-settle: sticky DỌN PHÒNG to tướng", "gọn"), [S("stamp", 1.2, "gọn"), S("tick", 3.6, "không")],
    [{"kind": "sign", "x": 540, "y": 340, "s": 0.75, "rot": -3, "text": "DỌN PHÒNG", "at": 1.0}]),
 SC("b04", "struggle", "bed", "cut", C(0.72, "left", "sitting", "idle", "confused"), line("b04", "confused"),
    ("Chibi nhìn núi đồ rồi nằm lướt điện thoại (mmx-glide + mmx-cruise)", "lướt"), [S("snap", 1.6, "không biết"), S("swish", 3.8, "lướt")],
    [{"kind": "phone", "x": 260, "y": 1200, "s": 0.7, "rot": 8, "at": 3.6, "text": "TikTok"}]),
 SC("b06", "struggle", "bed", "cut", C(0.72, "left", "sitting", "idle", "despair"), line("b06", "focused"),
    ("mmx-accel-exit: tờ lịch bay T10 → T1, ghế vẫn chất áo", "tủ đồ"), [S("tick", 1.4, "cuối tuần"), S("stamp", 5.0, "tủ đồ")],
    [{"kind": "vignette", "at": 0.0, "dark": 0.45}, {"kind": "calendar", "x": 260, "y": 1000, "s": 0.6, "pages": ["T10", "T11", "T12", "T1"], "tearAt": [2.6, 3.1, 3.6]}]),
 SC("b07", "evidence", "paper", "mmx-soft-land", C(0.76, "left", "standing", "talking", "surprised"), line("b07", "focused"),
    ("bar-grow + mmx-soft-land: bảng KRUGER & EVANS 2004 → STEEL 2007", "liệt kê"), [S("ding", 3.0, "liệt kê"), S("stamp", 9.0, "đẩy")],
    [{"kind": "sign", "x": 280, "y": 900, "s": 0.5, "rot": -3, "text": "KRUGER & EVANS 2004", "at": 2.0},
     {"kind": "words", "x": 280, "y": 1180, "s": 0.55, "words": ["LIỆT KÊ → ƯỚC", "NGÁN → ĐẨY LÙI"], "dropAt": [3.0, 8.0]}]),
 SC("b08", "payoff", "desk", "tdev-stagger", C(0.74, "left", "standing", "talking", "happy"), line("b08", "focused"),
    ("tdev-stagger: DỌN PHÒNG nổ thành hàng thẻ nhỏ; nhãn CHỈ THẤY HƯỚNG", "chia thành việc con"), [S("stamp", 1.2, "chia thành việc con"), S("pop", 7.5, "cả chục việc")],
    [{"kind": "words", "x": 280, "y": 900, "s": 0.55, "words": ["ÁO", "BÀN", "RÁC", "SÀN"], "dropAt": [1.2, 1.4, 1.6, 1.8]},
     {"kind": "sign", "x": 280, "y": 1250, "s": 0.45, "rot": 2, "text": "CHỈ THẤY HƯỚNG", "at": 4.5}]),
 SC("b09", "payoff", "bed", "mmx-snap-settle", C(0.74, "left", "standing", "talking", "happy"), line("b09", "focused"),
    ("step-recap: 3 thẻ ghế trống · bàn sạch · túi rác ✓, mỗi thẻ 20'", "một lần làm"), [S("tick", 3.5, "gom áo"), S("tick", 4.8, "dọn mặt bàn"), S("tick", 6.0, "bỏ rác"), S("ding", 8.5, "hạn thật")],
    [{"kind": "words", "x": 280, "y": 880, "s": 0.55, "words": ["GOM ÁO ✓", "DỌN BÀN ✓", "BỎ RÁC ✓"], "dropAt": [3.4, 4.7, 5.9]},
     {"kind": "calendar", "x": 280, "y": 1260, "s": 0.5, "pages": ["TỐI T5"], "tearAt": []}]),
 SC("b09c", "payoff", "desk", "tdev-modal", C(0.74, "left", "sitting", "typing", "focused"), line("b09c", "focused"),
    ("tdev-text-swap ÔN THI → ĐỀ CHƯƠNG 2; tdev-modal thẻ NẾU 21:00 (callback clip-01)", "chia nhỏ"), [S("pop", 2.4, "làm một đề"), S("tick", 5.5, "chín giờ tối")],
    [{"kind": "sign", "x": 280, "y": 900, "s": 0.5, "rot": -2, "text": "ĐỀ CHƯƠNG 2", "at": 2.2},
     {"kind": "sign", "x": 280, "y": 1200, "s": 0.45, "rot": 3, "text": "NẾU 21:00 → THẺ 1", "at": 5.2}]),
 SC("b10", "cta", "grid", "cut", C(0.5, "right", "standing", "talking", "happy"), line("b10", "happy"),
    ("mmx-pop-over (spring duy nhất): COMMENT 1 CHỮ, xé sticky DỌN PHÒNG (loop hook)", "Comment"), [S("pop", 4.0, "Comment")],
    [{"kind": "words", "x": 540, "y": 360, "s": 1.0, "words": ["COMMENT 1 CHỮ"], "dropAt": [3.8]}]),
]
ST = {  # rule-60 stage (action ≥8 chars, react) + rule-62 link; beat ids numbered clip-03.bNN
 "b01": ("Thầy gõ thước xuống bàn, nheo mắt nhìn khán giả", "nghiêm giả bộ", None),
 "b01b": ("Hiệp ngồi giữa núi áo, lịch lật ba trang", "ngán ngẩm", "nói tiếp vế meme: đề bài cụ thể"),
 "b03": ("Thầy dán sticky to tướng lên tường", "mỉa mai", "Thứ nhất của meme: lỗi ghi việc to"),
 "b04": ("Hiệp đứng xoay vòng rồi đổ người xuống nệm", "bối rối", "Thứ hai: hậu quả của việc không chia"),
 "b06": ("Tờ lịch bay vèo vèo qua bốn tháng", "chán chường", "Và cuối cùng: vòng lặp hứa hẹn"),
 "b07": ("Thầy tháo kính, chỉ thước vào bảng nghiên cứu", "ngạc nhiên", "đổi giọng sang bằng chứng"),
 "b08": ("Sticky lớn vỡ thành hàng thẻ nhỏ", "vỡ lẽ", "rút ra thông điệp HTB 4.7 từ bằng chứng"),
 "b09": ("Thầy tick từng thẻ, ghế trống dần", "hào hứng", "cách làm cụ thể cho ví dụ dọn phòng"),
 "b09c": ("Thẻ ôn thi lật mặt, thẻ nếu-thì bật ra", "tự tin", "áp sang ví dụ thứ hai + callback clip 1-2"),
 "b10": ("Thầy quay thẳng ống kính, chìa tay mời", "thân thiện", "chốt và mời comment, loop về hook"),
}
for n, sc in enumerate(A, 1):
    a, r, lk = ST[sc["id"]]; sc["stage"] = {"action": a, "react": r}; sc["beat"] = f"clip-03.b{n:02d}"
    if lk: sc["link"] = lk
base = json.load(open('/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/spec.json'))
s = {k: base[k] for k in ("transition_sfx", "pacing")}
s.update({"id": "clip-03-final", "clip": "clip-03", "title": "Bản chất của việc hứa cuối tuần dọn phòng: chia việc lớn thành việc con (HTB 4.7)",
  "week": 1, "theme": "dark", "pillar": "1 Làm ít, xong nhiều", "story": "monologue Thầy (L-039), ví dụ dọn phòng + ôn thi (L-040)",
  "trend": "F06 'bản chất' meme + comment Apify 16/10 (final/trend-signals.md)", "voice_prefix": P,
  "revisions": [{"v": 3, "date": "2026-10-16", "note": "script v3 Hiệp duyệt (14:00): độc thoại Thầy, dọn phòng/ôn thi"}],
  "cover": {"direction": "a", "theme": "dark", "series": "Làm ít, xong nhiều", "ep": 3, "hero": ["DỌN PHÒNG?", "CHIA NHỎ!"], "accent": 1, "strike": 0, "expression": "despair", "action": "reacting", "emote": "!", "tilt": -5},
  "hook": {"text": "BẢN CHẤT LÀ GÌ?", "scenes": ["b01", "b01b"], "format": "meme 'Thì cái bản chất của cái việc… là gì?' monologue"},
  "engagement": [{"type": "relatable-question", "beat": "b07", "text": "Nghe quen hông?"}, {"type": "comment-challenge", "beat": "b10", "text": "Comment một chữ nha!"},
                 {"type": "loop", "beat": "b10", "text": "to quá", "hook_word": "bản chất"}],
  "voices": {"Thầy": "F5 · Thái Sơn speed 0.9"},
  "throughline": "Ai cũng hứa dọn phòng VÀ ghi gọn một chữ, NHƯNG việc to quá nên né mãi, VÌ VẬY chia thành việc con xong trong một lần làm rồi mới ước giờ",
  "hook_question": {"asked": "bản chất của việc hứa cuối tuần dọn phòng là gì?", "answered": "không phải lười, việc to quá: chia thành việc con"},
  "structure": {"hook": ["b01", "b01b"], "intro": ["b03", "b04", "b06"], "body": ["b07", "b08", "b09", "b09c"], "summary": ["b10"], "cta": ["b10"]},
  "hook_alt": {"type": "direct", "text": "Dọn phòng không xong không phải vì lười."},
  "callbacks": ["clip-01 (4.1 nếu-thì 21:00)", "clip-02 (4.9 rối thì chia nhỏ)"],
  "parts": [{"id": "A", "engine": "remotion", "scenes": A}]})
json.dump(s, open(D + 'spec.json', 'w'), ensure_ascii=False, indent=2)
print("VI words", sum(len(re.sub(r"\*", "", l["text"]).split()) for sc in A for l in sc["lines"]))
