---
title: "clip-01 cover (DL-046, bản nháp, chờ Hiệp chọn)"
date: 2026-10-14
type: readme
tags: [content]
status: ready
source: "oneup-studio (soạn trong repo)"
---

# clip-01 cover (DL-046, bản nháp, chờ Hiệp chọn)
Template: `video-engine/src/composition/Cover.tsx` (Remotion still 1080×1920). Render:
`npx remotion still src/index.ts Cover out.png --props="$(cat cover-a.props.json)"`

Các slot cố định: tag series + số tập, hero 2–4 chữ (1 chữ nhấn kiểu pill ink, có thể gạch chữ cũ), chibi tạo dáng riêng với biểu cảm cường điệu (không lấy frame video), logo +1 nhỏ, theme theo luật 17. Mọi slot nằm trong vùng an toàn của lưới profile (crop 3:4 giữa, y 240–1680).

- **A, Big type:** chữ thói quen cũ bị gạch → chữ mới trong pill ink, chibi phản ứng mạnh ở dưới.
- **B, Split:** nửa trên panel ink "Kế hoạch học: ~~MAI HỌC~~", nửa dưới "Đổi thành: NẾU–THÌ" + chibi.
- **C, Sticker card:** hero "CHỈ 1 CÂU" + tấm thẻ vé NẾU/THÌ điền sẵn ví dụ, chibi chỉ vào thẻ.

`grid-mock*.png`: 6 tập đầu (theme theo theme-map) crop 3:4 như lưới profile TikTok. Khi Hiệp chọn: copy bản đã chọn thành `../cover.png`, sửa post.md mục 2.

## Best practice đã áp dụng (tra cứu 14/10/2026: thumbcrafted.com, pod2reels.com, gradiently.design)
- Thiết kế cho crop 3:4 của lưới trước (vùng y 240–1600). Vùng an toàn cả hai chế độ xem là y 290–1600: chữ, mặt nhân vật, logo đều nằm trong đó. Logo đặt ở y 1470 để tránh số view ở góc dưới-trái.
- Hero 3–5 chữ đậm, tương phản cao, lệch trái (bên phải để trống cho nút bấm). Có mặt nhân vật với biểu cảm rõ.
- Cùng một template cho cả series để lưới profile trông có kế hoạch. Không lặp lại caption hay frame video.
