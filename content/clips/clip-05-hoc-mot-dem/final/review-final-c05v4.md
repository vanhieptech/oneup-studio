# Rule Reviewer: cổng final clip-05 v4, vòng 2 (bản nền xám), 26/10/2026 13:45 giờ VN (UTC+7)

Chấm lại từ đầu trên bản render cuối `e9a1a5b` (index `0d9965e`). Vòng chấm ngày 22/10 bị ngắt giữa chừng nên bỏ, không dùng kết quả cũ.
Frame và số đo của vòng này nằm ở `/workspace/review-c05/final2/r3/`.

## Kết luận: **CHƯA ĐẠT**, chỉ vì bản Reels
- **Bản TikTok đạt hết luật.** Gồm `clip-05-v4-tiktok.mp4`, `cover.png` và `post.md` phần TikTok.
- **Bản Reels** (`clip-05-v4-reels.mp4`, dùng cho Reels, Shorts và Threads) có 3 lỗi chặn, R1–R3. News sửa, chỉ ở bản Reels.
- Không phải sửa giọng, lời, bản TikTok hay bìa.

## 0. Trạng thái file (so với `0d9965e`)
- Từ `0d9965e` tới HEAD chỉ có 2 commit trend (`445c37b`, `c156bce`), không đụng clip-05.
- File đã commit của clip-05 không đổi.
- `git ls-remote origin main` = `0d9965e` ✓. Box đang đi trước origin 2 commit trend; Social Research/News push khi Mac online.
- Mọi file trong `final/` có mtime 23/10/2026 18:21 giờ VN. Đó là lúc chép đồng bộ, không phải lúc render.

| File chưa commit | sha256 (12 ký tự đầu) | Ghi chú |
|---|---|---|
| `cover.png` | 8bdf6443c40e | Trùng byte `cover/cover-a.png`; md5 bf27abd3… khớp post.md |
| `cover/cover-a.png` | 8bdf6443c40e | Render template A |
| `cover-1080x1350.png` | e8315add53f7 | 1080×1350 |
| `contact-sheet.png` | 2bec28f0ed7f | 1770×1554 |
| `voice-track-c05v4.wav` | b3f933972ab1 | Giống `voice-only-c05v4.wav` (52b14825e1fc, rev5 `764c16d`) cả 18 câu (corr 1.0000, lệch 0), chỉ dài thêm 0,32s lặng cuối |

- Các mp4: tiktok 06a91f6c7d53, reels 6a92f06a03f9, light 97cb40fa449d.
- `final/out/` không còn trên box (thư mục bị gitignore, mất khi đồng bộ lại).
- Clip-04 có commit cover và contact sheet, nên News cần commit 4 ảnh trên của clip-05 (N2).

## 1. `check-rules.py --final --stt` (ASR_MODEL=medium float32)
Kết quả: 229 check, 1 ✖, 17 ⚠. Bản đầy đủ: `r3/check-rules-final-stt.txt`.
| Mục | Đánh giá |
|---|---|
| ✖ rule-4 thiếu `out/clip-05-final.mp4` | **Lỗi tool/môi trường.** `out/` bị gitignore và mất khi đồng bộ. Mình trỏ `out/clip-05-final.mp4` → `clip-05-v4-tiktok.mp4` (symlink tạm, đã xoá) rồi chạy `--final` lại: **208 check, 0 ✖, PASS**. Kết quả: rule-4 MP4 55,03s, 1080×1920 30fps H.264 High yuv420p bt709, −14,2 LUFS, peak −0,8 dBFS ✓ (`r3/check-rules-final-nostt-symlink.txt`) |
| ⚠ rule-46 STT b08 0,67 «Cô mang số hôm nha» | **Lỗi tool, giọng không đổi.** Chi tiết ở §2 |
| ⚠ rule-7 219 chữ · rule-58 b02a dài · rule-60 / L-031 tiểu từ · rule-41 không có từ English | Lời đã khoá (Chốt v4 23:01, L-072). «Comment» và «clip» có trong lời nhưng tool không đếm. Chấp nhận, như vòng 1 |
| ⚠ rule-42 ×8 (b03/b06 comic) | Đồ thị cột và dải lịch trên nền giấy, đúng visual plan. Tool chỉ nhìn engine. Chấp nhận |
| ⚠ L-006 b01a/b01b không có `phrases` | Giọng lấy từ voice-only đã chấm. Chấp nhận |
| ⚠ E1 c04/c14 0,12s | Chỗ ngậm phụ âm cuối, đã chấp nhận ở vòng giọng 1–3 |
| ⚠ L-013 2 commit chưa push | 2 commit trend, không phải clip-05 |
| ✔ L-033 layout collisions: none | **Không đúng cho Reels:** `layoutCheck.ts` chỉ chấm `plan-A` (layout TikTok), không biết ô phụ đề Reels. Đây là lỗ hổng tool khiến R1–R3 lọt qua (T1) |
| ✔ L-083, L-084, L-067, L-070, rule-53/54, L-020 | Đã kiểm tay lại ở dưới, khớp |

## 2. Giọng và b08/c18 «Comment»
- **Giọng trong MP4 = voice-only rev5.** So tương quan từng câu c01–c18 với `voice-only-c05v4.wav`:
  - TikTok: 0,9993–0,9999, lệch 0,000s ở cả 18 câu.
  - Reels: 0,9990–0,9998, lệch đúng +0,500s (khung cover).
  - Phần dư là SFX và ambience. Không có nhạc.
- **Nguyên nhân cảnh báo b08 0,67:** tool không nghe audio trong MP4 mà nghe file `video-engine/public/voice/c05v4-c18.wav`.
  - File này không phải đoạn rev5: tương quan tốt nhất với voice-only chỉ 0,20. Các câu khác như c16b, c09, c01a khớp 1,0000. Có thể là bản cắt cũ còn sót.
  - File dài 1,37s, dưới 1,5s, nên `stt_check.py` đệm thêm 0,6s lặng.
  - Whisper medium nghe file thô ra «Comment số hôm nha!». Khi đệm lặng thì ra «Cô mang số hôm nha», đúng con số 0,67.
- **Chạy lại STT medium float32 trên chính audio giao**, mỗi đoạn hai lần:

| Đoạn | Không prompt | Có prompt |
|---|---|---|
| voice-only 51,75–52,80 | «Comment số hôm nha!» | «Comment số hôm nha.» |
| tiktok.mp4 51,75–52,80 | «Comment số hôm nha!» | «Comment số hôm nha.» |
| voice-only c17+c18 49,5–53,03 | «Còn bạn, môn sắp thi còn cách mấy hôm? Comment số hôm nha!» | đúng |
| reels.mp4 52,25–53,30 | «Cô mang số hôm nha» | «Comment số hôm nha.» |

  - Audio Reels giống TikTok từng mẫu (corr 0,9998). Lệch kết quả chỉ do mép cửa sổ cắt, tức whisper không ổn định ở mép đoạn, không phải đọc sai.
  - Nghe trong ngữ cảnh cả câu thì đúng.
- **Kết luận b08:** lỗi tool. Giọng là bản rev5 Hiệp đã nghe, không cần làm lại. Việc cho tool ghi ở T2.
- Khoảng lặng giọng (silencedetect −40 dB, ≥0,25s): dài nhất 0,38s; c16→c17 (sau b07c) 0,26s, trong plan 0,40 ✓.
  - Trên MP4, đoạn lặng ≥0,6s duy nhất là end card 53,15–55,02s.
  - freezedetect (ngưỡng 0,01, ≥1,5s) chỉ bắt end card tĩnh 53,3–55,03s (thiết kế ~2s) ✓. Không có hình đứng dài giữa clip.

## 3. Thông số file
| File | Kích thước | Thời lượng | LUFS / peak |
|---|---|---|---|
| tiktok | 1080×1920 30fps H.264 High, AAC 48k mono | 55,033s (1651 frame) | −14,2 / −0,8 dBFS ✓ |
| reels | 1080×1920 | 55,54s (1666 frame) | −14,2 / −0,8 ✓ |
| light | 540×960 | 55,033s | −14,2 / −0,8 ✓ |

- **L-083:**
  - Reels mở bằng cover 15 frame (0,50s), SSIM ≥0,98. Frame 0 lệch trung bình chỉ 0,73/255 so với `cover.png` ✓.
  - TikTok frame 0 lệch 80,6/255, tức không có khung cover ✓.

## 4. Hình (frame ở `r3/tt/`, `r3/re/`; mỗi beat một frame)
- **Nền cảnh** (sau nén H.264 + grain): tường #E1E3DC, sàn #D0D0C7, sát #E4E4DF / #D2D1CA. Bìa #E4E4DD ✓ (H1).
- **Phụ đề:** chữ khoá ô mực ✓ (H2).
  - Quét 220 frame TikTok và 222 frame Reels (4 fps): **0 pixel cam #FF5A36 trong ô phụ đề**.
  - Cam chỉ còn ở đồ vật (đồng hồ cát, cột «đọc liền», chấm ôn, cờ), đúng màu accent của brand (L-050). Không phải lỗi.
- **EN chunk:** 24 chunk, dài nhất 7 từ ✓ (P-09).
  - b06: «Longer memory needs» / «wider gaps between reviews» ✓.
- **b02b «?»:** hiện lúc ~11,4s quanh (655–680, 720–770), cách xa tóc ✓.
- **b03 frame cuối (24,1s):** cột xám 210px, cột cam +2 ngày 208px (bằng xám).
  - Cột mực cao hơn xám ~6px, tức ~216px tính viền.
  - Cột cam lúc «ngay» (17,8s) cao 322px.
  - Cột mực ≤ cột đọc liền và > xám ✓ (F2 đã sửa).
- **End card 53,0–55,0s:**
  - Có «Thông tin tham khảo, không thay thế tư vấn chuyên gia».
  - Có 4 nguồn và «Trend: @ng__phanh · TikTok».
  - Credit nguyên văn: «Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/» ✓.
  - Không có câu nào ám chỉ tác giả bảo trợ ✓.
- **L-084 b01:** khung TikTok dựng bằng vật thể, chữ «Học 1 đêm mới hiểu sao…», @ng__phanh, share đếm tới 55,3K ✓.
  - Khớp dòng «Trend trong clip: b01…» trong `trend-signals.md` ✓.
- **(A) Nghi «minh» mất dấu ở 0:47–0:48 → BÁO NHẦM.**
  - Zoom bong bóng b07c TikTok ở 47,7 / 48,0 / 49,0s và Reels ở 48,6s: đều đọc rõ «mình **dễ nhớ ra** cách giải hơn.», dấu huyền nằm trên «mình» (`r3/zA-bubble-strip.png`).
  - Ghép 24 dòng `text` của spec được 219/219 chữ, khớp 100% `script-v4-LOCKED.md`.
  - Quét mọi chuỗi hiển thị trong spec: không chữ tiếng Việt nào mất dấu. Chỉ dính mã hex và ghi chú `link` tiếng Anh nội bộ. L-067 ✔.

## 5. (B) Bản Reels: ô phụ đề chạm nhân vật và đồ vật → **ĐÚNG MỘT PHẦN, có lỗi thật**
- Ô phụ đề Reels: phần trắng x 58–633, viền + bóng tới x 648, y 1006–1176 (2 dòng) hoặc 1006–1244 (3 dòng). Khớp luật layout Reels (x 60–640, y ≈1000–1240).
- Mặt (mắt, má, miệng) **không** bị che. Nhưng nhân vật x .79 vẫn bị kẹp giữa ô phụ đề bên trái và viền khung bên phải (x 1046).
- Bảng đo: `r3/reels-plate-scan.txt`, `r3/reels-plate-vs-head.txt`.

**R1. Ô phụ đề đè lên mép trái tóc Thầy.**
- Cách đo: tóc đen liền với bóng ô, không còn khe nền, ở x 650–655 trong 25–125 trên 178 hàng của ô.
- Các đoạn bị (giây tính theo file Reels):

| Beat | Giây trên Reels |
|---|---|
| b01b | 2,1–2,6 |
| b01c | 3,6–5,1 |
| b02a | 5,6–6,9 |
| b02b | 8,9–12,1 |
| b05a | 27,6–28,9 |
| b05c–d | 31,6–35,6 |
| b07b | 45,9–47,9 |
| b07c | 48,4–48,6 |
| b08 | 49,6, 50,9, 53,1 |

- Khe hở nhỏ nhất đo được là **0px** ở b01c, b02b, b05a, b07b, b07c.
- News ghi «hở 10–50px» ở b02b/b07b/b07c. **Mình đo lại không ra số đó.** Ở b02b 10,1s, tóc dính ô trên 124 hàng.
- Frame: `r3/zB-touch.png`, `r3/zB-more.png`, `r3/zB-plate-edge.png`.
- Luật: L-033 (va chạm), L-003 (phụ đề không đè nhân vật), rule-34.

**R2. Đồng hồ cát bị ô phụ đề che nửa trên.**
- b02a, Reels 5,6–8,4s: mép dưới ô cắt 38–50px bề ngang của đồng hồ cát.
- b05a, Reels 28,1–29,4s: mất nắp và nửa bầu trên. Frame: `r3/zB-hourglass-29.0.png`.
- Luật: L-033 (đồ vật dưới ô phải dời).
- Riêng b04 0:26 (sách) và b05c (sách, đồng hồ cát) đều nằm ngoài ô ✓. Phần này của báo động là nhầm.

**R3. Đầu Thầy bị viền khung phải cắt.**
- Ở b01b 2,1s, b05a 28,9s và b08 50,9–52,6s, tóc hoặc viền mặt chạy vào viền khung x 1046 trên 79–150 hàng. Khe hở 0px.
- Frame: `r3/zB-rightedge2.png`.
- b01c, b02b, b07b còn hở 20–23px. b07c chỉ hở 2px.
- Nguyên nhân: dời x .76 → .79 mà giữ nguyên cỡ nhân vật. Đầu rộng ~350–370px nên không còn chỗ cho cả hai bên.

**Gợi ý sửa (News quyết cách làm, chỉ trong `clip-05-reels-plan-v4.py`):**
- Thu nhỏ nhân vật trong Reels (cỡ ×0,85 quanh chân) và đặt x ≈ .80.
- Hoặc thu hẹp ô phụ đề Reels (right 440 → 480) rồi để x ≈ .77.
- Đồng hồ cát b02a/b05a: dời sang x ≥ 660 hoặc hạ xuống dưới y 1260.
- Điều kiện đạt: khe hở ≥ 16px với ô phụ đề **và** với viền phải ở mọi frame, đo lại bằng cùng script.

## 6. `post.md`
- **Số đo khớp ffprobe/ebur128:** 55,03s/1651, 55,54s/1666, −14,2 LUFS, −0,8 dBFS, 32,2 / 32,8 / 4,0 MB ✓.
- **Chữ và tiêu đề:** cover text 33 ký tự. Tiêu đề chung 60 ký tự, YouTube 65 (≤70) ✓.
- **Hashtag:** TikTok/Reels 4 (#hoctap #onthi #studytok #cachhoc), YouTube «#Shorts #hoctap #onthi», Threads 0 ✓.
- **Threads:** 496/500 ký tự, 1 câu hỏi ✓.
- **Credit, câu an toàn, nhãn AI:** credit nguyên văn và câu an toàn có ở cả 4 bản. Nhãn AI F5-TTS có, kèm hướng dẫn bật nhãn trên 4 nền tảng ✓.
- **Bảo trợ:** chỉ dòng tự soát T4 nhắc tới «bảo trợ», để phủ định. Không có claim nào ✓.
- **Cần sửa chữ sau khi sửa R1–R3 (N1):**
  - Dòng 33 «layoutCheck sạch» và dòng 212 «không chạm tóc» đang sai so với số đo. Ghi lại số đo thật.
  - Hai mục «Việc còn mở (chờ Hiệp quyết)» (cột mực b03, bìa sách xám) Rule Reviewer đã kết luận **đạt luật, không cần Hiệp** (vòng 1 §4). Chuyển sang «Đã chốt».

## 7. Phải sửa / việc còn lại
| # | Việc | Ai | Chặn? |
|---|---|---|---|
| R1–R3 | Bố cục nhân vật và đồng hồ cát trong bản Reels (§5). Render lại **chỉ bản Reels** (cover 0,5s giữ nguyên), không đổi giọng, lời hay TikTok | News | **Chặn** Reels/Shorts/Threads |
| N1 | Sửa 2 dòng sai và mục «chờ Hiệp quyết» trong post.md | News | Chặn cùng R1–R3 |
| N2 | Commit `cover.png`, `cover-1080x1350.png`, `cover/cover-a.png`, `contact-sheet.png`. Quyết `voice-track-c05v4.wav` (= voice-only + 0,32s) commit hay bỏ. Không commit `.env` | News | Không chặn |
| T1 | `layoutCheck.ts` / check-rules L-033 phải chấm cả `plan-reels.json` với ô phụ đề Reels (x 60–648, y 1000–1250) và viền khung x ≤ 1046 | News (tool) | Không chặn bản này |
| T2 | rule-46 STT nên cắt từ `voice-only` hoặc mix MP4 theo timing, thay cho `public/voice/*.wav` (c18 đang là bản cũ, corr 0,20). Không đệm lặng khi đoạn ≥1,0s | News (tool) | Không |

## Frame tiêu biểu (cho Hiệp)
- `/workspace/review-c05/final2/r3/re/cover-0.00.png`: khung đầu bản Reels = cover (L-083)
- `/workspace/review-c05/final2/r3/tt/b01a-0.2.png`: trend b01, nền xám, phụ đề ô mực
- `/workspace/review-c05/final2/r3/tt/b03-24.1.png`: b03 frame cuối, ba cột
- `/workspace/review-c05/final2/r3/tt/end-54.3.png`: end card
- `/workspace/review-c05/final2/r3/zB-more.png`: lỗi R1 (ô phụ đề đè tóc, đồng hồ cát b02a)

---

# Rule Reviewer: cổng final clip-05 v4, 22/10/2026 ~03:00 (giờ VN, UTC+7)

Chấm trên file xuất lại lúc 02:40–02:41: `clip-05-v4-tiktok.mp4` (md5 trùng `out/clip-05-final.mp4` render 02:38), `clip-05-v4-reels.mp4`, `clip-05-v4-light.mp4`. Bản xuất lúc 02:33 đã bị thay, không chấm.
Frame chấm nằm ở `/workspace/review-c05/` (1 frame/giây, cắt chi tiết). Kết quả check-rules ở `/workspace/review-c05/check-rules-final-stt.txt`.

## Kết luận: **CHƯA ĐẠT**. 4 lỗi chặn (F1–F4), 3 việc nhỏ nên sửa, 2 việc cần Hiệp quyết

## 1. Giọng vòng 4 (`764c16d`) và âm thanh trong MP4
- Chỉ đoạn 52,035–52,451s đổi so với vòng 3, phần còn lại giống từng mẫu ✓.
- /s/ của «số» (52,10–52,16): năng lượng trên 4 kHz −4,3 dB, «sau» −2,8, «sắp» −2,0 ✓ (trong khoảng −2…−6). Mức /s/ −19,1 dB, ngang «sau» −19,6 ✓. Hết xỉn.
- «số hôm» +2,38 dB so «Comment», +4,57 so «nha» ✓. Bước nhảy c18 0,345 ✓. STT medium 1,0 «Comment số hôm nha» ✓.
- Giọng trong MP4: so tương quan từng chunk với `voice-only-c05v4.wav` được 1,00 ở cả 18 chunk.
  - TikTok: lệch 0 ở c01–c16, **+0,60s ở c17–c18**.
  - Reels: lệch +0,512s (khung cover), c17–c18 +1,112s.
  - Không lẫn nhạc. SFX và ambience nhỏ hơn giọng (phần dư −8,5 dB). STT medium trên audio MP4 nghe đúng hết.
  - Ở end card, whisper bịa ra câu «Hãy subscribe…». Đây là lỗi ảo giác quen thuộc của whisper trên đoạn chỉ có ambience, không phải tiếng thật.
- −14,2 LUFS, peak −0,8 dBTP (luật ≤ −0,5) ✓. 1080×1920 30fps H.264 High bt709 ✓. Dài 55,63s / reels 56,13s ✓.

## 2. `check-rules.py --final --stt`: 225 check, 9 ✖, 17 ⚠
| Mục | Đánh giá |
|---|---|
| ✖ rule-32 post.md missing | **Thật.** Chỉ có `/workspace/voice-work/clip-05-v4-render/post/post.tpl.md`, chưa điền: `{THREADS}`, `{REELS}`, `{YT_TITLE}`, `{YT_DESC}`, `{TT}`, `{SSIM}`… còn để trống, `final/post.md` không tồn tại → **F1** |
| ✖ L-033 b02b qmark#4 che đầu Thầy (9637 px²) | Thật nhưng nhẹ. Dấu «?» ~10,5–11,8s chạm tóc → S1 |
| ✖ rule-46 STT b01a/b02b/b03a/b03b/b07c/b08×2 (0–0,35) | **Lỗi tool**, không phải lỗi giọng. Medium float32 trên chính audio MP4 các đoạn này ra đúng chữ (b01 «Bạn học dồn một đêm cho cả kỳ…», b02b, b03a–b, b07c, b08 «Comment số hôm nha»). Tương quan giọng 1,00. Tool cắt đoạn theo dòng caption, render log ghi «voice: 0 lines», nên đoạn cắt rỗng hoặc lệch và model nhỏ ra trống. Ghi bằng chứng theo L-068. |
| ⚠ rule-46 b03d 0,62 | Cùng lỗi tool |
| ⚠ rule-7 219 chữ, rule-58 b02a dài, rule-60 / L-031 tiểu từ | Lời đã khóa (Hiệp Chốt v4), chấp nhận |
| ⚠ rule-41 không có từ English mix | «clip», «Comment» có trong lời, tool không đếm. Chấp nhận |
| ⚠ rule-42 ×8 b03/b06 là comic chứ không phải motion graphics | Cảnh là đồ thị cột và dải lịch trên nền giấy, không nhân vật, đúng visual plan FLUX. Tool chỉ nhìn engine. Chấp nhận |
| ⚠ L-006 b01a/b01b thiếu `phrases` | Giọng lấy từ voice-only đã chấm, không qua prosody theo dòng. Chấp nhận |
| ⚠ E1 0,12s c04 / c14 | Chỗ ngậm phụ âm cuối -p/-ch (vòng 1–3). Chấp nhận |
| ⚠ L-013 10 commit chưa push | Báo Hiệp, push khi Mac online |

## 3. Cổng tay
- Lời trong bong bóng (24 dòng): khớp **100%** 219 chữ của `script-v4-LOCKED.md` ✓. Chính tả đúng.
- Phụ đề EN: 24 chunk đều ≤8 từ ✓, khớp thời điểm giọng (lệch ≤0,2s) ✓, đúng luật kênh (P-09, phụ đề EN; lời VI nằm ở bong bóng). Nghĩa đúng, nhưng vài chunk khác cột caption EN trong bản khóa → S2.
- End card 53,63–55,64s (2,0s; fade-in ~0,2s, đọc rõ khoảng 1,8s) ✓ luật ~2s.
  - Có câu an toàn đúng chữ, credit CC BY 4.0 nguyên văn (dấu –), 4 nguồn, «Trend: @ng__phanh · TikTok».
  - Không có câu nào ám chỉ tác giả bảo trợ ✓.
  - Chữ nhỏ và dày, 2s không đọc hết được. Caption bài đăng có bản đầy đủ nên chấp nhận.
- L-083: reels frame 0–14 SSIM 0,9997 so `cover.png` (0,5s) ✓. TikTok frame 0 khác cover (SSIM 0,41) ✓.
- L-084 trend b01:
  - Khung TikTok dựng bằng vật thể, chồng giáo trình, «Học 1 đêm mới hiểu sao…».
  - Nút share đếm lên rồi dừng ở **«55,3K»** từ ~0,9s ✓. Số «34,5K» / «38,9K» chỉ là số giữa lúc đang đếm (0,3–0,8s), không phải lỗi.
  - Handle **@ng__phanh**, 2 gạch dưới (spec, plan, end card đều 2) ✓. Hai gạch hiển thị liền nên nhìn như 3, nhưng chữ đúng.
  - `trend-signals.md` dòng «Trend trong clip» ghi «b01 · chỉ ở hình và chữ trên màn hình (lời không đọc câu viral)» ✓, khớp v4. Mục «Yếu tố… 1. Hook/lời» đã ghi «đã bỏ ở v4», không cũ.
- Claim cấm: không có «317 thí nghiệm đều thống nhất», %, số ngày giãn cụ thể, cơ chế «não…» trong lời, bong bóng, caption EN, bài đăng ✓. «+2 ngày» là mốc kiểm tra của nghiên cứu, không phải số ngày giãn ✓.
- b02b và b07b/c cùng góc máy (đồng hồ, tờ Punnett, Thầy, nền grid). Ô trống → ô điền ✓.
- Nhịp cắt: 23 cảnh, trung bình 2,4s, dài nhất b02b 3,73s và b08 3,6s (có chuyển động) ✓. Không có đoạn hình tĩnh dài.
- **Lặng giọng 1,0s ở 49,24–50,24s** (c16 «…cách giải hơn» → c17 «Còn bạn»). Do b07c giữ hình 0,6s, nên giọng c17–c18 bị dời +0,6s. Plan đọc: «không nghỉ nào > 0,5s». L-070: >0,8s là chặn. Hiệp muốn đọc nhanh → **F3**.
- **b03 cột «Lần 2 cách 1 tuần»** (đo pixel, đáy y≈990):
  - Cột xám cao 211px. Cột cam «đọc liền» lúc «ngay» cao 227px.
  - Lúc +2 ngày, cột cam tụt về ngang cột xám ✓ và cột mực cao **308px**.
  - Như vậy cột mực **cao hơn hẳn đỉnh cột cam «đọc liền»** (+81px). Trái điều kiện của FLUX v4 («cột cách 1 tuần không cao hơn cột đọc liền»), và hình gợi ra một so sánh giữa hai nhóm mà nguồn không nói → **F2**.
  - Cột mực chỉ hiện ở mốc +2 ngày: khớp lời c08 («…thì hai ngày sau vẫn hơn người đọc một lần») và khớp Rawson & Kintsch ✓.
  - Ghi chú: commit `f030144` không có trong repo trên box. Bản sửa của Deep Research nằm ở `97a50af` (visual-plan-v4.md dòng b03).
- **Theme:** spec/plan `dark`, check-rules rule-17 ✔. Engine chỉ đổi màu khung ngoài sang mực. Nền cảnh là giấy #F5F5F3, **y hệt clip-04 LIGHT**. Clip-03 DARK có nền xám #E4E4DF. Người xem sẽ thấy clip-05 sáng, liền sau clip-04 LIGHT → **H1**.
- **Reels/Shorts:** bản reels dùng layout TikTok, phụ đề ở y≈1488–1690 (77,5–88%). Vùng này trùng phần UI dưới của Reels/Shorts (username, caption, nút âm thanh). Engine đã có `layout:"reels"` (phụ đề y≈1000–1240) như clip-04 → **F4**.
- Gói đăng: caption TikTok, hashtag (4, đúng rule-53b), credit, câu an toàn, nhãn AI trong template đều đúng, không bịa số. Nhưng **Threads/IG/Shorts chưa có** (F1).

## 4. Bốn việc News còn để mở
| Việc | Quyết |
|---|---|
| Phụ đề tô cam #FF5A36 | **Đạt luật** (accent duy nhất của brand, dùng cho chữ khóa đúng nghĩa nhấn). Đây là đổi phong cách so clip-04 (nền mực), nên **Hiệp quyết (H2)**. Chữ trắng trên nền cam đọc được ở 1080p. |
| Cột thứ 3 b03 màu mực | **Đạt luật** (xanh lá chỉ dùng cho «xong/+1», rule-14), không cần Hiệp. Nhưng chiều cao cột sai (F2). |
| Bìa sách Sinh màu xám | **Đạt luật** (cùng lý do), không cần Hiệp. |
| Reels chưa có layout phụ đề riêng | **Phải sửa (F4)**, không phải lựa chọn: phụ đề nằm trong vùng UI Reels/Shorts. |

## 5. Phải sửa (News)
- **F1** Điền `final/post.md` từ `post.tpl.md`: Threads (≤500 ký tự, 1 câu hỏi), Reels (≤5 hashtag, credit + câu an toàn), YouTube Shorts (tiêu đề ≤70 ký tự không hashtag, mô tả có credit + link + 3 hashtag cuối), các số đo `{TT}{RE}{LI}{SSIM}{COVER_MD5}…`. Rồi chạy lại check-rules.
- **F2** b03e (~22,0–24,2s): hạ cột «Lần 2 cách 1 tuần» xuống trong khoảng xám → đỉnh cam lúc «ngay» (cao 215–227px, ví dụ bằng đỉnh cam 227px). Vẫn cao hơn xám, không số.
- **F3** b07c→b08 (49,24–50,24s): cắt hold b07c để khoảng lặng c16→c17 ≤0,45s (plan 0,40). Giọng c17–c18 trở lại đúng mốc voice-only. Kiểm lại phụ đề b08 và end card (tổng ~55,0s).
- **F4** Bản reels: render với `layout:"reels"` (phụ đề y≈1000–1240, title ≥300), giữ khung cover 0,5s. Soát frame vùng y>1450 không còn chữ.
- S1 (nên sửa) b02b ~10,5–11,8s: dời dấu «?» lên/phải ~60px khỏi tóc (L-033).
- S2 (nên sửa) đổi caption EN về cột bản khóa: b06 «Longer memory needs wider gaps between reviews» (thay 2 chunk «researchers found: to remember longer / the wider the gaps between reviews», câu bị cụt). b05c «One hour a day, as the guide says» giữ được.
- S3 (ghi chú) rule-46 STT của check-rules: sửa tool cắt đoạn và dùng `ASR_MODEL=medium`. Lần này đã ghi bằng chứng ở mục 2.

## 6. Cần Hiệp quyết
- **H1** Theme: chấp nhận «DARK = khung mực + cảnh giấy trắng» (nhìn giống LIGHT clip-04), hay đổi nền cảnh sang xám/grid như clip-03 để ra đúng DARK (render lại).
- **H2** Phụ đề tô cam #FF5A36 thay nền mực.

## Frame tiêu biểu
- `/workspace/review-c05/b01-0.2-full.png`: trend b01, @ng__phanh, light/dark
- `/workspace/review-c05/rails.png`: share 55,3K
- `/workspace/review-c05/b03strip.png`: cột b03 (ngay → +2 ngày, cột mực quá cao)
- `/workspace/review-c05/s2.png`: b02/b07 cùng góc máy, đoạn Cepeda
- `/workspace/review-c05/endcard.png`: end card
