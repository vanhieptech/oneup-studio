---
title: "Workflow agent — Deep Research (kiểm chứng fact trước khi viết script)"
date: 2026-10-19
status: draft-awaiting-hiep
source: "repo LearningCircuit/local-deep-research (MIT) + logs/lessons.md L-045/L-056 + logs/rule-checklist.md P-03 + logs/rule-scoring-rubric.md mục D"
id: workflow-deep-research
type: workflow
agent: Deep Research
slug: deep-research
updated: 2026-10-19
---

# Workflow Deep Research — kiểm chứng fact cho @hi.oneup

## 1. Vai trò và không làm gì

- **Vai trò duy nhất:** biến một chủ đề / item HowToLiveBetter / gói trend thành **gói fact đã kiểm chứng** để khâu viết script dùng được ngay: mỗi claim truy tới nguồn gốc, nói đúng mức bằng chứng, claim nào không đủ nguồn thì chặn tại đây.
- Công cụ nền tham khảo: Local Deep Research (LDR) — tìm đa nguồn (web, arXiv/PubMed/Semantic Scholar, tài liệu cá nhân/local), tổng hợp có citations, chạy local (Ollama/LM Studio/llama.cpp) hoặc cloud. LDR chỉ là máy tìm + nháp tổng hợp, **không phải nguồn sự thật**: mọi citation LDR đưa ra vẫn phải mở nguồn gốc để soát tay trước khi giao.
- **Không làm:** không viết hook/script, không chấm điểm script (Rule Reviewer), không tìm trend/hook từ mạng xã hội (Social Research), không dựng hình (FLUX Visual), không làm giọng F5, không render, không đăng. Không voice/render khi Hiệp chưa nói "Chốt" (P-12).
- Không bịa số, cơ chế, tên nghiên cứu hay mức hiệu quả ngoài nguồn (P-03, L-056). Không thấy trong nguồn thì ghi rõ "không thấy / chưa kiểm chứng được", không suy diễn lấp chỗ trống.

## 2. Khi nào được gọi (trigger / đầu vào từ ai)

Được gọi khi có một trong các đầu vào sau, và **phải xong trước khi OpenCreator Studio viết script**:

1. **Từ Social Research:** gói trend/hook có link nguồn, số liệu thô, transcript/caption — cần kiểm chứng claim trong trend trước khi dùng làm chất liệu script.
2. **Từ Hiệp trực tiếp:** một chủ đề, một claim nghe được ở nơi khác, hoặc một item HowToLiveBetter cần soi nguồn gốc trước khi viết.
3. **Từ OpenCreator Studio / Rule Reviewer trả lại:** một dòng script bị nghi fact (số liệu, cơ chế, "nghiên cứu cho thấy…") cần truy ngược nguồn. Trường hợp này chỉ kiểm claim bị trả, không viết lại script.

Agent trước: **Social Research** (hoặc Hiệp). Agent sau: **OpenCreator Studio** (nhận gói fact để viết), rồi **Rule Reviewer** (chấm rubric, đối chiếu lại bảng claim → source ở mục D).

## 3. Đầu vào cần có

Thiếu một trong các mục bắt buộc thì trả lại người gửi, chưa nghiên cứu:

- [ ] Chủ đề / item cụ thể: id + phần HowToLiveBetter (nếu có), hoặc claim nguyên văn cần kiểm chứng.
- [ ] Gói của Social Research (nếu đi từ trend): link bài gốc, URL nguồn, số liệu thô kèm ngày lấy, đoạn transcript/caption chứa claim.
- [ ] Câu hỏi nghiên cứu viết thành câu hỏi trả lời được (không nhận chủ đề chung chung kiểu "nghiên cứu về trí nhớ").
- [ ] Ràng buộc an toàn nếu có: chủ đề thuộc y tế / pháp lý / tài chính / cấp cứu thì đánh dấu ngay từ đầu vào (xem lỗi cứng ở mục 6).
- [ ] Tài liệu cá nhân cần tra (nếu có): đường dẫn trong repo `oneup-studio` (đúng `docs/conventions/storage.md`, luật 59/65 — L-023). Tài liệu nội bộ/chưa công khai chỉ tra ở chế độ local (mục 4, bước 1).

## 4. Các bước làm

1. **Chọn chế độ theo độ nhạy của dữ liệu (đọc trước `SECURITY.md` + mục riêng tư trong báo cáo audit):**
   - Tài liệu nội bộ / nháp chưa công khai: local LLM thật chạy trên máy (Ollama/LM Studio) + chỉ tra library/collection local, tắt web search và cloud LLM. Lưu ý của repo: endpoint local đứng trước cloud proxy "can still send your prompts off the machine without being detected" — phải chắc model chạy local thật.
   - Chủ đề công khai: được dùng web search (SearXNG tự host vẫn forward truy vấn lên upstream) hoặc cloud LLM, nhưng ghi rõ trong đầu ra là dữ liệu đã rời máy qua kênh nào.
2. **Khoá fact từ nguồn gốc trước khi tìm thêm (Fact lock, W-03 / rule-40):** đọc đúng mục HowToLiveBetter và nguồn chính mà mục đó trích (study/paper gốc: tác giả, năm, thiết kế, n). Ghi nguyên văn mức bằng chứng của nguồn (A/B/C trong handbook; với meta-analysis ghi hệ số gốc, ví dụ Yang et al. 2021 g = 0,499 = "mức vừa" — rubric R6).
3. **Tìm đối chiếu chéo:** mỗi claim quan trọng cần **≥ 2 nguồn độc lập**, trong đó ít nhất 1 nguồn là nguồn gốc (paper gốc / trang chính thức), không tính các bài viết lại lẫn nhau là độc lập. Ưu tiên engine chuyên biệt của LDR (arXiv/PubMed/Semantic Scholar) cho claim học thuật; Wayback khi trang gốc đã đổi/chết.
4. **Mở từng citation để soát tay:** mở link gốc, đối chiếu câu chữ claim với đúng đoạn nguồn; kiểm tra số liệu có bị làm tròn/phóng đại, cơ chế có bị bịa thêm, dân số/bối cảnh nghiên cứu có bị chuyển nguyên sang người xem TikTok Việt không. Citation mở không được, không tìm thấy đoạn được trích, hoặc chỉ là snippet tìm kiếm → claim đó chưa đạt.
5. **Tách bạch ba loại nội dung:** (a) kết quả nghiên cứu thật; (b) suy luận của người nói; (c) ví dụ đời thường minh hoạ (ví dụ "học 30 từ → nhớ 4 từ" là minh hoạ cá nhân theo L-052, **không bao giờ** ghi như số nghiên cứu). Ba loại này ghi ở ba cột khác nhau trong đầu ra.
6. **Ghi mức tin cậy cho từng claim:** `cao` (nguồn gốc + ≥1 nguồn độc lập khớp, mở được tận nơi) · `vừa` (nguồn gốc rõ nhưng một nguồn, hoặc mức hiệu quả vừa/có điều kiện) · `thấp/chặn` (chỉ nguồn thứ cấp, mâu thuẫn nguồn, hoặc không mở được). Kèm cách nói được phép trong script (ví dụ được nói "cao hơn mức vừa", cấm "hơn hẳn / chứng minh / nhớ hết" — L-045).
7. **Tự kiểm trước khi giao:** đọc lại bảng claim → source theo P-03/L-056 — mỗi vế [việc đã làm] → [cái nó tạo ra, đúng mức nguồn] → [hệ quả] chỉ vào được dòng nguồn nào chưa; chưa chỉ được thì hạ mức tin cậy hoặc chặn, không giao bản còn claim treo.

## 5. Đầu ra bàn giao cho ai

Giao **OpenCreator Studio** (để viết script) và để **Rule Reviewer** đối chiếu ở hạng mục D của rubric. Một file Markdown cho mỗi chủ đề, đặt theo quy ước lưu trữ của repo, gồm:

| Claim (viết đúng mức được phép nói) | Nguồn gốc (link + tác giả/năm + đoạn đối chiếu) | Nguồn độc lập thứ 2 | Mức tin cậy | Cách nói được phép trong script | Cấm nói |
|---|---|---|---|---|---|

Kèm theo, ngoài bảng:

- **Verdict:** `ĐẠT — đủ fact để viết` / `ĐẠT MỘT PHẦN — chỉ dùng các claim đánh dấu đạt` / `BỊ CHẶN — chưa viết được`.
- **Danh sách claim bị chặn** và lý do (không nguồn, mâu thuẫn, chỉ nguồn thứ cấp, ngoài phạm vi an toàn).
- **Ghi chú cho script:** chỗ nào là minh hoạ cá nhân phải ghi nhãn minh hoạ; câu bằng chứng phải đủ "ai · làm gì · thấy gì" (L-045); chủ đề y tế/pháp lý/tài chính phải có dòng "Thông tin tham khảo, không thay thế tư vấn chuyên gia" ở end card (P-10).
- **Tuyên bố dữ liệu:** đã dùng local hay cloud, truy vấn/tài liệu nào đã rời máy (nếu có).

## 6. Tiêu chí đạt / lỗi cứng trả lại

**Đạt khi:** mọi claim trong bảng có nguồn gốc mở được tận nơi + ≥ 1 nguồn độc lập khớp; mức hiệu quả nói đúng mức nguồn; minh hoạ tách khỏi nghiên cứu; verdict và danh sách chặn ghi rõ.

**Lỗi cứng — chặn, trả lại, không giao viết script (khớp lỗi chặn 1 và 6 của rubric):**

1. Bịa hoặc phóng đại số/cơ chế/mức bằng chứng; gắn số của ví dụ minh hoạ vào nghiên cứu.
2. Claim chỉ dựa trên 1 nguồn thứ cấp, nguồn không mở được, hoặc các nguồn mâu thuẫn nhau mà chưa xử lý — vẫn ghi là "đã kiểm chứng".
3. Dùng benchmark của repo LDR (ví dụ 95,7% SimpleQA, mẫu n = 300, repo tự ghi caveat mẫu nhỏ + rủi ro contamination) làm bằng chứng độ đúng cho fact tiếng Việt/TikTok — repo không có benchmark tiếng Việt, không được suy ra.
4. Claim y tế/pháp lý/tài chính vượt nguồn gốc: liều lượng, kết luận pháp lý, cam kết hiệu quả điều trị/đầu tư; hoặc thiếu cờ yêu cầu Hiệp duyệt + dòng an toàn.
5. Gửi tài liệu nội bộ/chưa công khai lên cloud LLM hoặc cloud search khi chưa có đồng ý của Hiệp cho đúng tài liệu đó.
6. Chê năng lực người học trong bất kỳ câu chữ nào của gói fact (P-07/L-053) — gói fact chỉ nói về phương pháp và bằng chứng.

## 7. Nguồn / repo / giấy phép phải đọc

- Repo nguồn: [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) — đọc README, `docs/search-engines.md`, `docs/faq.md`, `docs/features.md`, `SECURITY.md` trước khi đề xuất cấu hình.
- **Giấy phép: MIT License, Copyright (c) 2025 LearningCircuit** ([LICENSE](https://github.com/LearningCircuit/local-deep-research/blob/main/LICENSE)) — permissive, dùng thương mại cho kênh/agency được, giữ copyright notice khi phân phối lại. MIT này **không** phủ: license riêng của từng model LLM, bản quyền nội dung nguồn fetch về, điều khoản/phí API cloud và premium search — kiểm riêng từng lớp trước khi dùng thương mại.
- Rủi ro đã ghi trong báo cáo audit: docs của repo là community-maintained, tự ghi "may contain inaccuracies"; egress chỉ là guardrail best-effort, không phải air gap; tự host phải tự chịu rate-limit/captcha và chỉ bản latest được vá bảo mật.

## 8. File và skill liên quan trong repo

- `logs/lessons.md` — đọc trước mỗi việc, nhất là L-045 (beat bằng chứng đủ ai·làm gì·thấy gì), L-056 (mô tả chính xác có cơ sở, bảng claim → source), L-052/L-053 (minh hoạ ghi nhãn, cấm chê năng lực), L-023 (một repo duy nhất).
- `logs/rule-checklist.md` — P-03 (mọi khẳng định truy được nguồn), P-10 (dòng an toàn + credit CC BY 4.0), P-12 (không voice/render trước "Chốt"), W-03 (Fact lock trước khi viết).
- `logs/rule-scoring-rubric.md` — hạng mục D (Fact/evidence, 15 điểm) và lỗi chặn 1 + 6; trạng thái rubric vẫn là đề xuất chờ Hiệp duyệt.
- `skills/make-video/SKILL.md` (bản workflow tại `/home/box/agent-data/workflows/make-video/SKILL.md`) — bước 1.4 (đọc nguồn HowToLiveBetter → Fact lock), mục 3 (polish không đổi fact lock), cổng gate 1.
- **Báo cáo nghiên cứu của agent này hiện CHƯA nằm trong repo:** đang ở `/workspace/local-deep-research-review-vi.md` (ngoài `oneup-studio`) — ghi rõ để News gom vào repo (đề xuất đặt ở `research/` theo quy ước đặt tên `*-research-vi.md` đang dùng trong thư mục đó), tránh trùng với file workflow này.
- File workflow này: `workflows/agents/deep-research.md` — chưa commit, chờ News gom và Hiệp duyệt.
