---
id: clip-01.script-final
type: script
status: review (gate 2) · DEMO tuần 5
updated: 2026-10-13
tags: [clip-01, light, pillar-1, storytelling, story:S-01, omi, ai-voice, final]
---
# Clip 01 FINAL (demo / template tuần 5): "Mai học" → nếu… thì…

- **Nguồn chuẩn:** `final/spec.json` (sửa ở đây, không sửa file sinh ra). Build: `python3 pipeline/scripts/build-final.py content/archive/clip-01-implementation-intention/final/spec.json`.
- **Thời lượng:** 57.3s · 1080×1920 · 30fps · H.264 High yuv420p bt709 (tv range) · AAC 48 kHz mono · −14 LUFS · không nhạc · grain nhẹ.
- **Theme:** LIGHT (theme-map clip 1). Trụ 1 "Làm ít, xong nhiều". Trend: "mai làm" / "dự án ma" (câu chung, không phải chuyện thật của Hiệp).
- **Giọng (DL-030):** Hiệp = VieNeu-TTS preset **Đức Trí** (nam, miền Nam, trầm ấm, F0 ≈ 91 Hz, tempo 1.3×). Omi = preset **Kim Thanh** (nữ, miền Nam, tempo 1.12×). Không clone, chạy local.
- **Luật 11:** có Omi ⇒ `week: 5`. **Bản này KHÔNG đăng được như clip tuần 1.** Muốn đăng tuần 1: bỏ Omi (thoại của Omi chuyển cho Hiệp) → build lại.
- **Số từ VI:** 168 (trong mốc 150–170, luật 7).

## Beat table
| Beat | Thời gian | Phần | Hình | Ai nói | Lời VI (đọc) | Caption EN | Cảm xúc |
|---|---|---|---|---|---|---|---|
| b01 | 0.1–2.4s | Hook | Comic, giường 11:48 PM, Hiệp ngồi buồn, trăng + zzz | Hiệp | Kế hoạch học tô ích của mình là, mai học. | My TOEIC study plan: “tomorrow.” | neutral |
| b02 | 3.4–5.8s | Vật lộn | Comic, bàn làm việc: Hiệp gõ phím → dừng, buồn | Hiệp | Tối nào cũng vậy á: code xong, mệt, rồi, | Every night: code, tired, then… | neutral |
| b02 | 6.0–9.7s | Vật lộn | Comic, bàn làm việc: Hiệp gõ phím → dừng, buồn | Hiệp | Thôi, mai học. Mai của mình dài cả tuần luôn. | “Eh, tomorrow.” My tomorrow lasts all week. | sad |
| b03 | 10.4–15.6s | Vật lộn | Omi pop vào, trêu; Hiệp giật mình | Omi | Nhóm chat nào cũng có dự án ma. Còn bạn có hẳn kỳ thi ma á nha. | Everyone has a ghost project. You have a ghost exam. | teasing |
| b04 | 16.6–19.2s | Bước ngoặt | Giấy trắng, iris: Omi chỉ cách, Hiệp nhận ra 'như code' | Omi | Nè, sửa đúng một câu thôi: nếu, thì, | Change one sentence: IF… THEN… | focused |
| b04 | 19.4–21.8s | Bước ngoặt | Giấy trắng, iris: Omi chỉ cách, Hiệp nhận ra 'như code' | Hiệp | Nếu, thì? Nghe giống code ghê á. | If-then? Sounds like code. | happy |
| b05 | 22.6–25.9s | Giải thích | HyperFrames: If → Then, 4 thẻ When/Where/Cue/Then hiện theo từng chữ (stagger) | Hiệp | Công thức nè: mấy giờ, ở đâu, gặp gì, thì làm gì. | When, where, what cue, THEN what. | focused |
| b06 | 26.8–30.4s | Ví dụ | 'Mai học' bị gạch (strikethrough-replace) → thẻ IF 9 PM / THEN 1 listening | Hiệp | Ví dụ: chín giờ tối, gập laptop lại, thì mở một bài listening. | 9 PM, laptop closed: one listening lesson. | neutral |
| b07 | 31.3–35.6s | Bằng chứng | Số 94 đếm lên (count-up) + thước small/medium/large, d=0.65 (bar-grow) + nguồn | Hiệp | Gộp chín mươi tư kiểm nghiệm độc lập: ai viết nếu–thì, làm xong mục tiêu nhiều hơn hẳn. | 94 independent tests: if-then planners reached goals more often. | focused |
| b08 | 36.5–41.0s | 3 tác dụng | 3 dòng Start / Hold on (Messenger·3) / Quit what can't work, gạch chân vẽ tay (underline-draw) | Hiệp | Nó giúp lúc bắt đầu, lúc Messenger réo, và lúc nên bỏ việc chắc chắn không thành. | It helps you start, hold on when Messenger pings, and quit what can't work. | neutral |
| b09 | 41.6–45.3s | Payoff + lưu ý | Comic giấy: Omi nhắc giới hạn, Hiệp vui 'có hẹn với TOEIC' + ding | Omi | Mà nhớ nha: việc hông thật sự muốn thì viết cỡ nào cũng vậy. | Only works for goals you actually want. | focused |
| b09 | 45.5–48.9s | Payoff + lưu ý | Comic giấy: Omi nhắc giới hạn, Hiệp vui 'có hẹn với TOEIC' + ding | Hiệp | Ô kê. Chín giờ tối nay, mình có hẹn với tô ích. | Okay. 9 PM tonight: date with TOEIC. | happy |
| b10 | 49.9–54.3s | CTA + loop | Comic lưới: CTA comment, Omi chốt câu nối hook (loop) | Hiệp | Còn bạn? Viết một câu nếu–thì cho cái mai của bạn, rồi comment nha. | Your turn: one if-then line. Drop it in the comments. | happy |
| b10 | 54.5–56.8s | CTA + loop | Comic lưới: CTA comment, Omi chốt câu nối hook (loop) | Omi | Cái mai hết đường trốn rồi nha. | “Tomorrow” has nowhere to hide. | happy |

## Motion picks (skill motion-picks-per-script, catalog awesome-ai-motion)
| Beat | Ý đồ | Effect chính (slug) | Ghi chú |
|---|---|---|---|
| b01 | hook | `push-in` | camera push 0.06 + bubble pop + "11:48 PM" narration box |
| b02–b04 | kể chuyện | `squash-stretch` / `overlapping-action` (rig) | Omi `scale-pop` vào ở b03; chuyển cảnh slide / iris (`iris-mask`) |
| A→E | chuyển phần | `push-transition` (xfade slideleft 0.35s) + whoosh | |
| e01 | giải thích | `stagger` | thẻ hiện đúng chữ "mấy giờ / ở đâu / gặp gì / thì" |
| e02 | ví dụ / so sánh | `strikethrough-replace` | gạch "Mai học" rồi thay bằng thẻ IF/THEN |
| e03 | số liệu | `count-up` + `bar-grow` | 0→94; thước hiệu ứng tới d = 0.65 |
| e04 | liệt kê | `underline-draw` | 3 dòng, gạch chân vẽ tay khi đọc tới |
| E→B | chuyển phần | `iris-mask` (xfade circleopen) | |
| b09–b10 | payoff / CTA | `hard-shadow-pop` (bubble, caption) | ding khi "có hẹn"; câu cuối nối lại hook "mai" (loop) |

## Fact lock (giữ nguyên, rule-40)
94 kiểm nghiệm độc lập · hiệu ứng trung bình tới lớn (d = 0,65, trên màn hình) · 3 tác dụng: bắt đầu / giữ khi bị cắt ngang / bỏ việc chắc chắn không thành · chỉ hiệu quả với việc mình thật sự muốn · đa số nghiên cứu trên sinh viên, thói quen sức khoẻ (trên màn hình) · Gollwitzer & Sheeran (2006).

## [CẦN HIỆP XÁC NHẬN] (chi tiết đang để chung chung)
1. Có thật Hiệp đang học **TOEIC** không (story-bank S-01)? Video không nêu điểm mục tiêu hay ngày thi.
2. Tối nào cũng "code xong, mệt, rồi… mai học" có đúng thói quen thật?
3. Câu nếu–thì "chín giờ tối, gập laptop, mở một bài listening" là **ví dụ** (trên màn hình ghi "Example line"). Hiệp có dùng câu này thật không?
4. Câu kết "chín giờ tối nay mình có hẹn với TOEIC" là lời hứa của Hiệp, cần Hiệp đồng ý.
5. Không có câu nào nói "mình đã thử và hiệu quả" (chưa được xác nhận nên không đưa vào).

## STT (faster-whisper small, toàn bộ track final)
Nhận đúng toàn bộ câu. Sai chính tả do ASR, không phải lời: TOEIC → "TÔ ÍC", code → "cốt", laptop → "láp top", "gập" → "gặp". Trước câu "Thôi, mai học" có tiếng thở dài (tag [thở dài] của cảm xúc sad), ASR ghi thành "Xài…".

## Revisions
- 2026-10-13 DL-030: v1 final demo: Hiệp + Omi AI voices, comic A/B + HyperFrames explainer
- 2026-10-13 DL-030: review r1: b01 medium framing (caption covered face), EN highlight indices e03/e04, explainer layout fills frame, tv range, 2-pass loudness
- 2026-10-13 DL-030: review r2: e04 row 3 overflowed right edge (font 84→72), b09 EN highlight 'actually want'
- 2026-10-13 DL-030: review r3: b03 EN highlight 'ghost … exam.' (was 'a'); grain alls 4 + CRF 20/maxrate 14M (431 MB → ~30 MB)
