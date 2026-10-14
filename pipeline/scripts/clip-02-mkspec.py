import json
D='/workspace/oneup-studio/content/clips/clip-02-procrastination-discomfort/final/'
def L(text,en,hlw,phr,emo="focused",sset=None):
    ws=en.split(); hl=[]
    for w in hlw:
        idx=[i for i,x in enumerate(ws) if x.strip('.,:;!?“”"').lower()==w.strip('.,:;!?“”"').lower() and i not in hl]
        assert idx,(w,en); hl.append(idx[0])
    d={"speaker":"hiep","emotion":emo,"text":text,"en":en,"hl":hl,"phrases":[{"t":p} for p in phr]}
    if sset: d["set"]={"hiep":sset}
    return d
def SC(id,beat,part,bg,tr,cast,lines,fx,sfx,framing="medium",push=0.04,narr=None,props=None):
    d={"id":id,"beat":f"clip-02.{beat}","part":part,"background":bg,"framing":framing,"push":push,"transition":tr,"cast":[cast],"lines":lines,"fx":{"visual":fx[0],"word":fx[1]},"sfx":sfx}
    if narr: d["narration"]=narr
    if props: d["props"]=props
    return d
def SE(id,beat,motion,lines,hits,fx):
    return {"id":id,"beat":f"clip-02.{beat}","part":"explain","motion":motion,"lines":lines,"hits":[{"id":a,"f":b,"sfx":c,"word":w} for a,b,c,w in hits],"fx":{"visual":fx[0],"word":fx[1]}}
H=lambda x,pose="sitting",act="typing",ex="focused":{"id":"hiep","x":x,"facing":"right","pose":pose,"action":act,"expression":ex}
A=[SC("b01","b01","hook","desk","cut",H(0.74,act="idle",ex="sad"),[L("Tính năng Omi.","The Omi feature.",["Omi"],["Tính năng Omi."],"sad")],
      ("Hook cut 1: zoom mạnh vào màn hình laptop 'Omi feature · TODO', chữ hook to ngay frame 0; dấu đỏ POSTPONED đóng xuống","Omi"),[{"name":"stamp","atLine":0,"offset":0.0,"word":"Omi"}],framing="medium",push=0.16,narr="OMI FEATURE: HOÃN. HOÃN. HOÃN.",
      props=[{"kind":"laptop","x":330,"y":1330,"s":0.8,"text":"Omi feature","sub":"0 dòng code","stamp":"HOÃN","at":0.0}]),
   SC("b01b","b01","hook","desk","cut",H(0.86,act="idle",ex="confused"),[L("Hoãn hôm nay. Hoãn ngày mai. Rồi lại hoãn.","Not today. Not tomorrow. Again.",["Again."],["Hoãn hôm nay.","Hoãn ngày mai.","Rồi lại hoãn."],"sad")],
      ("Hook cut 2: 3 tờ lịch HÔM QUA / HÔM NAY / MAI xé liên tiếp theo từng chữ 'hoãn', camera giật nhẹ mỗi nhịp","hoãn"),[{"name":"click","atLine":0,"offset":0.0,"word":"Hoãn"},{"name":"click","atLine":0,"offset":0.76,"word":"Hoãn"},{"name":"stamp","atLine":0,"offset":1.5,"word":"lại hoãn"}],framing="medium",push=0.12,
      props=[{"kind":"calendar","x":360,"y":1010,"s":0.8,"rot":-4,"pages":["HÔM NAY","MAI","TUẦN SAU","THÁNG SAU"],"tearAt":[0.0,0.76,1.5]}]),
   SC("b01c","b01","hook","desk","cut",H(0.5,act="idle",ex="sad"),[L("Toang thật rồi.","It's over.",["over."],["Toang thật rồi."],"sad")],
      ("Hook cut 3: cận mặt Hiệp, giọt nước mắt, nền tối dần (vignette), chữ TOANG! đập xuống rung","Toang"),[{"name":"stamp","atLine":0,"offset":0.0,"word":"Toang"}],framing="medium",push=0.12,
      props=[{"kind":"vignette","at":0.0,"dark":0.6},{"kind":"words","x":540,"y":300,"s":1.45,"words":["TOANG!"],"dropAt":[0.0]}]),
   SC("b02","b02","struggle","desk","cut",H(0.42,act="typing",ex="sad"),[L("Mở code ra, năm giây sau đã lướt TikTok.","Open the code… five seconds later: TikTok.",["TikTok."],["Mở code ra,","năm giây sau đã lướt TikTok."],"sad",{"action":"idle","expression":"sad"}),
       L("Chán nản, tội lỗi, rồi tự mắng: mình lười quá.","Drained, guilty: “I'm so lazy.”",["guilty:","lazy."],["Chán nản, tội lỗi,","rồi tự mắng: {ừm} mình lười quá."],"sad")],
      ("Comic: tay rời bàn phím sang điện thoại (màn hình sáng), rồi Hiệp gục xuống; 3 chữ CHÁN NẢN / TỘI LỖI / LƯỜI rơi xuống đè lên đầu (squash)","tội lỗi"),[{"name":"pop","atLine":0,"offset":1.6,"word":"TikTok"},{"name":"stamp","atLine":1,"offset":2.5,"word":"lười"}],
      props=[{"kind":"laptop","x":300,"y":1330,"s":0.62,"text":"Omi feature","sub":"đang mở…"},{"kind":"phone","x":800,"y":1120,"s":0.95,"rot":8,"at":1.5,"text":"TikTok"},
             {"kind":"cloud","x":360,"y":300,"s":0.7,"at":2.1,"words":["CHÁN NẢN","TỘI LỖI","LƯỜI"],"dropAt":[2.33,2.95,4.55]}]),
   SC("b03","b03","turn","paper","iris",H(0.5,pose="standing",act="thinking",ex="surprised"),[L("Nhưng nghiên cứu nói: thường đâu phải lười. Mình đang né một cảm giác.","Research says: usually not lazy. You're dodging a feeling.",["not","dodging"],["Nhưng nghiên cứu nói:","thường đâu phải lười.","Mình đang né một cảm giác."],"focused",{"action":"reacting"})],
      ("Comic: iris mở sang giấy trắng, chữ 'LƯỜI' bị bút gạch, Hiệp ngẩng lên nhận ra","né một cảm giác"),[{"name":"pen","atLine":0,"offset":1.6,"word":"đâu phải lười"}])]
E=[SE("e01","b04","label-reveal",[L("Trì hoãn là né cảm giác khó chịu: chán, sợ làm dở, hay không biết bắt đầu. Nghe quen không?","Procrastination = dodging discomfort: boredom, fear of failing, no clear start. Sound familiar?",["dodging","discomfort:","familiar?"],["Trì hoãn là né cảm giác khó chịu:","chán, sợ làm dở,","hay không biết bắt đầu.","Nghe quen không?"])],
      [("shield",0.2,"swish" if False else "pop","né"),("faces",0.7,"tick","chán")],("Một việc (thẻ 'Báo cáo') tỏa ra 3 'gai' cảm xúc Chán / Sợ làm dở / Không biết bắt đầu; mũi tên né cong vòng qua thẻ","khó chịu")),
   SE("e02","b05","count-up",[L("Gộp sáu trăm chín mươi mốt hệ số tương quan: việc càng khó chịu, càng thấy mình kém, càng dễ hoãn.","691 correlations: the nastier the task and the lower your confidence, the more you delay.",["691","nastier","confidence,"],["Gộp sáu trăm chín mươi mốt hệ số tương quan:","việc càng khó chịu,","càng thấy mình kém,","càng dễ hoãn."])],
      [("count",0.02,"rise","sáu trăm chín mươi mốt"),("bars",0.75,"ding","càng dễ hoãn")],("Số 691 đếm lên; 2 thanh trượt 'Task feels bad' và 'I can't do it' cùng tăng, kim 'Delay' vọt lên theo","sáu trăm chín mươi mốt")),
   SE("e03","b06","scale-tip",[L("Vì phần thưởng ở xa, cái khó chịu ở ngay bây giờ. Nên điện thoại thắng.","Because the reward is far away, the discomfort is right now. So the phone wins.",["far","now.","phone"],["Vì phần thưởng ở xa,","cái khó chịu ở ngay bây giờ.","Nên điện thoại thắng."])],
      [("tip",0.62,"snap","bây giờ"),("win",0.9,"ding","điện thoại thắng")],("Cái cân: bên trái 'phần thưởng' nhỏ dần khi trượt xa trên trục thời gian, bên phải icon điện thoại; cân nghiêng hẳn về phía điện thoại","ở xa")),
   SE("e04","b07","question-card",[L("Nên trước khi làm, hỏi một câu: việc này khó chịu ở chỗ nào?","So before you start, ask: what exactly feels bad here?",["ask:","bad"],["Nên trước khi làm,","hỏi một câu:","việc này khó chịu ở chỗ nào?"])],
      [("q",0.55,"pop","khó chịu ở chỗ nào")],("Thẻ câu hỏi lớn '?' lật ra (card-flip), kính lúp soi vào thẻ 'Báo cáo' tìm chỗ gai","hỏi một câu")),
   SE("e05","b08","match-fix",[L("Không biết bắt đầu? Viết ba gạch đầu dòng. Sợ dở? Cho phép nháp xấu.","No clear start? Write 3 bullets. Afraid it'll be bad? Allow an ugly draft.",["3","bullets.","ugly"],["Không biết bắt đầu?","Viết ba gạch đầu dòng.","Sợ dở?","Cho phép nháp xấu."])],
      [("bullets",0.3,"pen","ba gạch đầu dòng"),("draft",0.85,"stamp","nháp xấu")],("Mỗi gai cảm xúc được 'gỡ' bằng một miếng vá: 3 gạch đầu dòng tự viết ra; con dấu 'DRAFT · OK' đóng lên tờ giấy nguệch ngoạc","gạch đầu dòng")),
   SE("e06","b09","timer",[L("Thấy chán? Hẹn mười phút, hết giờ thì được dừng.","Bored? Set 10 minutes. When it rings, you may stop.",["10","stop."],["Thấy chán?","Hẹn mười phút,","hết giờ thì được dừng."])],
      [("timer",0.35,"tick","mười phút"),("ring",0.85,"ding","được dừng")],("Đồng hồ hẹn giờ 10:00 quay ngược, vòng tiến độ chạy; chuông reo, biển 'STOP OK' bật lên","mười phút")),
   SE("e07","b10","mistake-stamp",[L("Lỗi hay gặp: mắng mình rồi gồng. Mắng xong, việc càng khó chịu.","Common mistake: scold yourself and force it. That makes the task feel worse.",["Common","mistake:","worse."],["Lỗi hay gặp:","mắng mình rồi gồng.","Mắng xong, việc càng khó chịu."])],
      [("stamp",0.35,"stamp","mắng mình"),("worse",0.85,"rise","càng khó chịu")],("Bong bóng 'Mình lười quá!' bị dấu đỏ '✕ KHÔNG GIÚP' đè lên; gai trên thẻ 'Báo cáo' dài thêm ra","mắng mình"))]
B=[SC("b11","b11","payoff","paper","cut",H(0.66,pose="standing",act="talking",ex="focused"),[L("Lưu ý: nghiên cứu này là tương quan, chỉ cho thấy hướng. Lưu lại, lần sau hoãn thì mở ra.","Note: correlational, a pattern only. Save this for the next time you stall.",["correlational,","Save"],["Lưu ý:","nghiên cứu này là tương quan,","chỉ cho thấy hướng.","Lưu lại, lần sau hoãn thì mở ra."])],
      ("Comic: Hiệp giơ ngón tay, bảng nhỏ 'tương quan khác nhân quả'; icon bookmark nảy lên ở chữ 'lưu lại'","tương quan"),[{"name":"tick","atLine":0,"offset":1.0,"word":"tương quan"},{"name":"pop","atLine":0,"offset":3.4,"word":"Lưu lại"}],
      props=[{"kind":"sign","x":400,"y":930,"s":0.72,"rot":-5,"text":"CHỈ LÀ TƯƠNG QUAN","at":1.0}]),
   SC("b12","b12","cta","grid","slide",H(0.5,pose="standing",act="talking",ex="happy"),[L("Việc bạn đang hoãn khó chịu chỗ nào? Comment một chữ.","What feels bad about the task you're avoiding? One word in the comments.",["bad","One"],["Việc bạn đang hoãn","khó chịu chỗ nào?","Comment một chữ."],"happy"),
      L("Còn tính năng Omi? Mình đi hỏi câu đó đây.","And the Omi feature? Asking myself right now.",["Omi"],["Còn tính năng Omi?","Mình đi hỏi câu đó đây."],"happy",{"action":"reacting"})],
      ("Comic: slide sang lưới, Hiệp chỉ vào người xem; câu cuối quay lại màn hình 'Omi feature' như hook (loop), Hiệp mở laptop","Omi"),[{"name":"ding","atLine":1,"offset":0.1,"word":"hỏi câu đó"}])]
s={"id":"clip-02-final","clip":"clip-02","title":"Trì hoãn = né cảm giác khó chịu, không phải lười (Steel 2007)","week":1,"theme":"dark","pillar":"1 Làm ít, xong nhiều",
 "story":"S-02 Omi feature (Hiệp xác nhận 14/10, DL-047)","trend":"‘vừa than bị dí deadline vừa lướt TikTok’ (vtcnews.vn; câu chung, không phải chuyện thật của Hiệp)",
 "revisions":[{"date":"2026-10-14","dl":"DL-044","note":"gate-1 draft: info-complete script + rule-52 effects table + template-A cover (rule 54)"}],
 "transition_sfx":{"part":"whoosh-soft","scene":"swish"},
 "cover":{"direction":"a","theme":"dark","series":"Làm ít, xong nhiều","ep":2,"hero":["LƯỜI?","ĐANG NÉ!"],"accent":1,"strike":0,"expression":"sad","action":"reacting","emote":"!","tilt":-5},
 "cover_options":[{"hero":["LƯỜI?","ĐANG NÉ!"],"picked":True},{"hero":["HOÃN MÃI","VÌ SỢ"]},{"hero":["TỰ MẮNG","VÔ ÍCH"]}],
 "hook":{"text":"OMI FEATURE: HOÃN. HOÃN. HOÃN.","scenes":["b01","b01b","b01c"]},
 "engagement":[{"type":"relatable-question","beat":"e01","text":"Nghe quen không?"},{"type":"save-prompt","beat":"b11","text":"Lưu lại, lần sau hoãn thì mở ra."},{"type":"comment-challenge","beat":"b12","text":"Comment một chữ."},{"type":"loop","beat":"b12","text":"Còn tính năng Omi?","hook_word":"Omi"}],
 "parts":[{"id":"A","engine":"remotion","transitionOut":"slideleft","scenes":A},{"id":"E","engine":"hyperframes","dir":"explainer","transitionOut":"circleopen","sections":E},{"id":"B","engine":"remotion","scenes":B}]}
json.dump(s,open(D+'spec.json','w'),ensure_ascii=False,indent=2)
import re
n=sum(len(re.sub(r"\{[^}]*\}|\*","",l["text"]).split()) for p in s["parts"] for x in p.get("scenes",p.get("sections",[])) for l in x["lines"])
print("VI words",n)
