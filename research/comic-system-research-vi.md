---
title: "Nghiên cứu: hệ thống minh hoạ comic cho clip kể chuyện (Hiệp + Omi)"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: research.comic-system
type: research
status: reference
updated: 2026-10-12
tags: [comic, characters, illustration, ai-image, omi]
---
# Nghiên cứu: hệ thống minh hoạ comic cho clip kể chuyện (Hiệp + Omi)
Kiểm qua GitHub API ngày 12/10/2026 (số sao, license, ngày push gần nhất). Mục ghi [cần kiểm lại] là chưa mở nguồn.

## 1. Công cụ vẽ bằng code (tất định, kiểm soát được brand)
| Công cụ | License | Bảo trì | Dùng cho | Ghi chú |
|---|---|---|---|---|
| [rough.js](https://github.com/rough-stuff/rough) | MIT | 21k★, push 07/2024 (ổn định, ít đổi) | nét vẽ tay cho khung, hình, mũi tên | seed cố định nên ra kết quả tất định |
| [roughViz](https://github.com/jwilber/roughViz) | MIT | 7k★, 04/2024 | biểu đồ vẽ tay | cho beat dạng data |
| [Excalidraw](https://github.com/excalidraw/excalidraw) + [excalidraw-libraries](https://github.com/excalidraw/excalidraw-libraries) | MIT | 134k★, push 12/10/2026 | phác cảnh bằng tay rồi xuất SVG | xuất SVG từ trong app hoặc `@excalidraw/utils` (exportToSvg) [cần kiểm lại API headless]. Thư viện cộng đồng: license từng gói khác nhau |
| [tldraw](https://github.com/tldraw/tldraw) | **license riêng của tldraw** (không phải OSS tự do, bản dùng production có watermark hoặc cần license) | 51k★, 12/10/2026 | canvas | **Không khuyên dùng** (không đạt luật miễn phí cho production) |
| [DiceBear](https://github.com/dicebear/dicebear) | MIT (code). Mỗi style có license riêng (ví dụ Notionists, Open Peeps CC0, một số CC BY) | 9.8k★, 11/10/2026 | avatar có seed | tốt cho nhân vật phụ. Phải kiểm license từng style |
| [Beanheads (BigHeads)](https://github.com/RobertBroersma/beanheads) | MIT | 1.5k★, 01/2026 | avatar React có tham số | style phẳng có màu, phải ép về đơn sắc |
| Open Peeps (openpeeps.com) | CC0 [cần kiểm lại] | | người vẽ tay đen trắng | **rất hợp brand**. Ghép phần cơ thể |
| Humaaans (humaaans.com) | free cho thương mại [cần kiểm lại license chính xác] | | người phẳng | nhiều màu, ít hợp brand |
| [comicgen](https://github.com/gramener/comicgen) | MIT | 618★, 04/2024 (ít bảo trì) | nhân vật comic SVG có tham số | ý tưởng hay, style không hợp brand |
| SVG rig tự viết (`brand/characters/rig.py`) | của mình | | Hiệp + bubble + đạo cụ | **đang dùng**. Kiểm soát 100% brand và tính nhất quán |
| [Rive](https://github.com/rive-app/rive-wasm) | runtime MIT, editor freemium | 12/10/2026 | rig nhân vật có state machine (chớp mắt, nói) | để sau, khi cần Omi chuyển động mượt |
| [lottie-web](https://github.com/airbnb/lottie-web) / [dotlottie-web](https://github.com/LottieFiles/dotlottie-web) | MIT | 09/2025 / 10/2026 | phát animation JSON | HyperFrames có adapter sẵn |
| GSAP (DrawSVG, MorphSVG, SplitText đều miễn phí) · [anime.js](https://github.com/juliangarnier/anime) MIT · [HyperFrames](https://github.com/heygen-com/hyperframes) Apache-2.0 | | đang hoạt động | hiện từng panel, vẽ nét dần, bubble bật ra | **dùng cho chuyển động** |
| Speech bubble | | | | Không có thư viện riêng đáng tin cậy. Tự vẽ trong `rig.bubble()` (SVG + foreignObject để chữ Be Vietnam Pro xuống dòng) |

## 2. AI tạo ảnh chạy local (miễn phí)
| Lựa chọn | License | Chạy trên Mac Apple Silicon | Nhất quán nhân vật | Rủi ro "nhìn như AI" |
|---|---|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | GPL-3.0 (app). Model có license riêng | Có (MPS), 137k★, 12/10/2026 | tốt với LoRA nhân vật + IP-Adapter / InstantID | cao nếu không kiểm soát style |
| Draw Things (app Mac/iOS) | app miễn phí, mã đóng [cần kiểm lại] | Có, tối ưu Metal | LoRA được | như trên |
| [DiffusionBee](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui) | AGPL-3.0 | Có, nhưng push cuối 10/2024 (gần như dừng) | yếu | |
| Model SDXL | CreativeML OpenRAIL++-M (thương mại được, có điều khoản sử dụng) [cần kiểm lại] | | | |
| [FLUX](https://github.com/black-forest-labs/flux): schnell Apache-2.0; dev **non-commercial** | | nặng (12B), Mac chạy chậm | tốt | |
| [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | Apache-2.0 (code). Trọng số theo license của model gốc | | giữ khuôn mặt hoặc style từ ảnh tham chiếu | |

**Đánh giá theo luật kênh:**
- Luật 13 và 24 cấm video AI và giọng AI. Ảnh AI tĩnh chưa bị cấm rõ ràng, nhưng nó **mâu thuẫn tinh thần của rule-20 (anti-AI-look)** và có thể phải gắn nhãn AI trên TikTok.
- Ảnh AI khó giữ đúng đơn sắc ink/paper, dễ ra kiểu bóng bẩy và tay méo.
- **Đề xuất:** không dùng AI image trong video. Nếu cần, chỉ dùng local (ComfyUI + SDXL) để **phác ý tưởng bố cục**, rồi vẽ lại bằng rig hoặc vẽ tay. Cần Hiệp quyết.

## 3. Stack đề xuất
1. **Nhân vật:** rig SVG tự viết (`brand/characters/rig.py`) cho Hiệp. Omi dùng SVG brand có sẵn (dạng companion, 12 mood). Bộ lọc feTurbulence / displacement tạo cảm giác nét tay. Có thể ghép phần cơ thể từ Open Peeps (CC0) nếu cần thêm dáng.
2. **Khung, mũi tên, biểu đồ:** rough.js / roughViz với seed cố định. Phác cảnh phức tạp bằng Excalidraw, xuất SVG vào repo.
3. **Layout và render:** `content/clips/<clip>/comic/spec.json` → `pipeline/comic/render.py` (Chrome headless), giống storyboard (rule-36).
4. **Chuyển động:** HyperFrames + GSAP (DrawSVG vẽ nét, bubble bật ra, panel hiện dần). Rive sau này cho Omi chớp mắt.
5. **Không dùng:** tldraw (license), AI image trong video thành phẩm.

## 4. Nhất quán nhân vật qua các clip
- Mọi clip dùng chung `rig.py` (khoá tỉ lệ, kiểu tóc, nét 5px) và chung `FILTER(seed=3)`.
- Chỉ đổi biểu cảm và dáng bằng tham số, không vẽ lại từ đầu.
- Đổi model sheet thì tăng version (v0.1 → v0.2) và ghi DL.
