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
A=[SC("b01","b01","hook","desk","cut",H(0.74,act="idle",ex="sad"),[L("POV: tính năng Omi.","POV: the Omi feature.",["Omi."],["POV: tính năng Omi."],"sad")],
      ("Hook cut 1 (format POV): push mạnh vào laptop 'Omi feature · 0 dòng code', chữ hook to ngay frame 0; dấu đỏ DỜI đóng xuống","Omi"),[{"name":"stamp","atLine":0,"offset":0.0,"word":"Omi"}],framing="medium",push=0.16,narr="POV: TÍNH NĂNG OMI · DỜI. DỜI. DỜI.",
      props=[{"kind":"laptop","x":330,"y":1330,"s":0.8,"text":"Omi feature","sub":"0 dòng code","stamp":"DỜI","at":0.0}]),
   SC("b01b","b01","hook","desk","cut",H(0.86,act="idle",ex="confused"),[L("Hôm nay dời. Mai lại dời.","Pushed today. Pushed again tomorrow.",["again"],["Hôm nay dời.","Mai lại dời."],"sad")],
      ("Hook cut 2: lịch DEADLINE xé 2 tờ HÔM NAY → MAI → MAI NỮA theo từng chữ 'dời', camera giật nhẹ mỗi nhịp","dời"),[{"name":"click","atLine":0,"offset":0.0,"word":"Hôm nay dời"},{"name":"stamp","atLine":0,"offset":0.8,"word":"lại dời"}],framing="medium",push=0.12,
      props=[{"kind":"calendar","x":360,"y":1010,"s":0.8,"rot":-4,"pages":["HÔM NAY","MAI","MAI NỮA"],"tearAt":[0.0,0.8]}]),
   SC("b01c","b01","hook","desk","cut",H(0.5,act="idle",ex="sad"),[L("Thành dự án ma luôn.","Now it's a ghost project.",["ghost"],["Thành dự án ma luôn."],"sad")],
      ("Hook cut 3 (meme 'dự án ma'): mặt Hiệp méo xệch, nền tối dần (vignette), chữ DỰ ÁN MA đập xuống rung","dự án ma"),[{"name":"stamp","atLine":0,"offset":0.25,"word":"dự án ma"}],framing="medium",push=0.12,
      props=[{"kind":"vignette","at":0.0,"dark":0.6},{"kind":"words","x":540,"y":300,"s":1.3,"words":["DỰ ÁN MA"],"dropAt":[0.25]}]),
   SC("b02","b02","struggle","desk","cut",H(0.42,act="typing",ex="sad"),[L("Thế là mở code, năm giây sau lướt TikTok.","So I open the code… five seconds later: TikTok.",["TikTok."],["Thế là mở code,","năm giây sau lướt TikTok."],"sad",{"action":"idle","expression":"sad"}),
       L("Rồi chán nản, tội lỗi, tự xỉ vả: lười quá.","Then drained, guilty, beating myself up: “so lazy.”",["guilty,","lazy."],["Rồi chán nản, tội lỗi,","tự xỉ vả: {ừm} lười quá."],"sad")],
      ("Comic: tay rời bàn phím chộp điện thoại (màn hình sáng), rồi Hiệp gục xuống; 3 chữ CHÁN NẢN / TỘI LỖI / LƯỜI rơi đè lên đầu (squash)","tội lỗi"),[{"name":"pop","atLine":0,"offset":1.5,"word":"TikTok"},{"name":"stamp","atLine":1,"offset":2.1,"word":"lười"}],
      props=[{"kind":"laptop","x":300,"y":1330,"s":0.62,"text":"Omi feature","sub":"đang mở…"},{"kind":"phone","x":800,"y":1120,"s":0.95,"rot":8,"at":1.3,"text":"TikTok"},
             {"kind":"cloud","x":360,"y":300,"s":0.7,"at":2.0,"words":["CHÁN NẢN","TỘI LỖI","LƯỜI"],"dropAt":[2.25,2.8,4.1]}]),
   SC("b03","b03","turn","paper","iris",H(0.5,pose="standing",act="thinking",ex="surprised"),[L("Nhưng thứ mình né đâu phải code, mà là cảm giác khó chịu.","But what I'm dodging isn't the code. It's the bad feeling.",["dodging","feeling."],["Nhưng thứ mình né đâu phải code,","mà là cảm giác khó chịu."],"focused",{"action":"reacting"})],
      ("Comic: iris mở sang giấy trắng, chữ 'CODE' bị bút gạch, mũi tên bật sang đám mây nhỏ 'KHÓ CHỊU'; Hiệp ngẩng lên nhận ra","cảm giác khó chịu"),[{"name":"pen","atLine":0,"offset":1.2,"word":"đâu phải code"}],
      props=[{"kind":"sign","x":300,"y":930,"s":0.72,"rot":-5,"text":"KHÓ CHỊU","at":1.6}])]
E=[SE("e01","b04","label-reveal",[L("Tức là trì hoãn: né chán ngán, sợ hỏng, hay rối. Nghe quen không?","So procrastination = dodging boredom, fear of messing up, or confusion. Sound familiar?",["dodging","familiar?"],["Tức là trì hoãn:","né chán ngán, sợ hỏng, hay rối.","Nghe quen không?"])],
      [("shield",0.25,"pop","né"),("faces",0.6,"tick","chán ngán")],("Thẻ 'Omi feature' mọc 3 'gai' cảm xúc Chán ngán / Sợ hỏng / Rối; mũi tên né cong vòng qua thẻ","né")),
   SE("e02","b05","count-up",[L("Bằng chứng: gộp sáu trăm chín mươi mốt hệ số tương quan, việc càng khó chịu, càng thấy mình kém, càng dễ hoãn.","Proof: 691 pooled correlations. The nastier the task and the lower your confidence, the more you delay.",["691","nastier","confidence,"],["Bằng chứng:","gộp sáu trăm chín mươi mốt hệ số tương quan,","việc càng khó chịu,","càng thấy mình kém,","càng dễ hoãn."])],
      [("count",0.12,"rise","sáu trăm chín mươi mốt"),("bars",0.8,"ding","càng dễ hoãn")],("Số 691 đếm lên; 2 thanh 'Task feels bad' và 'I can't do it' cùng dâng, kim 'Delay' vọt lên theo","sáu trăm chín mươi mốt")),
   SE("e03","b06","scale-tip",[L("Vì phần thưởng tận cuối tháng, còn khó chịu ập tới ngay, nên tay chộp TikTok.","The reward is weeks away, the discomfort hits now, so your hand grabs TikTok.",["weeks","now,","grabs"],["Vì phần thưởng tận cuối tháng,","còn khó chịu ập tới ngay,","nên tay chộp TikTok."])],
      [("tip",0.55,"snap","ập tới ngay"),("win",0.9,"ding","chộp TikTok")],("Cái cân: phần thưởng teo nhỏ trôi về mốc 'cuối tháng', cục 'khó chịu' rơi bịch xuống đĩa bên kia; bàn tay chộp điện thoại","ập tới")),
   SE("e04","b07","question-card",[L("Vậy trước khi gõ, hỏi: việc này khó chịu chỗ nào?","So before you start, ask: what exactly feels bad here?",["ask:","bad"],["Vậy trước khi gõ, hỏi:","việc này khó chịu chỗ nào?"])],
      [("q",0.55,"pop","khó chịu chỗ nào")],("Thẻ câu hỏi lớn '?' lật ra (card-flip), kính lúp soi vào thẻ 'Omi feature' tìm chỗ gai","hỏi")),
   SE("e05","b08","match-fix",[L("Nếu rối, viết ba gạch đầu dòng.","Lost? Write 3 bullets.",["3","bullets."],["Nếu rối, viết ba gạch đầu dòng."]),L("Sợ hỏng, cho phép nháp xấu.","Afraid of messing up? Allow an ugly draft.",["ugly"],["Sợ hỏng, cho phép nháp xấu."])],
      [("bullets",0.3,"pen","ba gạch đầu dòng"),("draft",0.85,"stamp","nháp xấu")],("Mỗi gai được 'gỡ' bằng một miếng vá: 3 gạch đầu dòng tự viết ra; con dấu 'DRAFT · OK' đóng lên tờ giấy nguệch ngoạc","gạch đầu dòng")),
   SE("e06","b09","timer",[L("Còn chán, hẹn mười phút rồi được dừng.","Bored? Set 10 minutes, then you may stop.",["10","stop."],["Còn chán, hẹn mười phút rồi được dừng."])],
      [("timer",0.35,"tick","mười phút"),("ring",0.85,"ding","được dừng")],("Đồng hồ hẹn giờ 10:00 quay ngược, vòng tiến độ chạy; chuông reo, biển 'STOP OK' bật lên","mười phút")),
   SE("e07","b10","mistake-stamp",[L("Ngược lại, mắng mình rồi gồng chỉ làm việc nặng nề hơn.","The trap: scolding yourself and forcing it only makes the task heavier.",["scolding","heavier."],["Ngược lại,","mắng mình rồi gồng","chỉ làm việc nặng nề hơn."])],
      [("stamp",0.35,"stamp","mắng mình"),("worse",0.85,"rise","nặng nề")],("Bong bóng 'Lười quá!' bị dấu đỏ '✕ NOT HELPING' đè lên; thẻ 'Omi feature' trĩu xuống, gai dài thêm","mắng mình"))]
B=[SC("b11","b11","payoff","paper","cut",H(0.66,pose="standing",act="talking",ex="focused"),[L("Lưu ý: nghiên cứu tương quan thôi. Lưu lại, lần sau hoãn thì mở.","Note: correlational only. Save this for the next time you stall.",["correlational","Save"],["Lưu ý: nghiên cứu tương quan thôi.","Lưu lại, lần sau hoãn thì mở."])],
      ("Comic: Hiệp giơ ngón tay, biển 'CHỈ LÀ TƯƠNG QUAN'; icon bookmark nảy lên ở chữ 'lưu lại'","tương quan"),[{"name":"tick","atLine":0,"offset":0.9,"word":"tương quan"},{"name":"pop","atLine":0,"offset":2.4,"word":"Lưu lại"}],
      props=[{"kind":"sign","x":400,"y":930,"s":0.72,"rot":-5,"text":"CHỈ LÀ TƯƠNG QUAN","at":0.9}]),
   SC("b12","b12","cta","grid","slide",H(0.5,pose="standing",act="talking",ex="happy"),[L("Còn bạn, việc đang hoãn khó chịu chỗ nào? Comment một chữ.","And you? What feels bad about the task you're avoiding? One word in the comments.",["bad","One"],["Còn bạn, việc đang hoãn","khó chịu chỗ nào?","Comment một chữ."],"happy"),
      L("Phần mình, mở Omi ra hỏi liền.","Me? Opening Omi and asking right now.",["Omi"],["Phần mình,","mở Omi ra hỏi liền."],"happy",{"action":"reacting"})],
      ("Comic: slide sang lưới, Hiệp chỉ vào người xem; câu cuối quay lại laptop 'Omi feature' như hook (loop), Hiệp mở laptop","Omi"),[{"name":"ding","atLine":1,"offset":0.1,"word":"hỏi liền"}],
      props=[{"kind":"laptop","x":300,"y":1330,"s":0.62,"text":"Omi feature","sub":"bắt đầu…"}])]
s={"id":"clip-02-final","clip":"clip-02","title":"Trì hoãn = né cảm giác khó chịu, không phải lười (Steel 2007)","week":1,"theme":"dark","pillar":"1 Làm ít, xong nhiều",
 "length_exception":"DL-058: Hiệp 14/10 17:54 chỉ cắt e06 nếu > 62s (cho phép ≤ 62s)","story":"S-02 Omi feature (Hiệp xác nhận 14/10, DL-047)","trend":"POV (TikTok #1 format tuần 5–11/10, top 36,1M, postdom) + meme ‘dự án ma’ (YT 23k); bỏ góc ‘không phải lười’ (bão hòa, digest 14–15/10)",
 "revisions":[{"date":"2026-10-15","dl":"DL-059","note":"rewrite: one continuous story with connectors, precise vocabulary, POV hook"},{"date":"2026-10-14","dl":"DL-044","note":"gate-1 draft: info-complete script + rule-52 effects table + template-A cover (rule 54)"}],
 "transition_sfx":{"part":"whoosh-soft","scene":"swish"},
 "cover":{"direction":"a","theme":"dark","series":"Làm ít, xong nhiều","ep":2,"hero":["LƯỜI?","ĐANG NÉ!"],"accent":1,"strike":0,"expression":"sad","action":"reacting","emote":"!","tilt":-5},
 "cover_options":[{"hero":["LƯỜI?","ĐANG NÉ!"],"picked":True},{"hero":["HOÃN MÃI","VÌ SỢ"]},{"hero":["TỰ MẮNG","VÔ ÍCH"]}],
 "hook":{"text":"POV: TÍNH NĂNG OMI · DỜI. DỜI. DỜI.","scenes":["b01","b01b","b01c"],"format":"POV + meme dự án ma (DL-059)"},
 "engagement":[{"type":"relatable-question","beat":"e01","text":"Nghe quen không?"},{"type":"save-prompt","beat":"b11","text":"Lưu lại, lần sau hoãn thì mở."},{"type":"comment-challenge","beat":"b12","text":"Comment một chữ."},{"type":"loop","beat":"b12","text":"mở Omi ra","hook_word":"Omi"}],
 "parts":[{"id":"A","engine":"remotion","transitionOut":"slideleft","scenes":A},{"id":"E","engine":"hyperframes","dir":"explainer","transitionOut":"circleopen","sections":E},{"id":"B","engine":"remotion","scenes":B}]}
json.dump(s,open(D+'spec.json','w'),ensure_ascii=False,indent=2)
import re
n=sum(len(re.sub(r"\{[^}]*\}|\*","",l["text"]).split()) for p in s["parts"] for x in p.get("scenes",p.get("sections",[])) for l in x["lines"])
print("VI words",n)
