---
title: "Trend digest 2026-10-28"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-28
type: trend-digest
status: draft-needs-review
updated: 2026-10-28
tags: [trends, digest, daily]
date: 2026-10-28
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-28 (Thứ Tư)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 13). **X MCP: có chạy**, trends VN 19 (“Thứ 4/Thứ Tư”, “Chào/Sáng”, phim Thái, K-pop; chỉ móc giờ là dùng được) + worldwide 14 (bóng đá, show Mỹ; bỏ hết) + 30 story X News (3 query: productivity habits, AI at work, Gen Z Vietnam; max_age 72h) → `x-extra.json` 63 mục. Đã bỏ story chính trị (bầu cử Mỹ, Trump/Ventura), ADHD (nhãn chẩn đoán), phát ngôn bộ trưởng Ấn Độ, AGI làm lương về 0.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 445 thô → 428 cụm; raw.json 428 mục (335 ok · 20 caution · 73 drop, gồm 31 drop tay) → 355 qua lọc. Chấm tay 15 mục. Drop tay: chính trị, tội phạm/rửa tiền, tôn giáo, bi kịch, bệnh, scandal ngoại tình/showbiz, nhãn y khoa (ADHD, ferritin face), nỗi sợ mất việc vì AI.
Dữ liệu: `collect.json`, `x-extra.json`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc; bỏ mục heuristic lạc đề như thể thao Mỹ “winning habits”, iMac M6, mỏ đá Pháp)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | “Đợt lạnh”: Google Trends VN 2000+; miền Bắc dự báo se lạnh sáng/đêm khoảng 1–2/11 | 0.765 | 1.0 / 0.0 | [Google Trends VN](https://trends.google.com/trends/explore?geo=VN&q=%C4%91%E1%BB%A3t%20l%E1%BA%A1nh), [SK&ĐS 28/10](https://nc23.cnnd.vn/chi-tiet-dot-khong-khi-lanh-sap-toi-o-mien-bac-169261028061923102.htm), [Tiền Phong](https://tienphong.vn/mien-bac-bao-gio-chuyen-lanh-post1888876.tpo) | 3.5 (clip-07) | LIGHT |
| 2 | “Giải mã thói quen tự cản trở bản thân” (self-sabotage, theo Washington Post) | 0.627 | 1.0 / 0.15 | [VnExpress](https://vnexpress.net/giai-ma-thoi-quen-tu-can-tro-ban-than-5137355.html) | 4.9 + 4.7 (callback clip-02) | DARK |
| 3 | Lịch làm việc của Ian Fleming: hai khối viết mỗi sáng, chiều nghỉ (X News, số liệu chưa tự kiểm) | 0.433 | 1.0 / 0.0 | [X News](https://x.com/i/trending/2114965888676036940) | 3.13 (clip-12), caution | DARK |
| 4 | “Đừng bao giờ khinh thường một bông hoa chưa nở” (ngày 3) | 0.362 | 0.5 / 0.4 | [Kenh14 qua Google News](https://kenh14.vn/trend-dung-bao-gio-khinh-thuong-mot-bong-hoa-chua-no-oanh-tac-mxh-nhin-anh-truoc-va-sau-moi-hieu-cau-noi-nay-215261026165945031.chn) | 4.12 (clip-06, đang làm) | DARK |
| 5 | Phòng trọ 12m² của cô gái lương 11 triệu “không muốn sống tạm bợ” | 0.336 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/can-phong-tro-12m2-cua-co-gai-luong-11-trieu-thang-khong-muon-song-tam-bo-215261025211956159.chn) | chưa có mục khớp; caution tiền | — |
| 6 | “Người rất thành công có cần sở thích ngoài công việc?” | 0.315 | 1.0 / 0.0 | [X News](https://x.com/i/trending/2115137233048985805) | 22.x (thư giãn), cần Deep Research | — |
| 7 | Lịch nghỉ dịp lễ cuối cùng của năm 2026 (mốc cuối năm) | 0.254 | 1.0 / 0.1 | [Dân Trí](https://dantri.com.vn/noi-vu/lich-nghi-dip-le-cuoi-cung-cua-nam-2026-20261027194815581.htm) | P05 mốc mùa | — |
| 8 | Thứ Hai mệt rũ, social jetlag (ngày 3) | 0.184 | 0.5 / 0.47 | [X News](https://x.com/i/trending/2114686643084935556) | 3.2 (clip-14) | DARK |
| 9 | Cất bằng đại học đi học nghề | 0.18 | 1.0 / 0.0 | [VnExpress](https://vnexpress.net/cat-bang-dai-hoc-di-hoc-nghe-5136998.html) | 31.x, chưa map | — |
| 10 | Brain stacking (ngày 4, bão hoà) | 0.128 | 0.25 / 0.97 | [Mashable qua Google News](https://news.google.com/rss/articles/CBMicEFVX3lxTE1tM0ZtalhsQ2Q5S2ZFVm84cGNZZ1hCMjNzWURKaXVhLXcydnVvVEJJMGhtNS1JQTNEUC1qclZ6Y0dGb1oyUE85MnlPZVYxMEFhakduZ1NOc0tXb2FKNzVDbVlpMG1CTmRzdkZLQ2ZGNzA?oc=5) | 3.1 (clip-08, stub 26/10) | DARK |

Đã xem và bỏ: ADHD habits/hyperfocus (nhãn chẩn đoán), Gen Z “thriving” thấp kỷ lục (gắn trầm cảm/thất nghiệp), Millennials burnout (caution, dễ thành than thở), AI tạo/mất việc (bão hoà + nỗi sợ mất việc), BIGBANG/AHOF (người nổi tiếng), mưa lớn miền Trung (thiên tai).

## TikTok signals
Không có dữ liệu Apify hôm nay. Proxy tin tức, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| “Đừng bao giờ khinh thường một bông hoa chưa nở” | Google News “trend TikTok” (Kenh14) | vẫn còn trong feed ngày 3 | ok nếu bỏ phần ngoại hình | B-bonghoa-01 (clip-06) |
| Brain stacking | Google News US “TikTok trend” (Mashable, The Hill) | ngày 4, The Hill hỏi “có đảo ngược brain rot?” | ok | B-brainstack-01 (clip-08) |
| “Ferritin face” | Google News US (Cosmopolitan, Independent) | trend sức khoẻ | drop (claim y khoa) | — |

## Learning
- Không thêm P-row. P03/P04/P05/P10/P12 +1 (patterns.md).
- Mới: tín hiệu mùa “đợt lạnh” là móc thời điểm tốt cho buổi sáng (P05+P12), hợp clip LIGHT.
- Bão hoà nên tránh: brain stacking (sat 0.97), AI ở chỗ làm, thứ Hai mệt mỏi (ngày 3). ADHD tiếp tục xuất hiện trên X nhưng luôn bỏ vì là nhãn chẩn đoán.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-dotlanh-01 | đợt lạnh | sáng se lạnh, kéo chăn tới cổ, lướt hết nhóm công việc rồi mới dậy | 3.5 | "Miền Bắc sắp se lạnh rồi. Sáng mai thử ra khỏi chăn trước, rồi mới mở tin nhắn, mà mở đúng ba lần trong ngày thôi." (P12+P05) | empathy / data | clip-07 (3.5) | LIGHT |
| B-tucantro-01 | tự cản trở bản thân | bìa hồ sơ nằm trên bàn cả tuần, tối thứ Năm vẫn chưa mở | 4.9 + 4.7 | "Bạn biết hạn nộp giấy tờ là thứ Sáu, vậy mà tới tối thứ Năm vẫn chưa dám mở cái bìa hồ sơ ra?" (P10+P03) | contrarian / empathy | ý tưởng mới (callback clip-02) | DARK |
| B-fleming-01 | lịch làm việc Ian Fleming | ngồi bàn mười tiếng mà chẳng xong trang nào | 3.13 (+3.5) | "Người viết mười bốn cuốn James Bond chỉ làm việc hai khối mỗi sáng. Còn bạn ngồi bàn mười tiếng thì xong được mấy trang?" (P10+P04) | contrarian / data | clip-12 (3.13) hook thay thế | DARK |

Cầu nối về trục kênh (rule 26/10): cả ba chỉ dùng trend làm cái móc ở hook; thông điệp là một việc nhỏ làm được hôm nay (ra khỏi chăn trước khi mở tin nhắn · mở việc ra năm phút · làm theo khối rồi nghỉ).

## Differentiation
- **B-dotlanh-01** — Mọi người đang nói: khi nào miền Bắc chuyển lạnh, mấy độ, mặc gì ([SK&ĐS](https://nc23.cnnd.vn/chi-tiet-dot-khong-khi-lanh-sap-toi-o-mien-bac-169261028061923102.htm), [Tiền Phong](https://tienphong.vn/mien-bac-bao-gio-chuyen-lanh-post1888876.tpo)). Góc của mình: cái lạnh làm mình nằm lì trong chăn và việc đầu tiên tay làm là mở tin nhắn; ra khỏi chăn trước, gom tin nhắn vào ba khung giờ.
- **B-tucantro-01** — Mọi người đang nói: tự cản trở là do nỗi sợ sâu xa, hãy nhận diện và quan sát suy nghĩ ([VnExpress](https://vnexpress.net/giai-ma-thoi-quen-tu-can-tro-ban-than-5137355.html)). Góc của mình: không cần đào nỗi sợ trước, mở việc ra đúng năm phút; khi việc có hình hài, nỗi sợ tự nhỏ lại.
- **B-fleming-01** — Mọi người đang nói: ngưỡng mộ lịch sống cân bằng nhiệt đới ([X News](https://x.com/i/trending/2114965888676036940)). Góc của mình: bí mật không phải biển Jamaica mà là làm theo khối có giờ dừng; quá nhiều giờ thì giờ thêm ra ít giá trị (3.13).

## Plan stubs
- `plans/plan-1-dot-lanh-gom-tin-nhan.json` — ✔ validate 9 scenes, 59.00s (stub-needs-approval). Trend ở b01 (L-084: chăn, trời se lạnh). Ví dụ đời thường (chăn, nhóm công việc, rửa mặt), không môn học (L-087, check-rules --subjects PASS).
- `plans/plan-2-tu-can-tro-nam-phut.json` — ✔ validate 9 scenes, 57.00s (stub-needs-approval). Ví dụ giấy tờ cần nộp; bỏ chuyện bệnh, cai nghiện, tình cảm trong bài gốc.
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact, Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Miền Bắc sắp se lạnh rồi. Sáng mai thử ra khỏi chăn trước, rồi mới mở tin nhắn, mà mở đúng ba lần trong ngày thôi." (B-dotlanh-01, clip-07, LIGHT)
2. "Bạn biết hạn nộp giấy tờ là thứ Sáu, vậy mà tới tối thứ Năm vẫn chưa dám mở cái bìa hồ sơ ra?" (B-tucantro-01, DARK)
3. "Người viết mười bốn cuốn James Bond chỉ làm việc hai khối mỗi sáng. Còn bạn ngồi bàn mười tiếng thì xong được mấy trang?" (B-fleming-01, clip-12, caution)

## Safety notes
- B-dotlanh-01: chỉ dùng sáng se lạnh; không nhắc mưa lớn/lũ miền Trung. Thời điểm lạnh (1–2/11) là dự báo, clip không hứa ngày cụ thể.
- B-tucantro-01: bài gốc có chuyện sa sút trí tuệ, cai nghiện, phản bội; không dùng phần nào.
- B-fleming-01: người nổi tiếng đã mất, góc trung tính; bỏ chi tiết rượu; “14 cuốn”, “2.000 chữ” chỉ từ tóm tắt X, chưa tự kiểm, Deep Research phải kiểm trước khi dùng.
- Mưa lớn Trung Bộ, chính trị, ADHD, ferritin face: bỏ.
