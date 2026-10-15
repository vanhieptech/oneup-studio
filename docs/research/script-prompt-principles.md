---
id: research.script-prompt-principles
type: research
status: Hiệp đưa (prompt YouTube scriptwriter), chuyển thể cho TikTok ~45s tiếng Việt; áp dụng từ clip-02 v7
updated: 2026-10-15
---
# Nguyên tắc viết kịch bản (từ prompt Hiệp gửi), bản cho TikTok ~45s

Lý do: Hiệp chê clip-02 nghe "giả trân". Nguồn gốc: một prompt "YouTube scriptwriter" Hiệp chia sẻ (17:4x 15/10). Dưới đây là phần cốt lõi, đã chỉnh cho clip 40–48s, ~110–130 chữ.

## 1. Cấu trúc (bắt buộc, khai trong `spec.structure`)
| Phần | Độ dài ~45s | Việc phải làm |
|---|---|---|
| Hook | ≤ 2 câu, 0–3s | Bắt tai, mở một khoảng trống thông tin (câu hỏi người xem muốn biết đáp án) |
| Intro | 1 câu | Vì sao nên coi tiếp; mở vòng (open loop), có thể callback clip trước |
| Body: vấn đề | 1–2 câu | Chuyện thật, cụ thể |
| Body: khám phá | 2–3 câu | Đi tìm nguyên nhân, có nghiên cứu/số liệu thật |
| Body: cao trào | 2–3 câu | Khoảnh khắc "à ra vậy" + cách làm |
| Tóm tắt | 1 câu | Trả lời câu hỏi hook |
| CTA | 1, ngắn hơn 1 câu | Chỉ MỘT lời kêu gọi |

## 2. Ba kiểu hook (không bao giờ mở chung chung kiểu "Hôm nay mình sẽ nói về…")
- **Trực tiếp:** gọi tên người/việc/vấn đề cụ thể. "Omi á, mình dời hoài luôn!"
- **Gây tranh cãi:** "Điều không ai nói về trì hoãn…", phải có bằng chứng ngay sau.
- **Phủ định:** "Đừng bao giờ…", "Đừng chửi mình lười nữa."

## 3. Giọng người thật
- Nói như kể với bạn ngoài quán cà phê: đồng cảm, thỉnh thoảng hài.
- Có thành ngữ, ẩn dụ, giai thoại, đối thoại tự nhiên; tiểu từ Nam Bộ (á, nha, hông, nè, luôn).
- Chữ đơn giản, đứa 12 tuổi hiểu; không từ chung chung, không từ sang chảnh.
- Có nghiên cứu/số liệu thật (nói kèm giới hạn, vd "đi chung thôi nha").
- Kịch bản copy ra đọc được ngay: lời thoại riêng, hành động/hình ở cột khác.
- Mỗi câu một từ nhấn `{nhấn: …}` (luật 63).

## 4. Tự kiểm trước khi gửi Hiệp
- Đọc to: có câu nào mình sẽ không bao giờ nói với bạn? → viết lại.
- Có từ trừu tượng nào thay được bằng hình cụ thể? (khó chịu → rối nùi, sợ code xấu)
- Hook có tên việc cụ thể + câu hỏi? Tóm tắt có trả lời câu đó? CTA có đúng một?
