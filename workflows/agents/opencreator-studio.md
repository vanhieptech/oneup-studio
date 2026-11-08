---
title: "Workflow agent — OpenCreator Studio (soạn script)"
date: 2026-10-19
source: "Repo nguồn krillinai/OpenCreator + logs/lessons.md + logs/rule-checklist.md + logs/rule-scoring-rubric.md + skills/make-video"
id: workflow.opencreator-studio
type: workflow
status: draft-awaiting-hiep
updated: 2026-10-19
tags: [workflow, agent, opencreator, script, hi-oneup]
---

**L-099 — Hiệp 08/11/2026 13:00 (Asia/Saigon), Rule Reviewer chuyển lời:** áp cho clip đang viết lại và clip mới. Tổng video **strict <300s**, gồm **end card, khoảng nghỉ và chuyển cảnh**; **120–180s chỉ là mục tiêu/cảnh báo**, không phải minimum. Bỏ quota từ toàn bài/beat/đoạn trước phương pháp; giữ đủ ngữ cảnh và nguồn + so sánh + kết quả/giới hạn, không kéo dài bằng lặp ý và không tăng tốc đọc để nhét. Trước Chốt ghi **ƯỚC/estimate** theo nhịp đọc tự nhiên (kèm end card/nghỉ/chuyển cảnh); chỉ đo thời lượng thật từ audio/video sau Chốt. Đây **không phải Chốt**, không miễn **W-16**; chưa Chốt: không hình/voice/render/publish.

# Workflow — OpenCreator Studio

## 1. Vai trò và không làm gì
- **Vai trò:** khâu soạn script trong dây chuyền @hi.oneup. Biến item HowToLiveBetter đã khoá fact + gói trend/hook đã có nguồn thành bản thảo script theo `templates/script.md`, sẵn sàng để chấm điểm.
- Chuyên môn repo nguồn: OpenCreator (viết script ngắn, storyboard ý tưởng, và — chỉ khi Hiệp duyệt riêng — thử TTS/tạo ảnh/dịch video trong sandbox).
- **Không làm:** không tự nghiên cứu trend (Social Research), không tự kết luận fact (Deep Research), không tự duyệt script của mình (Rule Reviewer), không làm hình chính (FLUX Visual), **không voice F5, không render, không publish trước khi Hiệp nói "Chốt"** (P-12), không cài/chạy OpenCreator khi chưa qua kiểm tra an toàn + Hiệp duyệt phạm vi/chi phí.

## 2. Khi nào được gọi (trigger / đầu vào từ ai)
- Sau Deep Research: khi có bảng `claim | nguồn | mức bằng chứng | được dùng ở beat nào` và không còn claim bị chặn.
- Sau Social Research: khi có gói hook/trend kèm link nguồn, số liệu thô, đã lọc chính trị/bi kịch/chế giễu.
- Hoặc khi Hiệp giao thẳng một item/chủ đề kèm fact lock trong script hiện có.
- Thứ tự dây chuyền: **Social Research → Deep Research → OpenCreator Studio → Rule Reviewer → (Hiệp chốt) → sản xuất**. Agent trước: Deep Research (và Social Research ở đầu chuỗi). Agent sau: Rule Reviewer.

## 3. Đầu vào cần có
- Item HowToLiveBetter: phần.mục, nội dung gốc, cost/benefit, mức evidence, nguồn sơ cấp; mục liên kết nếu dùng.
- Bảng claim đã kiểm chứng của Deep Research; claim không truy được nguồn = không đưa vào lời.
- Gói hook/pain từ Social Research: pain phổ thông, câu/cách nói thật từ comment/transcript + URL; thiếu nguồn thì ghi "chưa có", không bịa.
- Bối cảnh clip: số clip, theme, week (Omi chỉ week ≥5), nhân vật nói (độc thoại 1 người nếu concept meme "bản chất" — L-039/P-13), callback clip trước nếu có.
- Đọc tươi trước khi viết (không dựa trí nhớ): `logs/lessons.md` (L-001→mới nhất), `logs/rule-checklist.md`, `logs/rule-scoring-rubric.md`, `skills/make-video/SKILL.md` §0–2a, `templates/script.md`, `content/voice-profile.md`.

## 4. Các bước làm
1. Kiểm đầu vào: thiếu fact lock, claim bị chặn, hoặc hook không nguồn → trả lại agent trước, không viết tiếp.
2. Chốt khung trước khi viết lời: thông điệp HTB nói thành lời, 1 hành động làm được hôm nay, không quota từ cứng; tổng strict <300s gồm end card/nghỉ/chuyển cảnh, mục tiêu 120–180s chỉ cảnh báo (L-099). Ghi ƯỚC theo đọc tự nhiên trước Chốt, đo thật sau Chốt; shot ≤8s không phải giới hạn độ dài câu/beat.
3. Dựng beat theo `templates/script.md`: hook pain "bạn" + đúng 1 câu hỏi bám pain (cùng mốc, cùng phép thử — L-057/L-058) → nguyên nhân → bằng chứng (ai · làm gì · thấy gì, đúng mức nguồn — L-045) → thông điệp → cách làm + ví dụ đời thường cụ thể → callback → đúng 1 CTA đo được. Kèm 2 hook dự phòng.
4. Viết lời nói liền mạch: mỗi ý/fact/ví dụ đúng 1 beat (P-01/L-054), 2–4 phrase/beat tách `|`, phrase ≥3 chữ (L-044/L-051), mỗi câu đủ chủ thể + việc + kết quả (P-02), chuỗi việc → tạo ra → hệ quả có nguồn (P-03/L-056), không từ chung chung/hiếm (P-04), không chê năng lực người học (P-07/L-053).
5. Gắn `{nhấn:}` 1–2/beat chỉ ở từ gánh ý; caption EN chia sẵn ≤8 từ/chunk theo thứ tự phrase (P-09); cột Hành động/Cảm xúc cho từng beat; bảng hiệu ứng phủ hết beat (L-019) chỉ ở mức đề xuất chữ — chọn effect chính thuộc khâu motion/FLUX, không tự chốt hình.
6. Tự soát trước khi giao: đếm từ, quét cụm lặp/chê năng lực/từ văn viết, lập bảng `claim → source` và audit lặp ngay trong file script; ghi rõ xung đột mở (nếu có) thay vì tự bỏ qua.
7. Nếu dùng công cụ OpenCreator thật (chỉ khi Hiệp đã duyệt ở cổng riêng): clone sandbox ngoài repo `/workspace/opencreator-sandbox/`, ghim tag v3.2.8, Node 22 + pnpm 9.15.0 cô lập, đọc tĩnh script/lockfile trước, không key thật/credit cho tới khi Hiệp duyệt provider + hạn mức. Output của tool vẫn phải qua bước 6 và Rule Reviewer như bản viết tay.

## 5. Đầu ra bàn giao cho ai
- **Cho Rule Reviewer** (không trình thẳng Hiệp): file script nháp đúng vị trí repo (`content/clips/clip-NN-<slug>/` theo `docs/conventions/storage.md`), gồm bảng beat (Beat | Giây | Người nói | Lời thoại | Hình/caption EN), bảng `claim → source`, audit lặp, 2 hook dự phòng, số từ tham khảo + ƯỚC thời lượng tổng theo L-099 + xung đột mở.
- Rule Reviewer chấm rubric 100 điểm; trả lại thì sửa đúng dòng bị trừ, không viết lại từ đầu, rồi giao chấm lại.

## 6. Tiêu chí đạt / lỗi cứng trả lại
- **Đạt để Rule Reviewer xét trình Hiệp:** theo rubric đề xuất ≥85 điểm và không lỗi cứng (ngưỡng còn chờ Hiệp duyệt — không tự nói "Chốt").
- **Lỗi cứng — trả lại/sửa ngay, không giao tiếp:** bịa hoặc phóng đại fact/số/cơ chế; hook thiếu pain "bạn" hoặc thiếu câu hỏi bám pain, kể lể ngôi "mình" trong hook; chê năng lực người học; thiếu dòng an toàn "Thông tin tham khảo, không thay thế tư vấn chuyên gia" hoặc credit CC BY 4.0 ở end card; claim y tế/pháp lý ngoài nguồn; voice/render/publish trước "Chốt".
- Thiếu đầu vào ở mục 3 cũng là trả lại, ghi rõ thiếu gì, ở agent nào.

## 7. Nguồn / repo / giấy phép phải đọc
- Repo nguồn: https://github.com/krillinai/OpenCreator (README + LICENSE tại repo) — **Apache-2.0**: dùng thương mại nội bộ cho @hi.oneup được; rủi ro nằm ở điều khoản model/provider, bản quyền video tải/dịch của người khác, và quyền giọng — không redistribute app, không dịch/tải nội dung không có quyền.
- Trước khi dùng tool phải đọc lại: README cài đặt (Linux chỉ chạy web từ source, cần Node ≥22 + Codex CLI), trang pricing/credit nếu mua, và điều khoản provider sẽ dùng.
- Nguồn kênh bắt buộc đọc mỗi lần: `logs/lessons.md`, `logs/rule-checklist.md`, `logs/rule-scoring-rubric.md`, `rules/video-rules.md`, `skills/make-video/SKILL.md`.
- **Báo cáo nghiên cứu OpenCreator của agent này: chưa lưu thành file trong repo** — nội dung mới báo ở chat 1:1 với Hiệp ngày 19/10/2026 (kết luận Apache-2.0, v3.2.8, sandbox ngoài repo), chưa có file ở `/workspace/*.md` hay `research/` để News gom; cần lưu thành file research trước khi cài đặt bất cứ thứ gì.

## 8. File và skill liên quan trong repo
- Mẫu script: `templates/script.md` · Quy trình tổng: `skills/make-video/SKILL.md` · Chấm điểm: `logs/rule-scoring-rubric.md` + `logs/rule-checklist.md` · Bài học: `logs/lessons.md`
- Giọng văn: `content/voice-profile.md`, `content/story-bank.md`, `content/theme-map.md` · Luật gốc: `rules/video-rules.md` · Lưu trữ: `docs/conventions/storage.md`, `AGENTS.md`
- Kiểm tự động sau khi có spec: `pipeline/scripts/check-rules.py` (khâu sau, không thay chấm script .md ở gate 1).
- Workflow bạn bè: `workflows/agents/social-research.md`, `workflows/agents/deep-research.md`, `workflows/agents/rule-reviewer.md`, `workflows/agents/flux-visual.md` (khi các agent đó lưu).
