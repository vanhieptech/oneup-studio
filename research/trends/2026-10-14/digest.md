---
id: trends-2026-10-14
type: trend-digest
status: draft-needs-review
updated: 2026-10-14
tags: [trends, digest, daily]
date: 2026-10-14
collector: pipeline/scripts/trend-collect.py + X MCP extra + Wikipedia fallback (ngày 12/10)
skill: trend-digest v3
---
# Trend digest 2026-10-14

**Nguồn:** 36/38 chạy được (33 nguồn trong sources.yaml + 3 nguồn X qua MCP + 2 Wikipedia lấy bù ngày 12/10). Lỗi: `wiki-vi`, `wiki-en` trả 404 vì Wikimedia chưa ra số liệu ngày 13/10 lúc 7:56 sáng giờ VN (00:56 UTC); đã lấy bù top pageviews ngày 12/10. Bỏ qua theo quy định: TikTok Creative Center, Reddit, rsshub.app.
**Số lượng:** 514 mục thô → 484 cụm → 393 qua lọc (370 ok · 23 caution) · 91 drop (62 do lọc từ khoá + 29 lọc tay: tưởng niệm/chính trị, bệnh của người có tên, tội phạm, bê bối, chiến sự). Shortlist đọc tay: 23 mục.
**X:** trends VN (20) + worldwide (20) + 29 story X News từ 3 truy vấn (habits/productivity, AI at work, Vietnam gen Z), max 72h.
Dữ liệu: `collect.json`, `x-extra.json`, `raw.json` (đã chấm bằng trend-learn.py; mục ngoài shortlist bị giới hạn fit ≤0.4 vì chưa đọc tay), `score.txt`.

## Top 10 (đã lọc, bỏ mục pattern-evidence)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Lời khuyên "vào họp cứ nói, nói đại cũng được" gây tranh cãi | 0.825 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2110082413669781821) | 4.5 agenda, họp ngồi dài hơn 34% · 4.6 bớt họp | DARK |
| 2 | IMF: AI chạm ~40% việc làm; call center giảm; "AI lấy việc thì đổi nghề gì?" | 0.621 | 1.0 / 0.23 | [X News IMF](https://x.com/i/trending/2109519588488589399), [call center](https://x.com/i/trending/2108736245752816097), [pivot](https://x.com/i/trending/2109131951491944621) | 23.10 chọn kỹ năng cần tay chân, phán đoán tại chỗ | DARK |
| 3 | Dân trade: kỷ luật, quy trình hơn động lực; giữ việc chính khi làm side | 0.584 | 1.0 / 0.17 | [X News](https://x.com/i/trending/2110056148217041263), [day job](https://x.com/i/trending/2109662429584249056) | 4.2 viết điều kiện dừng trước khi bắt đầu | LIGHT |
| 4 | Nghỉ mạng xã hội có đáng? (+ Tiền Phong: Gen Z đánh đổi gì cho giờ sống trên mạng) | 0.568 | 1.0 / 0.25 | [X News](https://x.com/i/trending/2109743689849282611) | 3.20 giới hạn app xem đời người khác · 4.15 | DARK |
| 5 | 10.000 bước/ngày có thực tế? (ngày thứ 2) | 0.533 | 1.0 / 0.30 | [X News](https://x.com/i/trending/2109372046493003926) | 2.17 (clip 18) | LIGHT |
| 6 | Sếp ôm thêm việc vì cấp dưới lạm dụng AI (ngày 2, 2 nguồn) | 0.507 | 1.0 / 0.25 | [VnExpress](https://vnexpress.net/sep-om-them-viec-vi-cap-duoi-lam-dung-ai-5130995.html) | 4.7 (clip 3) | DARK |
| 7 | "Năng suất tuổi trưởng thành = thử mẹo tâm lý mới liên tục" (ngày 2) | 0.505 | 1.0 / 0.25 | [Bluesky](https://bsky.app/profile/astrokatie.com/post/3mxh6wwsuku27) 3,7k like | 4.12 (clip 6) | DARK |
| 8 | Tranh cãi iPhone 18 Pro mất dần sức hút (2 nguồn + Google Trends VN) | 0.497 | 1.0 / 0.15 | [VnExpress](https://vnexpress.net/tranh-cai-iphone-18-pro-mat-dan-suc-hut-5131460.html) | 5.23 chờ 24 giờ trước món to · 6.24 | LIGHT |
| 9 | Vì sao ngày càng ít người đi họp lớp | 0.495 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/vi-sao-ngay-cang-nhieu-nguoi-khong-con-to-chuc-hay-tham-gia-cac-buoi-hop-lop-21526101318104287.chn) | 22.9 gặp người định kỳ là chi cho sức khoẻ | LIGHT |
| 10 | Google thử vòng phỏng vấn đọc code lạ có Gemini (chi tiết từ X News, cần kiểm) | 0.480 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2109399914962694292) | 23.19 tự kiểm theo cách sẽ dùng | LIGHT |

Đáng để ý (caution): [Microsoft được cho là cắt nhóm R&D tại VN](https://vnexpress.net/microsoft-sa-thai-nhan-su-tai-viet-nam-5131896.html) (3 nguồn: VnExpress, CafeBiz, Genk) → 5.27 quỹ khẩn cấp 3–6 tháng, chỉ góc đồng cảm · [Nhân viên lương 19 triệu chi 9 triệu làm phòng ngủ](https://kenh14.vn/nhan-vien-van-phong-luong-19-trieu-chi-9-trieu-lot-xac-phong-ngu-215261013114816225.chn) (không phán xét người thật) · [Shipper giao hàng 6.935 ngày](https://kenh14.vn/tai-san-o-que-cua-shipper-sn-1973-giao-hang-lien-tuc-suot-6935-ngay-215261013223224713.chn) (4.12, số đẹp đối lại "21 ngày") · [Giận giúp làm việc khó tốt hơn?](https://x.com/i/trending/2109703683294339093) (3.23, sách nói xả giận bằng vận động không hạ hoả) · #2026MAMAVOTE top X VN (fandom, chỉ dùng làm "thức tới 2h", 3.9).

## Learning
- **Pattern mới:** P10 "Tưởng tượng: bạn cố hết sức mà vẫn…" (3 hook X News cùng dạng) · P11 "Lời khuyên X đang gây bão, hai phe cãi, hông ai hỏi câu gốc" (họp, 10k bước, Gen Z stare). Format mới F05: comic chia hai phe.
- P03 "Ai cũng nói X, sách nói Y" mạnh nhất ngày thứ 2 liên tiếp (seen 5). P04 thêm 2 (IMF 40%, call center −4%/năm).
- **Bão hoà, tránh góc thẳng:** "trì hoãn không phải lười" (YT VN: 1,41M · 833k · 675k cùng một góc, ngày thứ 2) · "how to REALLY stop procrastinating" EN · 10k bước (ngày 2) · "AI lấy việc" nói chung (nhiều nguồn cùng một giọng lo sợ) · study-with-me / lock in.
- Hai ngày liền có chủ đề AI (hôm qua plan-1 AI code). Hôm nay chọn stub không phải AI để đổi góc so với 3 clip gần nhất.

## Bridges (khác biệt)
| id | Trend → khoảnh khắc | Bài học | Mọi người đang nói | Góc của mình | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|---|
| B-meeting-01 | #1 → ngồi họp cả tiếng nói một câu cho có | 4.5 + 4.6 | Phe "cứ nói cho sếp thấy" vs phe "lời khuyên tệ, giả mất mic để chuồn" ([X](https://x.com/i/trending/2110082413669781821)) | Cả hai phe coi cuộc họp là đương nhiên; sách hỏi trước: có agenda chưa, có cần ngồi không (họp ngồi dài hơn 34%, quyết định như nhau; thí nghiệm nhóm 5 người) | "Lời khuyên đang gây bão nè: vào họp thì cứ nói, nói đại cũng được, miễn sếp thấy bạn có mặt." (P11+P04) | humor / data | DARK | ý tưởng mới, trụ 2 |
| B-exit-01 | #3 → cắn răng đẩy tiếp một việc đã hỏng | 4.2 | Động lực thì hết, kỷ luật và quy trình mới bền ([X](https://x.com/i/trending/2110056148217041263), [X](https://x.com/i/trending/2109288556262821898)) | Kỷ luật không có điều kiện dừng dễ thành cố đấm; viết sẵn "tới ngày X chưa đạt Y thì dừng" lúc còn tỉnh. Chuyện OneUp `[CẦN HIỆP XÁC NHẬN]` (S-02) | "Mấy hôm nay ai cũng nói: động lực thì hết, kỷ luật mới ở lại." (P03) | contrarian / story | LIGHT | ý tưởng mới, trụ 1 |
| B-aijob-01 | #2 → lo AI lấy việc, tính học gì | 23.10 | AI sẽ thay 40% việc / học AI hoặc mất việc / đổi sang nghề cần người | Đừng hỏi "nghề nào chết", hỏi việc của bạn cần tay chân, sáng tạo, giao tiếp tới đâu; sách ghi con số 47% cũ đã bị nghiên cứu sau hạ thấp nhiều | "Đừng hỏi nghề nào chết. Hỏi việc của bạn cần tay chân và phán đoán tại chỗ tới đâu." (P04→P03) | data / contrarian | DARK | ý tưởng mới, trụ 5 |
| B-scroll-01 | #4 → lướt đời người khác trước khi ngủ | 3.20 | Nghỉ hẳn mạng xã hội mới khoẻ / nghỉ là làm màu | Hông cần bỏ hẳn: thử nghiệm giới hạn 10 phút mỗi app trong 3 tuần thì cô đơn và trầm cảm giảm (143 sinh viên, chỉ một nghiên cứu) | "Hông cần bỏ mạng xã hội. Thử 10 phút mỗi app, 3 tuần." (P03) | data / empathy | DARK | clip-22, hook thay thế |
| B-hoplop-01 | #9 → ngại đi họp lớp | 22.9 | Họp lớp là khoe khoang, so bì nên bỏ cũng được | Bớt quan hệ làm mình mệt (3.16), nhưng giữ vài cuộc gặp làm mình hồi sức; ít giao tiếp đi kèm rủi ro tử vong cao hơn ~30% (quan sát, không phải nhân quả). `[CẦN HIỆP XÁC NHẬN]` S-06 | "Họp lớp ngày càng vắng. Mà gặp người thường xuyên là khoản chi cho sức khoẻ đó." (P03) | empathy / data | LIGHT | ý tưởng mới |
| B-iphone-01 | #8 → muốn đổi máy vì tin đồn | 5.23 / 6.24 | iPhone 18 đáng hay không đáng nâng cấp | Câu hỏi không phải máy mới tốt cỡ nào, mà là đợi 24 giờ rồi còn muốn hông, và có phải mua để "lên một bậc" với bạn bè | "iPhone 18 chưa ra, mà bạn đã muốn đổi máy chưa?" (P01) | humor | LIGHT | ý tưởng mới |
| B-interview-01 | #10 → luyện thuật toán mà đi làm toàn đọc code người khác | 23.19 | Google đổi cách phỏng vấn, dân dev lo luyện cả hai | Tự kiểm theo đúng cách sẽ dùng; cần kiểm nguồn gốc tin trước khi viết | "Google thử phỏng vấn bằng đọc code lạ. Bạn đang luyện đúng thứ sẽ phải làm chưa?" (P04) | data | LIGHT | ý tưởng mới |

## Plan stubs (đều ✔ validate)
- `research/trends/2026-10-14/plans/plan-1-hop-khong-agenda.json` (B-meeting-01, 8 cảnh, 48 giây, DARK, tuần 2). ✔ `npm run validate`.
- `research/trends/2026-10-14/plans/plan-2-ky-luat-thieu-mot-dong.json` (B-exit-01, 7 cảnh, 44 giây, LIGHT, tuần 1). ✔ `npm run validate`.
Cả hai `status: stub-needs-approval`, có một beat chuyện thật để trống `[CẦN HIỆP XÁC NHẬN]`. Không dùng Omi (tuần < 5). Explainer HyperFrames ghi trong `ideas.json`.

## Script hooks (cần Hiệp duyệt)
1. "Lời khuyên đang gây bão nè: vào họp thì cứ nói, nói đại cũng được, miễn sếp thấy bạn có mặt." (B-meeting-01)
2. "Mấy hôm nay ai cũng nói: động lực thì hết, kỷ luật mới ở lại. Đúng, mà còn thiếu một dòng." (B-exit-01)
3. "Đừng hỏi nghề nào chết. Hỏi việc của bạn cần tay chân và phán đoán tại chỗ tới đâu." (B-aijob-01)
4. "Hông cần bỏ mạng xã hội. Thử 10 phút mỗi app, 3 tuần." (B-scroll-01)

## An toàn
Lọc tay thêm 29 mục bộ lọc từ khoá bỏ sót: lễ truy điệu ở công viên Lê Thị Riêng (Google Trends VN, VnExpress, Dân Trí, Thanh Niên), bệnh của Giáo hoàng, khoản thu nhập của chủ tịch FIFA, tài tử Breaking Bad qua đời, các mục chính trị Mỹ/Brazil/Ấn Độ, tội phạm. Caution: Microsoft cắt nhân sự (người mất việc), phòng ngủ 9 triệu (người thật), fandom MAMA, "salt stomping" giúp ngủ (tuyên bố sức khoẻ không nguồn), A2O thần tượng 13 tuổi (không dùng).

## Đề xuất sửa công cụ (chờ Hiệp, không tự sửa)
- `trend-collect.py` nguồn wiki: khi ngày hôm qua trả 404 thì tự lùi về 2 ngày trước (job chạy 7:55 sáng VN, trước giờ Wikimedia ra số).
- `trend-learn.py score` chỉ đọc `raw.json` của các ngày trước, nên mục trong `2026-10-13/raw.v2.json` không được tính trùng (vì vậy novelty hôm nay đều 1.0; mục "ngày 2" đã được cộng saturation_signal bằng tay). Đề xuất đọc thêm `raw.v*.json`.
