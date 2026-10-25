---
title: "Trend digest 2026-10-25"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-25
type: trend-digest
status: draft-needs-review
updated: 2026-10-25
tags: [trends, digest, daily]
date: 2026-10-25
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-25 (Chủ nhật)

**Nguồn:** 31/36 collector. Lỗi: vnexpress-moi (SSL EOF), tinhte (HTTP 521), kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 10). X MCP: trends VN 20 (“Chủ Nhật”, “Chào/Sáng”, phim Thái, coin; chỉ “Chủ Nhật” dùng làm móc giờ) + worldwide 20 (anime Nhật, bóng đá, bầu cử Brazil; không dùng) + 15 story X News (3 query: productivity habits, AI at work, Vietnam gen Z; max_age 72h; đã bỏ 9 story chính trị/bầu cử, biểu tình, cần sa, chủng tộc, thuốc lá, sa thải OpenAI, trẻ trị liệu tâm lý) → `x-extra.json` 55 mục.
**Apify TikTok-native: vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, 1 hashtag + 1 query, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Số dư y như 22/10 → chu kỳ chưa reset. Không run id, 0 clip. Theo quyết định 22/10 của Hiệp: chờ chu kỳ mới, không nâng gói. Xem `apify/README.md`.
**Số lượng:** collector 409 thô → 394 cụm; raw.json 394 mục (329 ok · 15 caution · 50 drop) → 344 qua lọc. Chấm tay 15 mục; drop tay 10 (chuyện hôn nhân/chia tay người nổi tiếng ×4, công an/chính quyền ×2, chính trị ×1, phá cửa “door kick challenge” ×1, coin ×2).
Ghi chú: job 23/10 và 24/10 không chạy ra digest (run lỗi), nên không có file cho hai ngày đó.
Dữ liệu: `collect.json`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc; bỏ mục heuristic lạc đề như Bluesky game, BBC lão hoá, “Advent grind”)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Nghỉ việc làm riêng: nuôi side project 1 tiếng/ngày tới khi bằng 60% lương | 0.736 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2113685619998372109) | 12.18 bán trước rồi mới làm (B) | DARK |
| 2 | “Kiên trì 6 tháng, khó thì làm ít lại” | 0.561 | 1.0 / 0.23 | [X News](https://x.com/i/trending/2113963042178257128) | 4.12 thói quen tính theo tháng (callback clip-06) | DARK |
| 3 | Trì hoãn hại sức khoẻ (SCMP) | 0.338 | 1.0 / 0.20 | Google News (SCMP) | 4.9 (đã dùng ở clip-02, chỉ callback) | — |
| 4 | Dân X kể chuyện ngủ: ngày nghỉ nằm 13 tiếng + trend VN “Chủ Nhật” | 0.327 | 0.33 / 0.42 | [X News](https://x.com/i/trending/2114005059952324691) | 3.2 cố định giờ dậy cả cuối tuần (B) | DARK |
| 5 | Gen Z “học cách nói không” | ~0.3 | 1.0 / 0.20 | Google News (Hà Nội TV) | 3.16 bớt quan hệ làm mình cạn sức (C) | — |
| 6 | Gen Z ngại nghe điện thoại nơi công sở | ~0.2 | 1.0 / 0.10 | Google News (Nhân lực Nhân tài) | chưa có mục khớp rõ (3.5 lỏng) | — |
| 7 | Vợ chồng 60 tuổi sống 8 năm trong 65m² mà luôn gọn | ~0.2 | 1.0 / 0.10 | [Kenh14](https://kenh14.vn/cap-vo-chong-tuoi-60-song-trong-can-ho-65m-suot-8-nam-nha-khong-lon-nhung-luc-nao-cung-gon-gang-ngan-nap-21526102419181736.chn) | 4.10 để đồ cần gần, đồ không muốn đụng xa | LIGHT |
| 8 | Gmail có thể bị dùng cho quảng cáo (chính sách mới của Google) | ~0.2 | 1.0 / 0.10 | [Ars](https://arstechnica.com/gadgets/2026/10/updated-google-privacy-policy-says-your-gmail-might-be-used-for-advertising/) | phần 14 — chưa đối chiếu mục; caution thương hiệu | — |
| 9 | “Thờ năng suất mệt quá” (phản ứng văn hoá năng suất) | ~0.2 | 1.0 / 0.30 | [Bluesky](https://bsky.app/profile/fearjunkie.bsky.social/post/3mygcgc76g22q) | 3.13 (callback B-49h-01) | — |
| 10 | Đọc nhiều có giúp viết hay hơn? | ~0.2 | 1.0 / 0.20 | [X News](https://x.com/i/trending/2113344436113473964) | 23.14 tự kiểm (callback clip-04) | — |

Đã xem và bỏ: AI ở chỗ làm (5 story, ngày 12, bão hoà), traders kỷ luật (ngày 10), Gen Z vs millennial mua nhà (số Mỹ, caution), Gallup Gen Z 44% (sức khoẻ tinh thần, không bridge), iPhone Duo nứt màn hình (ngày 6, thương hiệu), concert BIGBANG (người nổi tiếng).

## TikTok signals
Không có dữ liệu Apify hôm nay (vẫn hết hạn mức). Proxy tin tức: Google News “trend TikTok” (Teen Vogue anti-blush, “I'm So Sorry” transformation, “Brutus” sound; không khớp kênh), Gen Z “học cách nói không”. Không có view/comment/transcript nên không xếp hạng.

## Learning
- **Tiền và sự nghiệp quay lại:** tín hiệu mạnh nhất là tranh luận “chừng nào nghỉ việc làm riêng”. Lần đầu bridge vào phần 12 (khởi nghiệp), dùng mục 12.18 vì không dính luật Trung Quốc (12.1 là luật TQ, bỏ).
- **Chủ nhật là móc giờ:** trend VN “Chủ Nhật” + story ngủ bù ngày nghỉ → hợp đăng sáng Chủ nhật cho 3.2.
- Pattern: P03 +2, P10/P12/P13/P08 +1. Không thêm P-row.
- **Bão hoà, tránh góc thẳng:** AI ở chỗ làm (ngày 12), trading (ngày 10), giấc ngủ chung chung (chỉ còn góc cuối tuần 3.2), iPhone Duo (ngày 6).

## Bridges (khác biệt)
| id | Trend → khoảnh khắc | Bài học | Mọi người đang nói | Góc của mình | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|---|
| B-bantruoc-01 | #1 → ôm ý tưởng cả năm, tin làm ra rồi sẽ có người mua | 12.18 (B) | Nuôi side project 1 tiếng/ngày tới 60% lương rồi mới nghỉ ([X News](https://x.com/i/trending/2113685619998372109)) | Câu “chừng nào nghỉ” đến sau. Trước hết phải biết có ai chịu trả tiền chưa: một trang giới thiệu, vài chục người đặt trước hoặc mua đơn nhỏ. Thử nghiệm ngẫu nhiên 116 startup Ý (Camuffo 2020): nhóm kiểm bằng phản hồi thị trường làm ăn tốt hơn, đổi hướng kịp hơn, không bỏ sớm hơn | "Bạn tính nghỉ việc để làm riêng, vì tin rằng làm ra rồi thì sẽ có người mua, đúng không?" (P10+P03) | contrarian / data | DARK | ý tưởng mới |
| B-weekend-02 | #4 → Chủ nhật nằm tới trưa, tối trằn trọc, thứ Hai nặng trịch | 3.2 (B) | Ngày nghỉ cứ ngủ bù cho đã ([X News](https://x.com/i/trending/2114005059952324691)) | Ngủ nướng đẩy đồng hồ sinh học lùi như lệch múi giờ (61 SV, nhóm thất thường trễ ~2,5 tiếng; Phillips 2017). Giữ giờ dậy, muốn bù thì tối ngủ sớm hơn | "Chủ nhật bạn tính ngủ tới trưa cho bù, vậy mà sao sáng thứ Hai còn mệt hơn?" (P12+P03) | data / contrarian | DARK | clip-14 hook thay thế |
| B-6thang-01 | #2 → nghe “kiên trì 6 tháng”, tuần hai vẫn khó là muốn bỏ | 4.12 (B) | Kiên trì 6 tháng sẽ ra kết quả ([X News](https://x.com/i/trending/2113963042178257128)) | Không có con số chung: 18 tới 254 ngày tuỳ người và tuỳ việc, lỡ một ngày không về 0 (Lally 2010) | "Ai cũng nói kiên trì sáu tháng. Vậy tuần thứ hai thấy vẫn khó, bạn có nghĩ mình thất bại không?" (P03+P08) | data / empathy | DARK | củng cố clip-06 |
| B-noikhong-01 | #5 → ai nhờ cũng gật, tối về hết sức | 3.16 (C) | Gen Z học cách nói không (Google News) | Mức C, mẫu đặc biệt (phụ nữ goá 60–89 tuổi); chỉ dùng phụ cho B-nhanviec-01 | "Ai nhờ gì bạn cũng gật, rồi tối về chẳng còn sức làm việc của mình?" (P10) | empathy | — | phụ B-nhanviec-01 |

## Differentiation
- **B-bantruoc-01** — Mọi người đang nói: chờ side project tới 60% lương rồi mới nghỉ ([X News](https://x.com/i/trending/2113685619998372109)). Góc của mình: đo bằng tiền người lạ chịu trả trước, không bằng lời khen của bạn bè.
- **B-weekend-02** — Mọi người đang nói: ngày nghỉ nằm 13 tiếng cho bù ([X News](https://x.com/i/trending/2114005059952324691)). Góc của mình: ngủ bù tới trưa chính là thứ làm thứ Hai mệt; bù bằng giờ đi ngủ, không bằng giờ dậy.

## Plan stubs
- `plans/plan-1-ban-truoc-roi-moi-lam.json` — ✔ validate 9 scenes, 53.00s (stub-needs-approval; tài chính/kinh doanh → dòng “Thông tin tham khảo, không thay thế tư vấn chuyên gia” ở beat cuối, cần Hiệp duyệt trước khi xuất; không nêu số % vì sách ghi chưa kiểm).
- `plans/plan-2-chu-nhat-ngu-toi-trua.json` — ✔ validate 9 scenes, 53.00s (stub-needs-approval).
- Thứ tự vấn đề → nguyên nhân có bằng chứng → mục tiêu → giải pháp → kết quả → CTA; câu đầy đủ chủ ngữ. Chuyện thật của Hiệp để `[CẦN HIỆP XÁC NHẬN]`. Kịch bản thật do OpenCreator Studio viết, Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Bạn tính nghỉ việc để làm riêng, vì tin rằng làm ra rồi thì sẽ có người mua, đúng không?" (B-bantruoc-01)
2. "Chủ nhật bạn tính ngủ tới trưa cho bù, vậy mà sao sáng thứ Hai còn mệt hơn?" (B-weekend-02)
3. "Ai cũng nói kiên trì sáu tháng. Vậy tuần thứ hai thấy vẫn khó, bạn có nghĩ mình thất bại không?" (B-6thang-01)
4. "Ai nhờ gì bạn cũng gật, rồi tối về chẳng còn sức làm việc của mình?" (B-noikhong-01)

## Safety notes
- B-bantruoc-01: chủ đề tiền/kinh doanh → dòng an toàn + Hiệp duyệt; không khuyên nghỉ việc hay không; không nêu tên Justin Welsh trong clip.
- B-weekend-02: không dùng số “6 giờ 34 phút” và “một phần ba người Mỹ” của X (không có trong sách).
- Gmail/Google privacy: caution thương hiệu, chưa đối chiếu mục phần 14; chưa bridge.
- Bỏ toàn bộ story chính trị, biểu tình, cần sa, chủng tộc, tâm lý trẻ vị thành niên.
