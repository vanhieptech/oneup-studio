---
title: "Arena Writer B (M2 — 5-Second Vulnerable Story (Tâm sự khoảnh khắc thật 5 giây))"
date: 2026-11-27
id: arena.writer-b-m2
type: draft
status: draft
source: "oneup-studio (script-arena.py, HTB 3.5)"
updated: 2026-11-27
tags: [arena, script-draft, m2]
---
# Đấu trường Kịch bản — Writer B (`M2`: 5-Second Vulnerable Story (Tâm sự khoảnh khắc thật 5 giây))

> **LỆNH PHA 1 (PURE VOICE PASS — `DL-079`):** Đọc 2–3 clip duyệt gần nhất để thấm nhạc điệu miền Nam xưng mình–bạn, rồi viết liền 1 hơi sống động theo đúng phương pháp dưới đây. **Không mở bảng cấm từ trong lúc viết.** Sau khi viết xong mới sang Pha 2 kiểm Fact-lock & âm tiết (`200–265` âm tiết, `b01 ≤ 20`, mỗi beat `≤ 45`).

- **Phương pháp được khóa:** `M2` — 5-Second Vulnerable Story (Tâm sự khoảnh khắc thật 5 giây) (*gần gũi · chân thật · tự giễu nhẹ*)
- **Cách mở Hook:** Mở thẳng vào 1 khoảnh khắc thật hơi chạnh hoặc tự giễu của chính Hiệp trong 5 giây đầu.
- **Đường cong cảm xúc bắt buộc (`Emotional Wave`):** Tự giễu gần gũi → Tự trách âm ỉ (Dip) → Thử nhiều cách vẫn vấp → Lật góc nhìn bằng 1 bằng chứng → Nhẹ gánh → Rủ bạn kể chuyện
- **Mẫu duyệt gợi ý nghe nhịp:** a-c01, a-c04
- **Trend/Bối cảnh đang nóng (< 72h):** Sếp nhắn đúng hai chữ 'em ơi' rồi im luôn — áp lực canh chấm đỏ tin nhắn cả ngày (B-msg-02) (dùng làm xương sống ẩn dụ ngay Hook, cấm câu meta «dạo này có câu trend nói»)

## Fact-lock dùng chung (tuyệt đối không vượt ngoài khối này — H1)

---
title: "clip-07 fact lock — Kushlev & Dunn 2015 (HTB 3.5)"
date: 2026-11-27
id: clip-07.fact-lock
type: research
status: locked
updated: 2026-11-27
tags: [clip-07, fact-lock, kushlev-2015, htb-3.5]
source: "HowToLiveBetter 3.5 + Kushlev & Dunn (2015), Computers in Human Behavior 43:220-228, doi:10.1016/j.chb.2014.11.005"
---

# clip-07 fact lock

Nguồn kiểm: HowToLiveBetter mục `3.5` + bài gốc Kushlev & Dunn (2015), *"Checking email less frequently reduces stress"*, *Computers in Human Behavior* 43, 220–228 (`doi:10.1016/j.chb.2014.11.005`, bằng chứng mức B). Lời thoại chỉ được nói trong khung dưới.

| Được nói | Cấm |
|---|---|
| Kushlev & Dunn 2015 (`doi:10.1016/j.chb.2014.11.005`); lời đọc «nhóm Kushlev năm 2015», màn hình `KUSHLEV & DUNN 2015` | «chứng minh», «nhiều nghiên cứu», «khoa học khẳng định» |
| 124 người lớn, 2 tuần tự so với chính mình: tuần gom còn 3 lần/ngày (dù thực tế chỉ kéo xuống tầm 4–5 lần) vs tuần thả cửa (trung bình ~15,5 lần/ngày — có thể nói gọn «hơn 15 lần») | Bịa thêm số % giảm stress hoặc % tăng năng suất |
| Căng thẳng hằng ngày giảm rõ ở mức vừa-nhỏ (`d = 0,37`), trong khi lượng email nhận và trả lời vẫn y như cũ | Nói «hết stress», «tăng gấp đôi năng suất», «làm việc hiệu quả hơn hẳn» (nghiên cứu đo căng thẳng, không đo năng suất) |
| Rào giới hạn (≤ 1 vế ngắn): mới đo trên email (chưa đo trực tiếp chat/tin nhắn tức thời), một nghiên cứu, mức giảm vừa phải | Gán kết quả đo trực tiếp cho Zalo/Slack/tin nhắn mà không rào «đo trên email» |
| Không bịa cơ chế não; chỉ nói đúng trải nghiệm «cứ mở ra đóng vô / canh chấm đỏ khiến đầu căng» | Cơ chế não ngoài nguồn: dopamine, cortisol, tuyến thượng thận, sóng não |
| 3 khung giờ (9h sáng, 1h trưa, 4h chiều) + câu báo team «việc gấp thì gọi» = gợi ý áp dụng 3.5 (luật 67), không phải số liệu nghiên cứu | Nói bệnh lý (rối loạn giấc ngủ, trầm cảm, lo âu lâm sàng) |

<!-- GATE0-BRIEF:BEGIN (pipeline/scripts/gate0.py) -->
## Gate 0 brief (@hi.oneup)

### 1. Ý tưởng đã chọn + fact package
- [idea-bank] Check tin nhắn 3 khung giờ, việc gấp thì gọi (B-msg-02) | 3.5 | trụ 2 tập trung | "Sếp nhắn đúng hai chữ “em ơi” rồi im luôn. Bạn mở điện thoại ra coi lại mấy lần?" | LIGHT | stub 2026-10-19, chờ duyệt (clip-08 hook thay thế; `research/trends/2026-10-19/plans/plan-2-check-tin-nhan-3-lan.json`)
- [idea-bank] Sáng se lạnh: ra khỏi chăn trước, gom tin nhắn mở ba lần một ngày (B-dotlanh-01) | 3.5 | trụ 2 tập trung | "Miền Bắc sắp se lạnh rồi. Sáng mai thử ra khỏi chăn trước, rồi mới mở tin nhắn, mà mở đúng ba lần trong ngày thôi." | LIGHT | stub 2026-10-28, chờ duyệt (clip-07 hook trend; `research/trends/2026-10-28/plans/plan-1-dot-lanh-gom-tin-nhan.json`)
- [idea-bank] AI ước dư, người ước thiếu: ước theo lần trước (B-estimate-02) | 4.4 | trụ 1 | "AI ước hai tuần mà làm hai tiếng. Còn bạn, lần gần nhất ước ba ngày thì mất mấy ngày?" | DARK | ý tưởng (2026-10-20; clip-05 hook thay thế)
- Fact package: chưa có (`research/explainers/<chủ-đề>.md`); mọi số liệu cần claim → nguồn trước khi viết (H1).

### 2. Mạch cốt truyện
- **Phương pháp dẫn chuyện (Archetype `M2`):** 5-Second Vulnerable Story (Tâm sự khoảnh khắc thật 5 giây) — màu sắc: *gần gũi · chân thật · tự giễu nhẹ*
  - Cách mở Hook: Mở thẳng vào 1 khoảnh khắc thật hơi chạnh hoặc tự giễu của chính Hiệp trong 5 giây đầu.
  - Đường cong cảm xúc (`Emotional Wave`): Tự giễu gần gũi → Tự trách âm ỉ (Dip) → Thử nhiều cách vẫn vấp → Lật góc nhìn bằng 1 bằng chứng → Nhẹ gánh → Rủ bạn kể chuyện
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
- Story bank S-02 oneup-2h: Tự làm OneUp + Omi một mình, khoảng 2h/ngày sau giờ làm (cần Hiệp xác nhận + chi tiết)
- Story bank S-04 tiktok-zero: Mở kênh TikTok từ 0 follower (cần Hiệp xác nhận + chi tiết)
- **Giọng Hiệp (`content/voice-profile.md` §2, bắt buộc):** miền Nam nhất quán, xưng mình–bạn; cấm trộn chữ Bắc «ấy / thế / nhé» cạnh «hông / nha / nè». Có chủ thể/ngữ khí trò chuyện ngay câu đầu (không mở bằng châm ngôn cụt chủ ngữ); đọc lên phải giống tin nhắn thoại gửi bạn thân.
- **Kiến trúc 2 Pha chống Prompt Bloat (DL-079, `docs/prompts/writer-hi-oneup.md`):** **Pha 1 (Pure Voice)** học nhạc điệu từ 2–3 mẫu duyệt gần nhất, viết liền 1 hơi sống động trước (không mở bảng cấm). **Pha 2 (Surgical Audit)** mới kiểm Fact-lock, ngân sách âm tiết, tách Beat có đánh dấu `**nhấn**` mỗi câu — chỉ sửa vi phẫu từ vi phạm, cấm gọt phẳng khẩu ngữ.
- **Ngân sách nguyên liệu (Anti-Stuffing Budget, DL-077..079):** không phải checklist điền đủ.
  - **Đúng 1 nỗi đau đại chúng** · **Đúng 1 câu hỏi trung tâm** · **6–7 beat, ~200–265 âm tiết (~65–88s)** (`b01` ≤ 20 âm tiết rõ nghĩa trong 3s đầu, `b01+b02` ≤ 65, beat ≤ 45; `audio-precheck.py` cảnh báo `HOOK_LONG` / `SLOW_ENTRY` / `BEAT_BLOAT`).
  - **Bằng chứng ≤ 35 âm tiết (Storytelling the Study + Climactic Order):** dẫn từ kỳ vọng sai → cú tỉnh ngộ (không nhảy kiểu Wikipedia), đặt **số nhỏ trước → số lớn gây bất ngờ cuối câu** (`18 → 254 ngày, hơn 8 tháng`), dịch nghĩa số lớn, bỏ cỡ mẫu/số tuần/món phụ khỏi lời đọc; rào giới hạn ≤ 1 vế ngắn; gia vị giọng chọn **tối đa 1–2 thứ** tự nhiên.
  - **Đủ ý & Khép vòng + CTA chia sẻ đồng hành + Thought-Flow over Connector-Glue (DL-069, DL-080, DL-081):** giải tỏa nỗi lo ở Hook **ngay sau số liệu**, có 1 đổi thước đo + 1 hành động cụ thể; CTA phải **đồng cảm («ai bị giống mình») + lắng nghe góc nhìn/cách mỗi người vượt qua khúc dễ nản**, **cấm khảo sát xã giao sáo rỗng («bạn đang tập gì, được bao lâu») & cấm ép «comment 1 chữ»**; cấm mở câu rập khuôn `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`, cấm câu meta «dạo này có câu trend nói» hay cảnh giả «lướt trúng câu đang trend»; trend là xương sống ngay Hook hoặc xin ngoại lệ như `DL-069`.
  - **Given–New Conceptual Flow + 4 hướng dẫn chuyện (`docs/research/storytelling-craft-guide.md`, DL-078/079):** chọn 1 hướng ở Gate 0 (`Misconception Reveal` · `Everyday Paradox` · `5-Second Moment` · `Self-Dialogue`); nối bằng tâm lý/tình huống ngầm (**CẤM điệp từ cuối–đầu cơ học Anadiplosis** kiểu `còn đó → Công còn đó`); Đề–Thuyết tự nhiên, 1 họ ẩn dụ duy nhất, không từ lệch nghĩa.
- Chuyện thật từ `content/story-bank.md` (`[CẦN HIỆP XÁC NHẬN]` nếu chưa chốt), không bịa kết quả.
- **Chỉ nạp 4 thứ khi viết nháp v1/v2:** (1) brief này (Gate 0 + Fact-lock + trend); (2) `content/voice-profile.md` §2–3; (3) 2–3 bản đã duyệt gần thể loại nhất: a-c02 `content/archive/clip-02-procrastination-discomfort/final/script-final.md`, a-c03 `content/archive/clip-03-big-task-chunking/final/script-final.md`, a-c04 `content/archive/clip-04-gap-sach-tu-kiem/final/script-v18-LOCKED.md`; (4) dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md` nếu có. Không nạp `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv`, style-pairs vào bước viết; các bảng đó chỉ cho `check-rules.py --audit` sau khi lời đã xong.
- **Fact-lock:** ghi danh sách số/kết luận được phép nói và danh sách CẤM (từ/số bị cấm, cơ chế não ngoài nguồn) trước khi viết; chạm vào danh sách cấm = H1. **Single-Point Alignment:** chọn 1 câu hỏi trung tâm; hook và bằng chứng là câu hỏi và câu trả lời của cùng câu đó.
- **Nhịp thực tế của 5 clip đã duyệt** (đo từ file, không phải khuôn liệt kê): học độ dài beat + cách chuyển ý + giọng, không chép câu.
  - a-c01: tự giễu + ví dụ đời thường: «mai học» của chính Hiệp, kế hoạch nếu–thì cụ thể, trả lời tuần tự
    12 beat · 201 âm tiết · TB 16.8 âm tiết/beat · 21 câu · beat: b01 9, b02 11, b03 13, e01 21, e02 18, e03 12, e04 15, e05 23, e06 19, e07 22, b11 17, b12 21
  - a-c02: khung «bản chất» + meme đời thường: hook thầy hỏi bản chất, 3 dấu hiệu, 1 con số Steel, gọi lại clip-01 ← mẫu gần nhất, mở đọc
    11 beat · 212 âm tiết · TB 19.3 âm tiết/beat · 26 câu · beat: b01 4, b01b 10, b02 9, b03 18, b05 23, b06 26, b07 35, b08 29, b09 20, b09c 22, b10 16
  - a-c03: hook câu hỏi mở + chia nhỏ vật lý: việc to thành vài việc cầm được, hai nghiên cứu ngắn, ví dụ dọn phòng/ôn thi ← mẫu gần nhất, mở đọc
    10 beat · 298 âm tiết · TB 29.8 âm tiết/beat · 21 câu · beat: b01 17, b02 26, b03 27, b04 41, b05 47, b06 24, b07 37, b08 26, b09 24, b10 29
  - a-c04: kể chuyện khép vòng: mở bằng chuyện học tối qua sáng quên, đi một mạch, chốt đúng nỗi đau mở đầu ← mẫu gần nhất, mở đọc
    8 beat · 187 âm tiết · TB 23.4 âm tiết/beat · 13 câu · beat: Hook 21, Ví dụ 31, Nguyên nhân 29, Mục tiêu 14, Cách làm 31, Bằng chứng 27, Kết quả 19, CTA 15
  - a-c05: giọng miền Nam + miếng hài nhập vai: «hà / nè / hông», thí nghiệm có số rõ, câu rào giới hạn, cú hài ghi sổ đầu bài
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
- Góp ý clip: «1» (chọn Phương án 1: Slot #7 Tuần 2 LIGHT — 3.5 Check tin nhắn theo đợt 3 lần/ngày, Pain-Wave công sở B-msg-02) (2026-11-27 23:33)
<!-- GATE0-BRIEF:END -->

## Gate 0.5 — Hook Arena

4 mở đầu theo 4 góc cho `clip-07` (xương sống nỗi đau `B-msg-02`, chọn Top 1 đúng chất `M2`):

1. **Góc 1 — Tự giễu khoảnh khắc thật (`M2` · Chọn Top 1):**
   «Sếp nhắn đúng hai chữ “em ơi” rồi im luôn — mười phút mình mở máy coi năm lần.» *(18 âm tiết · rõ tình huống ngay 3 giây đầu, có cái giá cụ thể & tự giễu nhẹ)*
2. **Góc 2 — Cận cảnh thói quen lén coi:**
   «Tin nhắn “em ơi” chưa thấy gõ tiếp, mà mình đã mở màn hình lên xuống chục bận.» *(18 âm tiết)*
3. **Góc 3 — So sánh đời thường:**
   «Người ta chờ tin người yêu, còn mình ngồi canh chấm đỏ từ chữ “em ơi” của sếp.» *(18 âm tiết)*
4. **Góc 4 — Nghịch lý nhẹ:**
   «Chưa biết sếp dặn gì, mới hai chữ “em ơi” thôi mà tim mình đã chạy deadline trước.» *(19 âm tiết)*

**Chốt Top 1:** Góc 1 — đi thẳng vào 1 khoảnh khắc ai đi làm cũng thấy mình trong đó, không mở bài chung chung, không nhắc chữ «trend».

---

## Bảng khung mạch + Đường cong Cảm xúc

- **Phương pháp:** `M2` — 5-Second Vulnerable Story (*gần gũi · chân thật · tự giễu nhẹ*).
- **Câu hỏi trung tâm (Single-Point Alignment):** Canh tin nhắn liền tay vậy, mình đỡ trễ việc hay chỉ tự làm đầu căng thêm?
- **Ngân sách âm tiết:** 7 beat · **234 âm tiết đọc** (~75–82s tốc độ tự nhiên 2.9–3.1 âm tiết/s, `b01` = 18, `b01+b02` = 53, beat dài nhất = 38).
- **Ghi chú luật 67 (chi tiết dựng / gợi ý áp dụng):** Tình huống sếp nhắn «em ơi» và thói quen canh chấm đỏ là chi tiết dựng minh họa nỗi đau `B-msg-02`; 3 khung giờ (9 giờ sáng, 1 giờ trưa, 4 giờ chiều) và câu báo team «việc gấp thì gọi nha» là gợi ý áp dụng mục 3.5, không phải số liệu nghiên cứu.

| Beat | Giây ước | Vai trò | Đường cong Cảm xúc (Emotional Wave) | Âm tiết đọc |
|---|---|---|---|---|
| b01 | 0–6s | Hook 5 giây | **Tự giễu gần gũi:** mở thẳng vào cảnh sếp nhắn «em ơi» rồi im, 10 phút mở máy 5 lần | 18 |
| b02 | 6–17s | Nỗi đau lặp + tự trách | **Vulnerability Dip:** ngày thường cũng bị chấm đỏ kéo tay, tối mệt mà việc còn nguyên, tự trách mình dễ phân tâm | 35 |
| b03 | 17–28s | Thử cách cũ vẫn vấp + câu hỏi | **Bế tắc nhẹ → Tò mò:** tắt chuông vẫn lén coi vì sợ lỡ việc gấp; đặt đúng 1 câu hỏi trung tâm | 34 |
| b04 | 28–39s | Bằng chứng (Fact-lock) | **Lật góc nhìn:** Kushlev & Dunn 2015 (đo trên email), Climactic Order `3 lần` vs `hơn 15 lần` → căng thẳng giảm rõ mức vừa phải | 35 |
| b05 | 39–49s | Giải tỏa + bẻ thước đo | **Nhẹ gánh:** lượng email nhận/trả lời vẫn y như cũ; gỡ nhãn tự trách «mình yếu» | 36 |
| b06 | 49–60s | Cách làm cụ thể | **Chủ động & gọn:** báo team «việc gấp thì gọi nha», gom tin nhắn đúng 3 khung giờ 9h / 1h / 4h | 38 |
| b07 | 60–72s | Khép vòng + CTA đối thoại | **Khiêm tốn & đồng hành:** hạ cái tôi, đồng cảm «có ai cũng hay canh chấm đỏ giống mình hông?», mời kể cách xử lý | 38 |

---

## Đọc liền một mạch

Sếp nhắn đúng hai chữ “em ơi” rồi im luôn — mười phút mình mở máy coi năm lần.

Hông riêng bữa đó đâu. Ngày thường cứ thấy chấm đỏ là tay mình tự chụp máy. Tối về đầu nặng trịch, việc chính còn nguyên, mình lại tự trách sao dễ phân tâm quá.

Tắt chuông cũng thua. Mình vẫn lén bật màn hình coi, sợ việc gấp người ta kiếm hông ra. Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ căng đầu thêm?

Nhóm Kushlev năm 2015 đo trên email nè: tuần gom còn 3 lần một ngày, so với thả cửa hơn 15 lần, căng thẳng giảm rõ mức vừa phải.

Số email nhận với trả lời vẫn y như cũ. Nghe vậy tự nhiên nhẹ hẳn cái vai — hóa ra mình hông yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căng hà.

Từ đó mình đổi luật: báo trước với team “việc gấp thì gọi nha”. Còn tin nhắn cứ gom đúng 3 khung giờ — 9 giờ sáng, 1 giờ trưa, 4 giờ chiều — mở một lượt rồi xử gọn.

Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi khác. Có ai cũng hay canh chấm đỏ giống mình hông? Hay bạn nghĩ sao, có cách gì né cảnh đó — comment kể mình nghe với nha.

---

## Bảng Beat (chỉ text, chưa render)

| Beat | Lời thoại (in **đậm** đúng 1 từ nhấn mỗi câu) | Ý hình | Caption EN (≤ 8 từ/chunk) |
|---|---|---|---|
| b01 | Sếp nhắn đúng hai chữ “em ơi” rồi im luôn — mười phút mình mở máy coi **năm** lần. | Comic cận mặt Hiệp nhìn màn hình hiện đúng bóng chat “em ơi”, đồng hồ nhảy 10 phút, tay bật tắt máy 5 nhịp liên tiếp. | Boss texts "hey" then ghosts. / I checked five times in ten minutes. |
| b02 | Hông **riêng** bữa đó đâu. Ngày thường cứ thấy chấm đỏ là tay mình tự **chụp** máy. Tối về đầu nặng trịch, việc chính còn nguyên, mình lại tự **trách** sao dễ phân tâm quá. | Comic chia nhịp: chấm đỏ bật lên tay tự với theo; chuyển cảnh tối muộn, đèn bàn sáng, danh sách việc chính còn trắng tinh, Hiệp ôm trán thở dài. | Not just that day. / Red dot pops, I grab my phone. / Exhausted at night, blaming my focus. |
| b03 | Tắt chuông cũng **thua**. Mình vẫn **lén** bật màn hình coi, sợ việc gấp người ta kiếm hông ra. Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ **căng** đầu thêm? | Comic biểu tượng chuông gạch chéo mà tay Hiệp vẫn lén chạm màn hình; dấu hỏi lớn tách hai vế “đỡ trễ việc” vs “căng đầu thêm”. | Muting fails too. / I still peek, fearing missed urgent pings. / Faster work, or just more stress? |
| b04 | Nhóm Kushlev năm 2015 đo trên email nè: tuần gom còn 3 lần một ngày, so với thả cửa hơn **15** lần, căng thẳng giảm rõ mức vừa phải. | Motion thẻ nguồn `KUSHLEV & DUNN 2015` + nhãn nhỏ `đo trên email`; hai cột so sánh bật theo thứ tự `3 lần/ngày` rồi vọt lên `>15 lần/ngày`, thanh căng thẳng hạ rõ ở mức vừa phải. | Kushlev 2015 tested this on email: / 3 checks vs over 15 a day. / Stress dropped noticeably. |
| b05 | Số email nhận với trả lời vẫn y như **cũ**. Nghe vậy tự nhiên **nhẹ** hẳn cái vai — hóa ra mình hông yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căng hà. | Motion hai chồng thư đến/đi giữ nguyên chiều cao; chuyển lại comic Hiệp thả lỏng hai vai, nhãn tự trách “yếu” bị gạch nhẹ đi. | Emails received and replied stayed the same. / Instant relief. / Not weak—just constant switching. |
| b06 | Từ đó mình đổi luật: báo trước với team “việc gấp thì **gọi** nha”. Còn tin nhắn cứ **gom** đúng 3 khung giờ — 9 giờ sáng, 1 giờ trưa, 4 giờ chiều — mở một lượt rồi xử gọn. | Comic Hiệp gửi một tin ngắn cho team có biểu tượng điện thoại; chuyển thanh thời gian ngày gọn với đúng 3 mốc sáng bật: `9:00` · `13:00` · `16:00`. | New rule: tell the team to call. / Batch messages at 9, 1, and 4. |
| b07 | Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi **khác**. Có ai cũng hay **canh** chấm đỏ giống mình hông? Hay bạn nghĩ sao, có cách gì né cảnh đó — comment **kể** mình nghe với nha. | Comic Hiệp gập máy đặt sang bên, vai thả nhẹ, nghiêng đầu nhìn người xem thân thiện, bong bóng trò chuyện mở chờ câu chuyện. | Just my workaround; every workplace differs. / Anyone else glued to red dots? / How do you handle it? Tell me. |

---

## Lời đọc (checker input)

1. **[b01 · hook tự giễu]** Sếp nhắn đúng hai chữ “em ơi” rồi im luôn — mười phút mình mở máy coi năm lần.
2. **[b02 · vulnerability dip]** Hông riêng bữa đó đâu. Ngày thường cứ thấy chấm đỏ là tay mình tự chụp máy. Tối về đầu nặng trịch, việc chính còn nguyên, mình lại tự trách sao dễ phân tâm quá.
3. **[b03 · thử cách cũ + câu hỏi]** Tắt chuông cũng thua. Mình vẫn lén bật màn hình coi, sợ việc gấp người ta kiếm hông ra. Ủa mà canh liền tay vậy, mình đỡ trễ việc hay chỉ căng đầu thêm?
4. **[b04 · bằng chứng]** Nhóm Kushlev năm 2015 đo trên email nè: tuần gom còn 3 lần một ngày, so với thả cửa hơn 15 lần, căng thẳng giảm rõ mức vừa phải.
5. **[b05 · nhẹ gánh + bẻ thước đo]** Số email nhận với trả lời vẫn y như cũ. Nghe vậy tự nhiên nhẹ hẳn cái vai — hóa ra mình hông yếu, chỉ tại mở ra đóng vô cả ngày nên đầu căng hà.
6. **[b06 · cách làm 3 khung giờ]** Từ đó mình đổi luật: báo trước với team “việc gấp thì gọi nha”. Còn tin nhắn cứ gom đúng 3 khung giờ — 9 giờ sáng, 1 giờ trưa, 4 giờ chiều — mở một lượt rồi xử gọn.
7. **[b07 · khép vòng + CTA đối thoại]** Mình gỡ kiểu đó thôi, chứ mỗi chỗ làm mỗi khác. Có ai cũng hay canh chấm đỏ giống mình hông? Hay bạn nghĩ sao, có cách gì né cảnh đó — comment kể mình nghe với nha.

---

## Tự kiểm ngữ nghĩa tiếng Việt (a–d)

- **(a) Đề–Thuyết & mạch tư duy:** Mỗi beat đi đúng một chuyển động tâm lý tự nhiên (tự giễu 5s → tự trách âm ỉ → thử tắt chuông vẫn vấp → lật bằng số liệu → nhẹ gánh gỡ tự trách → 3 khung giờ → hỏi chuyện đồng cảm). Không nhảy cóc, không điệp từ cuối–đầu cơ học (Anadiplosis), 0/7 beat mở bằng keo từ nối (`Tại/Mà/Vậy/Nghĩa là/Nên`).
- **(b) Giọng miền Nam & nhịp khẩu ngữ:** Xưng `mình – bạn` nhất quán; dùng từ đệm miền Nam tự nhiên (`hông, nè, hà, nha`) và khẩu ngữ đời thường (`bữa đó, chụp máy, mở ra đóng vô, chỗ làm, xử gọn`), không lẫn chữ Bắc (`ấy, thế, nhé`), không hình ảnh văn chương sến. Nhịp câu xen ngắn–vừa–dài (18 / 5–12–18 / 4–15–15 / 35 / 11–25 / 14–24 / 11–10–17).
- **(c) Fact-lock (H1) & luật 67:** Khóa chặt Kushlev & Dunn 2015 («nhóm Kushlev năm 2015»), đặt Climactic Order (`3 lần` → `hơn 15 lần`), giữ đúng kết luận «căng thẳng giảm rõ mức vừa phải» và «số email nhận với trả lời vẫn y như cũ», rào gọn 1 vế «đo trên email nè». Không dùng từ cấm («chứng minh», «nhiều nghiên cứu», dopamine/cortisol, «tăng năng suất», bệnh lý). Tình huống sếp nhắn «em ơi» và gợi ý 3 khung giờ (9h/1h/4h) + «việc gấp thì gọi» được ghi chú đúng luật 67.
- **(d) Ngân sách âm tiết & CTA (DL-081):** Tổng 234 âm tiết đọc (trong khung 200–255), `b01` = 18 (≤ 20), `b01+b02` = 53 (≤ 60), mọi beat ≤ 38 (≤ 42). Beat cuối `b07` tách riêng CTA đối thoại thật: hạ cái tôi + đồng cảm + mời kể cách xử lý, không khảo sát sáo rỗng, không ép comment 1 chữ.
