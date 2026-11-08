"""clip-04 v14 spec generator. Dialogue EXACT from final/script-v14.md as locked by Hiep 'chot' 2026-10-20.
DO NOT change a word. voice_prefix c04v14, Thay only F5 Thai Son speed 0.9 (voice-phrase-f5.py hardcodes 0.9).
Parts: A remotion b01-b05, E hyperframes b06-b07, B remotion b08-b10. End card appended at assemble stage (ffmpeg, 2s)."""
import json, re, shutil, os
D='/workspace/oneup-studio/content/clips/clip-04-gap-sach-tu-kiem/final/'
P='c04v14b'  # v14b 20/10: F5 speed 1.0 regen (Rule Reviewer QA), 4 EN chunks restored by splitting lines (words unchanged)
# lines: (scene, text_with_bold, phrases_with_nhan_pipe_split_by_|_as_list, en_chunk, hl_words, emotion)
# Each entry = ONE spec line (caption chunk <=8 words). Phrases are the | splits inside that line.
L=[]
def add(sc, text, phrases, en, hl, emo):
    L.append(dict(sc=sc,text=text,phrases=phrases,en=en,hl=hl,emo=emo))
# b01
add("b01","Học thuộc tối qua, sáng dậy **quên sạch**?",["Học thuộc tối qua, sáng dậy {nhấn: quên sạch}?"],"Memorized last night, forgotten this morning?",["forgotten"],"surprised")
add("b01","**Không nhìn sách**, bạn có thể nhớ được những gì?",["{nhấn: Không nhìn sách},","bạn có thể nhớ được những gì?"],"Without looking, what can you recall?",["recall"],"focused")
# b02
add("b02","Ví dụ học từ tiếng Anh để đi du lịch.",["Ví dụ học từ tiếng Anh để đi du lịch."],"Example: thirty English travel words",["English"],"neutral")  # delivery rev3: no break «tiếng Anh / để đi»
add("b02","Tối đọc đi đọc lại.",["Tối đọc đi đọc lại."],"Reread them again that night",["Reread"],"focused")
add("b02","Ba mươi từ, tới **thuộc làu**.",["Ba mươi từ, tới {nhấn: thuộc làu}."],"Until they felt fluent",["fluent"],"focused")
add("b02","Tưởng mai nhớ hết.",["Tưởng mai nhớ hết."],"Thought I'd remember everything tomorrow",["remember"],"happy")
# b03
add("b03","Sáng dậy, gấp sách viết lại.",["Sáng dậy, gấp sách viết lại."],"Morning: closed book, wrote back",["closed"],"focused")
add("b03","airport, hotel, ticket, passport.",["airport,","hotel,","ticket,","passport."],"airport, hotel, ticket, passport",["passport"],"focused")
L[-1]["keep"]=True; L[-1]["respell_en"]=True  # F5: one unit per word (no merge) -> clear break between the 4 words (QA b03b)
add("b03","Tới từ thứ năm, hành lý. **Bút dừng**.",["Tới từ thứ năm, hành lý.","{nhấn: Bút dừng}."],"At fifth word, pen stopped",["stopped"],"surprised")
L[-1]["keep"]=True  # prosody-plan: pause (period) before the stressed 'Bút dừng'; do not merge short units
add("b03","Không nhớ từ tiếng Anh.",["Không nhớ từ tiếng Anh."],"Couldn't recall English word",["recall"],"sad")
# b04
add("b04","Mình chột dạ. Hay tối qua chỉ nhìn chữ đến **quen mắt**?",["Mình chột dạ.","Hay tối qua chỉ nhìn chữ đến {nhấn: quen mắt}?"],"Had I only looked until familiar?",["familiar"],"confused")
L[-1]["keep"]=True
add("b04","**Giấy trắng** sau passport.",["{nhấn: Giấy trắng} sau passport."],"Blank after passport on paper",["Blank"],"sad")
add("b04","Dừng ở đó.",["Dừng ở đó."],"I stopped right there",["stopped"],"sad")
# b05
add("b05","Viết không ra, mình **mở sách**.",["Viết không ra, mình {nhấn: mở sách}."],"When stuck, open book",["open"],"focused")
add("b05","Xem đúng chỗ bí: **luggage**.",["Xem đúng chỗ bí: {nhấn: luggage}."],"Check stuck spot: luggage",["luggage"],"focused")
add("b05","Gấp lại, viết tiếp.",["Gấp lại, viết tiếp."],"Close book, keep writing",["writing"],"happy")
# b06 (hyperframes e06)
add("b06","Yang gộp **222 nghiên cứu**.",["Yang gộp {nhấn: 222 nghiên cứu}."],"Yang pooled 222 studies",["222"],"focused")
add("b06","Hơn 48 ngàn học sinh.",["Hơn 48 ngàn học sinh."],"Over 48,000 students total",["48,000"],"focused")
add("b06","Lớp có kiểm nhỏ.",["Lớp có kiểm nhỏ."],"Small quizzes in class",["quizzes"],"focused")
add("b06","Điểm cao hơn mức vừa.",["Điểm cao hơn mức vừa."],"Modestly higher scores overall",["higher"],"focused")
# b07 (hyperframes e07)
add("b07","Dunlosky xếp mười cách.",["Dunlosky xếp mười cách."],"Dunlosky ranked ten methods",["ranked"],"focused")
add("b07","Tự kiểm nằm **nhóm cao nhất**.",["Tự kiểm nằm {nhấn: nhóm cao nhất}."],"Self-testing in highest group",["highest"],"focused")
add("b07","Đọc lại, gạch chân nằm nhóm thấp nhất.",["Đọc lại, gạch chân nằm nhóm thấp nhất."],"Rereading, highlighting in lowest group",["lowest"],"focused")
add("b07","Vẫn có ích. Tác dụng hẹp.",["Vẫn có ích.","Tác dụng hẹp."],"Still helps, but narrowly",["helps"],"neutral")
L[-1]["keep"]=True
# b08
add("b08","Mình chia ba mươi thẻ thành **ba chồng**.",["Mình chia ba mươi thẻ thành {nhấn: ba chồng}."],"Thirty cards in three piles",["three"],"focused")
add("b08","Mỗi chồng mười thẻ.",["Mỗi chồng mười thẻ."],"Ten cards in each pile",["Ten"],"focused")
add("b08","Học xong chồng đầu.",["Học xong chồng đầu."],"Finish first pile, close book",["Finish"],"happy")
add("b08","Gấp sách, viết lại đúng chồng đó.",["Gấp sách, viết lại đúng chồng đó."],"Write that pile back",["Write"],"happy")
# b09
add("b09","Sáng hôm sau, quay lại giấy đó.",["Sáng hôm sau, quay lại giấy đó."],"Next morning, same paper again",["Next"],"happy")
add("b09","Sách vẫn gấp. **Viết trước**.",["Sách vẫn gấp.","{nhấn: Viết trước}."],"Book still closed, wrote first",["closed"],"focused")
L[-1]["keep"]=True
add("b09","Lần này viết thêm được **luggage**.",["Lần này viết thêm được {nhấn: luggage}."],"Added luggage this time",["luggage"],"happy")
# b10
add("b10","**Luggage** bí sáng hôm trước.",["{nhấn: Luggage} bí sáng hôm trước."],"Luggage stuck previous morning",["stuck"],"focused")
add("b10","Sáng hôm sau tự viết được,",["Sáng hôm sau tự viết được,"],"Next morning wrote it myself",["myself"],"happy")
add("b10","không cần sách.",["không cần sách."],"Without opening the book",["opening"],"happy")
add("b10","Bạn viết lại được mấy từ?",["Bạn viết lại được mấy từ?"],"How many words for you?",["many"],"focused")
add("b10","Comment con số đó nha.",["Comment con số đó nha."],"Comment that number below",["Comment"],"happy")

# verify spoken text (strip bold) concatenated per scene equals v14 exactly (word sequence)
V14={
"b01":"Học thuộc tối qua, sáng dậy quên sạch? Không nhìn sách, bạn có thể nhớ được những gì?",
"b02":"Ví dụ học từ tiếng Anh để đi du lịch. Tối đọc đi đọc lại. Ba mươi từ, tới thuộc làu. Tưởng mai nhớ hết.",
"b03":"Sáng dậy, gấp sách viết lại. airport, hotel, ticket, passport. Tới từ thứ năm, hành lý. Bút dừng. Không nhớ từ tiếng Anh.",
"b04":"Mình chột dạ. Hay tối qua chỉ nhìn chữ đến quen mắt? Giấy trắng sau passport. Dừng ở đó.",
"b05":"Viết không ra, mình mở sách. Xem đúng chỗ bí: luggage. Gấp lại, viết tiếp.",
"b06":"Yang gộp 222 nghiên cứu. Hơn 48 ngàn học sinh. Lớp có kiểm nhỏ. Điểm cao hơn mức vừa.",
"b07":"Dunlosky xếp mười cách. Tự kiểm nằm nhóm cao nhất. Đọc lại, gạch chân nằm nhóm thấp nhất. Vẫn có ích. Tác dụng hẹp.",
"b08":"Mình chia ba mươi thẻ thành ba chồng. Mỗi chồng mười thẻ. Học xong chồng đầu. Gấp sách, viết lại đúng chồng đó.",
"b09":"Sáng hôm sau, quay lại giấy đó. Sách vẫn gấp. Viết trước. Lần này viết thêm được luggage.",
"b10":"Luggage bí sáng hôm trước. Sáng hôm sau tự viết được, không cần sách. Bạn viết lại được mấy từ? Comment con số đó nha."}
from collections import defaultdict
got=defaultdict(str)
for l in L: got[l["sc"]]+= (" " if got[l["sc"]] else "")+l["text"].replace("**","")
for k,v in V14.items():
    assert got[k]==v, (k,got[k],v)
for l in L: assert len(l["en"].split())<=8, l
print("text-lock OK, lines",len(L))

# say: respell foreign names for F5 (display text unchanged)
SAY={"Yang":"Giang","Dunlosky":"Đun lốt ki","Comment":"Com men","airport":"e pọt","hotel":"hô ten","ticket":"tích kịt","passport":"pát pọt","luggage":"lắc ghịt"}
def mkline(l, idx_in_scene):
    t=l["text"]; say=re.sub(r"\{nhấn: ([^}]*)\}",r"\1"," ".join(l["phrases"]))
    for a,b in SAY.items(): say=re.sub(rf"\b{a}\b",b,say)
    phr=[]
    for p_ in l["phrases"]:
        q=p_
        if l.get("respell_en"):
            for a,b in [("airport","e pọt"),("hotel","hô ten"),("ticket","tích kịt"),("passport","pát pọt")]: q=q.replace(a,b)
        for a,b in [("Yang","Giang"),("Dunlosky","Đun lốt ki"),("222","hai trăm hai mươi hai"),("48 ngàn","bốn mươi tám ngàn"),("Comment","Com men"),("luggage","lắc ghịt"),("Luggage","Lắc ghịt")]:
            q=q.replace(a,b)
        phr.append(q)
    ws=l["en"].split(); hl=[]
    for w in l["hl"]:
        i=[j for j,x in enumerate(ws) if x.lower().strip(",.:?")==w.lower().strip(",.:?")]
        assert i,(w,l["en"]); hl.append(i[0])
    key=l["sc"]+("ab"[idx_in_scene] if False else "")  # voice_file set after counting lines per scene
    return {"speaker":"hiep","emotion":l["emo"],"text":t,"say":say,"en":l["en"],"hl":hl,
            "phrases":[dict({"t":p},**({"keep":True} if l.get("keep") else {})) for p in phr],"voice_role":"Thầy"}
from collections import Counter
cnt=Counter(l["sc"] for l in L); seen=Counter()
lines_by={}
for l in L:
    seen[l["sc"]]+=1; idx=seen[l["sc"]]-1
    ln=mkline(l,idx)
    suffix=("abcdef"[idx] if cnt[l["sc"]]>1 else "")
    # voice-phrase stitch keys: scene id + a/b... only first two letters used in old code ('ab'[li]); our scenes have <=4 lines -> patch gen to use abcd
    ln["voice_file"]=f"voice/{P}-{l['sc']}{suffix}.wav"
    lines_by.setdefault(l["sc"],[]).append(ln)

def C(x=0.72,pose="sitting",act="talking",ex="focused",facing="left"):
    return {"id":"hiep","x":x,"facing":facing,"pose":pose,"action":act,"expression":ex}
def SFX(n,off,w,atLine=0): return {"name":n,"atLine":atLine,"offset":off,"word":w}
BK=lambda **kw: dict({"kind":"book","x":300,"y":1020,"s":0.85},**kw)
SH=lambda **kw: dict({"kind":"sheet","x":470,"y":1250,"s":0.48},**kw)
SCHED={"kind":"sheet","x":185,"y":620,"s":0.30,"rot":7,"inkLines":3,"inkAt":0}
PILE={"kind":"pile","x":300,"y":900,"s":0.55}
# pen prop (FLUX QA 20/10): tip position keys [t_scene, x, y] in frame px; stops = motionless. Butt under chibi hand (~619,1378).
PEN=lambda keys,rot=22: {"kind":"pen","x":0,"y":0,"s":1,"rot":rot,"len":200,"keys":keys}
PEN_STOP=[[0,434,1306]]
B03_KEYS=[[0,409,1206],[2.1,409,1206],[2.48,514,1206],[2.55,409,1231],[2.93,514,1231],[3.0,409,1256],[3.38,514,1256],[3.45,409,1281],[3.83,514,1281],[4.2,409,1306],[4.4,409,1306],[5.05,434,1306]]
def SC(id,part,bg,tr,cast,fx,sfx,props,push=0.05,trans="cut"):
    return {"id":id,"beat":f"clip-04.{id}","part":part,"role":"Thầy","background":bg,"framing":"medium","push":push,"transition":trans,"cast":[cast],"fx":{"visual":fx[0],"word":fx[1]},"sfx":sfx,"props":props,"lines":lines_by[id]}
A=[
 SC("b01","hook","desk","cut",C(act="idle",ex="surprised"),("mmx-cut-on-motion: but dung tren giay trang dung nhip cau hoi, sach gap day sang ben (frame 0)","quên sạch"),[SFX("snap",0.0,"quên sạch")],[BK(state="closed"),SH(inkLines=0),PEN([[0,430,1228],[0.15,430,1228],[0.75,472,1246]],rot=38)],push=0.14),
 SC("b02","struggle","desk","cut",C(ex="happy"),("mmx-cruise: mot trang lat deu lap lai, chong the giu nguyen","thuộc làu"),[SFX("swish",0.5,"đọc đi đọc lại")],[BK(state="open",flipAt=1.2),dict(SCHED),PILE]),
 SC("b03","struggle","desk","cut",C(act="talking",ex="focused"),("mmx-glide: tay glide doc giay, but dung o cho trang sau 4 vet dong","Bút dừng"),[SFX("pen",0.5,"viết lại")],[BK(state="closed"),dict(SCHED),SH(inkLines=4,inkAt=2.1,inkStagger=0.45),PEN(B03_KEYS)]),
 SC("b04","struggle","desk","cut",C(act="idle",ex="confused"),("mmx-cruise cham: sach VAN GAP, but nam yen canh giay trang","Giấy trắng"),[SFX("swish",0.5,"quen mắt")],[BK(state="closed"),dict(SCHED),SH(inkLines=4,inkAt=-3),PEN(PEN_STOP)]),
 SC("b05","payoff","desk","cut",C(ex="focused"),("mmx-snap-settle: sach MO dung mot lan o cho bi roi gap lai, tay settle tren giay","mở sách"),[SFX("pop",0.3,"mở sách"),SFX("pen",2.0,"viết tiếp")],[BK(state="closed",openAt=0.8),dict(SCHED),SH(inkLines=4,inkAt=-3),PEN(PEN_STOP)]),
]
B=[
 SC("b08","payoff","desk","cut",C(pose="standing",ex="focused"),("tdev-stagger: pile tach 3 bundles, om chong dau viet lai","ba chồng"),[SFX("pop",0.4,"ba chồng"),SFX("pen",2.5,"viết lại")],[BK(state="closed"),dict(SCHED),{"kind":"bundles","x":255,"y":990,"s":0.5,"count":3}]),
 SC("b09","payoff","desk","cut",C(ex="happy"),("mmx-soft-land: quay ve giay cu, them dung 1 vet dong moi o cho trang","luggage"),[SFX("swish",0.2,"Sáng hôm sau"),SFX("pop",3.0,"luggage")],[BK(state="closed"),dict(SCHED),SH(inkLines=5,inkAt=-1.4,inkStagger=0.9)]),
 SC("b10","cta","desk","cut",C(ex="happy"),("mmx-soft-land: giu khung giay da co them dong, chi nhe xuong duoi","Luggage"),[SFX("pop",0.2,"Luggage"),SFX("tick",3.5,"con số")],[BK(state="closed"),dict(SCHED),SH(inkLines=5,inkAt=0)]),
]
def SEC(id,beat,fx,hits):
    return {"id":id,"beat":beat,"part":"evidence","motion":"tdev-stagger","fx":{"visual":fx[0],"word":fx[1]},"hits":hits,"lines":lines_by[beat.split(".")[-1]]}
E=[SEC("e06","clip-04.b06",("tdev-stagger: 2 chong bai kiem khong chu + 2 thanh diem khong chu, thanh co kiem nho cao hon mot doan vua","222 nghiên cứu"),[{"id":"papers","f":0.15,"sfx":"ding","word":"Yang"},{"id":"bars","f":0.55,"sfx":"rise","word":"cao hơn"}]),
   SEC("e07","clip-04.b07",("tdev-stagger: 10 the trang thanh hang, bo tu kiem chong cao, chong doc lai/gach chan o thap van dung yen","nhóm cao nhất"),[{"id":"cards","f":0.2,"sfx":"tick","word":"mười cách"},{"id":"high","f":0.5,"sfx":"ding","word":"cao nhất"}])]
# stage/link info (rule-58/60 manual fields used by old specs)
STAGE={"b01":("Sach gap day sang ben, giay trang, but dung ngay frame dau","sung, dau cu the"),"b02":("Lat trang deu toi khuya, chong 30 the con du","tu tin sai"),"b03":("Viet 4 vet dong roi but dung o cho trang","sung, khung that"),"b04":("But nam yen canh giay trang, sach van gap","chot da, tu hoi"),"b05":("Mo sach dung cho bi mot lan, gap lai viet tiep","quyet tam nhe"),"b06":("2 chong bai kiem + thanh diem tren cung ban hoc","chac chan, muc vua"),"b07":("10 the trang, chong cao/thap canh sach giay","ro rang, tran an"),"b08":("Pile tach 3 bundles, om chong dau","nhe dau, viec nho lai"),"b09":("Cung to giay cu, them 1 vet dong o cho trang","am, thang nho"),"b10":("Nhin camera, chi nhe xuong duoi","am, dut")}
LINKS={"b02":"callback hook: toi hom truoc cua cau quen sach","b03":"sang day cua toi b02, phep thu gap sach","b04":"chot da ngay tai cho trang cua b03","b05":"xu ly dung cho bi vua dung o b04","b06":"bang chung cho viec vua lam o b05","b07":"xep hang bo sung cho bang chung b06","b08":"ap cach tu kiem vao chong the cua b02","b09":"sang hom sau quay lai dung to giay b03","b10":"payoff dung tu luggage o b05/b09, callback cau hoi hook"}
for sc in A+B:
    a,r=STAGE[sc["id"]]; sc["stage"]={"action":a,"react":r}
    if sc["id"] in LINKS: sc["link"]=LINKS[sc["id"]]
for sec in E:
    bk=sec["beat"].split(".")[-1]; a,r=STAGE[bk]; sec["stage"]={"action":a,"react":r}; sec["link"]=LINKS[bk]
A[0]["narration"]="HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?"  # L-067: on-screen text MUST keep diacritics
base=json.load(open('/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/spec.json'))
s={k:base[k] for k in ("transition_sfx","pacing")}
s.update({"id":"clip-04-final","clip":"clip-04","title":"Gấp sách tự kiểm (HTB 23.14) - script v14 locked","week":1,"theme":"dark","pillar":"Học đúng cách","story":"monologue Thay (L-039), vi du 30 tu tieng Anh di du lich (minh hoa), L-050 meaning-by-objects zero-doodle, L-059 bang canh 9 cot trong script-v14.md","trend":"supporting-signal only: final/trend-signals.md (HTB 23.14 topic, khong trend-driven)","voice_prefix":P,
 "revisions":[{"v":"v14","date":"2026-10-20","note":"Hiep 'chot' script-v14: loi nguyen van v14 khong sua chu; spec moi c04v14, F5 Thai Son 0.9, Remotion b01-b05/b08-b10 + HyperFrames b06-b07, end card 2s credit CC BY 4.0"}],
 "cover":{"direction":"a","theme":"dark","series":"Học đúng cách","ep":4,"hero":["HỌC THUỘC TỐI QUA?","SÁNG QUÊN SẠCH!"],"accent":1,"strike":0,"expression":"despair","action":"reacting","emote":"!","tilt":-5},
 "hook":{"text":"HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?","scenes":["b01"],"format":"pain point truc tiep + cau hoi gan pain (Hiep chot nguyen van b01); hinh frame 0: sach gap, giay trang, but dung"},
 "engagement":[{"type":"relatable-question","beat":"b01","text":"Không nhìn sách, bạn có thể nhớ được những gì?"},{"type":"comment-challenge","beat":"b10","text":"Comment con số đó nha."},{"type":"loop","beat":"b10","text":"Luggage bí sáng hôm trước","hook_word":"quên sạch"}],
 "voices":{"Thầy":"F5 · Thái Sơn speed 0.9"},
 "throughline":"Học thuộc tối qua VÀ sáng dậy quên sạch, NHƯNG chỉ nhìn chữ thì quen mắt chưa tự nhớ lần nào, VÌ VẬY gấp sách tự viết lại, chia nhỏ thẻ và sáng hôm sau viết trước khi mở sách",
 "hook_question":{"asked":"Không nhìn sách, bạn có thể nhớ được những gì?","answered":"viet lai duoc may tu; luggage bi sang hom truoc, sang hom sau tu viet duoc"},
 "structure":{"hook":["b01"],"intro":["b02","b03","b04"],"body":["b05","b06","b07","b08"],"summary":["b09"],"cta":["b10"]},
 "hook_alt":{"type":"direct","text":"(giu nguyen hook Hiep chot o b01, khong dung hook_alt)"},
 "callbacks":[],
 "parts":[{"id":"A","engine":"remotion","transitionOut":"fade","scenes":A},{"id":"E","engine":"hyperframes","dir":"explainer","transitionOut":"fade","sections":E},{"id":"B","engine":"remotion","scenes":B}]})
json.dump(s,open(D+'spec.json','w'),ensure_ascii=False,indent=2)
print("spec written")
