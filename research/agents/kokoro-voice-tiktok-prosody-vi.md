---
title: "Kokoro Voice — Nhấn và ngắt giọng cho TikTok/Shorts tiếng Việt: nguồn, đối chiếu repo, checklist F5 clip-04, đề xuất check"
date: 2026-10-20
status: draft
source: "Kokoro Voice (agent), theo W-19 / L-078: mỗi agent tự nghiên cứu cách làm TikTok trong phần việc của mình"
id: kokoro-voice-tiktok-prosody
type: research
tags: [voice, prosody, tts, f5-tts, tiktok, w-08, w-17, l-069, l-070, clip-04]
---

# Nhấn và ngắt giọng cho TikTok/Shorts tiếng Việt — nghiên cứu cho khâu giọng

**Phạm vi:** chỉ có nghiên cứu và đề xuất. Mình không tạo audio, không tải model, không sửa `pipeline/`, `check-rules.py`, không commit. Các con số đo bản giọng cũ đều lấy từ file đã có trong repo (`content/clips/clip-04-gap-sach-tu-kiem/final/prosody-measure-v16c.md`, `script-v18-delivery.md`).

**Yêu cầu của Hiệp làm thước đo cho file này (L-078 → W-17):** nhấn đúng chữ; chỉ ngắt ở chỗ ngắt cụm tự nhiên; **không bao giờ ngắt giữa câu/giữa cụm**; vẫn đọc nhanh như hiện tại (L-074).

**Cách ghi độ tin cậy:** ✅ có nguồn chính, đọc trực tiếp · 🟡 nguồn phụ/vendor hoặc chỉ đọc tóm tắt · ❓ suy luận của mình, chưa có nguồn, phải nghe để xác nhận.

---

## 0. Tóm tắt nhanh (7 điểm)

1. **Hook phải nói ngay, không có lặng mở đầu.** TikTok đo 2 giây và 6 giây đầu; TikTok khuyến nghị nêu nội dung chính trong 3 giây đầu và đặt hook trong 6 giây đầu. ✅🟡 → Âm đầu tiên phải ≤0,3 s (rule-55 đã có). Mới: trong hook thì nghỉ phải ngắn hơn phần thân (xem điểm 7, đang mâu thuẫn).
2. **Đọc nhanh là đúng hướng, nhưng chưa ai chứng minh có "tốc độ tối ưu".** Creator TikTok nói chuyện trực diện bằng tiếng Anh có trung vị khoảng 215 từ/phút (mẫu nhỏ, 4 creator). Một nghiên cứu trên 2.511 video quảng bá cho thấy nói nhanh hơn thì được share nhiều hơn. 🟡 → Ủng hộ L-074 (bỏ trần 5 âm tiết/s). Không dịch được "từ/phút" tiếng Anh sang "âm tiết/giây" tiếng Việt.
3. **Tiếng Việt miền Nam nhấn bằng KÉO DÀI là chính, không phải bằng âm lượng.** Trong nghiên cứu của Brunelle (2017), người nói miền Nam nhấn chữ khi sửa ý người khác bằng cách kéo dài âm tiết (mọi người, mọi thanh). Họ **không** dùng âm lượng. Chỉ 7/10 người nâng cao độ, và chỉ ở thanh sắc/ngang, không ở thanh huyền. ✅ → Đây là chỗ **mâu thuẫn tiềm ẩn** với W-08/L-070 hiện tại: nhấn bằng +2 dB, không đổi tempo (mục 3).
4. **Chỗ ngắt cụm tự nhiên trong tiếng Việt = lặng + kéo dài âm tiết đứng trước chỗ ngắt.** Trong lời nói tự nhiên giọng Nam, âm tiết trước lặng dài hơn 26%, âm tiết cuối câu dài hơn 42% (S10); trong giọng đọc, âm tiết cuối ngữ đoạn dài hơn 41–70% (S6). Một khoảng lặng chèn vào mà âm tiết trước đó không kéo dài sẽ nghe như "bị cắt". Ngược lại, chỉ một khoảng lặng ~0,14 s đã đủ để người nghe cảm thấy có ranh giới cụm. ✅ → Ngưỡng hiện tại (chỉ chặn khoảng lặng ≥0,25 s giữa cụm) **quá lỏng**. Ở v16c có hai khoảng lặng giữa cụm 0,19 s và 0,22 s vẫn lọt.
5. **Lặng trước punchline: bằng chứng lẫn lộn.** Danh hài chuyên nghiệp có nghỉ trước punchline dài hơn khoảng 157 ms. Nhưng khi chỉ nghe tiếng, kéo dài khoảng nghỉ này không làm người nghe thấy buồn cười hơn. Kể chuyện cười đời thường thì không có lặng trước punchline; punchline được nói **thấp hơn và chậm hơn**, không to hơn. ✅ → Không thêm lặng dài cho punchline. Giữ `///` ≤0,4 s như plan đang ghi; đuôi câu punchline để rơi giọng.
6. **Đối thoại hai nhân vật: người sau nói gần như ngay.** Khoảng chờ đổi lượt lời phổ biến nhất là 0–200 ms (trung bình khoảng 208 ms, 10 ngôn ngữ). ✅ → Khi Hiệp chibi ↔ Omi đổi lượt trong cùng beat, nghỉ 0,1–0,25 s, **không** dùng 0,35–0,4 s như hết câu/hết beat (mục 2.6). Hiện chưa có luật nào cho khoảng này.
7. **Trong repo có mâu thuẫn chưa ai quyết:** L-027 / check `L-027` yêu cầu khoảng lặng trong hook ≤0,1 s. Plan đọc v18 (theo W-08/L-070) lại đặt phẩy 0,18 s và hết câu 0,35 s ngay trong hook c01–c02. Mình chỉ báo, không tự chọn (mục 3, dòng X1).

**Check đáng làm nhất (mục 5):** E1, **"ngắt giữa cụm tương đối"**. Hạ ngưỡng lặng giữa cụm từ 0,25 s xuống khoảng 0,12–0,15 s và tính tương đối so với khoảng nghỉ phẩy ngắn nhất của chính bản đó. Check này nhắm thẳng câu Hiệp chê ("ngắt nghỉ ngừng nhấn nhá không hợp lý", L-069) và lấp đúng lỗ hổng đã thấy ở v16c s09.

---

## 1. Nguồn đã đọc (link cụ thể)

| # | Nguồn | Nói gì (phần dùng ở đây) | Độ tin cậy |
|---|---|---|---|
| S1 | TikTok Ads Help, *Creative best practices for performance ads*: https://ads.tiktok.com/resources/help/article/creative-best-practices | Hook trong 6 s đầu; nêu nội dung chính trong 3 s đầu; chữ trên màn hình 5–10 từ/giây; có CTA rõ | ✅ (nguồn chính thức, nhưng viết cho quảng cáo, không riêng video kể chuyện) |
| S2 | TikTok for Business, *Creative Codes*: https://ads.tiktok.com/business/en-US/blog/creative-best-practices-top-performing-ads | "90% tác động ghi nhớ quảng cáo nằm trong 6 giây đầu"; cấu trúc hook → thân → kết | ✅ (số liệu của TikTok, cho quảng cáo) |
| S3 | DeepClick, *Ad hook in the first 3 seconds* (2026): https://deepclick.com/resources/blog/ad-hook-first-3-seconds/ | TikTok báo số view 2 s và 6 s → 2 giây đầu là lúc giữ người xem dừng lướt; hook đặt cả trong lời lẫn chữ để xem không tiếng vẫn hiểu | 🟡 (blog vendor) |
| S4 | ManyScripts, *How to Yap on TikTok* (03/10/2026): https://www.manyscripts.com/blog/how-to-yap-on-tiktok | 42 video nói trực diện của 4 creator tiếng Anh: trung vị 215 từ/phút, câu mở đầu khoảng 13 từ, chỉ 1/42 video mở bằng lời chào | 🟡 (vendor, mẫu nhỏ, tiếng Anh) |
| S5 | *Exploring user engagement behavior with short-form video advertising… a visual-audio perspective*, Internet Research: https://doi.org/10.1108/intr-07-2023-0521 | Theo tóm tắt hiện trong kết quả tìm kiếm: trên 2.511 video quảng bá TikTok, nói nhanh hơn thì được share nhiều hơn, nhưng like/comment không tăng đáng kể | 🟡 (**chưa đọc được toàn văn**, trang DOI hết thời gian chờ khi tải) |
| S6 | Brunelle (2017), *Stress and phrasal prominence in tone languages: The case of Southern Vietnamese*, JIPA 47(3): https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/stress-and-phrasal-prominence-in-tone-languages-the-case-of-southern-vietnamese/13F3BF93FCA2C9BD365B2AC012C35B7D | Miền Nam: không có trọng âm từ; âm tiết cuối ngữ đoạn dài hơn **+41% đến +70%**; khi nhấn để sửa ý thì **kéo dài** ở mọi người nói, **không tăng âm lượng**; nâng F0 chỉ ở 7/10 người, chỉ ở sắc/ngang, **không ở huyền** | ✅ (đọc toàn văn) |
| S7 | Jannedy, *Prosodic Focus in Vietnamese*: https://publishup.uni-potsdam.de/frontdoor/index/index/docId/1754 · Jannedy (2008), *The effect of focus on lexical tones in Vietnamese*: https://doi.org/10.36505/exling-2008/02/0029/000088 | Tiếng Việt không có từ đánh dấu tiêu điểm, chỉ dùng ngữ điệu; trường độ, F0 và cường độ "bù trừ" cho nhau; khi nhấn, âm tiết dài ra; F0 tăng ở thanh ngang, sắc có dáng "hẫng rồi vọt" (giọng Hà Nội) | ✅ (abstract; giọng Bắc) |
| S8 | *Investigating the variation of intonation contours in Northern Vietnamese tones*, Frontiers 2024: https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1411660/full | 70 người nói giọng Bắc: khi nhấn, sắc lên cao ở cuối; huyền/ngã/ngang rơi mạnh hơn; hỏi/nặng có dáng lên–xuống. Cách nhấn **tuỳ thanh** | ✅ (giọng Bắc, không phải giọng của kênh) |
| S9 | Nguyen, Rilliard, Tran, d'Alessandro (2014), *Prosodic phrasing modeling for Vietnamese TTS using syntactic information*, Interspeech: https://www.isca-archive.org/interspeech_2014/nguyen14_interspeech.pdf | Bảng 5: nghỉ trung bình ở ranh giới ngữ điệu (gồm dấu câu giữa câu) ≈ **252 ms**, ranh giới cụm ngữ âm cấp 1 ≈ **219 ms**, cấp 2 ≈ **139 ms**. Kéo dài âm tiết cuối cụm khoảng 135%. Chỉ chèn nghỉ mà không kéo dài thì "ranh giới bị gãy, không tự nhiên" | ✅ (đọc toàn văn; giọng đọc chậm Hà Nội) |
| S10 | Brunelle, Chow & Nguyễn (2015), *Effects of lexical frequency and lexical category on the duration of Vietnamese syllables*, ICPhS: https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2015/Papers/ICPHS0341.pdf | Ngữ liệu **nói tự nhiên giọng Nam**, 64.639 âm tiết: âm tiết cuối câu dài hơn **42%**, âm tiết trước lặng dài hơn **26%** (hai hiệu ứng không cộng dồn); hư từ ngắn hơn từ thực khoảng **46 ms** | ✅ (đọc toàn văn) |
| S11 | *Acoustic Correlates of Statement and Question Intonation in Southern Vietnamese* (ĐH Hawaii): https://evols.library.manoa.hawaii.edu/items/49c63aa1-ade2-4da4-901c-3464f15cc9f4 | Theo tóm tắt hiện trong kết quả tìm kiếm: câu hỏi miền Nam có F0 chung cao hơn, to hơn, nhanh hơn; âm tiết cuối dài và dải cao độ rộng hơn. Lên giọng cuối câu là phổ biến nhưng không cố định, có thể đè lên thanh xuống | 🟡 (**trang chặn 403**, chưa đọc toàn văn) |
| S12 | Zhong & Wu (2026), *Prosodic Markers in Mandarin Stand-Up Comedy*, Speech Prosody: https://www.isca-archive.org/speechprosody_2026/zhong26_speechprosody.html | Danh hài nghỉ trước punchline dài hơn baseline +157 ms (634,5 vs 477,9 ms); người nghe chỉ nghe tiếng thì không thấy buồn cười hơn khi nghỉ dài hơn | ✅ |
| S13 | Pickering et al. (2009), *Prosodic Markers of Saliency in Humorous Narratives*: https://doi.org/10.1080/01638530902959604 · Attardo et al. (2011), *Timing in the performance of jokes*: https://doi.org/10.1515/humr.2011.015 | Punchline **thấp hơn, chậm hơn**, không to hơn; không có lặng đáng kể trước punchline | ✅ (abstract) |
| S14 | Stivers et al. (2009), *Universals and cultural variation in turn-taking in conversation*, PNAS: https://www.pnas.org/doi/10.1073/pnas.0903616106 | 10 ngôn ngữ: khoảng chờ đổi lượt phổ biến nhất 0–200 ms, trung vị chung khoảng +100 ms, trung bình +208 ms; trả lời chậm thường là tín hiệu không đồng ý hoặc khó trả lời | ✅ (không có tiếng Việt trong mẫu) |
| S15 | F5-TTS `src/f5_tts/infer/README.md`: https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer/README.md · `utils_infer.py`: https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer/utils_infer.py · issue #1034: https://github.com/SWivid/F5-TTS/issues/1034 | F5 **không có SSML/`<break>`/emphasis**; muốn có nghỉ thì thêm dấu câu hoặc dấu cách; tự chia đoạn ở dấu câu + khoảng trắng; ghép các đoạn bằng `cross_fade_duration=0.15`; muốn nghỉ chính xác thì sinh từng đoạn rồi chèn lặng (`remove_silence=False`) | ✅ |
| S16 | Thánh Lồng Tiếng AI, *Giọng đọc AI tiếng Việt tự nhiên…*: https://thanhlongtiengai.com/bai-viet/giong-doc-ai-tieng-viet-tu-nhien-cho-video.html | Vendor Việt: TikTok cần giọng "có năng lượng, vào ý nhanh"; muốn hết robot thì "câu ngắn, dấu câu hợp lý"; tên riêng/tiếng Anh phải chỉnh cách viết; dùng giọng người khác cần xin phép | 🟡 (quảng cáo sản phẩm, không có số liệu) |
| S17 | **Trong repo:** `research/trends/2026-10-15/audio/delivery-analysis.md` (đo F0/RMS/trường độ audio trend «bản chất» bằng pyin + faster-whisper) | Mẫu trend tiếng Việt thật: stem nhấn +8…+11 st, chữ ruột kéo 0,44–0,68 s (gấp khoảng 2 lần chữ thường 0,2–0,3 s), đuôi rơi −9…−17 st; chen ngang sát nút 0–0,2 s | ✅ (dữ liệu nội bộ đã đo, 1 audio) |

**X public search:** mình đã thử một truy vấn tiếng Việt (giọng AI/giọng đọc + TikTok + nhấn/ngắt/hook). Kết quả chỉ có 1 post cá nhân, không có thông tin kỹ thuật, nên **không dùng**. Mình không tìm được nguồn công khai nào đo nhịp giọng của các kênh TikTok tiếng Việt cụ thể. Nhận định về "kênh Việt làm thế nào" trong file này dựa trên S16 (vendor), S17 (một audio trend đã đo) và ngữ âm học tiếng Việt (S6–S11). **Đây là chỗ thiếu bằng chứng lớn nhất của file này.**

---

## 2. Kỹ thuật trend: tóm tắt có nguồn, đối chiếu cái repo đã có

Cột "Repo hiện tại": **Có** = đã có luật hoặc code; **Mới** = chưa có; **Mâu thuẫn** = ngược với nguồn hoặc giữa các luật với nhau.

### 2.1 Nhịp hook 0–3 s

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Âm đầu tiên vang ngay, không fade-in, không lặng mở đầu | S1, S3 | **Có:** rule-55 (chữ đầu ≤0,3 s, đổi hình ≤1 s). Bản voice-only v16c: s01 bắt đầu ở 0,03 s ✓ |
| Hook vừa trong lời vừa trên chữ (xem không bật tiếng vẫn hiểu) | S3, S1 | **Có:** rule-55, narration = `hook.text` |
| Câu hook ngắn; câu đầu tiên là một ý trọn | S4 (≈13 từ tiếng Anh), L-057/L-058 | **Có** ở khâu script. Không phải việc của khâu giọng |
| Trong hook nghỉ ngắn hơn phần thân để giữ đà | S1/S3 (2 giây đầu quyết định) + L-027 | **Mâu thuẫn:** L-027 (≤0,1 s) vs plan W-08 (0,18/0,35 s) — xem X1 |

### 2.2 Tốc độ

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Đọc nhanh hơn hội thoại thường | S4, S5 | **Có:** L-074 (F5 speed 1.0, bỏ trần âm tiết/s). v16c đo được khoảng 4,48 chữ/s nói thuần |
| Có thể có "điểm quá tải" với nội dung giải thích (đường chữ U ngược) | Tóm tắt một nghiên cứu video giáo dục trong kết quả tìm kiếm (AAEE 2025, https://aaee2025.org/microsite/pdf/full-paper_288.pdf) | ❓ **chưa đọc toàn văn.** Không đủ để đặt trần. Chỉ dùng STT/nghe tai để bắt chữ bị nuốt (đúng L-074) |
| Đổi nhịp theo đoạn: thông tin thì nhanh, cảm xúc thì chậm lại một chút | S16 (vendor) | 🟡 Một phần: plan v18 ghi "hơi chậm lại" ở c04. **Không** đổi bằng tempo/rubberband (L-006/L-008); đổi bằng cách chọn take hoặc speed F5 theo từng chunk |

### 2.3 Nhấn từ khoá / con số

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Một chữ gánh ý mỗi câu, không rải nhấn; không nhấn hư từ (hư từ tự nhiên ngắn hơn khoảng 46 ms) | L-031, L-052, P-08 (≤2/beat); S10 | **Có** (nhấn hư từ chưa có check → E2) |
| **Nhấn tiếng Việt miền Nam = kéo dài âm tiết là chính**; âm lượng gần như không dùng; nâng cao độ chỉ ở sắc/ngang, không ở huyền | S6 ✅, S7 ✅, S8 ✅ (Bắc) | **Mâu thuẫn tiềm ẩn:** W-08/L-070/`voice-delivery-f5.py` nhấn chỉ bằng gain (≥+2 dB) và *không đổi tempo*. `voice-prosody.py` (đường cũ) nhấn bằng tempo ×0,9 + **+0,8 st cho mọi thanh** + 1,5 dB. Như vậy đường mới làm đúng cái mà người miền Nam ít dùng (âm lượng); đường cũ nâng cao độ cả thanh huyền/nặng, là cái S6 thấy không xảy ra. **Chưa chắc:** S6 là giọng đọc trong phòng thu, có thể giọng kể TikTok "diễn" mạnh hơn; +2 dB vẫn có thể nghe được. Xem đề xuất T3 + E3 |
| Chữ "ruột" của trend kéo khoảng 2× chữ thường; stem nhấn cao; đuôi rơi | S17 ✅ | **Có:** L-036 (stem\|payload), áp cho meme stem |
| Con số: đọc thành chữ, giữ nguyên trong cụm (không tách "222" khỏi "nghiên cứu") | S15 (F5 đọc số theo kiểu tiếng Anh nếu không chuyển sang chữ), L-010/L-025 | **Có:** `RESP` trong `voice-delivery-f5.py`, R1/R2 của plan v18. **Mới:** con số là ứng viên nhấn tự nhiên, nhưng ở v18 «222» và «2006» không được nhấn — đúng, vì chữ gánh ý là «cao hơn» / «hai ngày sau». Đừng nhấn số chỉ vì là số |

### 2.4 Ngắt nhịp theo cụm

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Ranh giới cụm = lặng **+ kéo dài âm tiết đứng trước** | S6, S9, S10 | **Mới.** Repo chỉ đo độ dài lặng. Lặng chèn vào chỗ F5 không tự kéo dài sẽ nghe như "cắt" (S9 ghi rõ: chỉ chèn nghỉ thì ranh giới gãy). Hiện `voice-delivery-f5.py` cắt ở điểm năng lượng thấp rồi chèn lặng theo plan, nên chỗ này có thể bị |
| Chỉ cần lặng khoảng 140 ms là người nghe đã thấy ranh giới cụm (đọc chậm) | S9 | **Mâu thuẫn với ngưỡng:** cờ "ngắt giữa cụm" hiện chỉ bắt lặng **≥0,25 s**. v16c s09 có lặng 0,19 s («lớp có») và 0,22 s («nhỏ thì») vẫn qua. Ở giọng đọc nhanh, lặng 0,2 s trong cụm còn dễ nhận ra hơn → E1 |
| Thứ bậc nghỉ: phẩy < hết câu < hết beat | S9 (IP ≈252 > PhP1 ≈219 > PhP2 ≈139 ms) | **Có:** W-08, cờ "thứ bậc nghỉ" trong `voice-delivery-f5.py` |
| Không có SSML; nghỉ đến từ dấu câu hoặc ghép đoạn | S15 | **Có:** L-016/L-070 (chunk = một lần F5, `keep`, không cắt trong output) |
| «X thì Y»: nếu có hơi thì đặt **sau** «thì», không đặt trước | ❓ (cảm nhận ngữ pháp: «thì» khép phần đề; chưa có nguồn trích) | **Mới, chưa chắc.** v16c s09 bị F5 ngừng ở «nhỏ \| thì» trong 7/8 seed, tức đúng chỗ sai. Đề xuất cho khâu chọn take (T5); cần Hiệp nghe để xác nhận |

### 2.5 Lặng trước punchline

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Danh hài có nghỉ trước punchline dài hơn khoảng +0,16 s; với người chỉ nghe tiếng thì không làm tăng độ buồn cười | S12 | **Có một phần:** `///` = 0,4 s trong plan (v16c dùng 1 lần sau «khựng»; v18 không dùng). Giữ ở mức **nghỉ hết câu + ≤0,15 s**, không kéo dài hơn |
| Punchline thấp hơn và chậm hơn, không to hơn | S13 | **Có một phần:** L-036 "đuôi rơi". **Mâu thuẫn nhẹ:** W-08 yêu cầu chữ nhấn ≥+2 dB *kể cả khi là punchline cuối câu* (vd c05 «bí»). Theo S13, punchline cuối câu nên để rơi giọng tự nhiên, chỉ thêm gain vừa đủ ❓ |

### 2.6 Đối thoại hai nhân vật (Hiệp chibi nam ↔ Omi nữ)

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Đổi lượt lời gần như ngay: 0–200 ms, trung bình khoảng 0,2 s | S14 | **Mới.** Plan chỉ có `//` 0,35 s và `//\|` 0,4 s. Đổi người nói mà dùng 0,35–0,4 s sẽ nghe như "đọc kịch bản". Chen ngang trong trend: 0–0,2 s (S17) |
| Trả lời chậm hơn là có nghĩa (lưỡng lự, không đồng ý) | S14 | **Mới:** chỉ kéo dài khoảng chờ khi script ghi rõ nhân vật lưỡng lự (đã có `{ngập ngừng}` ở L-017 cho trong câu; giữa hai lượt lời thì chưa có) |
| Hai giọng phân biệt rõ, không bị nhập vào nhau khi ghép | voice-profile §3a/§3b | **Có:** 2 ref (thai-son / my-duyen). **Mới:** chưa đo khoảng cách F0 trung vị giữa hai giọng sau khi master (E5) |
| Omi chỉ xuất hiện từ tuần ≥5 | L-011 | **Có.** Clip-04 v18 chỉ có một giọng (Thái Sơn) nên mục này áp cho clip sau |

### 2.7 Cảm xúc theo ngữ cảnh

| Kỹ thuật | Nguồn | Repo hiện tại |
|---|---|---|
| Cường độ cảm xúc theo loại dòng (hook nhanh; tự trách gắt; tuyệt vọng kéo «…») | L-027/L-028 | **Có** |
| Câu hỏi: lên giọng cuối là phổ biến nhưng không bắt buộc; câu hỏi miền Nam còn cao hơn, to hơn, nhanh hơn ở cả câu | S11 🟡 | **Có một phần:** cờ ↗ ≥+0,5 st ở âm tiết cuối. **Lưu ý:** câu hỏi không có tiểu từ (v18 c01 «…quên sạch?») thì lên giọng là tín hiệu *duy nhất* → càng quan trọng. «sạch» là thanh nặng tắc, lại vừa là chữ nhấn vừa là âm tiết lên giọng. `voice-delivery-f5.py` hiện chọn take có lên giọng (điểm thưởng khi chọn take, không ép). Đường cũ `voice-phrase-f5.py` thì ép +2,5 st lên âm tiết cuối, dễ làm méo thanh nặng → kiểm STT riêng âm tiết đó (E3c) |
| F5 bắt chước phong cách của audio tham chiếu (zero-shot) → một ref trung tính thì dải cảm xúc hẹp | S15 (cơ chế ref audio + ref text) | ❓ **Đề xuất, chưa thử:** thêm ref cảm xúc thứ hai cho cùng nhân vật, cũng **tổng hợp bằng preset VieNeu** (không clone người thật, đúng DL-035), dùng cho dòng cần cảm xúc mạnh. Đây là thay đổi pipeline/brand, cần Hiệp duyệt (T7) |
| Tag `[cười]`/`[thở dài]` bị đọc thành chữ | L-005 | **Có** (cấm) |

---

## 3. Mâu thuẫn và chỗ chưa rõ cần người quyết (mình không tự chọn)

| # | Mâu thuẫn | Bên A | Bên B | Đề xuất quyết | Ai quyết |
|---|---|---|---|---|---|
| X1 | Nghỉ trong hook | L-027 + check `L-027`: lặng giữa mệnh đề/dòng trong hook ≤0,1 s | W-08 / L-070 / plan v18: phẩy 0,18 s, hết câu 0,35 s, hết beat 0,4 s, áp cả cho hook c01–c02 | Ghi một ngoại lệ hook vào W-08, ví dụ: hook phẩy 0,10–0,12 s, hết câu trong hook 0,2–0,25 s, vẫn giữ thứ bậc phẩy < chấm. `check L-027` hiện chỉ chạy ở đường spec/timing, nên bản voice-only theo plan v18 sẽ không bị bắt | Rule Reviewer đề xuất → Hiệp |
| X2 | Cách nhấn | W-08: gain ≥+2 dB, không đổi tempo, không chẻ chữ | S6/S7: miền Nam nhấn bằng kéo dài âm tiết; không dùng âm lượng; nâng cao độ chỉ ở sắc/ngang | **Không đổi luật ngay.** Thêm *tiêu chí chọn take*: trong các seed đạt STT, ưu tiên take có âm tiết nhấn dài hơn trung vị câu (F5 tự kéo, không phải rubberband), rồi mới thêm gain. Không bao giờ nâng semitone cho chữ nhấn thanh huyền/nặng | Rule Reviewer + Hiệp nghe A/B 2–3 câu |
| X3 | Hai đường code nhấn khác nhau | `voice-prosody.py`: tempo ×0,9 + 0,8 st + 1,5 dB (spec không có `{nhấn:}`) | `voice-delivery-f5.py`: chỉ gain; `voice-phrase-f5.py`: rubberband stretch/pitch | Thống nhất một định nghĩa "nhấn" cho cả ba đường, theo X2 | Người giữ pipeline (News) — **không phải Kokoro Voice tự sửa** |
| X4 | Ngưỡng "ngắt giữa cụm" | `voice-delivery-f5.py measure`: chỉ cờ khi lặng giữa cụm ≥0,25 s | S9: ranh giới cụm cấp thấp chỉ khoảng 0,14 s; v16c lọt 0,19 s và 0,22 s | E1 | Rule Reviewer |
| X5 | Punchline cuối câu | W-08: chữ nhấn ≥+2 dB ở mọi vị trí | S13: punchline thấp và chậm hơn | Chữ nhấn ở cuối câu (punchline): chấp nhận +1…+2 dB *nếu* đã dài hơn trung vị câu ≥1,3×; đuôi rơi | Rule Reviewer |

---

## 4. Checklist nhấn/ngắt áp ngay cho F5 khi làm giọng clip-04

**Trạng thái:** v18 đã được Hiệp chốt (L-078, `final/script-v18-LOCKED.md`, Hiệp nói «Oke duyệt»). Plan đọc `final/script-v18-delivery.md` đã có, kèm quyết định của Rule Reviewer lúc 23:17 ngày 20/10. Người làm giọng là **News** (F5 · Thái Sơn, speed 1.0). Checklist này **bổ sung** cho checklist 8 mục cuối plan v18, không thay thế. Không đổi chữ nào của lời đã khoá (L-072/L-046).

Ký hiệu dùng đúng như repo: `/` phẩy 0,18 s · `//` hết câu 0,35 s · `//|` hết beat 0,4 s · `///` lặng có chủ ý · **đậm** = `{nhấn:}` · ↗ câu hỏi. Ở đường spec: `{nhấn: …}`, dấu câu trong `phrases[].t`, `gap`/`gap_max`/`whole`.

### 4.1 Trước khi sinh (chỉ đọc chữ, không tốn CPU)

- [ ] **T1 — Ký hiệu ngắt khớp dấu câu, 1:1.** Mỗi `/` nằm sau một dấu `,` hoặc `:` trong LOCKED; mỗi `//`, `//|` nằm sau `.`/`?`/`!`; ngoài ra không có ký hiệu nào khác. Plan v18 tự đếm 16 phẩy + 13 chấm/hỏi khớp. Đây đúng là câu "chỉ ngắt ở chỗ ngắt cụm" của Hiệp, viết thành luật đếm được.
- [ ] **T2 — Danh sách cụm cấm ngắt** (ghi vào plan, để News soát khi chọn take). Với v18: «hai trăm hai mươi hai nghiên cứu», «năm hai ngàn lẻ sáu», «ba mươi từ tiếng Anh», «mỗi phần mười từ», «từ thứ năm là hành lý», «kiểm tra ngay», «kiểm tra nhỏ thì điểm», «kiểm tra lại nhớ hơn hẳn» (R4: «lại» = ngược lại), «cần là sáng hôm sau» (R9), «chữ hành lý», «nhóm của Yang». Quy tắc chung: không ngắt giữa số và danh từ, giữa động từ và bổ ngữ ngắn, giữa «nhóm/chữ/lớp» và phần đi sau.
- [ ] **T3 — Chữ nhấn là chữ mang nội dung.** Không đặt nhấn lên «là/thì/mà/nha/á/rồi». Mỗi câu 1 chữ nhấn, mỗi beat tối đa 2 (P-08). v18 sau quyết định của Rule Reviewer: b03 giữ «kiểm tra ngay», «hai ngày sau»; b05 giữ «ba phần», «gấp sách» ✓.
- [ ] **T4 — Chữ nhập F5 đã chuẩn hoá** (chỉ ở đầu vào F5, chữ hiển thị giữ nguyên): «2006», «222», «Yang», «luggage», «Comment» như R1–R6. Số nằm trong cùng chunk với danh từ đi sau nó (T2).
- [ ] **T5 — Câu có «X thì Y»** (c07 «nếu kiểm tra ngay thì…», c14 «…kiểm tra nhỏ thì điểm…»): sinh 8–10 seed như Rule Reviewer đã duyệt. Thứ tự ưu tiên khi chọn take: (1) take không có lặng nào giữa «X» và «thì»; (2) nếu F5 có hơi, chấp nhận lặng ngắn **sau** «thì», không nhận lặng **trước** «thì». ❓ Mục (2) là đề xuất của mình, phải nghe tai để xác nhận.
- [ ] **T6 — Hook c01–c02:** chờ quyết X1. Trong lúc chờ, sinh và đo theo plan v18 như đã duyệt, nhưng **ghi riêng** khoảng lặng trong hook vào `prosody-measure-v18.md`, để khi X1 được quyết thì không phải đo lại.
- [ ] **T7 — Cảm xúc:** chỉ dùng ref `thai-son.wav` như hiện tại. Không thêm ref mới khi chưa có quyết định (mục 2.7).

### 4.2 Sau khi sinh — chọn take, đo, nghe (thêm vào checklist 8 mục của plan v18)

- [ ] **C1 — Lặng giữa cụm theo ngưỡng tương đối** (xem E1). Ghi mọi khoảng lặng ≥0,12 s nằm ngoài ký hiệu, dù chưa tới 0,25 s. Soi kỹ các cụm ở T2.
- [ ] **C2 — Kéo dài trước ranh giới.** Ở mỗi `//` và `//|`: âm tiết cuối không bị cụt (đo trường độ ≥1,2× trung vị âm tiết của câu đó). Nếu khoảng nghỉ phải *chèn* thêm vì F5 không tự dừng, chọn take khác trước khi chèn lặng dài vào giữa câu.
- [ ] **C3 — Nhấn có kéo dài.** Ngoài +2 dB theo W-08, ghi thêm *tỉ lệ trường độ* của âm tiết nhấn so với trung vị câu. Khi nhiều seed cùng đạt STT, ưu tiên take có tỉ lệ cao hơn. Không dùng rubberband để kéo (L-006, L-008).
- [ ] **C4 — Chữ nhấn thanh huyền/nặng/ngã: không nâng semitone.** Chữ nhấn v18 kết thúc bằng thanh huyền/nặng: «quên sạch» (c01, nặng, lại là âm tiết hỏi), «ba mươi từ» (c03), «hai ngày sau» («ngày» huyền), «ba phần» (c10), «tự viết được» (c16, nặng), «mấy từ» (c17). Chữ có thể nâng: «bí» (sắc), «gấp sách» (sắc), «kiểm tra ngay»/«sáng hôm sau» (ngang). Hiện `voice-delivery-f5.py` chỉ dùng gain nên không vướng; check này dành cho `voice-prosody.py` (+0,8 st) và `voice-phrase-f5.py`.
- [ ] **C5 — Câu hỏi ↗** (c01 «quên sạch?», c02 «những gì?», c17 «mấy từ?»): ưu tiên take F5 tự lên giọng (như `voice-delivery-f5.py` đang chọn). Nếu phải chỉnh cao độ thì chạy STT riêng âm tiết cuối; STT ra chữ khác thì bỏ chỉnh và chọn take khác.
- [ ] **C6 — Punchline cuối beat** (c05 «…thì mình **bí**», c08 «…nhớ hơn hẳn»): đuôi câu rơi giọng; nghỉ sau vẫn đúng 0,4 s của `//|`, không kéo thêm (S12/S13).
- [ ] **C7 — Nghe tai từng câu**, ghi theo mẫu W-08: giây · lỗi · cách sửa. Câu nào STT nghi ngờ (Yang, luggage, Comment) thì ghi «cần nghe tai», không tự kết luận đạt.

### 4.3 Bảng tra nhanh: ý muốn → cách viết bằng markup có sẵn

| Muốn | Đường plan đọc (`voice-delivery-f5.py`) | Đường spec (`voice-prosody.py` / `voice-phrase-f5.py`) | Ghi chú |
|---|---|---|---|
| Ngắt cụm trong câu | thêm `/` **chỉ khi lời đã có dấu phẩy** | dấu `,` trong `phrases[].t` (180 ms) | Lời khoá không có phẩy thì **không** ngắt. Muốn ngắt mới phải xin Hiệp sửa lời |
| Hết câu | `//` 0,35 s | `.` 350 ms, `?`/`!` 400 ms | Thứ bậc: phẩy < chấm |
| Hết beat | `//\|` 0,4 s | khoảng giữa dòng | |
| Nhấn | `**chữ**` (gain ≥+2 dB) + chọn take dài hơn (C3) | `{nhấn: chữ}` | 1 chữ/câu; không nâng semitone thanh huyền/nặng (C4) |
| Lặng trước punchline | `///` ≤0,4 s, chỉ khi script có | `…` (500 ms) hoặc `gap` | Bằng chứng yếu → dùng ít, tối đa 1 lần/clip ❓ |
| Hook liền một hơi | (chờ X1) | `whole: true`, `gap_max: 0.1`, speed 1.2 (L-027) | Hai đường đang khác nhau |
| Đổi lượt Hiệp ↔ Omi | *(chưa có ký hiệu)* — đề xuất `>` = 0,15 s | khoảng giữa dòng khác speaker | Mới, xem E5 |
| Câu hỏi lên giọng | `↗` | `?` | Kiểm STT âm tiết cuối (C5) |

---

## 5. Đề xuất check tự động cho `check-rules.py` (chỉ đề xuất, chưa viết code)

Xếp theo giá trị / công làm. Mọi check đều đọc file đo đã có (`final/prosody-measure-*.json` do `voice-delivery-f5.py measure` sinh ra, có word timestamps) hoặc chỉ đọc chữ. Không cần sinh thêm giọng.

| Ưu tiên | Mã đề xuất | Check | Dữ liệu cần | Ngưỡng đề xuất | Chặn / cảnh báo | Vì sao |
|---|---|---|---|---|---|---|
| **1 (đáng làm nhất)** | **E1 — ngắt giữa cụm tương đối** | Mọi khoảng lặng giữa hai từ **không** có ký hiệu `/ // //\| ///` | word timestamps trong measure json (đã có) | ≥0,12 s → cảnh báo; ≥ min(0,15 s; 0,8 × phẩy ngắn nhất đo được trong bản) → **chặn**. Cụm trong danh sách cấm (T2) → chặn từ 0,12 s | Chặn | Đúng lỗi Hiệp chê (L-069/W-17). Ngưỡng 0,25 s hiện tại để lọt 0,19/0,22 s ở v16c s09; S9 cho thấy chỉ ~0,14 s đã thành ranh giới cụm |
| 2 | **E2 — ký hiệu ngắt ↔ dấu câu** | Trước khi sinh: so plan đọc với `script-vNN-LOCKED.md`. Mỗi `/` ↔ `,`/`:`; mỗi `//`/`//\|` ↔ `.`/`?`/`!`; `↗` chỉ ở câu kết thúc bằng `?`; mỗi câu ≤1 chữ đậm, mỗi beat ≤2 (P-08); chữ đậm không phải hư từ (là, thì, mà, nha, á, rồi, nè, hông) | chỉ cần chữ | đúng/sai | Chặn | Rẻ, chạy trước 60–90 phút CPU của F5. Hiện `voice-delivery-f5.py parse` mới kiểm khớp chữ và hết câu bằng `//`, chưa kiểm `/` ↔ phẩy |
| 3 | **E3 — nhấn có trường độ + nhấn đúng theo thanh** | (a) tỉ lệ trường độ âm tiết nhấn / trung vị âm tiết của câu; (b) nếu có chỉnh semitone dương cho chữ nhấn thanh huyền/nặng/ngã → cảnh báo; (c) câu hỏi có chỉnh lên giọng → STT âm tiết cuối phải khớp | measure json + log chỉnh (`emph_db_before_after`, `question_rise_st` đã có) + bảng thanh của chữ (tách dấu Unicode) | (a) <1,1× → cảnh báo; (b) bất kỳ → cảnh báo; (c) không khớp → chặn | Cảnh báo (c: chặn) | S6/S7/S8. Để cảnh báo trước, chờ Hiệp nghe A/B rồi mới nâng lên chặn |
| 4 | **E4 — kéo dài trước ranh giới** | Âm tiết cuối trước `//`, `//\|` có trường độ ≥1,2× trung vị câu | measure json | <1,2× → cảnh báo | Cảnh báo | S6/S9/S10: thiếu kéo dài thì khoảng lặng nghe như bị cắt |
| 5 | **E5 — đổi lượt hai nhân vật** | (a) khoảng giữa hai dòng khác người nói trong cùng beat: 0,08–0,3 s, trừ khi có `{ngập ngừng}`; (b) F0 trung vị Hiệp (Thái Sơn) và Omi (Mỹ Duyên) sau master cách nhau ≥ một khoảng tối thiểu (ngưỡng sẽ đo từ hai ref hiện có rồi mới đặt) | timing + speaker + pyin (code F0 đã có trong `voice-prosody.py --metrics`) | (a) ngoài khoảng → cảnh báo | Cảnh báo | S14; L-011 nên chỉ chạy khi clip có Omi (tuần ≥5) |
| 6 | **E6 — nghỉ trong hook nhất quán** | Sau khi X1 được quyết: một ngưỡng chung cho hook ở cả đường spec (`L-027`) lẫn đường plan đọc | measure json + `part: hook` / beat b01 | theo quyết định X1 | Chặn | Hiện L-027 không chạy trên bản voice-only theo plan → hai luật có thể cùng "đạt" mà lời ra khác nhau |

**Không đề xuất check:** tốc độ (âm tiết/giây) vì L-074 đã bỏ; độ dài nghỉ trước punchline vì bằng chứng S12/S13 không đủ để chặn.

**Mức trả lời của câu "check nào đáng làm nhất":** **E1**, sau đó là **E2**. E1 sửa đúng lỗi bị chê, chỉ đọc file đo đã có, và lấp lỗ hổng đã xảy ra thật (v16c s09). E2 rẻ nhất, chặn lỗi trước khi tốn giờ CPU sinh giọng.

---

## 6. Việc khâu giọng làm tiếp (không làm trong file này)

1. Rule Reviewer xem X1–X5 và E1–E6; Hiệp quyết X1 (hook) và X2 (cách nhấn).
2. Khi News làm giọng v18: áp checklist mục 4 cùng với checklist 8 mục của plan; ghi thêm số đo C1–C5 vào `final/prosody-measure-v18.md`.
3. Nếu Hiệp đồng ý thử X2: chỉ nghe A/B 2–3 câu đã có trong v18 (cùng lời khoá), so "chọn take dài hơn + gain" với "chỉ gain". Không thêm ref mới, không đổi engine.
4. Kokoro-Vietnamese **không** liên quan tới việc này: giọng sản xuất vẫn là F5. Đánh giá Kokoro vẫn theo `research/agents/kokoro-vs-f5tts-initial-research-vi.md` và workflow `workflows/agents/kokoro-voice.md` (chỉ A/B mù khi Hiệp chốt script; fail cổng license hoặc chất lượng thì không đổi pipeline).

## 7. Điều chưa chắc chắn (ghi thẳng)

- Không có nguồn công khai đo nhịp giọng của **kênh TikTok tiếng Việt cụ thể**. Phần "trend" dựa trên tài liệu chính thức của TikTok (viết cho quảng cáo), blog vendor, một audio trend đo trong repo, và ngữ âm học tiếng Việt.
- S6 (miền Nam) đo giọng đọc trong phòng thu với lối nhấn để sửa ý người khác. Giọng kể TikTok có thể nhấn mạnh hơn và dùng âm lượng nhiều hơn. X2 phải được nghe A/B mới kết luận.
- S7, S8, S9 là giọng Bắc / Hà Nội; S9 là giọng đọc chậm. Ngưỡng ms chỉ để định hướng, phải đo lại trên giọng F5 Thái Sơn.
- S5, S10, S11 mình chỉ đọc qua tóm tắt trong kết quả tìm kiếm, chưa đọc toàn văn (S5 tải DOI quá thời gian chờ, S11 trang chặn 403).
- Quy tắc «X thì Y — nếu có hơi thì đặt sau "thì"» là cảm nhận ngữ pháp của mình, chưa có nguồn trích.
- Không có số nào ở đây được đo lại trên audio mới. Mọi số của clip-04 lấy từ `prosody-measure-v16c.md` và `script-v18-delivery.md` đã có trong repo.
