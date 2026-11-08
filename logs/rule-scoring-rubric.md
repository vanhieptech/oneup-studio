---
title: "Rubric chấm điểm script video ngắn — ĐỀ XUẤT chờ Hiệp duyệt (chưa chốt)"
date: 2026-10-19
status: proposal-awaiting-hiep
source: "logs/rule-checklist.md (64 rule, commit 4a7c477) + logs/lessons.md L-001–L-058 + hiệu chuẩn clip-04 v04–v07"
id: rule-scoring-rubric
type: rubric
updated: 2026-10-19
---

# Rubric chấm điểm script — OneUp / @hi.oneup (ĐỀ XUẤT, chưa chốt)

> **Trạng thái:** bản đề xuất để Hiệp duyệt trọng số/ngưỡng. Chưa thay `logs/rule-checklist.md`, chưa sửa skill make-video. Không dùng rubric này để tự nói "Chốt"; chỉ Hiệp nói "Chốt" mới voice/render (P-12).

## 1. Research → nguyên tắc (phân biệt nguồn ngoài vs suy ra nội bộ)

| # | Nguyên tắc áp dụng | Bằng chứng / nguồn ngoài (URL) | Suy ra cho kênh này (nội bộ, chờ duyệt) |
|---|---|---|---|
| R1 | Thông điệp chính phải xuất hiện rất sớm; không có benchmark retention 3s phổ quát đáng tin — đừng bịa % | TikTok qua tổng hợp: >63% video CTR cao đưa thông điệp chính trong 3s — https://clouted.com/blog/tiktok-hook-performance-statistics ; cảnh báo số 71% bị diễn giải ngược — https://ethosengine.io/insights/three-second-hook-rule-what-platforms-measure | Chấm *nội dung* hook (pain + câu hỏi) ở script, không chấm % retention khi chưa có analytics của kênh |
| R2 | Mở đầu mạnh liên quan sâu tới độ xem hết, nhưng số liệu là dữ liệu tài khoản cụ thể, không chuyển nguyên sang kênh | MuseOn 10.000 video: retention trung vị 56% ở 3s, tương quan hạng 5s↔độ sâu xem 0,83 — https://www.museon.ai/blog/hooked-or-skipped | Trọng số hook cao nhất (20đ); ngưỡng retention thật chỉ đặt sau khi có dữ liệu @hi.oneup |
| R3 | Câu hỏi cụ thể tạo khoảng trống thông tin (information gap) kéo xem tiếp; payoff phải đóng lại ở cuối | CHI 2025 Curious Shorts — https://dl.acm.org/doi/10.1145/3706598.3713951 ; hook study TikTok (mẫu nhỏ, exploratory) — https://www.inspirajournals.com/uploads/Issues/2123118371.pdf | Hook 1 câu hỏi bám pain (P-05/P-06) + CTA/callback đóng vòng; hỏi lửng không mốc = trừ nặng |
| R4 | Chia đoạn (segmenting) + tín hiệu nhấn (signaling) giảm quá tải; caption cắt theo cụm cú pháp dễ đọc hơn cắt tuỳ tiện | Mayer segmenting/signaling — https://doi.org/10.1017/cbo9780511816819.012 ; subtitle segmentation (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7901653/ | Phrase 2–4/beat, vế ≤12 chữ, EN chunk ≤8 từ theo phrase (P-09); đây là ngưỡng nội bộ từ rule cũ, không phải hằng số khoa học |
| R5 | Văn nói trò chuyện, gọi người học trực tiếp, hiểu/transfer tốt hơn văn viết trang trọng | Personalization effect — https://doi.org/10.1037/0022-0663.96.2.389 ; tổng hợp Mayer ch.13 — https://www.cambridge.org/core/books/multimedia-learning/personalization-voice-and-image-principles/97F9B31362E6491806A4718FECCADE3D | Văn nói miền Nam, từ đời thường, cấm từ văn viết (rule-60); mức "tự nhiên" chấm manual bằng đọc to |
| R6 | Fact giáo dục phải đúng mức meta-analysis; testing effect là thật nhưng mức vừa, có điều kiện | Yang et al. 2021: 222 nghiên cứu, 48.478 HS, g=0,499 — https://doi.org/10.1037/bul0000309 / https://pubmed.ncbi.nlm.nih.gov/33683913/ | Nói "cao hơn mức vừa", cấm "hơn hẳn/chứng minh/nhớ hết"; mọi số phải có claim→source |

## 2. Đối chiếu với checklist hiện có

- **Map trực tiếp:** R1/R2/R3 → P-05, P-06, L-057, L-058, L-021/rule-55 (phần lời), L-030/rule-62, rule-56 · R4 → P-09, L-044, L-051, rule-58/61 · R5 → P-08, L-024/rule-60, L-052 · R6 → P-03, P-10, L-045, L-056, rule-40.
- **Mới hoàn toàn (chưa có trong 64 rule):** (a) thang điểm 0–100 + neo điểm từng hạng mục; (b) verdict 3 mức theo tổng điểm thay cho đạt/chưa đạt nhị phân; (c) quy tắc *cap* (lỗi nặng khoá trần điểm hạng mục dù tổng cao); (d) bảng hiệu chuẩn 4 bản v04–v07 đối chiếu verdict thật của Hiệp.
- **Xung đột giữ nguyên, không tự waive:** X-01 ngân sách từ (luật 7: 150–170 vs L-054: ~220–250 vs thực tế v07: 199) — rubric tạm chấm theo dải 190–210đ cho clip kiểu clip-04 và ghi chờ duyệt; X-02/C-3 rule-55 frame-0 (tầng spec, không tính vào điểm lời); C-1 credit (chờ Hiệp quyết, xem §4); C-2 tiểu từ (L-045 thắng quota rule-60 ở tầng lời); C-4 trend-signals/hashtag (tầng gói đăng).

## 3. Rubric 100 điểm (7 hạng mục)

Mỗi hạng mục chấm theo neo: **tối đa** = đạt hết mô tả; **giữa** = đạt ý chính nhưng còn 1 lỗi rõ; **thấp** = lỗi ở câu/beat gánh ý chính. Trừ điểm phải trích dòng.

| Hạng mục | Trọng số | Neo tối đa | Trừ điểm điển hình | Map rule | Đo |
|---|---:|---|---|---|---|
| A. Hook pain-point + câu hỏi | 20 | "Bạn" + pain phổ thông ở hiện tại ngay câu 1; đúng 1 câu hỏi cùng mốc/cùng phép thử; không kể lể "mình"; nhấn ở punch | Không câu hỏi −8; câu hỏi lửng ("nếu giờ…") −6; hook kể chuyện ngôi "mình" −8; pain ngách/chung chung −4 | P-05/P-06, L-057/58 | manual + regex đếm "?" khả thi |
| B. Mạch giữ xem tới cuối | 15 | Mỗi ý/fact/ví dụ 1 lần ở 1 beat; beat sau tiến ý mới; hook→payoff→CTA đóng vòng; beat ≤8s | Lặp 1 ý chính sang beat khác −3/lần; beat đóng kín như gạch đầu dòng −2; không callback/đóng vòng −3 | P-01, L-030/043/051/054, rule-62 | manual; đếm từ/ngram automated một phần |
| C. Rõ ý & chính xác logic (tiếng Việt nói) | 20 | Mọi câu đủ chủ thể+việc+kết quả/việc tiếp; chuỗi việc→kết quả→hệ quả đúng nguồn; không từ chung chung/hiếm gánh ý | Câu gỡ trách chung chung đứng một mình −5; từ mơ hồ gánh ý ("sai cách", "ít hiệu quả hơn mình tưởng", "lộ chỗ hổng") −2/cụm; câu cụt bắt đoán −2/câu | P-02/P-03/P-04, L-055/56, rule-58 | manual (không bịa automated cho nghĩa) |
| D. Fact / evidence / không hứa lố | 15 | Mọi claim chỉ vào được claim→source; đúng mức nguồn (g=0,499 = "mức vừa"); ví dụ đời thường ghi minh hoạ; thắng nhỏ đếm được | Nói quá mức nguồn −4; gắn số minh hoạ vào nghiên cứu −5; hứa kết quả ("nhớ hết", "nhẹ đầu") −3 | P-03/P-08, L-045/056, rule-40 | manual đối chiếu nguồn |
| E. Ngắn gọn & tải nhận thức / caption | 15 | Đúng ngân sách từ/thời lượng đã ghi trong file; 2–4 phrase/beat, phrase ≥3 chữ, vế ≤12 chữ; EN ≤8 từ/chunk, đúng thứ tự lời, hl đúng từ khoá | Vượt ngân sách >10% −4, >30% −8; phrase vụn/quá dài −2; EN chunk >8 từ hoặc lệch thứ tự −2/chunk | P-09, L-044/051/054, rule-4/7/9/58/61 | automated phần lớn (đếm từ, đếm EN, timing) |
| F. Tone mềm, nhấn, cảm xúc | 10 | Nói như kể với bạn; cảm giác/suy nghĩ thật từng chặng; nhấn 1–2/beat đúng từ gánh ý; ví dụ có chi tiết đo được | Beat 0 nhấn hoặc >2 nhấn −1/beat; beat bằng chứng khô như báo cáo −3; thiếu cảm xúc ở beat đau −2 | P-08, L-031/036/052, rule-63 | đếm `{nhấn:}` automated; tone manual đọc to |
| G. CTA & hồ sơ gate 1 | 5 | Đúng 1 CTA đo được (comment con số), không xin like/follow; có cột Hành động/Cảm xúc, bảng hiệu ứng, end card an toàn + credit | CTA xin tương tác −3; thiếu cột Hành động/Cảm xúc −2; thiếu end card −3 (xem thêm lỗi chặn) | rule-56, L-019/024, P-10 | automated một phần trên spec/post |

### Ngưỡng verdict (ĐỀ XUẤT — chờ Hiệp duyệt)
- **≥85, không lỗi chặn, không xung đột mở:** ĐẠT — trình Hiệp chốt.
- **75–84:** CHƯA ĐẠT (sửa nhỏ) — sửa đúng dòng, chấm lại, chưa trình.
- **60–74:** CHƯA ĐẠT (sửa vừa).
- **<60:** CHƯA ĐẠT (sửa lớn/viết lại beat lỗi).

### Lỗi chặn (hard gate — CHƯA ĐẠT bất kể tổng điểm)
1. Bịa số/cơ chế/nguồn, hoặc phóng đại mức evidence (P-03).
2. Chê năng lực người học ở lời/caption/post: "đầu dở/mình dở/bạn dở/kém/nhớ kém" và biến thể (P-07/L-053).
3. Thiếu dòng an toàn hoặc thiếu credit tác giả/CC BY 4.0 ở end card/gói đăng (P-10). *Biến thể wording credit đang tranh chấp (C-1) không phải "thiếu": ghi xung đột mở, verdict "đạt về điểm — chờ Hiệp quyết", không tự waive.*
4. Hook không có pain "bạn" + câu hỏi bám pain (kể lể ngôi "mình" ở hook) (P-05/P-06).
5. Làm voice/render/publish trước khi Hiệp nói "Chốt" (P-12) — lỗi quy trình, chặn cả gói.
6. Medical/legal/dosage/kết luận chuyên môn ngoài nguồn (rule an toàn gốc).

## 4. Hiệu chuẩn: chấm 4 bản clip-04 đối chiếu verdict thật của Hiệp

Verdict thật (từ chính file script + lessons, không bịa): v04 — Hiệp: "Dài dòng, lặp từ quá nhiều" (L-054) → chưa chốt. v05 — bị thay bởi v06 sau chê từ chung chung/thiếu rõ nghĩa (L-055/L-056; mục "Đã sửa" trong script-v06) → chưa chốt. v06 — chuỗi chê L-055→L-058 trên các trạng thái hook trong quá trình sửa + Rule Reviewer chấm CHƯA ĐẠT (nhấn lệch, thiếu cột, 210 từ) → chưa chốt. v07 — Rule Reviewer "đạt kèm xung đột", Hiệp **chưa** nói Chốt (chờ quyết C-1) → không tính là đã đạt cuối cùng.

| Bản | A/20 | B/15 | C/20 | D/15 | E/15 | F/10 | G/5 | Tổng | Verdict rubric | Khớp verdict thật? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| v04 (345 từ, ~95s) | 7 | 6 | 9 | 12 | 4 | 7 | 3 | **48** | Chưa đạt — sửa lớn | ✔ Hiệp chê dài/lặp |
| v05 (225 từ, ~65s) | 8 | 11 | 10 | 12 | 9 | 7 | 3 | **60** | Chưa đạt — sửa vừa | ✔ chưa chốt, bị chê chung chung |
| v06 (210 từ, ~62s) | 19 | 12 | 17 | 14 | 9 | 6 | 2 | **79** | Chưa đạt — sửa nhỏ | ✔ Reviewer chưa đạt |
| v07 (199 từ, ~59s) | 19 | 14 | 18 | 14 | 13 | 9 | 4 | **91** | Đạt về điểm — **chờ Hiệp quyết C-1** | ✔ chưa tự coi là chốt |

**Dòng trích làm neo (đạt/không đạt):**
- Không đạt (v04, L-055): "Không phải tại bạn đâu, bạn đang học {nhấn: sai cách} đó." — gỡ trách chung chung, không nói rõ không-phải-gì/là-gì → C trừ nặng.
- Không đạt (v05): "Bạn đang học {nhấn: sai cách} thôi." / "chỉ ít hiệu quả hơn mình tưởng" / "lộ ngay chỗ hổng" / "cho nhẹ đầu" — từ chung chung gánh ý chính; hook không có câu hỏi → A/C trừ.
- Không đạt trong quá trình v06 (ghi trong L-058, trạng thái trung gian không còn ở file cuối): "Nếu giờ hỏi lại, bạn nói ra được mấy ý?" — câu hỏi lửng không mốc → A trừ 6 theo neo.
- Đạt (v06 cuối → v07 giữ nguyên): "Bạn học tới khuya, đọc đi đọc lại tưởng thuộc hết rồi, sáng ra {nhấn: quên sạch}. | Sáng nay không mở sách, bạn tự nói lại được {nhấn: mấy ý}?" — pain "bạn" + 1 câu hỏi cùng mốc sáng/cùng phép thử.
- v06→v07 sửa đúng neo F/G: b03/b07/b08 từ 0 `{nhấn:}` thành 1 nhấn/beat; thêm cột Hành động/Cảm xúc; EN b05 sửa thứ tự "Do not be afraid / This is not an exam".

**Điểm v07 chi tiết (để Hiệp xem rubric có đúng ý):** A19 (hook khoá, trừ 1 vì punch còn phải chứng ở spec rule-55 — không tính điểm lời), B14 (cầu nối "thấp nhất" b05→b06 đúng 1 lần), C18 ("Giấy trắng chỗ nào, chưa thuộc chỗ đó" cụ thể; trừ nhẹ câu b05 dài gánh 2 xếp hạng), D14 (Yang/Dunlosky đúng mức vừa; ví dụ 30→4 ghi minh hoạ), E13 (199 từ/~59s; 35 chunk EN ≤7 từ), F9 (1–2 nhấn/beat), G4 (CTA comment con số; trừ 1 vì hashtag/C-4 thuộc gói đăng). **Xung đột mở:** C-1 credit, C-3 rule-55 tầng spec, C-4 hashtag/trend ở gói đăng.

## 5. Skill: đề xuất (chưa tự sửa)

- **Đã ghi trong repo:** rubric này (`logs/rule-scoring-rubric.md`) đủ tự chứa để dùng lại ở gate 1.
- **Đề xuất chờ Hiệp duyệt (không tự làm):** tạo `skills/rule-review/SKILL.md` (mirror theo `docs/conventions/storage.md`: bản chạy `/home/box/agent-data/workflows/rule-review/`) với các bước: đọc checklist + rubric → đếm automated (từ/EN/nhấn/grep chê năng lực) → chấm 7 hạng mục kèm trích dòng → kiểm lỗi chặn/xung đột → xuất verdict + bảng hiệu chuẩn khi sửa rubric. Lý do tách skill mới thay vì nhét vào make-video: make-video là workflow end-to-end (intake→render→post); chấm điểm là cổng độc lập dùng trước gate 1 và cả khi Hiệp chỉ gửi script lẻ. Cập nhật make-video chỉ nên là 1 dòng trỏ sang rule-review ở bước gate 1 — đề xuất, chờ duyệt.

## 6. Quyết định cần Hiệp duyệt (chưa chốt)
1. Trọng số A20/B15/C20/D15/E15/F10/G5 có đúng ý không (hiện C+A = 40% vì Hiệp chê nhiều nhất ở rõ nghĩa + hook)?
2. Ngưỡng 85/75/60 và việc "75–84 vẫn là CHƯA ĐẠT, chưa trình".
3. Danh sách lỗi chặn §3, đặc biệt: hook thiếu câu hỏi = chặn (không chỉ trừ điểm).
4. Ngân sách từ chuẩn để chấm E (X-01: 150–170 luật 7 vs ~199–250 thực tế L-054) — chọn một dải chính thức.
5. C-1 credit: giữ nguyên văn đã chốt hay theo rule-13 ("đã chuyển thể" + link giấy phép).
6. Có tạo skill `rule-review` như §5 không, hay chỉ giữ rubric trong `logs/`?
