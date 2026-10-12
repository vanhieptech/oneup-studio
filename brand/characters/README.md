---
id: characters
type: brand
status: prototype
updated: 2026-10-12
tags: [characters, comic, omi, hiep]
---
# Characters (prototype v0.1)
- **Hiệp** (nhân vật chính): avatar cách điệu, **không phải chân dung thật**. Nét ink trên nền paper. Có đủ góc xoay, 6 biểu cảm, 3 dáng chính. Rig code: `rig.py`. Sheet: `hiep-model-sheet.png`, `hiep-poses.png`.
- **Omi**: dùng SVG brand có sẵn (`brand/omi-exports/svg/companion/*`), dạng **companion** cho vai trợ lý. Omi bay lơ lửng, không có thân, cao khoảng ngang vai Hiệp, kích thước khoảng 0,9 lần cái đầu. Bubble của Omi là thẻ bo tròn, đuôi bằng chấm, có tag "Omi". Sheet: `omi-sheet.png`.
- **Bubble của Hiệp**: hình chữ nhật bo tròn vẽ tay, đuôi nhọn. **Narration**: khối ink, chữ paper in hoa.
- Render lại: `python3 brand/characters/sheets.py`. Comic strip: `python3 pipeline/comic/render.py content/clips/<clip>`.
- ⚠ **Mâu thuẫn với rule-11:** luật hiện tại cho Omi xuất hiện từ tuần 5. Bản này chỉ là prototype, chưa đổi luật. Chờ Hiệp quyết định.
