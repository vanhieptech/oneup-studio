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
def SC(id,beat,part,bg,tr,cast,lines,fx,sfx,framing="medium",push=0.04,narr=None):
    d={"id":id,"beat":f"clip-02.{beat}","part":part,"background":bg,"framing":framing,"push":push,"transition":tr,"cast":[cast],"lines":lines,"fx":{"visual":fx[0],"word":fx[1]},"sfx":sfx}
    if narr: d["narration"]=narr
    return d
def SE(id,beat,motion,lines,hits,fx):
    return {"id":id,"beat":f"clip-02.{beat}","part":"explain","motion":motion,"lines":lines,"hits":[{"id":a,"f":b,"sfx":c,"word":w} for a,b,c,w in hits],"fx":{"visual":fx[0],"word":fx[1]}}
H=lambda x,pose="sitting",act="typing",ex="focused":{"id":"hiep","x":x,"facing":"right","pose":pose,"action":act,"expression":ex}
A=[SC("b01","b01","hook","desk","cut",H(0.42),[L("Deadline sáng mai. Mở file báo cáo, năm giây sau, mình đang lướt TikTok.","Deadline tomorrow. Open the report… five seconds later: TikTok.",["Deadline","TikTok."],["Deadline sáng mai.","Mở file báo cáo,","năm giây sau, mình đang lướt TikTok."],"neutral",{"action":"idle","expression":"confused"})],
      ("Comic bàn tối: màn hình laptop 'report.docx' trống, tay Hiệp trượt sang điện thoại, màn hình điện thoại sáng lên; camera push-in","TikTok"),[{"name":"click","atLine":0,"offset":0.4,"word":"Mở file"},{"name":"pop","atLine":0,"offset":2.2,"word":"TikTok"}],narr="11:20 PM"),
   SC("b02","b02","struggle","desk","slide",H(0.42,act="idle",ex="sad"),[L("Rồi tự mắng: mình lười quá.","Then I scold myself: “I'm so lazy.”",["lazy."],["Rồi tự mắng:","{ừm} mình lười quá."],"sad")],
      ("Comic: Hiệp gục xuống bàn, đám mây đen nhỏ trên đầu với chữ 'LƯỜI' đè xuống (squash)","lười"),[{"name":"stamp","atLine":0,"offset":1.4,"word":"lười"}]),
   SC("b03","b03","turn","paper","iris",H(0.5,pose="standing",act="thinking",ex="surprised"),[L("Nhưng nghiên cứu nói: thường đâu phải lười. Mình đang né một cảm giác.","Research says: usually not lazy. You're dodging a feeling.",["not","dodging"],["Nhưng nghiên cứu nói:","thường đâu phải lười.","Mình đang né một cảm giác."],"focused",{"action":"reacting"})],
      ("Comic: iris mở sang giấy trắng, chữ 'LƯỜI' bị bút gạch, Hiệp ngẩng lên nhận ra","né một cảm giác"),[{"name":"pen","atLine":0,"offset":1.6,"word":"đâu phải lười"}])]
E=[SE("e01","b04","label-reveal",[L("Trì hoãn là cách né cảm giác khó chịu: chán, sợ làm dở, hay không biết bắt đầu.","Procrastination = dodging discomfort: boredom, fear of doing badly, no clear start.",["dodging","discomfort:"],["Trì hoãn là cách né cảm giác khó chịu:","chán, sợ làm dở,","hay không biết bắt đầu."])],
      [("shield",0.2,"swish" if False else "pop","né"),("faces",0.7,"tick","chán")],("Một việc (thẻ 'Báo cáo') tỏa ra 3 'gai' cảm xúc Chán / Sợ làm dở / Không biết bắt đầu; mũi tên né cong vòng qua thẻ","khó chịu")),
   SE("e02","b05","count-up",[L("Gộp sáu trăm chín mươi mốt hệ số tương quan: việc càng khó chịu, càng thấy mình không làm được, càng dễ hoãn.","691 correlations: the nastier the task and the lower your confidence, the more you delay.",["691","nastier","confidence,"],["Gộp sáu trăm chín mươi mốt hệ số tương quan:","việc càng khó chịu,","càng thấy mình không làm được,","càng dễ hoãn."])],
      [("count",0.02,"rise","sáu trăm chín mươi mốt"),("bars",0.75,"ding","càng dễ hoãn")],("Số 691 đếm lên; 2 thanh trượt 'Task feels bad' và 'I can't do it' cùng tăng, kim 'Delay' vọt lên theo","sáu trăm chín mươi mốt")),
   SE("e03","b06","scale-tip",[L("Vì phần thưởng thì ở xa, còn cái khó chịu ở ngay bây giờ. Nên điện thoại thắng.","Because the reward is far away, the discomfort is right now. So the phone wins.",["far","now.","phone"],["Vì phần thưởng thì ở xa,","còn cái khó chịu ở ngay bây giờ.","Nên điện thoại thắng."])],
      [("tip",0.62,"snap","bây giờ"),("win",0.9,"ding","điện thoại thắng")],("Cái cân: bên trái 'phần thưởng' nhỏ dần khi trượt xa trên trục thời gian, bên phải icon điện thoại; cân nghiêng hẳn về phía điện thoại","ở xa")),
   SE("e04","b07","question-card",[L("Nên trước khi làm, hỏi một câu: việc này khó chịu ở chỗ nào?","So before you start, ask: what exactly feels bad here?",["ask:","bad"],["Nên trước khi làm,","hỏi một câu:","việc này khó chịu ở chỗ nào?"])],
      [("q",0.55,"pop","khó chịu ở chỗ nào")],("Thẻ câu hỏi lớn '?' lật ra (card-flip), kính lúp soi vào thẻ 'Báo cáo' tìm chỗ gai","hỏi một câu")),
   SE("e05","b08","match-fix",[L("Không biết bắt đầu? Viết ba gạch đầu dòng. Sợ dở? Cho phép nháp xấu.","No clear start? Write 3 bullets. Afraid it'll be bad? Allow an ugly draft.",["3","bullets.","ugly"],["Không biết bắt đầu?","Viết ba gạch đầu dòng.","Sợ dở?","Cho phép nháp xấu."])],
      [("bullets",0.3,"pen","ba gạch đầu dòng"),("draft",0.85,"stamp","nháp xấu")],("Mỗi gai cảm xúc được 'gỡ' bằng một miếng vá: 3 gạch đầu dòng tự viết ra; con dấu 'DRAFT · OK' đóng lên tờ giấy nguệch ngoạc","gạch đầu dòng")),
   SE("e06","b09","timer",[L("Thấy chán? Hẹn mười phút, hết giờ thì được dừng.","Bored? Set 10 minutes. When it rings, you may stop.",["10","stop."],["Thấy chán?","Hẹn mười phút,","hết giờ thì được dừng."])],
      [("timer",0.35,"tick","mười phút"),("ring",0.85,"ding","được dừng")],("Đồng hồ hẹn giờ 10:00 quay ngược, vòng tiến độ chạy; chuông reo, biển 'STOP OK' bật lên","mười phút")),
   SE("e07","b10","mistake-stamp",[L("Lỗi hay gặp: mắng mình rồi gồng. Mắng xong, việc còn khó chịu hơn.","Common mistake: scold yourself and force it. That makes the task feel worse.",["Common","mistake:","worse."],["Lỗi hay gặp:","mắng mình rồi gồng.","Mắng xong, việc còn khó chịu hơn."])],
      [("stamp",0.35,"stamp","mắng mình"),("worse",0.85,"rise","khó chịu hơn")],("Bong bóng 'Mình lười quá!' bị dấu đỏ '✕ KHÔNG GIÚP' đè lên; gai trên thẻ 'Báo cáo' dài thêm ra","mắng mình"))]
B=[SC("b11","b11","payoff","paper","cut",H(0.5,pose="standing",act="talking",ex="focused"),[L("Lưu ý: đây là nghiên cứu tương quan, chỉ cho thấy hướng, chưa phải nguyên nhân.","Note: correlational research. A pattern, not proof of cause.",["correlational","pattern,"],["Lưu ý:","đây là nghiên cứu tương quan,","chỉ cho thấy hướng,","chưa phải nguyên nhân."])],
      ("Comic: Hiệp giơ ngón tay nhắc ý, bên cạnh tấm bảng nhỏ 'tương quan ≠ nhân quả' với hai mũi tên","tương quan"),[{"name":"tick","atLine":0,"offset":1.0,"word":"tương quan"}]),
   SC("b12","b12","cta","grid","slide",H(0.5,pose="standing",act="talking",ex="happy"),[L("Việc bạn đang hoãn khó chịu chỗ nào? Comment một chữ.","What's the bad part of the task you're avoiding? One word in the comments.",["bad","One"],["Việc bạn đang hoãn","khó chịu chỗ nào?","Comment một chữ."],"happy"),
      L("Lần sau mở TikTok, hỏi câu đó trước.","Next time you open TikTok, ask that first.",["ask"],["Lần sau mở TikTok,","hỏi câu đó trước."],"happy",{"action":"reacting"})],
      ("Comic: slide sang lưới, Hiệp chỉ vào người xem; câu cuối nối lại hook 'mở TikTok' (loop), điện thoại nhỏ hiện lại góc khung","một chữ"),[{"name":"ding","atLine":1,"offset":0.1,"word":"hỏi câu đó"}])]
s={"id":"clip-02-final","clip":"clip-02","title":"Trì hoãn = né cảm giác khó chịu, không phải lười (Steel 2007)","week":1,"theme":"dark","pillar":"1 Làm ít, xong nhiều",
 "trend":"‘vừa than bị dí deadline vừa lướt TikTok’ (vtcnews.vn; câu chung, không phải chuyện thật của Hiệp)",
 "revisions":[{"date":"2026-10-14","dl":"DL-044","note":"gate-1 draft: info-complete script + rule-52 effects table + template-A cover (rule 54)"}],
 "transition_sfx":{"part":"whoosh-soft","scene":"swish"},
 "cover":{"direction":"a","theme":"dark","series":"Làm ít, xong nhiều","ep":2,"hero":["LƯỜI","NÉ KHÓ CHỊU"],"accent":1,"strike":0,"expression":"sad","action":"reacting","tilt":-5},
 "parts":[{"id":"A","engine":"remotion","transitionOut":"slideleft","scenes":A},{"id":"E","engine":"hyperframes","dir":"explainer","transitionOut":"circleopen","sections":E},{"id":"B","engine":"remotion","scenes":B}]}
json.dump(s,open(D+'spec.json','w'),ensure_ascii=False,indent=2)
import re
n=sum(len(re.sub(r"\{[^}]*\}|\*","",l["text"]).split()) for p in s["parts"] for x in p.get("scenes",p.get("sections",[])) for l in x["lines"])
print("VI words",n)
