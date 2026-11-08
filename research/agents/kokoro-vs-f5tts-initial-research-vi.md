---
title: "Nghiên cứu: Kokoro so với F5-TTS (bản đầu)"
date: 2026-10-19
source: "agent research 19/10/2026 (goc o /workspace, da gom vao repo)"
id: research.kokoro-vs-f5tts
type: research
status: reference
updated: 2026-10-19
tags: [tts, kokoro, f5-tts, voice]
---
# Kokoro vs F5-TTS — Nghiên cứu ban đầu cho pipeline giọng @hi.oneup

- **Ngày kiểm tra:** 2026-10-19 (Asia/Saigon)
- **Phạm vi:** Nghiên cứu ban đầu, *chưa* tạo audio, *chưa* clone giọng, *chưa* tải model, *chưa* cài đặt nặng. Chỉ inventory nhẹ trên box + đọc nguồn chính thức/cộng đồng qua web.
- **Bối cảnh đã chốt:** Chỉ làm giọng sau khi Hiệp chốt script. Pipeline hiện tại: Hiệp chibi = F5-TTS từ reference "Thái Sơn", Omi = F5-TTS từ reference "Mỹ Duyên" (xem mục 5 về điểm tích hợp thực tế trên box).

---

## 0. Kết luận nhanh (TL;DR)

1. **Kokoro chính thức (hexgrad/Kokoro-82M) KHÔNG hỗ trợ tiếng Việt thật.** Không có voice tiếng Việt, không có `lang_code` tiếng Việt trong `KPipeline`, và maintainer đã trả lời thẳng trong issue xin tiếng Việt là *chưa có dữ liệu tiếng Việt đủ tốt để train*. Đây là kết luận chắc chắn nhất của báo cáo này, có nguồn trực tiếp bên dưới.
2. **Cái "có vẻ như tiếng Việt" gồm 3 thứ khác nhau, đừng trộn lẫn:**
   - (a) `misaki` (thư viện G2P đi kèm Kokoro) *có* file `vi.py` thử nghiệm dựa trên Viphoneme — tức là có mã chuyển chữ→phiên âm, nhưng **không được nối vào `KPipeline`** (`LANG_CODES` không có tiếng Việt) và **không có voice/model đã train bằng phiên âm đó**. Có G2P ≠ đọc được tiếng Việt hay.
   - (b) Ép Kokoro tiếng Anh/tiếng khác đọc text tiếng Việt qua espeak-ng fallback: về kỹ thuật có thể thử hack, nhưng không có bằng chứng chất lượng, gần như chắc chắn sai dấu/âm cuối. Không coi là "hỗ trợ".
   - (c) **Bản fine-tune cộng đồng `contextboxai/Kokoro-Vietnamese`** (2026, ngoài hexgrad): có 14 voicepack tiếng Việt, có ONNX, ghi license Apache-2.0 trên model card. Đây là ứng viên *duy nhất* đáng đưa vào vòng thử — nhưng **không phải Kokoro chính thức**, chưa có benchmark độc lập, và nguồn gốc dữ liệu train (LarVoice) chưa kiểm chứng được license/quyền giọng nói ở mức đủ an toàn cho thương mại.
3. **Nếu chỉ xét Kokoro chính thức: không đáng thử cho video tiếng Việt, và không thay được F5-TTS hiện tại** vì hai lý do độc lập, mỗi lý do đã đủ để loại: (i) không có tiếng Việt; (ii) **không có voice cloning / reference audio** — Kokoro chỉ có voice preset dạng style-vector đóng gói sẵn, "decoder only: no encoder release", nên không thể tạo giọng Hiệp/Omi từ `thai-son.wav` / `my-duyen.wav` như F5 đang làm.
4. **Điểm Kokoro thắng F5 thật sự là license + tốc độ/nhẹ:** weights chính thức Apache-2.0 (dùng thương mại được, kể cả TikTok monetization, nếu chỉ dùng weights/voice chính thức), 82M tham số, chạy nhanh hơn thời gian thực trên CPU, không cần GPU. Nhưng lợi thế license này **không tự động áp cho bản Kokoro-Vietnamese cộng đồng** cho tới khi rõ dữ liệu train.
5. **Khuyến nghị:** Giữ nguyên pipeline F5 cho sản xuất. Khi Hiệp chốt script, chỉ chạy **một vòng A/B mù tối thiểu** (mục 6) giữa F5 hiện tại và *Kokoro-Vietnamese cộng đồng* (không phải Kokoro gốc) trên đúng 1 đoạn ngắn, với điều kiện pass/fail định trước. Nếu Kokoro-VI thua ở bất kỳ tiêu chí "cổng" nào (sai dấu/âm cuối nghe rõ, không giữ được hai nhân vật phân biệt, license không rõ) → **không đổi pipeline**, ghi log và dừng.

---

## 1. Kokoro chính thức — sự thật từ repo/model card

### 1.1 Model, kiến trúc, kích thước

| Mục | Giá trị | Nguồn |
|---|---|---|
| Tên | Kokoro-82M, inference library `kokoro` (pip) | GitHub README: "An inference library for Kokoro-82M. You can `pip install kokoro`" — https://github.com/hexgrad/kokoro |
| Tham số | 82 triệu | HF model card: "open-weight TTS model with 82 million parameters" — https://huggingface.co/hexgrad/Kokoro-82M |
| Kiến trúc | StyleTTS 2 + ISTFTNet; **decoder-only, không phát hành encoder** | HF: "Architecture: StyleTTS 2 … ISTFTNet … Decoder only: no diffusion, no encoder release" — cùng link trên. Hệ quả trực tiếp: không có đường zero-shot cloning từ audio tham chiếu như F5/XTTS. |
| Sample rate ra | 24 kHz | Ví dụ chính thức `sf.write(..., 24000)` trong README GitHub/HF |
| Version model mới nhất được liệt kê | **v1.0, 2025-01-27**, "Few hundred hrs", 8 ngôn ngữ & 54 voices (bảng Releases trên HF; VOICES.md đếm 9 nhóm ngôn ngữ nếu tách Anh-Anh/Anh-Mỹ — xem 1.3) | https://huggingface.co/hexgrad/Kokoro-82M (bảng Releases) |
| Version package pip mới nhất tại ngày kiểm tra | `kokoro 0.9.4` | PyPI JSON: https://pypi.org/pypi/kokoro/json (`info.version = 0.9.4`) và `pyproject.toml` trên GitHub ghi `version = "0.9.4"` |
| Kích thước file (đường ONNX cộng đồng cho bản gốc) | `kokoro-v1.0.onnx` ≈ 326 MB (fp32), fp16 ≈ 164 MB, int8 ≈ 114 MB; voices ≈ 28 MB | Releases `thewh1teagle/kokoro-onnx`: https://github.com/thewh1teagle/kokoro-onnx/releases — đây là export cộng đồng, không phải artifact chính thức của hexgrad. |

### 1.2 Giấy phép — tách 3 lớp

| Lớp | License | Nguồn | Dùng thương mại? |
|---|---|---|---|
| **Code** (`hexgrad/kokoro`) | Apache-2.0 | File `LICENSE` ở root repo (Apache License Version 2.0) + `pyproject.toml`: `License :: OSI Approved :: Apache Software License` — https://github.com/hexgrad/kokoro/blob/main/LICENSE | Có |
| **Weights Kokoro-82M v1.0** | Apache-2.0 | HF model card header `license: apache-2.0`; thân bài: "With Apache-licensed weights, Kokoro can be deployed anywhere…" và "This is an Apache-licensed model, and Kokoro has been deployed in numerous projects and commercial APIs." — https://huggingface.co/hexgrad/Kokoro-82M | **Có**, theo tuyên bố của tác giả. Lưu ý dữ liệu train có thành phần CC BY (Koniwa, SIWIS — bảng "Creative Commons Attribution" trên model card) cần giữ attribution nếu áp dụng; đây là nghĩa vụ ghi công, không phải cấm thương mại. |
| **Từng voice chính thức** | Đi cùng weights Apache-2.0; mỗi voice là 1 file `.pt` style-vector trong repo HF (`voices/<name>.pt`), chất lượng được chấm grade A→F trong VOICES.md theo chất lượng/dung lượng dữ liệu train của chính voice đó | https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md | Theo cùng license weights. **Chưa chắc chắn:** VOICES.md không cấp license riêng từng voice và không nói rõ danh tính/quyền nhân thân của người góp giọng gốc; nếu dùng voice preset nguyên bản cho thương hiệu lâu dài vẫn nên tự nghe + tự chịu rủi ro nhận diện giọng thật. |

> **Điều chưa chắc chắn (license):** Báo cáo này đọc license ở cấp repo/model card. Nó không phải tư vấn pháp lý. Điểm cần kiểm tra lại trước khi thương mại hoá bằng *bản cộng đồng tiếng Việt* nằm ở mục 2.3.

### 1.3 Ngôn ngữ hỗ trợ chính thức — không có tiếng Việt

Bằng chứng theo 3 lớp độc lập, cùng chỉ một hướng:

1. **Danh sách voice chính thức (VOICES.md)** chỉ có 9 nhóm: American English (11F/9M), British English (4F/4M), Japanese (4F/1M), Mandarin Chinese (4F/4M), Spanish (1F/2M), French (1F), Hindi (2F/2M), Italian (1F/1M), Brazilian Portuguese (1F/2M) — tổng 54 voices. **Không có Vietnamese.** Nguồn: https://huggingface.co/hexgrad/Kokoro-82M/raw/main/VOICES.md
2. **Code `KPipeline`** (`kokoro/pipeline.py` trên `main`): `LANG_CODES = {a, b, e, f, h, i, p, j, z}` và `ALIASES` chỉ map en/es/fr/hi/it/pt-br/ja/zh. Gọi `KPipeline(lang_code='vi')` sẽ `assert lang_code in LANG_CODES` và fail. Các ngôn ngữ ngoài Anh/Nhật/Trung đều rơi vào `EspeakG2P` fallback với cảnh báo *"Chunking logic not yet implemented"*. Nguồn: https://github.com/hexgrad/kokoro/blob/main/kokoro/pipeline.py
3. **Maintainer trả lời trực tiếp (issue #153, "Request for Vietnamese Language Support", mở 2025-03-28, vẫn open, cập nhật tới 2025-09-10):**
   - hexgrad, 2025-03-28: *"I currently do not have any Vietnamese data yet, nor any means of procuring it"* và từ chối Common Voice vì cho là dữ liệu "impure" làm giảm chất lượng.
   - Khi được gợi ý dataset `capleaf/viVoice` (CC-BY-NC-SA): *"viVoice is `cc-by-nc-sa`; license should be cc-by or more permissive for me to train on it."*
   - Nguồn: https://github.com/hexgrad/kokoro/issues/153
   - **Hệ quả thú vị cho @hi.oneup:** chính dataset họ ViVoice là họ dữ liệu đứng sau checkpoint F5 tiếng Việt đang dùng local (mục 5) — tức là rào cản license mà hexgrad né, Hiệp đã *chủ động chấp nhận* ở pipeline F5 (DL-035).

**Về `misaki[vi]`:** Repo misaki có `misaki/vi.py` (dựa trên Viphoneme, https://github.com/v-nhandt21/Viphoneme; README misaki mục "Vietnamese" chỉ link tới đó) và `vi_cleaner`. Nhưng: (i) `KPipeline` không import/không expose nó; (ii) không có voice nào được train để "hiểu" hệ phiên âm đó trong Kokoro-82M v1.0; (iii) không có tài liệu chính thức nào hướng dẫn chạy tiếng Việt. **Đánh giá: đây là mã G2P thử nghiệm nằm sẵn trong thư viện phụ trợ, không phải tính năng tiếng Việt của Kokoro.** Ai nói "Kokoro hỗ trợ tiếng Việt vì misaki có vi.py" là đang nhầm lớp G2P với lớp model+voice.

**Mức chất lượng bằng chứng sẵn có cho tiếng Việt chính thức:** *Không có.* Không sample, không MOS, không benchmark, không voice. Với các ngôn ngữ chính thức, bằng chứng chất lượng là: samples trên HF (SAMPLES.md), grade từng voice trong VOICES.md, và việc model từng đứng cao trên TTS Arena — tất cả đều **không bao gồm tiếng Việt**, không suy diễn sang tiếng Việt được (tiếng Việt có 6 thanh điệu + âm cuối -c/-t/-p/-m/-n/-ng/-nh và nguyên âm ă/â/ơ/ư/ô/ê rất khác hệ phiên âm Anh/Nhật/Trung đã train).

---

## 2. Đường tiếng Việt duy nhất có thật: bản cộng đồng Kokoro-Vietnamese

### 2.1 Nó là gì

| Mục | Giá trị | Nguồn |
|---|---|---|
| Repo code | `iamdinhthuan/Kokoro-Vietnamese` (tạo 2026-06-19 theo metadata tìm kiếm; ~120 stars tại ngày kiểm tra — số này biến động) | https://github.com/iamdinhthuan/Kokoro-Vietnamese |
| Weights | `contextboxai/Kokoro-Vietnamese` trên HF: `kokoro_vi.pth` ≈ 327 MB, `kokoro_vi.onnx` ≈ 326 MB, `config.json`, `voices.json`, 14 file `voicepacks/*.pt` | https://huggingface.co/contextboxai/Kokoro-Vietnamese/tree/main |
| G2P tiếng Việt | `vig2p` (khác `misaki/vi.py` ở trên — đây là G2P riêng của bản fine-tune) | Model card + README repo |
| Voices (14) | Nữ/giọng kể: `diem_trinh` (mặc định), `mai_linh`, `mai_loan`, `my_yen`, `ngoc_huyen`, `thuc_trinh`; Nam: `hung_thinh`, `manh_dung`, `phat_tai`, `thanh_dat`, `tuan_ngoc`, `duc_an`, `duc_duy`; + `storyvert` | Bảng Voices trong README/model card |
| Cách chạy | PyTorch: `kokoro-vietnamese --text … --voice diem_trinh --device cuda/cpu`; ONNX: `pip install -e ".[onnx]"` rồi `kokoro-vietnamese-onnx … --device cpu` (tự tải file từ HF khi không chỉ đường local) | README repo |
| Thông tin train công bố | Fine-tune từ Kokoro, dữ liệu **LarVoice multi-speaker**, stage-2 checkpoint `epoch_2nd_00006.pth`, validation loss 0.2935, voicepack trích 200 samples/voice, 24 kHz | Model card: https://huggingface.co/contextboxai/Kokoro-Vietnamese |

### 2.2 Cái chưa có (quan trọng hơn cái đã có)

- **Không benchmark độc lập:** Không MOS/UTMOS, không WER/CER bằng ASR, không A/B công khai, không sample gallery được kiểm chứng ngoài repo tự công bố. Con số duy nhất là validation loss nội bộ (0.2935) — không dịch sang "nghe hay/dở" được.
- **Không rõ miền giọng:** Model card không ghi Bắc/Trung/Nam cho từng voice. @hi.oneup cần **Nam miền Nam** cho cả hai nhân vật (voice-profile.md) — phải nghe thử mới biết, không đọc spec mà kết luận được.
- **Không cloning:** 14 voicepack là preset cố định. Muốn "giọng Hiệp" từ `thai-son.wav` thì không có đường zero-shot; trích voicepack mới cần quy trình train stage-1 như họ đã làm với LarVoice — ngoài phạm vi "thử nhanh".
- **Độ mới/rủi ro bảo trì:** Repo rất mới (2026), ít issue, một nhóm tác giả. Có thể dừng bất cứ lúc nào; đổi lại artifact đã tải về thì chạy offline được.

### 2.3 License của bản cộng đồng — cờ vàng

- Model card HF ghi `license: apache-2.0` và repo GitHub có file LICENSE Apache-2.0. **Nhưng** weights được fine-tune trên **LarVoice** — tại thời điểm kiểm tra, tôi **không truy cập/xác minh được license gốc của LarVoice và quyền sử dụng giọng của từng speaker trong đó** (API HF trả lỗi khi truy vấn dataset theo đường dẫn đoán; model card Kokoro-Vietnamese cũng không trích license của LarVoice).
- Vì vậy: *"Apache-2.0" trên model card là tuyên bố của người fine-tune, chưa phải bằng chứng chuỗi quyền (chain of rights) sạch.* Trước khi dùng cho TikTok monetization, cần tối thiểu: (1) tìm được trang gốc LarVoice + license; (2) xác nhận license đó cho phép fine-tune + phân phối voicepack + dùng thương mại; (3) lưu lại bằng chứng đó cạnh file này. **Chưa làm được 3 việc này thì rủi ro license của Kokoro-VI chưa chắc đã thấp hơn F5 hiện tại** — F5 ít nhất đã được Hiệp ý thức và chấp nhận rủi ro bằng văn bản (DL-035), còn Kokoro-VI hiện là rủi ro *chưa được định giá*.

---

## 3. Yêu cầu chạy cục bộ + đối chiếu máy box hiện tại

### 3.1 Kokoro chính thức cần gì

| Mục | Yêu cầu / đặc tính | Nguồn / ghi chú |
|---|---|---|
| Cài đặt | `pip install kokoro>=0.9.4 soundfile` + hệ thống `espeak-ng` (cho fallback Anh & một số ngôn ngữ) | README GitHub, mục Usage/Advanced |
| Python | PyPI `kokoro 0.9.4`: `requires_python >=3.10, <3.13`. **Lưu ý mâu thuẫn nguồn:** `pyproject.toml` trên GitHub `main` ghi `>=3.10, <3.14`. Lấy PyPI làm chuẩn khi cài thật vì pip sẽ enforce theo PyPI. | https://pypi.org/pypi/kokoro/json ; https://github.com/hexgrad/kokoro/blob/main/pyproject.toml |
| Phụ thuộc chính | `torch`, `transformers`, `misaki[en]>=0.9.4`, `numpy`, `huggingface_hub`, `loguru` | `pyproject.toml` |
| GPU | **Không bắt buộc.** CPU chạy nhanh hơn thời gian thực trong các benchmark độc lập (mục 3.2). GPU chỉ giảm thêm. macOS Apple Silicon: `PYTORCH_ENABLE_MPS_FALLBACK=1` để dùng MPS. Windows: cài espeak-ng bằng `.msi` riêng. | README GitHub mục macOS/Windows |
| VRAM/RAM ước tính | Model 82M → weights fp32 ≈ 330 MB, fp16 ≈ 165 MB. RAM/VRAM làm việc thực tế thường ~1–3 GB cho single-stream (ước tính từ kích thước model + các hướng dẫn triển khai; **không phải con số chính thức từ hexgrad** — đánh dấu là ước tính). | Suy ra từ kích thước ONNX ở mục 1.1 + benchmark bên dưới |
| ONNX | Có, do cộng đồng: `onnx-community/Kokoro-82M-v1.0-ONNX`, `thewh1teagle/kokoro-onnx` (fp32/fp16/int8). Chạy bằng onnxruntime CPU, bỏ được torch. Bản Kokoro-VI cũng tự export ONNX được. | Mục 1.1, 2.1 |
| Tốc độ (bằng chứng ngoài) | Benchmark gist (PyTorch/ONNX, CPU/GPU): CPU x86 lớn (c6a.8xlarge) ≈ **5× thời gian thực**; GPU tới 36–96× tuỳ instance. Benchmark CPU 4-core độc lập khác: RTF ≈ 0.64–0.67 (≈1.5× thời gian thực), UTMOS ≈ 4.44–4.46 cho tiếng Anh. **Tất cả là tiếng Anh, máy khác — chỉ để ước lượng bậc độ lớn, không phải cam kết trên box này.** | https://gist.github.com/efemaer/23d9a3b949b751dde315192b4dcf0653 ; https://heyneo.com/blog/kokoro-supertonic-inflect-nano-pocket-tts-cpu-benchmark |

### 3.2 Inventory box Linux hiện tại (đo 2026-10-19, chỉ lệnh nhẹ)

| Mục | Thực tế trên box | Hệ quả |
|---|---|---|
| OS/CPU | Linux x86_64, kernel 6.12, **8 core** | Đủ chạy Kokoro CPU và đang chạy F5 CPU. |
| GPU | **Không có**: `nvidia-smi: command not found` | Mọi thử nghiệm phải giả định CPU-only. Không sao với Kokoro; F5 hiện tại cũng đang `device="cpu"` (xem mục 5). |
| RAM | 15 GiB total (~8.5 GiB available lúc đo), swap 0 | Đủ cho Kokoro (~1–3 GB ước tính) và F5 hiện tại. |
| Disk | 125 G total, **104 G trống** (18% used) | Đủ chỗ cho cả model Kokoro (~0.3–0.7 GB) lẫn F5 checkpoint sẵn có (5.1 GB). |
| Python hệ thống | **Python 3.13.5**, pip 25.1.1 | **Xung đột cần lưu ý:** PyPI `kokoro 0.9.4` đòi `<3.13` → `pip install kokoro` trên Python 3.13.5 nhiều khả năng bị pip chặn. Cần tạo venv Python 3.10–3.12 riêng (hoặc dùng đường ONNX của Kokoro-VI để né torch/kokoro gốc). Đây là ma sát cài đặt thật, không phải lý thuyết. Các venv sẵn có (`f5-venv`, `tts-venv`) đều đang ở Python 3.13.5. |
| espeak-ng | **Chưa cài** (`which espeak-ng` rỗng) | Cần `apt install espeak-ng` nếu thử đường Kokoro gốc/fallback. Bản Kokoro-VI dùng `vig2p` nên có thể không cần — phải kiểm tra khi thử thật. |
| torch/kokoro hệ thống | Chưa có trong pip hệ thống | Đúng kỳ vọng; mọi thứ đang nằm trong venv riêng theo engine. Giữ nguyên pattern đó nếu thử. |

**Trả lời thẳng câu "chạy trên box này được không":** Được về phần cứng (CPU/RAM/disk dư dả, và box đã chứng minh chạy F5 CPU cho sản xuất). Trở ngại duy nhất đã thấy trước là **Python 3.13 vs `kokoro<3.13`** và **chưa có espeak-ng** — cả hai giải quyết được bằng venv Python 3.12 riêng + apt, thuộc loại việc "làm khi có script chốt", không làm bây giờ.

---

## 4. So sánh thẳng: F5-TTS hiện tại vs Kokoro cho video ngắn tiếng Việt 2 nhân vật

Pipeline F5 "hiện tại" ở bảng này là cấu hình *thực tế trên box* (không phải F5 upstream chung chung): checkpoint `hynt/F5-TTS-Vietnamese-ViVoice` (theo docstring trong `pipeline/tts/f5tts_gen.py`: CC-BY-NC-SA-4.0, non-commercial, Hiệp đã chấp nhận — DL-035), reference là câu trung tính tổng hợp từ preset VieNeu (Thái Sơn / Mỹ Duyên), chạy CPU, bọc ngoài bởi `voice-prosody.py` (chia phrase, nghỉ theo dấu câu, chọn take bằng ASR/F0, mastering −16 LUFS…).

| Tiêu chí | F5-TTS hiện tại (@hi.oneup) | Kokoro chính thức (hexgrad) | Kokoro-Vietnamese cộng đồng |
|---|---|---|---|
| **Tiếng Việt** | Đã train riêng cho tiếng Việt (họ ViVoice), đang dùng thật cho clip đã xuất bản | **Không có** (mục 1.3) | Có, fine-tune riêng; chất lượng *chưa được kiểm chứng độc lập* |
| **Voice cloning / reference audio** | **Có — đây là lý do nó được chọn.** Zero-shot từ `thai-son.wav`/`my-duyen.wav` + ref_text; đổi ref là đổi giọng | **Không.** Chỉ preset style-vector; không encoder | **Không** zero-shot. Chỉ 14 preset; muốn giọng mới phải train |
| **Hai nhân vật phân biệt (nam Hiệp / nữ Omi)** | Có sẵn: 2 ref khác nhau, giữ qua mọi clip | Không áp dụng (không tiếng Việt, không clone) | Có thể map tạm: 1 nam preset ↔ Hiệp, 1 nữ preset ↔ Omi — nhưng đó là **đổi giọng nhân vật**, không phải giữ giọng hiện tại. Khán giả cũ sẽ nghe khác hẳn. Phải được Hiệp duyệt như một quyết định brand, không phải quyết định kỹ thuật. |
| **Cảm xúc / diễn xuất** | Kế thừa cảm xúc từ reference + punctuation/phrase markup rất sâu đã xây (luật 46: `{nhỏ:…}`, `{kéo: nha}`, từ đệm, nghỉ ms theo dấu) + chọn take theo F0 | Chỉ có `speed`; không emotion control, không markup tương đương | Tương tự Kokoro gốc: `speed`, chia câu + crossfade. Toàn bộ lớp markup/nghỉ/chọn take hiện tại phải làm lại hoặc bỏ |
| **Độ tự nhiên tiếng Việt (dấu, âm cuối)** | Đã được nghe duyệt qua nhiều clip thật (c03/c04…); rủi ro đã biết: phải viết số thành chữ, phiên âm từ Anh (TOEIC→"tô ích"), hạ chữ thường theo checkpoint | Không có dữ liệu để nói — không có tiếng Việt | **Chưa biết.** Rủi ro cụ thể cần nghe: thanh điệu (ngang/huyền/sắc/hỏi/ngã/nặng), âm cuối -c/-t/-p, cặp ă/â, ơ/ư, giọng Nam vs Bắc, từ đệm nha/á/hông/nè, chen tiếng Anh kiểu voice-profile. Validation loss không trả lời được câu nào trong số này. |
| **Tốc độ suy luận** | CPU, NFE=32, mỗi phrase nhiều take (3 take/phrase theo seed/speed grid) rồi chọn — chậm theo thiết kế để lấy chất lượng; đổi lại cache theo hash nội dung | Rất nhanh: ~1.5–5× thời gian thực trên CPU trong benchmark tiếng Anh | Kỳ vọng cùng bậc Kokoro gốc (cùng kiến trúc 82M + có ONNX CPU), nhưng **chưa đo trên box, chưa đo tiếng Việt** |
| **License thương mại (TikTok monetization)** | **Không sạch:** code F5 upstream MIT, nhưng weights upstream CC-BY-NC-4.0 (train trên Emilia) và checkpoint tiếng Việt đang dùng ghi CC-BY-NC-SA-4.0 — cả hai đều **non-commercial**. Hiệp đã *chấp nhận rủi ro* này (DL-035), tức là đang dùng với rủi ro đã biết, không phải "được phép". Nguồn upstream: https://github.com/SWivid/F5-TTS/blob/main/LICENSE (MIT cho code) + https://huggingface.co/SWivid/F5-TTS (model card `license: cc-by-nc-4.0`) + docstring local ở mục 5 | **Sạch nhất trong 3 cột:** Apache-2.0 cả code lẫn weights → dùng thương mại được (kèm attribution cho phần CC BY trong dữ liệu train nếu áp dụng) | **Chưa rõ:** card ghi Apache-2.0 nhưng chuỗi quyền LarVoice chưa xác minh (mục 2.3). Chưa kết luận "sạch hơn F5" được. |
| **Rủi ro chính** | License NC (đã chấp nhận); reference leakage (đã có cơ chế trim bằng ASR); tốc độ render | Dùng sai chỗ: không tiếng Việt + không clone → không thay thế được, dù license đẹp | License dữ liệu chưa rõ; chất lượng dấu/âm cuối chưa chứng minh; repo mới, bảo trì mong manh; đổi giọng nhân vật = rủi ro brand |
| **Trưởng thành / bằng chứng** | Đang chạy sản xuất thật trên box | Rất trưởng thành *cho các ngôn ngữ của nó* (54 voices, grades, samples, nhiều API thương mại dùng) | Non trẻ: 1 bản fine-tune, không benchmark ngoài |

**Đọc bảng trên trong 10 giây:** Kokoro gốc thắng F5 ở license + tốc độ nhưng *thua tuyệt đối* ở hai tiêu chí cổng của use case này (tiếng Việt + cloning). Kokoro-VI cộng đồng gỡ được tiêu chí tiếng Việt *trên danh nghĩa*, vẫn thua ở cloning, và chưa chứng minh được chất lượng lẫn license. Vì vậy Kokoro — ở cả hai dạng — **không phải "bản nâng cấp" của pipeline hiện tại; nó là một hướng khác với đánh đổi khác.**

---

## 5. Điểm tích hợp thực tế trên box (chỉ đọc, không sửa file)

Tìm nhẹ trong `/workspace` cho thấy hệ sinh thái @hi.oneup đã có sẵn và đang vận hành — Kokoro nếu thử sẽ phải *cắm vào* đây, không đứng một mình:

- **Repo:** `/workspace/oneup-studio/` (có `.git`), tài liệu giọng nói tại `content/voice-profile.md` (status: confirmed, cập nhật 2026-10-12; quy định giọng Nam miền Nam, xưng mình–bạn, markup luật 46, DL-035/DL-039/DL-040).
- **Reference audio hiện tại:** `/workspace/oneup-studio/assets/voice-refs/thai-son.wav` (233 KB) và `my-duyen.wav` (271 KB) — là câu trung tính tổng hợp từ preset VieNeu, *không clone người thật* (ghi rõ trong voice-profile).
- **Checkpoint F5:** `/workspace/f5-ckpt/model_last.pt` (**5.1 GB**) + `vocab.txt`; venv riêng `/workspace/f5-venv/` (Python 3.13.5); còn có `/workspace/tts-venv/` (VieNeu) và `/workspace/asr-venv/` (faster-whisper để chấm take).
- **Code tích hợp:**
  - `pipeline/tts/f5tts_gen.py` — batch synthesis, `F5TTS(model="F5TTS_Base", ckpt_file=…, device="cpu")`, `nfe_step=32`, docstring ghi rõ model `hynt/F5-TTS-Vietnamese-ViVoice (CC-BY-NC-SA-4.0, NON-COMMERCIAL; risk accepted by Hiệp, DL-035)`.
  - `pipeline/scripts/voice-prosody.py` — lớp prosody dùng chung theo `engine` (`vieneu-tts` / `f5-tts`): chia phrase 2–8 âm tiết, gap theo dấu câu, 3 take/phrase, gate ASR ≥ 0.8, mastering. **Đây là điểm tích hợp tự nhiên nhất nếu thử Kokoro-VI:** thêm một `engine="kokoro-vi"` vào cùng job schema, tái dùng nguyên lớp phrase/gap/master, chỉ thay phần sinh raw audio. Không cần sửa `build-final.py` ngoài việc cho phép engine mới (nó đã rẽ nhánh theo `pv.get("engine")`).
  - `pipeline/scripts/check-rules.py` — đang hard-code map nhân vật→engine/ref: `{"omi": ("f5-tts", "F5 · Mỹ Duyên", …), "hiep": ("f5-tts", "F5 · Thái Sơn", …)}`. Đổi engine cho nhân vật nào thì phải sửa map này + `voice-profile.md` — tức là đổi giọng = đổi cả tài liệu brand, cần Hiệp duyệt.
- **Không thấy** thư mục/repo Kokoro nào có sẵn trên box, cũng không thấy script mẫu đang chờ giọng ngoài quy trình script của oneup-studio (`templates/script.md`). Phù hợp với bối cảnh "chưa có script Hiệp chốt" → chưa có gì để render thử lúc này.
- Ngoài phạm vi nhưng đáng ghi: trên box còn có `/workspace/VieNeu-TTS/` (engine cũ DL-033) — nhắc để khỏi nhầm VieNeu (preset gốc tạo ref) với F5 (engine hiện tại) và với Kokoro (ứng viên mới).

---

## 6. Kế hoạch thử nghiệm tối thiểu khi Hiệp đã chốt script

Nguyên tắc: **một vòng duy nhất, định trước pass/fail, thua là dừng.** Không "thử cho biết rồi tính tiếp" vô hạn.

### 6.1 Điều kiện tiên quyết (trước khi render bất kỳ giây nào)

1. Hiệp chốt **1 đoạn script ngắn 30–45 giây** đúng format hiện tại (`phrases`, có cả Hiệp + Omi, có câu hỏi/câu cảm thán/câu chen tiếng Anh/từ đệm miền Nam — vì đó là chỗ TTS tiếng Việt hay gãy).
2. Chốt trước cặp voice Kokoro-VI đem thử (gợi ý: 1 nam trong `manh_dung/hung_thinh/tuan_ngoc` cho Hiệp + 1 nữ trong `diem_trinh/mai_linh/my_yen` cho Omi) — chốt bằng cách nghe sample có sẵn của repo, chưa render script.
3. Kiểm tra license LarVoice theo 3 bước ở mục 2.3 và ghi kết quả vào log. **Không rõ license → vẫn được nghe thử nội bộ, nhưng kết quả "pass" về âm thanh cũng không được phép chuyển sang dùng thương mại.**

### 6.2 Thiết kế A/B mù

| Hạng mục | Cách làm |
|---|---|
| Mẫu | Cùng 1 đoạn script chốt ở 6.1, render 2 bản: **A = F5 hiện tại** (nguyên pipeline, kể cả prosody/master) và **B = Kokoro-VI** (qua cùng lớp phrase/gap/master nếu tích hợp được ở mức tối thiểu; nếu không, render raw rồi master cùng preset −16 LUFS để công bằng loudness). |
| Làm mù | Đổi tên file thành `X.wav`/`Y.wav` ngẫu nhiên, một người (hoặc script) giữ đáp án, Hiệp nghe không biết bản nào là engine nào. Nghe bằng tai nghe + loa điện thoại, mỗi bản nghe tối đa 2 lượt. |
| Tiêu chí chấm (thang 1–5 mỗi tiêu chí, ghi kèm câu/phút bị lỗi) | (1) **Đúng dấu & âm cuối** — đếm lỗi nghe rõ, không chỉ cho điểm cảm tính; (2) **Tự nhiên/ngắt nghỉ** như người Nam nói chuyện; (3) **Phân biệt nhân vật** Hiệp/Omi + giữ chất nhân vật; (4) **Cảm xúc** theo `emotion` từng câu (teasing/happy/focused/sad); (5) **Từ đệm & chen Anh** (nha/á/hông/nè, deadline/focus…) có tự nhiên không; (6) **Artifact** (rè, nuốt chữ, lặp, leakage). |
| Metric khách quan kèm theo | Thời gian render wall-clock cho cùng đoạn (giây render / giây audio = RTF) trên chính box này; ASR (faster-whisper sẵn có) transcribe lại cả hai bản → tỉ lệ khớp chữ với script (cổng hiện tại của pipeline là ≥ 0.8); số take phải render lại. |
| Người chấm | Hiệp là tai quyết định. Nếu có thể, thêm 1 người nghe mù thứ hai chỉ để kiểm tra "người ngoài có nghe ra lỗi dấu không" — không bắt buộc. |

### 6.3 Pass / Fail định trước (chốt trước khi nghe)

**Kokoro-VI chỉ được coi là "đáng đi tiếp" khi đạt TẤT CẢ:**

- Không có lỗi dấu/âm cuối *nghe rõ* nào mà bản F5 không mắc (lỗi loại này tính theo số đếm, không theo điểm trung bình).
- Điểm trung bình 6 tiêu chí ≥ F5, và không tiêu chí nào thấp hơn F5 quá 1 điểm — đặc biệt tiêu chí (3) phân biệt nhân vật không được thua.
- ASR khớp chữ ≥ 0.8 (ngang cổng pipeline hiện tại) và RTF không chậm hơn F5 (kỳ vọng nhanh hơn rõ; nếu không nhanh hơn thì mất một lý do đổi).
- License LarVoice đã rõ ở mức dùng thương mại được, có bằng chứng lưu kèm.

**Fail ở bất kỳ điều nào → không đổi pipeline.** Ghi kết quả vào `oneup-studio/logs/decision-log.md` (theo đúng nếp DL-xxx hiện tại), giữ F5 cho sản xuất, và chỉ xem lại Kokoro khi có một trong hai thay đổi vật chất: (a) hexgrad ra voice tiếng Việt chính thức, hoặc (b) bản cộng đồng công bố benchmark/license dữ liệu rõ ràng. Không lặp lại vòng thử chỉ vì "có version mới" mà không có hai thay đổi trên.

### 6.4 Việc kỹ thuật tối thiểu khi bắt đầu vòng thử (chưa làm bây giờ)

1. Tạo venv Python 3.12 riêng (né xung đột `kokoro<3.13` nếu cần thư viện gốc; đường ONNX của Kokoro-VI có thể né được cả torch lẫn giới hạn này — kiểm tra tại chỗ).
2. Tải artifact Kokoro-VI (~0.7 GB tổng) vào thư mục cache riêng, **không** đụng `f5-ckpt/`.
3. Thêm `engine="kokoro-vi"` vào `voice-prosody.py` theo đúng job schema hiện có; giữ nguyên phrase/gap/take-pick/master.
4. Render, làm mù, chấm theo 6.2–6.3, ghi log, **dừng**.

---

## 7. Điều chưa chắc chắn — liệt kê trung thực

1. **License LarVoice / quyền giọng trong Kokoro-Vietnamese:** chưa xác minh được (mục 2.3). Đây là ẩn số lớn nhất nếu cân nhắc thương mại.
2. **Chất lượng tiếng Việt của Kokoro-VI:** chưa có bất kỳ bằng chứng độc lập nào; mọi nhận định trong báo cáo này về nó đều là "chưa biết, phải nghe".
3. **Miền giọng (Bắc/Nam) của 14 voicepack Kokoro-VI:** model card không ghi; phải nghe.
4. **VRAM/RAM & tốc độ Kokoro:** số liệu lấy từ benchmark tiếng Anh trên máy khác; bậc độ lớn đáng tin (model 82M rất nhẹ), con số cụ thể trên box này chỉ biết khi đo thật ở vòng thử.
5. **Mâu thuẫn `requires_python`:** PyPI nói `<3.13`, GitHub `main` nói `<3.14`. Pip sẽ theo PyPI khi cài từ PyPI; nếu cài từ GitHub source có thể khác. Ghi nhận để khỏi bất ngờ, không ảnh hưởng kết luận chính.
6. **Số liệu biến động theo thời gian:** stars/version/downloads trong báo cáo là tại 2026-10-19; repo cộng đồng Kokoro-Vietnamese còn rất mới, có thể thay đổi nhanh.
7. Báo cáo này **không phải tư vấn pháp lý** về license; nó tóm tắt license công bố công khai và chỉ ra chỗ chưa đủ bằng chứng.

---

## 8. Nguồn đã dùng (link cụ thể)

**Kokoro chính thức**
- Repo + README + LICENSE + pyproject: https://github.com/hexgrad/kokoro · https://github.com/hexgrad/kokoro/blob/main/LICENSE · https://github.com/hexgrad/kokoro/blob/main/pyproject.toml
- Code pipeline (LANG_CODES không có tiếng Việt): https://github.com/hexgrad/kokoro/blob/main/kokoro/pipeline.py
- Model card (82M, Apache-2.0, v1.0 2025-01-27, kiến trúc, dữ liệu train): https://huggingface.co/hexgrad/Kokoro-82M
- Danh sách voice chính thức (9 nhóm ngôn ngữ, 54 voices, không tiếng Việt): https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- Issue xin tiếng Việt + trả lời của maintainer: https://github.com/hexgrad/kokoro/issues/153
- Misaki G2P (có `vi.py` thử nghiệm, link Viphoneme): https://github.com/hexgrad/misaki · https://github.com/hexgrad/misaki/blob/main/misaki/vi.py · https://github.com/v-nhandt21/Viphoneme
- PyPI (version 0.9.4, requires_python): https://pypi.org/pypi/kokoro/json
- ONNX cộng đồng cho bản gốc: https://github.com/thewh1teagle/kokoro-onnx/releases · https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX

**Kokoro-Vietnamese cộng đồng**
- Code: https://github.com/iamdinhthuan/Kokoro-Vietnamese
- Weights/model card (14 voices, vig2p, LarVoice, Apache-2.0 tự công bố): https://huggingface.co/contextboxai/Kokoro-Vietnamese · https://huggingface.co/contextboxai/Kokoro-Vietnamese/tree/main

**F5-TTS (đối chiếu)**
- Code MIT / weights upstream CC-BY-NC-4.0: https://github.com/SWivid/F5-TTS/blob/main/LICENSE · https://huggingface.co/SWivid/F5-TTS
- Thảo luận monetization (chính cộng đồng F5 khuyên Kokoro nếu cần license thoáng + cloning thì qua model khác): https://huggingface.co/SWivid/F5-TTS/discussions/18
- Cấu hình local đang dùng: `/workspace/oneup-studio/pipeline/tts/f5tts_gen.py`, `/workspace/oneup-studio/content/voice-profile.md`, `/workspace/oneup-studio/pipeline/scripts/voice-prosody.py` (đọc tại chỗ trên box, 2026-10-19)

**Benchmark tốc độ Kokoro (tiếng Anh, máy khác — chỉ tham khảo bậc độ lớn)**
- https://gist.github.com/efemaer/23d9a3b949b751dde315192b4dcf0653
- https://heyneo.com/blog/kokoro-supertonic-inflect-nano-pocket-tts-cpu-benchmark

---

*Báo cáo nghiên cứu ban đầu — chưa tạo audio, chưa tải model, chưa cài đặt, chưa sửa file pipeline nào. File duy nhất được ghi là chính báo cáo này. Bước tiếp theo thuộc về Hiệp: chốt script, rồi mới chạy vòng A/B ở mục 6.*
