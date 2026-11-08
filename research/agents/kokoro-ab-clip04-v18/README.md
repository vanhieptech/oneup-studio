# Kokoro-Vietnamese vs F5 v18: thử c07 / c08 / c14 (clip-04)

**Trạng thái (2026-10-20 23:30, UTC+7): đã cài xong, CHƯA synth, CHƯA load model.** News yêu cầu chờ F5 v18 render xong rồi mới load Kokoro (lần trước chạy hai model cùng lúc bị hết RAM, L-041). Lúc kiểm tra, F5 `f5tts_gen.py batch-all.json` vẫn đang chạy (PID 722198, cwd `/workspace/voice-work/clip-04-v18c`, ~5,4 GB RSS, RAM còn trống ~4 GB). Thư mục này chỉ để thử nghiệm, không phải giọng sản xuất, không ghi gì vào `final/` của clip.

## Câu thử (lấy nguyên văn từ chunk table trong `final/script-v18-delivery.md`, khớp `script-v18-LOCKED.md`)
| id | Nhân vật | Text nhập | Nhấn (sau quyết định của Rule Reviewer 23:17) |
|---|---|---|---|
| c07 | Hiệp (nam) | nếu kiểm tra ngay thì nhóm đọc lại làm tốt hơn. | kiểm tra ngay |
| c08 | Hiệp (nam) | Nhưng hai ngày sau, nhóm tự kiểm tra lại nhớ hơn hẳn. | hai ngày sau |
| c14 | Hiệp (nam) | thấy lớp có kiểm tra nhỏ thì điểm cao hơn lớp không làm kiểm tra nhỏ, ở mức vừa. | cao hơn |

Clip-04 chỉ có Hiệp, không có Omi. Ba câu này không có TOEIC, Omi, chữ số hay tiếng Anh nên không cần phiên âm, và cũng không có tag. Đọc ở speed 1.0, không tua. Mỗi chunk là đúng 1 lần gọi model, không cắt bên trong output (L-016). Bản cộng đồng không có SSML và không chỉnh được độ nhấn, nên nếu cần +2 dB như delivery file thì phải làm ở hậu kỳ. Mình chưa làm bước đó để so sánh thô cho công bằng.

Kiểm tra G2P (`vig2p`, chưa load model) ra phoneme hợp lý cho cả 3 câu. Thanh điệu được mã bằng mũi tên ↗↘↓, «tr»→ʈʂ, «s»→ʂ. Xem `lines.json`.

## Cài đặt (đã xong)
- venv Python 3.12.15 tại `/workspace/kokoro-vn/venv` (dùng uv, chạy nice 15). Các gói: torch 2.14.1+cpu, onnxruntime 1.31.0, transformers 4.57.6, vig2p 0.1.2, kokoro-vietnamese 0.1.0 (editable), pyloudnorm 0.2.0. Không đụng vào `f5-venv`, `tts-venv` hay `asr-venv`.
- Code: `/workspace/kokoro-vn/src`, bản clone `github.com/iamdinhthuan/Kokoro-Vietnamese` commit `a249afe` (2026-06-27).
- Weights: `/workspace/kokoro-vn/hf`, lấy `huggingface.co/contextboxai/Kokoro-Vietnamese` ở revision `9f210d6`. Gồm `kokoro_vi.onnx` 311 MB, `kokoro_vi.pth` 313 MB, 14 voicepack.
- Không cần espeak-ng vì G2P tiếng Việt dùng `vig2p`.

## Script sẵn để chạy (khi News báo F5 xong)
1. `/workspace/kokoro-vn/venv/bin/python synth_kokoro.py`: dùng ONNX trên CPU với 8 thread, chuẩn −14 LUFS và peak ≤ −0,5 dBFS. Ghi `kokoro/<id>-kokoro-<voice>.wav` và `kokoro/synth-log.json` (thời gian synth, RTF, LUFS). **Script tự từ chối chạy nếu thấy có tiến trình F5.**
2. `/workspace/asr-venv/bin/python stt_score.py kokoro/*.wav`: tính STT bằng đúng các hàm `stt/norm/sim` của `pipeline/scripts/voice-delivery-f5.py` (faster-whisper small int8), ngưỡng ≥ 0,8, đồng thời dò các chỗ lặng ≥ 0,25s không nằm ở dấu câu (R4). Bước này cũng load model nên phải chạy sau khi F5 xong.
3. `/workspace/kokoro-vn/venv/bin/python prep_blind.py --voice <pack> --f5 c07=<take F5 News chọn>,c08=…,c14=…`: chuẩn cả hai bản về −14 LUFS 48k, đặt tên mù `blind/<id>-X|Y.wav`, đáp án để riêng ở `blind-key.json`. Sau đó chạy `stt_score.py blind/*.wav`.

## Voicepack (chốt trước khi nghe, xem `lines.json`)
Ứng viên nam đoán theo tên, giới tính chưa xác minh bằng tai: manh_dung, hung_thinh, tuan_ngoc, duc_an, duc_duy, thanh_dat, phat_tai. Luật chọn: (1) loại pack nghe ra giọng nữ hoặc có câu STT < 0,8; (2) lấy pack có STT trung bình cao nhất; (3) nếu hoà trong khoảng ±0,02 thì chọn pack có F0 gần Thái Sơn nhất; (4) nghe tai chỉ dùng để loại lỗi dấu, âm cuối, lặng giữa cụm. Kokoro chạy deterministic, không có seed, nên mỗi voicepack chỉ có một take.

## License (kiểm tại nguồn ngày 2026-10-20)
- **Code** (`iamdinhthuan/Kokoro-Vietnamese`): file `LICENSE` là Apache-2.0, `pyproject.toml` cũng ghi Apache-2.0.
- **Weights và voicepack** (`contextboxai/Kokoro-Vietnamese`): model card gắn tag `license: apache-2.0`, nhưng không có file LICENSE riêng và không ghi nguồn dữ liệu. Phần nền là Kokoro-82M của hexgrad, cũng Apache-2.0.
- **Dữ liệu train: CHƯA RÕ, có rủi ro.** Trong repo, config `config_vietnamese_larvoice_multispeaker_stage{1,2}.yml` và `scripts/modal_vietnamese_larvoice_train.py` dùng tarball `dataset_voxcpm_larvoice.tar`. Bản mirror `anphunl/Kokoro-Vietnamese` ghi «voicepacks are derived from the LarVoice multi-speaker training set». LarVoice (larvoice.com) là dịch vụ TTS và voice cloning **thương mại**. Mình không tìm được dataset LarVoice nào công khai kèm license. Điều khoản của LarVoice (docs.larvoice.com/tai-khoan/dieu-khoan-su-dung, cập nhật 16/07/2025) chỉ nói về việc dùng dịch vụ: cấm resale, cấm giả mạo, và muốn dùng thương mại mở rộng phải xin quyền riêng. Không có điều khoản nào cho phép lấy output để train rồi phân phối model. Tên file gợi ý dữ liệu có thể là audio tổng hợp (VoxCPM/LarVoice), nhưng đây chỉ là suy luận, chưa xác minh. Kết luận: **thẻ Apache-2.0 trên weights chưa chứng minh được quyền dùng thương mại.** Theo workflow mục 6, cổng license hiện chưa đạt, nên chỉ được nghe nội bộ, không được khuyến nghị dùng cho clip đăng.

## Kết quả STT / RTF / nhận xét
Chưa có, vì chưa synth. Mình sẽ điền số đo thật sau khi chạy. Không ghi số ước đoán.
