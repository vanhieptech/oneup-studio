"""clip-02 v14 spec generator (meme 'bản chất' stem, Thầy + Hiệp-né). Lines/voice keys from v14 voice batch.
Loads the existing spec (keeps cover/meta), replaces parts/hook/engagement, appends a revision."""
import json, re, sys
D = '/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/'
# key, role, display text, spoken(say), en, hl words
RAW=[  # v15: say uses '|' = phrase split (L-036), {nhấn:}/{kéo:} = emphasis on the payload word
("b01","thay","Thì cái **bản chất** của cái việc mở laptop rồi lướt TikTok… là gì?","Thì cái {nhấn: bản chất}|của cái việc mở láp tóp rồi lướt Tíc Tóc...|là gì?","So what's the essence of opening your laptop… then scrolling TikTok?",["essence"]),
("b02","ne","Ờ… coi clip **xíu thôi** đã chứ, bạn ơi!","Ờ... coi clíp {nhấn: xíu thôi}|đã chứ, bạn ơi!","Uh… just a few clips first, buddy!",["few"]),
("b03","thay","Thứ nhất là các bạn phải **lướt** liên tục ở trên giường, ngón cái chạy như máy may, một cách lặp đi lặp lại.","Thứ nhất là|các bạn phải {nhấn: lướt} liên tục ở trên giường,|ngón cái chạy như máy may,|một cách {kéo: lặp đi lặp lại}.","First: scroll nonstop in bed, thumb running like a sewing machine, over and over.",["scroll","over"]),
("b04","ne","Clip nữa thôi… **clip nữa thôi**…","Clíp nữa thôi...|clíp {nhấn: nữa thôi}...","One more clip… just one more…",["more"]),
("b05","thay","Thứ hai là khi nào xuất hiện **cái cảm giác khó chịu** khi mở file để làm việc… thì phải đổi việc liền.","Thứ hai là {nhấn: khi nào}|xuất hiện {kéo: cái cảm giác khó chịu}|khi mở phai để làm việc...|thì phải đổi việc liền.","Second: the moment that uncomfortable feeling shows up when you open the work file… switch tasks fast.",["uncomfortable","switch"]),
("b06a","thay","Và cuối cùng là các bạn phải tự **chửi** bản thân mình cho đã — rồi mai lại né.","Và cuối cùng là|các bạn phải tự {nhấn: chửi} bản thân mình cho đã,|rồi mai lại né.","And finally: curse yourself out properly, then dodge again tomorrow.",["curse","tomorrow."]),
("b06b","ne","Đồ lười! Thôi **để mai**…","Đồ lười!|Thôi {nhấn: để mai}...","Lazy bum! Eh… tomorrow then…",["tomorrow"]),
("b07","thay","Nghe quen hông? Mà các nhà khoa học nói: Steel gom **691** kết quả — việc càng khó chịu, càng bị dời.","Nghe quen hông?|Mà các nhà khoa học nói:|Xtiu gom {nhấn: sáu trăm chín mươi mốt} kết quả,|việc càng khó chịu, càng bị dời.","Sound familiar? But scientists say: Steel pooled 691 results. The nastier the task, the more it gets delayed.",["familiar?","691","delayed."]),
("b08a","thay","Bạn trì hoãn **không phải vì lười**, mà vì đang né cái cảm giác khó chịu — nên đừng chửi mình, hãy làm bước đầu nhỏ tới mức hết khó chịu.","Bạn trì hoãn {nhấn: không phải vì lười},|mà vì đang né cái cảm giác khó chịu.|Nên đừng chửi mình,|hãy làm bước đầu {kéo: nhỏ} tới mức hết khó chịu.","You don't procrastinate because you're lazy. You're dodging a bad feeling. So don't scold yourself. Make the first step so small it stops feeling bad.",["lazy.","dodging","small"]),
("b08b","ne","À… mình đang **né** thiệt.","À...|mình đang {nhấn: né} thiệt.","Oh… I really am dodging.",["dodging."]),
("b09a","thay","Như vầy nè: sửa đúng **một dòng** thôi.","Như vầy nè:|sửa đúng {nhấn: một dòng} thôi.","Like this: fix just one line.",["one","line."]),
("b09b","ne","À… hết **đường né** luôn á.","À...|hết {nhấn: đường né} luôn á.","Oh… no way to dodge now.",["dodge"]),
("b10","ne","Không lười, chỉ đang **né**. Việc bạn đang né là gì? Comment một chữ nha!","Không lười,|chỉ đang {nhấn: né}.|Việc bạn đang né là gì?|Com men một chữ nha!","Not lazy, just dodging. What are you dodging? Comment one word!",["lazy,","dodging?","one"]),
]

LN = {k: (r, t, s, en, hw) for k, r, t, s, en, hw in RAW}
def line(k, emo):
    r, t, s, en, hw = LN[k]; ws = en.split(); hl = []
    for w in hw:
        i = [j for j, x in enumerate(ws) if x.lower() == w.lower() and j not in hl]; assert i, (w, en); hl.append(i[0])
    return {"speaker": "hiep", "emotion": emo, "text": t, "say": re.sub(r"\{(?:nhấn|kéo): ([^}]*)\}", r"\1", s.replace("|", " ")), "en": en, "hl": hl,
            "phrases": [dict({"t": p.strip()}, **({"emph": True} if "{nhấn:" in p or "{kéo:" in p else {})) for p in s.split("|")], "voice_pending": "v15 (L-036 per-clause F5)",
            "voice_role": "Thầy" if r == "thay" else "Hiệp-né"}
def C(x, facing, pose, act, ex): return {"id": "hiep", "x": x, "facing": facing, "pose": pose, "action": act, "expression": ex}
def SC(id, part, bg, tr, cast, lines, fx, sfx, props, narr=None, push=0.06):
    d = {"id": id, "beat": f"clip-02.{id}", "part": part, "role": lines[0]["voice_role"], "background": bg, "framing": "medium", "push": push,
         "transition": tr, "cast": [cast], "fx": {"visual": fx[0], "word": fx[1]}, "sfx": sfx, "props": props, "lines": lines}
    if narr: d["narration"] = narr
    return d
S = lambda n, li, off, w: {"name": n, "atLine": li, "offset": off, "word": w}
A = [
 SC("b01", "hook", "grid", "cut", C(0.72, "left", "standing", "talking", "focused"), [line("b01", "focused")],
    ("Smash: chữ BẢN CHẤT đập giữa khung, Thầy gõ thước; điện thoại TikTok bật lên", "bản chất"),
    [S("stamp", 0, 0.0, "bản chất"), S("pop", 0, 2.2, "TikTok")],
    [{"kind": "words", "x": 540, "y": 330, "s": 1.25, "words": ["BẢN CHẤT LÀ GÌ?"], "dropAt": [0.0]}, {"kind": "phone", "x": 300, "y": 1250, "s": 0.75, "at": 1.6, "text": "TikTok"}],
    narr="BẢN CHẤT LÀ GÌ?", push=0.14),
 SC("b02", "hook", "bed", "cut", C(0.5, "right", "sitting", "idle", "happy"), [line("b02", "happy")],
    ("Hiệp-né thò đầu ôm điện thoại, mắt lim dim; chữ XÍU THÔI? nảy", "xíu thôi"),
    [S("pop", 0, 0.6, "xíu thôi")], [{"kind": "phone", "x": 860, "y": 1250, "s": 0.7, "rot": 8, "at": 0.0, "text": "TikTok"}, {"kind": "words", "x": 540, "y": 330, "s": 1.0, "words": ["XÍU THÔI?"], "dropAt": [0.5]}]),
 SC("b03", "struggle", "bed", "cut", C(0.7, "left", "standing", "talking", "focused"), [line("b03", "focused")],
    ("Thầy chỉ thước vào điện thoại trên gối; ngón cái lặp như máy may", "lướt"),
    [S("tick", 0, 1.0, "lướt"), S("tick", 0, 3.4, "máy may")],
    [{"kind": "phone", "x": 300, "y": 1250, "s": 0.8, "at": 0.3, "text": "TikTok"}, {"kind": "sign", "x": 330, "y": 420, "s": 0.7, "rot": -3, "text": "THỨ NHẤT · LƯỚT LẶP", "at": 0.0}]),
 SC("b04", "struggle", "bed", "cut", C(0.5, "right", "sitting", "idle", "neutral"), [line("b04", "neutral")],
    ("Close-up ngón cái quẹt lia; mặt Hiệp-né đờ ra", "clip nữa thôi"),
    [S("swish", 0, 0.1, "Clip nữa thôi"), S("swish", 0, 1.3, "clip nữa thôi")],
    [{"kind": "phone", "x": 860, "y": 1250, "s": 0.8, "at": 0.0, "text": "TikTok"}, {"kind": "words", "x": 540, "y": 330, "s": 1.0, "words": ["CLIP NỮA THÔI"], "dropAt": [0.2]}]),
 SC("b05", "struggle", "desk", "slide", C(0.72, "left", "standing", "talking", "confused"), [line("b05", "confused")],
    ("File mở ra → sóng đỏ cảm giác khó chịu; Thầy chỉ sang chổi + app review đồ ăn", "cảm giác khó chịu"),
    [S("snap", 0, 1.8, "cảm giác khó chịu"), S("swish", 0, 5.0, "đổi sang việc khác")],
    [{"kind": "laptop", "x": 290, "y": 1330, "s": 0.7, "text": "oneup.swift", "sub": "KHÓ CHỊU", "at": 0.0}, {"kind": "sign", "x": 330, "y": 420, "s": 0.7, "rot": 3, "text": "THỨ HAI · ĐỔI VIỆC", "at": 4.8}]),
 SC("b06", "struggle", "bed", "cut", C(0.5, "right", "sitting", "idle", "despair"), [line("b06a", "focused"), line("b06b", "sad")],
    ("Chữ LƯỜI rơi đè Hiệp-né (rung); lịch xé sang MAI", "chửi"),
    [S("stamp", 0, 1.6, "chửi"), S("stamp", 1, 0.0, "Đồ lười")],
    [{"kind": "vignette", "at": 0.0, "dark": 0.5}, {"kind": "cloud", "x": 540, "y": 270, "s": 0.65, "at": 0.0, "words": ["LƯỜI!"], "dropAt": [1.6]},
     {"kind": "calendar", "x": 800, "y": 520, "s": 0.6, "pages": ["HÔM NAY", "MAI"], "tearAt": [3.2]}]),
 SC("b07", "evidence", "paper", "iris", C(0.7, "left", "standing", "talking", "surprised"), [line("b07", "focused")],
    ("Thầy tháo kính; bảng STEEL 2007 · 691 KẾT QUẢ; rồi bảng NÉ KHÓ CHỊU ≠ LƯỜI", "691"),
    [S("ding", 0, 3.0, "691"), S("stamp", 0, 8.0, "cảm giác khó chịu")],
    [{"kind": "sign", "x": 300, "y": 1150, "s": 0.6, "rot": -3, "text": "STEEL 2007 · 691 KẾT QUẢ", "at": 2.8}, {"kind": "sign", "x": 300, "y": 1330, "s": 0.6, "rot": 2, "text": "NÉ KHÓ CHỊU ≠ LƯỜI", "at": 7.8}]),
 SC("b08", "payoff", "desk", "cut", C(0.6, "left", "standing", "talking", "sad"), [line("b08a", "focused"), line("b08b", "surprised")],
    ("Takeaway: chữ LƯỜI bị gạch, thay bằng NÉ KHÓ CHỊU; bậc thang đầu tiên thu nhỏ còn 1 bậc tí xíu", "không phải vì lười"),
    [S("stamp", 0, 1.2, "không phải vì lười"), S("pop", 0, 6.0, "nhỏ")], [{"kind": "sign", "x": 330, "y": 420, "s": 0.7, "rot": -4, "text": "KHÔNG LƯỜI · ĐANG NÉ", "at": 0.8}]),
 SC("b09", "payoff", "desk", "slide", C(0.66, "left", "sitting", "typing", "happy"), [line("b09a", "focused"), line("b09b", "surprised")],
    ("Một dòng code sáng lên, dấu ✓ đóng xuống; Hiệp-né ngồi dậy", "một dòng"),
    [S("pop", 0, 1.8, "một dòng"), S("stamp", 1, 0.4, "đường né")],
    [{"kind": "laptop", "x": 280, "y": 1330, "s": 0.6, "text": "oneup.swift", "sub": "dòng 1 ✓", "at": 0.0}, {"kind": "sign", "x": 330, "y": 420, "s": 0.7, "rot": 3, "text": "1 DÒNG · HẾT ĐƯỜNG NÉ", "at": 1.6}]),
 SC("b10", "cta", "grid", "cut", C(0.5, "right", "standing", "talking", "happy"), [line("b10", "happy")],
    ("Hiệp-né quay thẳng camera; chữ BẠN ĐANG NÉ GÌ? (loop về hook 'né')", "Comment"),
    [S("pop", 0, 1.6, "Comment")], [{"kind": "vignette", "at": 0.0, "dark": 0.5}, {"kind": "words", "x": 540, "y": 360, "s": 1.1, "words": ["COMMENT 1 CHỮ"], "dropAt": [1.5]}]),
]
s = json.load(open(D + 'spec.json'))
s.update({"title": "Bản chất của việc mở laptop rồi lướt TikTok: né cảm giác khó chịu (Steel 2007)",
  "hook": {"text": "BẢN CHẤT LÀ GÌ?", "scenes": ["b01", "b02"], "format": "meme 'Thì cái bản chất của cái việc… là gì?' + chen ngang (v14)"},
  "engagement": [{"type": "relatable-question", "beat": "b07", "text": "Nghe quen hông?"}, {"type": "comment-challenge", "beat": "b10", "text": "Comment một chữ nha!"},
                 {"type": "loop", "beat": "b10", "text": "né", "hook_word": "bản chất"}],
  "voices": {"Thầy": "F5 · Thái Sơn speed 0.9", "Hiệp-né": "F5 · Thái Sơn speed 0.95, +2 semitone", "Omi": "không nói (đèn)"},
  "parts": [{"id": "A", "engine": "remotion", "scenes": A}]})
s["revisions"].append({"v": 15, "date": "2026-10-16", "dl": "L-036", "note": "v15 draft: Day 2 takeaway (4.9) at b08 + CTA echo, Thứ hai shortened, per-clause phrases + {nhấn:}/{kéo:} (chưa voice)"})
json.dump(s, open(D + 'spec.json', 'w'), ensure_ascii=False, indent=2)
n = sum(len(re.sub(r"\{[^}]*\}|\*", "", l["text"]).split()) for sc in A for l in sc["lines"]); print("VI words", n)
