---
id: clip-05.motion-spec-v23
type: motion-spec
status: draft
updated: 2026-11-19
tags: [clip-05, motion, visual-plan, v23, howtolivebetter-23.14, motion-picks-per-script]
title: "Clip 05 v23: kịch bản dựng hình + motion theo từng beat"
script: content/clips/clip-05-hoc-mot-dem/final/script-v23-LOCKED.md
skill: skills/motion-picks-per-script
---

# Clip 05 v23: kịch bản dựng hình + motion

Lời: bản Hiệp **Chốt 19/11/2026** (`final/script-v23-LOCKED.md`). File này chỉ là **kế hoạch hình và motion**. Chưa làm giọng, chưa vẽ, chưa render. Giây là **ƯỚC** theo nhịp đọc 4,5 âm tiết/giây; sau khi có giọng F5 thật thì snap lại theo `timing.json` (L-099).

## 0. Khung chung (áp cho cả clip)

| Mục | Quy định | Căn cứ |
|---|---|---|
| Khung | 1080×1920, 9:16 | brand-tokens `video` |
| Format | Comic + motion graphics. Hiệp chibi (rig `brand/characters/`) là người kể duy nhất. Không quay thật, không b-roll, không ảnh AI người thật | DL-027, rule-11 (tuần 1, không Omi) |
| Nền | Bàn học/bàn làm việc sáng, theme **light**: bg `#F7F7F5`, surface `#FFFFFF`, ink `#111111`, muted `#6B6B6B` | brand-tokens `colors.light` |
| Hai màu so sánh xuyên suốt | **Đọc lại** = muted `#6B6B6B` (xám). **Tự viết** = momentum `#B45309` (cam đất). Giữ đúng hai màu này từ b01b tới b07 để người xem không phải học lại mã màu | brand-tokens; awesome-ai-motion `step-recap.avoid` (không đổi màu giữa chừng) |
| Font | Be Vietnam Pro cho mọi chữ trên hình | brand-tokens `fonts` |
| Caption EN | Lớp cố định, plate theo brand (`caption.plate`, bottomOffset 420), chunk 3–5 từ, từ đang nói ink 700 + gạch chân. Không tính là effect | brand-tokens `caption`, rule caption |
| Vùng an toàn | Mọi prop, chữ, biểu đồ, doodle nằm **y ≤ 1400**, không lọt dải caption | L-038, doodle rules |
| Prop | Chỉ vật đời thường: sách bìa trơn (không tên môn), tờ giấy, bút, đồng hồ, lịch, điện thoại. Hai bài thí nghiệm vẽ là tờ giấy có icon mặt trời / rái cá, không chữ môn học | L-087 |
| Luật craft | Một effect chính mỗi shot, tối đa một điểm nhấn. Vào thì giảm tốc, ra thì tăng tốc. Gần như không fade cảnh, nối cảnh bằng cut. Cả clip chỉ một spring nhìn thấy được (ở CTA). Chữ trên hình ≥ 1 s. Không chớp sáng, không glitch, không texture | motionmaxxing laws, route shorts |
| SFX | Chỉ trong `SFX_OK` (pop, ding, whoosh, tick, click, whoosh-soft, swish, ambience, snap, pen, stamp, rise). Nền `ambience` cả clip | check-rules `SFX_OK` |
| Khác clip-04 | Clip-04 đã dùng `mmx-cut-on-motion` ở hook, `tdev-panel` cho thẻ nghiên cứu, `tdev-stagger`, và **cột đổi chỗ bằng `mmx-snap-settle`** cho cùng thí nghiệm. Clip-05 tránh cả bốn: hook dùng `mmx-crash-in`, thẻ nguồn dùng `tdev-modal`, số liệu dùng **đường kẻ giao nhau** (`line-draw`), ba bước dùng `tdev-page` | logs/effects-log.md, make-video §5 |

## 1. Bảng dựng hình từng shot

Cột «Effect» ghi slug + nguồn. «Mốc» là chữ trong lời mà motion phải rơi đúng vào.

| Shot | ƯỚC (s) | Lời (rút gọn) | Ý định | Hình (context) | Effect chính | Thông số | Điểm nhấn (≤1) | Mốc | SFX |
|---|---|---|---|---|---|---|---|---|---|
| **b01a** Hook | 0.0–6.5 | «Nếu bạn muốn nhớ lâu mà cứ ngồi đọc đi đọc lại, thì bạn đang chọn cách nhớ kém hiệu quả hơn rồi đó.» | 주목 끌기 (câu phán) | Frame 0 đã có hình, không màn trắng: Hiệp chibi ngồi trước cuốn sách mở, mắt đảo qua lại (rig loop «đọc»), số «×3» nhỏ cạnh sách. Tới «kém hiệu quả hơn»: Hiệp ngẩng lên nhìn thẳng camera, chữ VI **«KÉM HIỆU QUẢ HƠN»** đập vào giữa khung trên (y ≈ 520) | `mmx-crash-in` (motionmaxxing) cho chữ «KÉM HIỆU QUẢ HƠN» | từ scale ~3.5× về 1.0, 10–12 f, punch qua rồi settle; chữ ink 800, plate trắng `hard-shadow` 6 px | — | «kém hiệu quả hơn» | `stamp` frame chữ chạm |
| **b01b** Hook | 6.5–15.0 | «Đọc lại chỉ giúp… mấy phút đầu… còn để qua vài ngày thì những người tự viết ra… nhớ được nhiều hơn bạn.» | 비교 | Chia đôi khung: trái sách mở (xám, nhãn «Đọc lại»), phải tờ giấy + bút đang viết (cam, nhãn «Tự viết ra»). Trên đầu mỗi bên một đồng hồ nhỏ. «Mấy phút đầu»: bên trái sáng hơn một chút. «Vài ngày»: lịch lật 2 tờ, bên phải sáng lên, bên trái mờ 3 px | `split-compare` (awesome-ai-motion) | đường chia 50% → 35% (ở «mấy phút đầu», nghiêng về trái) → 65% (ở «vài ngày», nghiêng về phải) → 50% giữ; mỗi đoạn 0,6–0,65 s, ease power2.inOut; đường chia đứng yên ở cuối shot | `tdev-icon-swap` (transitions.dev): icon đồng hồ → lịch ở «vài ngày» | «mấy phút đầu», «vài ngày» | `whoosh-soft` khi đường chia chạy |
| **b02** Vấn đề | 15.0–27.0 | «Nghe hơi ngược đời ha… đọc tới hai ba lượt cho chắc, vậy mà vài bữa sau… lờ mờ vài ý, uổng công dễ sợ.» | 분위기 (nỗi đau) | Cut cứng. Hiệp đọc sách, ngón tay đếm 1-2-3 lượt (đồng hồ góc chạy). Cut: Hiệp đứng trước bạn đồng nghiệp chibi (không mặt, không tên), bong bóng thoại của Hiệp có 4 dòng chữ đang **mờ dần** thành vệt xám, chỉ còn 1 dòng đọc được. «Uổng công dễ sợ»: Hiệp xụ vai, gục đầu nhẹ | `mmx-soft-inout` (motionmaxxing) cho chữ trong bong bóng mờ dần | blur 0 → 6 px + opacity 1 → 0,35 trong 1,2 s, bắt đầu ở «vài bữa sau», xong trước «lờ mờ»; còn đúng 1 dòng rõ | `tdev-shake` (transitions.dev) cho Hiệp ở «uổng công dễ sợ» | «lờ mờ», «uổng công» | `tick` ×3 khi đếm lượt |
| **b03a** Dẫn chứng: nguồn | 27.0–33.5 | «Mà chuyện này năm 2006 có hai nhà tâm lý học là Roediger và Karpicke đem ra làm thí nghiệm rồi.» | 설명 (nguồn) | Thẻ nguồn trắng hiện trên bàn: «Roediger & Karpicke · 2006 · Thí nghiệm 1». Hiệp đứng cạnh chỉ tay vào thẻ | `tdev-modal` (transitions.dev) | scale 0.96 → 1 + opacity, 0,4 s; giữ ≥ 3 s | — | «Roediger và Karpicke» | `pop` nhỏ |
| **b03b** Dẫn chứng: hai cách học | 33.5–51.0 | «Họ cho một trăm hai mươi sinh viên học hai bài ngắn, một bài về mặt trời, một bài về rái cá biển, mỗi lượt học bảy phút… Bài thứ nhất… đọc lại… Bài thứ hai… gấp lại, tự viết ra… không có ai chấm hay sửa giùm.» | 설명 + 순서·흐름 | Vẽ dần ngay trên bàn (thấy được quá trình): (1) một sinh viên chibi không mặt + nhãn «120 sinh viên»; (2) hai tờ giấy nhỏ, icon mặt trời và rái cá + đồng hồ «7 phút/lượt»; (3) ở «Bài thứ nhất»: mũi tên xám tới tờ 1, tờ mở ra, nhãn «Bài 1: đọc lại»; (4) ở «Bài thứ hai»: mũi tên cam tới tờ 2, tờ úp xuống, bút viết lên giấy trắng, nhãn «Bài 2: gấp lại, tự viết»; (5) «không ai chấm»: dấu ✕ nhỏ lên icon cây bút đỏ chấm bài | `doodle-drawing` (anidoodle, Remotion port) | nhiều nét, mỗi cụm vẽ 0,5–0,8 s rơi đúng chữ; seed cố định theo cue; nét ink, mũi tên theo hai màu so sánh; khung y + h ≤ 1400 | `doodle-cross` lên icon «bút chấm» ở «không có ai chấm» | «một bài về mặt trời», «Bài thứ nhất», «Bài thứ hai», «chấm hay sửa» | `pen` khi nét vẽ |
| **b03c** Dẫn chứng: ba nhóm | 51.0–59.5 | «Sau đó họ kiểm tra… còn nhớ được bao nhiêu phần trăm số ý. Họ chia ra ba nhóm… nhóm thì sau năm phút, nhóm sau hai ngày, nhóm sau một tuần.» | 순서·흐름 | Khung tách thành ba cột, mỗi cột một nhóm 3 sinh viên chibi không mặt + nhãn mốc: «5 phút», «2 ngày», «1 tuần». Dòng nhỏ dưới: «Mỗi mốc là một nhóm khác nhau» | `clock-wipe` (awesome-ai-motion) để mở lần lượt ba cột | mỗi cột một vòng 0,6 s, linear, tâm đặt ngoài nhân vật; cột mở đúng chữ mốc | — | «năm phút», «hai ngày», «một tuần» | `tick` mỗi cột |
| **b04a** Kết quả: 5 phút | 59.5–68.0 | «Nhóm kiểm tra sau năm phút nhớ được tám mươi mốt phần trăm… bảy mươi lăm… đọc lại nhỉnh hơn một chút thiệt.» | 데이터 증명 | Biểu đồ đường, trục ngang 3 mốc (5 phút · 2 ngày · 1 tuần), trục dọc «% số ý nhớ đúng (trung bình)». Ở mốc 5 phút hiện hai điểm: xám 81 (cao hơn), cam 75 | `count-up` (awesome-ai-motion) cho hai nhãn 81 và 75 | 0 → giá trị trong 1,0 s, ease power2.out, giữ ≥ 0,5 s; nhãn bám điểm | — | «tám mươi mốt», «bảy mươi lăm» | `tick` nhẹ |
| **b04b** Kết quả: lật ngược | 68.0–78.5 | «Nhưng tới nhóm hai ngày thì lật ngược lại: … năm mươi bốn… sáu mươi tám. Còn nhóm một tuần… bốn mươi hai… năm mươi sáu.» | 데이터 증명 + 비교 | Hai đường kẻ dần từ mốc 5 phút sang 2 ngày và **cắt nhau** (xám đi xuống 54, cam xuống ít hơn, 68), rồi kéo tiếp tới 1 tuần (42 / 56). Giống dạng hình 1 trong bài báo (hai đường giao nhau) | `line-draw` (awesome-ai-motion) | mỗi đoạn 1,2–1,6 s, linear, chấm đầu đường 8 px; đoạn 1 chạy trên «lật ngược lại», đoạn 2 trên «một tuần»; giữ hình cuối ≥ 1 s; nhãn số luôn hiện cạnh đầu đường (line-chart-race.avoid: không giấu nhãn khi giao nhau) | `doodle-circle` khoanh chỗ hai đường cắt nhau, rơi đúng «lật ngược lại» | «lật ngược lại», «năm mươi sáu» | `swish` khi giao nhau |
| **b04c** Giới hạn | 78.5–85.0 | «Có điều thí nghiệm này chỉ làm với mấy bài ngắn kiểu đó, nên chưa nói được hết chuyện nhớ trong đời sống hằng ngày.» | 설명 (giới hạn) | Biểu đồ thu nhỏ lên góc trên trái, thẻ chữ giới hạn trượt vào bên dưới: «Chỉ đo bài đọc ngắn · không đo đời sống hằng ngày» | `mmx-soft-land` (motionmaxxing) cho thẻ giới hạn | trượt lên 24 px + opacity, 0,45 s; chữ đọc được ≥ 2 s; biểu đồ thu bằng `mmx-glide` | — | «chỉ làm với mấy bài ngắn» | không |
| **b05** Mục tiêu | 85.0–92.0 | «Vậy nên cái bạn cần nhắm tới là: … vài ngày sau vẫn tự nói lại được ý chính, khỏi phải mở ra coi.» | 강조 + 비교 (đổi mục tiêu) | Tấm bảng nhỏ trên bàn có dòng «Đọc cho đủ 3 lượt». Gạch ngang dòng đó, dòng mới hiện dưới: **«Vài ngày sau vẫn tự nói lại được»**. Hiệp gật đầu, sách gấp lại trong tay | `strikethrough-replace` (awesome-ai-motion) | gạch 0,35 s trái → phải, nghỉ 0,1 s, dòng mới lên 12 px trong 0,25 s; dòng cũ giữ opacity 0,45 | — | «cần nhắm tới», «tự nói lại được» | `pen` lúc gạch |
| **b06a** Cách làm: ba bước | 92.0–100.5 | «Cuốn Cẩm nang sống đáng giá hướng dẫn cách làm gọn lắm: học xong thì gấp sách lại, tự kiểm một lần, rồi mới mở ra so lại.» | 순서·흐름 | Thẻ nhỏ «Cẩm nang sống đáng giá · 23.14» góc trên. Ba thẻ bước lật lần lượt như trang: ① sách gấp, ② tờ giấy + bút, ③ sách mở cạnh tờ giấy | `tdev-page` (transitions.dev) cho từng thẻ bước | mỗi thẻ 0,45 s, vào từ phải; thẻ trước lùi nhẹ; ba thẻ cùng ở lại thành hàng khi hết câu | — | «gấp sách lại», «tự kiểm một lần», «so lại» | `click` mỗi thẻ |
| **b06b** Cách làm: làm thật | 100.5–111.5 | «Cụ thể là bạn lấy một tờ giấy, viết ra hết những ý còn nhớ, viết sai cũng được, miễn là đừng lật sách. Viết xong rồi mới mở sách ra so, ý nào sót hay ghi sai thì khoanh lại, lần sau đọc kỹ đúng mấy chỗ đó thôi.» | 설명 | Cận cảnh bàn (góc từ trên xuống): tay chibi viết 4 dòng nguệch ngoạc lên giấy, tay kia đè lên sách đóng (ở «đừng lật sách»). Sách mở ra cạnh giấy, đối chiếu: 2 chỗ trên giấy được khoanh | `doodle-circle` (anidoodle) ×2 trên tờ giấy | mỗi vòng 0,5 s, seed cố định, nét cam; rơi đúng «khoanh lại» | — | «đừng lật sách», «khoanh lại» | `pen` |
| **b06c** Lời khuyên vs thí nghiệm | 111.5–116.0 | «Bước so lại này là lời khuyên của cẩm nang, còn thí nghiệm hồi nãy chưa thử tới bước đó.» | 설명 (phân biệt nguồn) | Thẻ bước ③ phóng nhẹ lên giữa, gắn nhãn dán: «Lời khuyên của cẩm nang · thí nghiệm chưa thử» | `tdev-badge` (transitions.dev) cho nhãn dán | 0,5 s; nhãn nằm trên thẻ ③, giữ ≥ 2 s | — | «lời khuyên của cẩm nang» | `pop` |
| **b06d** Không tốn thêm giờ | 116.0–120.0 | «Mà cũng đâu có tốn thêm giờ, lượt đọc lại thứ hai bạn đổi thành lượt tự viết là được.» | 비교 | Hai ô thời gian xếp hàng «Lượt 1: đọc · 7'» và «Lượt 2: đọc lại · 7'». Ô 2 đổi thành «Lượt 2: tự viết · 7'», icon mắt đổi thành bút; tổng thời gian giữ nguyên | `tdev-text-swap` (transitions.dev) cho nhãn ô 2 | 0,3 s; rơi đúng «đổi thành lượt tự viết» | `tdev-icon-swap`: mắt → bút cùng lúc | «đổi thành» | `snap` |
| **b06e** Hơi khó chịu | 120.0–123.5 | «Lúc viết bạn sẽ thấy hơi khó chịu, vì thấy rõ mình quên chỗ nào, chuyện đó bình thường thôi.» | 분위기 | Hiệp nhăn mặt nhìn tờ giấy còn chỗ trống, rồi thở ra, gật đầu nhẹ | `mmx-no-dead-frame` (motionmaxxing) | giữ khung với scale creep 1,00 → 1,02 suốt shot, không cắt | — | «bình thường thôi» | không |
| **b07** Kết quả | 123.5–133.5 | «Làm vậy thì bạn khỏi phải đoán mình đã thuộc tới đâu, vì nhìn tờ giấy là biết liền. Lần sau bạn chỉ cần đọc lại đúng mấy ý hay quên, chứ không phải đọc lại cả bài rồi vẫn lờ mờ như trước.» | 강조 (khép vòng b02) | Quay về khung b02: Hiệp trước đồng nghiệp, nhưng lần này cầm tờ giấy có 2 chỗ khoanh. Camera đẩy vào tờ giấy, 2 chỗ khoanh rõ. Bong bóng thoại của Hiệp lần này chữ rõ, không mờ | `push-in` (awesome-ai-motion) vào tờ giấy | scale 1,0 → 1,4 trong 1,8 s, ease power1.inOut, tâm là 2 chỗ khoanh; giữ ≥ 0,5 s | — | «nhìn tờ giấy là biết liền», «lờ mờ» | không |
| **b08** CTA | 133.5–142.0 | «Giờ bạn thử luôn với chính clip này đi: úp điện thoại xuống, lấy giấy viết ra mấy ý vừa nghe, rồi comment cái ý bạn nhớ rõ nhất cho mình coi nha.» | 브랜딩 / CTA | Hiệp cầm điện thoại, úp xuống bàn (rig), đẩy tờ giấy trắng về phía camera. Ô comment nhỏ bật ra cạnh tờ giấy với chữ «Ý bạn nhớ rõ nhất là…» | `mmx-pop-over` (motionmaxxing), **spring duy nhất của clip**, cho ô comment | peak 1,08 tại t 0,72, tổng 0,5 s; ô comment ở y ≤ 1400 | — | «comment cái ý bạn nhớ rõ nhất» | `pop` |
| **End** End card | 142.0–150.0 | «Thông tin tham khảo, không thay thế tư vấn chuyên gia.» | 브랜딩 | Thẻ cuối nền sáng: câu an toàn (to nhất) · credit «Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/» · nguồn «Roediger, H. L., & Karpicke, J. D. (2006). Psychological Science, 17(3), 249–255. doi:10.1111/j.1467-9280.2006.01693.x» · «Không có sự bảo trợ của tác giả cẩm nang hay tác giả nghiên cứu» | `mmx-soft-land` (motionmaxxing) cho các dòng | lên 16 px + opacity, 0,45 s, lệch 80 ms giữa các dòng; giữ tới hết; credit cỡ chữ đọc được trên điện thoại | — | — | `ambience` tắt dần |

**Nối cảnh:** các shot nối bằng cut thẳng. Chỗ đổi bối cảnh lớn (b01b → b02, b03c → b04a, b05 → b06a, b06e → b07) cắt trên chuyển động: shot sau đã đang chạy ở frame đầu, không fade (luật craft motionmaxxing). Clip-04 đã dùng preset `mmx-cut-on-motion` như một effect ở hook, nên clip này chỉ áp như luật nối cảnh, không làm điểm nhấn.

## 2. Chữ trên màn hình theo shot

| Shot | Chữ VI trên hình (ngoài caption EN) | Thời gian hiện tối thiểu |
|---|---|---|
| b01a | **KÉM HIỆU QUẢ HƠN** | ≥ 2 s |
| b01b | Đọc lại · Tự viết ra | cả shot |
| b02 | (bong bóng chữ mờ, chỉ 1 dòng đọc được) | — |
| b03a | Roediger & Karpicke · 2006 · Thí nghiệm 1 | ≥ 3 s |
| b03b | 120 sinh viên · 7 phút/lượt · Bài 1: đọc lại · Bài 2: gấp lại, tự viết | mỗi nhãn ≥ 1,5 s |
| b03c | 5 phút · 2 ngày · 1 tuần · Mỗi mốc là một nhóm khác nhau | cả shot |
| b04a–b | % số ý nhớ đúng (trung bình) · 81 / 75 · 54 / 68 · 42 / 56 | tới hết b04b |
| b04c | Chỉ đo bài đọc ngắn · không đo đời sống hằng ngày | ≥ 2 s |
| b05 | ~~Đọc cho đủ 3 lượt~~ → Vài ngày sau vẫn tự nói lại được | ≥ 2 s |
| b06a | Cẩm nang sống đáng giá · 23.14 · ① Gấp sách ② Tự viết một lần ③ Mở ra so lại | cả shot |
| b06c | Lời khuyên của cẩm nang · thí nghiệm chưa thử | ≥ 2 s |
| b06d | Lượt 1: đọc · 7' · Lượt 2: ~~đọc lại~~ tự viết · 7' | ≥ 1,5 s |
| b08 | Ý bạn nhớ rõ nhất là…? | ≥ 2 s |
| End | xem bảng ở mục 1 | tới hết |

## 3. Soát trước khi giao (motion-picks-per-script bước 7)

| Kiểm | Kết quả trên kế hoạch |
|---|---|
| Một effect chính mỗi shot, tối đa một điểm nhấn | Đạt (b01b, b02, b03b, b04b, b06d mỗi shot có 1 điểm nhấn) |
| Chỉ một spring nhìn thấy được | Đạt: `mmx-pop-over` ở b08 |
| Không fade cảnh, không chớp, không glitch hay texture | Đạt |
| Chữ trên hình ≥ 1 s | Đạt theo mục 2 |
| Mọi thứ y ≤ 1400 | Ghi trong từng shot; kiểm lại trên frame thật sau render |
| Không prop môn học (L-087) | Đạt: hai bài vẽ bằng icon mặt trời / rái cá, sách bìa trơn |
| Số liệu đúng fact lock, nói kèm mốc 5 phút, không «+14%» | Đạt: b04a hiện 81/75 trước, nhãn «% số ý nhớ đúng (trung bình)» |
| Hình không gán bài mặt trời = đọc lại | Đạt: nhãn là «Bài 1 / Bài 2», icon chỉ để phân biệt hai tờ (thí nghiệm hoán đổi, lock RK §3) |
| Biểu đồ đường nối ba nhóm khác nhau | Chú ý: đường nối giữa các mốc là cách bài báo vẽ (hình 1), nhưng có thể khiến người xem tưởng cùng một nhóm. Đã bù bằng nhãn «Mỗi mốc là một nhóm khác nhau» ở b03c và lời «tới nhóm hai ngày / còn nhóm một tuần» |
| Không trùng signature clip-04 | Đạt (xem mục 0, dòng «Khác clip-04») |
| Giấy phép | awesome-ai-motion MIT; transitions.dev (free, dùng thương mại + sửa OK); motionmaxxing Apache-2.0; anidoodle Apache-2.0 |
| Brand | Màu, font, plate caption lấy từ `brand/brand-tokens.json` |

## 4. Việc sau khi Hiệp duyệt kế hoạch này

1. Viết `spec.json` mới cho v23 từ lời đã khóa + bảng trên (make-video §2). `final/spec.json` hiện là bản v4, chưa đụng tới.
2. Làm giọng F5 · Thái Sơn theo markup trong script, đo `timing.json`, snap lại mọi mốc ở mục 1.
3. Render, chạy `check-rules.py --final`, xem lại 2 vòng (rule-34), gate 2.
