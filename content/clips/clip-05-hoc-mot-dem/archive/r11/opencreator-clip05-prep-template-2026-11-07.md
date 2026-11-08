---
title: "clip-05 (23.14 tự kiểm khi đọc, hướng C): bài học kỹ thuật + MẪU TRỐNG file kịch bản — bản sửa sau review CHƯA ĐẠT"
date: 2026-11-07
author: OpenCreator Studio
status: chuẩn bị, chưa có lời thoại, chưa kiểm giọng
revision: r2 (14:1x, 07/11, giờ VN) — sửa 10 điểm Rule Reviewer + cập nhật phạm vi Dunlosky do Reviewer chuyển 14:09
scope: kỹ thuật viết + khung trống. Không tự nghiên cứu trend/fact, không script, không voice/render. Concept một dòng ở file riêng.
type: prep
tags: [clip-05, r11, archive]
source: "/workspace/opencreator-clip05-prep-template-2026-11-07.md (archived as-is in commit 0d569da; author OpenCreator Studio)"
---
# clip-05: bài học + mẫu trống (07/11/2026, giờ VN)

> **Cập nhật 07/11/2026 (UTC+7):** khung này dùng cho bản nháp hiện hành r11.1 `/workspace/opencreator-clip05-script-r11.1-draft-2026-11-07.md`. r11 (`opencreator-clip05-script-r11-draft-2026-11-07.md`) bị Reviewer + Deep chấm CHƯA ĐẠT. r11.1 chưa review lại; đọc to CHƯA KIỂM.


## 0. Nguồn đã đọc và trạng thái (kiểm git lúc ~14:1x, giờ VN)
| File | Commit | Trạng thái quan sát / được chuyển |
|---|---|---|
| `research/fact-packages/factcheck-clip05-lock-2026-11-07.md` (Deep) | `b02dd07` (13:25) | **Phạm vi Dunlosky dòng 22–28 do Deep chọn, Rule Reviewer chuyển lúc 14:09.** Mình không tự factcheck. News báo đã sync. |
| `research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md` (Deep) | `d673dd9` (14:07) | Nối **có điều kiện**: trend là bối cảnh, tự kiểm là khuyến nghị riêng khi mục tiêu là học/nhớ. Phần thân file vẫn ghi «chưa commit» — dòng cũ; git có commit, News báo sync. |
| `research/trends/2026-11-07-clip05-texthip-bridge-check.md` (Social) | `bd53fd3` (14:07) | Có nguồn báo chí mô tả #texthip. **Không xác nhận hot trên TikTok, không có số tương tác.** Không có nguồn nào nói người theo trend quên. Phần thân cũng ghi «chưa tạo trong repo» — dòng cũ. |
| `git ls-remote origin main` | `bd53fd3` | Khớp HEAD local |
| Hướng C | — | Hiệp chọn (Rule Reviewer chuyển 14:05). Mình chưa tự xác minh. |
| L-096 với bằng chứng xếp hạng | — | Theo Reviewer chuyển 14:09: L-096 chấp nhận **đối chiếu xếp hạng** (tự kiểm hữu ích cao, đọc lại thấp), không bắt buộc thí nghiệm chia nhóm. **Hết blocker tìm A-vs-B.** |
| `logs/lessons.md` (L-097), `logs/rule-checklist.md` | working tree | Có sửa chưa commit. Mình đọc bản đang có trên đĩa. |
| Rules đã đọc lại cho lần sửa này | — | rule-52 (dòng 158–162), rule-56, rule-62, rule-64 (dòng 228–232); checklist P-10, P-15, P-16, W-04, W-11, W-13, W-16, L-088, L-089, L-090, L-094, L-096 (dòng 178) |

**Rủi ro lớn phải báo:** clip-04 (v18 đã chốt) cũng dùng 23.14, cũng là gấp sách rồi viết lại, cũng dẫn Yang và Roediger. clip-05 trên cùng mục **phải khai callback với clip-04 (rule-62)** và đổi hẳn tình huống, hook, CTA. Danh sách điều cần tránh nằm ở file concept.

## 1. Bài học kỹ thuật (độc lập với việc chọn trend)

Ký hiệu: **[Q]** nguồn nói thật · **[S]** suy luận của mình · **[Luật]** luật hoặc lesson của kênh, có sức chặn.

### 1.1 Nguồn đã đọc và mức tin
| Mã | Nguồn | Loại | Dùng được tới đâu |
|---|---|---|---|
| A1 | TikTok Creator Academy, «Captivating content with great storytelling» — https://www.tiktok.com/creator-academy/article/captivating-content-with-great-storytelling | Lời khuyên chính thức cho creator, không kèm số liệu | Gợi ý cách làm, **không phải bằng chứng retention** |
| A2 | TikTok Creator Academy, «Understanding and engaging with your audience» — https://www.tiktok.com/creator-academy/article/Understanding-and-engaging-with-your-audience | Như A1 | Như A1 |
| A3 | TikTok Ads Help, «Creative best practices for performance ads» (cập nhật 06/2025) — https://ads.tiktok.com/help/article/creative-best-practices | **Hướng dẫn quảng cáo trả phí** | Chỉ để tham khảo. **Không được coi là bằng chứng retention của clip organic.** |
| A4 | Dahlstrom 2014, PNAS 111 Suppl 4:13614–20, PMID 25225368 (đọc abstract qua NCBI) | Bài tổng quan về truyền thông khoa học | Kể chuyện giúp người không chuyên hiểu và hứng thú; chuyện cũng tự có sức thuyết phục nên có vấn đề đạo đức. **Không nói gì về TikTok hay retention.** |
| A5 | Blossom, «Educational TikToks That Hold Viewers» — https://blossai.com/blog/educational-videos-that-hold | Blog bên thứ ba, không có dữ liệu | Ý tưởng tham khảo, mức tin thấp nhất |
| R | Lessons và rule-checklist của kênh | Luật Hiệp đã duyệt | **Thắng mọi nguồn A khi xung đột** |

### 1.2 Bài học cụ thể → dùng ở đâu trong script sau
| # | Bài học | Nguồn | Áp vào | Cách kiểm khi viết |
|---|---|---|---|---|
| K1 | Mở bằng vướng mắc người xem đang gặp, nói thẳng bằng «bạn». Câu hỏi đi kèm phải được trả lời ngay sau. | [Q] A1/A2 (câu hỏi được trả lời dần trong clip) + [Luật] L-057, L-058, L-094 | b01 → b02 | Câu hỏi b01 có câu trả lời ở b02, hoặc ở câu kế có chữ báo đây là câu trả lời? |
| K2 | Hook có lý do dừng lướt cụ thể: cái mới, cái bất ngờ, hoặc cái giá rõ ràng. Người lạ đọc câu đầu phải nói lại được clip bàn chuyện gì. | [Luật] L-096, L-064 · [Q] A1 (thứ thấy đầu tiên phải khác lạ, chữ ngắn nói chủ đề) | b01 + chữ màn hình frame 0 | Viết được câu «vì sao người lướt sẽ dừng»? Làm phép thử người lạ chưa? |
| K3 | Có thể mở giữa cao trào rồi quay lại. Câu quay lại phải gọi đúng mốc thời gian hoặc hành động đã nêu. | [Q] A1 (tease kết quả / bắt đầu ở cao trào) · [S] nối với L-058 | b01–b02 | Câu quay lại có lặp mốc của hook, hay là «nếu…» lửng? |
| K4 | Một thông điệp, một tình huống đọc xuyên suốt. Ví dụ phải xuất hiện sớm. | [Q] A1 (một key message) · A5 · [Luật] L-063, L-087 | Toàn clip; ví dụ phải có mặt ở b02 | Viết được cả clip thành 1 câu? Mỗi beat trả lời được đang làm gì / với cái gì / khựng ở đâu? |
| K5 | Nghiên cứu là câu trả lời cho câu hỏi của hook, không phải đoạn giảng. Nói đủ ai, xét cái gì, kết quả đúng chữ nguồn. | [Luật] L-088, L-096, W-12 · [Q] A4 · [S] chuyện càng cuốn càng phải giữ đúng phạm vi | b03 | Đúng nguyên văn gói Deep đã xác nhận? Không «nhiều nghiên cứu thấy»? Không biến xếp hạng thành phép thử A-vs-B? |
| K6 | Thứ tự lập luận: vấn đề và nguyên nhân → mục tiêu → giải pháp → kết quả. | [Luật] W-16 (L-077) | b02 → b06 | Gán nhãn vai trò từng câu, xem có lệch thứ tự không |
| K7 | Ý trừu tượng phải thành vật và hành động thấy được, không vẽ chữ. | [Q] A5 (làm ý trừu tượng thành vật, so trước/sau) · [Luật] L-050, L-066 | Cột khung hình, mọi beat | Vật nào lời nhắc tới như hành động chính thì có prop thật chưa? |
| K8 | Chữ trên màn hình làm kênh thứ hai cho người xem tắt tiếng. | [Q] A1/A2 (caption, chữ dán) · [Luật] P-09 (EN ≤ 8 từ mỗi chunk) | Cột chữ màn hình | Đếm từ mỗi chunk |
| K9 | Một CTA (một yêu cầu), nói rõ người xem làm gì, quay lại hook, chữ mới so với clip trước. Các kiểu engagement khác rải ở beat khác, không gộp thành nhiều yêu cầu. | [Q] A3 (strong CTA — hướng dẫn quảng cáo) · A2 (giữ trò chuyện ở bình luận) · [Luật] rule-56, L-088 | b07 | Đếm yêu cầu trong CTA = 1? So với CTA của clip-04 và các bản clip-05 cũ? |
| K10 | Giữ người xem bằng nối nhân quả hoặc đối chiếu, không «rồi thì». | [Luật] L-089, L-092, L-094 · [Q] research/tiktok-script-craft-2026-10-20.md (vyral) | Mọi cặp câu | Bảng cặp câu ở §4 |

**Xung đột cần nhớ:** A3 khuyên hook trong 6s đầu, còn kênh đòi 3s (rule-55, L-021) → **theo kênh**. Nguồn bên ngoài thích câu ngắn cụt, còn W-09 và L-096 cấm câu cộc, cấm thiếu chủ ngữ → **theo kênh**. Kiểu hook: X-08 **đã hết là blocker** (Reviewer 14:14, thông tin chuyển); r11 dùng tình huống → câu hỏi (P-16/P10).

---

## 2. MẪU TRỐNG file kịch bản (copy ra file nháp; mọi ô `[…]` để trống tới khi đủ nguồn)

```markdown
---
title: "clip-05 r11.x: [tiêu đề = thông điệp 23.14]"
date: [YYYY-MM-DD]
type: script
status: draft — chưa đọc to, chưa chấm, chưa kiểm giọng
handbook: 23.14 (chính) · 23.16 (phụ, chỉ ý «đọc lại hữu ích thấp, không vô dụng»)
direction: C — bối cảnh đọc → đổi rõ mục tiêu sang học/nhớ → khuyến nghị riêng (Hiệp chọn; Reviewer chuyển 14:05)
trend_id: texthip-kr-reading-lifestyle-znews-1693810   # ID nội bộ của Social, KHÔNG phải ID nền tảng, KHÔNG phải nhãn hot; không dùng B-texthip-01 (4.15)
hook_pattern: [P-xx active trong research/trends/patterns.md, khác pattern các bản bị bác]
trend_beats: [b01 / b02]
trend_spoken: "[cụm nói thành lời, đúng điều nguồn Social ghi]"
example_evidence: Lee Yunjee tập đọc sách + viết nhật ký để giảm lệ thuộc nội dung ngắn (Znews 05/11/2026 06:00, znews.txt dòng 24–26, snapshot 07/11 14:07:28 giờ VN) — CHỈ là bối cảnh trend, KHÔNG phải ví dụ tự kiểm / đọc-quên / đọc để làm theo
example_label: "MINH HỌA BIÊN TẬP CỦA KÊNH"   # bắt buộc cho mọi ví dụ đọc để làm theo / tự kiểm trong lời; tách khỏi evidence trend
fact_sources: research/fact-packages/factcheck-clip05-lock-2026-11-07.md@b02dd07 (dòng 22–28) · research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md@d673dd9
trend_sources: research/trends/2026-11-07-clip05-texthip-bridge-check.md@bd53fd3
callbacks: [clip-04 (23.14 gấp sách) — bắt buộc khai, rule-62]
viewer_pronoun: bạn (b01 → b07)
transition_sfx: {part: "whoosh-soft", scene: "swish"}
---

## A. Một câu của cả clip
[ … ]  (nếu phải dùng 2 câu → là 2 video)

## A2. Các ô giữ người xem (điền trước khi viết lời)
| Ô | Nội dung | Luật |
|---|---|---|
| Hứa lợi ích sớm (hứa kết quả, KHÔNG nói cách làm trước nguyên nhân) | [beat · ý] | W-11, W-16 thắng |
| Móc giữa clip (câu hỏi hoặc chỗ nhận ra, ở khoảng 30–60% thời lượng) | [beat · ý] | W-13 |
| Callback có chủ đích tới clip trước | [clip-04: gọi lại thế nào, không lặp chữ] | rule-62, L-088 |
| Thông điệp HTB 23.14 NÓI THÀNH LỜI (gần nguyên văn tiêu đề mục) | [beat · câu] | templates/script.md (beat Thông điệp), L-036 |
| Tóm tắt 1 câu trả lời câu hỏi hook | [beat] | rule-64 |

## B. Trend / bridge C (theo nguồn đã lưu; không tự nghiên cứu thêm)
**Bối cảnh trend (chỉ được nói điều nguồn ghi):**
| Nguồn | Ngày bài | Snapshot / truy xuất | Nói được gì | Không được nói |
|---|---|---|---|---|
| Znews (bài gốc) | 05/11/2026 06:00 GMT+7 | Social đọc lúc 07/11 14:07:28 (giờ VN); snapshot `znews.txt` | Báo mô tả đọc sách/#texthip thành phong cách sống của một bộ phận người trẻ Hàn; trường hợp Lee Yunjee tập đọc, viết nhật ký để bớt lệ thuộc nội dung ngắn (lời một người) | «Gen Z Hàn bỏ video ngắn»; hot trên TikTok; người theo trend quên |
| Vietnam.vn (bản đăng lại Znews) | hiển thị 04/11/2026 (lệch với ngày gốc) | Social đọc lúc 07/11 14:07:28 (giờ VN); `vietnam-vn.txt` | Không phải nguồn độc lập thứ hai | Dùng ngày 04/11 như ngày gốc |
| The Korea Times (Park Han-sol) | 04/11/2026 07:00 KST = 05:00 giờ VN | Social đọc lúc 07/11 14:07:28 (giờ VN); `korea-times.txt` | Đọc để tận hưởng, chia sẻ; câu lạc bộ; text-hip như thể hiện gu | «Viral» = nhãn của báo, không phải xác nhận hot; số liệu đọc và doanh thu là số báo dẫn lại, chưa kiểm |
| Digest cũ | snapshot 05/11/2026, commit `4014ab3` | — | B-texthip-01 thuộc 4.15 | Đổi nhãn sang 23.14 |
| Tương tác TikTok / hashtag | — | **KHÔNG CÓ** | — | Không điền số, không gọi hot |

**Tách bối cảnh với khuyến nghị:**
| Ô | Nội dung |
|---|---|
| Bối cảnh (trend, chỉ để mở chuyện) | [một câu, đúng chữ nguồn Social] |
| Câu đổi mục tiêu (đọc để tận hưởng ≠ đọc để học/nhớ) | [một câu; không chê đọc thưởng thức] |
| Khuyến nghị riêng của kênh (23.14) | [chỉ áp khi mục tiêu là học/nhớ; không nói là bài học của trend] |
| Câu cấm (Deep d673dd9 + Social bd53fd3) | người theo #texthip đọc mà không nhớ · trend giúp nhớ · họ thắng nhờ tự kiểm / không bằng ý chí · dùng số người đọc làm số đo trí nhớ · pilsa/chép tay = tự kiểm · gọi hot |
| trend_id | `texthip-kr-reading-lifestyle-znews-1693810` — ID nội bộ Social, không phải ID nền tảng, không phải nhãn hot |
| example_evidence (trend) | Chỉ có Lee Yunjee: tập đọc sách và viết nhật ký để giảm lệ thuộc nội dung ngắn (Znews 05/11 06:00, znews.txt dòng 24–26, snapshot 07/11 14:07:28). Một trường hợp báo chí, không xác nhận đã giảm thời gian màn hình hay nhớ tốt hơn. **Chỉ dùng làm bối cảnh.** |
| Nguồn KHÔNG có (ghi null, không bịa) | ví dụ đọc để làm theo · đọc rồi quên · tự kiểm trong trend · bình luận khán giả |
| Ví dụ chính trong lời (đọc để làm theo / tự kiểm) | [ … ] — nhãn bắt buộc **MINH HỌA BIÊN TẬP CỦA KÊNH**; không gọi là example_evidence; không suy «nhớ được chỉ dẫn = làm theo thành công»; pilsa không phải retrieval |
| Nguồn metadata | Social qua Reviewer chuyển 14:14 · archive `bd53fd3` (Social đọc lại) · addendum `/workspace/clip05-texthip-metadata-2026-11-07.json` **ngoài repo, chưa SHA, chưa commit/sync** — mình đọc nhưng không tự xác minh thêm |
| Trend nói thành lời ở | [b01 / b02] |
| Kết luận bridge của Rule Reviewer về độ tự nhiên (L-096 (4)) | [CHƯA THẤY kết luận] |

## C. Fact lock (attribution: Deep chọn, Rule Reviewer chuyển 14:09 — OpenCreator không tự factcheck)
| # | Claim nói trong lời | Nguyên văn tham khảo được phép | Nguồn | Giới hạn bắt buộc | Beat |
|---|---|---|---|---|---|
| C1 | Đối chiếu XẾP HẠNG trong tổng quan | «Năm 2013, nhóm Dunlosky đánh giá mười kỹ thuật học. Tự kiểm tra được xếp mức hữu ích cao, đọc lại ở mức thấp.» (câu fact tham khảo, chưa chấm luật script) | factcheck-clip05-lock@b02dd07 dòng 22–28 | Là tổng quan xếp hạng, KHÔNG phải thí nghiệm chia nhóm. Không «đọc lại vô dụng». Không nói nhớ lâu, nhớ hơn trực tiếp, %, hay kết quả chắc chắn cho người đi làm. Không nói hiệu quả với người theo #texthip. | b03 |
| C2 | Bước tự kiểm của cẩm nang | Gấp tài liệu → tự nói hoặc viết điều nhớ được → mở ra đối chiếu và sửa (F5) | 23.14 qua lock@b02dd07 và bridge@d673dd9 | Là lời khuyên của cẩm nang; ví dụ đời thường ghi «minh họa» | b05 |
| C3 | (phụ) Đọc lại | Mức hữu ích thấp, không vô dụng | 23.16 qua lock@b02dd07 | Chỉ dùng nếu cần, không chê người đọc lại | b03 |
| — | **Yang 2021** | KHÔNG dùng trong lời, KHÔNG lên end card khi lời không nói claim Yang | lock@b02dd07 | — | — |
Ví dụ đời thường và mọi con số gợi ý của kênh: ghi nhãn «minh họa / gợi ý của kênh». Ví dụ Deep gợi ý: đọc bài về chi tiêu, gấp lại kể điều muốn áp dụng — chỉ là minh họa.

## D. Hook (P-15 / P-16 / L-088 / L-094 / L-096 / rule-64 — mở cao trào KHÔNG được miễn luật nào)
| Ô | Nội dung |
|---|---|
| Lời hook (văn nói) | [để trống] |
| Câu đầu nêu đang đọc/học gì ở mức chung + chỗ đau cụ thể (P-16) | [có/không — chỉ ra chữ] |
| Phép thử người lạ: chỉ đọc câu đầu, nói lại được chuyện gì + đau ở đâu (P-16, L-064) | [chưa thử / kết quả] |
| Câu hỏi (nếu có) bám đúng nỗi đau / mốc / phép thử của câu trước, không «nếu…» lửng (P-06, L-058) | [ … ] |
| Câu hỏi được trả lời ngay ở câu kế, hoặc câu sau có chữ báo trả lời (L-094) | [câu nào] |
| Nếu mở ở cao trào (P-15): vẫn phải đủ 4 dòng trên; con số hoặc bối cảnh cụ thể không ép vào 3s đầu | [ … ] |
| Lý do người lướt sẽ dừng (1 câu, L-096 (1)) | [ … ] |
| Kiểu hook (rule-64: trực tiếp / gây tranh cãi có bằng chứng ngay sau / phủ định) + pattern P-xx | [ … ] |
| Khác kiểu và khác 6 chữ đầu so với 2 clip trước và các bản bị bác (L-088, `--fresh`) | [có/không — so với danh sách trong file concept] |
| Không chê người đọc / người theo trend (P-07, Deep d673dd9) | [ … ] |
| Chữ màn hình frame 0 + 2 cut/hit trong 0–3s (rule-55) | [ … ] |
| Ngân sách chữ | **Chưa chốt**, tùy tốc độ giọng thật. Rule-55 chỉ đòi lời đầu ≤ 0,3s và vế đầu ≤ 6 chữ. |

**hook_alt (bắt buộc, rule-64):**
| Ô | Nội dung |
|---|---|
| Lời hook_alt | [để trống] |
| Kiểu (khác kiểu hook chính) | [ … ] |
| Kiểm cùng các dòng P-16 / P-06 / L-094 / L-088 như hook chính | [chưa kiểm] |

**Khung rule-64 (`spec.structure`):** Hook [beat] → Intro, vì sao xem tiếp [beat] → Body: vấn đề [ ] · khám phá có nguồn [ ] · cao trào và cách làm [ ] → Tóm tắt 1 câu trả lời hook [ ] → 1 CTA [ ]

## E. Bảng beat (W-04: đủ cột trình Hiệp; giây dự kiến, CHƯA ĐO; ngân sách chữ chưa chốt)
### b01 Hook
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Hook (pain + câu hỏi nếu có) |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | — (mở clip). Nếu hook có 2 câu: câu 2 nối câu 1 bằng chữ [ … ] |
| Nguồn của claim | [không mang claim nghiên cứu] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b02 Bối cảnh trend → đổi mục tiêu sang học/nhớ
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Vấn đề / trả lời ngay câu hỏi hook (L-094) |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [câu đầu b02 trả lời câu hỏi b01 bằng chữ nào] |
| Nguồn của claim | [bối cảnh trend: chỉ điều nguồn Social ghi, xem bảng B] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b03 Nguyên nhân + dẫn chứng
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Nguyên nhân + dẫn chứng |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [dẫn chứng trả lời chỗ vướng b02 bằng chữ nào; không mở bằng «Theo nghiên cứu»] |
| Nguồn của claim | [bảng C dòng C1 — Dunlosky 2013, đối chiếu xếp hạng] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b04 Mục tiêu
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Mục tiêu |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [mục tiêu nảy ra từ b03 bằng chữ nào; giữ ngôi «bạn»] |
| Nguồn của claim | [ … ] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b05 Giải pháp — một bước làm được hôm nay
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Giải pháp |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [bước này đạt mục tiêu b04 ra sao, nối bằng chữ nào] |
| Nguồn của claim | [bảng C dòng C2 — 23.14 / F5] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b06 Kết quả / đóng vòng
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | Kết quả |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [quay lại đúng chỗ vướng b02; không hứa nhớ lâu, không con số] |
| Nguồn của claim | [không thêm claim mới] |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### b07 CTA
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Vai trò W-16 | CTA (một yêu cầu) |
| Người nói | [Thầy — một người nói từ b01 tới b07 (L-039); Omi chỉ khi tuần ≥ 5 (rule-11)] |
| Ngữ cảnh | [ai, đang đọc gì, ở đâu, lúc nào] |
| Cảnh / shot | [ … ] |
| Hành động (stage.action) | [ … ] |
| Cảm xúc / phản ứng (stage.react) | [ … ] |
| Lời thoại (văn nói) | [để trống — đúng MỘT yêu cầu; chữ mới so với danh sách tránh; không xin like/follow] |
| {nhấn:} (1–2 chữ gánh ý) | [ … ] |
| Ngắt tự nhiên | [chỉ ở dấu câu / ranh giới cụm; câu không cần ngắt thì không ngắt] |
| Minh họa bằng vật / hành động (fx.visual, L-050) | [ … ] |
| Animation / EFX (motion slug, 1 hiệu ứng chính) | [ … ] |
| SFX nhấn → đúng chữ nhấn | [`sfx` → «chữ»] |
| Chuyển cảnh vào + SFX | [cut / mmx-… + swish / whoosh-soft] |
| Chữ màn hình EN (≤ 8 từ/chunk) | [ … ] |
| Vì sao thể hiện thế này | [ … ] |
| Liên kết với câu/beat trước | [gắn với bước b05, gọi lại từ khóa hook (loop)] |
| Nguồn của claim | — |
| Trạng thái | chưa viết · chưa đọc to · chưa kiểm giọng |

### End card · tĩnh, không thoại
| Ô | Nội dung |
|---|---|
| Giây (dự kiến, chưa đo) | [ … ] |
| Dòng an toàn (nguyên văn) | Thông tin tham khảo, không thay thế tư vấn chuyên gia |
| Credit (câu chuẩn, bắt buộc, không thay) | Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/ |
| Bắt buộc thêm (P-10), cả end card lẫn post.md | Đã chuyển thể. Giấy phép: https://creativecommons.org/licenses/by/4.0/ |
| Nguồn nghiên cứu | Dunlosky et al. 2013 — chỉ nếu C1 thật sự được nói. Không Yang. |
| Chứng thực | Không câu nào ngầm nói tác giả cẩm nang chứng thực kênh |
| Hình / chuyển cảnh + SFX | [ … ] |
| Nhãn AI khi đăng (post.md) | Giọng của Hiệp (nhân vật) … là giọng AI tổng hợp (F5-TTS). (chỉ nêu nhân vật thật sự nói) |

## E2. Bảng hiệu ứng (rule-52, dòng 158–162; phủ mọi beat, duyệt ở gate 1 trước render)
| Beat | Engine | Hiệu ứng / ẩn dụ hình ảnh | Gắn với chữ | SFX nhấn → chữ | Chuyển cảnh vào (+SFX) |
|---|---|---|---|---|---|
| b01 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b02 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b03 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b04 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b05 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b06 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| b07 | [remotion / hyperframes] | [ … ] | «[ … ]» | `[sfx]` → «[ … ]» | [kiểu] (`[sfx]`) |
| end | [ … ] | [ … ] | — | — | [ … ] |
Explainer section: `hits` 1–3 mỗi section, mỗi hit có SFX và chữ. Mức clip: `transition_sfx: {part: "whoosh-soft", scene: "swish"}`. Bảng phải sinh bằng `fx-table.py` theo đúng version đang trình.

## E3. Sơ đồ engagement (rule-56: ≥ 3 kiểu; CTA vẫn chỉ MỘT yêu cầu)
| Kiểu | Beat | Vai trò | Ghi chú |
|---|---|---|---|
| comment-challenge (bắt buộc) | b07 | **Chính là yêu cầu duy nhất của CTA** | [chữ mới; người xem trả lời ngay được] |
| loop (bắt buộc) | b07 | Câu cuối lặp từ khóa hook: `hook_word: [ … ]` | Không phải yêu cầu thứ hai |
| relatable-question | [b02–b04] | Câu đồng cảm giữa clip, không đòi hành động | Có thể trùng ô «móc giữa clip» |
| save-prompt (tùy chọn) | [chỉ ở caption hoặc bình luận ghim, không trong lời CTA] | Tránh thành yêu cầu thứ hai | [ … ] |
| Bình luận ghim | post.md | Nối tiếp comment-challenge | [ … ] |
| Cấm | — | like đi / follow nha / nhớ like / xin follow / thả tim đi | — |

## F. Bảng cặp câu (L-094) — điền sau khi có lời
| Cặp | Câu N (tóm) | Câu N+1 (tóm) | Quan hệ (trả lời / giải thích / đối chiếu / hệ quả) | Nhờ chữ nào | Đạt? |
|---|---|---|---|---|---|
| [ … ] | [ … ] | [ … ] | [ … ] | [ … ] | [ … ] |

## G. Thứ tự kiểm (đọc to TRƯỚC, checker SAU)
1. **Đọc to liền mạch b01 → CTA (L-089), làm ĐẦU TIÊN.** Ghi kết quả bằng lời thường: chỗ vấp, beat nhảy, câu gắn thêm. Chưa có người đọc thật thì ghi «**chưa kiểm**», không ghi «đạt».
2. Nghe một lần là hiểu (L-091), bảng cặp câu (F).
3. Rồi mới chấm luật tay và chạy `check-rules.py --subjects / --l088 / --trend / --flow / --clarity / --link / --repeat / --evidence / --choppy / --fresh <draft.md>`. Dán kết quả thật, không tự ghi «PASS». Cờ ⚠ không thay cho bước 1.
```

**Về giây và số chữ:** W-14 đặt tổng khoảng 140–175 chữ cho cả clip. Mốc giây từng beat và số chữ cho hook chưa chốt. Chỉ có số thật khi đo bằng giọng thật sau «Chốt» (P-12, L-072).

---

## 3. Quy trình kiểm văn nói (đã soạn quy trình trên giấy; CHƯA áp vào lời nào vì mẫu còn trống)

Dùng khi đã có lời. Làm theo thứ tự, bước nào trượt thì sửa xong mới sang bước sau.

0. **Đọc to liền mạch trước tiên (L-089).** Một người đọc thật cả bài b01 → CTA như người xem, trước mọi bước dưới và trước mọi checker. Chưa đọc thật thì ghi «chưa kiểm».

1. **Văn nói hay văn viết.** Gạch mọi từ nối văn viết hoặc học thuật trong danh sách rule-60 (tức là, do đó, vì vậy, tuy nhiên, điều này, hơn nữa, cơ chế…). Gặp câu nào mình sẽ không bao giờ nói với bạn ngoài quán cà phê thì viết lại (script-prompt-principles §4).
2. **Chủ ngữ (W-09, L-071).** Gạch chủ ngữ và động từ của từng câu. Câu thiếu thì nối vào câu trước bằng phẩy, «rồi» hoặc «nên». Không chặt câu để đủ số chữ.
3. **Quan hệ câu (L-089, L-092, L-094).** Điền bảng F. Cặp nào phải giải thích thêm mới nối được thì trượt. Không dùng «Nhưng» hay «Mà» để nối hai chủ đề khác nhau.
4. **Câu cộc — hai ngưỡng khác nhau, không đánh đồng:**
   - *Chữ gốc của lesson L-096 (logs/lessons.md):* ✖ khi 2 câu **dưới 8 chữ** liền nhau, hoặc **quá 30%** số câu dưới 8 chữ.
   - *Checker hiện hành (`check-rules.py --choppy`, News c40e811, ghi ở rule-checklist dòng 178):* không để 2 câu **≤ 10 chữ** liền nhau, và **≤ 30%** câu cộc (ngưỡng News hiệu chỉnh trên r9.2).
   - Ghi kết quả của **cả hai** riêng. Ngưỡng ≤ 10 chữ chặt hơn ở luật «hai câu liền nhau». Nếu hai ngưỡng cho kết quả khác nhau, báo Rule Reviewer, không tự chọn một.
5. **Từ đời thường (P-03, rule-58, L-091).** Bỏ từ Hán Việt hiếm, từ văn chương, từ mơ hồ («trôi», «mọi thứ», «một cảm giác»), ẩn dụ thay cho nghĩa thẳng. Tìm từ sắc hơn bằng `pipeline/scripts/vn-words.py`.
6. **Không chê người học (P-07, L-053).** Chỉ chê cách làm.
7. **Nhấn (P-08, L-031).** Mỗi beat 1–2 chữ nhấn, đặt ở chữ gánh ý. Nhấn bằng âm lượng, không bằng cách chèn lặng.
8. **Ngắt (W-08, W-17, L-070).** Chỉ ngắt ở dấu câu hoặc ranh giới cụm nghĩa. Không ngắt giữa số và danh từ, giữa động từ và tân ngữ ngắn, hay giữa tên riêng. Ghi ký hiệu `/` (phẩy), `//` (chấm/hỏi), `//|` (hết beat). Câu không cần ngắt thì không thêm ngắt, kể cả trước trạng ngữ.
9. **Câu hỏi và điều kiện nói với người xem (W-10).** Mở mềm bằng «giả sử», «thử», «lỡ như»…, không mở bằng câu lệnh trơ.
10. **Ngôi nhất quán (L-089).** Một ngôi «bạn» từ b01 tới b07. Không chèn câu «Mình cần…» ở beat mục tiêu.

**Hai cặp minh họa chung (KHÔNG phải nội dung clip-05, không chứa claim):**
| Văn viết | Văn nói |
|---|---|
| «Do thời gian hạn chế, việc rửa chén thường bị trì hoãn.» | «Tối nào về mình cũng mệt, nên mình cứ hẹn mai mới rửa chén.» (vế nào cũng có chủ ngữ «mình», nối bằng «nên», từ đời thường) |
| Ngắt sai: «Mình cứ hẹn `/` mai mới rửa chén.» (ngắt chen vào giữa câu ngắn, không cần) | Không ngắt: «Mình cứ hẹn mai mới rửa chén.» (câu ngắn, đọc liền một hơi) |

**Diễn tập đọc thử:** chỉ được ghi «đã đọc thử» khi có người thật sự đọc. Không có audio thì cột giọng ghi «chưa kiểm». **Trong lượt này mình không đọc thành tiếng, không nghe, không đo thời lượng, không tạo audio.**

---

## 4. Bảng trạng thái
| Hạng mục | Trạng thái |
|---|---|
| Bài học kỹ thuật (§1) | Xong, có nguồn và nhãn Q/S/Luật |
| Mẫu trống (§2) | Xong bản r2: đủ cột W-04, bảng hiệu ứng rule-52, hook + hook_alt, ô giữ người xem, engagement rule-56, end card P-10. Chưa có lời |
| Quy trình kiểm văn nói (§3) | Đã soạn quy trình trên giấy, **chưa áp vào lời nào** |
| Fact C1 (Dunlosky, đối chiếu xếp hạng) | Phạm vi do Deep chọn, Reviewer chuyển 14:09. Mình không tự kiểm |
| Bridge C | Deep: nối có điều kiện (d673dd9). Social: nguồn đủ cho bối cảnh, không đủ gọi hot (bd53fd3). **Chưa thấy kết luận của Rule Reviewer về độ tự nhiên** |
| trend_id cho bridge C | `texthip-kr-reading-lifestyle-znews-1693810` (ID nội bộ Social, không phải nhãn hot) |
| example_evidence | Chỉ Lee Yunjee, chỉ là bối cảnh. Ví dụ chính trong lời là **MINH HỌA BIÊN TẬP CỦA KÊNH**. Addendum metadata chưa SHA, chưa sync |
| Trùng mục 23.14 với clip-04 | **Rủi ro**, cần khai callback và đổi hẳn tình huống |
| Đọc to bằng người thật | **Chưa kiểm** |
| Kiểm bằng giọng thật / TTS | **Chưa kiểm** (cấm trước «Chốt», P-12) |
| Đo thời lượng | **Chưa đo** |
| check-rules | Chưa chạy (chưa có lời) |
| L-097 trong lessons / checklist | Working tree, chưa commit |

## 5. Checklist bàn giao trước khi viết lời
- [x] Hiệp chọn hướng C (Reviewer chuyển 14:05).
- [x] Đọc fact nền b02dd07 (dòng 22–28), fact bridge d673dd9, trend bridge bd53fd3.
- [x] Đọc hook/CTA cũ của clip-05 (v1–v10, review r10.2), clip-03, clip-04 (v18 LOCKED và script-final) → danh sách tránh trong file concept.
- [x] Chuẩn bị 3 concept một dòng: `/workspace/opencreator-clip05-concept-prep-2026-11-07.md`.
- [x] Social cấp trend_id và example_evidence (Reviewer chuyển 14:14). Addendum JSON ngoài repo, chưa SHA, chưa sync. Không chờ ví dụ trend không tồn tại.
- [x] Concept 2 «Bài đọc để làm theo» do Reviewer chọn 14:14; X-08 không còn blocker (thông tin chuyển).
- [x] Bản nháp hiện hành r11.1: `/workspace/opencreator-clip05-script-r11.1-draft-2026-11-07.md` (r11 CHƯA ĐẠT; r11.1 173 chữ, chưa review lại; đọc to CHƯA KIỂM).
- [ ] Rule Reviewer chấm r11.1 (manual gates L-089/L-090/L-091/L-094/L-095/L-096) và độ tự nhiên của bridge.
- [ ] Viết lời vào mẫu §2, đọc to trước, rồi mới chạy checker, gửi Rule Reviewer. Không gửi Hiệp.
- [ ] Không voice/render trước khi Hiệp nói «Chốt».
