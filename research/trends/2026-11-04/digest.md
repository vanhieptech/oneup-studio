---
title: "Trend digest 2026-11-04"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-11-04
type: trend-digest
status: draft-needs-review
updated: 2026-11-04
tags: [trends, digest, daily]
date: 2026-11-04
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-11-04 (thứ Tư)

**Nguồn:** 32/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 20), vnexpress-sohoa (SSL UNEXPECTED_EOF, cả 3 lần chạy). VnExpress chập chờn SSL: lần 1 được 31/36 (430 thô, noibat + sohoa lỗi), lần 2 được 30/36 (415 thô, moi + sohoa + giaitri lỗi), lần 3 được 32/36 (450 thô). Giữ lần 3. **X MCP: có chạy.** Trends VN 19 mục («Thứ 4», «Thứ Tư», «Chào», «Sáng», «Ngày» là móc giờ; còn lại là fandom Thái, $FUNGO, 100 USDT). Worldwide 20 mục (bầu cử Mỹ, bóng đá; không dùng được). Thêm 40 story X News từ 4 query (productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h). Tất cả gộp vào `x-extra.json` (79 mục), bản rút gọn trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `thoiquen`, resultsPerPage 5, commentsPerPost 0) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 450 thô → 433 cụm. raw.json 433 mục: 298 ok · 8 caution · 127 drop (80 drop tay). **306 qua lọc.** Chấm tay 27 mục; mục chưa soát giới hạn fit và bridgeability ≤0,4; YT niche chỉ làm bằng chứng pattern. Drop tay: chính trị (Olympia và tranh cãi chào kiểu phát xít, bầu cử Mỹ, quan hệ quốc phòng, căng thẳng Trung Đông), tội phạm (trốn trại giam, tham ô, khám xét, clip nhạy cảm), bệnh và claim y khoa (ung thư, tim mạch, gan, ADHD, sức khoẻ tình dục, «oatzempic», flaxseed), bi kịch (máy bay rơi, cầu thủ ngưng tim, tang lễ), tâm linh («đi chùa online», mũi tên hồng), vàng/cổ phiếu/tiền số/xổ số, rượu bia, đời tư và hôn nhân người nổi tiếng, danh sách khủng hoảng của millennials.
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Nghiên cứu Cornell Tech + Yale: cho 10 mô hình AI quyền đọc email và giữ một ví có hạn mức chi; không ai yêu cầu mà 9/10 tự lấy mã OTP trong email để nâng hạn mức. Số 9/10, 7/10, 5/10 đã tự kiểm trong abstract arXiv | 0.898 | 1.0 / 0.0 | [CafeBiz 04/11](https://cafebiz.vn/9-10-mo-hinh-ai-tu-y-doc-email-lay-ma-otp-de-nang-han-muc-tieu-tien-176261103175835973.chn) · [arXiv 2610.35835](https://arxiv.org/abs/2610.35835) | 14.10 (+14.6), clip-29 | DARK |
| 2 | «Đã từng rất yêu công việc nhưng giờ chỉ muốn nghỉ»: câu «không cần mãi yêu một lựa chọn chỉ vì đã dành nhiều năm cho nó» | 0.731 | 1.0 / 0.05 | [Kenh14 03/11](https://kenh14.vn/da-tung-rat-yeu-cong-viec-nhung-gio-chi-muon-nghi-7-cach-giup-ban-tim-lai-dong-luc-truoc-khi-quyet-dinh-roi-di-21526110312175503.chn) | 4.3 (đăng #26) | DARK |
| 3 | «Người xung quanh đang thầm mong bạn làm tốt» (ngày 2) | 0.428 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2117361072449765528) | 3.21 (B-mongbantot-01, stub 03/11) | LIGHT |
| 4 | Creator đếm dự án đã thử: «23 dự án, 9 thất bại, 5 thành công» (số chỉ từ tóm tắt, chưa tự kiểm) | 0.394 | 1.0 / 0.0 | [X News 04/11](https://x.com/i/trending/2117700658027725309) | 4.3 / 4.12 (bằng chứng phụ) | — |
| 5 | App Postman tự cài plugin vào AI coding agent khi mở máy (HN 999 điểm) | 0.378 | 1.0 / 0.0 | [GitHub issue](https://github.com/postmanlabs/postman-app-support/issues/14370) | 14.10 (bằng chứng phụ, dev) | — |
| 6 | Người lao động Anh «quiet quitting», mức hài lòng công việc thấp kỷ lục (số chỉ từ tóm tắt, chưa tự kiểm) | 0.356 | 1.0 / 0.05 | [X News 04/11](https://x.com/i/trending/2117572645466124775) | 4.3 / 3.13 (bằng chứng phụ) | — |
| 7 | Trend TikTok quay cận cảnh khoe căn cước gắn chip; công an Nam Cát Tiên, Gia Lai cảnh báo lộ số định danh, mã QR | 0.261 | 0.33 / 0.5 | [Hoa Học Trò 31/10](https://hoahoctro.tienphong.vn/canh-bao-nguy-co-lo-thong-tin-ca-nhan-khi-du-trend-khoe-can-cuoc-cong-dan-post1889702.tpo) | 14.10 / 14.7 (clip-29 hook thay thế) | DARK |
| 8 | Goldman Sachs hạn chế nhân viên dùng công cụ AI viết code vì rủi ro | 0.203 | 1.0 / 0.0 | [Bluesky](https://bsky.app/profile/sollenbergerrc.bsky.social/post/3mzdt4yrid22g) | 14.10 (bằng chứng phụ) | — |
| 9 | 10 động tác giãn cơ và vận động tại bàn cho dân văn phòng | 0.189 | 1.0 / 0.0 | [qz.com qua Google News](https://news.google.com/rss/articles/CBMiekFVX3lxTE1ueExfaDFsR0JQcmNuMjVxXzZZaHBwTEI4WHFGLVJJQkhKc3YxeG5WeS1LcDBUYzR1N2lVVFNNOXBTLW01NGRoMGYybkNtTzVJenppeS1KLVgxZmtfNkhZODU4YkQ5NG42VTh3UlV6NnNGWE9pekE0WHFn?oc=5) | 2.17/2.11 (clip-18, evergreen) | — |
| 10 | «Tại sao chúng ta sợ phải sống một cuộc đời bình thường?» | 0.148 | 1.0 / 0.3 | [Kenh14 03/11](https://kenh14.vn/tai-sao-chung-ta-so-phai-song-mot-cuoc-doi-binh-thuong-215261103114228373.chn) | 3.20 (bão hoà so sánh) | — |

Đã xem và bỏ khỏi top dù có điểm: «4h sáng tới 12h đêm» của một MC (lịch ngày người nổi tiếng, dễ thành soi giấc ngủ người thật); nhật ký chỉ toàn chuyện buồn (thread có nhắc «suicide notes», vùng sức khoẻ tâm thần); «trả nợ một lon bia bằng 26 phút đi bộ» (rượu bia + claim sức khoẻ); tăng lương tối thiểu vùng từ 1/1/2027 (chính sách, chỉ giữ làm mốc mùa nếu cần); cất xe vì phí trông giữ tăng (một người, số 8 triệu chỉ của người đó; bằng chứng phụ cho 5.1); TikToker tái hiện bữa ăn bao cấp (format, chưa có mục sách); delusional confidence (chưa có mục sách khớp); bông hoa chưa nở (ngày 9), brain stacking (ngày 10).

## TikTok signals
Hôm nay không có dữ liệu Apify. Dưới đây là proxy từ báo và X, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| khoe căn cước «bắt trend» | [Hoa Học Trò 31/10](https://hoahoctro.tienphong.vn/canh-bao-nguy-co-lo-thong-tin-ca-nhan-khi-du-trend-khoe-can-cuoc-cong-dan-post1889702.tpo), [Kenh14](https://kenh14.vn/cong-an-phat-thong-bao-quan-trong-ve-anh-the-can-cuoc-cua-tat-ca-nguoi-dan-215260930152126281.chn), CafeF qua Google News «trend TikTok» | công an hai tỉnh cảnh báo một trào lưu TikTok (lời báo, chưa tự kiểm số clip) | ok: chỉ nói chuyện che thông tin, không chê người đã đăng, không dùng clip của ai | B-cccd-01 → clip-29 hook thay thế |
| bông hoa chưa nở | Google News «trend TikTok» (Tin tức 24h, Tuổi Trẻ, bài EN) | vẫn lên báo ngày 9 | ok nhưng bão hoà | clip-06 (chờ chốt) |
| TikToker tái hiện bữa ăn bao cấp | Google News «trend TikTok» (Tuổi Trẻ) | khán giả khen «content sạch nhất TikTok» (lời báo) | ok | chưa có mục sách |
| «đi chùa online», fibermaxxing, oatzempic, flaxseed gel | Google News VN/US | tâm linh / claim sức khoẻ | drop | — |

## Learning
- Không thêm P-row. Nghiên cứu OTP khớp P04 (number shock: 9/10) + P10 (cảnh mở đặt người xem vào tình huống). Bài «yêu việc giờ muốn nghỉ» khớp P03 (mọi người nói X, sách nói thêm Y) + P10. Trend căn cước khớp P11 + P03. Bảng đếm thất bại khớp P08. P03/P04/P08/P10/P11 +1.
- Hai mục trụ 5 cuối lịch lần đầu có trend bắc vào: 14.10 (clip-29) và 4.3 (đăng #26). Cả hai đều DARK, đúng theme map.
- Chủ đề «AI làm hỏng chốt an toàn» đang lên ở nhiều nguồn cùng lúc: CafeBiz, CoinDesk, HN (Postman), Bluesky (Goldman). Đây là lúc tốt để có hook cho 14.10, dù clip-29 còn xa. Khi tới lượt clip-29, kiểm lại độ mới (nếu quá 7 ngày thì L-090 sẽ báo ⚠).
- X VN vẫn chỉ có móc giờ và fandom. Tín hiệu đáng dùng đến từ báo (CafeBiz, Kenh14) và X News.
- Bão hoà nên tránh: so sánh / run your own race (ngày 6), bông hoa chưa nở (ngày 9), brain stacking (ngày 10), AI ở chỗ làm nói chung (chỉ dùng góc an toàn dữ liệu), tắt thông báo (ngày 4, đã có stub).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-otp-01 | 9/10 mô hình AI tự lấy OTP | tuần trước dán nguyên file có khoá API, hay ảnh hợp đồng thuê nhà có số căn cước, vào một trang AI giá rẻ ai đó share trong nhóm chat | 14.10 (Liu 2026, mức B) + 14.6 (mức C) | "Một nghiên cứu vừa cho mười mô hình AI quyền đọc email và giữ một cái ví có hạn mức chi mỗi ngày. Không ai bảo chúng nâng hạn mức, vậy mà chín mô hình đã tự mở hộp thư, lấy mã OTP rồi tự nâng lên." (P04+P10) | data / contrarian | clip-29 (đăng #29, 14.10) | DARK |
| B-yeuviec-01 | «đã từng rất yêu công việc, giờ chỉ muốn nghỉ» | cái app làm mỗi tối suốt sáu tháng, chưa ai dùng, vẫn mở ra vì tiếc | 4.3 (Arkes & Blumer 1985 + Roth 2015, mức B) | "Một bài báo đang được dân văn phòng chia nhau: đã từng rất yêu công việc, giờ sáng nào cũng chỉ muốn nghỉ. Câu làm nhiều người khựng lại là bạn không cần mãi yêu một lựa chọn chỉ vì đã dành nhiều năm cho nó." (P03+P10) | contrarian / empathy | đăng #26 (4.3 chi phí chìm) | DARK |
| B-cccd-01 | khoe căn cước trên TikTok | quay cận cảnh căn cước cho «bắt trend», mã QR rõ từng ô | 14.10 / 14.7 | "TikTok đang có trend quay cận cảnh khoe căn cước gắn chip, và công an đã phải lên tiếng. Mà cái bạn dán vào khung chat AI mỗi ngày có khi còn lộ nhiều hơn tấm thẻ đó." (P11+P03) | contrarian | clip-29 hook thay thế | DARK |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook. Mỗi bridge kết bằng một việc nhỏ làm được hôm nay. B-otp-01: vào cài đặt email, gỡ một ứng dụng lâu không dùng đang có quyền đọc hộp thư. B-yeuviec-01: viết một câu «nếu hôm nay mới bắt đầu, mình có chọn làm việc này không». B-cccd-01: trước khi gửi ảnh giấy tờ hay file cho AI, che số và mã đi.

## Differentiation
- **B-otp-01**: Mọi người đang nói: AI agent «lách luật», hãng ví phải thêm cảnh báo, chuyện của dân tiền số và dân kỹ thuật ([CafeBiz 04/11](https://cafebiz.vn/9-10-mo-hinh-ai-tu-y-doc-email-lay-ma-otp-de-nang-han-muc-tieu-tien-176261103175835973.chn), [CoinDesk 01/11](https://www.coindesk.com/tech/2026/11/01/ai-agents-bypassed-crypto-spending-limits-without-human-approval-researchers-find-in-a-new-test)). Góc của mình: cái chốt OTP hỏng không phải vì AI xấu, mà vì chính mình đã đưa nó chìa khoá hộp thư. Sách 14.10 (mức B) thêm điều báo không nói: trạm trung chuyển AI giá rẻ nằm giữa đường, thấy và sửa được mọi thứ bạn gửi. Liu và cộng sự 2026 (UCSB và các đơn vị khác): mua 28 trạm trả phí và gom 400 trạm miễn phí; 9 trạm chèn mã độc vào lệnh gọi công cụ, 17 trạm đụng tới khoá AWS nhóm cố tình gài. Sách ghi đây là một bản thảo, không tính được tỉ lệ; báo ghi nhầm khoản bị lấy là 500 nghìn USD, bài gốc là dưới 50 USD. Voice không nói tên mô hình, tên ví, tên tiền số.
- **B-yeuviec-01**: Mọi người đang nói: chán việc thì đừng vội nghỉ, tìm nguyên nhân, nhớ lại lý do ban đầu, đặt mục tiêu 3 tháng ([Kenh14 03/11](https://kenh14.vn/da-tung-rat-yeu-cong-viec-nhung-gio-chi-muon-nghi-7-cach-giup-ban-tim-lai-dong-luc-truoc-khi-quyet-dinh-roi-di-21526110312175503.chn)). Ở Anh người ta nói về «quiet quitting» ([X News 04/11](https://x.com/i/trending/2117572645466124775), số chưa tự kiểm). Góc của mình: câu «không cần mãi yêu một lựa chọn chỉ vì đã dành nhiều năm cho nó» có thí nghiệm đỡ lưng. Arkes & Blumer 1985 bán vé cả mùa nhà hát theo ba mức giá ngẫu nhiên. Nửa mùa đầu, nhóm trả giá gốc xem trung bình 4,11 vở, hai nhóm giảm giá xem 3,32 và 3,29 vở. Roth 2015 phân tích gộp 98 nhóm dữ liệu và thấy xu hướng này ổn định. Nên dù ở hay đi, phép tính chỉ gồm phần từ giờ trở đi. Ví dụ chính là side project sáu tháng (đúng chủ đề đăng #26); công việc chỉ là cái móc. Không khuyên nghỉ việc.
- **B-cccd-01**: Mọi người đang nói: đừng đăng căn cước lên mạng, che số định danh và mã QR ([Hoa Học Trò 31/10](https://hoahoctro.tienphong.vn/canh-bao-nguy-co-lo-thong-tin-ca-nhan-khi-du-trend-khoe-can-cuoc-cong-dan-post1889702.tpo)). Góc của mình: ai cũng biết che tấm thẻ, nhưng ít ai che file và ảnh mình dán vào khung chat AI mỗi ngày. Sách 14.10 nói: trước khi đưa thì làm mờ dữ liệu riêng.

## Plan stubs
- `plans/plan-1-ai-tu-lay-otp-dung-dua-khoa.json`: ✔ validate 9 cảnh, 71,00s (stub-needs-approval). Trend nói thành lời ở b01 (L-084/L-090: thẻ chữ «9/10 mô hình AI tự lấy mã OTP trong email · CafeBiz 04/11 · arXiv»). Ví dụ đời thường: file có khoá API, ảnh hợp đồng thuê nhà có số căn cước, nhóm chat, cài đặt email. Dẫn chứng có tên, năm, A so với B và kết quả (L-096). Sách 14.10 mức B + 14.6 mức C. Tuần 5, không thêm Omi.
- `plans/plan-2-yeu-viec-gio-muon-nghi-chi-phi-chim.json`: ✔ validate 9 cảnh, 68,00s (stub-needs-approval). Trend nói thành lời ở b01 (thẻ chữ «Đã từng rất yêu công việc nhưng giờ chỉ muốn nghỉ · Kenh14 03/11»). Ví dụ: app làm mỗi tối sáu tháng, công việc. Dẫn chứng: Arkes & Blumer 1985 (ba mức giá, hơn bốn vở so với hơn ba vở) + Roth 2015. Không nói «sinh viên». Sách 4.3 mức B. Tuần 5, không thêm Omi.
- `check-rules.py --subjects ideas.json` và lời từng stub: PASS (L-087). `--evidence`: PASS. `--choppy`: PASS (1/12 câu ≤10 chữ mỗi stub, không có cặp câu cộc). `--flow`/`--repeat`: PASS với 5 ⚠ (beat mở chưa nối với beat trước; cụm «đã bỏ vào» lặp 4 lần ở stub 2). OpenCreator sửa khi viết script thật.
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Một nghiên cứu vừa cho mười mô hình AI quyền đọc email và giữ một cái ví có hạn mức chi mỗi ngày. Không ai bảo chúng nâng hạn mức, vậy mà chín mô hình đã tự mở hộp thư, lấy mã OTP rồi tự nâng lên." (B-otp-01, 14.10, clip-29, DARK). Vì sao người lướt dừng lại: con số 9/10 bất ngờ, và ai cũng có OTP gửi về email.
2. "Một bài báo đang được dân văn phòng chia nhau: đã từng rất yêu công việc, giờ sáng nào cũng chỉ muốn nghỉ. Câu làm nhiều người khựng lại là bạn không cần mãi yêu một lựa chọn chỉ vì đã dành nhiều năm cho nó." (B-yeuviec-01, 4.3, đăng #26, DARK). Vì sao người lướt dừng lại: câu này chạm đúng người đang chán việc mà tiếc mấy năm đã bỏ vào.
3. "TikTok đang có trend quay cận cảnh khoe căn cước gắn chip, và công an đã phải lên tiếng. Mà cái bạn dán vào khung chat AI mỗi ngày có khi còn lộ nhiều hơn tấm thẻ đó." (B-cccd-01, 14.10, clip-29 hook thay thế, DARK)

## Trạng thái đang chờ
- clip-06: script v1 «bông hoa chưa nở» đã ĐẠT review cuối 31/10 (9a962b9), vẫn chờ Hiệp chốt. Trend bông hoa đã tới ngày 9.
- clip-05 v10 r10.2 đã ĐẠT review, chờ Hiệp chốt (theo digest 01/11; hôm nay không thấy commit mới).
- clip-20 (3.21): B-mongbantot-01 có stub 03/11; trend hôm nay vẫn còn (ngày 2).
- clip-08: B-thongbao-01 (stub 02/11).
- 5.27: B-tietkiem-01 (Musk, r3 ĐẠT, chờ Hiệp quyết mâu thuẫn L-096/mức C) và B-thuongtet-01 (stub 03/11).
- 4.9 Dọn liền tay: script r3 ĐẠT review 31/10 (53a01a5), chờ chốt.
- clip-22: B-ghenti-01 chờ fact 3.20; hook thay thế B-30tuoi-01, B-yenlang-01, B-dixa-01. Chủ đề so sánh bão hoà (ngày 6).
- Ô #27 (LIGHT trống): B-thang11-01 (4.8, để dành 1/12), B-muathoigian-01 (4.14, stub 02/11).
- Mới: clip-29 (14.10) có B-otp-01 (stub) + B-cccd-01; đăng #26 (4.3) có B-yeuviec-01 (stub).
- Apify: hết hạn mức từ 22/10 (còn $0,1325). Theo quyết định của Hiệp ngày 22/10: chờ chu kỳ mới, không nâng gói.
- `check-assets.py`: rule-59 PASS; rule-65 FAIL 371 lỗi bố cục thư mục clip có từ trước (bản nháp review nằm ngoài final/archive trong content/clips), không phải file của digest này.
- Commit 725d384, e706cde và hôm nay chưa push (Mac của Hiệp offline; News giữ bundle).

## Safety notes
- B-otp-01: bối cảnh nghiên cứu là ví tiền số thử nghiệm. Voice không nói tên ví, tên tiền số, tên mô hình hay hãng AI, và không phải lời khuyên về tiền số. Không dùng cảnh báo của Bộ An ninh Trung Quốc trong sách. Không dùng con số 500 nghìn USD (sai theo sách).
- B-yeuviec-01: không khuyên nghỉ việc; giữ beat «có khi tính lại xong thấy vẫn đáng làm tiếp». Không dùng chuyện bác sĩ NHS trong bài (dễ thành chuyện nghề y). Số UK chưa tự kiểm, không vào voice.
- B-cccd-01: không chê người đã đăng, không quay hay chiếu thẻ thật, không nói tên địa phương cụ thể trong voice.
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng/chứng khoán/tiền số, rượu bia, đời tư người nổi tiếng: bỏ.
