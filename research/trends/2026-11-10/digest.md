---
title: "Trend digest 2026-11-10"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Treg TikTok (scrapecreators/tikhub)"
id: trends-2026-11-10
type: trend-digest
status: draft-needs-review
updated: 2026-11-10
tags: [trends, digest, daily]
date: 2026-11-10
collector: pipeline/scripts/trend-collect.py + X MCP + Treg
skill: trend-digest v4 (+ tiktok-research-via-treg, quyết định Hiệp 08/11)
---
# Trend digest 2026-11-10 (thứ Ba)

**Nguồn:** 34/36 collector ok. Lỗi: wiki-vi + wiki-en (HTTP 404, như các ngày trước). **X MCP: có chạy.** Trends VN 30 mục («Thứ 3», «Thứ Ba», «Sáng», «Lạnh», «Trời» là móc lịch/thời tiết; còn lại phim Thái, fandom, crypto, Jensen Huang (scandal đời tư): bỏ). Worldwide 30 mục (bóng bầu dục Mỹ, DC/Marvel, Nhật, Hegseth: không dùng). 40 story X News từ 4 query (habits productivity, AI at work burnout, Vietnam gen Z, self improvement motivation; max_age 72h). Gộp `x-extra.json` (100 mục), bản gốc trong `x-raw/`.
**Treg TikTok: CÓ chạy (Treg-first).** 14 call (13 tính tiền), tổng **$0,0218** (7 keyword search ScrapeCreators, 4 video detail + transcript (1 lỗi 404 miễn phí), 1 detail qua route tikhub (miss), 2 comments qua route tikhub). 172 kết quả search. Transcript thật 2/3 detail; music 3/3 detail (đều original sound). **Không dùng Apify.** Chi tiết call id, giới hạn: `treg/README.md`.
**Giới hạn TikTok:** keyword search, không phải bảng xếp hạng trend hay For You feed. `region=VN` chỉ là proxy (trường region trả về VN 166 / KR 3 / JP, US, SG 1); `date_posted=this-week` không bảo đảm, nhưng ngày đăng thật đều trong 03–10/11. Lượt xem là snapshot lifetime lúc ~08:15 giờ VN, không chứng minh đang tăng. Comment là trang đầu 20 cái theo thứ tự provider.
**Số lượng:** collector 501 thô → 483 cụm. raw.json 488 mục (thêm 5 TikTok-native): 378 ok · 23 caution · 87 drop (28 drop tay + 1 TikTok). **401 qua lọc.** Chấm tay 18 mục. Drop tay: scandal đời tư CEO Nvidia (≈15 tin VN/EN), TikToker bị bắt, nhân viên y tế chém hiệu trưởng, xe tải đâm xe, ung thư (2), ảnh hở hang, nợ nần người nổi tiếng, H3 cheating, ADHD doctor (nhãn y khoa), Hegseth / Iran / Trump (chính trị).

Dữ liệu: `collect.json`, `collect-run.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `treg/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | X News «performance punishment»: tự động hoá/làm nhanh thì bị giao thêm việc, không tăng lương; nhiều người khuyên giấu mẹo, làm chậm lại (tóm tắt kể chuyện gốc Reddit 15 giờ/tuần → dưới 1 phút: **chưa tự kiểm**, không dùng số) | 0.931 | 1.0 / 0.03 | [X News 09/11](https://x.com/i/trending/2119869962844037311) | 4.17 / đăng #13 (chưa có bridge nào) | LIGHT |
| 2 | TikTok «Pha hít thở lấy bình tĩnh đá penalty… cầu thủ Porto» (954.287 xem, 3.073 share, đăng 06/11; caption, chưa xem video; detail 2 provider không trả video lúc 08:30 → có thể đã gỡ) | 0.598 | 1.0 / 0.15 | [TikTok @onsportsplus](https://www.tiktok.com/@onsportsplus/video/7705013968930196744) | 22.8 / đăng #21 (hook thay thế) | LIGHT |
| 3 | TikTok câu nhại «Không cần đi làm nữa» (#khongcandilamnua): @giang.gia.doi 1.049.136 xem / 2.172 comment (đăng 04/11, transcript thật), @nguyentriduc92 540.017 xem, thêm @trantin03 41.386, @sangcachep116haonam 28.312 | 0.573 | 1.0 / 0.15 | [TikTok @giang.gia.doi](https://www.tiktok.com/@giang.gia.doi/video/7704181828688579848) | 12.24 (ý tưởng mới) | DARK |
| 4 | X: tranh luận «cuộc sống không ma sát» khi AI làm hết việc vặt (số 10% / 56% chỉ trong tóm tắt, chưa tự kiểm) | 0.344 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2119635796537839811) | 4.10 (phụ, chưa bridge) | — |
| 5 | X: nghiên cứu Nature ngủ 6,4–7,8 giờ ứng với tuổi sinh học cơ quan thấp nhất (UK Biobank ~500k; **bài xuất bản 13/05/2026**, đang được chia lại; tương quan, giấc ngủ tự khai — đã đối chiếu abstract) | — | 1.0 / 0.4 | [X News](https://x.com/i/trending/2119681579760984324) · [Nature](https://www.nature.com/articles/s41586-026-10524-5) | 3.3 (caution: mốc 6,4h dễ bị hiểu ngược «6 tiếng là đủ») | — |
| 6 | Kenh14: Miền Bắc bỏ qua mùa thu, vào thẳng rét | — | 1.0 / 0.5 | [Kenh14](https://kenh14.vn/rat-la-ngay-day-roi-mien-bac-chinh-thuc-bo-qua-mua-thu-tien-thang-den-cai-ret-co-ro-215261109214211077.chn) | callback B-dotlanh-01 (3.5) | — |
| 7 | TikTok «Ngủ đủ 2 tiếng trong 8 tiếng» (281.583 xem; caption) + «Tầm quan trọng của giấc ngủ» (218.919 xem) | — | 1.0 / 0.5 | [TikTok @kykytv](https://www.tiktok.com/@kykytv/video/7704685471942659348) | bằng chứng phụ 3.3 | — |
| 8 | X: buông ghen tị, lo đường của mình (ngày thứ 3) | — | 1.0 / 0.7 | [X News](https://x.com/i/trending/2119396468901437905) | 3.20 bão hoà, chỉ là bằng chứng | — |
| 9 | Kenh14 (qua GNews): Gen Z mua sắm «thích thì cứ thích, nhưng xuống tiền phải thấy xứng đáng» (chỉ tiêu đề, chưa đọc bài) | — | 1.0 / 0.4 | [GNews → Kenh14](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOLXFMaS1YMy02RmJsTTh1TlcwbVNubWlZVzVzN2ZwY3hUUVIzMWRTQUU2REFuekR6MEpPV0RnM0dEMGpuMkF0Zi1tcFJheWtxaW9neHluWDNuc2FORHRIbExXUkhBVUdXcEpsTGNLQ1N3MVhQT1V1UXJNdjI1andObHAzejBlbTdaQ2p2ODVsV2JULTlKbFR4VzZIREZLRjVMMjlyTmlDd2J1Wm5HYVZJLTNYLTRtdmlORTJMSWxYczZaMmtBUU40bzYyU1NzN2JpQnc?oc=5) | 5.x (phụ) | — |
| 10 | X: meme «làm chăm chỉ có đủ không» (có phần cầu nguyện → bỏ phần đó) | — | 1.0 / 0.3 | [X News](https://x.com/i/trending/2119785692138176522) | pattern P11 | — |

Đã xem và bỏ khỏi top: «Văn làm phiền người khác» (@koravel0 607k: transcript là văn mẫu nhại cuộc gọi trúng thưởng + tỏ tình, không liên quan), trend giới thiệu bản thân bằng một bức ảnh (người nổi tiếng, khó nối trục kênh), MBA CafeBiz (PR), Gen Z Mỹ về ở với bố mẹ (số Mỹ), «sống nhiều kiếp trước 30» (bối cảnh Mỹ), thói quen ngủ gật người Nhật (đã thấy 09/11, có B-nap-01). Điểm `rank` của các tin productivity tiếng Anh chung chung (Fed Minneapolis, ngân sách Canada…) là nhiễu heuristic, không xét.

## TikTok signals (Treg, snapshot 10/11 ~08:15 giờ VN)
| keyword | clip | xem / comment / share | hook / transcript (nguồn) | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| dung AI di lam | [@giang.gia.doi](https://www.tiktok.com/@giang.gia.doi/video/7704181828688579848) · đăng 04/11 12:20 · 28s | 1.049.136 / 2.172 / 2.368 | transcript thật (phụ đề tự động): «không cần đi làm nữa… mà sẽ sống an yên có tài chính suốt cuộc đời… ngày nào giờ nào bao nhiêu tuổi bạn sẽ tự do hoàn toàn»; comment (trích nguyên văn, mỗi cái một lời tự kể): «Tao nghỉ làm ở nhà 3 ngày mỳ tôm ko có mà ăn lại phải đi làm» (83 like) | original sound (Giang "giả dối") | **caution**: comment phần lớn chế giễu người nói; không nhắc/vẽ người đó | B-khongdilam-01 |
| dung AI di lam | [@nguyentriduc92](https://www.tiktok.com/@nguyentriduc92/video/7704248094052912405) · đăng 04/11 · 34s | 540.017 / 1.257 / 1.313 | caption «Không cần đi làm nữa 🥴» (không lấy transcript) | chưa lấy (search trim) | caution | F11 bằng chứng |
| hit tho sau binh tinh lai | [@onsportsplus](https://www.tiktok.com/@onsportsplus/video/7705013968930196744) · đăng 06/11 · 90s | 954.287 / 122 / 3.073 | caption «Pha hít thở lấy bình tĩnh đá penalty cực chất của cầu thủ Porto»; comment «Áp lực vãi chứ đừng có hỏi 😂😂» (1 like); transcript/music: không lấy được (404 / miss) | không có | caution: link có thể đã gỡ; cầu thủ thật, chỉ tích cực, không footage | B-penalty-01 |
| lam xong viec som bi giao them | [@nguyen_919191](https://www.tiktok.com/@nguyen_919191/video/7703783477799390516) · đăng 03/11 · 28s | 353 / 0 / 0 | caption «Làm càng giỏi, việc càng nhiều! Làm tốt được thưởng… thêm việc! … Còn lương thì vẫn đứng yên!»; transcript null | original sound | ok; phạm vi rất thấp | B-phimtat-01 (đỡ cho X) |
| lam xong viec som bi giao them | [@mu.s.vn.phng](https://www.tiktok.com/@mu.s.vn.phng/video/7704633920842665237) · đăng 05/11 | 129 / 0 / 0 | caption «KHEN XONG ÔM HẾT VIỆC… Hãy hỏi rõ phạm vi, nguồn lực và tiêu chí hoàn thành trước khi nhận» (góc người khác đã nói) | chưa lấy | ok | consensus cho B-phimtat-01 |
| ngu bao nhieu tieng la du | [@kykytv](https://www.tiktok.com/@kykytv/video/7704685471942659348) · đăng 05/11 | 281.583 / 99 / 316 | caption «Ngủ đủ 2 tiếng trong 8 tiếng» | chưa lấy | ok | phụ 3.3 |
| lam xong viec som bi giao them | [@koravel0](https://www.tiktok.com/@koravel0/video/7704296499475172616) · đăng 04/11 | 607.808 / 254 / 11.258 | transcript: văn mẫu nhại cuộc gọi trúng thưởng | original sound | drop (không liên quan) | — |

Không gọi sound chart hôm nay (series comic, không mượn audio; Viral 50 đã ghi 09/11).

## Learning
- **Thêm F11 (viral-quote parody):** một câu nói viral được nhiều creator nhại lại, caption chỉ là câu đó (#khongcandilamnua: 1,05M + 540k + 41k + 28k trong 03–04/11). Comment là nơi người xem chế giễu người nói → format luôn caution; chỉ mượn câu, không mượn người. P11 / P10 / P01 +1. Không thêm P-row.
- **«Làm giỏi bị giao thêm việc» mạnh ở X, yếu ở TikTok VN:** cùng ý ở VN chỉ có clip vài trăm xem. Bridge B-phimtat-01 dựa vào X News là chính; ghi rõ khi trình.
- **Bài «mới» có thể là bài cũ chia lại:** story X về giấc ngủ 6,4–7,8h dẫn bài Nature 13/05/2026. Luôn mở nguồn gốc trước khi gọi là tin mới.
- **Treg:** search trim mất music (lần 3). Clip thể thao bản quyền có thể biến mất trong vài ngày: gọi detail ngay khi chọn. Đọc transcript trước khi trả comments đã tiết kiệm 2 call (@koravel0, @nguyen_919191).
- Bão hoà nên tránh: so sánh 3.20 (ngày 3), quỹ dự phòng 5.27 (≥8 bridge), đếm ngược Tết/hết năm, thức khuya/ngủ bù (đã pick 08/11), Sunday scaries, Kim Dung / lương 31tr (đã pick 09/11).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-phimtat-01 | X «performance punishment» (+ TikTok VN «làm tốt được thưởng… thêm việc») | ngày nào cũng copy số từ email dán vào bảng tính, kéo chuột cả chục lần | 4.17 (mức B) | "Mạng đang cãi nhau: làm nhanh quá thì bị giao thêm việc, vậy có nên giấu mẹo đi không? Mình chọn cách khác: học đúng một phím tắt, rồi tự quyết phần giờ dư đi đâu." (P11, turn P06) | contrarian / empathy | **đăng #13 (4.17, LIGHT)**, bridge đầu tiên cho ô này | LIGHT |
| B-khongdilam-01 | TikTok #khongcandilamnua + comment «nghỉ 3 ngày mỳ tôm ko có» | 11 giờ đêm lưu số tài khoản của khoá học «không cần kinh nghiệm, không cần vốn» | 12.24 (mức B; bỏ toàn bộ vụ án, số, luật Trung Quốc) | "Cả TikTok đang nhại câu «không cần đi làm nữa». Vậy nếu tối nay gặp một khoá học hứa đúng câu đó, bạn sẽ hỏi họ câu gì trước khi chuyển khoản?" (P11 khớp một phần + F11) | empathy / contrarian | ý tưởng mới 12.24 (ngoài 30 ô) | DARK |
| B-penalty-01 | TikTok cầu thủ hít thở trước penalty | trước cuộc gọi khó với khách; sau khi lỡ lời với người nhà | 22.8 (mức B, 1 thử nghiệm, tự báo cáo) | "Cầu thủ đứng trước chấm phạt đền, cả sân nhìn mình, và việc đầu tiên anh làm là… thở. Trước một cuộc gọi khó, bạn có cho mình nhịp thở đó không?" (P01) | empathy | đăng #21 (22.8, LIGHT) hook thay thế B-met-01 | LIGHT |

Cầu nối về trục kênh (trend chỉ là móc): B-phimtat-01 → hôm nay học đúng một phím tắt cho thao tác lặp nhiều nhất và tự quyết phần giờ dư đi đâu (về đúng giờ / 10 phút đi bộ) (+1). B-khongdilam-01 → muốn bớt phụ thuộc vào việc là chính đáng; +1 tối nay là chép hai câu hỏi vào ghi chú trước khi trả tiền cho bất kỳ lời hứa thu nhập nào. B-penalty-01 → +1 là 5 phút thở dài vòng trước một việc khó hôm nay. Không trùng 08–09/11 (thức khuya #14, hết năm #27, Chủ nhật #24, Kim Dung #27, lương 31tr #28).

**Tách lớp bằng chứng:** (a) trend = X News + clip/comment TikTok ở trên (số liệu lấy từ Treg/X; số trong tóm tắt X ghi «chưa tự kiểm»); (b) fact sách = 4.17 (Lane et al. 2005, mức B; sách ghi thí nghiệm hiệu suất chỉ 6 người, không có số giây → không nêu «1 tiếng/tuần»), 12.24 (mức B, nguồn toàn Trung Quốc → chỉ dùng phần hành động), 22.8 (Balban et al. 2023, mức B, 1 thử nghiệm tự báo cáo); (c) cầu nối, hook và câu «tự quyết giờ dư đi đâu» = đề xuất biên tập của Social Research, chưa phải fact. Deep Research cần kiểm (b) trước khi OpenCreator viết.

## Differentiation
- **B-phimtat-01:** Mọi người đang nói: làm nhanh thì bị phạt bằng thêm việc, nên giấu mẹo, cố tình làm chậm ([X News 09/11](https://x.com/i/trending/2119869962844037311)), hoặc «hỏi rõ phạm vi, nguồn lực trước khi nhận» ([@mu.s.vn.phng](https://www.tiktok.com/@mu.s.vn.phng/video/7704633920842665237)). Góc của mình: không giấu, không làm chậm (không khuyên lừa sếp); mẹo vẫn đáng học theo sách 4.17, nhưng chỉ học thao tác lặp ≥10 lần/ngày, và chính mình đặt trước chỗ cho phần giờ được trả lại. Khác B-airead-01 (3.6) và B-otp-01 (14.10).
- **B-khongdilam-01:** Mọi người đang nói: chế giễu người nói và người ngồi nghe, đùa «không đi làm thì đi ăn cướp» ([@giang.gia.doi](https://www.tiktok.com/@giang.gia.doi/video/7704181828688579848)). Góc của mình: không cười ai; câu hứa đó kéo được người vì ai cũng mệt việc, nên cái cần là hai câu hỏi trước khi chuyển khoản (book fact phía consensus không có). Khác B-tietkiem-01 / B-thuongtet-01 (5.27) và B-bantruoc-01 (12.18).
- **B-penalty-01:** Mọi người đang nói: khen cầu thủ «lạnh», đoán tên, đùa bóng đá. Góc của mình: khoảnh khắc trước cú sút là khoảnh khắc ai cũng có (trước cuộc gọi khó); sách có kiểu thở cụ thể (hít hai nhịp bằng mũi, thở ra dài bằng miệng, 5 phút). Không nói cầu thủ dùng kiểu thở này (không biết). Khác B-floor-01 và B-met-01.

## Plan stubs
- `plans/plan-1-phim-tat-gio-du-cua-ban.json`: ✔ validate 9 cảnh, 70,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ đề xuất «Làm nhanh bị giao thêm việc? · X News 09/11» (L-084). Ví dụ đời thường: copy số từ email sang bảng tính, về đúng giờ, đi bộ. Tuần 3, không Omi. Theme light.
- `plans/plan-2-khong-can-di-lam-nua-hoi-hai-cau.json`: ✔ validate 9 cảnh, 67,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ «#khongcandilamnua · TikTok 04/11» (L-084); comment ở b02 là **diễn giải** lời tự kể (bản gốc: «Tao nghỉ làm ở nhà 3 ngày mỳ tôm ko có mà ăn lại phải đi làm»). Ví dụ: quảng cáo khoá học đêm khuya, ghi chú điện thoại. Không Omi. Theme dark.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087).
- Độ dài stub ~70s chỉ là khung; độ dài thật theo L-099 (<300s, mục tiêu 2–3 phút) do OpenCreator quyết sau khi Deep Research kiểm 4.17 / 12.24. Mã pattern trên là đề xuất của Social Research; Rule Reviewer/OpenCreator vẫn phải lập bảng hook thực ↔ P/F (L-100). Stub không cho phép tạo hình, giọng, render hay đăng trước Chốt.

## Script hooks (cần Hiệp duyệt)
1. "Mạng đang cãi nhau: làm nhanh quá thì bị giao thêm việc, vậy có nên giấu mẹo đi không? Mình chọn cách khác: học đúng một phím tắt, rồi tự quyết phần giờ dư đi đâu." (B-phimtat-01, 4.17, đăng #13, LIGHT).
2. "Cả TikTok đang nhại câu «không cần đi làm nữa». Vậy nếu tối nay gặp một khoá học hứa đúng câu đó, bạn sẽ hỏi họ câu gì trước khi chuyển khoản?" (B-khongdilam-01, 12.24, ý tưởng mới, DARK). Caution.
3. (phụ, không stub) "Cầu thủ đứng trước chấm phạt đền, cả sân nhìn mình, và việc đầu tiên anh làm là… thở. Trước một cuộc gọi khó, bạn có cho mình nhịp thở đó không?" (B-penalty-01, 22.8, đăng #21, LIGHT). Caution link.

## Safety notes
- B-phimtat-01: không khuyên giấu việc, làm chậm hay lừa công ty; không nêu số 15 giờ (chưa tự kiểm, gốc Reddit mình không được dùng).
- B-khongdilam-01: không nhắc, không vẽ, không lồng tiếng diễn giả bị nhại; không nói ai lừa đảo; không dùng audio gốc; bỏ toàn bộ vụ án, con số, luật, số điện thoại Trung Quốc của 12.24.
- B-penalty-01: không dùng footage (VTVcab, series comic); không nêu tên cầu thủ; link có thể đã gỡ → mở lại trước khi dùng.
- Giấc ngủ 6,4–7,8h: không dùng làm hook cho #15 (dễ bị hiểu ngược với 3.3), không nói tuổi thọ/bệnh.
- Chính trị, tội phạm, bệnh, scandal đời tư, tình dục, tôn giáo (phần cầu nguyện của meme), crypto: bỏ.

## Trạng thái đang chờ
- Đăng #13 (4.17): **B-phimtat-01 (đầu tiên)**. Đăng #21 (22.8): B-met-01, **+ B-penalty-01**. Ý tưởng mới 12.24: **B-khongdilam-01**.
- Hôm nay thứ Ba: không có weekly synthesis.
