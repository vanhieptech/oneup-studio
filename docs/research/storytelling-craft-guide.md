---
id: research.storytelling-craft-guide
type: research
status: ready
updated: 2026-11-27
date: 2026-11-27
tags: [script, craft, storytelling, cohesion, hi.oneup, DL-078]
title: "Storytelling craft guide: dẫn chuyện liền mạch cho video ngắn tiếng Việt (@hi.oneup)"
source: "Hiệp 27/11 (clip-06 v11): «có một chút liền mạch nhưng vài chỗ lại không rõ nghĩa, dẫn câu vẫn chưa liền mạch». Nền: Joseph Williams (Style: Lessons in Clarity and Grace, old-to-new), cấu trúc Đề–Thuyết của văn nói tiếng Việt, Randy Olson (ABT, But/Therefore), Veritasium/Kurzgesagt (misconception reveal), Johnny Harris (analogy-led), Matthew Dicks (Storyworthy, 5-second moment), DNA clip-02/03/05 đã duyệt."
---
# Storytelling craft guide (DL-078)

Vá từng chữ nối trên **một khuôn duy nhất** (`ONEUP-CORE-ARC`) không đủ: v9→v11 vẫn bị chê «rời rạc», «không rõ nghĩa». Gốc là thiếu hai thứ: (1) quy tắc để câu nối câu mà không cần keo từ nối, (2) nhiều hơn một hướng dẫn chuyện để chọn theo chủ đề. File này là chuẩn nghề; `docs/prompts/writer-hi-oneup.md` (lúc viết), `pipeline/scripts/gate0.py` (brief) và `docs/prompts/reviewer-script.md` (lúc duyệt) trỏ về đây. Không thay Fact-lock, giọng Hiệp, ngân sách âm tiết của DL-077.

## Trụ cột 1: ba nguyên lý liền mạch ở tầng câu và ý

### 1. Old-to-New Baton Pass (Joseph Williams)
Người xem không đọc lại được; tai chỉ giữ **ý mới ở cuối câu A**. Muốn câu B nối mượt mà không cần `Vì / Nên / Vậy`: **đầu câu B bắt lại đúng ý vừa thả ở cuối câu A (thông tin cũ), cuối câu B mới thả ý mới.**
- Cuối câu A là «không hợp» thì câu B phải nói tiếp về «hợp hay không», không nhảy sang chuyện khác. Sai mẫu (v11): b01 kết «chắc mình không hợp rồi», b02 mở «Hai tuần mà mình đòi quen liền…», làm rơi gậy.
- Đầu câu B có thể là đại từ trỏ rõ («con số đó», «chuyện đó») hoặc lặp đúng danh từ cuối câu A. Không đổi chủ đề giữa chừng.
- **Baton Check (cách kiểm):** gạch dưới 3–4 chữ cuối của mỗi câu, rồi nhìn 3–4 chữ đầu của câu kế. Hai đầu này không chạm nhau (không cùng chủ đề, không có đại từ trỏ) là chỗ đứt.

### 2. Đề–Thuyết văn nói tiếng Việt (Topic–Comment)
Tiếng Việt nói trọng **Đề**: đưa cái đang nói tới (Đề) ra đầu câu, có nhịp nghỉ hoặc tiểu từ mềm (`á / thì / là`), rồi mới tới nhận xét hoặc cú lật (Thuyết). Cùng một Đề thì lược chủ ngữ tự nhiên.
- Ví dụ: «Chuyện chạy bộ á, hai tuần đầu lúc nào cũng nặng như đeo chì.» tự nhiên hơn câu dịch khung Chủ–Vị–Tân kèm liên từ.
- **Từ miền Nam đời thường, đúng nghĩa.** Cấm ghép ẩn dụ trừu tượng không ai nói («cái nụ thói quen»); cấm từ lệch nghĩa («hụt bữa» nghe thành thiếu bữa ăn, dùng «lỡ bữa / nghỉ bữa»); cấm mở ẩn dụ thứ hai («đường còn dài») đè lên ẩn dụ chính (một hình duy nhất xuyên bài).

### 3. Nhưng / Vì vậy ở tầng ý (ABT, But–Therefore)
Hai ý liền nhau chỉ có hai quan hệ hợp lệ: **bẻ ngược (nhưng)** hoặc **hệ quả trực tiếp (vì vậy)**. Cấm kiểu «và rồi… và rồi…» (liệt kê).
- **Giải tỏa Hook ngay sau bằng chứng.** Vừa thả con số xong thì câu kế trả lời nỗi lo ở Hook («18–254 ngày» → «mới hai tuần oải là bình thường, đâu phải không hợp»). Không đẩy câu trả lời xuống beat cuối (lỗi v11 b04→b07).
- Ý tiếp theo phải đẻ ra từ chính kết luận vừa có («hơn 8 tháng» → «giữ lâu vậy kiểu gì cũng có hôm nghỉ»), không phải ý đứng riêng.
- Không dùng chữ nối (nhưng, vì vậy) như lớp sơn. Quan hệ phải có thật; chữ nối chỉ đánh dấu, không tạo mạch (Thought-Flow, DL-077 / v10).

## Trụ cột 2: bốn hướng dẫn chuyện (chọn ở Gate 0, xoay vòng)

Gate 0 chọn **một** hướng (ghi tên trong bảng khung mạch), không ép mọi clip vào cùng khuôn. Hook ≤ 20 âm tiết, 3 giây rõ nghĩa và ngân sách DL-077 áp cho cả bốn.

| # | Hướng | Nguồn phương pháp | Khung | Hợp với |
|---|---|---|---|---|
| 1 | **Misconception Reveal** | Veritasium, Kurzgesagt | Gọi thẳng niềm tin sai ai cũng tin → đồng cảm vì sao ai cũng dính → dữ liệu bẻ gãy → thước đo mới + 1 việc làm | Bài có lời đồn phổ biến (vd «21 ngày thành thói quen») |
| 2 | **Everyday Paradox / Analogy-Led** | Johnny Harris | 1 nghịch lý đời thường ai cũng thấy đúng → nối thẳng vào ẩn dụ/trend (làm xương sống, không dán thêm) → bằng chứng giải thích nghịch lý → 1 việc làm | Bài có câu trend/ẩn dụ mạnh (vd «bông hoa chưa nở») |
| 3 | **5-Second Moment & Contrast** | Matthew Dicks | Mở ở cảm xúc ngược hẳn cái kết (muốn bỏ cuộc, tự trách) → căng thẳng → khoảnh khắc nhận ra → nhẹ nhõm + hành động | Chuyện thật của Hiệp (`story-bank.md`), giàu đồng cảm |
| 4 | **Self-Dialogue** | DNA clip-02/03/05 đã duyệt | Hỏi thẳng nỗi đau → nhại lại suy nghĩ quen trong đầu → lật bằng chứng → cách làm gọn + miếng hài nhẹ | Bài cần giải trí, hài 4/5, nhịp nhanh |

Cách chọn nhanh: có lời đồn → #1; có câu trend/hình ẩn dụ sẵn → #2; có chuyện thật đã xác nhận → #3; còn lại mà cần hài nhịp nhanh → #4. Không có hướng nào được phép bỏ qua Fact-lock hoặc luật «1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng».

## Cách viết với bộ này (thứ tự)
1. Chọn hướng (1 trong 4) ở Gate 0, ghi trong bảng khung mạch.
2. Viết đoạn liền một hơi theo hướng đó; áp Baton Pass từng cặp câu, Đề–Thuyết khi đặt câu.
3. Chạy **Baton Check** và **phép thử bỏ từ nối đầu câu** trước khi cắt beat.
4. Cắt beat; kiểm Fact-lock, từ lệch nghĩa, ẩn dụ phụ; chạy checker và reviewer.

## Ví dụ làm mẫu: clip-06 hướng #2 (v12)
`content/clips/clip-06-bong-hoa-chua-no/final/script-v12-draft.md`: hook là nghịch lý (cây chờ cả mấy tháng, thói quen mới hai tuần đã muốn bỏ) → chạy bộ oải → «nụ» làm xương sống cho trend → Lally 18–254 ngày → giải tỏa «không hợp» ngay sau con số → «hơn 8 tháng thì kiểu gì cũng có hôm nghỉ» → việc tối nay → CTA.
