---
title: "Trend digest 2026-10-26"
source: "pipeline/scripts/trend-collect.py + X MCP extra + web search (Apify unavailable)"
id: trends-2026-10-26
type: trend-digest
status: draft-needs-review
updated: 2026-10-26
tags: [trends, digest, daily]
date: 2026-10-26
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-26 (Thứ Hai)

**Nguồn:** 32/36 collector. Lỗi: vnexpress-moi (SSL EOF), kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 11). Tinh tế đã chạy lại (hôm qua 521). X MCP: trends VN 30 (“Tuần”, “Thứ 2/Thứ Hai”, “Chào/Sáng”, phim Thái, K-pop, coin; chỉ “Thứ Hai” dùng làm móc giờ) + worldwide 29 (bầu cử Brazil, NFL, bóng đá; bỏ hết phần chính trị) + 21 story X News (3 query: productivity habits, AI at work, Gen Z Vietnam; max_age 72h; đã bỏ story cần sa, chủng tộc, sa thải OpenAI, chính sách AI Trung Quốc, bầu cử Mỹ ×2, thuốc lá) → `x-extra.json` 80 mục. Web search bổ sung 4 nguồn cho “brain stacking”.
**Apify TikTok-native: vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap` + query `productivity tips`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Số dư y như 22/10 và 25/10 → chu kỳ chưa reset. Không run id, 0 clip. Theo quyết định 22/10 của Hiệp: chờ chu kỳ mới, không nâng gói. Xem `apify/README.md`.
**Số lượng:** collector 442 thô → 423 cụm; raw.json 423 mục (335 ok · 25 caution · 63 drop) → 360 qua lọc. Chấm tay ~45 mục (gồm cụm AI ở chỗ làm và cụm chính trị Brazil); drop tay: tôn giáo ×2, bạo lực học đường, quy định phạt mạng xã hội, bệnh ung thư, chuyện hủy hôn người nổi tiếng, TikToker “đu rào” concert, địa chính trị chip.
Dữ liệu: `collect.json`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc; bỏ mục heuristic lạc đề như doanh thu 6K Additive, năng suất Canada, OECD)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Lương 15 triệu, cặp đôi Hà Nội chọn căn 9 triệu thay vì 6,5 triệu: cộng phí phát sinh và quãng đi làm | 0.693 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/luong-15-trieu-thang-cap-doi-o-ha-noi-chon-thue-nha-9-trieu-thay-vi-can-65-trieu-dang-sau-la-mot-phep-tinh-khac-215261025112024785.chn) | 4.18 đặt thời gian đi làm lên trước (B, sách ghi tranh cãi) | DARK |
| 2 | “Brain stacking”: xếp chồng sách, sudoku, nhật ký thay cho lướt điện thoại (ngày 2, 5 nguồn) | 0.606 | 0.5 / 0.35 | [Mashable](https://in.mashable.com/digital-culture/115269/what-is-brain-stacking-tiktoks-latest-trend-wants-you-to-put-down-your-phone), [Essence](https://girlsunited.essence.com/shopping/lifestyle/brain-stacking/), [HerCampus](https://www.hercampus.com/school/wvu/brain-stacking-is-this-what-our-minds-have-been-missing/) | 3.1 điện thoại ra khỏi tầm mắt (B) + 4.10 | DARK |
| 3 | 4 tiếng cho sở thích, việc vặt 90 giây để mấy ngày | 0.415 | 1.0 / 0.10 | [X News](https://x.com/i/trending/2114205407518576998) | 4.9 (callback clip-02); caution: nhãn ADHD | — |
| 4 | “Kiên trì mỗi ngày” (ngày 2) | 0.370 | 1.0 / 0.20 | [X News](https://x.com/i/trending/2113963042178257128) | 4.12 (callback clip-06) | — |
| 5 | Nghỉ việc làm riêng: side project tới 60% lương (ngày 2) | 0.292 | 0.5 / 0.40 | [X News](https://x.com/i/trending/2113685619998372109) | 12.18 (stub hôm qua) | — |
| 6 | X VN “Thứ Hai” / “Tuần” sáng đầu tuần | ~0.25 | 1.0 / 0.30 | [X VN](https://x.com/search?q=Th%E1%BB%A9%20Hai) | móc giờ cho 3.2 (B-weekend-02) | — |
| 7 | Đồng nghiệp chèn ép, tranh công: nhịn hay ăn thua đủ | 0.318 | 1.0 / 0.0 | [Kenh14](https://kenh14.vn/dong-nghiep-chen-ep-tranh-cong-nhin-nhuc-hay-an-thua-du-cach-xu-ly-khon-ngoan-de-khong-hao-ton-phuc-khi-su-nghiep-215261025195054466.chn) | 3.17 lỏng (tức thì rời đi) | — |
| 8 | Khi Gen Z làm tổ trưởng | 0.322 | 1.0 / 0.0 | Google News gen Z (TRT Huế) | chưa có mục khớp | — |
| 9 | Giá vàng lao dốc, mua đỉnh đầu tuần lỗ gần 5 triệu/lượng | ~0.2 | 1.0 / 0.10 | [Dân Trí](https://dantri.com.vn/kinh-doanh/gia-vang-lao-doc-nguoi-mua-lo-5-trieu-dongluong-sau-mot-tuan-20261026004141321.htm) | caution: đầu tư, không bridge | — |
| 10 | Đọc nhiều có giúp viết hay hơn? (ngày 3) | ~0.2 | 0.33 / 0.30 | [X News](https://x.com/i/trending/2113344436113473964) | 23.14 (callback clip-04) | — |

Đã xem và bỏ: AI ở chỗ làm (8 story, ngày 13, bão hoà), traders kỷ luật (ngày 11), BIGBANG Hà Nội và K-pop về VN (người nổi tiếng), Gallup Gen Z 44% (sức khoẻ tinh thần), iPhone Duo nứt màn hình (ngày 7, thương hiệu), dev tranh luận AI agent tự merge PR (AI bão hoà).

## TikTok signals
Không có dữ liệu Apify hôm nay (vẫn hết hạn mức). Proxy tin tức, không có view/comment/transcript nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| #brainstack #slowliving #morningroutine | Mashable 21/10, Essence, HerCampus, Zloppy | creator @mandyrulez phổ biến; video gần như không lời, chồng sách + sudoku + ly cà phê; techno-news ghi 80–140k like cho video phổ biến nhất (chưa tự kiểm) | ok | B-brainstack-01 (3.1 + 4.10) |
| “I'm So Sorry” transformation, “Brutus” sound, nấu bacon trong nước | Google News “trend TikTok” | ngày 2, không khớp kênh | ok | không |

## Learning
- **Brain stacking là trend thói quen TikTok-native duy nhất hôm nay** đủ sạch để dùng, lên ngày 2 với 5 nguồn (22/10 mới 1). Góc thẳng (“bỏ điện thoại, đọc sách đi”) đã có trong B-phone-01/02 nên phải lật: chồng sách không quyết định, chỗ để điện thoại mới quyết định.
- **Tiền nhà quay lại** qua Kenh14 (số thật của người thật trong tiêu đề, P04). Lần đầu bridge 4.18 bằng góc tiền thuê, không chỉ góc “đi làm xa”.
- Pattern: P03/P04/P10/P12 +1. Không thêm P-row. Thêm format **F08** (silent brain-stack routine) → bản comic: chồng sách rơi xuống từng cuốn, điện thoại trượt ra khỏi khung.
- **Bão hoà, tránh góc thẳng:** AI ở chỗ làm (ngày 13), trading (ngày 11), giấc ngủ chung chung (chỉ còn góc Chủ nhật/thứ Hai 3.2), iPhone Duo (ngày 7).

## Bridges (khác biệt)
| id | Trend → khoảnh khắc | Bài học | Mọi người đang nói | Góc của mình | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|---|
| B-brainstack-01 | #2 → xếp chồng sách đẹp mà điện thoại vẫn úp ngay bên cạnh | 3.1 (B) + 4.10 (B) | Xếp chồng sách, sudoku, nhật ký cạnh ly cà phê để khỏi lướt ([Mashable](https://in.mashable.com/digital-culture/115269/what-is-brain-stacking-tiktoks-latest-trend-wants-you-to-put-down-your-phone)) | Điện thoại nằm cạnh, dù không chạm, vẫn làm phần trí óc dùng được ít đi (Ward 2017, thí nghiệm với SV). Tối hôm trước cắm sạc điện thoại ở phòng khác, để sẵn sách trên bàn. Không cần mua gì | "Bạn cũng xếp một chồng sách thật đẹp để khỏi lướt điện thoại, vậy mà ngồi năm phút là tay lại mò máy?" (P03+P15) | contrarian / data | DARK | clip-08 (3.1) hook thay thế |
| B-commute-02 | #1 → chọn trọ rẻ hơn một triệu, ngày nào cũng ngồi xe gần cả tiếng | 4.18 (B, tranh cãi) | Giá thuê rẻ chưa chắc rẻ, phải cộng điện nước, phí dịch vụ ([Kenh14](https://kenh14.vn/luong-15-trieu-thang-cap-doi-o-ha-noi-chon-thue-nha-9-trieu-thay-vi-can-65-trieu-dang-sau-la-mot-phep-tinh-khac-215261025112024785.chn)) | Còn khoản không ai ghi vào bảng tính là giờ ngồi xe: mỗi chiều bớt 30 phút thì mỗi tuần có lại khoảng 5 tiếng. Nói thật mục này sách ghi còn tranh cãi, chỉ là một yếu tố để cân | "Bạn chọn căn trọ rẻ hơn một triệu, mà đã tính mỗi ngày mình ngồi xe bao lâu chưa?" (P04+P01) | data / empathy | DARK | ý tưởng mới |
| B-viecvat-01 | #3 → ngồi bốn tiếng với sở thích, email 90 giây để ba ngày | 4.9 (callback clip-02) | Não ADHD hyperfocus việc thích, đơ với việc vặt ([X News](https://x.com/i/trending/2114205407518576998)) | Không gắn nhãn ADHD; trì hoãn là né cảm giác khó chịu, không phải lười (clip-02) | "Bạn ngồi bốn tiếng với sở thích không thấy mệt, mà một việc chín mươi giây thì để tới ba ngày?" (P10) | empathy | — | callback clip-02 |
| B-weekend-02 (nhắc lại) | #6 → sáng thứ Hai nặng trịch | 3.2 (B) | — | Stub hôm qua; trend “Thứ Hai” hôm nay xác nhận móc giờ, hợp đăng tối Chủ nhật hoặc sáng thứ Hai | (giữ hook 25/10) | data | DARK | clip-14 |

## Differentiation
- **B-brainstack-01** — Mọi người đang nói: chồng sách càng đẹp càng dễ bỏ điện thoại ([Mashable](https://in.mashable.com/digital-culture/115269/what-is-brain-stacking-tiktoks-latest-trend-wants-you-to-put-down-your-phone)). Góc của mình: điện thoại úp ngay cạnh chồng sách vẫn ăn bớt sức tập trung; đổi chỗ để điện thoại chứ không cần mua thêm sách.
- **B-commute-02** — Mọi người đang nói: cộng đủ điện nước, phí dịch vụ rồi mới so giá thuê ([Kenh14](https://kenh14.vn/luong-15-trieu-thang-cap-doi-o-ha-noi-chon-thue-nha-9-trieu-thay-vi-can-65-trieu-dang-sau-la-mot-phep-tinh-khac-215261025112024785.chn)). Góc của mình: cộng thêm cả giờ ngồi xe, vì 30 phút mỗi chiều là khoảng 5 tiếng mỗi tuần, và nói rõ bằng chứng còn tranh cãi.

## Plan stubs
- `plans/plan-1-brain-stack-dien-thoai-phong-khac.json` — ✔ validate 9 scenes, 56.00s (stub-needs-approval).
- `plans/plan-2-thue-nha-tinh-gio-di-lam.json` — ✔ validate 9 scenes, 58.00s (stub-needs-approval; tiền nhà → dòng “Thông tin tham khảo, không thay thế tư vấn chuyên gia” ở beat cuối, Hiệp duyệt trước khi xuất; mục sách có ghi tranh cãi, beat 8 nói thẳng điều đó).
- Thứ tự vấn đề → nguyên nhân có bằng chứng → mục tiêu → giải pháp → kết quả → CTA; câu đầy đủ chủ ngữ. Chuyện thật của Hiệp để `[CẦN HIỆP XÁC NHẬN]`. Kịch bản thật do OpenCreator Studio viết, Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Bạn cũng xếp một chồng sách thật đẹp để khỏi lướt điện thoại, vậy mà ngồi năm phút là tay lại mò máy?" (B-brainstack-01)
2. "Bạn chọn căn trọ rẻ hơn một triệu, mà đã tính mỗi ngày mình ngồi xe bao lâu chưa?" (B-commute-02)
3. "Bạn ngồi bốn tiếng với sở thích không thấy mệt, mà một việc chín mươi giây thì để tới ba ngày?" (B-viecvat-01)

## Safety notes
- B-commute-02: chủ đề tiền nhà → dòng an toàn + Hiệp duyệt; không dùng số thời gian đi lại của Trung Quốc trong sách; không nêu tên hai người trong bài Kenh14; nói rõ mục 4.18 còn tranh cãi.
- B-brainstack-01: không nêu tên @mandyrulez trong clip, không chép hình/âm của video gốc; Ward 2017 là thí nghiệm lab với sinh viên, tác động cộng dồn chưa ai đo.
- B-viecvat-01: không dùng nhãn ADHD, không chẩn đoán.
- Giá vàng: caution, không đưa lời khuyên đầu tư. Bỏ toàn bộ story chính trị, bầu cử, cần sa, chủng tộc, bạo lực, bệnh tật.
