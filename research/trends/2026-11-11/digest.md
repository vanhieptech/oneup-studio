---
title: "Trend digest 2026-11-11"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Treg TikTok (scrapecreators/tikhub)"
id: trends-2026-11-11
type: trend-digest
status: draft-needs-review
updated: 2026-11-11
tags: [trends, digest, daily]
date: 2026-11-11
collector: pipeline/scripts/trend-collect.py + X MCP + Treg
skill: trend-digest v4 (+ tiktok-research-via-treg, quyết định Hiệp 08/11)
---
# Trend digest 2026-11-11 (thứ Tư, ngày 11.11)

**Nguồn:** 34/36 collector ok. Lỗi: wiki-vi + wiki-en (HTTP 404, như các ngày trước). **X MCP: có chạy.** Trends VN 30 mục («Thứ 4», «Thứ Tư», «Sáng», «Lạnh», «Chào» là móc lịch/thời tiết; còn lại phim Thái, fandom, crypto, Xiaomi, Jensen Huang (scandal): bỏ). Worldwide 30 mục (Pocky/Pepero day Nhật–Hàn, chính trường Mỹ, thể thao: không dùng). 40 story X News từ 4 query (habits productivity, AI at work, Vietnam gen Z, burnout work life balance; max_age 72h). Gộp `x-extra.json` (100 mục), bản gốc trong `x-raw/` (+ 1 search post xác nhận biểu đồ cà phê).
**Treg TikTok: CÓ chạy (Treg-first).** 17 call, tổng **$0,0302** (balance 0,94007 → 0,90987, khớp): 11 keyword search ScrapeCreators ($0,00188), 4 video detail + transcript ($0,00188), 2 comments qua route tikhub ($0,001). 285 kết quả search. Transcript thật 3/4 detail; music 4/4 detail (đều original sound). **Không dùng Apify** (không thiếu capability, không lỗi). Chi tiết: `treg/README.md`, `treg/shortlist.json`.
**Giới hạn TikTok:** keyword search, không phải bảng xếp hạng hay For You feed. `region=VN` chỉ là proxy (trường region: VN 175 / TW 4 / ID, PK, FI 1 trên 182 dòng đầu). Ngày đăng thật 04–11/11. Lượt xem là snapshot lifetime lúc ~08:00–08:45 giờ VN, không chứng minh đang tăng. Comment là trang đầu theo thứ tự provider; mỗi comment là một lời tự kể. Query 11.11: 31/54 dòng là quảng cáo/livestream (is_ad).
**Số lượng:** collector 498 thô → 481 cụm. raw.json 486 mục (thêm 5 TikTok-native): 345 ok · 20 caution · 121 drop (60 drop tay + 1 TikTok). **365 qua lọc.** Drop tay: scandal đời tư CEO Nvidia (≈12 tin), thiên tai/lũ miền Trung, tàu mắc cạn, ung thư/nhãn y khoa, vụ án, chính trị VN/Mỹ/Iran, chính sách giáo dục (lớp chuyên theo môn, học phí: chính sách + L-087), «đi chùa online» (tôn giáo), chế giễu giọng/vùng miền, thuốc lá, tình dục, ADHD (nhãn y khoa).

Dữ liệu: `collect.json`, `collect-run.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `treg/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | X News «Caffeine Graph Reveals Lingering Effects on Sleep»: biểu đồ (của Charles Postiaux) mô phỏng caffeine còn trong người tới giờ ngủ; consensus: dừng trước trưa / 8–9 tiếng, tuỳ gen, «bạn không cảm thấy đâu» (các số 285 mg, 67 mg lúc ngủ, bán thải 5h, −45 phút chỉ có trong tóm tắt: **chưa tự kiểm**). Post xác nhận «went viral yesterday» (lượt tương tác thấp) | 0.891 | 1.0 / 0.1 | [X News 09/11](https://x.com/i/trending/2119903300115943689) · [@ebubxchii_](https://x.com/ebubxchii_/status/2120184557622133231) · [@NeoHealthApp](https://x.com/NeoHealthApp/status/2120126323054231749) | 3.4 / đăng #17 (hook mới) | DARK |
| 2 | TikTok «Dưới 30 tuổi nên xem» (listicle 4 điều, 7m20s; 718.650 xem, 72.448 like, 406 comment, 9.977 share, 22.968 save; đăng 06/11 23:06; transcript thật) | 0.722 | 1.0 / 0.1 | [TikTok @quocnguyenkieuvi](https://www.tiktok.com/@quocnguyenkieuvi/video/7705090431322787080) | 22.9 (+3.16) ý tưởng mới | LIGHT |
| 3 | X News «Does Life Improve After a Tough 20s? People Share Raw Stories» (caution: chuyện riêng, có thể có nội dung nặng) | 0.489 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2120064631528165536) | bằng chứng phụ cho #2 | — |
| 4 | Ngày 11.11: Genk «Cẩm nang săn sale 11.11: 4 bước chốt đơn» (bài PR Lazada) + cụm TikTok Shop «#TikTokShop1111 #SaleToVoDoi» toàn livestream quảng cáo (vd 559.984 xem, is_ad) | 0.482 | 1.0 / 0.3 | [Genk 10/11](https://genk.vn/cam-nang-san-sale-1111-4-buoc-chot-don-cho-nhung-tin-do-mua-sam-165261110162326102.chn) · [TikTok ad ví dụ](https://www.tiktok.com/@viettel_store_aar/video/7704631721861418258) | callback B-gachngang-01 (5.24) → 12.12 | DARK |
| 5 | X News «Short Daily Practice Builds Real Skills Over Time» | — | 1.0 / 0.4 | [X News](https://x.com/i/trending/2119987056231199205) | bằng chứng phụ 23.15 / clip-05 (không đẩy) | — |
| 6 | X News khỉ/mèo mệt mỏi + «Tuesday fatigue» + «Time change fatigue» (đổi giờ ở Mỹ, không áp dụng VN) | — | 1.0 / 0.7 | [X News](https://x.com/i/trending/2120307529058300058) · [X News](https://x.com/i/trending/2120148909045526691) | bão hoà (mệt mỏi đã pick 07/11) | — |
| 7 | TikTok @braincorevn «Uống cà phê lúc 4h chiều rồi thắc mắc sao 1h sáng chưa ngủ… Caffeine ở lại lâu hơn bạn nghĩ!» (404 xem, đăng 07/11; caption, transcript null) | — | 1.0 / 0.1 | [TikTok](https://www.tiktok.com/@braincorevn/video/7705277410563951878) | tín hiệu VN rất nhỏ cho #1 | — |
| 8 | TikTok @carter.selfdev «Bận rộn cả ngày mà không có gì cháy lên» (ẩn dụ kính lúp; 24.853 xem, đăng 05/11, transcript thật) | — | 1.0 / 0.3 | [TikTok](https://www.tiktok.com/@carter.selfdev/video/7704640861753068821) | pattern (clip đã tự nói bài học, không bridge) | — |
| 9 | X News «AI Boosts Tasks but Falls Short on Full Jobs» / «AI cut half entry-level jobs» | — | 1.0 / 0.7 | [X News](https://x.com/i/trending/2120229263949373596) | bão hoà (AI ở chỗ làm) | — |
| 10 | X News «Millennials Share Voicemail and Tech Habits» | — | 1.0 / 0.2 | [X News](https://x.com/i/trending/2120232637067297052) | bridge yếu, bỏ | — |

Đã xem và bỏ khỏi top: thói quen ngủ gật người Nhật (VnExpress, đã bỏ 09–10/11, có B-nap-01), Kenh14 «30 tuổi… thăng tiến» (nguồn Trung Quốc, chuyện phân biệt tuổi 35 → caution), Kenh14 «6 lý do khiến bạn luôn hết tiền» (bài cũ tháng 10 đăng lại), «làm phó TGĐ ngân hàng đu trend» (người thật, PR), số giờ làm việc mỗi người (bão hoà). Điểm `rank` của tin productivity tiếng Anh chung chung (Johns Hopkins, Brazil, ArcGIS…) là nhiễu heuristic.

## TikTok signals (Treg, snapshot 11/11 ~08:00–08:45 giờ VN)
| keyword | clip | xem / comment / share | hook / transcript (nguồn) | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| tuoi 20 met moi that bai | [@quocnguyenkieuvi](https://www.tiktok.com/@quocnguyenkieuvi/video/7705090431322787080) · đăng 06/11 23:06 · 7m20s | 718.650 / 406 / 9.977 | caption «Dưới 30 tuổi nên xem»; transcript thật (4 điều), điều cuối (trích nguyên văn transcript): «đừng tiêu thời gian cho những người chỉ biết rủ đi ăn chơi, nhậu nhẹt»; comment (trích nguyên văn, mỗi cái 1 lời tự kể): «khó, nói thiệt là khó. Dưới 30 khó mà vững tâm như vậy…» (2.377 like), «T đã bỏ được từ năm 22 tuổi, hầu như rất ít bạn bè luôn…» (242), «Tự chơi 1 mình không bạn bè» (133) | original sound (creator) | **caution**: KOL thật, không nêu tên/vẽ; bỏ lời khuyên hôn nhân/con/ngoại hình | B-gapnguoi-01 |
| ca phe buoi chieu mat ngu | [@braincorevn](https://www.tiktok.com/@braincorevn/video/7705277410563951878) · đăng 07/11 · 90s | 404 / 0 / 0 | caption (xem Top 10 #7); transcript null | original sound | ok; phạm vi rất thấp | B-cafe6h-02 (đỡ cho X) |
| uong ca phe mat ngu | [@trangxitrum5](https://www.tiktok.com/@trangxitrum5/video/7704547318439218439) · đăng 05/11 · 27s | 245 / 8 / 3 | caption «mất ngủ vì cafe nhưng sáng vẫn uống tiếp»; 8 comment = sticker, bạn bè | chưa lấy (search trim) | ok; vô dụng | — |
| ngoi van phong ca ngay | [@carter.selfdev](https://www.tiktok.com/@carter.selfdev/video/7704640861753068821) · đăng 05/11 · 88s | 24.853 / 11 / 133 | caption «Ánh nắng cả ngày không đốt nổi một tờ giấy, nhưng qua một chiếc kính lúp thì chỉ cần vài giây»; transcript thật | original sound | ok | pattern P11/ẩn dụ |
| san sale xong het tien | [@btvy_office](https://www.tiktok.com/@btvy_office/video/7705780920220978439) · đăng 08/11 · 21s | 177.038 / 35 / 1.314 | caption «đều hết tiền mà oke là saoo»; transcript là game → drop | original sound | drop (lạc đề) | — |
| san sale 11.11 / gio hang 11.11 | [@viettel_store_aar](https://www.tiktok.com/@viettel_store_aar/video/7704631721861418258), [@tunpham97](https://www.tiktok.com/@tunpham97/video/7704179845017718024) · 04–07/11 | 452.275 / – / –; 376.351 / – / – | quảng cáo/livestream (is_ad) «Cùng chờ đón 11h ngày 11.11» | chưa lấy | không trích, không vẽ người/thương hiệu | callback B-gachngang-01 |

Không gọi sound chart (series comic, không mượn audio). Sound metadata ≠ quyền dùng lại.

## Learning
- **Biểu đồ cà phê viral nhưng consensus đã dẫn đúng nghiên cứu Drake 2013 như sách 3.4**: fact không còn là điểm khác biệt. Góc phải đến từ 3.11 (ly 3 giờ chiều có việc của nó → giao cho 10 phút chợp mắt), không từ fact.
- **Listicle KOL «cắt bạn» bị chính mục sách 22.9 phản biện** (sách ghi 22.9 không mâu thuẫn 3.16: cắt mối làm cạn sức, giữ mối làm hồi sức) → hook P03 tốt; comment tự kể «bỏ xong không còn bạn» cho khoảnh khắc thật. F07 +1 (listicle «4 điều»).
- **Ngày 11.11 trên TikTok là quảng cáo:** search 11.11 chủ yếu is_ad livestream; ngôn ngữ nỗi đau phải lấy từ báo hoặc clip không phải ad. Không có clip «săn xong hối hận» nào đáng dùng (query «chốt đơn rồi hối hận», «săn sale xong hết tiền» ra game/giải trí).
- **Treg:** clip <1k view: comment là sticker/bạn bè → đừng trả tiền comment (trangxitrum5). Raw comments của tikhub có trường `cookie` / `tt_chain_token` của provider → redact trước khi commit.
- Bão hoà nên tránh: mệt mỏi/khỉ mệt (07/11), AI ở chỗ làm, giờ làm việc, «15 phút mỗi ngày» (đã có clip-05), so sánh 3.20.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-cafe6h-02 | X «Caffeine graph» (+ TikTok @braincorevn) | 3 giờ chiều ở văn phòng, mắt díp lại, đồng nghiệp rủ order cà phê sữa đá | 3.4 (mức A) + 3.11 (mức B) | "Ly cà phê ba giờ chiều giúp bạn qua cơn buồn ngủ, mà tối lại nằm mãi mới ngủ được? Mấy hôm nay có một biểu đồ cà phê lan khắp mạng: cà phê ở lại trong người lâu hơn cơn tỉnh rất nhiều." (P10 + P03) | contrarian / data | **đăng #17 (3.4, DARK, tuần 3)** — hook trend mới cho góc B-cafe6h-01, **không phải góc mới** | DARK |
| B-gapnguoi-01 | TikTok «Dưới 30 tuổi nên xem» + comment «bỏ được từ năm 22 tuổi, hầu như rất ít bạn bè» | tối thứ Sáu từ chối cuộc nhậu, tháng sau nhóm thôi rủ, cuối tuần chỉ còn mình với điện thoại | 22.9 (mức A, quan sát) + 3.16 (mức C) | "Một clip hơn bảy trăm nghìn lượt xem đang khuyên người dưới ba mươi: bớt thời gian cho những người chỉ rủ đi ăn chơi, nhậu nhẹt. Mà dưới comment, có người kể mình bỏ được từ năm hai mươi hai, giờ gần như chẳng còn bạn." (P03 + F07) | contrarian / empathy | ý tưởng mới 22.9 (ngoài 30 ô; trụ 4) | LIGHT |
| B-gachngang-01 (callback) | ngày 11.11 (Genk PR + cụm ad TikTok Shop) | mở app sale thấy giá gạch 999 còn 499 là bấm đặt | 5.24 (+5.23, mức C) | giữ hook cũ (21/10) | contrarian / data | chuyển đích sang **12.12 / Black Friday** (11.11 đã qua) | DARK |

Cầu nối về trục kênh (trend chỉ là móc): B-cafe6h-02 → +1 là dời ly cà phê cuối lên trước 2 giờ chiều một tuần, và chợp 10 phút khi buồn ngủ chiều. B-gapnguoi-01 → +1 là tuần này hẹn một người bạn đi bộ/ăn sáng lúc đang vui. B-gachngang-01 → không phải tư liệu mới, chỉ là callback. Không trùng 08–10/11 (thức khuya #14, hết năm #27, Chủ nhật #24, Kim Dung #27, lương 31tr #28, phím tắt #13, không đi làm 12.24, penalty #21).

**Tách lớp bằng chứng:** (a) trend = X News + post X + clip/comment/transcript TikTok ở trên (số TikTok lấy từ Treg; số trong tóm tắt X ghi «chưa tự kiểm», không vào voice); (b) fact sách = 3.4 (Drake et al. 2013, Gardiner et al. 2023, mức A; sách ghi Drake 1 lab, liều cao, người chuyển hoá chậm cần sớm hơn), 3.11 (Brooks & Lack 2006, mức B, 1 nghiên cứu lab), 22.9 (Holt-Lunstad et al. 2015, mức A nhưng quan sát; OR ≈1,26–1,32 với tử vong; chưa có RCT), 3.16 (Rook 1984, mức C); (c) cầu nối, hook, câu «giao việc của ly cà phê cho 10 phút chợp mắt» và «cắt cuộc nhậu, đừng cắt người» = đề xuất biên tập của Social Research, chưa phải fact. Deep Research cần kiểm (b) trước khi OpenCreator viết.

## Differentiation
- **B-cafe6h-02:** Mọi người đang nói: dừng cà phê trước trưa hoặc 8–9 tiếng trước ngủ, tuỳ gen, và «bạn sẽ không cảm thấy đâu» ([X News 09/11](https://x.com/i/trending/2119903300115943689); [@NeoHealthApp](https://x.com/NeoHealthApp/status/2120126323054231749) dẫn Drake). Góc của mình: không bắt nhịn bằng ý chí; ly 3 giờ chiều đang làm một việc (đẩy cơn buồn ngủ chiều) → giao việc đó cho 10 phút chợp mắt (3.11, consensus không nhắc), callback #16. Thân bài có thể dùng lại khung `2026-10-20/plans/plan-2-ca-phe-6-tieng.json`; khác B-caphesang-01 (cà phê buổi sáng, 29/10).
- **B-gapnguoi-01:** Mọi người đang nói: dưới 30 hãy bớt người chỉ rủ ăn chơi, nhậu nhẹt, tìm môi trường kỷ luật ([TikTok 06/11](https://www.tiktok.com/@quocnguyenkieuvi/video/7705090431322787080)); comment đồng tình «khó, nói thiệt là khó». Góc của mình: không cãi chuyện bớt nhậu; thêm phần clip không nói: bớt cuộc nhậu khác bớt người, sách xếp gặp người đều đặn ngang một khoản chi cho sức khoẻ và tự ghi không mâu thuẫn với việc cắt mối làm cạn sức. Khác B-hoplop-01 (họp lớp, 14/10), B-home-01 (ở nhà, 15/10), B-noikhong-01 (3.16, từ chối lời nhờ).

## Plan stubs
- `plans/plan-1-bieu-do-ca-phe-ly-ba-gio-chieu.json`: ✔ validate 9 cảnh, 63,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ đề xuất «Biểu đồ cà phê · X 09/11» (L-084); hình gợi ý: đồng hồ comic với ly cà phê mờ dần theo giờ tới lúc ngủ (vẽ lại ý, không chép biểu đồ). Ví dụ đời thường: văn phòng 3 giờ chiều, cà phê sữa đá, chợp mắt. Tuần 3, không Omi. Theme dark.
- `plans/plan-2-cat-cuoc-nhau-dung-cat-nguoi.json`: ✔ validate 9 cảnh, 62,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ «TikTok 06/11 · "Dưới 30 tuổi nên xem"» (L-084, không tên KOL); comment ở b02 là **diễn giải** lời tự kể (gốc: «T đã bỏ được từ năm 22 tuổi, hầu như rất ít bạn bè luôn»). Ví dụ: cuộc nhậu tối thứ Sáu, điện thoại, đi bộ/ăn sáng. Không Omi. Theme light. Beat b06 có chữ «tử vong» (đúng số liệu sách) → Deep Research / Rule Reviewer / Hiệp quyết giữ hay bỏ.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087).
- Độ dài stub ~60s chỉ là khung; độ dài thật theo L-099 (<300s, mục tiêu 2–3 phút) do OpenCreator quyết sau khi Deep Research kiểm. Mã pattern là đề xuất; Rule Reviewer/OpenCreator vẫn lập bảng hook thực ↔ P/F (L-100). Stub không cho phép tạo hình, giọng, render hay đăng trước Chốt.

## Script hooks (cần Hiệp duyệt)
1. "Ly cà phê ba giờ chiều giúp bạn qua cơn buồn ngủ, mà tối lại nằm mãi mới ngủ được? Mấy hôm nay có một biểu đồ cà phê lan khắp mạng: cà phê ở lại trong người lâu hơn cơn tỉnh rất nhiều." (B-cafe6h-02, 3.4, đăng #17, DARK).
2. "Một clip hơn bảy trăm nghìn lượt xem đang khuyên người dưới ba mươi: bớt thời gian cho những người chỉ rủ đi ăn chơi, nhậu nhẹt. Mà dưới comment, có người kể mình bỏ được từ năm hai mươi hai, giờ gần như chẳng còn bạn." (B-gapnguoi-01, 22.9, ý tưởng mới, LIGHT). Caution KOL.
3. (phụ, không stub) callback B-gachngang-01 cho 12.12: "Giá gạch từ 999 ngàn xuống còn 499 ngàn, bạn thấy mình vừa lời được năm trăm ngàn, đúng không?" (5.24, DARK).

## Safety notes
- B-cafe6h-02: không nói bệnh/mất ngủ lâm sàng, không khuyên bỏ hẳn cà phê; không dùng số trong tóm tắt X (67 mg, 285 mg, 5 giờ); không chép biểu đồ gốc (vẽ lại ý).
- B-gapnguoi-01: không nêu tên, không vẽ, không lồng tiếng KOL; không dùng phần hôn nhân/con cái/ngoại hình của clip; không chê người hay nhậu; số tử vong là quan sát, không đưa vào hook.
- 11.11: không trích/vẽ KOL bán hàng, thương hiệu, livestream; số «sale 3–15/11» trong caption ad: chưa tự kiểm.
- Chính trị, thiên tai, tội phạm, bệnh, scandal đời tư, tôn giáo, chế giễu vùng miền/giọng, thuốc lá, tình dục, chính sách giáo dục: bỏ.

## Trạng thái đang chờ
- Đăng #17 (3.4): B-cafe6h-01, **+ B-cafe6h-02 (hook trend mới)**. Ý tưởng mới 22.9: **B-gapnguoi-01**. B-gachngang-01 (5.24): đổi đích sang 12.12.
- Hôm nay thứ Tư: không có weekly synthesis.
