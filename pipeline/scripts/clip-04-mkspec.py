"""clip-04 v3.1 spec generator (script LOCKED by Hiep 18/10, hook C1). Dialogue EXACT from script-final v3.1.
New props book/sheet (L-050 meaning-by-objects, zero doodle). voice_prefix c04v1, Thay only F5 Thai Son 0.9."""
import json, re
D = '/workspace/oneup-studio/content/clips/clip-04-gap-sach-tu-kiem/final/'
P = 'c04v1'
RAW = [
("b01", "Bạn tưởng mình **hay quên** hả?", "Bạn tưởng mình {nhấn: hay quên} hả?", "You think you just forget easily?", ["forget"]),
("b01b", "Không đâu, bạn đọc cả tối mà đầu vẫn **trống** — vì bạn có **nhớ gì đâu** mà quên.", "Không đâu, bạn đọc cả tối mà đầu vẫn {nhấn: trống} —|vì bạn có {nhấn: nhớ gì đâu} mà quên.", "No — you read all night and your head is still empty, because you never actually remembered it in the first place.", ["empty,", "remembered"]),
("b02", "Nghe vậy có tức không? Như ôn thi hay học tiếng Anh, mình đọc đi đọc lại, gạch chi chít, mà chữ vẫn **chưa vô đầu**.", "Nghe vậy có tức không?|Như ôn thi hay học tiếng Anh,|mình đọc đi đọc lại, gạch chi chít,|mà chữ vẫn {nhấn: chưa vô đầu}.", "Stings to hear that, doesn't it? Exam prep, English — rereading and highlighting everything, and it still won't stick.", ["Stings", "stick."]),
("b03", "Vậy tại mình đọc chưa đủ hả? Không hẳn đâu. Đọc lại chỉ làm mắt **quen mặt chữ**, thấy quen nên tưởng thuộc, chứ chưa tự nhớ lại lần nào.", "Vậy tại mình đọc chưa đủ hả?|Không hẳn đâu.|Đọc lại chỉ làm mắt {nhấn: quen mặt chữ},|thấy quen nên tưởng thuộc,|chứ chưa tự nhớ lại lần nào.", "Is it because you didn't read enough? Not really — rereading only makes your eyes recognise the page. Familiar feels like learned, but you never had to recall it.", ["enough?", "recognise", "recall"]),
("b04", "Vậy sao biết mình **thuộc thiệt**? Yang và cộng sự gom **222 nghiên cứu**, hơn **48 ngàn** học sinh: có kiểm tra nhỏ thì điểm **cao hơn**, ở mức vừa.", "Vậy sao biết mình {nhấn: thuộc thiệt}?|Yang và cộng sự gom {nhấn: hai trăm hai mươi hai nghiên cứu},|hơn {nhấn: bốn mươi tám ngàn} học sinh:|có kiểm tra nhỏ thì điểm {nhấn: cao hơn}, ở mức vừa.", "So how do you know you really learned it? Yang et al. pooled 222 studies, over 48,000 students: classes with small quizzes scored higher — a medium effect.", ["really", "222", "48,000", "higher"]),
("b05", "Nghe kiểm tra, bạn nghĩ bài thi hả? Không, đó là tự kiểm lúc học. Dunlosky xếp **mười cách học**, cách này ở nhóm **cao nhất**, đọc lại, gạch chân ở nhóm **thấp nhất**.", "Nghe kiểm tra, bạn nghĩ bài thi hả?|Không, đó là tự kiểm lúc học.|Đun lốt ki xếp {nhấn: mười cách học},|cách này ở nhóm {nhấn: cao nhất},|đọc lại, gạch chân ở nhóm {nhấn: thấp nhất}.", "Tests sound like exams, right? No — this is testing yourself while studying. Dunlosky ranked ten methods: self-testing in the top tier; rereading and highlighting in the bottom tier.", ["exams,", "ten", "top", "bottom"]),
("b06", "Vậy đọc lại bỏ luôn hả? Không hẳn, tác dụng nó hẹp hơn thôi. Học xong, **gấp sách lại** tự kiểm trước, đừng quay đầu **đọc lại** ngay.", "Vậy đọc lại bỏ luôn hả?|Không hẳn, tác dụng nó hẹp hơn thôi.|Học xong, {nhấn: gấp sách lại} tự kiểm trước,|đừng quay đầu {nhấn: đọc lại} ngay.", "So rereading is useless? Not quite — its effect is just narrower. Finish a section, close the book and test yourself first, instead of turning straight back to reread.", ["useless?", "narrower.", "close", "reread."]),
("b07", "Tự kiểm làm sao đây? Như mình nè: học xong một phần, mình **gấp sách lại**, ghi ra những gì còn nhớ, rồi mở sách coi sai chỗ nào.", "Tự kiểm làm sao đây?|Như mình nè: học xong một phần,|mình {nhấn: gấp sách lại}, ghi ra những gì còn nhớ,|rồi mở sách coi sai chỗ nào.", "How do you self-test? Like me: finish a section, close the book, write down what I remember, then open it to check where I went wrong.", ["self-test?", "close", "remember,", "wrong."]),
("b08", "Còn ôn thi, tiếng Anh thì sao? Thay vì đọc một chương ba lần, mình gấp lại, tự nói **chương này nói gì**. Bí chỗ nào là chưa thuộc chỗ đó.", "Còn ôn thi, tiếng Anh thì sao?|Thay vì đọc một chương ba lần,|mình gấp lại, tự nói {nhấn: chương này nói gì}.|Bí chỗ nào là chưa thuộc chỗ đó.", "What about exams or English? Instead of rereading a chapter three times, close it and say what it was about. Where you get stuck is what you haven't learned.", ["exams", "three", "about.", "stuck"]),
("b09", "Bài dài quá, kiểm sao hết? Nhớ clip trước không, bài dài thì **chia nhỏ ra** trước. Học xong phần nào, kiểm ngay phần đó.", "Bài dài quá, kiểm sao hết?|Nhớ clíp trước không,|bài dài thì {nhấn: chia nhỏ ra} trước.|Học xong phần nào, kiểm ngay phần đó.", "But what if it's long? Remember last clip: split the big pile first. Finish one small bundle, then test yourself on just that bundle.", ["long?", "split", "bundle,"]),
("b10", "Quay lại sáng mai coi, đâu phải mình học dở. Mắt quen chữ thôi, đầu chưa **tự nhớ** lần nào. Tối nay bạn nhớ được **mấy ý**? Comment một con số nha!", "Quay lại sáng mai coi,|đâu phải mình học dở.|Mắt quen chữ thôi, đầu chưa {nhấn: tự nhớ} lần nào.|Tối nay bạn nhớ được {nhấn: mấy ý}?|Com men một con số nha!", "Back to that next-morning moment: see, you're not bad at studying — your eyes got familiar, your brain never recalled. Tonight, how many ideas can you remember? Comment a number!", ["bad", "recalled.", "many", "number!"]),
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
def SC(id, part, bg, tr, cast, ln, fx, sfx, props, push=0.06):
    return {"id": id, "beat": f"clip-04.{id}", "part": part, "role": "Thầy", "background": bg, "framing": "medium", "push": push,
         "transition": tr, "cast": [cast], "fx": {"visual": fx[0], "word": fx[1]}, "sfx": sfx, "props": props, "lines": [ln]}
S = lambda n, off, w: {"name": n, "atLine": 0, "offset": off, "word": w}
BK = lambda **kw: dict({"kind":"book","x":300,"y":1020,"s":0.85}, **kw)
SH = lambda **kw: dict({"kind":"sheet","x":470,"y":1250,"s":0.48}, **kw)
A = [
 SC("b01","hook","desk","cut",C(0.72,"left","sitting","talking","happy"),line("b01","surprised"),
    ("Sach mo day, Hiep gat gu tu tin doc (mmx-glide lat trang)","hay quên"),[S("swish",0.2,"hay quên")],
    [BK(state="open"), SH(inkLines=0)],push=0.14),
 SC("b01b","hook","desk","cut",C(0.72,"left","sitting","idle","despair"),line("b01b","sad"),
    ("Cut cung ngay 'Khong dau': sach gap lai, giay van trang, Hiep om dau","trống"),[S("snap",0.0,"Không đâu"),S("stamp",1.9,"trống")],
    [BK(state="closed"), SH(inkLines=0)],push=0.14),
 SC("b02","struggle","desk","cut",C(0.72,"left","sitting","talking","confused"),line("b02","focused"),
    ("Sach mo lai lat lai nhieu vong (mmx-accel-exit), Hiep ngap","chưa vô đầu"),[S("swish",3.3,"đọc đi đọc lại"),S("pop",4.6,"gạch chi chít"),S("tick",6.2,"chưa vô đầu")],
    [BK(state="open",flipAt=3.3), SH(inkLines=0)]),
 SC("b03","struggle","desk","cut",C(0.72,"left","standing","talking","confused"),line("b03","confused"),
    ("Trang sach troi qua mat nhu bang chuyen (mmx-cruise), sach gap, but dung tren giay trang","quen mặt chữ"),[S("swish",3.4,"quen mặt chữ"),S("snap",6.9,"chưa tự nhớ lại")],
    [BK(state="open",flipAt=3.4,closeAt=6.9), SH(inkLines=0)],push=0),
 SC("b04","evidence","desk","cut",C(0.72,"left","standing","talking","surprised"),line("b04","focused"),
    ("The nghien cuu khong chu xep chong cao (tdev-stagger), to kiem nho, chong nho len vua","cao hơn"),[S("ding",2.2,"Yang"),S("pop",2.4,"222 nghiên cứu"),S("rise",7.3,"cao hơn")],
    [{"kind":"sheet","x":260,"y":1130,"s":0.65,"inkLines":0},{"kind":"sheet","x":290,"y":990,"s":0.65,"inkLines":0},{"kind":"sheet","x":265,"y":850,"s":0.65,"inkLines":0}, SH(inkLines=2,inkAt=7.3)]),
 SC("b05","evidence","grid","tdev-panel",C(0.74,"left","standing","talking","focused"),line("b05","focused"),
    ("Bo tu kiem o chong cao, chong sach doc lai o thap (ti le cao/thap, tdev-stagger)","cao nhất"),[S("pop",0.5,"bài thi"),S("tick",4.4,"mười cách học"),S("ding",6.1,"cao nhất"),S("tick",7.6,"thấp nhất")],
    [{"kind":"bundles","x":270,"y":800,"s":0.6,"count":1,"at":1.5}, BK(x=270,y=1270,s=0.6,state="closed")],push=0),
 SC("b06","payoff","desk","cut",C(0.72,"left","standing","talking","focused"),line("b06","focused"),
    ("Sach tu gap lai dung chu 'gap sach lai' (prop book bien doi trong canh, push-in 0.10)","gấp sách lại"),[S("snap",4.3,"gấp sách lại"),S("pen",5.2,"tự kiểm trước")],
    [BK(state="open",closeAt=4.3), SH(inkLines=0)],push=0.10),
 SC("b07","payoff","desk","cut",C(0.72,"left","sitting","talking","happy"),line("b07","focused"),
    ("Giay trang day dan dong muc khong doc duoc, mo sach doi chieu chi cho thieu","ghi ra những gì còn nhớ"),[S("pen",3.6,"ghi ra những gì còn nhớ"),S("swish",6.3,"mở sách"),S("tick",7.1,"sai chỗ nào")],
    [BK(state="closed",openAt=6.3), SH(inkLines=6,inkAt=3.6,inkStagger=0.5)]),
 SC("b08","payoff","desk","cut",C(0.72,"left","standing","talking","focused"),line("b08","focused"),
    ("Lat chuong nhanh bi chan, gap sach tu noi roi khung that 0.4s, mo dung trang bi","chương này nói gì"),[S("swish",2.2,"ba lần"),S("snap",3.9,"gấp lại"),S("pop",7.2,"chưa thuộc chỗ đó")],
    [BK(state="open",flipAt=2.2,closeAt=3.9,openAt=7.2,s=0.95,x=290), SH(inkLines=3,inkAt=-9)]),
 SC("b09","payoff","grid","cut",C(0.74,"left","standing","talking","happy"),line("b09","focused"),
    ("Callback L-050: pile cao tach thanh 3 bundles trong canh, om 1 bo gap + ghi kiem bo do","chia nhỏ ra"),[S("pop",3.2,"chia nhỏ ra"),S("snap",5.2,"Học xong phần nào"),S("pen",5.4,"kiểm ngay phần đó"),S("tick",6.2,"kiểm ngay phần đó")],
    [{"kind":"pile","x":320,"y":900,"s":0.75,"until":3.4},{"kind":"bundles","x":300,"y":1080,"s":0.62,"at":3.2}, SH(inkLines=2,inkAt=5.4)],push=0),
 SC("b10","cta","desk","cut",C(0.72,"left","standing","talking","happy"),line("b10","happy"),
    ("Loop b01: cung bo cuc sach gap, giay gio co dong; Hiep chi xuong cho con so","mấy ý"),[S("swish",0.3,"sáng mai"),S("pop",5.8,"mấy ý"),S("tick",7.7,"một con số")],
    [BK(state="closed"), SH(inkLines=4,inkAt=-9)],push=0.06),
]
ST = {
 "b01": ("Hiep ngoi doc sach day, gat gu tu tin", "tu tin", None),
 "b01b": ("Sach gap lai, Hiep om dau nhin camera, giay van trang", "tuyet vong", "cut cung tu hook: tu tin sup thanh trong rong"),
 "b02": ("Hiep lat sach lai lan hai, lan ba, ngap", "buc minh", "bat phan ung tuc sau cau che o b01"),
 "b03": ("Trang troi qua mat ba lan, but dung tren giay trang", "bo roi", "chua vo dau -> tai doc chua du?"),
 "b04": ("Hiep chi vao chong the nghien cuu cao, to kiem nho tren ban", "ngac nhien", "lam sao biet thuoc thiet -> bang chung Yang"),
 "b05": ("Hiep nhin hai chong cao/thap, lac dau go so bai thi", "nghiêm tuc", "kiem tra nghe nhu bai thi -> Dunlosky xep hang"),
 "b06": ("Hiep dinh mo sach lai thi dung, sach tu gap lai", "dut khoat", "doc lai bo luon? -> khong han, gap sach truoc"),
 "b07": ("Hiep gap sach, ghi ra giay, mo sach doi chieu chi cho thieu", "hao hung", "tu kiem lam sao -> lam mau ghi ra doi chieu"),
 "b08": ("Hiep gap sach chuong day tu noi, khung lai roi mo dung trang", "tu tin roi bo roi", "on thi/tieng Anh thi sao -> bi o dau la chua thuoc o do"),
 "b09": ("Hiep chia chong bai day thanh ba bo gon, om mot bo ghi kiem", "nhe nhom", "bai dai kiem sao het -> callback chia nho clip-03"),
 "b10": ("Hiep ha tay, nhin camera cho con so, giay da co dong", "am ap", "quay lai sang mai o b01 nhung giay da khac"),
}
for n, sc in enumerate(A, 1):
    a, r, lk = ST[sc["id"]]; sc["stage"] = {"action": a, "react": r}; sc["beat"] = f"clip-04.b{n:02d}"
    if lk: sc["link"] = lk
base = json.load(open('/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/spec.json'))
s = {k: base[k] for k in ("transition_sfx", "pacing")}
s.update({"id": "clip-04-final", "clip": "clip-04", "title": "Ban co nho gi dau ma quen: gap sach tu kiem (HTB 23.14)",
  "week": 1, "theme": "dark", "pillar": "Hoc dung cach", "story": "monologue Thay (L-039), on thi + tieng Anh (L-040), hook cau hoi mo C1 (L-043), L-050 meaning-by-objects zero-doodle",
  "trend": "trend 2026-10-17 plan-1 (final/trend-signals ref in script)", "voice_prefix": P,
  "revisions": [{"v": "3.1", "date": "2026-10-18", "note": "script v3.1 LOCKED by Hiep 18/10: hook C1, dialogue exact, per-scene production direction; book/sheet new props"}],
  "cover": {"direction": "a", "theme": "dark", "series": "Hoc dung cach", "ep": 4, "hero": ["CO NHO GI DAU?", "GAP SACH!"], "accent": 1, "strike": 0, "expression": "despair", "action": "reacting", "emote": "!", "tilt": -5},
  "hook": {"text": "CO NHO GI DAU MA QUEN", "scenes": ["b01", "b01b"], "format": "hook C1 che thang (L-043); no on-screen hook text per L-050 direction v3.1 (rule-55 narration waiver)"},
  "engagement": [{"type": "relatable-question", "beat": "b01", "text": "Bạn tưởng mình hay quên hả?"}, {"type": "comment-challenge", "beat": "b10", "text": "Comment một con số nha!"},
                 {"type": "loop", "beat": "b10", "text": "Quay lại sáng mai coi", "hook_word": "trống"}],
  "voices": {"Thầy": "F5 · Thái Sơn speed 0.9"},
  "throughline": "Bạn đọc cả tối mà đầu vẫn trống VÀ tưởng mình hay quên, NHƯNG đọc lại chỉ làm mắt quen mặt chữ chưa tự nhớ lần nào, VÌ VẬY học xong gấp sách tự kiểm trước rồi mới mở ra đối chiếu",
  "hook_question": {"asked": "ban tuong minh hay quen ha?", "answered": "khong phai quen: chua nho lan nao; gap sach tu kiem"},
  "structure": {"hook": ["b01", "b01b"], "intro": ["b02", "b03"], "body": ["b04", "b05", "b06", "b07", "b08", "b09"], "summary": ["b10"], "cta": ["b10"]},
  "hook_alt": {"type": "direct", "text": "Doc den lan thu ba van thay quen. Gap sach lai moi biet: quen mat chu thoi, dau thi trong rong."},
  "callbacks": ["clip-03 (chia nho ra truoc)"],
  "parts": [{"id": "A", "engine": "remotion", "scenes": A}]})
json.dump(s, open(D + 'spec.json', 'w'), ensure_ascii=False, indent=2)
print("VI words", sum(len(re.sub(r"\*", "", l["text"]).split()) for sc in A for l in sc["lines"]))
