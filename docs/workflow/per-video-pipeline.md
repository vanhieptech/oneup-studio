---
id: per-video-pipeline
type: workflow
status: active
tags: [workflow, pipeline, rule-65]
---
# Quy trình một video, từ ý tưởng tới sẵn sàng đăng

Đánh dấu **[Hiệp]** = cần Hiệp duyệt/làm; còn lại agent tự làm và báo tiến độ liên tục. Luật: `rules/video-rules.md`; skill: `skills/make-video/SKILL.md`.

1. **Chọn trend** — đọc digest mới nhất `research/trends/<ngày>/`, `patterns.md`; chọn 1 trend/format + ghi id (luật 37, 57). **[Hiệp]** chốt hướng nếu có nhiều lựa chọn.
2. **Đọc trước** — `docs/conventions/storage.md`, `logs/lessons.md`, `rules/video-rules.md`, `logs/decision-log.md`, `docs/research/script-prompt-principles.md`, kho văn nói `resources/vn-spoken/`.
3. **Viết nháp kịch bản** — bảng Cảnh | Hành động | Lời; hook ≤ 2 câu mở khoảng tò mò, ABT, callback clip trước, 1 CTA, văn nói Nam Bộ (luật 58–64). Lưu `content/clips/<clip>/final/script-*.md`.
4. **Duyệt kịch bản** — gửi bảng cho **[Hiệp]**; sửa tới khi OK. Mỗi góp ý → thêm/sửa lesson trước khi sửa.
5. **Voice mẫu 4 cảnh đầu** — F5 thai-son (`assets/voice-refs/`), phiên âm tiếng Anh/brand, mỗi cảnh 1 lần F5, STT ≥ 0,8 (L-025); xuất mp3 gửi nghe.
6. **Duyệt giọng** — **[Hiệp]** nghe mp3; chỉ OK mới làm tiếp.
7. **Voice toàn bộ + STT** — các cảnh còn lại cùng cách, re-roll take < 0,8; take chọn lưu `video-engine/public/voice/` (json có stt/stt_sim).
8. **Spec + storyboard** — cập nhật `final/spec.json` (nguồn sự thật: cảnh, cast, props, sfx, fx, caption, structure, engagement); `fx-table.py --write`.
9. **Checks** — `check-rules.py <clip>` (luật + lessons, gồm L-033 layout), `check-assets.py` (luật 59, 65), video-engine validate. ✖ phải sửa hoặc ghi rõ ngoại lệ đã được Hiệp duyệt.
10. **Render** — `build-final.py final/spec.json` (tự chạy `sync-shared.py`); trên Mac hoặc box. Output `final/out/clip-XX-final.mp4`.
11. **Tự QA khung hình** — trích frame giữa mỗi cảnh, contact sheet; soát bubble/props/mặt/caption/vùng an toàn TikTok; sửa gốc (layout/spec), render lại.
12. **Duyệt bản cắt cuối** — gửi bản 720p faststart < 10 MB cho **[Hiệp]**.
13. **Caption, hashtag, cover** — `post.md`, cover từ template `Cover.tsx` (L-020, luật 54); **[Hiệp]** chọn cover.
14. **Export** — bản full (1080×1920, −14 LUFS) + bản 720p preview.
15. **Ghi bài học** — mọi lỗi/góp ý mới vào `logs/lessons.md` (+ check tự động), quyết định vào `logs/decision-log.md`.
16. **Commit + push** — commit trong repo; push qua Mac bằng bundle tăng dần trong `.git/` (≤ 5 MB/mảnh), `git push origin main` không force, kiểm `origin/main` = HEAD. **[Hiệp]** duyệt lệnh trên Mac.
17. **Bộ đăng bài** — `post-checklist.md`: video full, caption, hashtag, cover, giờ đăng. **[Hiệp]** tự đăng (agent không đăng thay).
18. **Lưu trữ (luật 66)** — khi đủ gói đăng và **[Hiệp]** nói "duyệt": copy video full + 720p vào `media/clips/<clip>/` (+ MANIFEST), `git mv content/clips/<clip> content/archive/<clip>`, ghi `final/approved.json`, chạy `check-assets.py`, `media-sync.py` sang Mac, commit + push.
