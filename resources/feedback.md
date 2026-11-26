---
title: "Góp ý của Hiệp về lời script: chê gì, chấp nhận gì (bản gom cho người viết và reviewer)"
date: 2026-11-26
id: resources.feedback
type: resource
status: ready
updated: 2026-11-26
tags: [feedback, voice, script, reviewer, gate-0, two-tier]
source: "research/review-golden/index.json (hiep_quote nguyên văn), logs/lessons.md L-084…L-107, content/voice-profile.md §2–§3, DL-074"
---
# Góp ý của Hiệp về lời script

File gom góp ý **đang hiệu lực** để Gate 0, người viết và reviewer đọc một chỗ. Không thay nguồn gốc: lời nguyên văn và lý do đầy đủ nằm trong `research/review-golden/` và `logs/lessons.md`. Góp ý theo từng clip vẫn ghi ở `<clip>/final/feedback.md`. Khi Hiệp duyệt hoặc bác một bản mới, thêm một dòng ở bảng 1 hoặc 2 (kèm id mẫu / lesson), không gõ lại lời.

## 1. Hiệp chê (tránh) — lời nguyên văn
| Hiệp nói (nguyên văn, rút gọn) | Lỗi thật sự | Tầng (rubric §3b) | id |
|---|---|---|---|
| «Sao không có trend gì hết» | trend không nghe thấy trong hook | 2 (A) | r-c05-v2 · L-084 |
| «…lấy ví dụ từ sinh học không phổ biến lạc đề…» | ví dụ lấy từ môn học thay vì đời thường | 2 (C) | r-c05-v4 · L-087 |
| «Xàm quá dậy lúc review m đọc k thấy nó rời rạc à» | beat không nối nhau | 2 (B) | r-c05-r4 · L-089 |
| «Trong 3 ý đầu hơi lòng vòng chưa rõ nghĩa và khó hiểu» | hook vòng vo | 2 (A, C) | r-c05-r65 · L-091 |
| «Ý 2 đọc không liên quan giữa các câu» | câu trong một beat không cùng mạch | 2 (B) | r-c05-r67b · L-092 |
| «Các câu nói chưa có chiều sâu còn lủng củng lặp từ quá nhiều» | lặp từ, câu nông | 2 (C, F) | r-c05-r68 · L-093 |
| «Quá lộn xộn các câu thiếu liên kết» | cả bài không có chuỗi lý lẽ | 2 (B) | r-c05-r612 · L-094 |
| «Tệ quá làm lại từ đầu… sáng tạo hơn xem» | vá câu trên khung cũ, nhạt | 2 (A, B) | r-c05-r82 · L-095 |
| «…hook đâu dẫn chứng đâu câu văn cộc lôc xàm» | hook yếu, nguồn mơ hồ, câu cộc | 1 (H1) nếu nguồn sai; còn lại 2 | r-c05-r92 · L-096 |
| «Phải là hook và theo hướng story telling» | hook không kể chuyện | 2 (A) | r-c05-r183 · L-103 |
| «Xàm quá» (hook cái giá nhỏ, không bất ngờ) | hook kể chuyện thiếu cái giá | 2 (A) | r-c05-r1921 · L-104 |
| «Lời văn sến, giả, không giống người nói» | hình ảnh văn chương («cả mâm cơm im bặt») | 2 (C, F) | r-c05-r201 · L-105 |
| «Script vẫn xàm thiếu tự nhiên, cả ai nói lý do nghe mới quê…» | hàn 3 ý bằng dấu phẩy, từ sách | 2 (C) | r-c06-v3 · L-106 |
| «…rời rạc… không có cấu trúc tuần tự gì rõ ràng» | không có bảng mạch | 2 (B) | r-c06-v3r2 · L-107 |

## 2. Hiệp chấp nhận (không phạt)
- **Bản đã duyệt** là chuẩn sàn (rubric §3b): clip-01, clip-02, clip-03, clip-04 (`script-v18-LOCKED.md`), clip-05 (`DL-069`). Đường dẫn ở `research/review-golden/index.json`, mẫu `approved`. Cách viết bản duyệt đã dùng thì không bị trừ.
- **Giọng đã xác nhận** (`content/voice-profile.md` §2): mình – bạn, miền Nam, từ đệm nha / á / hông / nè / đó / hen / ha / luôn / thôi (không phải câu nào cũng có), hài 4/5 tự giễu và trêu thói quen, 1–3 từ tiếng Anh mỗi clip.
- **Câu mẫu Hiệp chấp nhận** (`content/voice-profile.md` §3, cột «Nên»): «Mai của mình dài cả tuần luôn á.» · «Nghe hơi kỳ, mà nó work nha.» · «…mình biết, mình cũng vậy.»
- **Hai kiểu hook đều đạt** (DL-074): chuyện thật ngôi một có cái giá và chỗ bất ngờ (L-103–L-105), hoặc «bạn» + nỗi đau + một câu hỏi bám nỗi đau.
- **Khẩu ngữ là cảnh báo mềm, trừ 0 điểm:** từ nối văn nói (`resources/vn-spoken/connectors.tsv`), câu ngắn ngắt nhịp, câu hỏi tu từ giữ chân.
- **Thời lượng** 120–180 s là mục tiêu; chỉ ≥ 300 s mới chặn (L-099). Không phạt tốc độ nói (L-074).

## 3. Tầng 1 (chặn tuyệt đối)
H1 fact bịa / quá mức nguồn · H2 ≥ 300 s · H3 sai brand / format kênh hoặc chê người xem · H4 lỗi cấu trúc nháp / spec. Chi tiết: `logs/rule-scoring-rubric.md` §3b.
