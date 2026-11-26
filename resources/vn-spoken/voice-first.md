---
title: "Voice-First Input: viết script từ ghi âm nói chay của Hiệp"
date: 2026-11-26
id: resources.vn-spoken.voice-first
type: resource
status: ready
updated: 2026-11-26
tags: [voice, transcript, gate-0, script, vn-spoken]
source: "Yêu cầu Hiệp 26/11 (giữ ~80% từ vựng gốc); pipeline/scripts/voice-memo.py (faster-whisper local); L-106 (viết từ đầu ra lời gượng)"
---
# Voice-First Input

Khi Hiệp nói chay 60–120 giây về ý tưởng, transcript đó là **đầu vào Gate 0**, không chỉ là mẫu giọng. Người viết tái cấu trúc nhịp giữ chân, không viết lại bằng từ của mình.

## Quy trình
1. Thu: Hiệp ghi âm (điện thoại hay Mac), file để ở `media/voice-memos/` (gitignored).
2. Chép: `python3 pipeline/scripts/voice-memo.py <file.m4a>` → `media/voice-memos/<tên>.txt`.
3. Gate 0: `python3 pipeline/scripts/gate0.py --memo media/voice-memos/<tên>.txt …` đưa transcript vào mảnh 3 (chi tiết thật) thay cho story-bank.
4. Viết: giữ từ, ví von, ví dụ, câu chửi yêu của Hiệp. Được phép: cắt câu lặp, đổi thứ tự cho hook lên đầu, chia beat, thêm câu nối (`connectors.tsv`), thêm câu dẫn nguồn (fact lock). Không được: đổi ví von của Hiệp sang ví von khác, thêm chuyện Hiệp không kể (`[CẦN HIỆP XÁC NHẬN]`).
5. Đo: `python3 pipeline/scripts/voice-memo.py keep <memo.txt> <draft.md>` in tỉ lệ từ của nháp có trong transcript. **Mục tiêu ≥ 80%** (từ có nghĩa, bỏ từ đệm và số); dưới mức đó là người viết đang thay giọng Hiệp. Câu dẫn nguồn và tên nghiên cứu được trừ ra khỏi mẫu số khi đánh dấu `{nguồn: …}`.

## Vì sao 80%
Hiệp đặt (26/11). 20% còn lại đủ cho câu nối, câu dẫn nguồn và CTA. Đây là cảnh báo cho người viết, không phải hard fail của reviewer (rubric §3b).
