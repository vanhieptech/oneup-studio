# Character rig v2 (chibi, liquid)
- `chars.html`: rig dạng JS/SVG (hiep(), omi()). Omi = blob Catmull-Rom 72 điểm + filter gooey; morph cảm xúc bằng nội suy tham số (không cần plugin).
- `scene-*.js`: cảnh. `node render.js anim|hiep|omi <outdir>` (puppeteer-core + Chrome) → ffmpeg ghép MP4.
- Hiệp là avatar generic: chưa có tóc/kính/quần áo thật.
