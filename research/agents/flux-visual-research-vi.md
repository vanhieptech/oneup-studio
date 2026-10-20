# Nghiên cứu FLUX.2 — FLUX Visual

- Repo nguồn: https://github.com/black-forest-labs/flux2 (Black Forest Labs)
- Ngày kiểm tra: 2026-10-19 (Asia/Saigon)
- Phạm vi: giấy phép, phần cứng, độ phù hợp cho thumbnail/bài đăng/minh họa của @hi.oneup
- Trạng thái: **chưa tải weights, chưa gọi API, chưa tạo ảnh nào.**

## 1. Giấy phép: code ≠ weights

- Code repo `flux2`: Apache 2.0 (`LICENSE.md` ở gốc repo) — tự do dùng/sửa/phân phối code suy luận.
- Weights nằm riêng ở `model_licenses/` và model card Hugging Face, không đi theo Apache của code. Autoencoder FLUX.2 cũng Apache 2.0 nhưng không đổi được giấy phép weights chính.

| Biến thể | Weights mở | Giấy phép weights | Thương mại cho @hi.oneup |
|---|---|---|---|
| FLUX.2 [klein] 4B (distilled) | Có | Apache 2.0 | Được, không cần xin phép/trả phí |
| FLUX.2 [klein] 4B Base | Có | Apache 2.0 | Được (hợp fine-tune/LoRA) |
| FLUX.2 [klein] 9B / 9B KV / 9B Base | Có (gated) | FLUX Non-Commercial | Không tự chạy local cho kênh thương mại — mua license self-host của BFL hoặc gọi API |
| FLUX.2 [dev] 32B | Có (gated) | FLUX Non-Commercial (`LICENSE-FLUX-DEV` v2.0) | Không cho mục đích thương mại/production khi tự chạy |
| FLUX.2 [pro] / [flex] / [max] | Không — API-only | Qua API BFL | Được — quyền thương mại gồm trong giá API |

Lưu ý lách luật dễ mắc: `LICENSE-FLUX-DEV` §2(d) cho phép dùng *Output* cho mọi mục đích kể cả thương mại (trừ train model cạnh tranh), nhưng §2(b)/§4(a) và trang trợ giúp của BFL giới hạn việc *chạy model* ở Non-Commercial Purpose; revenue-generating/production phải mua license. Không dựa vào khe §2(d) để tự chạy dev/9B cho kênh.

Nguồn: README + `LICENSE.md` + `model_licenses/LICENSE-FLUX-DEV` của repo; https://bfl.ai/models/flux-2-klein; https://help.bfl.ai/articles/9272590838 (licensing); https://help.bfl.ai/articles/4375863104 (API commercial); https://help.bfl.ai/articles/7108141705 (klein local); https://help.bfl.ai/articles/7986977817 (bảng giá API).

## 2. Phần cứng: yêu cầu vs box thật

Số chính thức: klein 4B — BFL ghi 8,4 GB VRAM, model card HF ghi ~13 GB VRAM (RTX 3090/4070+), README ghi "fits in ~8GB" → hiểu 8,4–13 GB tùy cách đo/offload. klein 9B: 19,6 GB; 9B Base: 21,7 GB (train 9B ~22 GB VRAM + 64 GB RAM; train 4B 12 GB VRAM + 32 GB RAM). 9B KV: chưa tìm thấy số VRAM chính thức — không đoán. [dev] 32B: bản gốc cần mức H100/80 GB+; bản 4-bit qua diffusers chạy RTX 4090 ở ~18–20 GB.

| Hạng mục | Yêu cầu klein 4B | Box đo 2026-10-19 | Đạt |
|---|---|---|---|
| GPU NVIDIA | RTX 3090/4070+, 8,4–13 GB VRAM | Không có GPU (`nvidia-smi` không có, không `/dev/nvidia*`) | Không |
| RAM | 32 GB (số công bố cho train) | 15 GiB tổng, ~8,1 GiB trống | Không |
| CPU | — | 8 vCPU Xeon (KVM) | Không thay được GPU |
| Đĩa | — | 125 GB, trống 104 GB | Đủ chứa weights |

Kết luận: box hiện không chạy local được bất kỳ biến thể FLUX.2 nào ở chế độ được hỗ trợ.

## 3. Độ phù hợp với @hi.oneup

- Klein 4B hỗ trợ text-to-image + sửa ảnh 1–nhiều ảnh tham chiếu trong cùng một model — đúng use-case lấy sheet nhân vật làm reference sinh biến thể. Độ nhất quán nét chibi ink phải test thật mới khẳng định, chưa có cơ sở hứa trước.
- Assets sẵn có (đúng nguồn duy nhất, rule-65): `brand/characters/` — `hiep-model-sheet.png` (2400×1500), `hiep-poses.png` (2400×1100), `omi-sheet.png` (2400×1420), bản `v2/` dọc 1080×1920; `brand/omi-exports/` — 242 file PNG/SVG pose/biểu cảm Omi. Hình thật nằm ở `brand/`, không phải `assets/` (chỉ có sfx + voice-refs).
- Ràng buộc kênh thắng FLUX: ảnh AI không vào final video (luật 42/43), cover final từ `Cover.tsx` (L-020/rule-54), nghĩa bằng vật/hành động không chữ (L-050), không mặt người giả chưa duyệt, Omi chỉ từ tuần ≥5 (rule-11). FLUX chỉ ở vai trò ý tưởng/tham chiếu hoặc hình bài đăng được Hiệp duyệt riêng — chi tiết ở `workflows/agents/flux-visual.md`.

## 4. Khuyến nghị và điều cần Hiệp duyệt

Phương án chính: **FLUX.2 [klein] 4B qua API chính thức của BFL** cho vòng test đầu (tham khảo từ $0,014/ảnh) — biến thể duy nhất Apache 2.0 cả khi self-host sau này, chạy được ngay khi box không có GPU.

Cần Hiệp duyệt trước:
1. Nạp credits BFL API + tạo API key (chi phí thật).
2. Upload sheet Hiệp/Omi lên API: theo FLUX API Service Terms §2(b), BFL được dùng Input/Output để vận hành, cải thiện và train model của họ. Không chấp nhận → bỏ API, chờ self-host klein 4B trên GPU RTX 3090/4070+ (duyệt thêm khoản thuê/máy GPU).
3. Xác nhận khung thương mại của @hi.oneup (báo cáo này đã tính theo trường hợp thương mại — an toàn nhất).
