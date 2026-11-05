---
title: "Trend digest 2026-11-05"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-11-05
type: trend-digest
status: draft-needs-review
updated: 2026-11-05
tags: [trends, digest, daily]
date: 2026-11-05
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-11-05 (thứ Năm)

**Nguồn:** 32/36 collector ok. Lỗi: vnexpress-giaitri (SSL UNEXPECTED_EOF), kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 21). vnexpress-sohoa hôm nay chạy lại được. **X MCP: có chạy.** Trends VN 20 mục («Thứ 5», «Thứ Năm», «Chào», «Sáng», «Ngày», «Chúc» là móc giờ; còn lại là fandom Thái, Fungo, NFTs). Worldwide 20 mục (Nhật, bóng đá, bầu cử Mỹ; không dùng được). Thêm 39 story X News từ 4 query (productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h). Gộp vào `x-extra.json` (79 mục), bản gốc trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `thoiquen`, resultsPerPage 5, commentsPerPost 0) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 449 thô → 436 cụm. raw.json 436 mục: 321 ok · 7 caution · 108 drop (46 drop tay). **328 qua lọc.** Chấm tay 22 mục; mục chưa soát giới hạn fit và bridgeability ≤0,4; YT niche chỉ làm bằng chứng pattern. Drop tay: tội phạm và tiền số (vụ hack Binance «bắt nguồn từ một kỹ sư muốn nhảy việc», VnExpress + CafeBiz + Ars, dù chạm 14.10), bệnh và nhãn y khoa («hội chứng thị giác màn hình», ADHD, nhồi máu cơ tim, u gan, claim mỡ bụng/oatzempic/fibermaxxing), bi kịch và tai nạn (máy bay, hoả hoạn, thiên tai), chính trị (bầu cử Mỹ, ngoại giao, Olympia), tôn giáo/tâm linh, vàng, Vietlott, rượu bia, đời tư và tài sản người nổi tiếng, chuyện một cặp vợ chồng viral (dễ thành chê).
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | #texthip: Gen Z Hàn gác video ngắn để đọc sách, câu lạc bộ đọc kín chỗ, trào lưu Phone Free. Khảo sát Bộ VHTT Hàn: nhóm tuổi 20 là nhóm duy nhất đọc nhiều lên (74,5% → 75,3%; số từ báo, chưa tự kiểm bản gốc) | 0.766 | 1.0 / 0.05 | [Znews/Vietnam.vn 04/11](https://www.vietnam.vn/trao-luu-nang-tam-van-hoa-doc-bo-phim-ngan-cua-gen-z-han-quoc) · [Korea Times 04/11](https://www.koreatimes.co.kr/lifestyle/trends/20261104/viral-text-hip-trend-boosts-bookstore-sales-brings-literature-to-food-aisles) | 4.15 (đăng #10) | LIGHT |
| 2 | KOL làm hai việc toàn thời gian, 33 tuổi lần đầu nghỉ hẳn Chủ nhật: «ngày không có thành tựu lại cho nhiều năng lượng» (caution: người có tên) | 0.631 | 1.0 / 0.05 | [Kenh14 05/11](https://kenh14.vn/the-30s-talk-an-phuong-30-tuoi-quyet-dinh-khong-lam-viec-chu-nhat-san-sang-cuoi-nguoi-quet-phai-tren-tinder-10-nam-truoc-215261105073609015.chn) | 3.13 (đăng #12) | DARK |
| 3 | #trusttheprocess30days (ngày 5): mỗi ngày một cảnh, cuối tháng ghép lại | 0.346 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2117637470414336083) | 4.12 (B-30canh-01, clip-30) | LIGHT |
| 4 | «Vì sao người già thường hạnh phúc hơn trung niên?» (Stone, Gallup 340.847 người; số từ báo, chưa tự kiểm bài gốc) | 0.315 | 1.0 / 0.0 | [VnExpress 04/11](https://vnexpress.net/vi-sao-nguoi-gia-thuong-hanh-phuc-hon-trung-nien-5139698.html) | chưa có mục sách khớp | — |
| 5 | «Không cần chuyện tình cổ tích, chỉ mong có người cùng rửa bát đến già» | 0.223 | 1.0 / 0.0 | [VnExpress 04/11](https://vnexpress.net/khong-can-chuyen-tinh-co-tich-chi-mong-co-nguoi-cung-rua-bat-den-gia-5140260.html) | 4.9 / phần 10 (bằng chứng phụ) | — |
| 6 | Apple Watch Live Rewind nghe giùm, tóm tắt giùm: người xung quanh có bị ghi âm? | 0.223 | 1.0 / 0.0 | [Tinh tế 04/11](https://tinhte.vn/thread/live-rewind-va-siri-recap-apple-watch-nghe-gium-tom-tat-gium-nguoi-xung-quanh-co-bi-ghi-am.4189630/) | 14.x (bằng chứng phụ) | — |
| 7 | Gen Z kiếm 50 triệu/tháng vẫn bị chê không lo mua nhà (caution: dễ thành chê, ghen tị) | 0.218 | 1.0 / 0.05 | VTC News qua Google News «gen Z» (chưa mở bài gốc) | 5.x (bằng chứng phụ) | — |
| 8 | 6 thói quen giữ bếp gọn mỗi ngày | 0.207 | 1.0 / 0.1 | Southern Living qua Google News US productivity (chưa mở bài gốc) | 4.9 (script dọn liền tay chờ chốt) | — |
| 9 | «Người xung quanh đang thầm mong bạn làm tốt» (ngày 3) | 0.187 | 0.5 / 0.45 | [X News](https://x.com/i/trending/2117361072449765528) | 3.21 (B-mongbantot-01) | LIGHT |
| 10 | Người lao động Anh bớt làm thêm vì áp lực kinh tế (ngày 2, số chưa tự kiểm) | 0.164 | 1.0 / 0.15 | [X News 04/11](https://x.com/i/trending/2118025889372127412) | 3.13 / 4.3 (bằng chứng phụ) | — |

Đã xem và bỏ khỏi top: vụ hack Binance từ một kỹ sư tải file «bài test tuyển dụng» (rất hợp 14.10 nhưng là tội phạm + tiền số, theo luật kênh thì bỏ); CEO Google «không học điều phối AI agents thì 2027 đứng nhìn» và ngân hàng cắt nhân sự vì AI (AI ở chỗ làm đã bão hoà, dễ gây hoang mang); «hội chứng thị giác màn hình» (nhãn y khoa); không khí lạnh miền Bắc (móc mùa, chưa có bridge); bông hoa chưa nở (ngày 10), brain stacking (ngày 11).

## TikTok signals
Hôm nay không có dữ liệu Apify. Proxy từ báo và X, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| #texthip / BookTok Hàn | [Znews/Vietnam.vn 04/11](https://www.vietnam.vn/trao-luu-nang-tam-van-hoa-doc-bo-phim-ngan-cua-gen-z-han-quoc) | báo ghi #texthip là hashtag mạng xã hội, giống cộng đồng BookTok (lời báo, chưa tự kiểm số bài) | ok | B-texthip-01 → đăng #10 |
| TikTok biến căn bếp thành «quầy pha chế» | Kenh14 qua Google News «trend TikTok» | format món quen làm lại | ok | chưa có mục sách |
| khoe căn cước «bắt trend» | CafeF qua Google News «trend TikTok» (ngày 4) | vẫn lên báo | ok | B-cccd-01 (clip-29) |
| bông hoa chưa nở | Google News «trend TikTok» (Vietnam.vn) | ngày 10 | ok nhưng bão hoà | clip-06 (chờ chốt) |
| oatzempic, fibermaxxing, brain stacking | Google News US | claim sức khoẻ / bão hoà | drop / tránh | — |

## Learning
- Không thêm P-row. #texthip khớp P13 (thế hệ khác làm khác) + P03 (mọi người nói «đọc nhiều hơn», sách nói «cài giới hạn cứng»). Chuyện nghỉ Chủ nhật khớp P10 + P03. P03/P10/P13 +1.
- Chủ đề «bớt làm, nghỉ có chủ đích» đang lên từ hai phía: Kenh14 (KOL nghỉ Chủ nhật) và X News (người lao động Anh bớt làm thêm, ngày 2). Hợp 3.13, mục chưa từng có trend tốt ngoài B-49h-01 và B-jevons-01.
- Trend «người trẻ bỏ video ngắn» quay lại lần hai sau B-phimngan-01 (29/10) và B-reading-01 (18/10): đăng #10 (4.15) giờ có ba lựa chọn hook.
- Mảng an toàn dữ liệu vẫn nóng (Binance, Apple Watch ghi âm, căn cước), nhưng clip-29 đã có ba hook, không cần thêm.
- Bão hoà nên tránh: bông hoa chưa nở (ngày 10), brain stacking (ngày 11), so sánh / buông so sánh (ngày 7), AI ở chỗ làm nói chung.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-texthip-01 | #texthip Gen Z Hàn | định đọc vài trang trước khi ngủ, mở điện thoại xem giờ, ngẩng lên đã mười hai giờ đêm | 4.15 (mức C, bỏ số Trung Quốc) | "Ở Hàn Quốc, người hai mươi mấy tuổi đang rủ nhau gác video ngắn để đọc sách, còn đặt cho nó một cái tên rất kêu là text hip." (P13+P03) | contrarian / empathy | đăng #10 (4.15) hook thay thế | LIGHT |
| B-chunhat-01 | KOL lần đầu nghỉ Chủ nhật | Chủ nhật vẫn mở laptop «làm nốt chút thôi», sáng thứ Hai đã mệt | 3.13 (Pencavel 2015, mức B) | "Một người làm hai việc toàn thời gian suốt mười năm, năm nay mới lần đầu nghỉ hẳn Chủ nhật. Và chị kể chính cái ngày không làm ra gì ấy lại cho chị nhiều năng lượng nhất tuần." (P10+P03) | data / contrarian | đăng #12 (3.13) hook thay thế | DARK |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook, mỗi bridge kết bằng một việc nhỏ làm được hôm nay. B-texthip-01: đặt 30 phút mỗi ngày cho đúng một app video ngắn. B-chunhat-01: Chủ nhật này nửa ngày không mở email công việc.

## Differentiation
- **B-texthip-01**: Mọi người đang nói: người trẻ Hàn «cai» video ngắn bằng sách, đọc sách thành thời thượng, mình cũng nên đọc nhiều hơn ([Znews/Vietnam.vn 04/11](https://www.vietnam.vn/trao-luu-nang-tam-van-hoa-doc-bo-phim-ngan-cua-gen-z-han-quoc), [Korea Times 04/11](https://www.koreatimes.co.kr/lifestyle/trends/20261104/viral-text-hip-trend-boosts-bookstore-sales-brings-literature-to-food-aisles)). Góc của mình: họ không thắng bằng ý chí, họ đọc ở chỗ điện thoại tự nằm yên trong túi. Sách 4.15 nói đúng điều đó: đừng cãi với chính mình mỗi tối, cài sẵn giới hạn cứng. Sách ghi mức C và tự nói chưa có nghiên cứu đo giới hạn xong lấy lại bao nhiêu giờ; số liệu trong sách là của Trung Quốc nên không dùng. Voice nói thật điều đó (b06).
- **B-chunhat-01**: Mọi người đang nói: tuổi 30 biết chọn cho mình, nghỉ là tự thưởng ([Kenh14 05/11](https://kenh14.vn/the-30s-talk-an-phuong-30-tuoi-quyet-dinh-khong-lam-viec-chu-nhat-san-sang-cuoi-nguoi-quet-phai-tren-tinder-10-nam-truoc-215261105073609015.chn); [X News 04/11](https://x.com/i/trending/2118025889372127412), số chưa tự kiểm). Góc của mình: nghỉ không chỉ là phần thưởng. Pencavel 2015 phân tích sổ sản lượng nhà máy Anh thời Thế chiến I: dưới một ngưỡng, giờ làm và sản lượng đi cùng nhau; quá ngưỡng thì tăng chậm dần, 70 giờ/tuần ra gần bằng 56 giờ. Sách ghi đây là việc tay chân, con số 49 không đáng tin, hướng đi thì đáng tin; voice không nói 49.

## Plan stubs
- `plans/plan-1-texthip-gioi-han-cung-video-ngan.json`: ✔ validate 9 cảnh, 69,00s (stub-needs-approval). Trend nói thành lời ở b01 (L-084: thẻ chữ «#texthip · Gen Z Hàn gác video ngắn để đọc sách · Znews 04/11»). Ví dụ đời thường: đọc trước khi ngủ, xem giờ trên điện thoại, cài đặt giới hạn app. Tuần 2, không Omi.
- `plans/plan-2-nghi-chu-nhat-qua-nguong-gio-lam.json`: ✔ validate 9 cảnh, 71,00s (stub-needs-approval). Trend ở b01 (thẻ chữ «30 tuổi quyết định không làm việc Chủ nhật · Kenh14 05/11»). Ví dụ: laptop Chủ nhật, tin nhắn sếp, email, app chat công ty. Dẫn chứng có tên, năm, A so với B và kết quả (L-096). Tuần 2, không Omi.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087). `--evidence`: PASS. `--choppy`: PASS cả hai (sau khi nối câu CTA). `--flow`: stub 1 PASS sạch; stub 2 PASS với 1 ⚠ (đổi ngôi kể: «mình» ở b02–b03, «bạn» ở b07–b09). `--repeat`: PASS. OpenCreator sửa khi viết script thật.
- L-096 lưu ý: stub 1 dùng mục mức C, không có câu dẫn chứng nghiên cứu; nếu Rule Reviewer đòi dẫn chứng thì cần Deep Research tìm một thử nghiệm giới hạn app (sách trỏ sang 3.20 có thử nghiệm ngẫu nhiên).
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Ở Hàn Quốc, người hai mươi mấy tuổi đang rủ nhau gác video ngắn để đọc sách, còn đặt cho nó một cái tên rất kêu là text hip." (B-texthip-01, 4.15, đăng #10, LIGHT). Vì sao người lướt dừng lại: đang lướt video ngắn mà nghe chuyện người ta bỏ video ngắn.
2. "Một người làm hai việc toàn thời gian suốt mười năm, năm nay mới lần đầu nghỉ hẳn Chủ nhật. Và chị kể chính cái ngày không làm ra gì ấy lại cho chị nhiều năng lượng nhất tuần." (B-chunhat-01, 3.13, đăng #12, DARK). Vì sao người lướt dừng lại: ngược với cảm giác «nghỉ là lười», trúng người đang làm cả cuối tuần.

## Trạng thái đang chờ
- clip-06 «bông hoa chưa nở» v1 và clip-05 v10 r10.2: đã ĐẠT review, vẫn chờ Hiệp chốt (không thấy commit mới).
- 4.9 Dọn liền tay r3 ĐẠT, chờ chốt. 5.27: B-tietkiem-01 (chờ Hiệp quyết L-096/mức C) và B-thuongtet-01.
- clip-29 (14.10): B-otp-01 (stub 04/11, Deep Research đã kiểm số 9/7/5 ở 773da9f) + B-cccd-01.
- Đăng #26 (4.3): B-yeuviec-01 (stub 04/11). clip-20 (3.21): B-mongbantot-01. clip-08: B-thongbao-01. Ô #27: B-thang11-01, B-muathoigian-01.
- Mới: đăng #10 (4.15) có B-texthip-01; đăng #12 (3.13) có B-chunhat-01.
- Apify: hết hạn mức từ 22/10 (còn $0,1325), theo quyết định của Hiệp ngày 22/10: chờ chu kỳ mới, không nâng gói.
- Commit 725d384, e706cde, 2f9dafa, 773da9f và hôm nay chưa push (Mac của Hiệp offline; News giữ bundle).

## Safety notes
- B-texthip-01: không nói tên thần tượng (bài báo có nhắc), không dùng số Trung Quốc trong 4.15, không nói tên app hay logo app.
- B-chunhat-01: không nêu tên KOL trong voice, không dùng chuyện mẹ mất, bệnh, cân nặng, vàng trong bài. Không khuyên bỏ việc hay từ chối làm thêm; hành động chỉ là nửa ngày không mở email.
- Chính trị, tội phạm, tiền số, bệnh, bi kịch, tâm linh, vàng, xổ số, rượu bia, đời tư người nổi tiếng: bỏ.
