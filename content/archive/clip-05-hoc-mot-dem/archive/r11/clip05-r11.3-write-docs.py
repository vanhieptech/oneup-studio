from pathlib import Path
import json,re
B=Path('/workspace');s=json.loads((B/'opencreator-clip05-spec-r11.3-draft-2026-11-07.json').read_text());beats=s['beats'];v=s['version']
mdp=B/'opencreator-clip05-script-r11.3-draft-2026-11-07.md';bp=B/'opencreator-clip05-storyboard-r11.3-plan-2026-11-07.md';sp=B/'opencreator-clip05-spec-r11.3-draft-2026-11-07.json'
def js(x):return json.dumps(x,ensure_ascii=False)
def capfmt(b):
    out=[]
    for c in b['captions']:
        words=c['en'].split();marked=' '.join(('**'+w+'**') if i in c['hl'] else w for i,w in enumerate(words));out.append(f'{c["id"]} [{len(words)}] {marked} (hl={c["hl"]})')
    return '<br>'.join(out)
def sound(b):return '; '.join(f'{x["name"]}→“{x["word"]}” @{x["at_estimate_s"]}s ƯỚC' for x in b['sfx'])
def main_table():
    a=['| Beat · giây ƯỚC · người nói | Cảnh/shot | Hành động | Cảm xúc | Lời có nhấn | Minh họa vật/ý nghĩa | Animation/EFX | Sound/SFX | EN ≤8/chunk · nhấn in đậm |','|---|---|---|---|---|---|---|---|---|']
    for b in beats:
        a.append('| '+' | '.join([f'{b["id"]} · {b["estimate_s"]} · Hiệp',b['shot'],b['stage']['action'],b['emotion'],b['marked_text'],b['why_visual'],b['engine_plan']+' / '+b['fx']['motion']['slug']+' '+js(b['fx']['motion']['params']),sound(b),capfmt(b)])+' |')
    a.append('| end · '+str(s['end_card']['estimate_s'])+' · không thoại | Card tĩnh có logo | Một entrance rồi giữ | Trung tính | Không thoại; không tính wordcount | An toàn + credit + đã chuyển thể + license | mmx-soft-inout9f, không doodle | whoosh-soft trước seam0.12s ƯỚC | Credit nguyên văn ở mục end card; không caption thoại |')
    return '\n'.join(a)
old=(B/'opencreator-clip05-script-r11.2-draft-2026-11-07.md').read_text();sources=old[old.index('## Nguồn và ranh giới claim'):old.index('## Bảng beat đầy đủ')]
links=[('S1→S2','“quên gì…không biết” → “nhận ra chỗ thiếu”: cùng nội dung chưa nhớ, từ không định danh sang có thể định danh; chưa giả định đã kể.','Không phải lời hứa tìm đủ mọi chỗ quên hay hết cần sách; chưa kiểm nghe/người lạ.'),('S2→S3','Từ một giá trị của đọc (học/nhớ) mở phạm vi cùng cuốn sách còn là phong cách sống/niềm vui.','ContextB đã được quyền giữ; không causal từ texthip, lời nối thật còn cần nghe. Không nói bỏ riêng câu trend làm method sụp.'),('TrongS3','Text hip gắn sách với lifestyle; “bạn có thể vừa…vừa…” là khả năng bổ sung mục tiêu cho cùng người đọc.','Không mô tả participant hay chia hai nhóm.'),('S3→S4','“học”→“Còn cách học”: lựa chọn kỹ thuật theo ranking.','Không coi ranking giải thích tại sao người theo trend quên.'),('S4→S5','“tự kiểm…cao”→muốn biết chỗ chưa nhớ: chuyển từ lựa chọn có nguồn sang mục tiêu.','Đã chấp nhận text ở r11.2; nghe/actual source review chưa có.'),('S5→S6','“Bạn muốn biết…”→“Muốn biết…”: câu giải pháp trả mục tiêu ngay.','Không treo câu hỏi qua trend.'),('S6→S7','“tự kiểm”→“Ví dụ”: minh họa đúng đóng–tự kể–mở dò.','Không là phương pháp mới; mock không phải trang HTB hay lời khuyên tài chính.'),('S7→S8','“mở ra dò”→“Lúc dò”: giờ mới có phần kể để đối chiếu với trang.','Nguồn pain không chứng minh đây là một phép thử có thật.'),('S8→S9','Phần kể chỉFood, trang cóRent→“khoản vừa sót”→bổ sungRent.','Payoff định danh chính chỗ thiếu đã hứa, không hứa nhớ lần sau/làm đúng công việc.'),('S9→S10','Từ minh họa cùng phép kể sang “Giả sử” với trang vừa đọc của người xem.','Điều kiện mềm giữ trong EN; không yêu cầu làm test rồi báo kết quả như hai việc.'),('S10→S11','“đủ hay thiếu”→comment một từ “đủ hoặc thiếu”.','Một CTA; loop từthiếu trong lời hứa hook.')]
a=[f'''---
title: "Clip05 {v} — nhận ra chỗ chưa nhớ"
date: 2026-11-07
type: script
status: draft — chưa Chốt, không tự pass
source: "Reviewer r11.2 + Social bd53fd3/pain7fb1e4b + Deep d673dd9/b02dd07"
tags: [clip05, r11.3, direction-C]
trend_id: {s['source']['trend_id']}
hook_pattern: P10
trend_beats: b02
trend_spoken: "Text hip"
example_evidence: x-2115086418192089298
fact_lock: research/fact-packages/factcheck-clip05-lock-2026-11-07.md
spoken_words: {s['word_count']}
---

# Actual draft r11.3 — không phải bản trình xin Chốt

Đọc to/người lạ/nghe một lần/timing **CHƯA KIỂM**. Không có ai được ghi là đã đọc/nghe. Text checks chỉ chẩn đoán, không thay cổng tai. Preview gate1 **CHƯA CHUẨN BỊ ẢNH**: chưa PNG/contactsheet, cover3hướng/grid, hai vòng soát mắt. Đây là thiếu preview trước cổng trình, KHÔNG đồng nhất với Chốt lời; không nói mọi ảnh phải chờ sau Chốt. Phạm vi lượt này chỉ MD/JSON/plan/số học, không ảnh/voice/render/engine code/repo edits/tin nhắn.

## Lời thoại — {s['word_count']} từ
''']
for i,b in enumerate(beats):a.append(f'{i+1}. **[{b["label"]}]** {b["text"]}')
a+=['\n## Thay actual hook, không vá liên từ/không đổi B\n',f'''| r11.2 bị trả | r11.3 |
|---|---|
| {old.split('1. **[Hook / pain + hứa]** ')[1].splitlines()[0]} | {beats[0]['text']} |

Một ý cả clip: Muốn nhớ nội dung bên cạnh niềm vui đọc, bạn có thể dùng tự kiểm rồi dò văn bản để nhận ra phần thiếu, được minh họa bằng khoản thuê nhà có trên trang nhưng thiếu trong phần kể.

F1: không còn pain tìm trang rồi hứa về việc kể chưa xảy ra; cả hook và payoff bây giờ cùng nội dung chưa nhớ. F2: đảo ngay ở pain “quên gì cũng không biết”, rồi hứa có thể gọi ra chỗ thiếu cụ thể; đây là đề xuất tăng lực mở, KHÔNG tự kết luận peak. Không gọi unknown-omission là kết quả Social/Dunlosky. Không giải thích cơ chế não hay tạo nhân quả texthip→quên.

Giữ nguyên toàn bộ b02–b07 so r11.2: context B, ranking, goal, đóng–kể–dò, Food/Rent, CTA. Không thêm vòng outline/3ý tưởng/research. Hook_alt khác kiểu (chưa chọn/chưa duyệt, không count): “{s['hook_alt']['text']}”.

Count theo khoảng trắng: {s['word_count']} = {str([b['word_count'] for b in beats])}; sau hook trước method **50 =18+21+11**. Study21từ/1câu. Không ép55–60s; ngân sách hình/thoại hiện {s['duration_estimate_s']}s ƯỚC, chưa đo. Bỏ ý tìm-trang chứ không chặt câu cộc để vừa số.

### Vai trò beat / xóa BEAT (không thêm điều kiện causal trend)

| Beat | Vai trò | Mất nếu bỏ |
|---|---|---|
| b01 | Nội dung quên chưa gọi tên→hứa có thể nhận ra phần thiếu | Mất pain/hứa cùng đối tượng |
| b02 | Cùng sách có giá trị lifestyle/đọc vui và mục tiêu học đồng tồn tại | Mất định phạm vi nhiều giá trị của đọc; không khẳng định method mất tiền đề logic nếu bỏ câu trend |
| b03 | Đối chiếu utility có nguồn để cân nhắc kỹ thuật | Mất dẫn chứng cụ thể |
| b04 | Muốn nhận ra chỗ chưa nhớ | Mất câu mục tiêu mà “Muốn biết” trả lời |
| b05 | Đóng–tự kể–mở dò, HTB nói thành lời | Mất thao tác và phần kể cho payoff |
| b06 | Dò thấy thiếuRent, bổ sung trong phần kể | Mất định danh chỗ thiếu để trả hook |
| b07 | Giả định mềm + commentmột từ + loop | Mất challenge/loop |
''',sources,'## Bảng đồng bộ 9 cột — kế hoạch, không ảnh\n',main_table(),'\n## Trường chi tiết từng beat\n']
for b in beats:
    a.extend([f'### {b["id"]} · {b["label"]}\n','| Trường | Kế hoạch / giới hạn |','|---|---|'])
    rows=[('Vai trò',b['role']),('Ngữ cảnh',b['context']),('Người nói/giọng','Hiệp/Thầy, ngôi bạn; F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app'),('Ngắt tự nhiên',b['pause_plan']),('Lời + nhấn',b['marked_text']),('Semantic VI–EN focus',js(b['emphasis_focus'])),('VI→EN slices', '<br>'.join(c['vi_text']+' → '+c['en'] for c in b['captions'])),('Liên kết',b['link']),('Claim/source',b['claim_source']),('Timing',str(b['estimate_s'])+' ƯỚC; cues f=null, frame_estimate chỉsố kếhoạch, không lời đã đo'),('Còn chờ','Actual Deep/Social/Reviewer; đọc to/người lạ/timing CHƯA KIỂM')]
    a.extend('| '+x+' | '+y+' |' for x,y in rows)
a+=['\n## Bảng hiệu ứng r11.3 — cùng JSON, không chạy fx-table.py/renderer\n','| Beat | Engine · main/source/params | Vật/hành động | Anchor + SFX ƯỚC |','|---|---|---|---|']
for b in beats:a.append('| '+b['id']+' | '+b['engine_plan']+' · '+b['fx']['motion']['slug']+'/'+b['fx']['motion']['source']+' '+js(b['fx']['motion']['params'])+' | '+b['fx']['visual']+' | '+sound(b)+' |')
a+=['| end | static · mmx-soft-inout9f | Credit tĩnh | whoosh-soft ở seam−0.12s, không nhấn thoại |','\nMột main/beat,0accent,0doodle; vật/rig có sẵn, không ảnh mới. SFX từ assets/sfx/SOURCES.md14–16. Ambience brown-noise nhỏ xuyên clip, không nhạc. Transitionseam dùng swish/whoosh-soft; xem parts_plan, không nhập nhằng cutSFX với wordhit. Hitước phải resnap; mix/pitch/phrasetiming CHƯA KIỂM. effects-log chưa có đủ signatureclip04 để đối chiếu; không tự ghi “không lặp”. Catalog hiện có, không install/newcode/HFbuild/lint.\n', '## Map scene / narration / timing / layout — plan không chạy\n',f'Spec `{sp}`; storyboard `{bp}`. `planning_only=true`, `renderable=false`, `locked=false`; parts_plan KHÔNG là productionparts.\n',js(s['timing_model']),'\n| Unit → target | Beat / voice line | Giây ƯỚC | Narration hiển thị | Caption refs / layout |','|---|---|---|---|---|']
for part in s['parts_plan']:
    for u in part.get('scenes',part.get('sections',[])):
        narration=u['narration']['text'] if u['narration'] else ('inherit globalhook-title' if u['beat']=='b01' else 'none; not a missing spoken line')
        a.append(f'| {part["id"]}/{u["id"]}→{u["production_target"]} | {u["beat"]}/{u["voice_line_ref"]} | {u["interval_estimate_s"]} | {narration} | {",".join(u["caption_segment_refs"])} / {u["layout_ref"]} |')
a += [f'''\nFirst scene `narration.text` = `hook.text` = **{s['hook']['text']}**. Đây là titleEN, không phải thoạiVI. Một linevi-b01 chạy liên tục qua3cut, không sinh/cắt lời thành3line. Globalhook-title/captionlayer giữ qua cut; không nhân title thành propwords. Voiceonset0.06s, cuts0.8/2.0s, hitsemantic tại{[x['at_estimate_s'] for x in beats[0]['sfx']]}s đều ƯỚC; hitthứ2 sau3s không được tính như hittrong3s. Đã map mỗi cueđến đúngscene và wordrange trongJSON.

### Safezone nhất quán, kiểm số học không thay kiểm mắt

- Content `[60,150,960,1310]` = x60–1020/y150–1460 theo layout.ts6–8. Đây KHÔNG là vùng của caption/logo.
- Captionzone riêng `[60,1488,960,312]` = y1488–1800. ActualstandardRemotiontop1488 (SceneRenderer41–42), HFtop1500 (captions.tpl10). ReserveRemotion[70,1488,948,272], HF[70,1500,948,272] gồm shadow; không còn tự ghi mọi chữ phảiy≤1460 rồi đặtcaption1490.
- Logo slot riêng[60,80,100,70]. Mỗi top-level object và motionenvelope được script số học kiểm containment/disjoint/caption tránh; không coi như actualplaceBubble/layoutCheck/preview.
- Targethooktitley170; current SceneRenderer standardtop66 chưa nhận target này. CurrentCaption.tsx dùngEN_FONT, heightwrap động; BVP/localfont/actualheight chưa xác nhận. HFtemplate cóMAXW4: chunkduyệt≤8 có thể chia subgroup đúng thứtự, nhưng chưa chốt timing từngsubgroup; không đượcpopchunk đểvừa.
- Map này là standardTikTok1080×1920; Reels captiony1000/narrow chưa map, không an toàn theo kếthừa.
- Cover có hai loại bbox: targetstrict-safe hợp số học, nhưng envelope dựkiến theo slottemplate hiện có rig/circle[390,1000,660,660] vượt right30/bottom60 so vùngrule. Giữ findingFAILriêng, không gọi coverđạt hay tự nới safezone. Target cầnport/decision vì props templatehiện tại chưaexpose tọa độ ấy. Chưa sửaengine.
- Script: `/workspace/clip05-r11.3-validate-plan.py`; output `/workspace/clip05-r11.3-local-validation-2026-11-07.json`. Số học target không chứng minh chữ thật vừa/khôngche/camera projection/safeUI nền tảng.
''','## Quan hệ từng cặp câu — text audit, không thay đọc to\n','| Cặp | Liên hệ trong lời | Còn mở |','|---|---|---|']
a.extend('| '+x+' | '+y+' | '+z+' |' for x,y,z in links)
a+=['\n## Audit lặp và polish\n','| Cụm | Giữ/bỏ và vai trò |','|---|---|','| quên | Giữ2lần hook: pain khônggọi tên → hứa vượt trạngthái chỉbiết mìnhquên; không suy cơchế |','| chỗ thiếu / khoản vừa sót / thiếu | Promise → định danhRent/payoff → lựa chọnCTA; không thêm một beat giảng lại insight |','| tự kiểm | Giữ2lần: rankingb03 và tênkhuyếnnghịHTBb05, không hai phươngpháp |','| học | Hookđích → b02giátrị đi cùng → b03kỹthuật; không lặp thêm câu motivation |','| bạn có thể ×2 | Giữ ởb01 như hứa có điều kiện, b02 như khả năng hai giá trị đồngtồn tại; checkerngram vẫn cảnh báo, không tựwaive/không lặp lần3 |','| đủ hay thiếu / đủ hoặc thiếu | Câu hỏi lựa chọn và một lờimời commentngaysau, không đếm từ/ý |','| Bỏ | tìmtrang/cứphải, kểthiếu/ngayđó trước khi kể, tối–sáng/ngãba/doingfail; không thayvật đểgiữ cơchế cũ |','\nPolish chỉ trên chữ: fact/ranking/context/method giữ nguyên; bỏ referent thiếu, không thêmkhẩu hiệu/trí nhớ như não lưu/tức là. Văn nói/tone/nhấn thật CHƯA KIỂM; không nhận đây là chuyệnđờiHiệp. Tương phản hook là chính pain→outcome, không bịa nhânquả.\n','## Issue Reviewer r11.2 → vị trí / sửa / còn mở\n','| Issue | Vị trí | Sửa | Còn mở |','|---|---|---|---|']
a.extend('| '+r['issue']+' | '+r['location']+' | '+r['change']+' | '+r['open']+' |' for r in s['issue_resolution'])
a+=['\n## End card / safety / credit / license\n',f'Ước{s["end_card"]["estimate_s"]},3s chưa đo độ đọc. Không thoại/không chibi, giữlogo. Fullcredit cũng phải ởpost.']
a.extend('- '+x for x in s['end_card']['text_lines'])
a+=['- '+s['publication_plan']['ai_disclosure']+' Chỉ công bố/bậtAI khi thực cógiọng; chưa cóaudio.','\n## Engagement / callback / cover / preview\n','| Kiểu | Kế hoạch |','|---|---|']
a.extend('| '+x['type']+' | '+x['beat']+': '+x['text']+' |' for x in s['engagement'])
a += ['\nGhim đề xuất, chưa đăng: '+s['pinned_comment_plan'],'CTA một yêu cầu commentmột từ; EN giữSay/Would giảđịnh. Khônglike/follow/share/save. Callback04 chỉ khai cùng23.14; không nói đãđăng/đãxem. Dark/slot5 dựkiến theo theme-map, releasestatus clip04 chưa xác nhận.','\nCoverA props kếhoạch: `'+js(s['cover'])+'`. ep=number5, emote! có hỗ trợ trongCover.tsx. Đây là đối chiếu literalfields, KHÔNG schemaenginevalidate hay render. Khôngframegrab, không doodle.','**Preview gate1: CHƯA CHUẨN BỊ ẢNH**. Thiếu storyboard1frame/beat, PNG/contactsheet, coverA/B/C/grid và2vòngsoátmắt. Không lấy filekếhoạch này thay preview; cũng không coi preview hình là Chốt lời. Không tạoảnh theo phạmvi.','\n## Checks / hashes — xem sidecar đúng file cuối\n','Chạy checker gốc không thay code/metadata: subjects/l088/trend/flow/clarity/link/repeat/evidence/choppy/fresh. Output `/workspace/clip05-r11.3-checker-output-2026-11-07.txt`; số học `/workspace/clip05-r11.3-local-validation-2026-11-07.json`; hashes `/workspace/clip05-r11.3-delivery-manifest-2026-11-07.json`. Không productionchecker/build/STT/--final.','L090 lookup registry còn FAIL riêng; example_evidence có locator archive hợp lệ phạmvi mộtngười, không thiếu nguồnC nghiên cứu. Không waiver, không đồng bộmetadata/repo. Nếu freshso r11.2 báo giống, đó là kết quả máy phảigiữ: bản này sửa hữu hạn trênB được chấp nhận, không tự đổiconcept đểqua ngưỡng.','Kết quả máy đã chạy: subjects/l088/flow/clarity/link/repeat/evidence/choppy/fresh-vs-conceptcũ exit0. L0881cờ vịtrí, flow1cờb04/b06, link3/10cặp, repeatcờ “bạn có thể”×2. Trend exit1 registry. Freshriêng so r11.2 exit1 chain0.89/hook0.23 (giữB theo chỉđạo); không xóa lỗi này hay đổiconcept để ép máy. Sidecar là kết quả chính xác trên SHA cuối.','Read-aloud/người lạ/nghe1lần/timing CHƯA KIỂM. ActualDeep/Social/Reviewer SHA mới CHƯA KIỂM. Không trìnhxinChốt, không tựPASS. Gói postfinal/giọng/mix/lint/render làpha sau, không làm lý do dừng sửa lời.']
mdp.write_text('\n'.join(a)+'\n')
# Board is generated from the same JSON, not a second transcription.
a=['---','title: "Clip05 r11.3 — storyboard FILE KẾ HOẠCH"','date: 2026-11-07','type: storyboard-plan','status: draft-planning-only-no-images','source: opencreator-clip05-spec-r11.3-draft-2026-11-07.json','tags: [clip05, storyboard, planning-only]','---','\n# CHƯA CHUẨN BỊ ẢNH — không phải preview đã duyệt','Không PNG/contactsheet/cover3hướng/grid, không2vòngsoátmắt. Fileplan không thay previewgate1; previewtĩnh là bước riêng với Chốt lời/voice/video. Không tạoảnh/voice/render trong lượt này. Mọi giây làbudgetƯỚC; không cówordtimestamp/ảnhthật.\n','## Đồng bộ cảnh/lời/nhấn/EN/motion\n',main_table(),'\n## Frame đầu–giữa–cuối dự kiến\n','| Beat | Đầu→giữa→cuối / reveal | Layout ref |','|---|---|---|']
frames=[('b01','Sách mở + titleEN frame0 → cutmặt khựng vì chưa gọi tênđược nội dungquên → về cùngsách; chưa cóphầnkể, chưaMoney/Rent.','hook-wide / hook-reaction / hook-wide'),('b02','Giữcuốn sách → panelText hip/Reading as lifestyle → cùngngườiđọc cóthểđọcvui+ học, khônghai nhóm.','reading-context'),('b03','10thẻtrungtính 2hàng×5 → nhận diện2kỹthuật → chỉhai nhómutilityHIGH/LOW, khôngrank1–10/tăng% haycomic.','ranking'),('b04','Trởlạingườiđọc/sáchmở → tò mò nội dungchưanhớ → taychuẩnbị, chưađóng làmtest.','reading-goal'),('b05','NêuHTB trước → mới gấp/kểFood → mởbảnnguồn, chưahiệnRent trướccue b06.','reading-method'),('b06','Hai cộtSource/Retelling → đúngtiềnthuênhà mới lộRentnguồn → đúngbổsung mới thêmRent vào phầnkể.','comparison'),('b07','Vềcùngngườiđọc → lựa chọnComplete/Missing → mộtôcomment/loop, khôngnútLike/Follow.','cta'),('end','Cardcredit/an toàn → giữđọc → hết, khôngtăng3s chođủ55s.','credit')]
a.extend('| '+x+' | '+y+' | '+z+' |' for x,y,z in frames)
a+=['\n## Map thật trong kế hoạch (không là engine spec)\n','| Unit | Beat / VIref | Time ƯỚC | Narration / layout | Captionrefs |','|---|---|---|---|---|']
for p in s['parts_plan']:
    for u in p.get('scenes',p.get('sections',[])):
        a.append(f'| {p["id"]}/{u["id"]} | {u["beat"]}/{u["voice_line_ref"]} | {u["interval_estimate_s"]} | '+(u['narration']['text'] if u['narration'] else ('inherit hook-title' if u['beat']=='b01' else 'no displaynarration'))+' / '+u['layout_ref']+' | '+','.join(u['caption_segment_refs'])+' |')
a+=['\n## VI→EN chunk / highlight / timing bindings\n','Một segment tại một thời điểm; layerliên tục qua hookcut. CácVI slice chỉmapbản dịch, KHÔNG làđơnvịsinh/cắtF5.\n','| ID | VI exact | EN / hl meaning | Time ƯỚC |','|---|---|---|---|']
for b in beats:
    for c in b['captions']:a.append('| '+c['id']+' | '+c['vi_text']+' | '+c['en']+' / '+str(c['hl'])+'='+str([c['en'].split()[i] for i in c['hl']])+' | '+str(c['interval_estimate_s'])+' |')
a+=['\n## Geometry / safezones','Tọa độ x,y,w,h. Content[60,150,960,1310], captionzone[60,1488,960,312], logoslot[60,80,100,70]. StandardRemotioncaptiontop1488/HFtop1500 cónguồn renderer; khôngnói caption phải ởcontenty≤1460. Boxlàallocation cómargin, khôngdom/glyph đo thật.\n','| Layout | Top-level allocations | Motion/collision scope |','|---|---|---|']
for id,l in s['layout_plans'].items():a.append('| '+id+' | '+js(l['objects'])+' | camera_push=0; testfullmotionenvelope, no duplicate/nestedbox collision excuses. Actualrig/bubbletail/propsfit chưađo. |')
a+=['\nChạy `/workspace/clip05-r11.3-validate-plan.py`, kết quả `/workspace/clip05-r11.3-local-validation-2026-11-07.json`. Chỉ tính containment, intersection và timebounds trênbox/timedeclared; không xemảnh, khôngrendererlayoutCheck. Targettitley170 cầnport vìstandardNarrationBox hiện defaulty66. Captionactualheightdynamic/fontEN_FONT/HFsubgroups≤4 vàReelscaptiontop1000 chưaQA; không bỏchunkduyệt.\n','## Trang minh họa','Cùng sáchmock. Nhãn “Editorial illustration” giữ trên khungminhhọa b05–06. Trang có “Record food expenses” và “Record rent”; phầnkể banđầu chỉ“Food expenses”. Rent chỉreveal ởcue tiềnthuênhàb06, rồi mớibổsung. KhônggắnlogoHTB nhưtrangchụp, khônglờikhuyên tài chính, khôngcaSocial/thínghiệmDunlosky.\n','## Cover plan — CHƯA CHUẨN BỊ ẢNH','```json',json.dumps(s['cover'],ensure_ascii=False,indent=2),'```',json.dumps(s['cover_plan'],ensure_ascii=False,indent=2),'Coverstrict-safe targetfit khôngchứngminhfixedtemplate đangfit. Envelope hiệnrig/circle vượt strictsafe right30/bottom60; findingFAILởsidecar, khôngtựnới vùngsafe. Template/schema/portdecision vàactualframes cònmở.\n','## End card / nguồn / safety','GiâyƯỚC '+str(s['end_card']['estimate_s'])+'; creditblock[70,240,940,1140], khôngcaptionthoại; readability3s CHƯA KIỂM.']
a.extend('- '+x for x in s['end_card']['text_lines'])
a+=['\n## Gate / các thiếu thật','- ActualDeep/Social/Reviewer chưa xemSHA r11.3; đọcto/ngườilạ/nghe1lần/timing CHƯA KIỂM.','- Preview gate1 CHƯA CHUẨN BỊ ẢNH. KhôngđồngnhấtfilekếhoạchhayChốtlờivớipreview. Cầnảnh/contactsheet/covergrid vàhai vòngsoátmắt theo phạmviđượcphép, khônglàmởlượt này.','- Productionmapping/schema/HFport/font/easing/actualcaption/bubble/coverstrictsafe chưađóng; parts_plan khôngrunnable, khôngcho build-final.','- L090 registry vẫnFAILriêng; khôngsửachecker/metadata đểđạt. Khôngtựresearch/ping/message.','- SauđúngChốt mớivoice/video, prosody/STT/realtiming/lint/mix/frameQA. Khôngaudiofinal/post12mụcđểchặn sửaactualdraft.']
bp.write_text('\n'.join(a)+'\n')
print(mdp,bp,sep='\n')
