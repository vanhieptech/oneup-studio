---
id: research.storytelling-craft-guide
type: research
status: ready
updated: 2026-11-27
date: 2026-11-27
tags: [script, craft, storytelling, cohesion, two-pass, cta-psychology, hi.oneup, DL-078, DL-079, DL-081]
title: "Storytelling craft guide: dẫn chuyện liền mạch, kiến trúc 2 pha & tâm lý CTA đối thoại thật (@hi.oneup)"
source: "DL-078, DL-079 & DL-081 (27/11): Joseph Williams (Given–New Cohesion vs Mechanical Anadiplosis), Đề–Thuyết tiếng Việt nói, Randy Olson (ABT), Veritasium/Kurzgesagt, Johnny Harris, Matthew Dicks, nghiên cứu 15 video TikTok thật (hook-script-study-2026-11-11.md), Curse of Instructions trên LLM, và nghiên cứu tâm lý bình luận video ngắn (Banner Blindness, Shared Struggle, Perspective Scaffolding + dữ liệu top comment teardown)."
---
# Storytelling craft guide (DL-078 · DL-079 · DL-081)

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

### 5. Tâm lý học CTA Đối thoại Thật — Đồng cảm, Cách vượt qua & Lắng nghe góc nhìn (*Authentic Conversation CTA*, DL-069 · DL-081)
Nghiên cứu hành vi người xem TikTok/Shorts (*Banner Blindness*, *Shared Vulnerability*, *Perspective Scaffolding*) và dữ liệu top comment thực tế trong repo (`manghocls` Khối 4: comment 509 tim chia sẻ cách làm riêng, comment 205 tim đồng cảm nỗi đau) chỉ ra **2 bẫy CTA thất bại phải cấm tiệt**:
- **Cấm Bẫy 1 — *Gimmick/Command CTA*:** «Comment một chữ / một con số nha» khi hỏi trải nghiệm/thói quen (cưỡng ép, sai ngữ nghĩa tiếng Việt).
- **Cấm Bẫy 2 — *Survey/Small-Talk Boilerplate (Khảo sát xã giao sáo rỗng)*:** «Dạo này bạn đang tập thói quen gì, được bao lâu rồi, comment kể mình nghe nha» — câu hỏi điểm danh khô như khảo sát, không có điểm chạm cảm xúc, bị não người xem lọc bỏ như câu thảo mai xin tương tác cuối clip.

**3 động cơ tâm lý thật sự kéo bình luận chất lượng** (mỗi CTA phải kết hợp ít nhất 2/3 động cơ này, đặt ở beat riêng sau khi người nói khiêm tốn nhận cách vừa nêu chỉ là lựa chọn của riêng `mình`):
1. **Shared Struggle / Empathy Mirror («Có ai bị giống mình hông?»):** Tự thú điểm yếu thật ở đúng khúc dễ gãy nhất (*cứ tới tuần hai là dễ nản*) để người xem thấy mình không cô đơn và muốn lên tiếng xác nhận.
2. **Crowdsourced Overcoming Strategy («Cách mọi người vượt qua khúc đó»):** Hỏi kinh nghiệm thực chiến mỗi người dùng để bước qua đúng ngưỡng khó vừa kể, thay vì hỏi chung chung họ đang làm việc gì.
3. **Open Perspective Listening («Mỗi người một góc nhìn / quan điểm riêng»):** Thể hiện rõ sự tôn trọng rằng không có một công thức đúng cho tất cả (người hợp đi nhẹ giữ nhịp, người hợp ép kỷ luật gắt, người cần bạn đồng hành) — mở sàn lắng nghe quan điểm cá nhân của từng người xem.

**3 mẫu khung CTA xoay vòng cho `@hi.oneup` (mở cửa đôi bằng `hay` để đón cả người đang nản, người nghĩ khác lẫn người có mẹo riêng; không dán nhãn khẩu hiệu khô và không dùng đuôi MC fanpage «chia sẻ cùng mình nha»):**
- *C1 — Hạ cái tôi + Mở cửa đôi bằng `Hay` (Đồng cảm · Góc nhìn khác · Cách vượt qua):* «Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác. Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»
- *C2 — Đặt 2 hướng thực tế (Perspective Split):* «Cách của mình là hạ nhẹ giữ nhịp thôi, chứ mỗi người hợp mỗi kiểu — tới khúc dễ nản đó bạn chọn đi nhẹ từ từ hay ép kỷ luật gắt luôn, comment cho mình nghe góc nhìn với nha.»
- *C3 — Khiêm tốn học hỏi kinh nghiệm riêng (`a-c05`):* Thừa nhận chắc nhiều bạn có cách hay hơn mình ở đúng bài toán vừa bàn, mời chia sẻ cách/quan điểm riêng của họ.

## Trụ cột 3: Bốn hướng dẫn chuyện chuyên nghiệp (chọn 1 ở Gate 0, xoay vòng)

| # | Hướng | Nguồn phương pháp | Khung dẫn mạch | Hợp với dạng bài |
|---|---|---|---|---|
| 1 | **Misconception Reveal** | Veritasium, Kurzgesagt | Gọi thẳng niềm tin sai phổ biến → đồng cảm vì sao ai cũng dính → dữ liệu bẻ gãy (Aha!) → thước đo mới + 1 việc làm | Có lời đồn phổ biến (vd «21 ngày thành thói quen») |
| 2 | **Everyday Paradox / Analogy-Led** | Johnny Harris | Đặt 1 nghịch lý đời thường có chủ thể trò chuyện → hòa câu trend/ẩn dụ làm xương sống → kỳ vọng sai vs số liệu thật → 1 việc làm | Có câu trend/ẩn dụ mạnh (vd «bông hoa chưa nở») |
| 3 | **5-Second Moment & Contrast** | Matthew Dicks | Mở ở cảm xúc ngược hẳn cái kết (muốn bỏ cuộc, tự trách) → căng thẳng → khoảnh khắc nhận ra sự thật → nhẹ nhõm + hành động | Chuyện thật của Hiệp (`story-bank.md`), giàu đồng cảm |
| 4 | **Self-Dialogue** | DNA clip-02/03/05 đã duyệt | Hỏi thẳng nỗi đau → nhại lại suy nghĩ quen trong đầu → lật bằng chứng → cách làm gọn + miếng hài nhẹ | Cần giải trí, hài 4/5, nhịp nhanh |
