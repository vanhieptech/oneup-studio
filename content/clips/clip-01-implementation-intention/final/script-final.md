---
id: clip-01.script-final
type: script
status: review (gate 1+2 gộp, DL-041) · tuần 1, không Omi
updated: 2026-10-14
tags: [clip-01, light, pillar-1, story:S-01, ai-voice, f5, final, week-1]
---
# Clip 01 FINAL v2: "Mai học" → nếu… thì… (bản đủ thông tin)

- **Nguồn chuẩn:** `final/spec.json` (bản cũ để ở `spec-v1-demo-w5.json`). Build: `python3 pipeline/scripts/build-final.py content/clips/clip-01-implementation-intention/final/spec.json`.
- **Thời lượng:** 60.7s ⚠ hơi quá mốc 55–60s của luật 4, nhưng trong mức ~70s Hiệp cho phép khi cần thêm thông tin (DL-041). 1080×1920 · 30fps · −14 LUFS · không nhạc.
- **Giọng:** F5-TTS Thái Sơn (DL-035), voice-prosody v5, sinh theo từng vế câu, tiểu từ đọc thường (DL-040). Chỉ có 1 tiếng đệm `{ừm}` ở b02. Không có Omi, nên là tuần 1.
- **Số từ VI:** 200, nhiều hơn mốc 170 của luật 7 vì thêm thông tin (DL-041).
- **Engine:** b01–b03 và b11–b12 làm bằng Remotion comic. e01–e07 làm bằng HyperFrames, lint PASS.

## Beat table
| Beat | Engine | Lời VI | Caption EN |
|---|---|---|---|
| b01 | remotion | Kế hoạch học TOEIC của mình là… **mai học**. | My TOEIC study plan: “tomorrow.” |
| b02 | remotion | Tối nào cũng vậy: code xong, mệt, rồi… “thôi, **mai học**.” | Every night: code, tired, then… “eh, tomorrow.” |
| b03 | remotion | Hoá ra mình đâu thiếu động lực. Mình thiếu **một câu**: nếu… thì… | Not missing motivation. Missing one sentence: IF… THEN… |
| e01 | hyperframes | Tâm lý học gọi nó là ý định thực hiện: viết sẵn mấy giờ, ở đâu, gặp gì, thì làm gì. | It's called an implementation intention: when, where, what cue, THEN what. |
| e02 | hyperframes | Vì mình quyết sẵn lúc còn tỉnh táo. Tới lúc mệt thì khỏi phải cãi với bản thân. | Decide while fresh. When the cue shows up, no debate with tired you. |
| e03 | hyperframes | Ví dụ: chín giờ tối, gập laptop, thì mở một bài listening. | Example: 9 PM, laptop closed, THEN one listening lesson. |
| e04 | hyperframes | Hoặc: sáng thứ ba tám giờ ngồi vào bàn, thì viết phần mở đầu trước. | Or: Tuesday 8 AM, at my desk, THEN write the intro first. |
| e05 | hyperframes | Gộp chín mươi tư kiểm nghiệm độc lập: người viết kiểu này đạt mục tiêu nhiều hơn rõ, hiệu ứng vừa tới lớn. | 94 independent tests: if-then planners hit goals more often. Medium-to-large effect. |
| e06 | hyperframes | Nó giúp bạn bắt tay làm, đứng vững khi bị chen ngang, và dừng việc chắc chắn không thành. | It helps you start, hold on when interrupted, and quit what can't work. |
| e07 | hyperframes | Lỗi hay gặp: “rảnh thì học”. Rảnh đâu phải tín hiệu. Phải là một giờ, một chỗ, hay một việc vừa xong. | Common mistake: “when I'm free.” Use a time, a place, or a finished task. |
| b11 | remotion | Mà nhớ: chỉ hiệu quả với việc bạn **thật sự muốn**. Viết mất một, hai phút thôi. | Only works for goals you actually want. Takes 1–2 minutes. |
| b12 | remotion | Thử luôn đi: viết một câu **nếu–thì** cho cái “mai” của bạn, rồi comment. | Try it now: one if-then line for your “tomorrow”. Comment it. |
| b12 | remotion | Cái “mai” hết đường trốn rồi. | “Tomorrow” has nowhere to hide. |

## Thông tin thêm so với bản cũ (audit theo nguồn)
| Mục | Bản cũ | Bản v2 |
|---|---|---|
| Tên kỹ thuật | không có | "ý định thực hiện" (implementation intention), e01 |
| Cơ chế (vì sao hiệu quả) | không có | quyết sẵn lúc còn tỉnh táo, tới lúc gặp tín hiệu thì khỏi cãi với cái mệt (e02) |
| Ví dụ | 1 | 2: ví dụ listening + ví dụ trong sách "sáng thứ ba 8 giờ → viết phần mở đầu" (e04) |
| Độ lớn hiệu ứng | chỉ hiện trên màn hình | đọc thành lời "vừa tới lớn", màn hình ghi d = 0.65 (e05) |
| 3 tác dụng | nói lướt | bắt tay làm / đứng vững khi bị chen ngang / dừng việc chắc chắn không thành (e06) |
| Lỗi hay gặp | không có | "rảnh thì học" → đổi thành một giờ / một chỗ / một việc vừa xong (e07) |
| Chi phí | không có | "viết mất một, hai phút" (b11) |
| Giới hạn | chỉ có câu "thật sự muốn" | "thật sự muốn" (đọc) + "mostly students & health habits" (trên màn hình) |
| CTA | comment | làm ngay: viết câu nếu–thì cho cái "mai" của bạn, rồi comment |
| Omi | có (nên phải là tuần 5) | bỏ (tuần 1) |

## Motion picks
stagger (e01) · two-column compare (e02) · strikethrough-replace (e03, e04) · count-up + bar-grow (e05) · underline-draw (e06) · scale-pop ✕ + stagger fixes (e07) · push-transition giữa các section · hard-shadow-pop bubble + ding (b12, câu cuối nối lại hook).

## Fact lock (rule-40, nguồn HowToLiveBetter ch.04 §4.1, mức bằng chứng A)
94 kiểm nghiệm độc lập · tỉ lệ đạt mục tiêu cao hơn · d = 0.65, vừa tới lớn · 3 giai đoạn: bắt đầu / giữ khi bị quấy rầy / rút khỏi hướng thất bại · mất 1–2 phút một câu · ví dụ trong sách: sáng thứ ba 8 giờ ngồi vào bàn → viết phần mở đầu · chỉ dùng cho mục tiêu thật sự muốn · đa số người tham gia là sinh viên, mục tiêu sức khoẻ · Gollwitzer & Sheeran (2006), Adv. Exp. Soc. Psych. 38, 69–119.
**Phần chuyển thể (không trích nguyên văn):** câu diễn đạt cơ chế ở e02 và mục "lỗi hay gặp" ở e07 là cách diễn giải từ yêu cầu "khi nào / ở đâu / tình huống cụ thể", không phải câu có trong sách.

## [CẦN HIỆP XÁC NHẬN] (chi tiết đang để chung chung)
1. Hiệp có thật đang học **TOEIC** không (S-01)? Clip không nói điểm mục tiêu hay ngày thi.
2. "Tối nào cũng code xong, mệt, rồi mai học" có đúng là thói quen thật của Hiệp không?
3. Câu "9 giờ tối, gập laptop → một bài listening" là **ví dụ**, trên màn hình có ghi "Example". Hiệp có muốn dùng nó làm câu của mình không?
4. Clip không có câu nào nói "mình đã thử và thấy hiệu quả" (vì chưa được xác nhận).
5. Thời lượng 60.7s và 200 từ: Hiệp có chấp nhận ngoại lệ này không, hay muốn cắt ví dụ thứ 2 (e04) để còn khoảng 56s?
