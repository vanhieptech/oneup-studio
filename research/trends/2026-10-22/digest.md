---
title: "Trend digest 2026-10-22"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-22
type: trend-digest
status: draft-needs-review
updated: 2026-10-22
tags: [trends, digest, daily]
date: 2026-10-22
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-22

**Nguồn:** 34/36 collector (wiki-vi + wiki-en HTTP 404, ngày thứ 9 liên tiếp). X MCP: trends VN 20 (lời chào “Thứ 5/Sáng”, Thái/K-pop, coin; không dùng) + worldwide 20 (NBA, game, chính trị Brazil; không dùng) + 17 story X News (3 query: productivity habits, AI at work, Vietnam gen Z; max_age 72h; đã bỏ 5 story chính trị/biểu tình) → `x-extra.json` 57 mục.
**Apify TikTok-native: KHÔNG CHẠY ĐƯỢC.** `clockworks/tiktok-scraper` bị từ chối 2 lần: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run” (gói free hết hạn mức). Không run id, 0 clip, fields coverage không có. Xem `apify/README.md`. Hôm nay không có bảng TikTok signals thật; tín hiệu TikTok chỉ là proxy tin tức (Google News “trend TikTok”, Kenh14).
**Số lượng:** collector 460 thô → 440 cụm; raw.json 440 mục (364 ok · 20 caution · 56 drop) → 384 qua lọc. Chấm tay 15 mục; drop tay 6 (tai nạn trẻ em, bệnh nặng người thật, công an, 2 tin y khoa, thầu doanh nghiệp).
Dữ liệu: `collect.json`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc; bỏ mục heuristic lạc đề như golf/NBA “habits”)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Sếp hỏi “Em có thể nhận thêm việc không?” — 3 cách từ chối “EQ cao” | 0.747 | 1.0 / 0.10 | [Kenh14](https://kenh14.vn/sep-hoi-em-co-the-nhan-them-viec-khong-3-cach-tu-choi-tuong-mat-long-nhung-thuc-ra-la-bieu-hien-cua-eq-cao-215261020214215741.chn) | 4.4 ước theo lần trước (+3.16 từ chối) | DARK |
| 2 | Kìm giận nơi làm việc mệt như làm thêm một ca | 0.376 | 0.5 / 0.30 | [X News](https://x.com/i/trending/2112572577571115169) | 3.23 cho cơ thể chậm lại (+3.17 rời chỗ) | DARK |
| 3 | Đến sớm, trả lương trước, ngồi chờ thợ tới trễ gần 3 tiếng | 0.270 | 1.0 / 0.00 | [X News](https://x.com/i/trending/2112823806846783530) | 4.4 (phụ) — caution, không nêu tên/quốc gia | — |
| 4 | Làm từ xa vs gắn bó văn phòng (ngày 3) | 0.258 | 1.0 / 0.30 | [X News](https://x.com/i/trending/2113064650589852113) | 4.18 (callback B-commute-01) | LIGHT |
| 5 | ChatGPT khoá cuộc trò chuyện nhạy cảm bằng PIN / Face ID | 0.255 | 1.0 / 0.05 | [Tinh tế](https://tinhte.vn/thread/chatgpt-cho-khoa-cuoc-tro-chuyen-nhay-cam-bang-ma-pin-hoac-face-id.4185675/) | phần 14 (bảo mật tài khoản) — chưa đối chiếu mục | — |
| 6 | “Brain stacking”: trend TikTok kêu gọi đặt điện thoại xuống | 0.228 | 1.0 / 0.35 | Google News (Mashable) | 3.1 (điện thoại bão hoà, chỉ ghi nhận) | — |
| 7 | Nhà ở: boomers vs người trẻ (số Mỹ) | 0.210 | 1.0 / 0.25 | [X News](https://x.com/i/trending/2112994548662317171) | 5.27 (callback, không dùng số Mỹ) | DARK |
| 8 | Mô hình CARE chọn nghề cho Gen Z | 0.184 | 1.0 / 0.00 | Google News (Dân Trí) | phần 31/23 — chưa đối chiếu | — |
| 9 | Thói quen từ tuổi thơ thiếu thốn (ngày 2) | 0.138 | 0.5 / 0.45 | [X News](https://x.com/i/trending/2112284691579486271) | 5.24 | LIGHT |
| 10 | Cày game 14 tiếng: sức tập trung đó dùng cho việc thật được không (ngày 2) | 0.092 | 0.5 / 0.45 | [X News](https://x.com/i/trending/2112259396973772892) | chưa có mục khớp | — |

Đã xem và bỏ: Công viên Lãm Làng hết cảnh nhảy múa (caution, tranh cãi địa phương), “Siêu quà” Doraemon (gắn khuyến mãi), Thần đồng AI / Apple Watch / iPhone Duo (nhân vật, thương hiệu), traders kỷ luật (ngày 8), AI-at-work (ngày 9), các story Gen Z biểu tình/chính trị (drop).

## TikTok signals
Không có dữ liệu Apify hôm nay (hết hạn mức). Proxy tin tức: Mashable “brain stacking” (bỏ điện thoại), Google News “Công viên Lãm Làng”, “Siêu quà Doraemon”. Không có view/comment/transcript nên không xếp hạng.

## Learning
- **Công sở lên ngôi lại:** hai tín hiệu mạnh nhất đều là chỗ làm (nhận thêm việc, kìm giận). Cả hai lật được bằng sách với mức B/A → P03 +2, P10 +2.
- **Hạn mức Apify:** gói free còn $0,1325, không đủ cho một run nhỏ nhất. Cần quyết định trước khi job mai chạy, nếu không mai cũng chỉ có proxy.
- Pattern: P03/P10 +2, P11/P13 +1. Không thêm P-row.
- **Bão hoà, tránh góc thẳng:** AI-at-work (ngày 9), trading (ngày 8), điện thoại (ngày 5), làm từ xa/commute (ngày 3), tiền 5.27 (đã có 3 bridge).

## Bridges (khác biệt)
| id | Trend → khoảnh khắc | Bài học | Mọi người đang nói | Góc của mình | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|---|
| B-nhanviec-01 | #1 → sếp hỏi nhận thêm việc, gật liền vì tưởng hai ngày là xong | 4.4 (B) | 3 cách từ chối khéo, từ chối là EQ cao ([Kenh14](https://kenh14.vn/sep-hoi-em-co-the-nhan-them-viec-khong-3-cach-tu-choi-tuong-mat-long-nhung-thuc-ra-la-bieu-hien-cua-eq-cao-215261020214215741.chn)) | Chưa bàn nhận hay từ chối; cái sai là câu “chắc hai ngày là xong”. Mở lại lần làm việc giống vậy gần nhất rồi mới hứa hạn (Buehler 1994: ước 33,9 ngày, thật 55,5; nhớ lại lần trước → xong đúng hạn 29,3% lên 60,0%) | "Sếp hỏi em nhận thêm việc này được không, bạn gật liền vì nghĩ chắc hai ngày là xong, đúng không?" (P03+P10) | contrarian / data | DARK | ý tưởng mới, gộp B-estimate-02 |
| B-giandiu-01 | #2 → đọc tin nhắn bị chê, muốn gõ trả lời liền hoặc chạy ra ngoài cho hả | 3.23 (A) + 3.17 (B) | Kìm giận mệt như làm thêm ca; hít thở, tự nhủ bình tĩnh ([X News](https://x.com/i/trending/2112572577571115169)) | Lời khuyên quen “đi chạy một vòng cho hạ hoả” gần như không giúp (gộp 154 nghiên cứu, 10.189 người: xả kiểu hưng phấn g = −0,02; làm cơ thể dịu g = −0,63). Úp điện thoại, rời bàn, thở chậm rồi mới trả lời | "Đang tức sếp, bạn xách giày đi chạy một vòng cho hạ hoả, đúng không?" (P03+P10) | contrarian / data | DARK | ý tưởng mới (trụ 2) |
| B-wait-01 | #3 → đến đúng giờ rồi ngồi chờ người khác trễ | 4.4 (phụ) | Chê văn hoá giờ giấc một nước ([X News](https://x.com/i/trending/2112823806846783530)) | Không chê ai; chỉ mượn cảnh chờ, nối vào ước thời gian theo lần trước | "Bạn tới đúng giờ, rồi ngồi chờ thêm ba tiếng. Ai cũng từng vậy, đúng không?" (P10) | empathy | — | phụ B-nhanviec-01 |

## Differentiation
- **B-nhanviec-01** — Mọi người đang nói: từ chối khéo khi sếp giao thêm ([Kenh14](https://kenh14.vn/sep-hoi-em-co-the-nhan-them-viec-khong-3-cach-tu-choi-tuong-mat-long-nhung-thuc-ra-la-bieu-hien-cua-eq-cao-215261020214215741.chn)). Góc của mình: trước câu trả lời có hay không là một con số hạn thật, lấy từ lần trước chứ không từ kế hoạch.
- **B-giandiu-01** — Mọi người đang nói: hít thở, tự nhủ bình tĩnh ([X News](https://x.com/i/trending/2112572577571115169)). Góc của mình: bác cái mẹo phổ biến “chạy một vòng cho hả” bằng bản gộp mức A, giữ lại chạy bộ cho tâm trạng lâu dài.

## Plan stubs
- `plans/plan-1-nhan-them-viec-uoc-lan-truoc.json` — ✔ validate 10 scenes, 57.00s (stub-needs-approval).
- `plans/plan-2-gian-dung-chay-mot-vong.json` — ✔ validate 10 scenes, 54.00s (stub-needs-approval; caution sức khoẻ tinh thần → dòng “Thông tin tham khảo, không thay thế tư vấn chuyên gia” ở beat 9, cần Hiệp duyệt trước khi xuất).
- Thứ tự vấn đề → nguyên nhân có bằng chứng → mục tiêu → giải pháp → kết quả → CTA; câu đầy đủ chủ ngữ. Chuyện thật của Hiệp để `[CẦN HIỆP XÁC NHẬN]`. Kịch bản thật do OpenCreator Studio viết, Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Sếp hỏi em nhận thêm việc này được không, bạn gật liền vì nghĩ chắc hai ngày là xong, đúng không?" (4.4)
2. "Đang tức sếp, bạn xách giày đi chạy một vòng cho hạ hoả, đúng không?" (3.23)
3. "Bạn tới đúng giờ, rồi ngồi chờ thêm ba tiếng. Ai cũng từng vậy, đúng không?" (4.4 phụ)

## Safety notes
- 3.23/3.17: giáp sức khoẻ tinh thần → dòng an toàn bắt buộc, không chẩn đoán; số liệu American Institute of Stress trong story X là số Mỹ, không dùng.
- Story giờ giấc: không nêu tên người nổi tiếng hay quốc gia, không chê văn hoá.
- Nhà ở boomers vs người trẻ: số Mỹ, không dùng làm số VN; không chê thế hệ.
- Apify hết hạn mức: không đổi sang trình duyệt/cookie, không gọi actor bị cấm.
