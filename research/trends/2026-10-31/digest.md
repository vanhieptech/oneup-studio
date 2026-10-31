---
title: "Trend digest 2026-10-31"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-10-31
type: trend-digest
status: draft-needs-review
updated: 2026-10-31
tags: [trends, digest, daily]
date: 2026-10-31
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-10-31 (Thứ Bảy)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 16). Lần chạy đầu vnexpress-moi lỗi SSL (UNEXPECTED_EOF), chạy lại thì ok. **X MCP: có chạy**: trends VN 20 (Thứ 7/Thứ Bảy, Halloween, phim Thái, Binance/SAFU, MAMA vote; chỉ móc giờ là dùng được) + worldwide 20 (Halloween Nhật, Ba Lan/Tusk, thể thao; bỏ hết) + 40 story X News (4 query: productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h) → `x-extra.json` 80 mục, bản gốc trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `hoctap`, resultsPerPage 5) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Chưa reset. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 466 thô → 449 cụm; raw.json 449 mục (293 ok · 20 caution · 136 drop, trong đó 74 drop tay) → 313 qua lọc. Chấm tay 23 mục. Mục chưa soát bị giới hạn fit ≤0,4 để heuristic không đẩy tin lạc đề lên. Mở lại 4 story X bị bộ lọc từ khoá chặn nhầm (millennials 30, growth over envy, AI agents). Drop tay gồm: chính trị (Ba Lan, kỷ luật cán bộ, bộ trưởng), tội phạm/lừa đảo (Mr Pips, phim lậu, trốn trại, fanpage giả), bi kịch (tàu Tây Ban Nha, người nổi tiếng qua đời, sinh tồn), bệnh và claim y khoa (ung thư, đột quỵ, cúm, Ebola, ferritin, kẹo an thần), tiền ảo/vàng (Binance, SAFU, XAUUSD), tôn giáo, ngoại tình, giảm cân/ngoại hình, thủ tục BHYT/căn cước.
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Elon Musk: “Tiết kiệm tiền cho tương lai là vô nghĩa” (post X 29/10). Theo VnExpress: 2,8 triệu lượt xem, 4.000 bình luận sau một ngày (chưa tự kiểm). Hai phe cãi nhau | 0.816 | 1.0 / 0.0 | [VnExpress 31/10](https://vnexpress.net/elon-musk-tiet-kiem-tien-cho-tuong-lai-la-vo-nghia-5138848.html) | 5.27 (B-tietkiem-01), caution | DARK |
| 2 | “Đừng bao giờ coi thường bông hoa chưa nở” lên báo lớn, người nổi tiếng bắt trend (ngày 3 trong ingest) | 0.573 | 1.0 / 0.15 | [VTC News 30/10](https://vtcnews.vn/trao-luu-bien-hinh-dung-bao-gio-coi-thuong-bong-hoa-chua-no-tran-ngap-tiktok-ar1048255.html), [Soha](https://soha.vn/trao-luu-bien-hinh-dung-bao-gio-coi-thuong-bong-hoa-chua-no-tran-ngap-tiktok-198261030155406384.htm), [CafeBiz](https://cafebiz.vn/trao-luu-bien-hinh-dung-bao-gio-coi-thuong-bong-hoa-chua-no-tran-ngap-tiktok-176261030153417037.chn) | 4.12 (clip-06, B-bonghoa-02) | DARK |
| 3 | Lời nhắc “đo tiến bộ bằng bước của mình, không bằng vạch đích của người khác” (ngày 2, X cập nhật 30/10) | 0.544 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2115788633512817077) | 3.20 (clip-22, B-ghenti-01) | DARK |
| 4 | “Clean as you go”: rửa dao ngay sau khi thái, nấu xong bếp gần như sạch; nhà ai cũng có người dọn liền và người để sau | 0.528 | 1.0 / 0.0 | [X News 30/10](https://x.com/i/trending/2116206747459420656) | 4.9 (B-donlientay-01) | LIGHT |
| 5 | Thế hệ trước sống tằn tiện (không internet, không latte), hai phe cãi nhau | 0.307 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2116197097968112024) | 5.27, caution | — |
| 6 | Sahil Bloom: làm việc khó sớm thì nhẹ đầu (ngày 3) | 0.269 | 0.5 / 0.35 | [X News](https://x.com/i/trending/2115816342687510634) | 4.9 (B-viecne-01, callback) | DARK |
| 7 | Dùng AI soạn tin nhắn để né xung đột gia đình | 0.243 | 1.0 / 0.0 | [VnExpress 30/10](https://vnexpress.net/dung-ai-soan-tin-nhan-de-ne-xung-dot-gia-dinh-5137840.html) | 3.16/3.17, chưa có bridge | — |
| 8 | Hết năm 2026, người sinh 1996 tròn 30: không còn millennial nào ở tuổi 20 (ngày 2–4 trên X) | 0.235 | 0.33 / 0.53 | [X News](https://x.com/i/trending/2115259918806622394), [X News](https://x.com/i/trending/2115094795404108071) | 3.20 (clip-22, B-30tuoi-01) | DARK |
| 9 | Lập trình viên nghiện chạy AI agent: lúc nào cũng thấy đang làm, dự án vẫn đứng | 0.221 | 1.0 / 0.30 | [X News](https://x.com/i/trending/2116171799830450436) | 3.7, AI ở chỗ làm đã bão hoà | — |
| 10 | Chuỗi phòng tập California dừng hoạt động, hội viên lo mất tiền thẻ trả trước | 0.214 | 0.5 / 0.25 | [VnExpress](https://vnexpress.net/lo-mat-tram-trieu-khi-chuoi-phong-tap-california-dung-hoat-dong-5138020.html), [CafeBiz](https://cafebiz.vn/cali-tham-do-goi-tap-599000-dong-thang-de-mo-lai-cau-lac-bo-quyen-loi-the-cu-se-ra-sao-176261031074552404.chn) | 5.21/5.22, caution (tranh chấp, người mất tiền) | — |

Đã xem và bỏ khỏi top dù điểm cao: Đình Bắc, Binz–Châu Bùi, nam ca sĩ bán cà phê (người nổi tiếng, không bắc được bài học); Halloween (hết hạn hôm nay); “Thứ 7/Thứ Bảy” trên X VN (chỉ là móc giờ); Bill Gates “kỹ năng lập trình lạc hậu” (AI bão hoà); thế hệ khoe ngủ ít (tô vẽ thiếu ngủ); Gen Z xin nghỉ ốm vì thiếu ngủ (ngủ bão hoà).

## TikTok signals
Hôm nay không có dữ liệu Apify. Dưới đây là proxy từ báo, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| bông hoa chưa nở (biến hình trước/sau) | VTC News, Soha, CafeBiz 30/10; Google News “trend TikTok” (Vietnam.vn: Huỳnh Lập, Phương Mỹ Chi) | “tràn ngập TikTok”, “nhiều video nhận được trăm nghìn lượt xem” (lời báo, chưa tự kiểm) | ok nếu đổi trước/sau ngoại hình thành trước/sau thói quen; không tên/ảnh người thật | B-bonghoa-02 (clip-06) |
| Brainstacking | Google News US (KXAN) | ngày 7 | ok, bão hoà | B-brainstack-01 (cũ) |
| Ferritin face, fibermaxxing | Google News US | trend sức khoẻ/thực phẩm chức năng | drop | — |
| Doraemon “Siêu quà” | Google News “trend TikTok” (Yeah1) | quảng cáo săn quà | bỏ | — |

## Learning
- Không thêm P-row. Câu của Musk khớp P11 (lời khuyên gây bão, hai phe) + P03. “Clean as you go” khớp P10 + P15. Millennials 30 khớp P05 + P13. P03/P05/P10/P11/P13/P15 +1.
- Tín hiệu mạnh nhất hôm nay là một **câu gây tranh cãi về tiền**, không phải clip. Móc nhìn thấy được (L-084): thẻ trích nguyên câu «Tiết kiệm tiền cho tương lai là vô nghĩa» kèm nguồn VnExpress, chỉ chữ, không ảnh.
- Ví dụ việc nhà (rửa dao, chồng chén) là loại ví dụ đời thường L-087 muốn nhưng ít khi lên trend. Nên giữ lại làm mẫu.
- Bão hoà nên tránh: AI ở chỗ làm, ngủ/Gen Z, brainstacking (ngày 7). Halloween hết hạn hôm nay.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-tietkiem-01 | Musk: tiết kiệm vô nghĩa | lương về trả thẻ, gửi về nhà, đóng tiền nhà, còn chút xíu, hẹn tháng sau | 5.27 | "Elon Musk vừa nói tiết kiệm cho tương lai là vô nghĩa. Có thể đúng với ông ấy. Còn bạn, nếu tháng sau mất việc, bạn sống được mấy tháng?" (P11+P03) | contrarian / empathy | ý tưởng mới trụ tiền (5.27), củng cố B-giulai-01 | DARK |
| B-bonghoa-02 | bông hoa chưa nở | thói quen mới tới tuần thứ ba chưa thấy gì đã tính bỏ | 4.12 | "Đừng bao giờ khinh thường một bông hoa chưa nở. Vậy sao thói quen mới tới tuần thứ ba chưa thấy gì, bạn đã tính bỏ?" (P03+F04) | contrarian / empathy | clip-06, bản sửa của B-bonghoa-01 | DARK |
| B-donlientay-01 | clean as you go | nấu xong để chén mai rửa, sáng ra càng ngán | 4.9 | "Có người nấu xong là bếp sạch luôn, vì thái hành xong họ rửa dao liền. Còn bồn rửa nhà bạn, tới tối đang chờ mấy cái?" (P10+P15) | empathy / humor | ý tưởng mới / callback clip-02 | LIGHT |
| B-30tuoi-01 | 1996 tròn 30 + growth over envy | lướt thấy bạn cùng tuổi khoe nhà, xe đúng dịp sắp 30 | 3.20 | "Hết năm nay, người sinh năm 1996 tròn ba mươi. Bạn đang đếm mình đã có gì, hay đang đếm người ta có gì?" (P05+P13) | empathy / contrarian | clip-22, hook thay thế cho B-ghenti-01 | DARK |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay: đặt một lệnh chuyển tự động nhỏ ngày lương về · giữ một thói quen và đếm theo tháng · làm liền việc dưới một phút lúc nó còn nhỏ · ghi một thứ mình nhích lên so với ba tháng trước.

## Differentiation
- **B-tietkiem-01**: Mọi người đang nói: hai phe dưới post của Musk, một bên tin AI làm tiền hết quan trọng, một bên bảo «ông có tiền nên mới nói vậy» ([VnExpress](https://vnexpress.net/elon-musk-tiet-kiem-tien-cho-tuong-lai-la-vo-nghia-5138848.html)). Góc của mình: không cãi chuyện tương lai AI, chỉ hỏi chuyện tháng sau. Sách 5.27: quỹ 3–6 tháng chi tiêu, đếm bằng tiền mình xài mỗi tháng chứ không bằng lương (mức C, sách ghi là kinh nghiệm phổ biến). Chuyện thật của Hiệp (S-07): [CẦN HIỆP XÁC NHẬN].
- **B-bonghoa-02**: Mọi người đang khoe ảnh ngày xưa – bây giờ, nói về «dậy thì thành công» ngoại hình ([VTC News](https://vtcnews.vn/trao-luu-bien-hinh-dung-bao-gio-coi-thuong-bong-hoa-chua-no-tran-ngap-tiktok-ar1048255.html)). Góc của mình: đổi trước/sau ngoại hình thành trước/sau một thói quen. «Tuần thứ ba» chỉ là câu hỏi, câu trả lời không nêu số ngày hình thành thói quen (ràng buộc Deep Research 30/10).
- **B-donlientay-01**: Mọi người đang nói dọn trong lúc nấu là tính ngăn nắp, kèm hiệu ứng Zeigarnik ([X News](https://x.com/i/trending/2116206747459420656)). Góc của mình: tự nhận mình là «đội để mai» (P15). Không chia phe ngăn nắp hay bừa bộn. Sách 4.9 (Steel 2007, mức A): việc càng gây khó chịu càng dễ bị dời, nên làm lúc nó còn là một con dao, chưa thành cả bồn chén. Không dùng Zeigarnik (chưa tự kiểm).
- **B-30tuoi-01**: Mọi người đang ôn lại tuổi 20, đùa về mốc 30 ([X News](https://x.com/i/trending/2115259918806622394)). Góc của mình: mốc 30 là lúc dễ so nhất. Đổi câu hỏi từ «người ta có gì» sang «mình đã có gì». Fact lấy từ sách 3.20, chờ Deep Research.

## Plan stubs
- `plans/plan-1-musk-tiet-kiem-vo-nghia-quy-du-phong.json`: ✔ validate 9 cảnh, 58,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ trích câu của Musk + nguồn VnExpress, chỉ chữ). Ví dụ đời thường: lương, thẻ, gửi về nhà, tiền nhà, lệnh chuyển tự động. Sách 5.27 mức C. Không dùng số bảo hiểm tiền gửi của Trung Quốc.
- `plans/plan-2-don-lien-tay-viec-chua-kip-to.json`: ✔ validate 9 cảnh, 58,00s (stub-needs-approval). Trend ở b01 (thẻ «Dọn trong lúc nấu · clean as you go»). Ví dụ việc nhà: dao, chén, nồi, áo, tin nhắn. Sách 4.9 (Steel 2007, mức A).
- `check-rules.py --subjects ideas.json`: PASS (L-087).
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Elon Musk vừa nói tiết kiệm cho tương lai là vô nghĩa. Có thể đúng với ông ấy. Còn bạn, nếu tháng sau mất việc, bạn sống được mấy tháng?" (B-tietkiem-01, ý tưởng mới 5.27, DARK, caution)
2. "Đừng bao giờ khinh thường một bông hoa chưa nở. Vậy sao thói quen mới tới tuần thứ ba chưa thấy gì, bạn đã tính bỏ?" (B-bonghoa-02, clip-06, DARK)
3. "Có người nấu xong là bếp sạch luôn, vì thái hành xong họ rửa dao liền. Còn bồn rửa nhà bạn, tới tối đang chờ mấy cái?" (B-donlientay-01, 4.9, LIGHT)
4. "Hết năm nay, người sinh năm 1996 tròn ba mươi. Bạn đang đếm mình đã có gì, hay đang đếm người ta có gì?" (B-30tuoi-01, clip-22, DARK)

## Trạng thái đang chờ
- clip-06: Hiệp vẫn chưa chọn hook. Có bốn lựa chọn: B-kiennhan-01 (Justin Welsh «quit our own thing»), B-maxxing-01 («maxxing», Từ của năm), B-bonghoa-01/02 («bông hoa chưa nở», hôm nay lên báo lớn). Ràng buộc Deep Research: «tới tuần thứ ba» chỉ được là câu hỏi, không nêu số ngày.
- clip-22: B-ghenti-01 (growth over envy, ngày 2) vẫn chờ fact 3.20. B-30tuoi-01 là hook thay thế.
- clip-05 v9: trend là x-2114817316420805048 (không đổi). `final/trend-signals.md` cần đồng bộ khi chốt v9.

## Safety notes
- B-tietkiem-01: Musk chỉ nhắc trung tính, không ảnh, không chính trị (ảnh gốc VnExpress chụp ở Nhà Trắng, không dùng). Không khuyên đầu tư. Số 2,8 triệu lượt xem / 4.000 bình luận là lời VnExpress, chưa tự kiểm, không đưa vào voice. Phần AI «tiêu diệt nhân loại» trong bài báo: bỏ.
- B-bonghoa-02: không ngoại hình, không body, không tên hay ảnh người nổi tiếng.
- B-donlientay-01: Zeigarnik chỉ có trong tóm tắt X, không dùng.
- B-30tuoi-01: không so lương hay giá nhà, không chê ai chậm.
- California Fitness: người thật mất tiền và đang tranh chấp, nên chỉ để caution. Muốn dùng phải được Hiệp duyệt và không nêu tên công ty.
- Chính trị, tội phạm, bệnh, bi kịch, tiền ảo/vàng: bỏ.
