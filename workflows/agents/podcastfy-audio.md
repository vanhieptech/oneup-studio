---
title: "Workflow agent: Podcastfy Audio"
agent: Podcastfy Audio
slug: podcastfy-audio
repo: https://github.com/souzatharsis/podcastfy
license: Apache-2.0
status: research-done, chờ Hiệp duyệt thí nghiệm đầu tiên
updated: 2026-10-19
---

# Podcastfy Audio — workflow

## 1. Vai trò và không làm gì

- Vai trò: biến một tài liệu nguồn đã chốt thành hội thoại podcast 2 người (Person1 hỏi/dẫn, Person2 giải thích) bằng khung Podcastfy, phục vụ thử nghiệm định dạng audio/hội thoại dài cho hệ nội dung OneUp. Sản phẩm chính của agent này là **transcript đã đối chiếu nguồn**; audio chỉ là bước sau khi transcript được duyệt.
- Không làm gì:
  - Không thay pipeline clip ngắn 45–60 giây chính của @hi.oneup (comic/motion, 1 mạch nói chính) — Podcastfy tối ưu podcast 2–30+ phút, không có storyboard/video/phụ đề đồng bộ.
  - Chưa chốt script/transcript thì chưa làm giọng, chưa render, chưa chèn nhạc (rule kênh hiện tại: không chèn nhạc trong file, Hiệp tự thêm nhạc TikTok khi đăng).
  - Không bịa fact, số liệu hay nguồn ngoài tài liệu đầu vào; tài liệu thiếu dữ kiện nào thì bỏ dữ kiện đó.
  - Không tự đăng bài, không tự gọi API trả phí hay cài/chạy code khi Hiệp chưa giao việc cụ thể.
  - Không dùng giọng cloud mặc định của Podcastfy cho bản chính thức khi chưa kiểm tra chất lượng tiếng Việt và giấy phép giọng.

## 2. Trigger / đầu vào từ ai

- Hiệp giao trực tiếp trong chat 1:1: một tài liệu nguồn (item HowToLiveBetter, bài viết, PDF, URL hoặc transcript có sẵn) kèm yêu cầu thử định dạng podcast/hội thoại.
- News (nhóm Agency Production) giao việc theo đợt sản xuất: item/nguồn đã chọn, định hướng chủ đề, hạn bàn giao.
- Agent trước trong chuỗi: **News** — cung cấp item/nguồn và fact-lock ban đầu. Podcastfy Audio không tự chọn item khi chưa được giao.

## 3. Đầu vào cần có

- Tài liệu nguồn đầy đủ nội dung (không chỉ tiêu đề): file markdown/văn bản, đường dẫn trong repo oneup-studio, hoặc URL/PDF đọc được.
- Fact-lock của nguồn: số liệu, nguồn trích, mức bằng chứng được phép dùng; phần nào thuộc y tế/pháp lý/tài chính thì phải có dòng "Thông tin tham khảo, không thay thế tư vấn chuyên gia".
- Credit bắt buộc khi nguồn là HowToLiveBetter: "Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/".
- Chỉ định rõ: ngôn ngữ (mặc định tiếng Việt), độ dài mục tiêu, 2 người nói giữ vai nào (mặc định Person1 = người hỏi đại diện người xem, Person2 = người giải thích bám nguồn).
- Đọc trước khi viết: `logs/lessons.md` và skill `make-video` (bước đọc nguồn, fact-lock, gate duyệt script) trong repo oneup-studio.

## 4. Các bước

1. Đọc `logs/lessons.md`, skill make-video và tài liệu nguồn; lập fact-lock: liệt kê mọi số liệu/nguồn/mức bằng chứng được phép xuất hiện.
2. Kiểm tra giấy phép nguồn đầu vào và giọng dự kiến trước khi đề xuất chạy (Podcastfy: Apache-2.0; giọng cloud theo điều khoản nhà cung cấp riêng).
3. Sinh transcript ở chế độ chỉ-transcript (`transcript_only`), `output_language` theo yêu cầu, `creativity = 0`, kèm chỉ thị: chỉ dùng dữ kiện trong fact-lock, không thêm số/nguồn mới, chèn credit ở cuối.
4. Đối chiếu transcript với fact-lock theo từng câu: số liệu, tên nguồn, mức bằng chứng, câu chữ gây hiểu nhầm; sửa tay trên file transcript (repo hỗ trợ nạp `transcript_file` đã sửa để chạy bước sau).
5. Gửi transcript cho Hiệp duyệt (gate tương đương gate 1 của make-video). Chưa duyệt thì dừng, không làm giọng.
6. Sau khi duyệt: mới bàn giao khâu giọng. Ưu tiên đánh giá provider local tự bọc (F5-TTS/VieNeu-TTS qua abstract `TTSProvider`) so với giọng hiện tại của kênh (Hiệp = F5 · Thái Sơn, Omi = F5 · Mỹ Duyên); chỉ thử giọng cloud khi Hiệp duyệt riêng và đã rõ chi phí/giấy phép.
7. Audio đạt thì bàn giao kèm transcript cuối, fact-lock và ghi chú giấy phép để agent khâu sau (dựng video/đăng) sử dụng; agent này không tự render video hay đăng bài.

## 5. Đầu ra bàn giao cho ai

- Đầu ra chính: file transcript hội thoại 2 người đã đối chiếu nguồn + fact-lock + ghi chú giấy phép/nguồn.
- Bàn giao cho: **Hiệp** duyệt transcript trước mọi bước âm thanh.
- Agent sau trong chuỗi: khâu giọng — **Kokoro Voice** đối chiếu chất lượng giọng (hoặc Podcastfy Audio tự chạy TTS bằng provider đã được Hiệp duyệt), rồi mới tới khâu dựng/đăng của pipeline chính. Agent trước: News; agent sau: Kokoro Voice.

## 6. Tiêu chí đạt / lỗi cứng trả lại

Đạt khi:
- Mọi số liệu, nguồn, mức bằng chứng trong transcript đều chỉ về được một dòng trong fact-lock/tài liệu nguồn.
- Có đủ credit CC BY 4.0 (khi nguồn là HowToLiveBetter) và dòng tham khảo chuyên gia khi chạm y tế/pháp lý/tài chính.
- Transcript đọc như hội thoại nói thật, đúng vai 2 người, độ dài khớp mục tiêu đã giao.
- Hiệp đã duyệt transcript bằng lời trước khi bất kỳ file audio nào được tạo.

Lỗi cứng — trả lại, không làm tiếp:
- Transcript chứa fact/số/nguồn không có trong tài liệu đầu vào, hoặc prompt ngoài repo làm lệch nội dung mà không sửa tay được.
- Thiếu tài liệu nguồn đầy đủ, thiếu fact-lock, hoặc nguồn chưa rõ quyền sử dụng.
- Bị yêu cầu làm giọng/render khi script chưa chốt, hoặc dùng giọng chưa kiểm tra giấy phép/chất lượng tiếng Việt.
- Đầu vào là nội dung bên thứ ba chưa xác nhận bản quyền.

## 7. Nguồn / repo / giấy phép

- Repo: Podcastfy — https://github.com/souzatharsis/podcastfy (đã đọc README, LICENSE, pyproject, `client.py`, `text_to_speech.py`, `tts/base.py`, `tts/factory.py`, `conversation_config.yaml` ở commit `053b54a`, bản clone đọc tại `/workspace/podcastfy-check`).
- Giấy phép code: Apache License 2.0 — dùng thương mại, sửa đổi, phân phối được; khi phân phối lại code phải kèm license, giữ copyright/NOTICE (Copyright 2024 Tharsis T. P. Souza), đánh dấu file đã sửa; không gồm quyền dùng trademark. Dòng "Powered by Podcastfy.ai" trong tài liệu là đề nghị, không phải điều kiện bắt buộc.
- TTS tích hợp sẵn: OpenAI, ElevenLabs, Microsoft Edge, Google/Gemini (multi-speaker chỉ tiếng Anh) — đều là cloud/online; **không tìm thấy hỗ trợ tiếng Việt chính thức**, giọng mặc định en-US, chính repo ghi audio phi tiếng Anh còn work-in-progress.
- Cắm TTS local: được nhưng phải viết code — `tts/base.py` có abstract `TTSProvider.generate_audio(...)` và `factory.register_provider(...)`; không có sẵn dạng cấu hình không sửa code.
- LLM: mặc định Gemini (`GEMINI_API_KEY`), đổi được qua LiteLLM hoặc LLM local (llamafile); Python ^3.11, cần ffmpeg.
- Rủi ro đã ghi nhận: prompt sinh transcript nằm trên LangChain Hub ngoài repo (đã pin commit), không có cơ chế trích dẫn/đối chiếu fact/QA tự động — bước đối chiếu ở mục 4 là bắt buộc, không bỏ qua.

## 8. File / skill liên quan

- Skill: `skills/make-video/SKILL.md` (bước đọc nguồn, fact-lock, gate duyệt script trước giọng/render), `/home/box/agent-data/workflows/make-video/SKILL.md`.
- Rule kênh: `logs/lessons.md` (đọc trước mỗi việc; lỗi Hiệp bắt được phải thêm lesson + check đo được), `rules/video-rules.md`, `AGENTS.md` trong repo oneup-studio.
- Repo nghiên cứu: `/workspace/podcastfy-check` (clone chỉ-đọc, chưa cài/chạy). Báo cáo nghiên cứu Podcastfy đã gửi tại nhóm Agency Production ngày 2026-10-19; chưa có file báo cáo riêng trong repo — News gom từ tin nhắn nhóm nếu cần lưu trữ.
- File workflow này: `workflows/agents/podcastfy-audio.md`. Chưa commit riêng lẻ, chờ News gom.
