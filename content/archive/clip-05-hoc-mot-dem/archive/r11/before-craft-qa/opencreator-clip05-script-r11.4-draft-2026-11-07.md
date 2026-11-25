---
title: "Clip05 r11.4 — B patch2, không rewrite"
date: 2026-11-07
type: script
status: draft — chưa Chốt, không tựpass
source: "Reviewer r11.3; Social bd53fd3/pain7fb1e4b; Deep d673dd9/b02dd07"
tags: [clip05, r11.4, patch2, direction-C]
trend_id: texthip-kr-reading-lifestyle-znews-1693810
hook_pattern: P10
trend_beats: b02
trend_spoken: "Text hip"
example_evidence: x-2115086418192089298
fact_lock: research/fact-packages/factcheck-clip05-lock-2026-11-07.md
spoken_words: 150
---

# Actual draft B patch2 — không trình xin Chốt

Đọc to/người lạ/nghe1lần/timing CHƯA KIỂM. Previewgate1 CHƯA CHUẨN BỊ ẢNH. Chỉ sửa3lỗi được giao, không outline/research/rewrite.

## Lời thoại —150 từ;50 sauhook trước method

1. **[Hook / pain + hứa]** Bạn đọc để học, mà quên gì cũng không biết. Bạn vẫn có thể nhận ra chỗ thiếu, chứ không chỉ biết mình quên.
2. **[Bối cảnh trend + thêm mục tiêu]** Text hip ở Hàn gắn sách với phong cách sống; bạn có thể vừa đọc vui vừa học.
3. **[Dẫn chứng chọn kỹ thuật]** Còn cách học, nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật, xếp tự kiểm hữu ích cao, đọc lại thấp.
4. **[Mục tiêu / móc giữa]** Bạn muốn biết chỗ nào trong trang sách chưa nhớ hông?
5. **[Giải pháp HTB / minh họa]** Muốn biết, Cẩm nang sống đáng giá khuyên tự kiểm nè. Ví dụ đọc trang chi tiêu, bạn gấp lại, kể điều nhớ được, rồi mở ra dò.
6. **[Payoff đối chiếu]** Lúc dò, bạn nhận ra bài nhắc ghi cả tiền thuê nhà, còn phần kể chỉ có tiền ăn. À, bạn bổ sung khoản vừa sót đó.
7. **[CTA / loop]** Giả sử kể lại trang bạn vừa đọc, bạn thấy đủ hay thiếu? Bình luận một chữ đủ hoặc thiếu nha.

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

## Nguồn và ranh giới claim

| Nguồn | Provenance | Được dùng | Không được suy |
|---|---|---|
| TrendC | research/trends/2026-11-07-clip05-texthip-bridge-check.md @bd53fd3; Znews05/11/2026 06:00, snapshot07/11 14:07:28 Asia/Saigon; News báo sync, không kiểm live lượt này | Text hip gắn sách/đọc với phong cách sống; b02 | Không gọi hot, không gán participants quên/tự kiểm, không chê pilsa, không nói mọi GenZ bỏ video ngắn |
| Pain độc lập | research/trends/2026-10-30/clip-05-v9-trend.md @7fb1e4b dòng17; x-2115086418192089298; reply27/10; snapshot30/10 18:25 Asia/Saigon;0like | MỘT tự thuật không nhớ điều đã đọc, đủ phát triển tình huống đọc theo bàn giao Social/Reviewer14:51 | Không đại diện khán giả kênh/đám đông/texthip; không chứng minh kể thiếu trong phép thử; không lấy buồn ngủ làm cơ chế. Dòng18 trong archive là diễn giải cũ quá rộng, KHÔNG coi là trích dẫn |
| Fact | factcheck-clip05-lock-2026-11-07.md @b02dd07 dòng22–28 | b03: tổng quan10kỹ thuật, đối chiếu HIGH/LOW utility | Không %/thí nghiệm chia nhóm/nhớ lâu/hiệu quả người đi làm; không phủ định tổng quan có bằng chứng học/nhớ |
| Phương pháp | clip05-texthip-fact-bridge-2026-11-07.md @d673dd9 dòng16–25 | b05: F5 đóng–tự kể–mở dò; mục tiêu nhớ là khuyến nghị riêng | Không coi đây là hành vi người theo trend, không hiệu quả thực hành đảm bảo |
| Trang chi tiêu | MINH HỌA BIÊN TẬP CỦA KÊNH; mock sách cùng lần đọc | b05–b06 có trang nhắc Food+Rent, phần kể chỉFood, rồi bổ sungRent | Không phải trang gốcHTB, không mẹo tài chính có nguồn, không kết quả thí nghiệm hay ca trong reply. Không khuyên quyết định chi tiền |

Pain quote nguyên văn để audit: “I can't replace doomscrolling with reading though because I can't remember what I read, especially if drowsy.” — https://x.com/phrog_lmao/status/2115086418192089298. Chỉ mở archive repo, KHÔNG dùng X tool/kiểm live. Markdown lưu là bằng chứng đang có; raw/live mới không có. Metadata chủ nguồn đang lưu, không bịa commit cho addendum.



## Một ý / count / mạch giữ nguyên
Bạn đọc vừa cóniềm vui vừa cóthêm mục tiêu nhớ; tựkiểm rồi dòtrang giúp nhận ra phần thiếu trong phần kể. Không causaltexthip→quên/không chêpilsa/không loại trừ đọcthưởng thức. Pain–promise–payoff đã được Reviewer r11.3 chấpnhận vềvăn bản, không viếtlại.
150 =24+18+21+11+28+27+21; premethod50=18+21+11; study21từ/1câu. Durationbudget 45.804444s ƯỚC, không đo/khôngpadding55s.

## Bảng9cột cùngJSON — toàn bộ là plan

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

## Trường chi tiết / nhấn VI–EN / nguồn

### b01 · Hook / pain + hứa
| Trường | Nội dung |
|---|---|
| Vai trò | Pain: chưa gọi tên được nội dung đã quên. Hứa: có thể nhận ra phần thiếu; cùng một đối tượng nội dung, không nói phần kể đã tồn tại. |
| Ngữ cảnh | Một lần đọc ở bàn, cùng sách mock; chưa giới thiệu thao tác tự kiểm, chưa có phần kể. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Phẩy sau học; câu đầu rơi ở không biết. Câu hứa liền mạch, nhấn chỗ thiếu; không chia chữ theo cut. |
| VI+nhấn | Bạn đọc để học, mà {nhấn: quên gì} cũng không biết. Bạn vẫn có thể nhận ra {nhấn: chỗ thiếu}, chứ không chỉ biết mình quên. |
| VI–ENmeaningfocus | [{"vi": "quên gì", "caption_targets": [{"id": "b01-cap02", "hl": [6], "highlight_words": ["forgot."]}]}, {"vi": "chỗ thiếu", "caption_targets": [{"id": "b01-cap03", "hl": [5], "highlight_words": ["missing,"]}]}] |
| VI→ENbinding | Bạn đọc để học,→You read to learn,<br>mà quên gì cũng không biết.→but can’t even tell what you forgot.<br>Bạn vẫn có thể nhận ra chỗ thiếu,→You may still spot what’s missing,<br>chứ không chỉ biết mình quên.→instead of only knowing you forgot. |
| Link | S1 chưa gọi tên được phần quên → S2 hứa có thể nhận ra phần thiếu ấy. Không cần người nghe tự thêm hành động kể hoặc mốc ngay đó. |
| Claim/source | Chi tiết comic biên tập phát triển từ pain đọc–nhớ có nguồn cá nhân; không trích source như đã có cảnh này hoặc tần suất quên. Hứa giới hạn có thể, chỉ đối chiếu văn bản. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b02 · Bối cảnh trend + thêm mục tiêu
| Trường | Nội dung |
|---|---|
| Vai trò | Cùng lần đọc có cả giá trị tận hưởng và mục tiêu học; trend làm bối cảnh, không làm bằng chứng quên. |
| Ngữ cảnh | Vẫn cùng cuốn sách và bàn; kể bối cảnh báo chí, không giả đây là người tham gia #texthip. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Dấu chấm phẩy phân hai ý bối cảnh/mục tiêu; không ngắt text hip hay phong cách sống. |
| VI+nhấn | Text hip ở Hàn gắn sách với phong cách sống; bạn có thể {nhấn: vừa đọc vui vừa học}. |
| VI–ENmeaningfocus | [{"vi": "vừa đọc vui vừa học", "caption_targets": [{"id": "b02-cap02", "hl": [2], "highlight_words": ["enjoy"]}, {"id": "b02-cap03", "hl": [1], "highlight_words": ["learn"]}]}] |
| VI→ENbinding | Text hip ở Hàn gắn sách với phong cách sống;→Korea’s text hip links books with lifestyle.<br>bạn có thể vừa đọc vui→You can enjoy reading<br>vừa học.→and learn at the same time. |
| Link | Cùng cuốn sách ở hook: từ nhu cầu học mở ra giá trị khác có thể đi cùng. Cuối beat giữ rõ chữ học để dẫn lựa chọn kỹ thuật. |
| Claim/source | Social bd53fd3 cho mô tả trend; hai mục tiêu đi cùng là lời nối biên tập, không kết quả nghiên cứu. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b03 · Dẫn chứng chọn kỹ thuật
| Trường | Nội dung |
|---|---|
| Vai trò | Từ mục tiêu học, đưa lựa chọn kỹ thuật có nguồn: chỉ xếp hạng hữu ích, không kết quả đo trực tiếp. |
| Ngữ cảnh | Chỉ bảng kỹ thuật trên mặt bàn cùng palette, không chibi trong explainer. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Nhịp phẩy sau cách học và kỹ thuật; không ngắt tên tác giả/năm hay mười kỹ thuật. Không đọc thành danh sách ba nhóm. |
| VI+nhấn | Còn cách học, nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật, xếp {nhấn: tự kiểm} hữu ích cao, {nhấn: đọc lại thấp}. |
| VI–ENmeaningfocus | [{"vi": "tự kiểm", "caption_targets": [{"id": "b03-cap03", "hl": [0, 1], "highlight_words": ["Practice", "testing:"]}]}, {"vi": "đọc lại thấp", "caption_targets": [{"id": "b03-cap04", "hl": [0, 1], "highlight_words": ["Rereading:", "low"]}]}] |
| VI→ENbinding | Còn cách học,→As for learning methods,<br>nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật,→Dunlosky’s team rated ten techniques in 2013.<br>xếp tự kiểm hữu ích cao,→Practice testing: high utility.<br>đọc lại thấp.→Rereading: low utility. |
| Link | Còn cách học nhận học ở b02; xếp hạng là lý do có nguồn để cân nhắc tự kiểm, không bằng chứng trend. |
| Claim/source | Deep b02dd07 dòng22–28. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b04 · Mục tiêu / móc giữa
| Trường | Nội dung |
|---|---|
| Vai trò | Mục tiêu: nhận ra phần nội dung chưa nhớ, không nói như thể phép tự kể đã diễn ra. |
| Ngữ cảnh | Quay lại cùng người đọc đang cân nhắc thêm mục tiêu học cho trang vừa thích. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Một câu hỏi liền; hông lên nhẹ tự nhiên, chưa có đo pitch. |
| VI+nhấn | Bạn muốn biết chỗ nào trong trang sách {nhấn: chưa nhớ} hông? |
| VI–ENmeaningfocus | [{"vi": "chưa nhớ", "caption_targets": [{"id": "b04-cap02", "hl": [4, 5], "highlight_words": ["haven’t", "remembered?"]}]}] |
| VI→ENbinding | Bạn muốn biết chỗ nào→Want to know which part<br>trong trang sách chưa nhớ hông?→of that page you haven’t remembered? |
| Link | Từ kỹ thuật tự kiểm được xếp hạng chuyển sang đích người xem muốn biết: nội dung nào chưa nhớ; b05 giải đáp ngay. |
| Claim/source | Mục tiêu/điều kiện biên tập, không claim thí nghiệm. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b05 · Giải pháp HTB / minh họa
| Trường | Nội dung |
|---|---|
| Vai trò | Gọi tên tự kiểm theo23.14 rồi làm đủ đóng→tự kể→mở dò trên một trang minh họa. |
| Ngữ cảnh | Cuốn sách minh họa mở đúng trang chi tiêu; đây KHÔNG phải trang chụp từ cẩm nang. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Phẩy sau Muốn biết; chấm trước Ví dụ; chuỗi thao tác giữ chủ ngữ bạn. Không chẻ kể điều nhớ được. |
| VI+nhấn | Muốn biết, Cẩm nang sống đáng giá khuyên {nhấn: tự kiểm} nè. Ví dụ đọc trang chi tiêu, bạn gấp lại, kể điều nhớ được, rồi mở ra {nhấn: dò}. |
| VI–ENmeaningfocus | [{"vi": "tự kiểm", "caption_targets": [{"id": "b05-cap01", "hl": [6], "highlight_words": ["self-testing."]}]}, {"vi": "dò", "caption_targets": [{"id": "b05-cap04", "hl": [4], "highlight_words": ["check."]}]}] |
| VI→ENbinding | Muốn biết, Cẩm nang sống đáng giá khuyên tự kiểm nè.→To find out, the handbook recommends self-testing.<br>Ví dụ đọc trang chi tiêu,→For a sample page about spending,<br>bạn gấp lại, kể điều nhớ được,→close it and retell what you remember.<br>rồi mở ra dò.→Then reopen it and check. |
| Link | Muốn biết trả lời ngay câu hỏi b04; ví dụ minh họa thao tác, không giới thiệu nguyên nhân mới. |
| Claim/source | Deep d673dd9 dòng16–17: F5. Trang chi tiêu là mock của kênh. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b06 · Payoff đối chiếu
| Trường | Nội dung |
|---|---|
| Vai trò | Đối chiếu đúng thứ vừa kể với đúng trang; chỉ bổ sung phần thiếu trong minh họa. |
| Ngữ cảnh | Hai bản: trang sách mock và phần tự kể; khoản thuê nhà chỉ được reveal lúc đối chiếu. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Phẩy sau Lúc dò và nhà; nghỉ chấm trước À. Không ngắt tiền thuê nhà. |
| VI+nhấn | Lúc dò, bạn nhận ra bài nhắc ghi cả {nhấn: tiền thuê nhà}, còn phần kể chỉ có tiền ăn. À, bạn {nhấn: bổ sung} khoản vừa sót đó. |
| VI–ENmeaningfocus | [{"vi": "tiền thuê nhà", "caption_targets": [{"id": "b06-cap02", "hl": [1], "highlight_words": ["rent,"]}]}, {"vi": "bổ sung", "caption_targets": [{"id": "b06-cap03", "hl": [2], "highlight_words": ["add"]}]}] |
| VI→ENbinding | Lúc dò, bạn nhận ra bài nhắc ghi cả→When checking, you notice the page includes<br>tiền thuê nhà, còn phần kể chỉ có tiền ăn.→recording rent, but you only mentioned food.<br>À, bạn bổ sung khoản vừa sót đó.→Ah, you add the expense you missed. |
| Link | Lúc dò nhận bước cuối b05; phát hiện phần thiếu nhờ đặt hai bản cạnh nhau, không suy thành khó khăn thực hành. |
| Claim/source | Kết quả trong mock: đối chiếu phần kể với trang; không đo/khẳng định hiệu quả ngoài đời. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |
### b07 · CTA / loop
| Trường | Nội dung |
|---|---|
| Vai trò | Điều kiện mềm, một yêu cầu comment một từ; nhắc thiếu để đóng vòng hook. |
| Ngữ cảnh | Cùng người đọc hướng mắt về camera; không giả đã áp dụng thành công ngoài đời. |
| Voice | Hiệp/Thầy ngôi bạn, F5·TháiSơn speed1.0 chỉ sauChốt; tuần1 khôngOmi/app |
| Pauseplan | Phẩy sau đọc; nghỉ câu hỏi; nha đọc thường cuối CTA. Không tạo file delivery audio. |
| VI+nhấn | Giả sử kể lại trang bạn vừa đọc, bạn thấy {nhấn: đủ hay thiếu}? Bình luận một chữ {nhấn: đủ hoặc thiếu} nha. |
| VI–ENmeaningfocus | [{"vi": "đủ hay thiếu", "caption_targets": [{"id": "b07-cap02", "hl": [3, 5], "highlight_words": ["complete", "missing"]}]}, {"vi": "đủ hoặc thiếu", "caption_targets": [{"id": "b07-cap03", "hl": [3, 5], "highlight_words": ["complete", "missing."]}]}] |
| VI→ENbinding | Giả sử kể lại trang bạn vừa đọc,→Say you retold the page you just read.<br>bạn thấy đủ hay thiếu?→Would it be complete or missing something?<br>Bình luận một chữ đủ hoặc thiếu nha.→Comment one word: complete or missing. |
| Link | Giả sử gọi lại phép tự kể trên một trang; đủ/thiếu nối payoff và từ thiếu của hook. Không yêu cầu làm test rồi lại comment như hai CTA. |
| Claim/source | Không claim hiệu quả hoặc phát hành clip04. |
| Trạngthái | read-aloud/stranger/timing CHƯA KIỂM; actualownerSHA chưareview |

## Bảng hiệu ứng r11.4 — một main/beat,0accent/0doodle

| Beat | Engine/main/source/params | Vật/hànhđộng | Anchor/SFX ƯỚC |
|---|---|---|---|
| b01 | remotion/mmx-whip/motionmaxxing {"duration_frames": 13, "x_px": [60, 0]} | Whip vào phản ứng khựng khi không gọi tên được nội dung quên; cùng rig/sách, không tạo vật mới. | stamp→“quên gì” @1.448889s ƯỚC; tick→“chỗ thiếu” @4.504445s ƯỚC |
| b02 | remotion/tdev-panel/transitions.dev {"duration_frames": 15, "rise_px": 32} | Panel bối cảnh bám sách hiện có, không chia người thành nhóm. | pop→“vừa đọc vui vừa học” @10.337777s ƯỚC |
| b03 | hyperframes/tdev-stagger/transitions.dev {"duration_frames": 15, "stagger_ms": 40} | Các thẻ hiện; dịch thẻ cùng timeline, không mô phỏng số đo. | ding→“tự kiểm” @16.148889s ƯỚC; tick→“đọc lại thấp” @17.537778s ƯỚC |
| b04 | remotion/mmx-glide/motionmaxxing {"duration_frames": 10, "x_px": [18, 0]} | Dịch framing nhẹ vào cuốn sách; không zoom vào chữ. | pop→“chưa nhớ” @20.86s ƯỚC |
| b05 | remotion/tdev-icon-swap/transitions.dev {"duration_frames": 11} | Trạng thái book đóng/mở; không vẽ lại sách. | click→“tự kiểm” @23.915555s ƯỚC; tick→“dò” @29.193333s ƯỚC |
| b06 | hyperframes/tdev-page/transitions.dev {"duration_frames": 14, "x_px": [8, 0]} | Hai panel đối chiếu đã có, thêm nhãn bằng transform; không doodle. | snap→“tiền thuê nhà” @31.971111s ƯỚC; ding→“bổ sung” @35.304445s ƯỚC |
| b07 | remotion/mmx-snap-settle/motionmaxxing {"duration_frames": 11, "scale": [0.96, 1]} | Ô comment hạ cánh, không overshoot/spring. | pop→“đủ hay thiếu” @39.748889s ƯỚC |
| end | static/mmx-soft-inout9f | Creditcard | whoosh-soft seam−0.12s ƯỚC |
SFXcó sẵn SOURCES14–16; swish/whoosh-softtransition vàambience brownnoise nhẹ xuyênclip; khôngnhạc. Assets-first, không còi/doodle/newassets. Signatureclip04/log/realmix/realcue chưa kiểm; khôngnpx/HFbuild/fx-table/codeengine.

## Mapping scene/narration/timing

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
{"status": "ESTIMATE ONLY — CHƯA KIỂM timing, not word timestamps", "method": "budget each VI caption slice at 3.6 whitespace words/s, minimum1.1s of planned caption time; voice onset0.06s only in b01. This is a provisional scheduling budget, NOT instructions to split/slow audio. Real voice remains one continuous line across hook cuts. Replace all estimated windows after Chốt/real voice.", "caption_intervals": "half-open [start,end); global caption layer spans cuts; no two caption segments simultaneously", "units": "seconds absolute from TikTok hook frame0; frame_estimate=round(seconds*30), never f measured", "tts_warning": "VI slices bind translation only, NOT F5 generation units. No TTS cuts except punctuation, after Chốt."}
Firstnarration.text=hook.text=FORGOT... WHAT?; titleEN, không phải VIspoken. Một linevi-b01 liên tục qua3cuts; caption/title không restart. Hookcuts0.8/2s, onset0.06s và mọiwordcue ƯỚC. Offsetreal/frame/f=null, estimatedcues/ranges ởtrườngriêng. Hitthứ2 sau3s không tínhvào0–3s.

## Geometry video — không đổi bố cục ngoài cover
Content[60,150,960,1310] khác captionzone[60,1488,960,312]. StandardRemotiontop1488/HFtop1500; reserveRemotion[70,1488,948,272]/HF[70,1500,948,272], logo[60,80,100,70]. Mọi layout_plans giữnguyên. Source: layout.ts6–8/18/48–50; SceneRenderer41–42/80–82; Caption.tsx20–22/30; captions.tpl10–13.
Cácbox/motionenvelope làallocation kếhoạch; không actualDOM/glyph. Targettitley170 vsdefault66, EN_FONT/BVP, wrapping/HFMAXW4 vàReelscaptiony1000 chưaport/QA. Khôngdropcaption haynhầm chuẩnTikTokvớiReels.

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

## Quan hệ câu / audit lặp giữ cơ sở r11.3
| Cặp | Link trong lời |
|---|---|
| S1→S2 | Không gọi tên được phầnquên→hứa có thể nhận ra chỗthiếu |
| S2→S3 | Cùng việcđọc mởthêm lifestyle/vui+học; nhịpnói cần tai, khôngcausal |
| TrongS3 | Trendcontext→“bạn có thể vừa…vừa…”: khả năngđồngtồn tại, khôngobservedparticipant |
| S3→S4 | học→Còn cách học, ranking |
| S4→S5 | lựa chọn tựkiểm→đích nhậnra chỗchưa nhớ |
| S5→S6 | Muốnbiết→Muốnbiết trảngay bằng HTB |
| S6→S7 | tựkiểm→Ví dụ đóng/kể/dò |
| S7→S8 | mởra dò→Lúc dò; giờ mới có phầnkể đểso |
| S8→S9 | chỉFood/nguồncóRent→bổsung khoản vừa sót |
| S9→S10 | khoản sót→Giảsử kểtrangriêng, đủ/thiếu |
| S10→S11 | lựa chọn đủ/thiếu→commentmột từ |
Liênkếttrên chữ không thay đọc to. XóaBEATb02 mấtđịnhphạmvi đọcvui+học; không thêmđiềukiện xóa riêngmệnhđềtrend làm method sụp.
| Cụm/ý | Giữ/bỏ/vai trò |
|---|---|
| bạn có thể | Main“bạn có thể” chỉ còn1lần b02; hookthêmvẫn→“Bạn vẫn có thể”, khôngauditwaiver choL093 |
| tựkiểm | Giữ2vai: rankingb03 vàkhuyếnnghịHTBb05 |
| thiếu | Promise→định danhRent→CTAloop, khôngbeatgiảng lại |
| đủhaythiếu/đủhoặcthiếu | Câuhỏi và1lờimời commentngaysau, khôngđếmý/từ |
| Bỏtiếp | Không quaylại tìmtrang/kểthiếuchưadiễnra, ngãba/tối–sáng/doingfail; khôngđổivật giữplot |
Polishtext-only: thay finitegram bằngcách nói đồngnghĩa, khôngđổi fact/context/method. Chưa đọc/nghe thật; khôngtựchứngnhận văn nói. Không chê năng lực/participants.

## Endcard / safety / credit/license
Ước[42.804444, 45.804444];3sreadability CHƯA KIỂM; static no voice.
- Thông tin tham khảo, không thay thế tư vấn chuyên gia
- Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
- Đã chuyển thể. Giấy phép: https://creativecommons.org/licenses/by/4.0/
- Dunlosky et al. (2013) · Trend context: Znews 05/11/2026
- Giọng của Hiệp (nhân vật) trong video là giọng AI tổng hợp (F5-TTS). ChỉbậtAI khi thực cógiọng.

## Engagement / callback
≥3kiểu: [{"type": "comment-challenge", "beat": "b07", "text": "Bình luận một chữ đủ hoặc thiếu nha.", "one_request": true}, {"type": "loop", "beat": "b07", "text": "đủ hoặc thiếu", "hook_word": "thiếu"}, {"type": "relatable-question", "beat": "b04", "text": "Bạn muốn biết chỗ nào trong trang sách chưa nhớ hông?"}]
Ghimđềxuất chưađăng: Giả sử kể lại trang vừa đọc, bạn chọn đủ hay thiếu? “Thiếu” chỉ nói phần kể so với trang sách, không đánh giá khả năng của bạn.
Một CTAcomment1từ, ENgiữgiảđịnhSay/Would; khônglike/follow. Callback04khai cùng23.14nhưng chưa biếtđăng, khôngnói cliptrước. ThemeDark/slot5releasehistory/signature cònmở.

## Gates / checks / hạn chế thật
- Đọc to/người lạ/nghe1lần/timing: CHƯA KIỂM. Không nói ai đã đọc/nghe thật; textchecks không thay cổng tai.
- Deep/Social/Reviewer chưa xem SHA r11.4. Không kếthừa verdict từ SHA cũ.
- Registry L090 lookup vẫn riêng, nguồn đã bàn giao không bị gọi là chưa nghiên cứu. Metadata/addendum/storage/archival scratch chưa sanctioned sync; không sửa ID/checker/metadata để qua máy.
- Callback/release04/theme/signature cònmở; không nói cliptrước đãđăng/đãxem. Effects-log không sửa. Không thêm nghiên cứu hay chờ việc này để cấm chuẩn bị file.
- Production schema/HFport/font/bubble/titleport/Reels/realcaption/hit/resnap/mix/frameQA chưađóng. Spec planning_only=true/renderable=false/locked=false, không đưa vào build.
- Previewgate1 CHƯA CHUẨN BỊ ẢNH. Không audio/images/render/repo edits/commit/push/messages.
- Textchecker nguyênbản: subjects/l088/trend/flow/clarity/link/repeat/evidence/choppy/fresh. Fresh lỗi khi so cùng vòngpatch được giữ nguyên, KHÔNG tự diễn giải cần rewrite; Reviewer đã xác định phạmvi patch2. Không tựPASS/xinChốt.
- Output: /workspace/clip05-r11.4-checker-output-2026-11-07.txt; numeric: /workspace/clip05-r11.4-local-validation-2026-11-07.json; manifest: /workspace/clip05-r11.4-delivery-manifest-2026-11-07.json. Không --final/STT/build/productionvalidator.

