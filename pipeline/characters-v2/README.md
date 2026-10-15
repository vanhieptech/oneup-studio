---
title: "Character rig v2 (chibi, liquid)"
date: 2026-10-13
type: readme
tags: [pipeline]
status: ready
source: "oneup-studio (soạn trong repo)"
---

# Character rig v2 (chibi, liquid)
- `chars.html`: rig dạng JS/SVG (hiep(), omi()). Omi = blob Catmull-Rom 72 điểm + filter gooey; morph cảm xúc bằng nội suy tham số (không cần plugin).
- `scene-*.js`: cảnh. `npm install` rồi `node render.js anim|hiep|omi <outdir>` (puppeteer-core + Chrome, `CHROME_PATH` để đổi). Đây là công cụ thử rig cũ; render thật dùng `video-engine/` → ffmpeg ghép MP4.
- Hiệp là avatar generic: chưa có tóc/kính/quần áo thật.
