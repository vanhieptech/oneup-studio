---
title: "Delivery analysis: trend audio 'bản chất' vs clip-02 v14 voice"
date: 2026-10-16
type: research
tags: [research, voice, clip-02, L-036]
status: draft
source: "ban-chat-dao-dong-dieu-hoa.mp3 (Hiệp gửi 15/10, gửi lại 16/10 — cùng sha256 83f53723…, không chép bản trùng); faster-whisper word timestamps (transcript-medium.txt) + librosa pyin F0 / RMS"
---
# Delivery analysis (L-036)
Đơn vị: thời lượng chữ (s), đỉnh F0 so với trung vị câu (st), năng lượng so với trung vị câu (dB). Chữ thường ≈ 0,2–0,3 s.

| Stem | Audio mẫu: chữ nhấn / kéo / pause | clip-02 v14 (F5 nguyên dòng) | Khác | Sửa (F5) |
|---|---|---|---|---|
| Thì cái bản chất của cái việc [X] là gì? | "cái bản chất" +11 st, +4 dB (đỉnh ngay đầu); "[X]" (Russian accent) kéo 0,6 s; "gì?" kéo 0,6 s rơi −17 st | "Thì" kéo 0,64 s (sai chữ); cao +5…+9 st đều mọi chữ tới "Tíc Tóc là"; "gì" ngắn 0,24 s, không rơi | nhấn sai chỗ, phẳng-cao, không rơi cuối | phrase 1 "Thì cái {nhấn: bản chất}" · 2 "của cái việc mở láp tóp rồi lướt Tíc Tóc…" (kéo chữ ruột) · 3 "là gì?" `emph_semi` −1, kéo |
| Thứ nhất là các bạn phải [A] liên tục ở [B], một cách lặp đi lặp lại | "Thứ" +11 st +8 dB kéo 0,42; payload "rô rõ" 0,58–0,68 +6 st +7 dB; "lưỡi/liên" nhấn; "lặp đi lặp lại" mỗi chữ 0,44–0,60 s, rơi −11…−13 st | "Thứ" kéo nhưng "nhất là các bạn" +6…+10 st; "lướt" chỉ 0,22 s; "lặp đi lặp lại" 0,18–0,22 s (không kéo) | chữ ruột "lướt" + "lặp đi lặp lại" không kéo, nói nhanh | tách "Thứ nhất là" · "các bạn phải {nhấn: lướt} liên tục ở trên giường," · "một cách… {kéo: lặp đi lặp lại}" speed 0.8 + emph_semi −1 |
| Thứ hai là khi nào xuất hiện [C] thì chúng ta phải [D] | "Thứ hai" +10…+11 st +9 dB; "khi" kéo 0,42 +10 st; "âm W" kéo 0,66 + punch +8 dB; "Thì" kéo 0,42 = pause bản lề; vế sau đọc nhanh, thấp | gần như mọi chữ +2…+10 st; "cảm giác khó chịu" không kéo (0,22–0,32); "thì" kéo 0,66 (đúng) | payload không kéo; quá dài (C+D ~30 chữ vs 13) | "Thứ hai là {nhấn: khi nào}" · "xuất hiện {kéo: cái cảm giác khó chịu}…" · "thì chúng ta phải đổi việc liền:" · "dọn bàn, coi ri viu." rơi |
| Và cuối cùng là các bạn phải [E] | "Và" kéo 0,52; "cuối cùng" +8,5 st +7 dB; vế sau đọc dồn nhanh 0,2–0,3/chữ, rơi −9…−12 st (giọng gằn) | "cuối cùng" +12 st (đúng); "chửi" −1,7 st (không nhấn!); "né" +5,8 st cuối câu (lên giọng) | chữ ruột "chửi" mất nhấn; cuối câu lên thay vì rơi gằn | "Và cuối cùng là" · "các bạn phải tự {nhấn: chửi} bản thân mình cho đã —" · "rồi mai lại né." emph_semi −1,5 |
| Chen ngang (No, we don't do that / What are you doing?) | 1–2 s, giọng khác, sát nút (pause 0–0,2 s) | Hiệp-né +2 st; khoảng 0,1–0,3 s | ổn | giữ; ≤ 0,15 s |

**Kết luận:** mẫu = "stem nhấn cao + chữ ruột kéo gấp đôi + đuôi rơi thấp"; F5 nguyên dòng cho "đều cao". Cần tách clause (L-007/L-016 v4) và nhấn/kéo chữ ruột.

**Dùng làm ref F5?** Không. Đây là giọng một creator thật (trend TikTok, không rõ bản quyền/được phép) → clone = vi phạm DL-035 ("voice presets, no cloning", check-rules "voice presets") và rủi ro nhận dạng giọng; nền nhạc/giọng Nga lẫn vào. Chỉ dùng làm mẫu nhịp (đo/đối chiếu), ref vẫn là thai-son.wav tổng hợp.
