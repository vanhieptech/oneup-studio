# @hi.oneup — Brand index cho video

Nguồn: `/Users/macbook/work/oneup/design-system/oneup/` (MASTER.md, brand/COLOR.md, brand/LOGO.md, brand/omi-exports, scripts/export_omi_assets.py). Bản sao trên box: `/workspace/hi-oneup/brand/` (chỉ file text + SVG chính; PNG vẫn ở Mac). Tokens máy đọc: `brand-tokens.json`. Preview: `brand-preview-dark.png`, `brand-preview-light.png` (nguồn `preview/gen.py`).

## 1. Màu
Triết lý: **ink + paper = brand**. Hue chỉ dùng cho ngữ nghĩa, không bao giờ là bản sắc.

| Role | Light | Dark (paper-on-ink) |
|---|---|---|
| bg | #F7F7F5 | #111111 |
| surface | #FFFFFF | #1C1C1A |
| ink (chữ/logo) | #111111 | #F7F7F5 |
| muted | #6B6B6B | #A3A3A0 |
| border | #E8E8E6 | #2E2E2C |
| soft / coachTint | #F0F0EE / #F4F4F2 | #242422 / #1A1A18 |
| success (chỉ "done") | #1A7F4B | #2F9E66 |
| momentum (at-risk + nhãn) | #B45309 | #D97706 |
| danger (chỉ lỗi) | #B91C1C | #DC2626 |

- Tỷ lệ: ~90% neutral · ~8% CTA (ink/paper) · ~2% hue semantic.
- Cấm: tím "AI", neon/glow, cream + terracotta, teal làm brand, cầu vồng, cặp #000/#FFF thuần, confetti, emoji icon, shadow nhiều lớp.
- Đề xuất video: **dark làm mặc định** cho text-over-b-roll (ink #111111 + chữ paper), light cho cảnh desk/app.

## 2. Caption word-by-word (đề xuất)
- Chữ chưa đọc: muted (#A3A3A0 trên nền tối / #6B6B6B trên nền sáng), DM Sans 500, 76px.
- Từ đang đọc: **paper #F7F7F5, weight 800 + gạch chân 8px** — nhấn bằng hình/độ đậm, không đổi hue.
- Từ khoá: pill paper (#F7F7F5 nền, chữ #111111, radius 14) — đúng "paper button on ink".
- Xanh success chỉ cho beat "done/+1". Không bao giờ dùng đỏ cho skip.
- Trên b-roll sáng: thêm plate #111111 ~80% sau caption để giữ contrast ≥4.5:1.
- Caption: plate bo 40px (surface 78–86%, viền border), cách đáy 420px, 3–5 từ/cụm; từ đã nói = ink, từ đang nói = ink 700 + gạch chân 6px, từ sắp tới = muted 55%.

## 3. Font
**Video: Be Vietnam Pro cho TOÀN BỘ chữ on-screen (EN + VI)** — Hiệp chốt 12/10/2026. OFL, v1.002, 400/500/600/700 tại `/workspace/hi-oneup/brand/fonts/BeVietnamPro-*.ttf`; đủ dấu tiếng Việt (test `preview/vi-test.png`).
- Thang video: wordmark "OneUp." 44/700 (−0.03em, dấu chấm opacity 0.35) · eyebrow 28/600 uppercase +0.14em · hero 104/700 (−0.035em, lh 1.02) · sub 36/400 muted · caption 76/600 (−0.02em, từ đang nói 700 + gạch chân 6px) · meta 26/500.
- Font app (tham khảo): DM Sans 4.004 static 400/500/600/700 — bằng chứng MASTER.md §3 "DM Sans only", `OUTypography.swift`, `UIAppFonts` trong Info.plist, CSS prototype. Không dùng trong video lúc này vì thiếu dấu chồng tiếng Việt (ế ạ ữ ơ ư). Instrument Serif chỉ có trong trang showcase brand, không dùng.
- Motion (MASTER §6): appear 280–360ms ease-out, spring 0.85→1.0 300ms, crossfade 200ms, không confetti.
- Theme LIGHT/DARK theo tone từng clip: xem `theme-map.md`.

## 4. Logo trong video
- Hero: `brand/logos/05-pair-plus.svg` (Pair +Bond +1: vòng mở = lắng nghe, 2 chấm = bạn + Omi, +/1 chung thân = bước tiếp theo).
- Màu: ink #111111 trên paper; paper #F7F7F5 trên ink. Không tô màu, không glow.
- Vị trí 1080×1920: góc trên-trái, x=72, y=236, mark 60px + wordmark "OneUp." 44px, opacity 100%, hiện suốt clip (safe zone: trên 220, dưới 380, phải 140).
- Outro tuỳ chọn (~3.2s): stroke-draw arc → 2 chấm → +/1 → wordmark, nhãn beat **Listen · Understand · Your +1**.
- `omi-load.svg` chỉ là loader app — không dùng làm logo video. Không dùng mặt Omi làm logo.

## 5. Omi — catalog (48 SVG + PNG 48/96/144/256)
Đường dẫn: `…/brand/omi-exports/svg/{form}/{mood}.svg`, PNG `…/png/{form}/{mood}/{mood}-{size}.png`. Nét ink #111111 (template, đổi sang #F7F7F5 trên nền tối).
Form (tăng dần theo Bond): **seed** (mặt trơn) → **companion** (+ "tai" lắng nghe) → **guide** (vầng + chấm trên đầu) → **anchor** (vòng đồng tâm + sao).

| Mood | Ý nghĩa (suy từ tên + nét vẽ; doc không ghi rõ) | Dùng trong video |
|---|---|---|
| idle | trạng thái chờ, mỉm cười nhẹ | nền/khởi đầu |
| wave | chào | mở/kết clip |
| think | đang nghĩ (alias "suggest") | đặt câu hỏi |
| quiet | trầm, yên | beat chậm/nghỉ |
| listen | lắng nghe (miệng phẳng) | khi người nói chia sẻ vấn đề |
| celebrate | ăn mừng (+ sao) | hoàn thành — không confetti |
| sleep | ngủ | nghỉ ngơi/năng lượng thấp |
| proud | tự hào | +1 đạt được |
| spark | loé ý tưởng | insight/hook |
| blush | ngại, ấm áp (má hồng ink) | cảm ơn/khen |
| worry | lo lắng | nêu nỗi đau (không shame) |
| cheer | cổ vũ | lời khuyến khích CTA |

**Lịch:** Omi **cấm** trong video tới **tuần 5**; màn hình app chỉ từ **tuần 3** (tuần 3–4 ngắn). Khi dùng: form khớp với giai đoạn Bond người xem đang nghe kể (mặc định seed).

## 6. Xung đột cần sửa
1. `clip-01-implementation-intention.md` dòng 51 "No logo required" ↔ rule 7 (logo nhỏ) → **phải thêm logo nhỏ** 05-pair-plus góc trên-trái.
2. `hi-oneup-video-rules.md` rule 7 ghi "assets needed from Hiệp" → nay đã có màu, font (DM Sans), logo; chỉ cần cập nhật trỏ về file này.
3. Rule 19 (motion từ awesome-ai-motion) phải lọc theo MASTER §6: không confetti, không glow/neon, không nảy mạnh — ưu tiên ease-out, crossfade, spring nhẹ.
4. Phong cách "app screen recording" trong rule 5 chỉ được dùng từ tuần 3.

## 7. Còn thiếu
- Wordmark "OneUp." dạng SVG (doc nhắc, nhưng không có file trong brand/logos; `03-listen-plus-one.svg`, `04-nest-plus.svg`, `06-mark-plus-one.svg` được nhắc trong LOGO.md nhưng không có trong thư mục).
- Ý nghĩa chính thức từng mood Omi (UX-COMPANION-SYSTEM.md / pages/omi-emotion.md có thể ghi — chưa đọc).
- Xác nhận: nền mặc định video dark hay light.
