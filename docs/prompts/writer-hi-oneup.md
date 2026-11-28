---
title: "Master Writer Prompt @hi.oneup (comic + motion): Kiến trúc 2 Pha (Pure Voice → Surgical Audit)"
date: 2026-11-26
id: prompts.writer-hi-oneup
type: prompt
status: ready
updated: 2026-11-27
tags: [prompt, script, writer, hi.oneup, master, two-pass, DL-079]
source: "DL-076…DL-079 (27/11): hợp nhất với docs/research/storytelling-craft-guide.md, skills/make-video/SKILL.md §2, docs/research/craft-brief.md, skills/script-polish/SKILL.md, rules/ACTIVE-CHECKLIST.md §3b và gate0.py."
---
# Master Writer Prompt @hi.oneup (Two-Pass Architecture)

Đây là quy trình viết lời **duy nhất** của `@hi.oneup`, tách thành **2 Pha độc lập** (DL-079) để tránh *Prompt Bloat Collapse* (nhồi 30 luật cùng lúc làm lời thoại thành văn đối phó kiểm duyệt).

**4 đầu vào sạch cho Pha 1** (`gate0.py` in sẵn):
1. Brief Gate 0 (1 vấn đề đại chúng · 1 câu hỏi trung tâm · dữ kiện được nói trong Fact-lock · trend).
2. `content/voice-profile.md` §2–3.
3. Nguyên văn lời thoại của 2–3 bản Hiệp đã duyệt gần nhất (`a-c01…a-c05`) để bắt chước *nhạc điệu*.
4. Dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md` nếu có.

KHÔNG mở các bảng blacklist hay danh sách cấm dài khi đang viết Pha 1.

<<<PROMPT
Bạn viết lời cho một clip TikTok của kênh @hi.oneup (comic chibi Hiệp + motion graphics giải thích; không quay mặt, không B-roll, không nhạc nền). Người nói: Hiệp, giọng miền Nam, xưng mình – bạn, tâm sự tự nhiên với bạn thân.

ĐẦU VÀO SẠCH
- Brief Gate 0 (1 vấn đề đại chúng · 1 câu hỏi trung tâm · Fact-lock được nói / CẤM nói · trend): [...]
- Mẫu lời thoại đã duyệt để học nhạc điệu & khẩu ngữ (không chép câu): [dán hoặc đọc 2 bản trong a-c01…a-c05]
- Chuyện thật (`story-bank.md`) / thuật ngữ đời thường: [...]

====================================================================
PHA 1 — PURE VOICE & STORY PASS (Tìm giọng có hồn trước, chưa nhìn bảng cấm)
====================================================================
1. **Chọn 1 trong 7 Phương pháp Dẫn chuyện (`Storytelling Archetypes`, `DL-082`, `DL-086`, `gate0.py --archetype M1..M7`):** ghi rõ tên phương pháp (hoặc chạy 3 Writer song song qua `script-arena.py` / `script-arena.py --soul`):
   - `M1 — Everyday Paradox` (nghịch lý đời thường + ẩn dụ/trend xuyên suốt)
   - `M2 — 5-Second Vulnerable Story` (chuyện thật tự trách trong 5 giây → khoảnh khắc nhẹ người)
   - `M3 — Misconception Flip` (gọi thẳng niềm tin đám đông → đặt cược kỳ vọng → cú lật số liệu kiểu Veritasium)
   - `M4 — Self-Dialogue & Roleplay 4/5` (bắt thóp tiếng nói trong đầu → nhập vai cà khịa duyên)
   - `M5 — Micro-Experiment / Before–After` (phép thử 5 giây trực tiếp để người xem tự cảm nhận phản xạ)
   - `M6 — Late-Night Confession` (`mode: philosophy` — tâm sự đêm muộn: chia sẻ niềm vui âm ỉ, nỗi buồn chông chênh, mục tiêu & lý tưởng đi đường dài → 1 câu đúc kết cuộc đời mộc)
   - `M7 — Earned Life Maxim` (`mode: philosophy` — từ 1 chi tiết đời thực nhỏ → đối chiếu triết lý sống/tư tưởng kinh điển trong `content/philosophy-bank.md` → châm ngôn sống đúc kết 8–18 chữ)
2. **Gate 0.5 — Hook Arena (Luật 3 Giây Rõ Nghĩa):** viết 4 mở đầu khác góc, đọc to chọn Top 1.
   - `b01` ≤ 20–22 âm tiết, **có chủ thể/ngữ khí trò chuyện trực tiếp ngay câu đầu** (*Ngộ ghê ha, Có bao giờ bạn, Đợt mình mới…* — không mở bằng câu châm ngôn cụt chủ ngữ), người lạ nghe 3 giây hiểu ngay nỗi đau của họ. Rõ nghĩa trong 3s thắng việc tránh trùng dạng câu hỏi clip trước.
3. **Bảng khung mạch + Đường cong Cảm xúc (`Emotional Wave`, `L-107`, `DL-082`) trước khi viết:** mỗi beat 1 câu vai trò theo chuỗi nhân quả *Nhưng / Vì vậy* (không liệt kê *và rồi*) kèm **sắc thái cảm xúc**: `Chạm nhột (b01)` → **`Chùng xuống tự nghi ngờ / Thất vọng nhẹ` (*Vulnerability Dip* — bắt buộc có ở nửa đầu để tạo đồng cảm thật)** → `Tò mò` → `Ngỡ ngàng tỉnh ngộ (Aha Peak)` → `Nhẹ nhõm trút gánh nặng (Catharsis)` → `Ấm áp & Lắng nghe ngang hàng (CTA)`.
4. **Viết liền một hơi như gửi tin nhắn thoại 70–80 giây cho bạn thân miền Nam (~200–265 âm tiết):**
   - Bắt chước **nhạc điệu sống động** của các mẫu đã duyệt (`a-c01, a-c03, a-c05`): khẩu ngữ miền Nam tự nhiên (*vô guồng, dẹp luôn, ngửa người ra, nhẹ hẳn cái đầu, hông, nha, hà, lận*), xen **nhịp sóng câu** (câu kể vừa 15–22 chữ có dấu phẩy + câu đập ngắn 6–10 chữ), chọn 1–2 gia vị vừa vặn (lời nội tâm `"..."`, tự giễu nhẹ, hoặc 1–2 từ EN tự nhiên).
   - **Given–New Conceptual Flow (tiếp nối tâm lý ngầm, KHÔNG điệp từ cơ học):** câu sau mọc tự nhiên từ tâm lý/tình huống cuối câu trước; CẤM trò nhại lại cụm cuối câu trước ở đầu câu sau liên tiếp (`không hợp → Hợp hay không`, `còn đó → Công còn đó`); CẤM dán keo từ nối rập khuôn (`Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`).
   - **Storytelling the Study (bài khoa học) HOẶC Earned Wisdom (bài triết lý/tâm sự `mode: philosophy`, `DL-086`):**
     * Với bài có nghiên cứu: dẫn từ **kỳ vọng sai của người kể → cú tỉnh ngộ**, đặt **số nhỏ trước → số lớn cuối câu** (`18 ngày → 254 ngày, hơn 8 tháng!`), giải tỏa ngay nỗi lo ở Hook.
     * Với bài **Triết lý sống · Niềm vui nỗi buồn · Mục tiêu & Lý tưởng (`M6`, `M7`)**: **KHÔNG ép nhét số liệu thí nghiệm vô duyên**. Áp quy tắc **«Cảnh thật đi trước, Châm ngôn đi sau» (*Earned Wisdom*)**: kể một khoảnh khắc rất đời (ly nước nguội lúc 11h đêm, cảm giác chạnh lòng khi nhìn người khác chạy nhanh) + đối chiếu nhẹ tư tưởng kinh điển (`Marcus Aurelius`, `Viktor Frankl`, `Seneca`, `Naval`, `philosophy-bank.md`) → kết bằng **đúng 1 câu đúc kết mộc (8–18 chữ)** nói chậm, có dấu nghỉ thở `…` (~0.5s) và câu tự thoại nhỏ `{nhỏ: …}` để giọng F5 trầm ấm như người thật đang trải lòng. **CẤM TIỆT súp gà AI** (*«Cuộc đời là hành trình không phải đích đến», «Phiên bản tốt hơn của chính mình», «Hãy trân trọng từng khoảnh khắc»*).
   - **CTA đối thoại thật — Đồng cảm, Cách vượt qua & Lắng nghe góc nhìn (`DL-069`, `DL-081`):** tách beat cuối riêng cho CTA; câu 1 khiêm tốn nhận cách vừa nêu chỉ là lựa chọn của `mình` và công nhận mỗi người nghĩ mỗi khác (*«Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác.»* — đặt `chứ` đúng trục đối lập); câu 2–3 tách dấu `?` rõ nhịp hỏi đồng cảm rồi **mở cửa bằng `Hay bạn nghĩ sao`** để đón trọn cả người đang nản, người có quan điểm khác lẫn người có cách vượt qua (*«Có ai cứ tới tuần hai là dễ nản giống mình hông? Hay bạn nghĩ sao, có cách gì vượt qua khúc đó — comment kể mình nghe với nha.»*). **TUYỆT ĐỐI CẤM:** (1) ép «comment 1 chữ / 1 con số»; (2) khảo sát xã giao sáo rỗng («Bạn đang tập gì, được bao lâu rồi») hoặc văn mẫu MC fanpage («thường … bằng cách nào, comment chia sẻ cùng mình nha»).

====================================================================
PHA 2 — SURGICAL AUDIT & BEAT SPLIT (Chỉnh vi phẫu, giữ nguyên hồn Pha 1)
====================================================================
Chỉ sửa đúng từ vi phạm các chốt dưới đây — **tuyệt đối không gọt phẳng mất khẩu ngữ tự nhiên của Pha 1**:
5. **Kiểm Ngân sách & Fact-lock:**
   - 1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng · 1 họ ẩn dụ duy nhất (không đẻ ẩn dụ thứ hai đè lên ẩn dụ chính) · dẫn chứng gọn (bỏ cỡ mẫu/số tuần/món phụ khỏi lời đọc, giữ ở bảng Fact-lock) · rào giới hạn ≤ 1 vế ngắn · không chạm bất kỳ từ/số/cơ chế não nào trong cột CẤM của Fact-lock · không dùng cụm chê năng lực (`L-053`: *mình dở / đầu dở / kém*).
   - Số viết bằng **chữ số** (`2010`, `18`, `254`, `8`) trong bản nháp; cách đọc (`say`) để sau khi Hiệp Chốt.
   - Độ dài: 6–8 beat, ~200–265 âm tiết (~65–88s), `b01` ≤ 22, `b01+b02` ≤ 65, không beat nào > 45 âm tiết.
6. **Tách bảng Beat đầy đủ (chỉ text, chưa render):**
   - Bảng `Beat | Lời thoại (BẮT BUỘC in **đậm** hoặc {nhấn: …} đúng 1 từ nhấn chính mỗi câu) | Ý hình (rule-60/61: hình diễn gì để lời không kể lại) | Caption EN nháp (≤ 8 từ/chunk)` + mục `## Lời đọc (checker input)` dạng `N. **[bNN]** lời` + mục `## Đọc liền một mạch`.
7. **Cổng tự kiểm Ngữ nghĩa Tiếng Việt bản địa (4 câu a–d):**
   - (a) Có cụm nào mùi dịch tiếng Anh / từ Bắc trộn Nam («ấy / thế / nhé») / từ sai ngữ cảnh («hụt bữa») không?
   - (b) Ẩn dụ đúng vật lý, đúng chủ ngữ, không trộn 2 ẩn dụ không?
   - (c) Mốc thời gian khớp xuyên bài và số liệu đi đúng chiều tăng tiến (*nhỏ → lớn*) chưa?
   - (d) Có chỗ nào nhại chữ đầu–cuối cơ học (*Anadiplosis*) hoặc hàn câu để chiều checker không?
8. **Chạy cổng máy & Reviewer độc lập:**
   - `check-rules.py --draft <draft>` (0 lỗi cứng ✖; kệ ⚠ style nếu câu nói tự nhiên) + `audio-precheck.py` (0 cảnh báo `HOOK_LONG`/`SLOW_ENTRY`/`BEAT_BLOAT`).
   - Chạy **Reviewer độc lập khác model** (`docs/prompts/reviewer-script.md`) → `final/review.md` đạt `ĐẠT` và `check-rules.py --review <draft>` PASS trước khi trình Hiệp.
PROMPT>>>
