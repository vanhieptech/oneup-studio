---
title: "Prompt + quy trình viết script @hi.oneup (dùng lại cho mọi clip)"
date: 2026-10-20
type: procedure
status: draft — chờ Rule Reviewer soát, chưa thay templates/script.md
source: "research/script-craft-opencreator-2026-10-20.md · research/tiktok-script-craft-2026-10-20.md · research/script-craft-2026-10-20.md · logs/lessons.md L-022..L-075 · logs/rule-checklist.md P-01..P-16, W-01..W-14"
---

# Prompt viết script @hi.oneup

Cách dùng: chạy **6 bước, mỗi bước là một lần gọi riêng** (viết nháp → chấm → sửa theo bản chấm; Anthropic chaining, Self-Refine). Bước chấm (5) do **một agent khác** làm, hoặc ít nhất một lần gọi riêng không thấy lý do của người viết. Mỗi lần Hiệp chê thì thêm một cặp vào `<examples>` và một dòng vào rubric, **trước** khi viết bản sau (rule-49, logs/lessons.md).

## 0. Brief (điền trước khi viết, thiếu ô nào thì chưa viết)

```xml
<brief>
  <item>HTB 23.14 — "Học xong gấp sách tự kiểm một lần, đừng quay đầu đọc lại" (mức A)</item>
  <one_sentence>Cả clip nói được trong 1 câu: …</one_sentence>
  <fact_lock>  <!-- chép nguyên văn từ fact-package, mỗi claim có nguồn + mức; KHÔNG thêm số -->
    - Yang 2021: 222 nghiên cứu, >48 ngàn học sinh; lớp có kiểm tra nhỏ điểm cao hơn lớp không làm kiểm tra nhỏ, mức vừa (mọi nhóm đều thi cuối)
    - Dunlosky 2013: tự kiểm tra nhóm cao nhất; đọc lại/gạch chân nhóm thấp nhất, vẫn có ích nhưng tác dụng hẹp
    - "quen mắt" chỉ được nói như câu tự hỏi có "hay"
  </fact_lock>
  <audience_pain>Nỗi đau phổ thông, ưu tiên lời thật trong comment/trend (dán link + nguyên văn)</audience_pain>
  <story_thread>Một việc cụ thể xuyên suốt: học gì, khựng ở đâu, payoff là đúng chỗ đó (W-06)</story_thread>
  <one_action>Một bước người xem làm được ngay hôm nay</one_action>
  <locked_by_hiep>Câu/lời Hiệp đã chốt nguyên văn (không được đổi nếu chưa hỏi)</locked_by_hiep>
  <budget>140–160 chữ VI; ~4,48 chữ/s F5 nói thuần → 150 chữ ≈ 41–42s giọng + 2s end card</budget>
  <tts_avoid>chột, xong, «Viết trước», từ tiếng Anh đứng một mình (<1s), «:» và «;» trong lời, tên tác giả trơ</tts_avoid>
</brief>
```

## 1. Prompt hệ thống cho người viết

```xml
<role>Bạn viết lời nói cho clip TikTok 40–50s của @hi.oneup: một người nói (Thầy), giọng miền Nam, mềm mà tập trung, như kể với bạn, đọc bằng F5-TTS.</role>
<hard_rules>   <!-- lỗi = chặn -->
1. Mọi câu đủ ai + làm gì (+ kết quả). Ngắn là bớt ý, không bớt chủ ngữ. Câu cùng người làm thì nối bằng phẩy/«rồi»/«nên». (W-09, L-071)
2. Không chê năng lực người học: cấm «dở/kém/nhớ kém/lười» về người xem; chỉ nói về cách học. (P-07, L-053)
3. Câu hỏi/điều kiện với người xem phải có từ dẫn mềm («giả sử», «thử», «nếu bây giờ», «lỡ như»), không mở câu bằng mệnh lệnh hay phủ định trơ. (W-10, L-073)
4. Mọi claim chỉ lấy từ <fact_lock>; không thêm số, cơ chế, «chứng minh», «nhớ hết». Ví dụ cá nhân phải là minh hoạ, không gắn vào nghiên cứu. (P-03, L-056, L-062)
5. Mỗi ý/fact/ví dụ nói đúng 1 lần. (P-01, L-054)
6. Không từ hiếm/văn chương, không văn viết («tức là», «lưu ý», «ngược lại»), không cụm mơ hồ («mọi thứ», «một cảm giác», «phần đó», «cách này» khi chưa nói là gì). (P-04, L-022, L-024, L-063)
7. Hook: nói thẳng nỗi đau của người xem (gọi «bạn»), nêu việc học chung trước, kèm một câu hỏi gắn đúng tình huống đó. Không mở bằng con số trơ, không bối cảnh ví dụ trong 3s đầu, không «nếu giờ…» lửng. (P-05, P-06, P-16, L-057, L-058, L-064)
8. «nha/nè/á» tối đa 1–2 lần cả clip; mỗi câu đúng 1 `{nhấn:}` ở từ gánh ý. (L-031, L-045, W-08)
</hard_rules>
<craft>   <!-- lỗi = trừ điểm -->
- Hứa kết quả cụ thể trước giây ~8 (≈35 chữ đầu). (W-11)
- Hết hook đến lúc nói cách làm ≤ ~50 chữ; cách làm tới trước giây ~15–20. (W-12)
- Nối beat bằng «nhưng / nên / vì vậy / hóa ra», không nối bằng «rồi thì». Xóa một beat mà mạch vẫn liền = beat thừa.
- Fact = câu trả lời cho chỗ khựng, 1 câu ≤ ~25 chữ: [nhóm của X] + [làm gì] + [thấy gì] + [mức]. Chức danh trước tên.
- Một chỗ xuống cảm xúc (khựng, câu cảm giác thật) và một chỗ lên (payoff). Đừng để năng lượng đều.
- Có 1 câu móc lại ở 30–60% thời lượng. (W-13)
- Kết: quay về đúng chỗ bí ở đầu; CTA một yêu cầu, người xem làm/comment được ngay trong 5 giây. (W-14)
</craft>
<examples>   <!-- 3–5 cặp, mỗi cặp: câu sai (lời thật đã bị Hiệp chê) → câu đúng → lý do -->
<example><bad>Tối đọc đi đọc lại. Tưởng mai nhớ hết.</bad><good>Tối đó mình đọc đi đọc lại, tưởng sáng mai nhớ hết.</good><why>Câu cụt, thiếu chủ ngữ (L-071)</why></example>
<example><bad>Không nhìn sách, bạn còn nhớ được những gì?</bad><good>Giả sử bây giờ không nhìn sách, bạn còn nhớ được những gì?</good><why>Mệnh lệnh cộc → điều kiện mềm (L-073)</why></example>
<example><bad>Không phải tại bạn đâu.</bad><good>Đọc lại nhiều lần làm chữ quen mắt, nhưng gấp sách thì chưa chắc tự viết ra được.</good><why>An ủi chung chung → nêu việc + hệ quả có nguồn (L-055, L-056)</why></example>
<example><bad>Ba mươi từ tối qua, sáng dậy chỉ còn bốn từ.</bad><good>Học thuộc tối qua, sáng dậy quên sạch?</good><why>Hook mở bằng số trơ, người lạ chưa biết chuyện gì (L-064)</why></example>
<example><bad>Dunlosky xếp các cách học: tự kiểm tra nằm nhóm cao nhất. Đọc lại, gạch chân nằm nhóm thấp nhất…</bad><good>Nên mình mới tin việc tự viết lại: nhóm của Yang gộp 222 nghiên cứu, thấy lớp có làm kiểm tra nhỏ thì điểm cao hơn, ở mức vừa.</good><why>Đoạn giảng hai nghiên cứu → một câu trả lời cho chỗ khựng (W-12, L-060)</why></example>
</examples>
```

## 2. Thứ tự làm (mỗi bước một output riêng, giữ lại trong file script)

1. **Danh sách nỗi đau (5 dòng).** Mỗi dòng: lời người học tự nói + nguồn (link comment/clip) hoặc ghi «suy luận». Chọn 1, ghi lý do.
2. **Viết 6–8 hook, mỗi hook một kiểu khác nhau** (lời người học tự nói · chấp nhận rồi «nhưng» · đối lập · lỗi tự nhận · kết quả trước · câu hỏi sắc · gọi đúng người xem). Chấm từng hook theo bảng H dưới đây. Lấy 1–2 hook cao nhất. Câu Hiệp đã chốt luôn nằm trong danh sách, ghi «chốt».
3. **Dàn beat** (chưa viết lời): mỗi beat ghi chức năng + 1 dòng ý + số chữ dự kiến + **chữ nối với beat trước** (nhưng/nên/…). Tổng ≤ 160. Kiểm: cách làm đến trước chữ thứ ~85.
4. **Viết nháp lời** theo dàn, đủ bảng 9 cột W-04 chỉ khi lời đã đạt (lời trước, sản xuất sau).
5. **Tự chấm bằng rubric R** (lần gọi riêng): ra bảng `dòng | luật | đạt/chưa | trích lời | cách sửa`, kèm `điểm rủi ro giữ người xem: giây | rủi ro | cách sửa` (mẫu ops120). Chỉ sửa đúng dòng bị chấm chưa đạt; không viết lại cả bài. Lặp tối đa 2 vòng, quá thì báo xung đột.
6. **Đọc to / kiểm F5:** đếm chữ bằng script; đọc to liền một hơi, đánh dấu chỗ vấp; quét `tts_avoid`; chỗ nào cần ngắt mà không có dấu câu → thêm phẩy. Sau đó mới giao Rule Reviewer.

### Bảng H — chấm hook (0–2 mỗi ô, tối đa 12; < 9 thì loại)

| Ô | 2 điểm khi |
|---|---|
| Người lạ hiểu | Đọc riêng câu đầu nói lại được clip nói gì + đau ở đâu (L-064) |
| Nỗi đau thật | Có lời thật trong comment/trend, hoặc là tình huống phổ thông ai cũng gặp (P-14) |
| Câu hỏi gắn tình huống | Cùng mốc, cùng phép thử; không có/không lửng, không rộng (P-06, shiyan521) |
| Mềm, không chê | Có từ dẫn mềm, không chê người (W-10, P-07) |
| Không tự đóng vòng | Hook không nói luôn đáp án (vòng mở được đóng ở payoff) |
| Đọc được trong ≤ 5s, F5 an toàn | ≤ ~22 chữ, không chữ tránh, không từ EN lẻ |

### Rubric R — chấm script (Đ = đạt / C = chưa; mọi ô «chặn» phải Đ)

| # | Mục | Chặn? | Cách kiểm |
|---|---|---|---|
| R1 | Fact chỉ từ fact lock, đúng mức, đúng nhóm so sánh; đã đọc đúng dòng trong file (L-062) | chặn | Bảng claim → nguồn từng beat |
| R2 | Mọi câu đủ chủ ngữ + động từ (W-09) | chặn | Bảng kiểm chủ ngữ từng câu |
| R3 | Không chê người học (P-07) | chặn | grep cụm cấm |
| R4 | Lời Hiệp đã chốt giữ nguyên văn, hoặc ghi rõ đã đổi để hỏi lại | chặn | So chuỗi |
| R5 | Hook đạt bảng H ≥ 9 và qua phép thử «người lạ» (P-05/P-16/L-064) | chặn | Bảng H |
| R6 | Điều kiện/câu hỏi với người xem mềm (W-10) | chặn | Rà câu có «bạn» |
| R7 | 140–160 chữ (W-14; F5 ≈ 41–45s) | chặn | Đếm bằng script |
| R8 | Hứa cụ thể trước ~35 chữ đầu (W-11) | — | Chỉ câu hứa; «một bước» chưa nói là gì thì chưa đạt |
| R9 | Hết hook → cách làm ≤ ~50 chữ; fact ≤ 1 câu ≤ ~25 chữ (W-12) | — | Đếm |
| R10 | Mỗi ý 1 lần, hook không bị beat sau nói lại (P-01) | — | Audit lặp |
| R11 | Beat nối bằng nhưng/nên…, không «rồi thì» (L-030/L-051) | — | Đọc chữ đầu beat |
| R12 | Một việc cụ thể xuyên suốt, payoff đúng chỗ bí (W-06/L-063) | — | Từng beat: làm gì, với cái gì |
| R13 | Có chỗ xuống + chỗ lên cảm xúc; có câu móc lại giữa clip (W-13, script-evaluator) | — | Đánh dấu 2 điểm |
| R14 | CTA 1 yêu cầu, làm/comment được ngay (W-14) | — | Đếm động từ yêu cầu |
| R15 | Không từ văn viết/hiếm/mơ hồ, không đại từ trơ (P-04) | — | `vn-words.py` + đọc tay |
| R16 | F5 an toàn: không chữ tránh, không «:»/«;», từ EN trong cụm dài, tên tác giả có chức danh | — | grep |
| R17 | «nha/nè» ≤ 1–2, đúng 1 `{nhấn:}`/câu (L-031, W-08) | — | Đếm |
| R18 | Caption EN ≤ 8 từ/chunk; end card an toàn + CC BY 4.0 (P-09, P-10) | chặn | Script đếm |

Kết quả: tất cả mục «chặn» Đ và ≥ 9/11 mục còn lại Đ → giao Rule Reviewer. Không thì sửa đúng dòng chưa đạt.

## 3. Định dạng output của người viết

```json
{"brief_ok": true, "pains": [...], "hooks": [{"type":"...", "text":"...", "H": {"nguoi_la":2,...}, "total":11}],
 "beats": [{"id":"b01","fn":"hook","link":"","words":20,"line":"...","est_s":[0,5]}],
 "word_count": 152, "rubric": [{"id":"R1","pass":true,"note":"..."}],
 "retention_risks": [{"t":"00:18","risk":"...","fix":"..."}], "open_questions_for_hiep": []}
```
(Cấu trúc JSON có giây từng đoạn lấy từ OpenCreator `scriptPrompt`; phần rủi ro lấy theo mẫu ops120 `review.py`.)

## Cập nhật 2026-10-20 (sau v18, Hiệp đã duyệt lời)

- **Thứ tự bắt buộc của các beat (W-16, L-077):** hook nỗi đau → ví dụ → nguyên nhân có dẫn chứng → mục tiêu, nói kiểu cá nhân («Mình cần là…») → cách làm → bằng chứng → kết quả quay về đúng chỗ bí → CTA khéo. Không đưa giải pháp lên trước vấn đề, dẫn chứng và mục tiêu. Bước 3 (dàn beat) phải theo đúng thứ tự này.
- **Một chữ chỉ mang một nghĩa trong cả clip.** Ví dụ «nhóm» đã dùng cho «nhóm đọc lại / nhóm tự kiểm tra» (nhóm trong thí nghiệm) thì không dùng thêm cho «nhóm của Yang» (nhóm tác giả), và ngược lại. Rubric thêm R19: quét các danh từ lặp, mỗi chữ phải giữ một nghĩa.
- **Caption (EN) và hình không được lộ chi tiết của beat sau.** Ví dụ chữ «luggage» không được hiện trên trang sách hay trong caption trước lúc lời nói ra nó. Rubric thêm R20.
- **Giữ chủ ngữ cả khi sửa theo góp ý của người chấm.** Bản sửa nào làm mất «mình/bạn/nhóm…» thì chấm lại R2 trước khi giao.
- **Tránh «xong»** (F5 đọc thành «sống»), cùng các chữ khác trong `tts_avoid`.
