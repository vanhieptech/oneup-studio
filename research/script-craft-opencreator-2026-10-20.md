---
title: "Nghiên cứu viết script TikTok — phần bổ sung của OpenCreator (20/10/2026)"
date: 2026-10-20
type: research
status: draft
source: "web + repo mở (đọc, không cài/chạy) + dữ liệu Apify đã có trong repo (16–20/10/2026, không chạy scrape mới)"
builds_on: research/tiktok-script-craft-2026-10-20.md (Deep Research) · research/script-craft-2026-10-20.md (Rule Reviewer) · docs/research/scriptwriting-research-2026-10-15.md · docs/research/script-prompt-principles.md
---

# Viết script TikTok — phần bổ sung (OpenCreator)

Hai file của Deep Research và Rule Reviewer đã có: hook trong 3 giây, khung hook → đẩy → trả lời → 1 CTA, nối bằng «nhưng/nên», 6–10 hook rồi chọn, mỗi ý một ví dụ, hứa sớm, móc lại giữa clip, đọc to rồi cắt ~20%. File này **không nhắc lại** những điểm đó, chỉ thêm 6 phần mới: (1) tốc độ nói đo thật, (2) viết cho tai nghe, (3) cách nhắc nghiên cứu khi nói, (4) mẫu prompt và vòng tự chấm, (5) lời thật của creator Việt, (6) các luật rút ra cho @hi.oneup, kèm ví dụ câu sai và câu đúng.

## 1. Tốc độ nói → ngân sách chữ (số đo, không đoán)

| Nguồn | Số đo | Ghi chú |
|---|---|---|
| Coupé và cs. 2019, *Science Advances* (EurekAlert: https://www.eurekalert.org/news-releases/763747 ; HKU: https://e3.eurekalert.org/news-releases/887122) | Tiếng Việt khoảng **5,3 âm tiết/giây** (Worldcrunch ghi 5,25: https://worldcrunch.com/culture-society/syllable-counting-and-the-secret-to-the-39speed39-of-languages/) | Đây là tốc độ **đọc** văn bản ngắn, không phải nói chuyện. Tiếng Việt mang khoảng 8 bit/âm tiết, cao nhất trong 17 ngôn ngữ, nên mỗi chữ chở nhiều thông tin. Hệ quả: câu ít chữ vẫn đủ ý, không cần độn chữ. |
| Giọng F5 của mình, v16c (`final/prosody-measure-v16c.md`) | 204 chữ: **45,5s nói thuần (≈4,48 chữ/s)**, cộng 9,5s nghỉ ra **55,3s giọng** (≈3,69 chữ/s tính cả nghỉ) | Đây là số dùng để lập kế hoạch. Một chữ tiếng Việt là một âm tiết. |
| VTT của creator Việt (Apify 16–20/10, `research/trends/*/apify/vtt/`, mình tự tính số chữ ÷ thời gian từ cue đầu đến cue cuối) | Clip nói thẳng vào camera: **~3,4–5,3 chữ/s**. Ví dụ @sabito_0668 4,54 · @biquyetdodaihoc 4,84 · @gonaox 4,24 · @_maingocduong_ 5,31 · @truecraft.coffee 4,20 | F5 speed 1.0 của mình (3,69 chữ/s tính cả nghỉ) nằm trong khoảng của người thật, hơi về phía chậm. Không cần đọc nhanh thêm (L-074). |

**Ngân sách:** 150 chữ ≈ 33,5s nói + ~7–8s nghỉ ≈ **41–42s giọng**. 160 chữ ≈ **44–45s**. 170 chữ ≈ **47–48s**. Cộng 2s end card. Vì vậy 140–160 chữ cho ra clip 43–47s, khớp con số của Deep Research và W-14.

## 2. Viết cho tai nghe (nguồn tin phát thanh, dạy viết lời đọc)

- **Mỗi câu một ý, thứ tự ai → làm gì → kết quả, câu chủ động.** WBA Newsroom: «The ear is trained to hear sentences written in subject-verb-object form» (https://www.wbanewsroom.org/newsroom-tips/tips-for-radio-news-writers/). UF/IFAS: câu ≤ 20 từ để người đọc còn lấy hơi (https://ask.ifas.ufl.edu/publication/WC193). Điểm này **trùng luật W-09 của Hiệp** (câu đủ chủ ngữ). Nguồn phát thanh có chấp nhận câu cụt «nếu vẫn rõ nghĩa», nhưng **luật của Hiệp thắng**.
- **Người nghe chỉ nghe được một lần.** DINFOS Broadcast Writing Style Guide: «understand your copy the first time they hear it», mỗi câu một ý chính, cẩn thận với đại từ mơ hồ «it/that/they» (https://www.dinfos.dma.mil/Portals/66/Documents/Academics/BOMD/2015%20DINFOS%20Broadcast%20Writing%20Style%20Guide.pdf). Với mình: «nó», «cái đó», «phần đó» đứng một mình là lỗi, giống L-063.
- **Số làm tròn, chức danh đặt trước tên, ít dấu hai chấm.** Media Helping Media: «nearly two thousand people» thay cho «1,988»; «Give titles before names»; chỉ dùng phẩy và chấm, tránh hai chấm và chấm phẩy (https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/). Với mình: nói «hơn hai trăm nghiên cứu» dễ nghe hơn «222». Nhưng fact lock đang khóa con số 222, nên muốn làm tròn phải hỏi Deep Research. Nói «nhóm nghiên cứu của Yang» rõ hơn «Yang» trơ, vì F5/STT đã nghe «Yang» thành «Giang» (`prosody-measure-v16c.md` s09). Dấu «:» trong lời làm F5 ngắt kiểu đọc bài.
- **Kiểm bằng cách đọc to.** Media Helping Media nói vậy, và các nguồn trong file Deep Research cũng nói vậy. Không nhắc lại thêm.

## 3. Nhắc nghiên cứu khi nói mà không khô

- **Truyện dễ hiểu và dễ nhớ hơn văn giải thích.** Mar và cs. 2021, *Psychonomic Bulletin & Review* 28(3):732–749, gộp 37 bài với 33.078 người tham gia: văn kể chuyện được hiểu và nhớ tốt hơn văn giải thích, g ≈ 0,55 (https://doi.org/10.3758/s13423-020-01853-1). Hệ quả: fact nên đặt **trong** chuyện, làm câu trả lời cho chỗ nhân vật khựng, không đứng riêng thành đoạn giảng. Ý này khớp L-060.
- **Kết quả trước, chi tiết sau, nói kèm giới hạn.** Northeastern, dẫn bộ công cụ AAAS: công chúng cần «key findings first, then the "So what?"» (https://graduate.northeastern.edu/knowledge-hub/tips-for-effective-science-communication/). Không dùng «chứng minh», chỉ nói «thấy»/«cho thấy», kèm mức độ («ở mức vừa»). Nguồn: bài của nhà khoa học K. Spaulding (LinkedIn, ý kiến cá nhân, không phải nghiên cứu): https://www.linkedin.com/posts/kristina-spaulding-phd-caab-91028282_proven-is-one-of-those-words-that-makes-activity-7512108263816204288-hPxr
- **Khuôn một câu cho mình:** [ai] + [làm gì, cỡ nào] + [thấy gì] + [mức], tối đa ~25 chữ (W-12). Ví dụ: «Nhóm của Yang gộp 222 nghiên cứu, thấy lớp có làm kiểm tra nhỏ thì điểm cao hơn, ở mức vừa.» (21 chữ, đúng fact lock nếu giữ nhóm so sánh, xem phần 7.)

## 4. Mẫu prompt và vòng tự chấm cho LLM viết script

| Nguồn | Điều rút ra |
|---|---|
| Anthropic, Prompting best practices (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Dùng **3–5 ví dụ mẫu** sát việc thật và khác nhau, mỗi ví dụ bọc trong thẻ `<example>`. Tách hướng dẫn, ngữ cảnh, ví dụ và đầu vào bằng thẻ XML. Chuỗi hay dùng nhất là **viết nháp → chấm theo tiêu chí → sửa theo bản chấm**, mỗi bước là một lần gọi riêng để xem được kết quả giữa chừng. |
| Self-Refine, Madaan và cs., NeurIPS 2023 (https://arxiv.org/abs/2303.17651 ; code https://github.com/madaan/self-refine) | Vòng viết → góp ý cụ thể, làm được → sửa, lặp tới khi đạt điều kiện dừng. Không cần huấn luyện thêm. Góp ý phải **làm được** (chỉ dòng, nói cách sửa), không phải lời khen chê chung. |
| AnastasiyaW, script-evaluator SKILL.md (https://github.com/AnastasiyaW/claude-code-config/blob/main/skills/video-production/script-evaluator/SKILL.md) | 6 trục chấm 1–10: căng thẳng, cụ thể, đường cảm xúc (ít nhất một chỗ xuống và một chỗ lên), hook, giọng người thật, đa dạng hình. **Sửa trục yếu nhất trước**: tổng điểm cao mà có một trục 2 điểm thì video vẫn hỏng. **Giữ fact trước khi chấm văn**: không bịa số để lên điểm. Có 5 kiểu clip phẳng; với mình có hai kiểu đáng chú ý: «Missing Middle» (đoạn giữa phẳng) và «Uniform Energy» (năng lượng đều từ đầu đến cuối). |
| shiyan521, short-video-script-sop, hook-formulas.md (MIT, https://github.com/shiyan521/short-video-script-sop/blob/main/references/hook-formulas.md) | 5 công thức hook xoay vòng: kết luận ngược trực giác, con số sốc, cảnh hồi hộp, câu hỏi, đối lập. Câu hỏi hook **không được rộng và không được hỏi có/không**. Hai vạch đỏ đáng chú ý: «không có 2 câu liền nhau không thêm thông tin»; «cấm câu tự hỏi tự đáp kiểu "bạn tưởng X? thật ra Y"» (khó nói tự nhiên). Phép thử: **xóa một câu mà người nghe vẫn hiểu thì câu đó phải xóa**. |
| vyralcontent hooks.md (MIT, https://github.com/vyralcontent/content-skills/blob/main/skills/viral-short-form/references/hooks.md) | 10 kiểu hook đã có trong file Deep Research. Phần mới: hook nên **đứng được cả khi tắt tiếng lẫn khi nghe**, lời nói đầu và caption đầu cùng một lời hứa. Phép thử «người lạ» trùng L-064. |
| ops120, video-recap-skills-plus review.py (https://github.com/ops120/video-recap-skills-plus/blob/main/skills/video-script/scripts/review.py) | Bộ chấm (LLM làm giám khảo) tách **lỗi chặn** (bịa, câu chưa trọn) khỏi **lỗi tay nghề** (hook yếu, thiếu mạch chính, «narrating the picture» tức lời tả lại hình, sáo rỗng, câu viết không cho tai). Bản chấm trả ra «retention_risk_points» (giây, rủi ro, cách sửa) và «spoken_language_rewrites». Mẫu này đáng chép. |
| krillinai/OpenCreator (Apache-2.0), `apps/daemon/src/creator/short-video-script/executor.ts` (hàm `scriptPrompt`) và `apps/daemon/src/creator/templates/short-video-script.ts`, nhánh master đọc ngày 20/10 (https://github.com/krillinai/OpenCreator) | Prompt viết script của OpenCreator **rất mỏng**: một lần gọi, trả JSON {hook, segments, cta} có thời lượng từng đoạn, sai số thời lượng có giới hạn. Luật chính chỉ có: hook nhanh vào chủ đề, CTA không ép bán, lời đọc lên được, **không bịa fact, trải nghiệm, số liệu hay trích dẫn**. Không có ví dụ mẫu, không có bước chấm. Nên lấy cấu trúc JSON có giây từng đoạn và luật cấm bịa, còn phần tay nghề phải tự xây (file `script-writer-prompt.md`). |

## 5. Lời thật của creator Việt (chỉ trích phần đã thu)

Nguồn là phụ đề VTT và caption do Apify thu ngày 16–20/10/2026, đã nằm trong repo. **Không chạy scrape mới.** Số view là số thô lúc thu.

| Clip | Số liệu lúc thu | Câu mở (phụ đề máy, nguyên văn, có lỗi chính tả của máy) | Bài học |
|---|---|---|---|
| @sabito_0668 https://www.tiktok.com/@sabito_0668/video/7670995147995237640 | 606.000 view · 68.800 like (20/10) | «phải thức khuya thì thức thôi nhưng để ý cơ thể một tí … để mình chia sẻ cách giảm tối đa tác hại của nó lưu lại nhé mình chia làm ba giai đoạn» | Mở bằng cách **chấp nhận hoàn cảnh của người xem** (không chê) rồi «nhưng», hứa cụ thể ngay (giảm tác hại, 3 giai đoạn), xin lưu sớm. Giọng mềm, không ra lệnh, rất gần ý L-073. |
| @biquyetdodaihoc https://www.tiktok.com/@biquyetdodaihoc/video/7620113093401627924 | 110.800 view (18/10) | «lười học quá bây giờ làm sao anh …» | Mở bằng **đúng câu người học hay nói** (nỗi đau nói bằng lời của họ). Phần sau thì quát mắng: không hợp kênh (P-07). |
| @camreadwonder https://www.tiktok.com/@camreadwonder/video/7614813783201975573 | 287.700 view · 32.800 like (20/10) | Caption: «Em học em không nhớ thì làm sao hả chị?», rồi «con người ta sẽ quên khoảng hơn 70% những gì mình học được trong 24h» | Hook là câu hỏi người học tự hỏi. **Con số 70%/24h không có nguồn trong clip**: không được chép sang mình (L-056, chưa kiểm chứng). |
| @gonaox https://www.tiktok.com/@gonaox/video/7694997202954915079 | 331.700 view (16/10) | «7 thói quen học tập của học sinh giỏi nhất lớp tôi đã dành ba tháng quan sát … bí quyết nằm ở 7 thói quen nhỏ mà 95% học sinh không biết» | Hook dạng danh sách + bằng chứng kiểu tự kể chuyện. «95%» **không có nguồn**: là kiểu số bịa phải tránh. |
| @hoc.di.roi.biet https://www.tiktok.com/@hoc.di.roi.biet/video/7695270625660652820 | 390.700 view (20/10) | «Xin lỗi mọi người nhá … mình sẽ xóa video này sau 24 tiếng …» | Hook kiểu giấu bí mật, dọa gỡ video, nói 6,27 chữ/s. Giữ người xem được nhưng là giật tít: **không dùng** (Teachera trong file Rule Reviewer: hook phải đúng nội dung). |
| @ng__phanh https://www.tiktok.com/@ng__phanh/video/7532553338664045831 | 1,1 triệu view · 695 comment (20/10), 20s | Caption: «Học 1 đêm mới hiểu sao kiến thức được dạy trong 1 kỳ» | Nỗi đau ôn thi một đêm, nói kiểu tự giễu mình chứ không chê người xem. Đây là **tín hiệu nỗi đau**, không phải mẫu cấu trúc. |
| @motionlab.fit https://www.tiktok.com/@motionlab.fit/video/7698336587259661586 | 5.056 view (20/10, đăng 19/10, clip dài ~5 phút) | «3 giờ chiều bạn ngồi trước màn hình mắt zip lại … bạn làm việc quen thuộc nhất xuống quán gọi một ly cà phê sữa đá … nếu vòng lặp này nghe quen video này dành cho bạn» | **Không phải bằng chứng hiệu quả** (view thấp, clip dài). Chỉ là mẫu câu tốt: gọi «bạn», mốc giờ cụ thể, hành động nhìn thấy được, câu «nếu… nghe quen thì…» đúng kiểu điều kiện mềm W-10. |
| @phamthuykieuhuong https://www.tiktok.com/@phamthuykieuhuong/video/7665937572925066516 | 995.100 view (17/10), 6s | «lặp lại ngắt quãng kỹ thuật fame mình vẽ sơ đồ tư duy My map Black cast và active recall» | Đã phân tích ở `final/trend-signals.md`. Clip chỉ liệt kê tên kỹ thuật, không có câu chuyện. |

Kết luận phần 5 (chỉ ở mức dữ liệu cho phép, mẫu nhỏ): clip học tập Việt nhiều view hay mở bằng **câu người học tự nói/tự hỏi** hoặc **chấp nhận hoàn cảnh rồi "nhưng"**. Nhiều clip dùng số không nguồn (70%, 95%): kênh mình không làm vậy, và đó có thể là điểm khác biệt nếu nói đúng nguồn một cách tự nhiên.

## 6. Rút ra cho @hi.oneup — 10 luật, mỗi luật ứng với một lỗi hay gặp

Các ví dụ tốt dưới đây đi theo chuyện clip-04 và fact lock hiện có. Đây là **ví dụ câu**, không phải script.

| # | Luật (nguồn) | Lỗi hay gặp | Câu sai → câu đúng |
|---|---|---|---|
| 1 | **Ngân sách 140–160 chữ, chia theo beat trước khi viết** (đo F5 4,48 chữ/s; phần 1) | Dài ~200 chữ | Trước khi viết, ghi sẵn: hook ≤ 22 · hứa ≤ 12 · chuyện ≤ 40 · bước ≤ 25 · bằng chứng ≤ 25 · đóng vòng ≤ 20 · CTA ≤ 16 chữ. |
| 2 | **Câu ai → làm gì → kết quả; câu cùng người làm thì nối bằng phẩy** (WBA; W-09) | Câu cụt không chủ ngữ | «Tối đọc đi đọc lại. Tưởng mai nhớ hết.» → «Tối đó mình đọc đi đọc lại, tưởng sáng mai nhớ hết.» |
| 3 | **Ngắn là bớt ý, không phải bớt chữ trong câu** (shiyan521: xóa câu mà vẫn hiểu thì xóa; DINFOS «concise») | Cắt chữ thành câu cụt để đạt số chữ | Không cắt «mình» khỏi câu. Cắt **cả một ý**: bỏ liệt kê bốn từ airport…passport, chỉ giữ chỗ bí. |
| 4 | **Không đại từ trơ, không cụm trừu tượng** (DINFOS «beware of it/that/they»; L-063) | «phần đó», «cách này», «một bước» chưa nói là gì | «Mình chỉ đổi đúng một bước.» → «Mình chỉ đổi một việc: học xong là gấp sách, tự viết lại.» |
| 5 | **Điều kiện mềm, kiểu chấp nhận rồi "nhưng"** (sabito_0668; L-073/W-10) | Câu ra lệnh cộc | «Gấp sách lại viết đi.» → «Đọc lại thì cứ đọc, nhưng trước khi ngủ, bạn thử gấp sách viết lại mười từ xem.» |
| 6 | **Bằng chứng = câu trả lời cho chỗ khựng, một câu, kết quả trước** (Mar 2021; AAAS qua Northeastern) | Đoạn giảng fact khô | «Dunlosky xếp các cách học… Yang gộp…» → «Nên mình mới tin việc tự viết lại: nhóm của Yang gộp 222 nghiên cứu, thấy lớp có làm kiểm tra nhỏ thì điểm cao hơn, ở mức vừa.» |
| 7 | **Chức danh trước tên, ít dấu hai chấm** (Media Helping Media; STT nghe «Giang») | Tên tác giả trơ, đọc như slide | «Yang tổng hợp…» → «Nhóm nghiên cứu của Yang…»; «Bước mình đổi là: …» → «Bước mình đổi là học hết mười từ thì gấp sách…» |
| 8 | **Đường cảm xúc có một chỗ xuống và một chỗ lên; sửa trục yếu nhất trước** (script-evaluator) | Năng lượng đều, đọc như thuyết minh | Chỗ xuống: «tới từ thứ năm thì mình bí, đầu trống trơn.» Chỗ lên: «sáng hôm sau, sách vẫn gấp, mình tự viết được luggage.» |
| 9 | **CTA làm được ngay và comment được ngay** (TokPortal: lời rủ comment cụ thể, dễ làm https://www.tokportal.com/post/tiktok-comments-strategy-turn-us-viewers-into-fans-and-customers ; TikTok: trả lời comment bằng video https://newsroom.tiktok.com/en-us/product-tutorial-reply-to-comments-with-video) | CTA bắt người xem đi học xong mới comment | «Lần học tới thử rồi comment…» → «Giả sử bây giờ gấp sách, bạn viết lại được mấy từ của bài hôm qua? Comment con số nha.» (Người xem trả lời được trong 5 giây. Comment hay nhất dùng để làm clip trả lời.) |
| 10 | **Không bao giờ chép số của creator khác; nói đúng nguồn để khác biệt** (camreadwonder 70%, gonaox 95% không nguồn; Spaulding «proven») | Bịa số hoặc nói quá | «Người ta quên 70% sau 24 giờ.» → không dùng. Nếu cần, chỉ nói fact đã khóa, kèm «ở mức vừa». |
| 11 | **Quy trình viết là một chuỗi có bước chấm riêng** (Anthropic chaining; Self-Refine; ops120 review.py) | Sửa đi sửa lại nhiều vòng | Thứ tự: nháp → bộ chấm riêng ra bảng lỗi theo dòng → chỉ sửa đúng các dòng đó → chấm lại. Mỗi lời Hiệp chê thành một dòng ví dụ sai/đúng trong prompt. Chi tiết: `research/script-writer-prompt.md`. |

## 7. Nhận xét v17 (`final/script-v17.md`, đọc lúc 20/10 ~22:30 giờ VN) — chỉ nêu điểm, không viết lại

Đếm bằng script (bỏ `{nhấn:}`): **161 chữ**, chia theo beat: b01 24 · b02 8 · b03 32 · b04 15 · b05 25 · b06 22 · b07 19 · b08 16. Theo số đo F5 thì khoảng 36s nói, ~44s giọng: đạt W-14.

**Rủi ro luật (cần Rule Reviewer hoặc Hiệp quyết):**
1. **Hook b01 vế 2 đã đổi so với câu Hiệp chốt (L-073).** v16c ghi rõ «Hook b01 do Hiệp chốt nguyên văn: … Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì?». v17 thay bằng «Có khi nào lỗi nằm ở cách ôn, chứ không phải ở trí nhớ của bạn?». Đổi lời Hiệp đã chốt thì phải trình rõ cho Hiệp là hook đã đổi.
2. **b01 vế 2 dễ bị bắt lỗi L-055/L-056.** Đây là dạng «không phải X mà là Y», nhưng Y («cách ôn») còn trừu tượng, chưa nói ôn sai ở việc gì. Câu cũng là câu hỏi **có/không**: shiyan521 xếp câu hỏi có/không vào loại phải tránh, vyral coi hook câu hỏi là kiểu yếu nếu không sắc. Ngoài ra câu này **đã nói luôn đáp án** (lỗi ở cách ôn), nên vòng tò mò đóng ngay giây 5, và b04 phải nói lại cùng ý (P-01/L-054).
3. **W-12: «từ hết hook tới lúc nói cách làm ≤ ~50 chữ».** Từ b02 tới b04 có 8 + 32 + 15 = **55 chữ** trước khi b05 nói cách làm, vượt ~10%. Cách làm tới ở khoảng giây 21, muộn hơn mốc 12–15s Deep Research đề xuất.
4. **b06 «lớp không có».** Câu bỏ lửng tân ngữ nên có thể nghe thành «lớp không có kiểm tra gì», tức đúng lỗi nói quá mà Deep Research đã bắt ở v16 (nhóm so sánh vẫn có bài thi cuối). Cần Deep Research soát lại. Nói «lớp không làm kiểm tra nhỏ» (như v16c) thì an toàn. Thêm nữa, «Yang» trơ đã bị STT nghe thành «Giang» ở v16c (s09). Media Helping Media khuyên đặt chức danh trước tên: «nhóm của Yang».
5. **b08 CTA có hai yêu cầu và trễ.** «Lần học tới, bạn thử gấp sách viết lại, rồi comment số từ nhớ được» nghĩa là người xem phải đi học xong mới comment được. W-14 yêu cầu một yêu cầu. Lời rủ comment nên làm được ngay (TokPortal). Tính kiểm được: bắt buộc.

**Điểm tay nghề nên sửa (có nguồn):**
6. **b02 «Mình chỉ đổi đúng một bước khi ôn.»** Câu có chủ ngữ, nhưng «một bước» chưa nói là bước gì và được kết quả gì. Lời hứa sớm nên nói rõ kết quả («deliver on the click», Paddy Galloway, ghi chú podcast https://pod.wave.co/podcast/sweat-equity/the-new-rules-of-youtube-in-2026-w-paddy-galloway), không chỉ báo là «có một bước». Theo DINFOS thì đây cũng là cụm trừu tượng phải chờ beat sau giải thích hộ (L-055).
7. **b05 «Bước mình đổi là:».** Có dấu hai chấm (Media Helping Media khuyên tránh, F5 dễ ngắt kiểu đọc bài). Chuyện chuyển từ «ba mươi từ» sang «mười từ» mà lời không nói đã chia thành ba chồng. Hình có ba chồng, nhưng tắt tiếng hoặc chỉ nghe thì người xem không biết mười từ ở đâu ra (L-063).
8. **b04 «chứ mình chưa hề tự nhớ ra?»** «chưa hề» nặng và tuyệt đối hơn nguồn. HTB 23.14 chỉ nói đọc lại tạo quen mắt chứ không làm nhớ chắc. Nên dùng chữ đúng mức hơn (P-03).
9. **Thiếu chỗ xuống cảm xúc rõ** (script-evaluator, trục đường cảm xúc). b03 kết bằng «thì bí» một chữ, chưa có câu cảm giác thật (L-052: mỗi fact đi kèm một cảm giác). Bản nghe sẽ dễ phẳng ở b03–b05.
10. **Hook chỉ có một kiểu (câu hỏi).** Deep Research và vyral đề xuất viết 6–10 hook nhiều kiểu rồi chọn. Một vài kiểu khác để Hiệp chọn, giữ luật «nỗi đau + câu hỏi» (P-05/P-16) và fact lock. Đây là **lựa chọn**, chưa chấm, chưa qua Rule Reviewer:
    - Lời người học tự nói (kiểu @biquyetdodaihoc / @camreadwonder): «Tối qua đọc tới thuộc làu, sáng nay gấp sách lại thì viết không ra?»
    - Chấp nhận rồi «nhưng» (kiểu @sabito_0668): «Đọc lại bài thì ai cũng đọc, nhưng sáng ra gấp sách, bạn viết lại được mấy chữ?»
    - Đối lập (shiyan521 «đối lập»): «Đọc đi đọc lại mười lần, gấp sách lại thì trắng giấy, bạn đã bị vậy chưa?»
    - Giữ nguyên câu Hiệp chốt ở L-073: «Học thuộc tối qua, sáng dậy quên sạch? Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì?»

**Đã đạt (không cần sửa):** mọi câu có chủ ngữ (W-09); fact chỉ còn một câu (W-12, 22 chữ); luggage chỉ xuất hiện sau khi mở sách (b05 → b07); «nha» đúng 1 lần; đóng vòng ở b07 quay về đúng chữ bí; bỏ liệt kê bốn từ tiếng Anh nên hết lỗi F5 đọc «Epoch/Backbox»; tránh được các chữ «chột», «xong», «Viết trước».

## Nguồn (tất cả đã đọc ngày 20/10/2026)
- Coupé và cs. 2019, Science Advances, qua EurekAlert: https://www.eurekalert.org/news-releases/763747 · https://e3.eurekalert.org/news-releases/887122 · Worldcrunch: https://worldcrunch.com/culture-society/syllable-counting-and-the-secret-to-the-39speed39-of-languages/ · Science/AAAS: https://www.science.org/content/article/human-speech-may-have-universal-transmission-rate-39-bits-second
- WBA Newsroom: https://www.wbanewsroom.org/newsroom-tips/tips-for-radio-news-writers/
- UF/IFAS WC193: https://ask.ifas.ufl.edu/publication/WC193
- DINFOS Broadcast Writing Style Guide 2015: https://www.dinfos.dma.mil/Portals/66/Documents/Academics/BOMD/2015%20DINFOS%20Broadcast%20Writing%20Style%20Guide.pdf
- Media Helping Media: https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/
- Mar và cs. 2021: https://doi.org/10.3758/s13423-020-01853-1
- Northeastern (AAAS toolkit): https://graduate.northeastern.edu/knowledge-hub/tips-for-effective-science-communication/
- K. Spaulding (LinkedIn, ý kiến): https://www.linkedin.com/posts/kristina-spaulding-phd-caab-91028282_proven-is-one-of-those-words-that-makes-activity-7512108263816204288-hPxr
- Anthropic prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Self-Refine: https://arxiv.org/abs/2303.17651 · https://github.com/madaan/self-refine
- script-evaluator: https://github.com/AnastasiyaW/claude-code-config/blob/main/skills/video-production/script-evaluator/SKILL.md
- short-video-script-sop: https://github.com/shiyan521/short-video-script-sop/blob/main/references/hook-formulas.md
- vyral hooks.md: https://github.com/vyralcontent/content-skills/blob/main/skills/viral-short-form/references/hooks.md
- ops120 review.py: https://github.com/ops120/video-recap-skills-plus/blob/main/skills/video-script/scripts/review.py
- krillinai/OpenCreator: https://github.com/krillinai/OpenCreator (executor.ts, templates/short-video-script.ts)
- Paddy Galloway (ghi chú podcast): https://pod.wave.co/podcast/sweat-equity/the-new-rules-of-youtube-in-2026-w-paddy-galloway
- TokPortal: https://www.tokportal.com/post/tiktok-comments-strategy-turn-us-viewers-into-fans-and-customers · TikTok Newsroom: https://newsroom.tiktok.com/en-us/product-tutorial-reply-to-comments-with-video
- Clip TikTok ở phần 5 (link trong bảng). Dữ liệu: `research/trends/2026-10-1{6,7,8}/apify/`, `research/trends/2026-10-20/apify/`.
- Chưa kiểm chứng, không dùng: «90% ad recall trong 6 giây đầu» (TikTok tự nêu cho quảng cáo, không phải cho clip giáo dục); «quên 70% sau 24 giờ» (camreadwonder); «95% học sinh không biết» (gonaox).
