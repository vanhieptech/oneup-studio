---
id: sample-full-w5
type: sample
status: internal (không đăng)
updated: 2026-10-13
tags: [sample, comic, omi-voice, hyperframes, rule-46, rule-45, rule-11]
---
# Sample tổng hợp (tuần 5+, nội bộ): comic + giọng Omi + explainer

Mục đích: chứng minh toàn bộ hệ thống chạy chung. `meta.week = 5` để qua luật 11. **Không đăng** (story chưa xác nhận đầy đủ, luật 41).

| Phần | Engine | Nguồn |
|---|---|---|
| Beat kể chuyện s1–s2 (12,8s) | Remotion `video-engine/` | `plan.json` → `npm run voice` → `plan.voiced.json` |
| Giọng Omi (2 câu, teasing → focused/happy) | VieNeu-TTS local, preset "Kim Thanh" | `video-engine/public/voice/*.wav` (cache theo hash) |
| Lời Hiệp | chỉ bubble (chưa có bản thu, không giả giọng) | |
| Beat giải thích If → Then (3,0s) | HyperFrames + GSAP local | `explainer/index.html` |
| Ghép (slideleft 0,35s, −14 LUFS, không nhạc) | ffmpeg | `pipeline/scripts/join-beats.sh` |

## Tái tạo
```bash
cd video-engine
npm run voice -- ../content/samples/sample-full-w5/plan.json
npm run render -- ../content/samples/sample-full-w5/plan.voiced.json --out-dir out
cd ../content/samples/sample-full-w5/explainer && npm i && PATH=/workspace/tools/node-v22.20.0-linux-x64/bin:$PATH \
  npx --yes hyperframes@0.8.150 render . -o ../../../../video-engine/out/sample-explainer.mp4 -f 30 --quality delivery
cd ../../../.. && pipeline/scripts/join-beats.sh video-engine/out/sample-full-w5-story.mp4 video-engine/out/sample-explainer.mp4 out.mp4
```
Kết quả đã kiểm (13/10/2026): 1080×1920, 30fps, H.264 + AAC 48 kHz, 15,47s. ASR (faster-whisper small) nghe đúng: "Ủa, lại mai học nữa hả? Ba lần rồi á nha!" (bắt đầu 2,48s, sau tiếng cười) và "Nè, nếu chín giờ thì mở sách 5 phút, dễ hông?" (7,16s).
Khi đăng bản thật có giọng Omi: bật nhãn "AI-generated content" + dòng caption (luật 46).
