---
title: "Giọng Omi: TTS tiếng Việt miễn phí, chạy local (13/10/2026)"
type: research
source: "oneup-studio (soạn trong repo)"
id: research-omi-voice-tts
date: 2026-10-13
tags: [omi, voice, tts]
status: decided (Hiệp chọn A ngày 13/10/2026, DL-025, rule-46)
---
# Giọng Omi: TTS tiếng Việt miễn phí, chạy local (13/10/2026)

> ✅ 13/10/2026: Hiệp chọn **A** (DL-025). Đã thành luật 46. Cài thực tế: `pip install vieneu` + `onnxruntime==1.22.1` (bản 1.31 lỗi "External data path escapes model directory" với cache HuggingFace). Preset Omi: "Kim Thanh" (nữ, miền Nam).

| Lựa chọn | License | Chất lượng tiếng Việt / cảm xúc | Chạy trên Mac M-series | Ghi chú |
|---|---|---|---|---|
| **VieNeu-TTS v3 Turbo** (pnnbao97) | **Apache-2.0** cả weights + giọng mẫu; được dùng thương mại | Tốt, 48 kHz, 23 giọng mẫu Bắc/Trung/**Nam**, chen En–Vi tự nhiên. Cảm xúc: tag thử nghiệm `[cười]`, `[thở dài]`, `[hắng giọng]` | Có: bản ONNX/GGUF chạy CPU, không cần GPU | **Khuyến nghị số 1**. Có watermark AI không nghe thấy (v2 Turbo) |
| viXTTS (capleaf, dựa trên XTTS-v2) | **Coqui Public Model License: không thương mại** | Khá, clone giọng 6s, cảm xúc theo giọng mẫu | Được (PyTorch MPS/CPU, chậm) | ❌ Kênh có kiếm tiền/quảng bá app thì rủi ro license |
| F5-TTS Vietnamese (cộng đồng, vd. hynt/F5-TTS-Vietnamese) | Code MIT nhưng weights gốc F5 **CC-BY-NC** | Rất tự nhiên, cảm xúc lấy theo audio mẫu (đổi audio mẫu vui/buồn) | Được (MLX/MPS), vài giây/câu | ⚠ Không thương mại, phải kiểm license từng checkpoint |
| Piper (vi_VN vais1000) | MIT (engine), giọng theo dataset | Đều, robot, không có cảm xúc | Rất nhanh | ❌ Không đạt "giọng nhiều cảm xúc" |

## Đề xuất cho Hiệp chọn
- **A.** Nới luật: cho phép **một** giọng AI duy nhất cho **Omi** (VieNeu-TTS, Apache-2.0, chạy local). Giọng Hiệp vẫn là giọng thật. Cảm xúc điều khiển bằng chọn giọng mẫu + tag + chỉnh tốc độ/pitch theo beat.
- **B.** Giữ luật: Omi không nói, chỉ có text bubble + SFX "blip" theo cảm xúc (kiểu Animal Crossing).
- **C.** Hiệp tự lồng tiếng Omi (pitch shift +4–6 semitone bằng ffmpeg/rubberband), cảm xúc do chính Hiệp diễn.
- Nếu chọn A: không clone giọng người khác, ghi chú "Omi dùng giọng tổng hợp" trong caption để minh bạch.
