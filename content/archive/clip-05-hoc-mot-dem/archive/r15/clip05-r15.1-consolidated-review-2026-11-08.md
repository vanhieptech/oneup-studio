# clip-05 r15.1 — review gộp (Rule Reviewer, chỉ đọc), 08/11/2026 ~14:30 giờ VN
- Bản: file 57322fba…0183c, lời ee0e5aa8…0652. Tính lại lúc gộp: vẫn khớp, không đổi.
- Không sửa lời, repo hay code. Không research. `git status` trước và sau khi chạy checker giống nhau.

## Kết luận
- r15.1 ĐẠT gate nghĩa/craft văn bản và gate nguồn (scoped) trên đúng SHA lời.
- Không phải PASS tổng, chưa Chốt. Còn chờ: checker --trend/clip-dir, đọc to người thật, archive.

## 1. Đã đạt
| Gate | Kết quả | Nguồn |
|---|---|---|
| Nghĩa/craft (Reviewer) | ĐẠT văn bản. K1 đóng (S01 «hai đoạn khác nhau»); các phần đạt của r15 giữ nguyên vì S02–S21 không đổi byte | /workspace/clip05-r15-rule-review-2026-11-08.md, /workspace/clip05-r15.1-rule-review-2026-11-08.md |
| Fact RK/F5 (Deep) | Không lỗi fact chặn trên SHA ee0e5aa8. S18 «nhỉnh hơn» CHẤP NHẬN vì đứng ngay sau 56/42; có rủi ro sắc thái, không đặt ngưỡng effect-size cho từ ngữ. K2 vì vậy đóng ở gate nguồn | /workspace/clip05-r15.1-factcheck-2026-11-08.md (sha e381e6bd…), dòng 7, 14–15, 37–53, 59–72 |
| Trend/attribution (Social) | ĐẠT S05 + caption + storyboard; không blocker; không chấm S18 | /workspace/social-clip05-r15.1-source-review-2026-11-08.md (sha 5f03d893…), dòng 6–7, 12, 19 |
| Sync nguồn | Cả hai report đọc live main a32f51f (pinned); blob nguồn khớp local. Local HEAD 8ff7698 ≠ live, không nói toàn repo đồng bộ. Mac CHƯA KIỂM. Hai report chưa archive | factcheck dòng 23, 33; social dòng 26–27 |

Scope và citation: cả hai report nêu đúng SHA file/lời, tách phạm vi (Deep = RK/F5; Social = trend), không tự PASS craft hay tổng. Không có điều nguồn mới nào làm mở lại phần nghĩa đã đạt.

## 2. Checker text-only đã chạy thật (trước Chốt, không plans/TTS/media)
Đầu vào là adapter có sẵn handoffs/clip-05-r15.1-checker-input.md. Mình đã kiểm: 9/9 đoạn trùng nguyên văn khối lời. Không ghi thêm file nào, không dùng --out.
| Flag | Kết quả | Ghi chú tay |
|---|---|---|
| --subjects | 0✖ 0⚠ | — |
| --l088 | 0✖ 1⚠: nháp ngoài thư mục clip nên không tự tìm file trend/fact | Gate tay đã có từ Deep/Social |
| --flow | 0✖ 1⚠: b03 «Với chuyện nhớ sau vài ngày», b08 «Với mục tiêu kể sau vài ngày» | Đã chấm tay là nối được (gọi lại S04/S13). Giữ |
| --clarity | 0✖ 2⚠: câu hỏi trước tình huống; S05 28 chữ, S17 32 chữ | Hook dữ liệu đã duyệt ở concept E. Câu dài là rủi ro nghe, chờ người thật |
| --link | 0✖ 1⚠: S03→S04, S05→S06 | Đã chấm tay: trả lời → hứa; «phép so này». Giữ |
| --repeat | 0✖ 1⚠: «trong thí nghiệm» ×5, «sau vài ngày» ×3… | Rủi ro nặng tai, không chặn |
| --evidence / --choppy | 0✖ 0⚠ | — |
| --fresh (so r12, r11.4) | 0✖. Hook giống nhất 0.06, chuỗi beat 0.07 | Lưu ý: checker báo «so 1 bản», nên có thể chỉ parse được r11.4 |
KHÔNG chạy:
- --trend: adapter thiếu trend_id/hook_pattern/trend_beats/trend_spoken; muốn chạy phải ghi adapter mới.
- Chế độ thư mục clip đầy đủ (rule-4 duration, rule-52/55/56…): cần spec.json; build plans có thể gọi voice.

## 3. Việc cụ thể cho News (khi được giao; không phải Reviewer làm)
1. Lưu r15.1 vào đúng path canonical của clip-05 qua luồng storage. Rồi chạy lại --l088 để nó tự tìm file trend/fact.
2. Tạo adapter/frontmatter text-only có trend_id (texthip-kr-reading-lifestyle-znews-1693810), hook_pattern, trend_beats, trend_spoken, example_evidence lấy từ registry/Social. Chạy `check-rules.py --trend`. Không đổi lời.
3. Chạy lại `--fresh --against` với đủ các bản bị bác (r11.4, r12, r14.2), xác nhận checker parse được từng bản.
4. Chế độ thư mục clip đầy đủ, rule-4 tổng <300s, rule-56 loop/engagement: chỉ chạy sau Chốt, với spec text-only. KHÔNG chạy `build-final --stage plans` trước Chốt (có thể gọi voice).
5. Archive hai report nguồn. Baseline storage 388 không phải lý do chặn lời.

## 4. Duration policy (L-099) — task ĐÓNG ở repo
- 8426a5e (13:06): duration_policy.py, check-rules rule-4 (≥300s ✖, ngoài 120–180s ⚠), rules, checklist, lessons L-099.
- 807bf15 (13:08): mirror skills/make-video + docs/plans.
- Cả hai commit nằm trong origin/main và HEAD local.
- tests.test_check_rules_l099: 19/19 OK (chạy lại lúc gộp).
- Chỗ còn ghi 45–60/55–60s trong repo đều đã gắn nhãn «supersedes»/lịch sử (make-video:15, 19; video-rules:273 là changelog), hoặc không liên quan (hyperframes talking-head-recut).
- Không cần Mac approval hay sửa gì thêm.
- Ghi chú: ước dùng 2.9 từ/s của policy cho lời 433 từ ≈ 149s, cộng endcard và chuyển cảnh nữa thì có thể sát hoặc vượt 180s. Chỉ là cảnh báo, <300s.

## 5. Còn chờ (không tự PASS)
- Đọc to, người lạ nghe hook, nghe một lần: CHƯA KIỂM. Rủi ro cần tai thật:
  - hook S01–S02 thiên giọng báo chí, nói về sinh viên;
  - câu dài S05/S17;
  - «trong thí nghiệm» lặp;
  - sắc thái «nhỉnh».
- Timing thật: sau Chốt.
- --trend, --l088 có ngữ cảnh clip, chế độ clip đầy đủ: chờ News như mục 3.
- Archive r15.1 + reports: CHƯA. Mac: CHƯA KIỂM.
- Hiệp chưa đọc thử, chưa Chốt. Không tạo hình/giọng trước Chốt.
