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
