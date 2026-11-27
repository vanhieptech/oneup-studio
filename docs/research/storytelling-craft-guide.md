---
id: research.storytelling-craft-guide
type: research
status: ready
updated: 2026-11-27
date: 2026-11-27
tags: [script, craft, storytelling, cohesion, two-pass, hi.oneup, DL-078, DL-079]
title: "Storytelling craft guide: dẫn chuyện liền mạch & kiến trúc 2 pha cho video ngắn tiếng Việt (@hi.oneup)"
source: "DL-078 & DL-079 (27/11): Joseph Williams (Given–New Cohesion vs Mechanical Anadiplosis), cấu trúc Đề–Thuyết tiếng Việt nói, Randy Olson (ABT / But–Therefore), Veritasium/Kurzgesagt (Misconception Reveal), Johnny Harris (Everyday Paradox), Matthew Dicks (Storyworthy), nghiên cứu 15 video TikTok thật (hook-script-study-2026-11-11.md), và nghiên cứu Curse of Instructions / Prompt Bloat trên LLM."
---
# Storytelling craft guide (DL-078 · DL-079)

Tài liệu chuẩn nghề của `@hi.oneup`, được trỏ từ `docs/prompts/writer-hi-oneup.md`, `pipeline/scripts/gate0.py` và `docs/prompts/reviewer-script.md`. Giải quyết dứt điểm hai bệnh: (1) câu rời rạc hoặc nối chữ cơ học, (2) văn bản đối phó kiểm duyệt (*Compliance Prose*) do nhồi quá nhiều luật vào cùng lượt viết.

## Trụ cột 1: Kiến trúc 2 Pha chống "Lời nguyền của Chỉ dẫn" (*Two-Pass Architecture*, DL-079)

Nghiên cứu trên LLM (*Curse of Instructions*) chỉ ra: nhồi ~30 mệnh lệnh cấm/ép vào cùng lượt viết sáng tạo làm phân mảnh sự chú ý của mô hình, biến lời kể thành văn bản cứng nhắc, phẳng cảm xúc. Vì vậy **tách hẳn bước Tìm giọng khỏi bước Kiểm luật**:

1. **Pha 1 — Pure Voice & Story Pass (Viết bằng Mẫu / Few-Shot Music):**
   - Chỉ mở: (a) 1 hướng dẫn chuyện đã chọn, (b) hạt giống chuyện + dữ kiện được phép nói trong Fact-lock, (c) nguyên văn lời thoại của 2–3 bản đã duyệt (`a-c01…a-c05`). **Không mở các danh sách cấm lúc này.**
   - Viết liền một hơi như tin nhắn thoại 70–80s Hiệp gửi bạn thân miền Nam: có ngữ khí mở lời trực diện (*Ngộ ghê ha, Đợt mình mới tập, Hồi trước mình cứ tưởng…*), khẩu ngữ sống động (*dẹp luôn, vô guồng, ngửa người ra, nhẹ hẳn cái đầu*), và nhịp sóng câu (câu kể vừa 15–22 chữ có dấu phẩy xen câu chốt ngắn 6–10 chữ).
2. **Pha 2 — Surgical Audit & Beat Split (Kiểm vi phẫu):**
   - Sau khi đã có bản thảo có hồn ở Pha 1, mới rà qua Fact-lock, ngữ nghĩa bản địa, ngân sách âm tiết, rồi cắt bảng Beat đầy đủ (`**nhấn**` mỗi câu, `Ý hình`, `Caption EN` ≤ 8 từ/chunk).
   - **Nguyên tắc vàng:** chỉ sửa vi phẫu đúng từ chạm cấm hoặc vấp lưỡi; **cấm viết lại thành câu công thức làm mất hồn khẩu ngữ của Pha 1**.

## Trụ cột 2: Bốn nguyên lý liền mạch ở tầng ý và tiếng Việt nói

### 1. Given–New Conceptual Flow (Joseph Williams) — KHÔNG PHẢI điệp từ đầu–cuối cơ học (*Anadiplosis*)
Người xem video không đọc lại được; tai chỉ giữ ý vừa mở ở cuối câu trước.
- **Given–New thật (vô hình, tự nhiên):** câu sau mọc tự nhiên từ tâm lý, tình huống hoặc kỳ vọng mà câu trước vừa gợi (vd *tưởng mình không hợp* → *lúc đó mình quên mất câu bông hoa chưa nở, mới hai tuần mới nhú cái nụ làm sao đòi nhẹ liền*).
- **CẤM lạm dụng điệp vòng từ vựng (*Mechanical Anadiplosis*, lỗi clip-06 v12):** không chơi trò bắt lặp mặt chữ 3–4 từ cuối câu N vào đầu câu N+1 liên tiếp (`không hợp → Hợp hay không`, `chưa quen → Thói quen`, `còn đó → Công còn đó`). Điệp từ chỉ dùng tối đa **1 lần/clip** nếu thật sự cần nhấn cao trào.
- **BẮT BUỘC giữ chiều cao trào tăng tiến (*Climactic Order*):** khi nêu dải số liệu, luôn đặt **số nhỏ trước → số lớn gây sốc ở cuối câu** (`nhanh nhất 18 ngày → lâu nhất tới 254 ngày, hơn tám tháng trời lận!`). Tuyệt đối cấm đảo ngược `254 → 18` chỉ để câu sau bắt chữ!

### 2. Đề–Thuyết văn nói tiếng Việt & Ngữ khí mở lời
- **Ngữ khí giao tiếp ngay câu đầu:** mở miệng phải có chủ thể/ngữ khí trò chuyện (*mình, bạn, Ngộ ghê ha, Có bao giờ bạn…*), không mở bằng câu châm ngôn tỉnh lược cụt chủ ngữ (*"Trồng cây thì chờ mấy tháng, tập thói quen hai tuần đã bỏ"*).
- **Đề–Thuyết (Topic–Comment):** đưa cái đang nói tới (Đề) ra đầu câu kèm nhịp nghỉ hoặc tiểu từ mềm (`á / thì / là`), đặt nhận xét/cú lật (Thuyết) ra sau.
- **Từ đời thường miền Nam đúng nghĩa:** cấm ghép ẩn dụ trừu tượng («cái nụ thói quen»), cấm từ lệch nghĩa («hụt bữa» → dùng «lỡ bữa / nghỉ bữa»), cấm mở ẩn dụ thứ hai («đường còn dài») đè lên ẩn dụ chính.

### 3. Chuỗi nhân quả *Nhưng / Vì vậy* (ABT) & Giải tỏa Hook ngay sau số liệu
- Hai ý nối nhau phải là **bẻ ngược (nhưng)** hoặc **hệ quả trực tiếp (vì vậy)** ở tầng ý, không liệt kê «và rồi… và rồi…».
- Vừa đưa xong con số bằng chứng thì **câu kế tiếp giải tỏa ngay nỗi lo ở Hook** (không trì hoãn xuống beat cuối), rồi từ chính kết luận mới («tính bằng tháng») mới tự đẻ ra hệ quả tiếp theo («làm mấy tháng kiểu gì cũng có hôm bận hay mệt phải nghỉ một bữa»).

### 4. Kể chuyện nghiên cứu (*Storytelling the Study*, rút từ 15 video thật `hook-script-study-2026-11-11.md`)
- Không nhảy thẳng vào *"Năm 2010, nhóm Phillippa Lally..."* kiểu Wikipedia.
- Dẫn vào bằng **kỳ vọng sai của người kể → cú tỉnh ngộ khi gặp dữ liệu thật**: *"Hồi trước mình cứ tưởng ráng hai ba tuần là vô guồng. Tới lúc đọc nghiên cứu năm 2010 của nhóm Phillippa Lally mới ngửa người ra..."* — biến số liệu thành bước ngoặt cảm xúc của chính câu chuyện.

## Trụ cột 3: Bốn hướng dẫn chuyện chuyên nghiệp (chọn 1 ở Gate 0, xoay vòng)

| # | Hướng | Nguồn phương pháp | Khung dẫn mạch | Hợp với dạng bài |
|---|---|---|---|---|
| 1 | **Misconception Reveal** | Veritasium, Kurzgesagt | Gọi thẳng niềm tin sai phổ biến → đồng cảm vì sao ai cũng dính → dữ liệu bẻ gãy (Aha!) → thước đo mới + 1 việc làm | Có lời đồn phổ biến (vd «21 ngày thành thói quen») |
| 2 | **Everyday Paradox / Analogy-Led** | Johnny Harris | Đặt 1 nghịch lý đời thường có chủ thể trò chuyện → hòa câu trend/ẩn dụ làm xương sống → kỳ vọng sai vs số liệu thật → 1 việc làm | Có câu trend/ẩn dụ mạnh (vd «bông hoa chưa nở») |
| 3 | **5-Second Moment & Contrast** | Matthew Dicks | Mở ở cảm xúc ngược hẳn cái kết (muốn bỏ cuộc, tự trách) → căng thẳng → khoảnh khắc nhận ra sự thật → nhẹ nhõm + hành động | Chuyện thật của Hiệp (`story-bank.md`), giàu đồng cảm |
| 4 | **Self-Dialogue** | DNA clip-02/03/05 đã duyệt | Hỏi thẳng nỗi đau → nhại lại suy nghĩ quen trong đầu → lật bằng chứng → cách làm gọn + miếng hài nhẹ | Cần giải trí, hài 4/5, nhịp nhanh |
