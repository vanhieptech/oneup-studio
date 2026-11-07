---
title: "CapCut smoke — solid One Dark layer"
date: 2026-11-07
id: docs-vht-capcut-smoke
type: guide
status: draft
updated: 2026-11-07
source: "channels/vanhiep-tech PLAN"
tags: [capcut, vanhiep-tech]
---
# CapCut smoke-test (V1)

**Luật:** mọi layer có **nền solid** `#282C34`. **Cấm** nền / preview hồng–magenta–fuchsia.

## 1. Render layer mẫu (MP4 solid)
```bash
cd channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane/layers/ov-d01
mkdir -p fonts && cp ../../../../../../brand/fonts/BeVietnamPro-{Regular,SemiBold,Bold}.ttf fonts/
npm i
npx hyperframes@0.8.150 check
mkdir -p ../../../../../../media/channels/vanhiep-tech/vht-20261107-oauth-control-plane
npx hyperframes@0.8.150 render --format mp4 \
  -o ../../../../../../media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-d01.mp4 .
```

## 2. Import CapCut
1. Project 1080×1920
2. A-roll trên track chính
3. Import `ov-d01.mp4` làm **cutaway / overlay full hoặc PiP** (đã có nền dark — không chroma, không ProRes alpha)
4. Cắt theo marker trong `script.md`

## 3. Ghi kết quả
Thêm dòng vào `PLAN.md` Revisions sau khi ghép thử trên máy bạn.
