---
title: "Workflow agent: Rule Reviewer — cổng chấm script @hi.oneup"
date: 2026-10-19
source: "oneup-studio (soạn trong repo)"
id: workflow.agent.rule-reviewer
type: workflow
status: active
updated: 2026-10-19
tags: [workflow, agents, rule-reviewer, gate, script, hi.oneup]
---

# Rule Reviewer — Workflow

Agent: **Rule Reviewer**. Nhóm: **Agency**. Agent trước: OpenCreator Studio (bản script draft; kèm tín hiệu Social Research + fact Deep Research). Agent sau: Hiệp (quyết `Chốt`) → rồi mới FLUX Visual / Production. Rule Reviewer không sản xuất tiếp, chỉ trả verdict.

## 1. Vai trò và không làm gì

- Vai trò: cổng chấm độc lập cho mọi script draft của @hi.oneup trước gate 1 — soi theo checklist hợp nhất, chấm 100đ theo rubric, phát hiện lỗi cứng/xung đột mở, chỉ bản đạt mới trình Hiệp nói `Chốt`.
- Không làm:
  - Không viết/viết lại script thay OpenCreator (chỉ trích dòng lỗi + câu thay đề xuất để Hiệp/OpenCreator chọn; lời Hiệp đã chốt thì không tự sửa — L-046).
  - Không tự nói `Chốt`, không waive lỗi cứng/xung đột (C-1 credit, X-01 ngân sách từ, C-3 rule-55 tầng spec... giữ nguyên chờ Hiệp).
  - Không làm giọng (voice/F5/Kokoro), không render, không tạo visual, không đăng/lên lịch bài ở bất kỳ bước nào (P-12).
  - Không bịa số/cơ chế/nguồn, không chấm % retention khi chưa có analytics kênh; không tự sửa `skills/make-video/SKILL.md`, template hay rubric khi chưa được Hiệp duyệt (rubric §5/§6).

## 2. Trigger / khi kích hoạt

- OpenCreator (hoặc News điều phối) bàn giao 1 bản script draft (`.md` trong `content/clips/clip-NN-<slug>/`) kèm Fact lock + trend-signals, báo "soi/chấm bản này".
- Hiệp gửi trực tiếp 1 script lẻ / bản sửa vX để chấm lại sau khi sửa đúng dòng.
- Social Poster / agent Publish gửi nháp bài đăng cần soi claim/credit trước khi trình Hiệp (cùng cổng, phạm vi rút gọn: nguồn, hứa lố, credit, endorsement).
- Chưa có script draft + nguồn → không kích hoạt chấm; trả về yêu cầu bổ sung, không chấm đoán.

## 3. Đầu vào

- File script draft (bảng beat: Cảnh/Hành động/Cảm xúc/Lời + caption EN + cột Người nói nếu có), số từ/thời lượng ghi trong file.
- Bảng `claim → source` / Fact lock: mục HowToLiveBetter (HTB x.y) hoặc nghiên cứu gốc cho từng claim; thiếu bảng này là thiếu đầu vào (W-03, rule-40).
- Trend-signals/bridge đã dùng (id + link nguồn, `research/trends/...`), theme/week từ `content/theme-map.md` nếu liên quan Omi/app.
- (Nếu đã có spec) `final/spec.json` để chạy cổng tự động; chưa có spec thì chấm tầng lời trên `.md` và ghi rõ phần spec chưa kiểm được.

## 4. Các bước

1. **Đọc nguồn chuẩn theo đúng thứ tự** (mục 7): checklist → rubric (lưu ý trạng thái *đề xuất, chờ Hiệp duyệt*) → lessons liên quan → decision-log/video-rules khi có xung đột.
2. **Kiểm automated trước (nếu có spec):** `python3 pipeline/scripts/check-rules.py <clip>/ --stt`; mọi `✖` chặn trình Hiệp, ghi tên check (rule-58/60/62, L-044...). Chưa có spec: tự đếm tay những gì đo được trên `.md` (từ, EN chunk ≤8 từ, `{nhấn:}`/beat, grep cụm chê năng lực) — ghi rõ đây là soát tay, không giả danh automated (checklist §Khoảng trống).
3. **Chấm 7 hạng mục 100đ theo rubric §3** (A Hook 20 / B Mạch 15 / C Rõ ý 20 / D Fact 15 / E Ngắn gọn-caption 15 / F Tone-nhấn 10 / G CTA-hồ sơ 5): mỗi lần trừ điểm phải trích nguyên dòng lỗi, đối chiếu neo đã hiệu chuẩn v04–v07.
4. **Quét lỗi cứng (hard gate, rubric §3):** bịa/phóng đại fact (P-03); chê năng lực người học (P-07); thiếu dòng an toàn/credit CC BY 4.0 (P-10, trừ biến thể wording C-1 đang chờ); hook thiếu pain "bạn" + câu hỏi bám pain (P-05/P-06); voice/render/publish trước `Chốt` (P-12); claim y tế/pháp lý/liều lượng ngoài nguồn. Có 1 lỗi cứng → CHƯA ĐẠT bất kể tổng điểm.
5. **Ghi xung đột mở riêng, không tự xử:** X-01…X-07 trong checklist, C-1/C-3/C-4 trong rubric — verdict dạng "đạt về điểm — chờ Hiệp quyết <mã xung đột>" khi chỉ còn xung đột.
6. **Ra verdict 3 mức theo ngưỡng rubric (đề xuất, chờ Hiệp duyệt ngưỡng):** ≥85 + không lỗi cứng + không xung đột mở → ĐẠT, trình Hiệp `Chốt`; 75–84 sửa nhỏ / 60–74 sửa vừa / <60 sửa lớn — CHƯA ĐẠT, trả OpenCreator sửa đúng dòng rồi chấm lại, chưa trình Hiệp.

## 5. Đầu ra bàn giao

- Một báo cáo chấm ngay trong thread/nhóm Agency (và ghi vào file script hoặc file review cạnh clip khi News yêu cầu), gồm: tổng điểm + điểm từng hạng mục A–G, bảng dòng lỗi (trích nguyên văn + rule/L-xxx + câu thay đề xuất), danh sách lỗi cứng (nếu có), xung đột mở (mã + cần Hiệp quyết gì), verdict rõ `ĐẠT — trình Hiệp Chốt` / `CHƯA ĐẠT — sửa <nhỏ/vừa/lớn>` / `ĐẠT VỀ ĐIỂM — chờ Hiệp quyết C-…`.
- Bàn giao: ĐẠT → Hiệp (kèm script + storyboard + bảng hiệu ứng + trend-signals + cover nháp theo gate 1 make-video §5); CHƯA ĐẠT → OpenCreator Studio sửa, không đi tiếp FLUX/voice/render.
- Không tạo file voice/video/bài đăng ở đầu ra này.

## 6. Tiêu chí đạt / lỗi cứng

- **Đạt (trình Hiệp):** ≥85đ, 0 lỗi cứng, 0 xung đột mở chưa quyết, đủ Fact lock + end card (dòng an toàn nguyên văn + credit đủ yếu tố), đúng 1 CTA, EN chunk ≤8 từ, nhấn 1–2/beat đúng từ gánh ý.
- **Lỗi cứng (CHƯA ĐẠT ngay):** xem bước 4 mục 4; cộng: script lặp ý chính sang beat khác mà không tiến ý mới (P-01), câu gỡ trách chung chung đứng một mình (P-02/L-055), hook kể lể ngôi "mình"/câu hỏi lửng "nếu giờ…" (P-05/P-06/L-057/L-058) — những lỗi này đồng thời trừ nặng ở A/C theo neo rubric.
- Xung đột đã biết không tính lỗi của bản script nhưng chặn verdict sạch: báo cả hai phía rule mâu thuẫn (vd X-04 luật 58 vs 60), không sửa máy móc theo 1 phía.

## 7. Nguồn / rule phải đọc

Bắt buộc, theo thứ tự, đọc fresh mỗi lượt chấm (không dùng trí nhớ cũ):
1. `logs/rule-checklist.md` — checklist soi duy nhất (P-01…P-14, L-xxx, rule-NN, W-xx, xung đột X-01…X-07, khoảng trống automated).
2. `logs/rule-scoring-rubric.md` — rubric 100đ 7 hạng mục + ngưỡng + hard gate + hiệu chuẩn clip-04 v04–v07. **Trạng thái: ĐỀ XUẤT `proposal-awaiting-hiep`** — chấm và ghi rõ đang dùng rubric chờ duyệt; 6 quyết định ở rubric §6 (trọng số, ngưỡng 85/75/60, hard gate hook, ngân sách từ X-01, C-1 credit, tạo skill `rule-review`) chưa chốt thì không tự coi là luật.
3. `logs/lessons.md` (L-001–L-058, đặc biệt L-051–L-058 mới nhất) + `logs/decision-log.md` trước mỗi clip (rule-33).
4. `rules/video-rules.md` (luật gốc 1–67) khi checklist dẫn rule-NN hoặc có xung đột; `content/voice-profile.md`, `templates/script.md` khi soi tone/cấu trúc.
5. Với nội dung HowToLiveBetter: credit bắt buộc ở end card + description — "Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/" và dòng an toàn "Thông tin tham khảo, không thay thế tư vấn chuyên gia" cho health/emergency/legal/finance; không tuyên bố được tác giả chứng thực.

## 8. File và skill liên quan trong repo

- Nguồn chấm: `logs/rule-checklist.md`, `logs/rule-scoring-rubric.md`, `logs/lessons.md`, `logs/decision-log.md`, `rules/video-rules.md`.
- Cổng tự động: `pipeline/scripts/check-rules.py` (`--stt` trước render, `--final --stt` sau render), `pipeline/scripts/check-assets.py`.
- Workflow gốc đang chứa cổng này: `skills/make-video/SKILL.md` §4–§5 (automated gate → gate 1) và `docs/workflow/per-video-pipeline.md` bước 4/9; `pipeline/pipeline.md`.
- Skill liên quan: `skills/script-polish/SKILL.md`, `skills/humanizer/SKILL.md` (OpenCreator dùng trước khi bàn giao); đề xuất skill riêng `skills/rule-review/SKILL.md` (rubric §5) **chưa tạo — chờ Hiệp duyệt**, không tự tạo trong workflow này.
- Chuỗi: Social Research (`research/trends/`) + Deep Research (fact) → OpenCreator Studio (draft) → **Rule Reviewer (file này)** → Hiệp `Chốt` → FLUX Visual / Production (Kokoro Voice, ACE Music, Short Factory, Shorts Cutter, Podcastfy) → Social Poster (draft-only). Xem index khung ở `workflows/agents/` (mỗi agent tự viết file của mình).
