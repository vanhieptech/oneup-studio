---
id: research-character-animation
date: 2026-10-13
tags: [character, animation, gsap, liquid]
---
# Nhân vật cute, bo tròn, chuyển động liquid: nghiên cứu (13/10/2026)

## Lựa chọn đã xem
| Công cụ | License / giá | Render ra video trên box | Hợp với stack? |
|---|---|---|---|
| **GSAP 3 + MorphSVG, MotionPath, CustomEase/CustomWiggle, Physics2D** | Miễn phí hoàn toàn (kể cả plugin "Club") từ 2025 sau khi Webflow mua lại; license "no charge" của GSAP, không phải OSS | Có: HyperFrames seek theo frame | ✅ lõi |
| SVG gooey filter (feGaussianBlur + feColorMatrix) | Chuẩn web | Có | ✅ hiệu ứng liquid/metaball |
| Blob nội suy điểm (Catmull-Rom, tự viết) | Code của mình | Có, deterministic | ✅ đang dùng ở test v2 |
| flubber (veltman/flubber) | MIT | Có | ➕ dự phòng morph giữa shape khác số điểm |
| Squash & stretch + spring tắt dần (công thức 1−e^(−kt)cos ωt) | – | Có | ✅ nguyên tắc chính |
| Rive | Runtime MIT; editor có gói free nhưng giới hạn (export/tính năng đổi theo gói, cần kiểm lại) | Render offline khó (canvas/WASM, phải tự chụp từng frame) | ⚠ đẹp nhất cho state machine, phụ thuộc editor đóng |
| Lottie (lottie-web) | MIT; tạo file cần After Effects/Bodymovin hoặc LottieFiles editor | Có (goToAndStop theo frame) | ➕ dùng asset có sẵn, không làm rig chính |
| DragonBones / Spine | DragonBones miễn phí nhưng gần như ngừng phát triển; Spine trả phí | Khó với pipeline web | ❌ |
| Open Peeps / Humaaans | CC0 | Có | ➕ tham khảo dáng, không cute/chibi |

## Khuyến nghị (3 dòng)
1. Rig nhân vật bằng **SVG code** (hình khối tròn, chibi đầu ~55% chiều cao), dựng trong HyperFrames.
2. Chuyển động bằng **GSAP** (CustomEase/spring cho squash-stretch, MorphSVG hoặc blob nội suy cho morph cảm xúc Omi) + **SVG gooey filter** cho chất liquid.
3. Mọi animation phải deterministic theo frame (seek), không dùng Rive/Lottie làm lõi; Lottie chỉ dùng cho asset phụ.

## Nguyên tắc "cute + liquid"
- Không có góc nhọn: mọi path đều stroke-linecap/linejoin round, bán kính bo lớn.
- Mắt to, có chấm highlight; má hồng bằng xám ấm (giữ 90/8/2, không thêm hue).
- Mỗi hành động: anticipation → action → overshoot → settle (spring). Đầu trễ nhịp so với thân (follow-through).
- Omi: luôn thở (pulse bán kính ±4%), lơ lửng (sin), wobble biên nhỏ (1–3%), đổi cảm xúc = morph shape + mắt "nháy" qua.
- Cách điệu mạnh: biểu cảm phóng đại (mắt ^^, mồ hôi, giọt nước), đạo cụ to để người xem hiểu ngữ cảnh ngay.

## Đã làm
`pipeline/characters-v2/` (rig v2), `brand/characters/v2/` (sheet + motion test 7s). Bản test dùng nội suy tự viết; khi đưa vào HyperFrames sẽ chuyển sang GSAP timeline.
