---
id: research.skillopt
type: research
status: reference
updated: 2026-10-12
tags: [skills, evaluation]
---
# Đánh giá microsoft/skillopt (12/10/2026)
**Có tồn tại [đã xác minh]:** https://github.com/microsoft/skillopt (tên chính thức "SkillOpt"). Kèm paper arXiv 2605.23904, bài viết của Microsoft Research (24/7/2026), và gói PyPI `skillopt` (v0.1.0 ngày 2/6/2026, v0.2.0 ngày 2/7/2026).
- **Làm gì:** coi file skill (markdown) như "tham số" để huấn luyện cho một agent có model cố định. Một model optimizer đọc các lần chạy đã chấm điểm rồi đề xuất sửa (thêm / xoá / thay) trong skill. Bản sửa chỉ được nhận khi điểm trên tập validation tăng. Kết quả là file `best_skill.md` (300–2.000 token), lúc dùng không tốn thêm lần gọi model nào. Có thêm **SkillOpt-Sleep**: chạy offline mỗi đêm, xem lại các phiên làm việc của Claude Code / Codex / Copilot để gom và chỉnh skill. Có WebUI (Gradio).
- **License:** MIT (Microsoft, 2026).
- **Mức hoạt động:** commit gần nhất 6/10/2026 (sửa bảo mật, thêm provider openai_compatible), số PR đã lên #305. Dự án đang được phát triển tích cực nhưng vẫn ở 0.x, mới khoảng 4 tháng tuổi. Trang GitHub qua công cụ fetch báo 0 sao, có thể do cache, nên mình không dùng con số đó.
- **Yêu cầu:**
  - Python ≥3.10, gói `openai`, `azure-identity`.
  - Cần **model LLM cho cả 2 vai** (optimizer và target): OpenAI / Azure / Claude / Qwen qua vLLM / Copilot / Cursor exec, hoặc bất kỳ endpoint `openai_compatible` nào (ví dụ Ollama, LM Studio chạy local).
  - Cần **một benchmark có chấm điểm tự động**: adapter, data loader, hàm chấm điểm cho từng lần chạy, cùng tập train và validation.
- **Chi phí:**
  - API trả phí: mỗi epoch chạy hàng chục đến hàng trăm rollout cộng các lần gọi optimizer, nên tốn tiền API thật. Mình chưa đo con số.
  - Model local (Ollama, Qwen trên Mac): miễn phí nhưng chậm, và optimizer yếu thì sửa skill kém.
  - Dùng qua `claude_code_exec` / `cursor_exec`: tốn hạn mức của gói đang trả.

## Có hợp với skill của kênh không?
- **motion-picks-per-script, skill viết script sau này:** đầu ra mang tính chủ quan (đẹp, tự nhiên, giữ chân người xem). SkillOpt cần **hàm chấm điểm tự động và đáng tin**, mà hiện mình chưa có. Chỉ số thật (tỉ lệ xem hết) về chậm, mỗi tuần 3 điểm dữ liệu, quá ít để làm tập validation.
- **"Chỉ công cụ miễn phí":** chỉ đạt khi chạy model local, mà chất lượng lúc đó không chắc. Nếu dùng API thì vi phạm luật 24.

## Đề xuất: **chưa áp dụng bây giờ, nhưng mượn cách làm.**
1. Áp dụng tinh thần của SkillOpt bằng tay qua luật 33: mỗi góp ý là một "điểm", sửa skill có giới hạn, và chỉ giữ bản sửa nếu clip sau tốt hơn. File `logs/decision-log.md` chính là tập dữ liệu sau này.
2. Xem lại khi có ≥20 clip đã đăng kèm chỉ số và góp ý. Khi đó có thể dựng benchmark nhỏ: input là script, output là motion picks, chấm theo rubric và lịch sử duyệt của Hiệp. Thử với model local qua `openai_compatible` (Ollama) để giữ đúng luật miễn phí.
3. SkillOpt-Sleep đáng thử sớm hơn nếu sau này Hiệp dùng Claude Code / Codex hằng ngày trên Mac, nhưng cần Hiệp đồng ý vì nó đọc lịch sử phiên làm việc.
**Phương án gần nhất khác** [cần kiểm lại]: DSPy (MIT) với optimizer MIPRO / GEPA cũng tối ưu prompt theo metric và cũng cần metric. TextGrad (MIT). Cả hai đều có cùng điểm nghẽn: phải có metric.
