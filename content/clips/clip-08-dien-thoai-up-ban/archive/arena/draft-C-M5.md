---
source: "oneup-studio (soạn trong repo)"
title: "Arena Writer C (M5 — Micro-Experiment / Before–After (Phép thử 5 giây trực tiếp))"
date: 2026-11-28
id: arena.writer-c-m5
type: draft
status: draft
updated: 2026-11-28
tags: [arena, script-draft, m5]
---
# Đấu trường Kịch bản — Writer C (`M5`: Micro-Experiment / Before–After (Phép thử 5 giây trực tiếp))

> **LỆNH PHA 1 (PURE VOICE PASS — `DL-079`):** Đọc 2–3 clip duyệt gần nhất để thấm nhạc điệu miền Nam xưng mình–bạn, rồi viết liền 1 hơi sống động theo đúng phương pháp dưới đây. **Không mở bảng cấm từ trong lúc viết.** Sau khi viết xong mới sang Pha 2 kiểm Fact-lock & âm tiết (`200–265` âm tiết, `b01 ≤ 20`, mỗi beat `≤ 45`).

- **Phương pháp được khóa:** `M5` — Micro-Experiment / Before–After (Phép thử 5 giây trực tiếp) (*tương tác · thực tế · cầm nắm được*)
- **Cách mở Hook:** Mời người xem làm ngay 1 phép thử tưởng tượng 5 giây để tự thấy phản xạ của chính mình.
- **Đường cong cảm xúc bắt buộc (`Emotional Wave`):** Kéo vào phép thử → Khựng lại thấy đúng là mình hay kẹt ở đó (Dip) → So sánh trước–sau → 1 bằng chứng chốt hạ → 1 bước thử tối nay → Hỏi kết quả & cách mỗi người
- **Mẫu duyệt gợi ý nghe nhịp:** a-c03, a-c01

## Fact-lock dùng chung (tuyệt đối không vượt ngoài khối này — H1)

---
title: "clip-08 fact lock — Ward 2017 (HTB 3.1)"
date: 2026-11-28
id: clip-08.fact-lock
type: research
status: locked
updated: 2026-11-28
tags: [clip-08, fact-lock, ward-2017, htb-3.1]
source: "HowToLiveBetter 3.1 + Ward, Duke, Gneezy & Bos (2017), doi:10.1086/691462, qua Canale et al. (2019) Sci Rep 9:18519"
---

# clip-08 fact lock

Nguồn đã mở: Canale, Vieno, Doro, Rosa Mineo, Marino & Billieux (2019), *Scientific Reports* 9:18519, mô tả đúng thiết kế Ward et al. (2017), *Journal of the Association for Consumer Research* 2:140–154 (`doi:10.1086/691462`). Bài gốc Chicago bị chặn bot ngày 28/11/2026, nên lời đọc chỉ nói những gì Canale viết ra được khi trích Ward. Meta Böttger et al. (2023), PMC10525686, đã mở: gộp «dùng máy» và «máy có mặt», g = −0,14 (nhỏ, không đồng nhất). Meta này không được nói trong lời.

| Được nói | Cấm |
|---|---|
| Ward, Duke, Gneezy & Bos 2017 (`doi:10.1086/691462`); lời đọc «nhóm Ward năm 2017»; màn hình `WARD ET AL. 2017` | «chứng minh», «khoa học khẳng định», «nhiều nghiên cứu cho thấy» khi không nêu tên |
| Hai thí nghiệm trong lab. Thí nghiệm 1: điện thoại của chính mình để im — trên bàn (trong tầm nhìn), trong túi/balo, hoặc phòng khác. Bài nhớ thao tác (OSpan) và một phần Raven kém hơn khi máy «sẵn» hơn | Nói «giảm IQ», «não bị rút», «kém hẳn», «rớt một nửa», bất kỳ số % hay cỡ mẫu nào (bài gốc chưa mở được) |
| Thí nghiệm 2: tắt nguồn hay để im không đổi kết quả; chỗ để máy mới đổi. Lời đọc: «Tắt nguồn không đổi gì.» | Nói tắt thông báo / Focus Mode là kết quả của Ward |
| Mức phụ thuộc máy có thể làm lệch mạnh hơn — chỉ được nói nếu cần, và phải là «người càng dính máy thì lệch càng rõ», không nói bệnh | Dopamine, cortisol, «nghiện» như chẩn đoán |
| Việc tối nay «cắm sạc ngoài phòng» là cách áp dụng mục 3.1 (máy ra khỏi tầm mắt), luật 67, không phải số liệu | Gán «câu đang viết» hay «phòng khách» vào kết quả nghiên cứu |
| Stothart 2015 (thông báo không mở) và Wilmer 2017 («mức gần bằng lúc đang dùng máy») nằm ngoài lời đọc | «gần bằng nghe gọi», «một tiếng rung cũng bằng nhấc máy» |

Câu hỏi trung tâm: úp máy xuống rồi, đầu óc có đỡ xao không? Câu trả lời được phép: trong lab của nhóm Ward, máy còn nằm trên bàn thì người ta làm bài nhớ tệ hơn so với lúc máy nằm phòng khác, dù tắt nguồn. Úp mặt xuống là cảnh của mình (giấu màn hình), không phải điều kiện thí nghiệm.

<!-- GATE0-BRIEF:BEGIN (pipeline/scripts/gate0.py) -->
## Gate 0 brief (@hi.oneup)

### 1. Ý tưởng đã chọn + fact package
- [ARC-003 · @hi.oneup] Dùng mạch lật định nghĩa 'ảo mộng mới' cho thói quen sống: chuyện nhiều người chăm chỉ bấm hoàn thành nhiệm vụ uống nước, ngủ sớm cho nhân vật ảo trên app quản lý thói quen hoặc xem clip dọn phòng lúc 2 giờ sáng thay vì tự làm ngoài đời; dùng Hiệp và Omi mổ xẻ lý do bộ não chuộng 'cảm giác sống gọn gàng giả lập' hơn thực tế rồi chốt 1 hành động 2 phút cực dễ bắt đầu. — hook nháp: Bạn có thấy kỳ không, mình từng thức tới hai giờ sáng chỉ để canh giờ cho nhân vật trong app đi ngủ sớm? (teardown `research/trends/2026-11-28/teardowns/trends-2026-11-28-01.md`)
- [ARC-003 · @hi.oneup] Vì sao bạn lên kế hoạch tập thể dục hay đọc sách mãi không làm nổi: không phải lười mà do đặt mục tiêu kiểu 'phải xong', thử đổi sang mục tiêu 'chỉ cần có mặt 10 phút' cùng đồng hồ hẹn giờ để não hết sợ bắt đầu (comic chibi Hiệp nằm lướt điện thoại đối đầu bức tường 'Mục tiêu khổng lồ' rồi thu nhỏ nó thành viên gạch 10 phút). — hook nháp: Có bao giờ bạn biết rõ hôm nay phải đọc sách hay tập thể dục, mà cứ nằm bấm điện thoại miết không nhấc người lên nổi không? (teardown `research/trends/2026-11-28/teardowns/trends-2026-11-28-04.md`)
- [ARC-001 · @hi.oneup] 3 việc nhỏ làm thói quen dính hơn (đời thường, không lấy môn học — L-087): Hiệp chibi thử từng việc, mỗi việc một cơ chế + một nghiên cứu có nguồn, motion beat giải thích cơ chế — hook nháp: [chuyện thật của Hiệp lần bỏ thói quen] + «có ba việc nhỏ mà mình ước biết sớm hơn» (teardown `research/trends/2026-11-26/teardowns/manghocls-7366613156908600583.md`)
- Fact package: chưa có (`research/explainers/<chủ-đề>.md`); mọi số liệu cần claim → nguồn trước khi viết (H1).

### 2. Mạch cốt truyện
- **Phương pháp dẫn chuyện (Archetype `M5`):** Micro-Experiment / Before–After (Phép thử 5 giây trực tiếp) — màu sắc: *tương tác · thực tế · cầm nắm được*
  - Cách mở Hook: Mời người xem làm ngay 1 phép thử tưởng tượng 5 giây để tự thấy phản xạ của chính mình.
  - Đường cong cảm xúc (`Emotional Wave`): Kéo vào phép thử → Khựng lại thấy đúng là mình hay kẹt ở đó (Dip) → So sánh trước–sau → 1 bằng chứng chốt hạ → 1 bước thử tối nay → Hỏi kết quả & cách mỗi người
- **ONEUP-CORE-ARC** Mạch 5 nhịp thực dụng @hi.oneup: tình huống → bẻ thước đo → 1 bằng chứng → 1 việc tối nay → CTA chia sẻ đồng hành · cơ chế hook: nỗi đau cụ thể → lật thước đo (thực dụng, gọn, sắc, tự giễu nhẹ) · bằng chứng: a-c01 (Hiệp, đã duyệt), a-c04 (Hiệp, đã duyệt) · đã dùng 0 lần · win_rate: chưa có
- Tổng hợp đa video (`research/trends/weekly-synthesis.md`): hook đang thắng — tò mò (danh sách có số + neo thành tích) (8.64)
  1. [Hook tình huống: 1 khoảnh khắc/sai lầm cụ thể ai cũng từng mắc, 1–2 câu] — không mở bài chung chung
  2. [Bẻ góc nhìn: nối vì sao mình nghĩ vậy, dẫn mượt sang trend nếu có (không nhảy cóc), rồi 1 câu hỏi gọn vạch ra cái bẫy đo sai]
  3. [1 bằng chứng đắt: câu dẫn tự nhiên + đúng 1 kết luận từ fact-lock; con số lớn phải dịch nghĩa cho người nghe; bỏ cỡ mẫu, bối cảnh phụ]
  4. [Cách làm: 1 đổi góc nhìn/thước đo + 1 hành động cụ thể tối nay, trên chính ví dụ của nhịp 1]
  5. [Khép vòng + CTA đối thoại thật (DL-069, DL-081): khiêm tốn nhận đó là cách của mình → đồng cảm «ai bị giống mình» ở khúc dễ nản + lắng nghe góc nhìn/cách vượt qua của mỗi người; cấm khảo sát sáo rỗng «bạn đang tập gì» & cấm ép comment 1 chữ]
- Mạch chuẩn `ONEUP-CORE-ARC`: **200–265 âm tiết ≈ 65–88s** đọc tự nhiên (2.7–3.3 âm tiết/s); các clip đã duyệt nằm ở ~190–310 âm tiết. Đủ ý thì dừng: không kéo dài, cũng không bóp cụt phần kể chuyện (chuyện thật, tự giễu, lời nội tâm là chất của kênh); chỉ mở rộng lên 120–180s (`--extended`) khi chủ đề có nhiều bước kỹ thuật thật sự.
  Ngân sách âm tiết mỗi nhịp (gợi ý để cân đối, không phải trần cứng): hook 15–20 · lật kèo 40–55 · chứng minh 55–70 · áp dụng 55–70 · kết 30–40. Một ví dụ xuyên suốt từ nhịp 1 tới nhịp 4. Không bịa chuyển cảnh, không câu tóm tắt bài học.

Nhịp cho @hi.oneup: gợi ý **65s** khi chưa có lời (65–88s, mạch lõi, hard cap < 300s gồm end card/nghỉ/chuyển cảnh, L-099). Câu chuyện đã đủ ý thì giữ độ dài đó, không kéo chữ. Story beat = comic, giải thích/bằng chứng = motion (DL-027).
| giây | vai trò | khung |
|---|---|---|
| 0–6 | hook | [Hook tình huống: 1 khoảnh khắc/sai lầm cụ thể ai cũng từng mắc, 1–2 câu] — không mở bài chung chung |
| 6–20 | lật kèo | [Bẻ góc nhìn: nối vì sao mình nghĩ vậy, dẫn mượt sang trend nếu có (không nhảy cóc), rồi 1 câu hỏi gọn vạch ra cái bẫy đo sai] |
| 20–37 | chứng minh | [1 bằng chứng đắt: câu dẫn tự nhiên + đúng 1 kết luận từ fact-lock; con số lớn phải dịch nghĩa cho người nghe; bỏ cỡ mẫu, bối cảnh phụ] |
| 37–55 | áp dụng | [Cách làm: 1 đổi góc nhìn/thước đo + 1 hành động cụ thể tối nay, trên chính ví dụ của nhịp 1] |
| 55–65 | kết | [Khép vòng + CTA đối thoại thật (DL-069, DL-081): khiêm tốn nhận đó là cách của mình → đồng cảm «ai bị giống mình» ở khúc dễ nản + lắng nghe góc nhìn/cách vượt qua của mỗi người; cấm khảo sát sáo rỗng «bạn đang tập gì» & cấm ép comment 1 chữ] |

Open Loop & Micro-Payoff (mỗi 35–45s):
- ~38s: trả một phần lời hứa (micro-payoff 1) → mở câu hỏi mới kéo sang đoạn sau (open loop 2)

### 3. Chi tiết thật + giọng Hiệp
- Story bank S-05 phone-bed: Hay thức khuya, cầm điện thoại trên giường (cần Hiệp xác nhận + chi tiết)
- Story bank S-02 oneup-2h: Tự làm OneUp + Omi một mình, khoảng 2h/ngày sau giờ làm (cần Hiệp xác nhận + chi tiết)
- Philosophy bank P-08 (Chấp nhận mất mát & đổi thay của cuộc đời): cảnh thật «Những mối quan hệ, giai đoạn, dự án từng gắn bó hết lòng nhưng tới lúc buộc phải khép lại» · nguồn `Epictetus (Amor Fati — yêu lấy số phận) · `29`` · đúc kết mộc: «Có những thứ khép lại không phải vì mình làm sai, mà vì vai trò của nó trong cuộc đời mình tới đó là trọn vẹn rồi.»
- Philosophy bank P-01 (Cô đơn khi theo đuổi mục tiêu): cảnh thật «11h đêm tắt màn hình, cả ngày cặm cụi làm thứ mình tin mà nhìn quanh chưa có gì để khoe, tự hỏi mình có đang đi lạc không» · nguồn `Marcus Aurelius (*Meditations*) · `S-02` làm OneUp 2h/tối` · đúc kết mộc: «Lúc chưa ai thấy kết quả, thứ giữ mình ngồi lại không phải động lực, mà là mình biết mình đang sống thật với điều mình chọn.»
- **Giọng Hiệp (`content/voice-profile.md` §2, bắt buộc):** miền Nam nhất quán, xưng mình–bạn; cấm trộn chữ Bắc «ấy / thế / nhé» cạnh «hông / nha / nè». Có chủ thể/ngữ khí trò chuyện ngay câu đầu (không mở bằng châm ngôn cụt chủ ngữ); đọc lên phải giống tin nhắn thoại gửi bạn thân.
- **Kiến trúc 2 Pha chống Prompt Bloat (DL-079, `docs/prompts/writer-hi-oneup.md`):** **Pha 1 (Pure Voice)** học nhạc điệu từ 2–3 mẫu duyệt gần nhất, viết liền 1 hơi sống động trước (không mở bảng cấm). **Pha 2 (Surgical Audit)** mới kiểm Fact-lock, ngân sách âm tiết, tách Beat có đánh dấu `**nhấn**` mỗi câu — chỉ sửa vi phẫu từ vi phạm, cấm gọt phẳng khẩu ngữ.
- **Ngân sách nguyên liệu (Anti-Stuffing Budget, DL-077..079):** không phải checklist điền đủ.
  - **Đúng 1 nỗi đau đại chúng** · **Đúng 1 câu hỏi trung tâm** · **6–7 beat, ~200–265 âm tiết (~65–88s)** (`b01` ≤ 20 âm tiết rõ nghĩa trong 3s đầu, `b01+b02` ≤ 65, beat ≤ 45; `audio-precheck.py` cảnh báo `HOOK_LONG` / `SLOW_ENTRY` / `BEAT_BLOAT`).
  - **Bằng chứng ≤ 35 âm tiết (Storytelling the Study + Climactic Order):** dẫn từ kỳ vọng sai → cú tỉnh ngộ (không nhảy kiểu Wikipedia), đặt **số nhỏ trước → số lớn gây bất ngờ cuối câu** (`18 → 254 ngày, hơn 8 tháng`), dịch nghĩa số lớn, bỏ cỡ mẫu/số tuần/món phụ khỏi lời đọc; rào giới hạn ≤ 1 vế ngắn; gia vị giọng chọn **tối đa 1–2 thứ** tự nhiên.
  - **Đủ ý & Khép vòng + CTA chia sẻ đồng hành + Thought-Flow over Connector-Glue (DL-069, DL-080, DL-081):** giải tỏa nỗi lo ở Hook **ngay sau số liệu**, có 1 đổi thước đo + 1 hành động cụ thể; CTA phải **đồng cảm («ai bị giống mình») + lắng nghe góc nhìn/cách mỗi người vượt qua khúc dễ nản**, **cấm khảo sát xã giao sáo rỗng («bạn đang tập gì, được bao lâu») & cấm ép «comment 1 chữ»**; cấm mở câu rập khuôn `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`, cấm câu meta «dạo này có câu trend nói» hay cảnh giả «lướt trúng câu đang trend»; trend là xương sống ngay Hook hoặc xin ngoại lệ như `DL-069`.
  - **Given–New Conceptual Flow + 4 hướng dẫn chuyện (`docs/research/storytelling-craft-guide.md`, DL-078/079):** chọn 1 hướng ở Gate 0 (`Misconception Reveal` · `Everyday Paradox` · `5-Second Moment` · `Self-Dialogue`); nối bằng tâm lý/tình huống ngầm (**CẤM điệp từ cuối–đầu cơ học Anadiplosis** kiểu `còn đó → Công còn đó`); Đề–Thuyết tự nhiên, 1 họ ẩn dụ duy nhất, không từ lệch nghĩa.
- Chuyện thật từ `content/story-bank.md` (`[CẦN HIỆP XÁC NHẬN]` nếu chưa chốt), không bịa kết quả.
- **Chỉ nạp 4 thứ khi viết nháp v1/v2:** (1) brief này (Gate 0 + Fact-lock + trend); (2) `content/voice-profile.md` §2–3; (3) 2–3 bản đã duyệt gần thể loại nhất: a-c03 `content/archive/clip-03-big-task-chunking/final/script-final.md`, a-c04 `content/archive/clip-04-gap-sach-tu-kiem/final/script-v18-LOCKED.md`, a-c05 `content/archive/clip-05-hoc-mot-dem/final/script-final.md`; (4) dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md` nếu có. Không nạp `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv`, style-pairs vào bước viết; các bảng đó chỉ cho `check-rules.py --audit` sau khi lời đã xong.
- **Fact-lock:** ghi danh sách số/kết luận được phép nói và danh sách CẤM (từ/số bị cấm, cơ chế não ngoài nguồn) trước khi viết; chạm vào danh sách cấm = H1. **Single-Point Alignment:** chọn 1 câu hỏi trung tâm; hook và bằng chứng là câu hỏi và câu trả lời của cùng câu đó.
- **Nhịp thực tế của 5 clip đã duyệt** (đo từ file, không phải khuôn liệt kê): học độ dài beat + cách chuyển ý + giọng, không chép câu.
  - a-c01: tự giễu + ví dụ đời thường: «mai học» của chính Hiệp, kế hoạch nếu–thì cụ thể, trả lời tuần tự
    12 beat · 201 âm tiết · TB 16.8 âm tiết/beat · 21 câu · beat: b01 9, b02 11, b03 13, e01 21, e02 18, e03 12, e04 15, e05 23, e06 19, e07 22, b11 17, b12 21
  - a-c02: khung «bản chất» + meme đời thường: hook thầy hỏi bản chất, 3 dấu hiệu, 1 con số Steel, gọi lại clip-01
    11 beat · 212 âm tiết · TB 19.3 âm tiết/beat · 26 câu · beat: b01 4, b01b 10, b02 9, b03 18, b05 23, b06 26, b07 35, b08 29, b09 20, b09c 22, b10 16
  - a-c03: hook câu hỏi mở + chia nhỏ vật lý: việc to thành vài việc cầm được, hai nghiên cứu ngắn, ví dụ dọn phòng/ôn thi ← mẫu gần nhất, mở đọc
    10 beat · 298 âm tiết · TB 29.8 âm tiết/beat · 21 câu · beat: b01 17, b02 26, b03 27, b04 41, b05 47, b06 24, b07 37, b08 26, b09 24, b10 29
  - a-c04: kể chuyện khép vòng: mở bằng chuyện học tối qua sáng quên, đi một mạch, chốt đúng nỗi đau mở đầu ← mẫu gần nhất, mở đọc
    8 beat · 187 âm tiết · TB 23.4 âm tiết/beat · 13 câu · beat: Hook 21, Ví dụ 31, Nguyên nhân 29, Mục tiêu 14, Cách làm 31, Bằng chứng 27, Kết quả 19, CTA 15
  - a-c05: giọng miền Nam + miếng hài nhập vai: «hà / nè / hông», thí nghiệm có số rõ, câu rào giới hạn, cú hài ghi sổ đầu bài ← mẫu gần nhất, mở đọc
    15 beat · 312 âm tiết · TB 20.8 âm tiết/beat · 24 câu · beat: b01 15, b01b 11, b02 19, b03 16, b07 35, b07b 20, b07c 21, b08 12, b09 26, b09b 11, b09c 16, b09d 27, b09e 15, b09f 35, b10 33

### 4. Lưu ý mới nhất
- Hiệp chê: «…hook đâu dẫn chứng đâu câu văn cộc lôc xàm» → hook yếu, nguồn mơ hồ, câu cộc (r-c05-r92 · L-096)
- Hiệp chê: «Phải là hook và theo hướng story telling» → hook không kể chuyện (r-c05-r183 · L-103)
- Hiệp chê: «Xàm quá» (hook cái giá nhỏ, không bất ngờ) → hook kể chuyện thiếu cái giá (r-c05-r1921 · L-104)
- Hiệp chê: «Lời văn sến, giả, không giống người nói» → hình ảnh văn chương («cả mâm cơm im bặt») (r-c05-r201 · L-105)
- Hiệp chê: «Script vẫn xàm thiếu tự nhiên, cả ai nói lý do nghe mới quê…» → hàn 3 ý bằng dấu phẩy, từ sách (r-c06-v3 · L-106)
- Hiệp chê: «…rời rạc… không có cấu trúc tuần tự gì rõ ràng» → không có bảng mạch (r-c06-v3r2 · L-107)
- Tầng 1 (chặn tuyệt đối): H1 fact không nguồn · H2 ≥ 300s · H3 sai brand/format kênh hoặc chê người xem · H4 lỗi cấu trúc. Tầng 2 so cặp Pairwise A/B với bản duyệt cùng chủ đề/format; khẩu ngữ tự nhiên không bị trừ.
- **Format:** 100% comic (Remotion `video-engine/`) + motion explainer (HyperFrames). Không quay mặt/b-roll, không nhạc nền (`rule-21`), không nhắc lịch đăng (`DL-028`), bắt buộc nhãn AI giọng (`rule-46`).
- **Độ dài (`L-099`, thay rule-4/7/61 cũ):** strict **< 300s** tính cả end card/nghỉ/xfade; mục tiêu **60–180s**. Clip cô đọng 60–119s không bị cảnh báo. Câu chuyện đã đủ ý thì dừng, không kéo chữ cho tới 120s. Không quota từ cứng, không tăng tốc giọng để nhét.
- **Tách cổng lời vs cổng hình (`L-098`):** **KHÔNG** sinh voice, ảnh, still preview hay render trước khi Hiệp **"Chốt"** đúng bản lời.
- Góp ý clip: «1» (2026-11-28 13:17)
- Góp ý clip: «hook quá tệ» (2026-11-28 14:04)
- Góp ý clip: «m có chia 3 lane script r chọn scrip tốt nhất khog, đảm bảo phải làm theo 100% /make-video» (2026-11-28 14:04)
- Góp ý clip: «vẫn tệ, m phải đọc toàn bộ cách làm của skills, cấm bỏ bất k2i bước nào» (2026-11-28 14:18)
<!-- GATE0-BRIEF:END -->

## Bản nháp của Writer C

**Writer C · `M5` Micro-Experiment / Before–After.** Hướng chuyện: `5-Second Moment` (Hiệp tự làm phép thử trên chính mình, người xem thấy ngay điện thoại úp + mắt liếc). Câu hỏi trung tâm: úp máy rồi, đầu óc có đỡ xao không? Hook và bằng chứng cùng trả lời câu này.

## Gate 0.5 — Hook Arena

Luật Hiệp: thấy điện thoại + cái liếc trong 3s đầu, không «câu đứt» trừu tượng, cấm khuôn «học năm phút là tay mò điện thoại». Hook M5 là Hiệp kể mình đã làm phép thử (không bảo người xem lật cái máy họ đang cầm xem TikTok).

| # | Mở đầu (b01) | Âm tiết | Thấy gì trong 3s | Chấm |
|---|---|---|---|---|
| H1 | Mình úp máy xuống bàn, ngồi viết mà mắt vẫn liếc cái lưng máy bốn lần. | 16 | Lưng điện thoại úp, bút chạy, mắt chibi Hiệp trượt qua máy, tick 1-2-3-4 | **Top 1**: có máy, có liếc, có con số tự đếm, là chuyện của mình (không ra lệnh người xem) |
| H2 | Màn hình tối thui, mình vẫn liếc cái điện thoại úp trên bàn hoài. | 14 | Điện thoại úp, đèn bàn, mắt liếc liên tục | **Backup**: gọn hơn, hết con số nên bớt «cú đếm» |
| H3 | Điện thoại úp rồi mà mắt mình cứ trượt qua nó, đếm thử mới biết. | 15 | Máy úp, mắt trượt, bảng đếm nhỏ | Loại: «đếm thử mới biết» hơi cụt, chưa có cảnh đang làm gì |
| H4 | Hôm qua mình ngồi đếm: máy úp sấp mà mắt liếc hết bốn lần. | 14 | Hiệp cầm bút đếm vạch bên lề giấy | Loại: «hôm qua ngồi đếm» kể lại, kém hiện tại bằng H1 |

Top 1 = H1, backup = H2. H1 ≤ 20 âm tiết (16). Số «bốn lần» là chi tiết dựng của cảnh (không phải số liệu nghiên cứu); cần Hiệp xác nhận hoặc đổi số theo chuyện thật.

## Bảng khung mạch

| Beat | Giây (ƯỚC) | Vai trò | Nội dung | Sóng cảm xúc |
|---|---|---|---|---|
| b01 | 0–5 | Hook phép thử | Hiệp úp máy, viết, đếm mắt liếc | Kéo vào, tò mò |
| b02 | 5–16 | Câu hỏi trung tâm | Máy úp, tắt tiếng, vẫn trượt mắt sang. Úp rồi sao đầu óc vẫn xao? | Bực nhẹ, vào đề |
| b03 | 16–29 | Dip + trước/sau | Máy sạc ngoài phòng viết một mạch; máy úp trên bàn viết câu nào liếc câu đó; cứ tưởng mình yếu ý chí | **Dip**: «đúng mình luôn» |
| b04 | 29–39 | Bằng chứng 1 | Nhóm Ward 2017, thí nghiệm đầu: máy im trên bàn làm bài nhớ tệ hơn máy phòng khác | Khựng, hóa ra có người đo |
| b05 | 39–49 | Bằng chứng 2 + rào | Thí nghiệm hai: tắt nguồn không đổi, chỗ để máy mới đổi; úp sấp là cảnh của mình | Nhẹ vai, rõ ranh giới |
| b06 | 49–61 | Đoán + bước tối nay | Mình đoán lưng máy vẫn kéo mắt (đoán); tối nay sạc máy ngoài phòng rồi coi đỡ xao hông | Có việc làm được |
| b07 | 61–73 | CTA DL-081 | Đây là cách của mình, đồng cảm «ai bị giống mình», hỏi cách mỗi người gỡ | Ấm, mời kể |

Sóng: kéo vào phép thử → Dip (thấy mình trong đó) → so sánh trước–sau → 1 bằng chứng chốt → 1 bước tối nay → hỏi cách mỗi người.

## Lời đọc

1. **[b01]** Mình úp máy xuống bàn, ngồi viết mà mắt vẫn liếc cái lưng máy bốn lần.
2. **[b02]** Máy úp sấp, tắt tiếng, hông rung hông sáng. Mình mới viết được hai dòng mà mắt đã trượt sang nó lần nữa. Úp rồi đó, sao đầu óc vẫn xao?
3. **[b03]** Hôm máy sạc ngoài phòng, mình viết một mạch hết trang. Hôm máy úp trên bàn thì viết câu nào liếc câu đó. Mình cứ tưởng tại mình yếu ý chí, tự trách hoài.
4. **[b04]** Nhóm Ward năm hai ngàn mười bảy cho người ta làm bài nhớ. Thí nghiệm đầu: máy của họ im trên bàn thì làm tệ hơn lúc máy nằm phòng khác.
5. **[b05]** Thí nghiệm thứ hai tắt nguồn luôn, kết quả hông đổi gì, chỉ chỗ để máy mới đổi. Úp sấp là cảnh của mình thôi, hông phải của thí nghiệm.
6. **[b06]** Mình đoán cái lưng máy vẫn kéo mắt mình, mà đó là mình đoán thôi nha. Tối nay mình thử sạc máy ngoài phòng, ngồi viết, rồi coi đầu óc đỡ xao hông.
7. **[b07]** Đây chỉ là cách của mình thôi, chắc mỗi người một kiểu. Có ai úp máy rồi mà mắt vẫn trượt qua giống mình hông? Bạn gỡ khúc đó sao, kể mình nghe với nha.

**Âm tiết (đếm từ, «2017» đọc «hai ngàn mười bảy» = 4):** b01 16 · b02 31 · b03 34 · b04 31 · b05 30 · b06 33 · b07 35 = **210** (trong 200–265). b01 = 16 ≤ 20; b01+b02 = 47 ≤ 65; beat dài nhất 35 ≤ 45; bằng chứng b04 31 và b05 30, đều ≤ 35. Ước ~72s.

## Bảng beat

Ký hiệu: `|` tách phrase, **nhấn** = từ nhấn giọng. EN ≤ 8 từ mỗi chunk.

| Beat | Giây | Lời thoại | Hình | EN |
|---|---|---|---|---|
| b01 | 0–5 | Mình **úp** máy xuống bàn, \| ngồi viết mà mắt vẫn **liếc** \| cái lưng máy **bốn** lần. | Cắt sát bàn frame 0: lưng điện thoại úp, bút chạy; mắt chibi Hiệp trượt qua máy, bốn tick hiện lần lượt | I flipped my phone face-down. \| Still glanced at it \| four times. |
| b02 | 5–16 | Máy úp sấp, tắt **tiếng**, \| hông rung hông sáng. \| Mình mới viết hai dòng \| mà mắt đã **trượt** sang nó. \| Úp rồi đó, \| sao đầu óc vẫn **xao**? | Màn hình gạch chéo chuông, trang giấy hai dòng; mắt trượt sang máy lần nữa; dấu hỏi nhỏ nổi trên đầu | Face-down, muted, no buzz. \| Two lines in, my eyes slid over. \| Face-down… \| so why am I distracted? |
| b03 | 16–29 | Hôm máy sạc **ngoài phòng**, \| mình viết một mạch hết trang. \| Hôm máy úp trên bàn \| thì viết câu nào **liếc** câu đó. \| Mình cứ tưởng tại mình \| yếu ý chí, tự **trách** hoài. | Chia đôi màn hình: trái trang giấy kín chữ, máy cắm sạc ngoài cửa; phải trang giấy chấm chấm, máy úp trên bàn, mắt liếc theo từng câu; Hiệp ôm trán | Phone charging outside: one full page. \| Phone face-down on desk: \| a glance per sentence. \| I blamed my willpower. |
| b04 | 29–39 | Nhóm **Ward** \| năm hai ngàn mười bảy \| cho người ta làm bài nhớ. \| Thí nghiệm đầu: \| máy của họ im trên **bàn** \| thì làm tệ hơn \| lúc máy nằm **phòng khác**. | Thẻ nguồn `WARD ET AL. 2017`; hai bàn chibi: bàn có điện thoại im, bàn không có máy (máy ở phòng bên); điểm bài bên có máy thấp hơn | Ward's group, 2017: \| a memory task. \| Phone silent on the desk, \| worse than phone in another room. |
| b05 | 39–49 | Thí nghiệm thứ **hai** \| tắt nguồn luôn, \| kết quả hông **đổi gì**. \| Chỉ **chỗ để máy** mới đổi. \| Úp sấp là cảnh của **mình** thôi, \| hông phải của thí nghiệm. | Nút nguồn tắt, điểm hai bên vẫn y như cũ; mũi tên chỉ sang vị trí máy; Hiệp giơ tay «cảnh của mình» (tag nhỏ: cảnh dựng, không phải thí nghiệm) | Second try: power off. \| Same result. \| Only where the phone sat mattered. \| Face-down is just my scene. |
| b06 | 49–61 | Mình **đoán** \| cái lưng máy vẫn kéo mắt mình, \| mà đó là mình đoán thôi **nha**. \| Tối nay mình thử \| **sạc máy ngoài phòng**, \| ngồi viết, \| rồi coi đầu óc đỡ **xao** hông. | Tag «MÌNH ĐOÁN» trên lưng máy; đêm, Hiệp cắm sạc máy ở ổ ngoài phòng khách, quay lại bàn, trang giấy trắng, bút sẵn | My guess: its back tugs my eyes. \| Just a guess! \| Tonight: charge it in another room, \| write, and see if my head quiets. |
| b07 | 61–73 | Đây chỉ là cách của **mình** thôi, \| chắc mỗi người một **kiểu**. \| Có ai úp máy rồi \| mà mắt vẫn trượt qua \| giống mình **hông**? \| Bạn gỡ khúc đó sao, \| **kể** mình nghe với nha. | Hiệp quay lại bàn đầu clip, máy úp, nghiêng đầu cười trừ; bong bóng chat trống chờ; tay khum sau tai lắng nghe | Just my way; everyone's different. \| Anyone else's eyes slide over \| even face-down? \| How do you handle it? \| Tell me. |

## Tự kiểm tiếng Việt

- **(a) Mùi Anh / Bắc trộn Nam / sai ngữ cảnh:** không có «ấy / thế / nhé»; dùng «hông / nha / hoài / coi / sao». «Úp sấp», «lưng máy» là cách nói đời thường. «Đỡ xao» đúng giọng Nam. Không có cụm dịch Anh. PASS.
- **(b) Ẩn dụ đúng hình ảnh, một họ:** chỉ một hình: mắt «trượt» sang máy (không trộn thêm ẩn dụ nào khác); «kéo mắt» nằm trong câu đoán, cùng họ hình. «Một mạch» là khẩu ngữ. PASS.
- **(c) Mốc và số tiến đúng chiều:** «bốn lần» (hook) → «hai dòng» (b02, cảnh dựng, không cạnh tranh số); bằng chứng không có số lớn/% (cấm), mốc duy nhất «hai ngàn mười bảy». Hai thí nghiệm đi theo thứ tự đầu → hai. PASS.
- **(d) Không điệp từ đầu–cuối cơ học, không hàn câu chiều checker:** b02 kết «xao», b03 mở «Hôm»; b03 kết «hoài», b04 mở «Nhóm»; b04 kết «phòng khác», b05 mở «Thí nghiệm»; b05 kết «thí nghiệm» chỉ là nhắc lại ranh giới, b06 mở «Mình đoán» (không lặp). «Nhóm Ward… cho người ta làm bài nhớ» tách câu khẩu ngữ. Không mở câu bằng Tại / Mà / Vậy / Nghĩa là / Nên / Còn. «Mà» chỉ xuất hiện giữa câu. PASS.

## Fact-lock

| Được nói (lời đọc) | Ở beat | Ghi chú |
|---|---|---|
| «Nhóm Ward năm hai ngàn mười bảy» (màn hình `WARD ET AL. 2017`) | b04 | Ward, Duke, Gneezy & Bos 2017, `doi:10.1086/691462`, qua Canale 2019 |
| Hai thí nghiệm; thí nghiệm đầu: máy im trên bàn → làm bài nhớ tệ hơn so với máy phòng khác | b04 | Đúng fact-lock: bài nhớ (OSpan), không nói Raven/IQ, không số, không cỡ mẫu |
| Thí nghiệm hai: tắt nguồn không đổi gì; chỗ để máy mới đổi | b05 | Đúng câu cho phép «Tắt nguồn không đổi gì» |
| «Úp sấp là cảnh của mình, hông phải của thí nghiệm» | b05 | Ranh giới bắt buộc: úp mặt là cảnh dựng |

- **Cảnh dựng (luật 67, không phải Ward):** Hiệp viết bài, «hai dòng», «bốn lần», «viết một mạch hết trang», «máy sạc ngoài phòng» là chi tiết hài của comic, không gán vào nghiên cứu. Số «bốn lần» và chuyện hai hôm viết cần Hiệp xác nhận hoặc đổi theo chuyện thật.
- **Đoán có đánh dấu:** «cái lưng máy vẫn kéo mắt mình» nói rõ «mình đoán thôi nha» (b06) + tag hình MÌNH ĐOÁN; nhóm Ward không đo cơ chế này trong lời đọc.
- **Việc tối nay:** «sạc máy ngoài phòng» là cách áp dụng mục 3.1 (máy ra khỏi tầm mắt), không phải số liệu; câu cuối b06 «coi đầu óc đỡ xao hông» là thử của Hiệp, không hứa kết quả.
- **Tuyệt đối không có trong lời:** «chứng minh», «khoa học khẳng định», IQ, dopamine, cortisol, «nghiện», số %/cỡ mẫu, Stothart, Wilmer, meta Böttger, «tắt thông báo / Focus Mode là kết quả Ward», «nhiều nghiên cứu».
- **CTA (DL-069, DL-081):** nhận đó là cách của mình → đồng cảm «ai bị giống mình» → hỏi cách mỗi người gỡ khúc đó. Không khảo sát «liếc mấy lần», không ép comment một chữ.

## Trả về cho điều phối viên (7 dòng đọc + âm tiết)

1. (16) Mình úp máy xuống bàn, ngồi viết mà mắt vẫn liếc cái lưng máy bốn lần.
2. (31) Máy úp sấp, tắt tiếng, hông rung hông sáng. Mình mới viết được hai dòng mà mắt đã trượt sang nó lần nữa. Úp rồi đó, sao đầu óc vẫn xao?
3. (34) Hôm máy sạc ngoài phòng, mình viết một mạch hết trang. Hôm máy úp trên bàn thì viết câu nào liếc câu đó. Mình cứ tưởng tại mình yếu ý chí, tự trách hoài.
4. (31) Nhóm Ward năm hai ngàn mười bảy cho người ta làm bài nhớ. Thí nghiệm đầu: máy của họ im trên bàn thì làm tệ hơn lúc máy nằm phòng khác.
5. (30) Thí nghiệm thứ hai tắt nguồn luôn, kết quả hông đổi gì, chỉ chỗ để máy mới đổi. Úp sấp là cảnh của mình thôi, hông phải của thí nghiệm.
6. (33) Mình đoán cái lưng máy vẫn kéo mắt mình, mà đó là mình đoán thôi nha. Tối nay mình thử sạc máy ngoài phòng, ngồi viết, rồi coi đầu óc đỡ xao hông.
7. (35) Đây chỉ là cách của mình thôi, chắc mỗi người một kiểu. Có ai úp máy rồi mà mắt vẫn trượt qua giống mình hông? Bạn gỡ khúc đó sao, kể mình nghe với nha.

Tổng **210** âm tiết.
