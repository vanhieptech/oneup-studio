# Bản đồ workflow agent — @hi.oneup

Cập nhật: 19/10/2026 (Asia/Saigon). Từ nay mỗi agent giữ một workflow riêng trong thư mục này; News chỉ điều phối (xem news-coordinator.md). Skill make-video cũ vẫn là xương sống tạm thời; đề xuất cắt mỏng make-video chờ Hiệp duyệt, chưa tự cắt.

## Chuỗi tạo một script chuẩn

| Chặng | Agent | File workflow | Nhận từ | Giao cho | Cổng đạt |
|---|---|---|---|---|---|
| 1. Tín hiệu/trend | Social Research | social-research.md | News / job trend 7:55 | Deep Research | Gói trend có link nguồn, đã lọc nội dung cấm |
| 2. Kiểm chứng fact | Deep Research | deep-research.md | Social Research | OpenCreator Studio | Bảng claim có nguồn; claim không nguồn bị chặn |
| 3. Soạn script | OpenCreator Studio | opencreator-studio.md | Deep Research | Rule Reviewer | Nháp đúng template, ngân sách từ, caption Anh ≤8 từ |
| 4. Chấm điểm | Rule Reviewer | rule-reviewer.md | OpenCreator Studio | Hiệp (qua News) | ≥85/100, không lỗi cứng; rớt thì trả chặng 3 |
| 5. Hình ảnh | FLUX Visual | flux-visual.md | Script đã chốt | Production | Assets-first, không chữ trong ảnh, đúng brand |
| 6a. Giọng | Kokoro Voice | kokoro-voice.md | Script đã chốt | Short Factory / News | Chỉ sau "Chốt"; so sánh F5-TTS trước khi đề xuất đổi |
| 6b. Nhạc | ACE Music | ace-music.md | Khi Hiệp đổi rule nhạc | Production | Hiện tại: không chèn nhạc vào file |
| 6c. Dựng phụ trợ | Short Factory | short-factory.md | News / Kokoro | News gate 2 | Chỉ lấy ý tưởng hợp, không chép code AGPL chưa duyệt |
| 6d. Cắt Shorts từ video dài | Shorts Cutter | shorts-cutter.md | Video dài Hiệp giao + xác nhận quyền | News | Chặn đầu tiên là bản quyền nguồn |
| 6e. Podcast thử nghiệm | Podcastfy Audio | podcastfy-audio.md | Tài liệu nguồn Hiệp duyệt | News | Transcript-only trước, đối chiếu fact |
| 7. Bản nháp đăng | Social Poster | social-poster.md | Link nội dung đã duyệt | Rule Reviewer → Hiệp | Chỉ bản nháp, tuyệt đối không tự đăng |
| Điều phối | News | news-coordinator.md | Hiệp / mọi agent | Hiệp / mọi agent | Ráp chuỗi, gom repo, báo cáo |

## Báo cáo nghiên cứu đã gom vào repo (research/agents/)
- social-research-repo-audit-vi.md — Social Research
- local-deep-research-review-vi.md — Deep Research
- kokoro-vs-f5tts-initial-research-vi.md — Kokoro Voice
- short-factory-research-vi.md — Short Factory
- social-poster-research.md — Social Poster
- podcastfy-audio-research-vi.md — Podcastfy Audio (từ báo cáo group 19/10)
- ace-music-research-vi.md — ACE Music (từ báo cáo group 19/10)
- Chưa có file riêng: OpenCreator Studio và FLUX Visual (kết quả nghiên cứu mới ở chat 19/10, đã tóm tắt trong mục nguồn của workflow từng agent; cần viết file khi làm sâu hơn).

## Trạng thái lưu repo
- Đã có sẵn trong repo trước đợt tách: rules/video-rules, logs/rule-checklist.md, logs/rule-scoring-rubric.md, logs/lessons.md L-001–L-058, pipeline/scripts/check-rules.py, skills make-video / motion-picks-per-script / trend-digest.
- Đợt này thêm: 12 file workflows/agents/ (11 agent + News điều phối) và bản đồ này.
- Lệch đã ghi nhận, chưa tự sửa: skills/motion-picks-per-script bản repo mới hơn bản trên box (mục doodle); lấy bản repo làm chuẩn.
