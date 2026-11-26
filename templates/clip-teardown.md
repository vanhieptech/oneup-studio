---
title: "Mẫu phân tích clip nhiều view (teardown)"
date: 2026-11-26
id: template.clip-teardown
type: template
status: ready
updated: 2026-11-26
tags: [template, trend, teardown, retention]
source: "oneup-studio: khung 11 mục (kế hoạch 26/11) + 5 phần phân tích video theo hướng dẫn Gemini Hiệp gửi 26/11 (đã chỉnh theo luật kênh)"
---
# Phân tích clip: <tên ngắn> (`<tiktok id>`)

Một file mỗi clip, lưu ở `research/trends/<YYYY-MM-DD>/teardowns/<id>.md` (+ `<id>.json` cùng cấu trúc). Mỗi mục ghi nguồn điền: **[Apify]** số liệu/phụ đề/comment, **[Gemini]** xem + nghe video (`pipeline/trends/teardown.py`), **[Claude]** tổng hợp. Mọi ý đánh dấu `quan sát` (thấy/nghe được, có mốc giờ) hoặc `suy đoán` (giải thích lý do). Không chép câu, hình, âm thanh vào clip của mình; chỉ mượn khung trừu tượng.

## 0. Chọn clip [Apify]
- Outlier: `play_count` ÷ trung vị view của creator (hoặc ÷ follower khi thiếu) = `<x>` (chỉ phân tích khi ≥ 3).
- Vì sao chọn cho kênh: chủ đề gần `<thói quen / học / trì hoãn / ngủ / tập trung / tiền>`.

## 1. Số liệu [Apify]
| link | creator (follower) | ngày đăng | độ dài | view | like | comment | share | save | share/view | sound |
|---|---|---|---|---|---|---|---|---|---|---|

## 2. Hook 0–3 giây [Gemini + Apify vtt]
- Câu nói đầu (nguyên văn từ phụ đề, chỉ để phân tích): …
- Chữ trên màn hình: …
- Hình / hành động gây chú ý (góc máy, biểu cảm, chuyển động): …
- Cơ chế tâm lý: tò mò · phản trực giác · đánh vào nỗi đau · kết quả gây sốc · khác: … (`suy đoán`)
- Kiểu hook: mã `P..` trong `research/trends/patterns.md` (hoặc đề xuất mã mới).
- Lời hứa ngầm với người xem: …

## 3. Xương sống theo mốc giờ [Gemini + Claude]
| mốc | vai trò (dẫn dắt · câu hỏi · chứng minh · lật kèo · giải thích · áp dụng · kết) | một câu tóm ý | cách chuyển sang đoạn sau |
|---|---|---|---|
| 0:00–0:03 | hook | | |
- Giây nào trả lời lời hứa của hook: …
- Vòng mở (open loop) mới ở đâu: …

## 4. Cách nói [Apify vtt + Claude]
- Ngôi kể, xưng hô: … · câu dài trung bình: … chữ · tốc độ: … chữ/phút
- Từ đệm, cách nối ý giữa các câu (ghi kiểu nối, không chép câu): …
- Cụm hay (ngắn < 10 chữ, kèm link) → đưa vào `resources/vn-spoken/phrase-bank.md` với nguồn.

## 5. Nhịp & ngắt nhịp (pattern interrupts) [Gemini]
- Trung bình bao nhiêu giây đổi góc máy / zoom / chèn hình / text mới: …
- Các điểm ngắt nhịp nổi bật: `0:04 SFX ting + zoom mặt` …
- **Dịch sang kênh:** @hi.oneup = đổi cảnh comic, hit motion + SFX (luật 50, 51), không quay, không B-roll (DL-027) · @vanhiep.tech = overlay `ov-*` / cutaway `cu-*` (`make-layer`).

## 6. Âm thanh & năng lượng [Gemini]
- Nhịp nói (nhanh/chậm, nhấn ở đâu), tone (tâm sự · tranh luận · chia sẻ kinh nghiệm): …
- SFX: … · Nhạc nền: chỉ ghi nhận (luật 21: clip mình không có nhạc trong file).

## 7. Kết thúc & CTA [Gemini + vtt]
- Kiểu kết: bất ngờ · loop về đầu · kêu gọi hành động · …
- Câu CTA: …

## 8. Comment [Apify]
- Người xem trích lại câu nào: …
- Họ hỏi gì / cãi gì: …
- Họ tự nói về nỗi đau ra sao (cụm ngắn kèm link, không ghi tên người comment) → bảng dịch thuật ngữ `research/explainers/<chủ-đề>.md`.

## 9. Vì sao nó chạy [Claude] (`suy đoán`, mỗi ý chỉ vào bằng chứng ở mục 2–8)
1. …

## 10. Mượn gì, không mượn gì
| mượn (khung trừu tượng) | không mượn |
|---|---|
| | câu chữ, hình, audio, nhân vật, tên kênh |

## 11. Công thức khung + chuyển sang kênh mình [Claude]
- Công thức 4–6 bước (dùng được cho chủ đề khác) → thêm/cập nhật trong `research/blueprints/` (`seen` +1).
- Áp cho @hi.oneup (comic + motion) hoặc @vanhiep.tech: …
- Hợp ý nào trong `content/idea-bank.md`: …
- Model đã dùng cho mục 2/3/5/6/7: `<tên model Gemini thật>` · ngày chạy: …
