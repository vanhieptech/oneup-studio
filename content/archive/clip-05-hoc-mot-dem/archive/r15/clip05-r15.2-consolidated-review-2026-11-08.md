# clip-05 r15.2 PATCH2 — review gộp (Rule Reviewer, chỉ đọc), 08/11/2026 ~14:45 giờ VN
- Bản mới nhất: handoffs/clip05-r15.2-full-draft-2026-11-08.md (mtime 14:26).
  - File SHA 87885dd3…7dc2, lời SHA 3a6f280d…a78e, 439 đơn vị. Mình tự tính lại, khớp.
- Luật/skill (mtime 13:06 / 12:40 / 13:02) không đổi so với các lượt trước.
- Đã đọc:
  - clip05-r15.2-rule-review (a84679f2…)
  - clip05-r15.2-factcheck (6a72bbd7…, 14:36)
  - social-clip05-r15.1-source-review (5f03d893…)
  - clip05-r15.1-consolidated-review (2e273aca…)

## Kết luận
- r15.2 ĐẠT nghĩa/craft văn bản (K1, K2 đóng) và ĐẠT fact Deep trên đúng SHA mới.
- Social: chỉ được mang sang phần byte không đổi, KHÔNG phải verdict Social trên SHA mới.
- KHÔNG phải PASS tổng, chưa Chốt.

## 1. Delta thật r15.1 → r15.2 (mình tự diff)
- Lời: chỉ đổi S18 «Tự viết nhỉnh hơn ở mốc này» → «Tự viết cho tỷ lệ ý nhớ đúng cao hơn ở mốc này». Vế sau dấu phẩy giữ nguyên.
  - Deep cũng kiểm độc lập: bỏ bytes S18 thì phần còn lại cùng hash 7153b793… (factcheck dòng 17–18).
- Ngoài lời, file đổi:
  - tiêu đề/ghi chú;
  - mapping S18;
  - caption S18 (dòng 201);
  - timing ƯỚC b07–b09;
  - mục 7, 10 (số đếm: 439 đơn vị, ƯỚC 181.08s / 205.30s);
  - mục 11 (checker trên adapter r15.2).
- KHÔNG đổi: lời S05, caption S05, dòng storyboard b02.

## 2. Gate
| Gate | Trạng thái | Căn cứ |
|---|---|---|
| Nghĩa/craft (Reviewer) | ĐẠT văn bản. K2 đóng; K1 giữ đóng; các mục đạt của r15/r15.1 giữ cho câu không đổi | clip05-r15.2-rule-review dòng 9–40 |
| Fact RK/F5 (Deep) | ĐẠT trên SHA 87885dd3 / 3a6f280d. S18 mới đúng tỷ lệ, chiều, mốc; không thêm mức độ hay effect size. Caption S18 cũng đạt | factcheck dòng 9–20, 38–56, 85 |
| Sync nguồn Deep | Live main a32f51f (ls-remote mới); blob nguồn khớp working tree. Local HEAD 8ff7698 ≠ live; Mac CHƯA KIỂM; report chưa archive | factcheck dòng 22–36 |
| Social | Verdict Social gắn SHA r15.1 (ee0e5aa8), không có verdict trên SHA mới. Có thể mang sang ở mức scope cho lời S05, caption S05 và storyboard b02, vì các byte này không đổi (đã diff). Caption S18 và các dòng b07–b09 đổi nhưng nằm ngoài scope trend; Deep đã chấm caption S18. Deep tự ghi không phát hành verdict Social (dòng 80) | social r15.1 dòng 6–12; factcheck dòng 77–81 |

## 3. Checker text-only — r15.1 cũ đã lỗi thời, mình đã chạy lại trên r15.2
- Adapter có sẵn clip-05-r15.2-checker-input.md (c18ba89d…): 9/9 đoạn trùng nguyên văn lời.
- Không ghi file, không --out; `git status` trước = sau.
- OC đã chạy trên r15.2: --subjects 0/0; --l088 0✖ 1⚠ (ngoài thư mục clip).
- Mình chạy lại:

| Flag | r15.2 | Thay đổi do S18 |
|---|---|---|
| --flow | 0✖ 1⚠ (b03, b08 mở beat) | không |
| --clarity | 0✖ 2⚠ | MỚI: S18 26 chữ >25. S17 32 chữ + S18 26 chữ đứng liền nhau ở payoff |
| --link | 0✖ 1⚠ (S03→S04, S05→S06) | không. S17→S18 không bị cờ |
| --repeat | 0✖ 1⚠ | «cho tỷ lệ» ×2 → ×3 |
| --evidence / --choppy | 0✖ 0⚠ | không |
| --fresh (r12, r11.4) | 0✖ (0.06 / 0.07) | không. Vẫn «so 1 bản» |

- Không cờ nào là lỗi chặn; các cảnh báo cũ đã được chấm tay ở review r15/r15.1.
- Rủi ro MỚI từ delta (không mở lại craft): hai câu dài liền nhau S17–S18 ở payoff, và «tỷ lệ ý nhớ đúng» lặp. Cả hai là rủi ro khi nghe, cần người thật, không chặn văn bản.
- Chưa chạy: --trend (adapter thiếu trường trend); chế độ thư mục clip đầy đủ (cần spec).

## 4. Việc còn lại chính xác (chờ owner cho phép điều phối; Reviewer không liên hệ ai)
1. Social: xác nhận hoặc phát verdict trên SHA 3a6f280d, hoặc owner chấp nhận mang sang theo scope byte không đổi ở mục 2.
2. News, sau khi được cho phép:
   - lưu r15.2 + reports vào path canonical;
   - chạy lại --l088 trong thư mục clip;
   - tạo adapter có trường trend và chạy --trend;
   - chạy --fresh --against đủ các bản bị bác (r11.4, r12, r14.2) và xác nhận parse được từng bản.
   - Không chạy --stage plans trước Chốt.
3. Người thật: đọc to, người lạ nghe hook, nghe một lần. CHƯA KIỂM. Ưu tiên tai thật cho hook S01–S02, S05, payoff S17–S18 (câu dài) và cụm lặp.
4. Trình Hiệp đọc thử: chỉ khi owner cho phép, ghi rõ là chưa có kiểm người đọc độc lập và chưa Chốt.
5. Sau Chốt: spec text-only → checker thư mục clip đầy đủ (rule-4 tổng <300s gồm endcard; rule-56) → sản xuất. Timing thật đo sau Chốt.
   - ƯỚC 181–205s: vượt target 180s nên chỉ cảnh báo; <300s.
