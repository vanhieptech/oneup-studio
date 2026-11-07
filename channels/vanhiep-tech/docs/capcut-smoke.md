---
title: "CapCut smoke — ProRes alpha / chroma"
date: 2026-11-07
id: docs-vht-capcut-smoke
type: guide
status: draft
updated: 2026-11-07
source: "channels/vanhiep-tech PLAN"
tags: [capcut, alpha, vanhiep-tech]
---
# CapCut smoke-test (V1)

Mục tiêu: chứng minh `ov-d01.mov` (ProRes 4444) overlay được trên A-roll trong CapCut Desktop. Fail → dùng chroma.

## 1. Render layer mẫu
```bash
cd channels/vanhiep-tech/clips/vht-20261107-oauth-control-plane/layers/ov-d01
mkdir -p fonts && cp ../../../../../../brand/fonts/BeVietnamPro-{Regular,SemiBold,Bold}.ttf fonts/
npm i
npx hyperframes@0.8.150 check
mkdir -p ../../../../../../media/channels/vanhiep-tech/vht-20261107-oauth-control-plane
npx hyperframes@0.8.150 render --format mov \
  -o ../../../../../../media/channels/vanhiep-tech/vht-20261107-oauth-control-plane/ov-d01.mov .
```

## 2. Test ProRes trong CapCut
1. New project 1080×1920
2. Thêm nền màu nổi (magenta / vàng) full frame
3. Import `ov-d01.mov` lên track trên
4. Play: quanh card phải **thấy màu nền** (trong suốt). Nếu cả khung đen/đặc → ProRes alpha fail trên build CapCut của bạn.

## 3. Fallback chroma
1. Trong `index.html`, thêm class `chroma` lên `body` (nền `#00FF00`)
2. Render lại `--format mp4` → `ov-d01-chroma.mp4`
3. CapCut: overlay → Effects → Chroma Key → chọn xanh

## 4. Cutaway
Nền paper solid `#F7F7F5` — không cần alpha; `--format mp4` là đủ.

## 5. Ghi kết quả
Sau smoke, thêm 1 dòng vào `PLAN.md` Revisions: `ProRes OK` hoặc `ProRes fail → chroma default`.
