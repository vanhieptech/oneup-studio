---
title: "Nghiên cứu: OpenCreator cho khâu soạn script @hi.oneup"
date: 2026-10-19
source: "OpenCreator Studio nghiên cứu chỉ đọc repo/docs ngày 19/10/2026, chưa cài/chưa chạy code"
id: research.opencreator
type: research
status: reference
updated: 2026-10-19
tags: [opencreator, krillinai, script, tts, video-translation]
---

# Nghiên cứu: OpenCreator (krillinai/OpenCreator)

Nguồn chính: https://github.com/krillinai/OpenCreator · README https://raw.githubusercontent.com/krillinai/OpenCreator/master/README.md · LICENSE https://raw.githubusercontent.com/krillinai/OpenCreator/master/LICENSE · Pricing https://www.open-creator.ai/pricing
Trạng thái kiểm tra (19/10/2026, Asia/Saigon): 13.721 stars, 1.507 forks, 38 open issues, tạo 2024-12-17, push gần nhất 2026-10-19, release mới nhất v3.2.8 (18/10/2026). Tiền thân là KrillinAI (dịch/lồng tiếng video), nay là không gian sáng tạo AI chạy local dùng Codex CLI làm engine tác vụ, kèm giao diện web và app desktop Electron.

## Tính năng dùng được cho @hi.oneup
- **Viết script:** Short Video Script theo chủ đề/khán giả/nền tảng/thời lượng/tone, Article Writer — hợp khâu soạn nháp sau khi đã có fact lock.
- **Tạo ảnh:** GPT Image / Seedream / Kling Image / Gemini, thumbnail và template sáng tạo — chỉ ở mức tham chiếu/thử, hình chính của kênh vẫn theo workflow FLUX/asset sẵn có.
- **Giọng đọc:** OpenAI TTS, MiniMax, Edge TTS (không cần API key), Aliyun, Volcengine — kênh vẫn dùng F5-TTS đã chốt; TTS của OpenCreator chỉ thử khi Hiệp duyệt riêng.
- **Dịch video:** transcribe (cloud Whisper hoặc local faster-whisper/whisper.cpp/WhisperKit), dịch phụ đề bằng LLM, lồng tiếng, sửa phụ đề theo timeline, xuất SRT/audio/video, hỗ trợ dọc/ngang.
- **Chỉnh sửa/nội dung khác:** tải video nhiều nền tảng, tạo video Seedance/Kling/Veo, Stick Figure Animation. Auto Clips và Digital Avatar vẫn đang phát triển, chưa coi là dùng được.

## Giấy phép và rủi ro
- **Apache License 2.0** (xác nhận từ file LICENSE và metadata GitHub): dùng thương mại, sửa và phân phối được, royalty-free, kèm grant bằng sáng chế. Nếu phân phối lại bản sửa phải kèm LICENSE, ghi chú file đã sửa, giữ attribution/NOTICE; không dùng tên OpenCreator làm thương hiệu của mình; phần mềm không có bảo hành.
- Rủi ro không nằm ở code mà ở lớp ngoài: điều khoản của model/provider (OpenAI, Seedance, Kling, Veo, MiniMax...) quyết định quyền dùng output thương mại; tải/dịch video của người khác chạm bản quyền nội dung nguồn và điều khoản nền tảng; clone/lồng tiếng cần quyền với giọng và nội dung gốc; template bên thứ ba phải kiểm credit riêng.
- Kết luận: dùng nội bộ để sản xuất clip gốc cho @hi.oneup thì rủi ro giấy phép thấp; không redistribute app, không tải/dịch nội dung không có quyền.

## Yêu cầu và chi phí
- Stack: TypeScript, React 18 + Vite (web), Fastify (daemon), Electron (desktop), SQLite local, FFmpeg/yt-dlp, Codex CLI. Runtime chỉ nghe 127.0.0.1, dữ liệu mặc định ở `.runtime/`.
- Linux chưa có app desktop — chỉ chạy web từ source: Node.js ≥22, pnpm 9.15.0 (ghim qua packageManager), Codex CLI đã đăng nhập; `pnpm web:dev` mở ở `http://127.0.0.1:19861/`. Desktop chỉ có macOS và Windows (bản Windows chưa ký Authenticode, phải kiểm SHA-256).
- Chi phí kiểu tự mang khóa (BYOK): cần đăng nhập ChatGPT/khóa OpenAI hoặc nhà cung cấp tương thích OpenAI, cộng khóa riêng cho ảnh/video/giọng/transcribe trong Settings; Edge TTS và Whisper local không cần khóa. Hoặc mua credit chính thức $5/2.500, $10/5.000, $20/10.000 (mua một lần, trang pricing ghi hiện không hết hạn; hủy tác vụ vẫn có thể bị tính nếu model đã nhận yêu cầu). Giá từng giây video/phút lồng tiếng cụ thể ngoài calculator ước tính thì **không rõ**, phải xem trong app trước khi chạy thật.
- Đối chiếu máy hiện tại: Node v20.19.2 (thiếu ≥22), pnpm 10.34.6 (repo ghim 9.15.0), chưa có Codex CLI, FFmpeg 7.1.5 có sẵn, RAM 15 GB, đĩa trống ~104 GB — muốn chạy phải cô lập toolchain, không nâng thẳng vào môi trường hiện tại.

## Không hợp / chưa nên dùng ngay
- Chưa cài và chưa chạy thử: chưa đọc tĩnh hết script cài đặt/lockfile, đây là các điểm rủi ro chuỗi cung ứng chính (script build KrillinAI, tải component theo yêu cầu như yt-dlp nightly và Remotion, Skills/MCP mà agent có thể thực thi).
- Không đưa vào trong repo oneup-studio: luật repo là không vendor repo ngoài, mọi asset @hi.oneup chỉ nằm trong oneup-studio.
- Không thay pipeline hiện tại của kênh (Remotion + F5-TTS + check-rules): OpenCreator chỉ là công cụ hỗ trợ ở khâu nháp/thử nghiệm, output vẫn qua gate Rule Reviewer.

## Đề xuất cài an toàn (chờ Hiệp chốt)
1. Clone cô lập ngoài repo ở `/workspace/opencreator-sandbox/`, chốt đúng tag v3.2.8, kiểm checksum nếu dùng bản binary.
2. Đọc tĩnh `package.json`, script build và lockfile trước khi chạy; Node 22 + pnpm 9.15.0 riêng, thư mục dữ liệu và `CODEX_HOME` riêng cho sandbox, `pnpm install --frozen-lockfile` rồi `pnpm audit`.
3. Chạy thử không tốn phí: chỉ loopback 127.0.0.1, file SRT/video tự sản xuất, chưa nhập khóa thật, chưa dùng cookie nền tảng.
4. Cổng chi phí riêng: Hiệp duyệt provider + hạn mức (BYOK hay gói $5) mới thử một tác vụ thật nhỏ và đối chiếu hoá đơn.
5. Cần Hiệp chốt trước: tính năng thử đầu tiên, chạy trên box (web) hay Mac/Windows (desktop), BYOK hay mua credit, có dùng đăng nhập Codex/ChatGPT sẵn có hay tài khoản riêng, và dữ liệu test tự sản xuất hay nội dung tải về.
