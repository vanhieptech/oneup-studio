---
title: "Clip05 r11.4 — storyboard FILE KẾ HOẠCH patch2"
date: 2026-11-07
type: storyboard-plan
status: draft-planning-only-no-images
source: opencreator-clip05-spec-r11.4-draft-2026-11-07.json
tags: [clip05, r11.4, patch2, planning-only]
---

# CHƯA CHUẨN BỊ ẢNH
KhôngPNG/contactsheet/cover3hướng/grid/2vòngsoátmắt. Chỉfileplan, khôngpreviewđãduyệt. Giọng/timing/ngườilạ chưa kiểm; previewhình khác Chốt lời. Khôngtạoảnh/audio/render.

## Patch1→patch2: actual line delta, không rewrite
r11.2 là full rewrite B gần nhất; r11.3=patch1; r11.4=patch2. Không đếm suffix thành3patch. Giữ threshold≥3patch cùngbase cho tươnglai, không tựmiễn; vòng này Reviewer không yêu cầu rewrite.

| Lỗi / vị trí | Patch1 r11.3 | Patch2 r11.4 | Còn mở |
|---|---|---|---|
| L093 · r11.3 D23 → r11.4 D23; JSONbeats.b01 | Bạn đọc để học, mà quên gì cũng không biết. Bạn có thể nhận ra chỗ thiếu, chứ không chỉ biết mình quên. | Bạn đọc để học, mà quên gì cũng không biết. Bạn vẫn có thể nhận ra chỗ thiếu, chứ không chỉ biết mình quên. | Hứa cóthể giữ, chỉ thêm vẫn; actualsourceSHA mới chưaownerreview |
| L043 · r11.3 D41/Jhook_alt → hook_alts | 1reserve negative | 2reserve: negativegiữ + question/promise | Cảhai chưa chọn/duyệt, khôngtính spoken count |
| Cover · r11.3 D234/envelope → cover props-plan/mapping | [390,1000,660,660]→x1050/y1660, vượt30/60 | −40/−70→[350,930,660,660]→x1010/y1590;10pxmargin | Nativeadapter/ảnh/schema/raster chưaQA |
| Đồngbộ phát sinh | VI slice b01promise7từ; cácwindowbudget cũ | VI slice8từ, ENthêmstill/chuyểnhlđúngmissing; wordrange/cue/scene/caption/estimatedwindows resynced | Mọi giây vẫn ƯỚC, không đo giọng |
Không sửa b02–b07, không đổi source/method/payoff/contextB. Ngram khắc phục bằng cách nói tươngđương, không giữ lỗi bằng auditwaiver.

## Hai hook dự phòng — KHÔNG chọn, không tính count
Main hook giữ ý/cấu trúc r11.3, chỉ thêm “vẫn” cho L093. Không đề xuất đổi concept B. R64:231 yêu cầu ít nhất1 hook_alt, checklist44/L043 yêu cầu2; lưu cả hook_alt compatibility và hook_alts[2], không coi R64 là trần1.

| Option / kiểu | Lời reserve / nhấn | Đối chiếu luật | Còn mở |
|---|---|---|---|
| negative; not selected | Bạn đọc để học, đừng để {nhấn: chỗ chưa nhớ} chỉ mang tên “quên rồi”. | negative format, topic reading-to-learn; not a new method; first clause4words; no niche/school subject/time jump; no procedure before goal; no open question to leave unanswered; editorial warning, not causal study claim; 14từ reserve | warning is a proposal, not mandatory self-testing for pleasure reading; no listener approval |
| question + promise; not selected | Bạn đọc để học, mà {nhấn: quên gì} cũng không biết hả? Bạn vẫn có thể nhận ra {nhấn: chỗ thiếu}, chứ không chỉ biết mình quên. | question about the same pain then a conditional promise; <=2sentences; first clause4words, learning pain before promise; hả is a soft rhetorical invitation, no method before goal; second sentence answers the rhetorical unknown-omission pain with a promise of identifying missing content, not a new claim about texthip; 25từ reserve | actual delivery/stranger/if selected whole-script fit pending; not counted or spoken |

## Cảnh/lời/nhấn/EN/motion cùngJSON

| Beat/giây ƯỚC/người nói | Cảnh/shot | Hành động | Cảm xúc | Lời có nhấn | Vật/hành động truyền nghĩa | Animation/EFX | SFX/sound | EN ≤8/chunk + nhấn |
|---|---|---|---|---|---|---|---|---|
| b01/[0, 6.726667]/Hiệp | h1 sách mở + người đọc; cut0.8s sang phản ứng khựng h2; cut2s về cuốn sách h3. Không lật tìm trang, không gấp sách làm test trong hook. | Người đọc dừng mắt trên trang, nét mặt ngơ ngác, bàn tay mở nhẹ; rig thở/chớp mắt. Cuốn sách không đổi thành kết quả kiểm tra. | Khựng vì không gọi tên được điều đã quên, rồi tò mò; không chê người học. | Bạn đọc để học, mà {nhấn: quên gì} cũng không biết. Bạn vẫn có thể nhận ra {nhấn: chỗ thiếu}, chứ không chỉ biết mình quên. | Đảo ở nội dung: không biết mình quên gì → có thể định danh chỗ thiếu; không lấy whip thay novelty. Đây là giả thuyết lực mở, chưa người lạ/nghe/timing. | remotion/mmx-whip {"duration_frames": 13, "x_px": [60, 0]} | stamp→“quên gì” @1.448889s ƯỚC; tick→“chỗ thiếu” @4.504445s ƯỚC | b01-cap01 [4] You read to learn,; hl=[]<br>b01-cap02 [7] but can’t even tell what you **forgot.**; hl=[6]<br>b01-cap03 [6] You may still spot what’s **missing,**; hl=[5]<br>b01-cap04 [6] instead of only knowing you forgot.; hl=[] |
| b02/[6.726667, 12.271111]/Hiệp | Trung cảnh giữ nguyên bàn và sách; panel EN Text hip / Reading as lifestyle xuất hiện bên sách, không montage Hàn hay inset hai nhóm người. | Vai thả lỏng, mắt dõi sách; panel đứng cạnh sách rồi nhập vào bố cục bàn, không phân loại nhân vật. | Thoải mái, tôn trọng sở thích đọc, không chế giễu. | Text hip ở Hàn gắn sách với phong cách sống; bạn có thể {nhấn: vừa đọc vui vừa học}. | Trend ở ngay lần đọc, không cắt sang bản tin xa lạ rồi quay lại. Không dùng từ khác/Not like để chia hai nhóm. | remotion/tdev-panel {"duration_frames": 15, "rise_px": 32} | pop→“vừa đọc vui vừa học” @10.337777s ƯỚC | b02-cap01 [7] Korea’s text hip links books with lifestyle.; hl=[]<br>b02-cap02 [4] You can **enjoy** reading; hl=[2]<br>b02-cap03 [6] and **learn** at the same time.; hl=[1] |
| b03/[12.271111, 18.637778]/Hiệp | Top-down bảng10 thẻ trung tính; hai thẻ Practice testing / Rereading về nhóm HIGH UTILITY / LOW UTILITY. Không trục1–10/không%. | Mười card cùng cỡ; hai card trượt về hai nhãn nhóm, tám card còn lại không có mức cụ thể. | Tập trung, tò mò về lựa chọn, không giọng công bố chiến thắng. | Còn cách học, nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật, xếp {nhấn: tự kiểm} hữu ích cao, {nhấn: đọc lại thấp}. | Card nhóm giữ đúng ranking. Khung không có người diễn thí nghiệm; so sánh không biến thành tăng trí nhớ. | hyperframes/tdev-stagger {"duration_frames": 15, "stagger_ms": 40} | ding→“tự kiểm” @16.148889s ƯỚC; tick→“đọc lại thấp” @17.537778s ƯỚC | b03-cap01 [4] As for learning methods,; hl=[]<br>b03-cap02 [7] Dunlosky’s team rated ten techniques in 2013.; hl=[]<br>b03-cap03 [4] **Practice** **testing:** high utility.; hl=[0, 1]<br>b03-cap04 [3] **Rereading:** **low** utility.; hl=[0, 1] |
| b04/[18.637778, 21.693333]/Hiệp | Trung cảnh, sách vẫn ở vị trí cũ, Thầy nghiêng đầu rồi nhìn trang; chưa đóng sách trước lời giải pháp. | Chibi nghiêng đầu, tay dừng trên bìa sách; mắt trở lại trang đang mở. | Tò mò, rủ nhẹ với hông, không kiểm tra năng lực. | Bạn muốn biết chỗ nào trong trang sách {nhấn: chưa nhớ} hông? | Giữ sách mở đến khi đã nêu mục tiêu, tránh nêu giải pháp trước dẫn chứng/mục tiêu. | remotion/mmx-glide {"duration_frames": 10, "x_px": [18, 0]} | pop→“chưa nhớ” @20.86s ƯỚC | b04-cap01 [5] Want to know which part; hl=[]<br>b04-cap02 [6] of that page you **haven’t** **remembered?**; hl=[4, 5] |
| b05/[21.693333, 29.471111]/Hiệp | Cận tay đóng sách rồi trung cảnh tự kể với bubble; cuối beat mở sách trở lại, chưa cho thấy khoản thiếu. | Bìa khép bằng prop book; bubble chứa phần nhớ; sách mở cạnh bubble để bắt đầu so. | Thân thiện lúc nè, bình tĩnh làm mẫu, không ra lệnh trơ. | Muốn biết, Cẩm nang sống đáng giá khuyên {nhấn: tự kiểm} nè. Ví dụ đọc trang chi tiêu, bạn gấp lại, kể điều nhớ được, rồi mở ra {nhấn: dò}. | Vật book/bubble có sẵn làm rõ thao tác; chỉ đây là lời chỉ cách gỡ nên được mô tả thao tác trong thoại. | remotion/tdev-icon-swap {"duration_frames": 11} | click→“tự kiểm” @23.915555s ƯỚC; tick→“dò” @29.193333s ƯỚC | b05-cap01 [7] To find out, the handbook recommends **self-testing.**; hl=[6]<br>b05-cap02 [6] For a sample page about spending,; hl=[]<br>b05-cap03 [7] close it and retell what you remember.; hl=[]<br>b05-cap04 [5] Then reopen it and **check.**; hl=[4] |
| b06/[29.471111, 36.971111]/Hiệp | Top-down hai cột Source page / Your retelling. Nguồn có Food + Rent; phần kể ban đầu chỉ Food. Rent xuất hiện thêm trong phần kể ở câu2. | Khối nhãn Rent ở bản gốc giữ nguyên; một bản label điền vào phần kể sau lời nhận ra, không gạch/vẽ nét. | Nhận ra rồi bổ sung, không ăn mừng như giải quyết tài chính. | Lúc dò, bạn nhận ra bài nhắc ghi cả {nhấn: tiền thuê nhà}, còn phần kể chỉ có tiền ăn. À, bạn {nhấn: bổ sung} khoản vừa sót đó. | Payoff là chỗ thiếu có tên trong phần kể, không kết quả người đó quản tiền tốt hơn. Không dùng disclaimer để chữa claim khác. | hyperframes/tdev-page {"duration_frames": 14, "x_px": [8, 0]} | snap→“tiền thuê nhà” @31.971111s ƯỚC; ding→“bổ sung” @35.304445s ƯỚC | b06-cap01 [7] When checking, you notice the page includes; hl=[]<br>b06-cap02 [7] recording **rent,** but you only mentioned food.; hl=[1]<br>b06-cap03 [7] Ah, you **add** the expense you missed.; hl=[2] |
| b07/[36.971111, 42.804444]/Hiệp | Trung cảnh Thầy và ô comment; hai lựa chọn Complete / Missing. Không thêm nút follow/like. | Chibi nhìn người xem, bàn tay mở nhẹ về khung bình luận; khung trượt ra để loop. | Mời chia sẻ, không thúc ép, nha đọc thường. | Giả sử kể lại trang bạn vừa đọc, bạn thấy {nhấn: đủ hay thiếu}? Bình luận một chữ {nhấn: đủ hoặc thiếu} nha. | EN giữ Say… và Would…; comment một trong hai từ, không đổi giả định thành lệnh kiểm tra. | remotion/mmx-snap-settle {"duration_frames": 11, "scale": [0.96, 1]} | pop→“đủ hay thiếu” @39.748889s ƯỚC | b07-cap01 [8] Say you retold the page you just read.; hl=[]<br>b07-cap02 [7] Would it be **complete** or **missing** something?; hl=[3, 5]<br>b07-cap03 [6] Comment one word: **complete** or **missing.**; hl=[3, 5] |
| end/[42.804444, 45.804444]/không thoại | Card tĩnh cólogo | Một entrance rồi giữ | Trung tính | Không thoại | Safety/credit/license | mmx-soft-inout9f | whoosh-soft seam−0.12s ƯỚC | Credit nguyênvăn ởmục endcard; khôngcaptionthoại |

## First→mid→end giữ nguyên patch1
b01: sáchmở/titleEN→mặtkhựng→cùngsách; chưaFood/Rent/phầnkể. b02: giữsách→panelText hip/lifestyle→đọcvui+học đồngtồn tại. b03:10thẻtrungtính→2kỹthuật→HIGH/LOWutility; khôngcomic/%. b04: tò mò→giữtrangmở→chưađóngtrướcmục tiêu. b05: HTB→đóng/kểFood→mởdò chưaRent. b06: nguồn/phầnkể→revealRent đúngcue→bổsung vào phầnkể. b07: ngườiđọc→Complete/Missing→1commentloop. End: credit/an toàn.

## Mapping

| Unit → engine target | Beat / voice-line | Giây ƯỚC | Narration hiển thị | Captionrefs / layout |
|---|---|---|---|---|---|
| A/b01-h1→parts[].scenes[] | b01/vi-b01 | [0, 0.8] | FORGOT... WHAT? | b01-cap01/hook-wide |
| A/b01-h2→parts[].scenes[] | b01/vi-b01 | [0.8, 2.0] | inherit globalhook-title | b01-cap01,b01-cap02/hook-reaction |
| A/b01-h3→parts[].scenes[] | b01/vi-b01 | [2.0, 6.726667] | inherit globalhook-title | b01-cap02,b01-cap03,b01-cap04/hook-wide |
| A/b02-s1→parts[].scenes[] | b02/vi-b02 | [6.726667, 12.271111] | none | b02-cap01,b02-cap02,b02-cap03/reading-context |
| E1/b03-e1→parts[].sections[] | b03/vi-b03 | [12.271111, 18.637778] | none | b03-cap01,b03-cap02,b03-cap03,b03-cap04/ranking |
| B/b04-s1→parts[].scenes[] | b04/vi-b04 | [18.637778, 21.693333] | none | b04-cap01,b04-cap02/reading-goal |
| B/b05-s1→parts[].scenes[] | b05/vi-b05 | [21.693333, 29.471111] | none | b05-cap01,b05-cap02,b05-cap03,b05-cap04/reading-method |
| E2/b06-e1→parts[].sections[] | b06/vi-b06 | [29.471111, 36.971111] | none | b06-cap01,b06-cap02,b06-cap03/comparison |
| C/b07-s1→parts[].scenes[] | b07/vi-b07 | [36.971111, 42.804444] | none | b07-cap01,b07-cap02,b07-cap03/cta |
| C/end-s1→parts[].scenes[] | end/None | [42.804444, 45.804444] | none | /credit |

## Caption/VI/range/timebindings ƯỚC
| ID | VI exact/range | EN+hl | Interval ƯỚC |
|---|---|---|---|
| b01-cap01 | Bạn đọc để học,/[0, 4] | You read to learn,/[] | [0.06, 1.171111] |
| b01-cap02 | mà quên gì cũng không biết./[4, 10] | but can’t even tell what you forgot./[6] | [1.171111, 2.837778] |
| b01-cap03 | Bạn vẫn có thể nhận ra chỗ thiếu,/[10, 18] | You may still spot what’s missing,/[5] | [2.837778, 5.06] |
| b01-cap04 | chứ không chỉ biết mình quên./[18, 24] | instead of only knowing you forgot./[] | [5.06, 6.726667] |
| b02-cap01 | Text hip ở Hàn gắn sách với phong cách sống;/[0, 10] | Korea’s text hip links books with lifestyle./[] | [6.726667, 9.504444] |
| b02-cap02 | bạn có thể vừa đọc vui/[10, 16] | You can enjoy reading/[2] | [9.504444, 11.171111] |
| b02-cap03 | vừa học./[16, 18] | and learn at the same time./[1] | [11.171111, 12.271111] |
| b03-cap01 | Còn cách học,/[0, 3] | As for learning methods,/[] | [12.271111, 13.371111] |
| b03-cap02 | nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật,/[3, 12] | Dunlosky’s team rated ten techniques in 2013./[] | [13.371111, 15.871111] |
| b03-cap03 | xếp tự kiểm hữu ích cao,/[12, 18] | Practice testing: high utility./[0, 1] | [15.871111, 17.537778] |
| b03-cap04 | đọc lại thấp./[18, 21] | Rereading: low utility./[0, 1] | [17.537778, 18.637778] |
| b04-cap01 | Bạn muốn biết chỗ nào/[0, 5] | Want to know which part/[] | [18.637778, 20.026667] |
| b04-cap02 | trong trang sách chưa nhớ hông?/[5, 11] | of that page you haven’t remembered?/[4, 5] | [20.026667, 21.693333] |
| b05-cap01 | Muốn biết, Cẩm nang sống đáng giá khuyên tự kiểm nè./[0, 11] | To find out, the handbook recommends self-testing./[6] | [21.693333, 24.748889] |
| b05-cap02 | Ví dụ đọc trang chi tiêu,/[11, 17] | For a sample page about spending,/[] | [24.748889, 26.415556] |
| b05-cap03 | bạn gấp lại, kể điều nhớ được,/[17, 24] | close it and retell what you remember./[] | [26.415556, 28.36] |
| b05-cap04 | rồi mở ra dò./[24, 28] | Then reopen it and check./[4] | [28.36, 29.471111] |
| b06-cap01 | Lúc dò, bạn nhận ra bài nhắc ghi cả/[0, 9] | When checking, you notice the page includes/[] | [29.471111, 31.971111] |
| b06-cap02 | tiền thuê nhà, còn phần kể chỉ có tiền ăn./[9, 19] | recording rent, but you only mentioned food./[1] | [31.971111, 34.748889] |
| b06-cap03 | À, bạn bổ sung khoản vừa sót đó./[19, 27] | Ah, you add the expense you missed./[2] | [34.748889, 36.971111] |
| b07-cap01 | Giả sử kể lại trang bạn vừa đọc,/[0, 8] | Say you retold the page you just read./[] | [36.971111, 39.193333] |
| b07-cap02 | bạn thấy đủ hay thiếu?/[8, 13] | Would it be complete or missing something?/[3, 5] | [39.193333, 40.582222] |
| b07-cap03 | Bình luận một chữ đủ hoặc thiếu nha./[13, 21] | Comment one word: complete or missing./[3, 5] | [40.582222, 42.804444] |
VI slices làbindingdịch, KHÔNG đơnvịsinh/cắtF5. Một globalcaptionsegment/lần; title/caption khôngreset qua3hookcuts.

## Bbox cùngJSON — chỉsốhọc
Content[60,150,960,1310]; captionzone[60,1488,960,312]; logo[60,80,100,70]. StandardRemotioncaption1488/HF1500; khôngcoi captionphảiởcontenty≤1460. Cácbox gồm dựtrùmargin, khôngactualraster.
| Layout | Allocations/motionenvelopes |
|---|---|
| hook-wide | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hook-title", "bbox": [180, 170, 780, 150], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [660, 390, 300, 350], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "same-book", "bbox": [140, 800, 720, 639], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection", "existing_prop_binding_plan": {"kind": "book", "x": 500, "y": 1119.5, "s": 1.35, "rot": 0, "local_bounds": [-240, -210, 240, 210], "padding": 36, "source": "layout.ts18/48–50", "actual_rendered": false}}] |
| hook-reaction | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hook-title", "bbox": [180, 170, 780, 150], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [211, 390, 648, 700], "zone": "content", "motion_envelope": {"x": [0, 60], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}] |
| reading-context | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "context-panel", "bbox": [180, 180, 780, 130], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "vi-bubble", "bbox": [100, 350, 500, 380], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [660, 390, 300, 350], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "same-book", "bbox": [140, 800, 720, 639], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection", "existing_prop_binding_plan": {"kind": "book", "x": 500, "y": 1119.5, "s": 1.35, "rot": 0, "local_bounds": [-240, -210, 240, 210], "padding": 36, "source": "layout.ts18/48–50", "actual_rendered": false}}] |
| reading-goal | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "vi-bubble", "bbox": [100, 350, 500, 380], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [660, 390, 300, 350], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "same-book", "bbox": [140, 800, 720, 639], "zone": "content", "motion_envelope": {"x": [0, 18], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection", "existing_prop_binding_plan": {"kind": "book", "x": 500, "y": 1119.5, "s": 1.35, "rot": 0, "local_bounds": [-240, -210, 240, 210], "padding": 36, "source": "layout.ts18/48–50", "actual_rendered": false}}] |
| reading-method | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "vi-bubble", "bbox": [100, 350, 500, 380], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [660, 390, 300, 350], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "same-book", "bbox": [140, 800, 720, 639], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection", "existing_prop_binding_plan": {"kind": "book", "x": 500, "y": 1119.5, "s": 1.35, "rot": 0, "local_bounds": [-240, -210, 240, 210], "padding": 36, "source": "layout.ts18/48–50", "actual_rendered": false}}] |
| ranking | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "ranking-heading", "bbox": [100, 220, 880, 100], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "ranking-objects", "bbox": [90, 350, 900, 1020], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 16], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}] |
| comparison | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "comparison-heading", "bbox": [100, 220, 880, 100], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "source-retelling", "bbox": [90, 350, 900, 1020], "zone": "content", "motion_envelope": {"x": [0, 8], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}] |
| cta | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "vi-bubble", "bbox": [100, 350, 500, 380], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "hiep-rig", "bbox": [660, 390, 300, 350], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "comment-options", "bbox": [100, 820, 760, 340], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [0.96, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}] |
| credit | [{"id": "logo", "bbox": [60, 80, 100, 70], "zone": "logo", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}, {"id": "credit-block", "bbox": [70, 240, 940, 1140], "zone": "content", "motion_envelope": {"x": [0, 0], "y": [0, 0], "scale": [1, 1]}, "bbox_status": "PLANNED allocation, not actual renderer projection"}] |
Camera_push0 trongplan; phép tínhcontainment/disjoint khôngthayactualrig/bubbletail/glyph/wrap/camera. StandardTikTokplan, khôngkếthừa sangReels.

## Cover patch2 — một mapping an toàn trong kế hoạch
Không đổi template A/theme/series/ep/hero/strike/accent/expression/action/tilt/font/text/logo. Chỉ dịch nhóm illustration có sẵn (halo/chibi/emote) −40px ngang, −70px dọc; số vượt30/60 được sửa, thêm10px thở phải/dưới. Không asset mới/ảnh/doodle.

```json
{
  "direction": "a",
  "theme": "dark",
  "series": "Read + Learn",
  "ep": 5,
  "hero": [
    "REREAD",
    "SELF-TEST"
  ],
  "strike": 0,
  "accent": 1,
  "expression": "confused",
  "action": "thinking",
  "emote": "!",
  "tilt": -5,
  "template": "video-engine/src/composition/Cover.tsx",
  "rendered": false,
  "note": "Native A props retained; one explicit illustration-group transform planned. Numeric bbox safe in this plan, not proof current fixed template implements override or images pass.",
  "illustration_transform_plan": {
    "translate_x_px": -40,
    "translate_y_px": -70,
    "applies_to": [
      "halo",
      "chibi",
      "emote"
    ],
    "keep_unchanged": [
      "direction A",
      "dark theme",
      "series/ep",
      "hero/strike/accent",
      "expression/action/tilt",
      "text slots",
      "logo slot"
    ],
    "purpose": "Fix right30/bottom60 overshoot with10px right/bottom breathing room, without redesign",
    "native_template_support": false,
    "status": "PLANNING override; current Cover.tsx fixed positions need adapter mapping later. No engine code/render/schema validation here."
  }
}
```
| Component allocation | r11.3 baseline | r11.4 plan | Strict-safe arithmetic |
|---|---|---|---|
| series | [72, 310, 850, 80] | [72, 310, 850, 80] | x60–1020/y290–1600 |
| hero | [66, 420, 930, 380] | [66, 420, 930, 380] | x60–1020/y290–1600 |
| rig+circle-reserve | [390, 1000, 660, 660] | [350, 930, 660, 660] | x60–1020/y290–1600 |
| logo | [72, 1470, 260, 70] | [72, 1470, 260, 70] | x60–1020/y290–1600 |
Mapping {"before_bbox": [390, 1000, 660, 660], "translate_px": [-40, -70], "after_bbox": [350, 930, 660, 660], "right_bottom_margins_px": [10, 10], "props_ref": "cover.illustration_transform_plan", "actual_renderer_implementation": "CHƯA KIỂM/NOT IMPLEMENTED in this read-only task"}
Current Cover.tsx chưa có native prop nhận transform này: illustration_transform_plan là mapping/props KẾ HOẠCH cần adapter ởpha sảnxuất, KHÔNG nói engine đã sửa. Baseline vượt vùng được giữ đểtruyvết, khôngtrộn với bboxr11.4. Không còn hai bảng target/current mâu thuẫn trong plan r11.4. Số học khác ảnh thật; schema/templateport/rigstroke/glyph/crop/readability CHƯA KIỂM.
**Preview gate1: CHƯA CHUẨN BỊ ẢNH** — thiếu PNG từngbeat/contactsheet/cover3hướng/grid/hai vòngsoátmắt. Fileplan không thay preview; preview hình khác Chốt lời và video. Không tạoảnh ởlượt này.

## Trang mock và endcard
Nhãn“Editorial illustration” b05–06. Cùngsáchmock khônggắntrangHTB: “Record food expenses”/“Record rent”; phầnkểchỉFood, Rentđúngcue mới lộ rồi thêm. Khôngsourcecase/thínghiệm/lờikhuyên tàichính.
EndƯỚC[42.804444, 45.804444],creditblock[70,240,940,1140];3s chưađo độđọc.
- Thông tin tham khảo, không thay thế tư vấn chuyên gia
- Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
- Đã chuyển thể. Giấy phép: https://creativecommons.org/licenses/by/4.0/
- Dunlosky et al. (2013) · Trend context: Znews 05/11/2026

## Gates / checks / hạn chế thật
- Đọc to/người lạ/nghe1lần/timing: CHƯA KIỂM. Không nói ai đã đọc/nghe thật; textchecks không thay cổng tai.
- Deep/Social/Reviewer chưa xem SHA r11.4. Không kếthừa verdict từ SHA cũ.
- Registry L090 lookup vẫn riêng, nguồn đã bàn giao không bị gọi là chưa nghiên cứu. Metadata/addendum/storage/archival scratch chưa sanctioned sync; không sửa ID/checker/metadata để qua máy.
- Callback/release04/theme/signature cònmở; không nói cliptrước đãđăng/đãxem. Effects-log không sửa. Không thêm nghiên cứu hay chờ việc này để cấm chuẩn bị file.
- Production schema/HFport/font/bubble/titleport/Reels/realcaption/hit/resnap/mix/frameQA chưađóng. Spec planning_only=true/renderable=false/locked=false, không đưa vào build.
- Previewgate1 CHƯA CHUẨN BỊ ẢNH. Không audio/images/render/repo edits/commit/push/messages.
- Textchecker nguyênbản: subjects/l088/trend/flow/clarity/link/repeat/evidence/choppy/fresh. Fresh lỗi khi so cùng vòngpatch được giữ nguyên, KHÔNG tự diễn giải cần rewrite; Reviewer đã xác định phạmvi patch2. Không tựPASS/xinChốt.
- Output: /workspace/clip05-r11.4-checker-output-2026-11-07.txt; numeric: /workspace/clip05-r11.4-local-validation-2026-11-07.json; manifest: /workspace/clip05-r11.4-delivery-manifest-2026-11-07.json. Không --final/STT/build/productionvalidator.

