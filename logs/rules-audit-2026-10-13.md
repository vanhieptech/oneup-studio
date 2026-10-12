---
id: rules-audit-2026-10-13
type: log
status: done
updated: 2026-10-13
tags: [rules, audit, rule-46]
---
# Audit bộ luật ngày 13/10/2026 (v2.6 → v3.0)

Đối chiếu 45 luật trong `rules/video-rules.md` với decision-log (DL-001…DL-024), `content/voice-profile.md`, `brand/brand-index.md`, `pipeline/pipeline.md`, `AGENTS.md`, `video-engine/README.md`. Kết quả: **1 luật mới, 13 luật sửa, 2 chỗ trùng gộp, 1 chỗ chờ Hiệp xác nhận.**

## Mâu thuẫn đã sửa
| Luật | Vấn đề | Sửa |
|---|---|---|
| 2 | "Không dùng giọng AI" ↔ Hiệp chọn A (Omi có giọng AI) | Giọng Hiệp/người thật luôn là giọng thật, không bao giờ AI. Ngoại lệ duy nhất là Omi (luật 46). Chưa có bản thu thì lời Hiệp chỉ là bubble |
| 24 | "Không giọng AI, nên không cần nhãn AI" | Không AI trong hình final. Clip có giọng Omi **phải** gắn nhãn AI |
| 25 ↔ 45 | Luật 25 chỉ nói HyperFrames + Manim, không có Remotion. Luật 45 lặp lại phần ranh giới engine | Luật 25 = vai trò cố định (Remotion: kể chuyện, HyperFrames: giải thích, VieNeu: giọng Omi, ffmpeg `join-beats.sh`: ghép). Luật 45 chỉ giữ chi tiết `video-engine` |
| 7 ↔ 41 | Cấu trúc "Hook → Vấn đề → Giải thích" mặc định ↔ luật 41 "kể chuyện trước" | Mặc định theo mạch kể chuyện (41). Dạng giải thích chỉ dùng khi không có chuyện thật |
| 16 ↔ 42 | "Chữ trên màn hình chỉ tiếng Anh" ↔ bubble comic tiếng Việt | Caption/tiêu đề tiếng Anh. Bubble và hộp dẫn chuyện của comic viết tiếng Việt |
| 18 ↔ 43 | Open Peeps cho minh hoạ người ↔ nhân vật chỉ dùng rig Hiệp/Omi | Không dùng Open Peeps cho nhân vật chính |
| 32 ↔ 31 | Nhắc đăng 4 ngày (T2/T4/T6/CN) ↔ 3 clip/tuần trong 2 tuần đầu | Tuần 1–2: T2/T4/T6. Thêm CN khi lên 4 clip/tuần. Gói đăng thêm dòng nhãn AI |
| 26 | Chỉ có whisper cho giọng Hiệp | Câu của Omi lấy timing + envelope từ TTS, kiểm bằng ASR |

## Cũ / lỗi thời đã dọn
- Header "v2, 12/10/2026" → **v3.0**. Changelog v2.6 bị dính dòng với v2.5 → tách lại.
- `brand/brand-index.md`: caption "DM Sans 500" → Be Vietnam Pro. Mục "rule 7 cũ cần asset" → đã xử lý. "Dark mặc định" → thay bằng luật 17.
- `research/omi-voice-tts-research-vi.md`: trạng thái "chờ Hiệp quyết" → đã quyết (A), kèm cách cài thật.
- `video-engine/README.md`: "chưa có voice/lip-sync" → mô tả luồng giọng Omi. Thêm giới hạn: không có grain, TTS không tất định (dùng cache).
- Độ dài 30–45s và Poppins: chỉ còn trong changelog/DL (lịch sử), không còn trong luật đang áp dụng. ✔
- Nhạc (luật 21): mọi file vẫn không nhạc, pipeline bước 16 thêm nhạc TikTok khi đăng. ✔ Khớp.
- Font (luật 15): Be Vietnam Pro ở cả engine Remotion, HyperFrames và bubble. ✔

## Trùng lặp đã gộp
- "Omi từ tuần 5" ở luật 11 và 42 → nằm ở luật 11 (kèm validator chặn `week < 5`), luật 42 chỉ dẫn lại.
- Vai trò engine ở luật 25 và 45 → gộp như trên.

## Thiếu → bổ sung
- **Luật 46 (mới): giọng AI của Omi.** VieNeu-TTS v3 Turbo (Apache-2.0) chạy local CPU/ONNX. Preset cố định "Kim Thanh" (nữ, miền Nam). Cấm clone giọng người thật và cấm `ref_audio`. `emotion` theo từng câu. Cache theo hash. Lỗi thì dùng placeholder có ghi rõ, không giả giọng.
- **Nhãn AI TikTok** (đã kiểm trang hỗ trợ TikTok ngày 13/10/2026): TikTok **bắt buộc** gắn nhãn cho nội dung AI có hình, *âm thanh* hoặc video trông/nghe như thật, và khuyến khích gắn cho nội dung tạo/sửa đáng kể bằng AI. Gắn nhãn AI cho nội dung không dùng AI là vi phạm điều khoản. Vì giọng Omi nghe như người thật, clip có Omi nói → bật **"AI-generated content"** + caption "Giọng của Omi là giọng AI tổng hợp (VieNeu-TTS)". Clip không có giọng Omi → không bật.
- Luật 5 thêm phong cách "comic kể chuyện". Logo (luật 14) đã có sẵn trong composition Remotion.

## Chờ Hiệp xác nhận
- **Luật 6 (tỉ lệ tự quay ≥ 50%)** không hợp với clip kể chuyện bằng comic. Đang **tạm áp dụng**: clip có comic thì comic + motion được tính là minh hoạ, nên có ít nhất 1 cảnh thật. Hiệp chốt lại giúp (DL-025).
