---
id: lessons
type: log
updated: 2026-10-13
tags: [lessons, self-learning, qa, rule-49]
---
# Lessons: lỗi đã gặp → kiểm tra tự động (rule-49)

Đọc file này trước mỗi clip (skill make-video bước 0). Mỗi lần Hiệp góp ý/chê: **thêm hoặc cập nhật một lesson + check trong `pipeline/scripts/check-rules.py` trước khi sửa**. Check đo được thì là ✖ (chặn duyệt); chưa tự động được thì ghi `manual` và nêu cách soát tay.

Trạng thái: `automated` (có check, chặn) · `partial` (check một phần) · `manual` (soát tay theo checklist) · `open` (chưa xử lý xong).

| ID | Ngày | Triệu chứng (lời Hiệp / hiện tượng) | Nguyên nhân gốc | Cách sửa | Cách phát hiện | Check tự động | Trạng thái |
|---|---|---|---|---|---|---|---|
| L-001 | 2026-10-12 | "Xấu quá, kiểm tra lại" (preview đầu) | Gửi bản chưa tự soát, layout/typography thô | Chuẩn premium, tự xem và sửa ≥2 vòng, contact sheet mỗi lần gửi (DL-004, luật 34) | Có contact-sheet.png; agent tự xem frame | `L-001 contact-sheet` | partial |
| L-002 | 2026-10-12 | "Dùng đúng font"; dấu tiếng Việt chồng/vỡ | DM Sans/Poppins thiếu dấu tiếng Việt chồng | Mọi chữ dùng Be Vietnam Pro nhúng local (DL-005/006, luật 15) | Quét font-family/@font-face trong explainer + fonts.ts | `rule-15` (đã có) | automated |
| L-003 | 2026-10-13 | Caption chồng nhau / che mặt nhân vật | Hai đoạn caption cùng hiện một lúc; caption đặt trùng vùng mặt | Caption theo segment, một segment hiện một lúc; caption ở dải dưới, mặt ở trên | Plan: các `caption.segments` không giao nhau về thời gian; caption y không giao với hộp mặt (renderer đặt cố định) | `L-003 caption-overlap` | partial (vùng mặt: soát frame) |
| L-004 | 2026-10-13 | Highlight sai từ | Chỉ số `hl` lệch số từ của caption EN | Kiểm `hl` nằm trong số từ `en`, highlight từ khoá (không phải từ đệm) | Spec: mỗi index `hl` < số từ `en`; từ highlight không nằm trong danh sách từ chức năng | `L-004 highlight-index` | automated |
| L-005 | 2026-10-13 | Giọng đọc "Thì…", "hờt" lạ | Tag VieNeu `[cười]`/`[thở dài]` bị đọc thành chữ | Cấm tag trong lời; thể hiện bằng biểu cảm (DL-033) | Quét `[...]` trong text/say/phrases | `L-005 tts-tags` | automated |
| L-006 | 2026-10-13 | "Nói như máy" | Tổng hợp cả câu rồi tua 1,3× → phẳng cao độ, mất ngắt | Prosody theo cụm, không tua > 1,15× (DL-033) | tempo phrase ∉ [0.85, 1.15] hoặc câu không có `phrases`/không qua prosody | `L-006 tempo-range` | automated |
| L-007 | 2026-10-13 | F5 ra rác/im lặng ở cụm ngắn | F5 sinh từng cụm ngắn → hallucinate ("Cảm ơn các bạn"), take rỗng | Sinh nguyên câu rồi mới xử lý (DL-035) | Voice JSON engine F5 phải là v3 line mode; STT từng câu | `L-007 f5-line-mode` | automated |
| L-008 | 2026-10-13 | "Bị vấp" (sample F5) | Ghép cụm từ nhiều take, cắt giữa âm tiết theo timestamp whisper (44/54 mép cắt > −32 dB), silenceremove gọt phụ âm, rubberband trên đoạn ngắn | 1 take/câu, chỉ cắt ở lặng thật (< −32 dB), zero-crossing + fade 12 ms, bỏ silenceremove/rubberband cho F5 (DL-036) | Mỗi câu: tất cả phrase cùng `take`; quét click (bước nhảy mẫu > 0,35 đỉnh) và mép đoạn năng lượng cao | `L-008 audio-cuts` | automated |
| L-009 | 2026-10-13 | Lặp/mất âm tiết | TTS lặp từ hoặc nuốt từ (F5 nuốt "á") | Chọn take bằng STT trừ điểm lặp; re-roll | So STT câu với lời: số âm tiết thừa > 20% hoặc lặp từ liền nhau → ✖; thiếu > 25% → ✖ | `L-009 stt-repeat-drop` | automated |
| L-010 | 2026-10-13 | TOEIC đọc sai | TTS đọc chữ Latin theo kiểu Việt sai | Bảng phiên âm thuật ngữ (TOEIC → "tô ích", OK → "ô kê") trong `say`/`phrases` | Lời có thuật ngữ trong KEY_TERMS mà phần đọc không dùng phiên âm | `L-010 key-terms` | automated |
| L-011 | 2026-10-13 | Omi xuất hiện trong clip tuần < 5 | Dùng bản mẫu có Omi như clip đăng | Validator chặn Omi khi `week < 5` (luật 11) | Spec: speaker/cast `omi` và `week < 5` | `L-011 omi-week` | automated |
| L-012 | 2026-10-13 | Âm lượng không đều giữa các clip | Không chuẩn hoá loudness | −14 LUFS ±1, peak ≤ −0,5 dBFS (luật 4) | ebur128 trên MP4 | `rule-4` (đã có) | automated |
| L-013 | 2026-10-13 | "Push hết lên git" nhưng chưa lên | Mac offline, commit chỉ nằm trên box | Bundle + đẩy khi Mac online; báo rõ "chưa push" | `git rev-list origin/main..HEAD` > 0 | `L-013 push-pending` (cảnh báo, không chặn) | open |
| L-014 | 2026-10-13 | Skill HyperFrames "đã cài nhưng chưa dùng" | Không đọc skill/không chạy lint trước khi dựng explainer | Bắt buộc đọc skill + `hyperframes lint` 0 lỗi (DL-032) | Có `hf-check.txt` với 0 errors cạnh explainer | `L-014 hf-lint` | automated |
| L-015 | 2026-10-13 | Job trend báo cáo không gửi / quá ít nguồn | Kết quả không post vào chat; 5 nguồn, 41 tin | trend-collect v3, 33+ nguồn, báo nguồn lỗi (DL-029 v3) | Digest ngày có ≥ 20 nguồn OK | — (ngoài clip, xem skill trend-digest) | manual |
