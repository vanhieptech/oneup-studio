---
title: "Podcastfy Audio: định dạng audio/hội thoại dùng lại cẩm nang + tín hiệu trend TikTok"
date: 2026-10-20
source: "Agent Podcastfy Audio; dữ liệu Apify có sẵn trong repo (16–20/10) + 1 run mới clockworks/tiktok-scraper 8iLSoB7NGCx3rBdfK (20/10 23:20 ICT)"
id: research.podcastfy-audio-formats-2026-10-20
type: research
status: draft — chờ Hiệp xem; News gom commit
updated: 2026-10-20
tags: [podcastfy, podcast, hoi-dap, dialogue, tiktok-trend, apify]
---
# Định dạng audio/hội thoại cho nội dung cẩm nang + cách làm TikTok dễ lên xu hướng

Việc do News giao trong nhóm Agency Production tối 20/10/2026. Clip-04 không bị đụng tới. Bản này chỉ là chữ: không làm giọng, không render.

Đọc kèm:
- Transcript mẫu để Hiệp duyệt: `research/agents/podcastfy-sample-transcript-2026-10-20.md`
- Dữ liệu thô của run mới: `research/agents/data/podcastfy-formats-2026-10-20/` (`raw-clockworks.json` 30 clip, `run-meta.json`, `vtt/` 12 phụ đề)
- Dữ liệu cũ dùng lại: `research/trends/2026-10-16…20/apify/clips.json` + `vtt/`

**Quy ước số liệu:** play/like/comment/share/save lấy từ Apify lúc chạy (cũ: ngày ghi trong đường dẫn; mới: 20/10/2026 23:21 ICT). Đây là ảnh chụp tại một thời điểm, số trên TikTok sẽ còn đổi. Tỉ lệ % = chỉ số chia play, do mình tự tính. Mốc giây lấy từ VTT tự động của TikTok, nên chữ có thể sai chính tả nhưng thời điểm thì đúng.

---

## 1. Các định dạng khả thi

Pipeline hiện tại: script tay qua gate Hiệp → giọng F5 (Hiệp = Thái Sơn, Omi = Mỹ Duyên) → video-engine comic 1080×1920 → không chèn nhạc. «Công sức» dưới đây so với một clip 1 người nói như clip-04.

| # | Định dạng | Hợp phần nào | Ưu | Nhược | Công sức trên pipeline hiện tại | Rủi ro bịa fact |
|---|---|---|---|---|---|---|
| D1 | **Hỏi–đáp Thầy–Omi 45–60s.** Omi hỏi đúng nỗi đau của người xem, Thầy trả lời bằng một item | 4, 19 (họp, tin nhắn, ước thời gian), 3 (năng lượng, ngủ), 23 (học) | Câu hỏi đặt ở giây 0 khớp luật hook L-057/L-058 và khớp mẫu đang chạy (mục 2, K1). Omi nói thay người xem nên Thầy không phải tự nói «bạn sai» (L-053). Đổi người nói tạo nhịp mà không cần thêm hiệu ứng | Omi chỉ được xuất hiện từ tuần 5 (L-011). Phải canh hai giọng F5 và khẩu hình hai nhân vật | **Thấp–vừa.** Engine đã có cast `omi` và hai giọng F5. Thêm việc: ghép lượt thoại, khoảng nghỉ lúc đổi người nói, biểu cảm người nghe | **Thấp** nếu mỗi câu của Thầy có cột đối chiếu fact. Câu của Omi là lời nhân vật, không được mang số |
| D2 | **Myth vs fact đối đáp.** Omi nói một niềm tin phổ biến, Thầy sửa bằng số trong item | Các item gỡ myth: 4.12 (21 ngày), 6.25 (ý chí cạn như pin), phần 6, 3.x (ngủ/cà phê) | Tạo phe và tranh luận trong comment (P11/P13 trong `patterns.md`). Hook dễ viết | Dễ thành giọng giảng hoặc chê người tin myth (L-053). Myth phải là câu người ta nói thật, không được tự dựng ra «người ta hay nói» | Như D1 | **Vừa.** Câu myth không có trong item thì phải ghi là lời nhân vật, không được trình bày như «khảo sát cho thấy» |
| D3 | **«Trả lời @bình luận».** Video trả lời một comment có thật, bằng tính năng reply của TikTok | Mọi phần ưu tiên, tuỳ comment | Comment có thật thì người xem tự thấy mình trong câu hỏi. Có data thật ở mục 2 (K4) | @hi.oneup chưa có dữ liệu comment của chính kênh (retro tuần 1 còn trống). Rule hiện tại: không trích nguyên văn comment của người khác vào clip (`patterns.md` P14/P15), nên phải Hiệp đổi rule hoặc chỉ dùng comment trên kênh mình | **Thấp** (giống D1) cộng bước lọc comment | **Vừa.** Comment hay hỏi những chỗ item không trả lời được; phải dám nói «sách không có số này» |
| D4 | **Skit tình huống đời thường** (gọi điện, sếp–nhân viên, mẹ–con), chốt bằng một item | 19 (họp, tin nhắn ngoài giờ), 3.1 (điện thoại), 4 | Lượt share cao nhất trong mẫu (mục 2, K5): 2–3% play | Lượt save thấp (0,2–0,3%). Ít chỗ cho dẫn chứng; dễ mất phần fact. Không được dán nhãn người khác (`patterns.md` F07) | **Vừa–cao.** Nhiều cảnh, nhiều biểu cảm, có thể cần nhân vật phụ | **Thấp** về số (vì ít số), nhưng **cao** về nói quá: skit hay phóng đại hệ quả |
| D5 | **Podcast clip 1–3 phút** (audio là chính, hình tĩnh/waveform/comic nhẹ) cho TikTok dài, YouTube, Spotify | Bất kỳ phần; hợp nhất là các item có nhiều ghi chú/giới hạn như 4.3, 4.4, 23.x | Lượt save cao (2,2–4,6% play ở các clip podcast VN, mục 2, K3). Dùng được Podcastfy (`transcript_only`) để nháp kịch bản 2 người | Dài hơn trần 60s của Shorts. Podcastfy không hỗ trợ tiếng Việt chính thức, phải cắm F5 vào `TTSProvider` (`research/agents/podcastfy-audio-research-vi.md`). Chưa có kênh YouTube/Spotify | **Cao.** Viết provider F5 cho Podcastfy, cùng bước kiểm 2–3 phút giọng (L-069/L-070) | **Cao** nếu để LLM của Podcastfy tự viết. Bắt buộc fact-lock và đối chiếu từng câu (workflow mục 4) |
| D6 | **Mini-series theo phần cẩm nang** («Tập n», mỗi tập một item, cuối tập nhá tập sau) | Một phần chạy liền 5–7 tập: 4 (thời gian) hoặc 14 (tài khoản & an toàn) | Đánh số tập và nhá tập sau là mẫu lặp lại trong data (mục 2, K4). Hợp với lịch theo trụ trong `theme-map.md` | Phải giữ đều đặn. Tập lẻ khó xem nếu người xem vào giữa chừng | **Thấp.** Lớp đóng gói (tên tập, thẻ «tập sau») bọc ngoài D1 hoặc D2 | Như D1/D2 |

---

## 2. Tín hiệu trend thật

### 2.1 Nguồn dữ liệu
- **Dùng lại** `research/trends/2026-10-16…20/apify/clips.json` (đã có VTT): @camreadwonder, @biquyetdodaihoc, @nhile_n, @kbhoanganh, @nhacomeo.mut, @sabito_0668.
- **Run mới** (chỉ 1 lần): `clockworks/tiktok-scraper`, run `8iLSoB7NGCx3rBdfK`, dataset `FGze4KzZeRwr6iYno`. 5 searchQueries không dấu: «podcast phat trien ban than», «hoi dap tam ly», «tra loi binh luan meo», «hoat hinh doi thoai bai hoc», «podcast clip productivity». resultsPerPage 6 → **30 clip**; DOWNLOAD_SUBTITLES; proxy None; không lấy comment. **0,0300 CU**. Theo cách quy đổi của README Apify 20/10 thì vào khoảng 0,01 USD; MCP không báo USD. Lần gọi đầu bị ngắt phía client trước khi trả run id, nên có thể đã tốn thêm tối đa khoảng 0,03 CU (`run-meta.json`).
- Query «hoi dap tam ly» lẫn clip phim (@vlive.dienanh 2,1M, @review.phim1774 3,1M), không phải dạng hỏi–đáp kiến thức, nên **loại**. Query «tra loi binh luan meo» ra chủ yếu kênh mèo.

### 2.2 Bảng clip dạng hội thoại / podcast / hỏi–đáp

**TikTok Việt Nam**

| Clip | Dạng | Dài | Play | Like | Cmt | Share | Save | Hook (0–3s, theo VTT/caption) | Cách dàn thoại |
|---|---|---|---|---|---|---|---|---|---|
| [@chongchongtre20s](https://www.tiktok.com/@chongchongtre20s/video/7693850547647958292) «Podcast 24» | Podcast 1 người kể lại hỏi–đáp | 174s | 864.700 | 124.800 | 279 | 15.700 | 20.450 | 0:00 «nếu chúng mày chuẩn bị đi tắm hoặc nấu cơm, cứ vứt tao ở đâu đó rồi bật max…» | Kể lại cuộc đối thoại với em họ: câu hỏi của em (0:10 «chị có thấy em ngu nhất trong nhà không») → trả lời → hỏi ngược («mày thích gì») |
| [@meomeoreadcoment](https://www.tiktok.com/@meomeoreadcoment/video/7627095729089039636) «Tập 4» | Đọc tin nhắn/thread đóng vai 2 người + bình luận | 80s | 556.300 | 40.800 | 259 | 12.800 | 1.739 | 0:00 «lý do chưa lấy được chồng» (đặt đề) | Hai vai đọc tin nhắn qua lại (0:02–0:33), rồi người dẫn bình luận, chốt ở 0:52 |
| [@camreadwonder](https://www.tiktok.com/@camreadwonder/video/7614813783201975573) | Hỏi–đáp «em hỏi – chị đáp» (không lời nói, chữ trên màn) | 34s | 287.700 | 32.800 | 58 | 2.707 | — | Caption mở bằng câu hỏi: «Em học em không nhớ thì làm sao hả chị?» | Câu hỏi của người học → «chị» trả lời bằng danh sách cách làm |
| [@nhacomeo.mut](https://www.tiktok.com/@nhacomeo.mut/video/7690545961994587412) | Skit công sở nhiều vai (gọi điện, sếp) | 80s | 268.100 | 75.800 | 323 | 9.302 | — | 0:00 «a lô Tin ơi» – «em nghe» | Đổi người nói mỗi 1–2s, lời ngắn, cảnh họp ở giữa clip |
| [@chinhicorner](https://www.tiktok.com/@chinhicorner/video/7633302415793474823) | 2 người hỏi–đáp theo bộ câu hỏi (36 câu hỏi của Arthur Aron) | 146s | 215.200 | 16.800 | 59 | 3.856 | 4.690 | 0:00 «nếu mày được rủ bất cứ ai trên thế giới đi ăn tối, người đó sẽ là ai» | Một người đọc câu hỏi, người kia trả lời; đánh số câu («câu thứ ba» ở 0:34) |
| [@hatmamnho20](https://www.tiktok.com/@hatmamnho20/video/7695072954387942663) | Podcast/kể chuyện giao tiếp | 123s | 128.700 | 17.400 | 37 | 1.097 | 5.947 | 0:00 «các bà có phát hiện ra kỹ năng giao tiếp dễ bị coi thường nhất…» | Nêu nỗi đau → kể chuyện thang máy với sếp (0:11) → lời hứa «một bí kíp duy nhất» (0:38) → ví dụ |
| [@biquyetdodaihoc](https://www.tiktok.com/@biquyetdodaihoc/video/7620113093401627924) | Hỏi–đáp «em hỏi – anh đáp» | 45s | 110.800 | 9.542 | 45 | 2.103 | — | 0:00 «lười học quá bây giờ làm sao anh» | Một câu hỏi, rồi một tràng trả lời kiểu mắng (anti-pattern với L-053) |
| [@nhile_n](https://www.tiktok.com/@nhile_n/video/7269745529582603526) | Skit 2 người, người dạy vặn người học | 114s | 740.300 | 53.000 | 265 | 1.543 | — | 0:02 «em cố gắng đứng lên cho chị coi coi» | Ra lệnh → người kia làm → vặn lại («cái đó là đứng»), lặp 2 vòng rồi mới giải thích (0:38) |
| [@hoaquankhoai](https://www.tiktok.com/@hoaquankhoai/video/7496304128247844103) | Hoạt hình 1 nhân vật nói với «bạn nhỏ» | 64s | 296.400 | 2.639 | 74 | 381 | 718 | 0:08 mới vào lời «chào bạn nhỏ, mình là…» | Độc thoại dạy đạo lý |
| [@quatangcuocsong543](https://www.tiktok.com/@quatangcuocsong543/video/7516045262926662918) | Hoạt hình mẹ–con hỏi–đáp | 52s | 15.300 | 153 | 10 | 158 | 9 | 0:00 «mẹ ơi tại sao con không được chơi điện thoại như các bạn khác» | Con hỏi → mẹ hỏi ngược bằng ví dụ (con lợn) → giảng |

**Quốc tế (podcast clip)**

| Clip | Dài | Play | Like | Cmt | Share | Save | Hook | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| [@onlythegreatminds](https://www.tiktok.com/@onlythegreatminds/video/7312638577257581829) (Bezos, nguồn Lex Fridman Podcast) | 76s | 899.200 | 71.500 | 506 | 826 | 9.392 | 0:00 câu hỏi của host «What's a perfectly productive day in the life of Jeff Bezos?» | Câu hỏi nằm ngay giây 0, sau đó khách trả lời liền một mạch |
| [@thediaryofaceofanpodcast](https://www.tiktok.com/@thediaryofaceofanpodcast/video/7696938641238527245) «Part 02» | 435s | 167.600 | 8.866 | 69 | 1.578 | 6.509 | Caption «No. 1 Neuroscientist Reveals How To UNLOCK Superhuman Focus…» | Host hỏi «where's the first place to start? What's the first domino?» (0:39–0:41) |
| [@twobrokechicks_](https://www.tiktok.com/@twobrokechicks_/video/7425885274367937812) | 21s | 14.400 | 729 | 17 | 27 | 43 | — | Podcast nhỏ |
| [@transform.podcast](https://www.tiktok.com/@transform.podcast/video/7475771177265351967) / [@365podcastshow](https://www.tiktok.com/@365podcastshow/video/7663974962163748104) / [@kali_onthe_daily](https://www.tiktok.com/@kali_onthe_daily/video/7637311204628630797) | 58s / 33s / 86s | 1.179 / 781 / 488 | 73 / 14 / 52 | 0 / 0 / 1 | 1 / 1 / 0 | 9 / 4 / 5 | Mở bằng «tips…», «want to boost your productivity…» | Clip podcast chung chung, hook không có câu hỏi hay nỗi đau cụ thể → gần như không ai xem |

### 2.3 Kỹ thuật lặp lại (rút từ bảng trên)

- **K1. Câu hỏi của người hỏi nằm ở giây 0, nói đúng nỗi đau.** Gặp ở @biquyetdodaihoc («lười học quá bây giờ làm sao anh», 0:00), @camreadwonder («Em học em không nhớ thì làm sao hả chị?»), @quatangcuocsong543 (0:00), @chinhicorner (0:00), @onlythegreatminds (0:00, 899.200 play). Ngược lại, ba clip podcast quốc tế mở bằng «tips/boost your productivity» chỉ được 488–1.179 play. Kỹ thuật này khớp L-057/L-058: người hỏi (Omi) nói nỗi đau và câu hỏi, người đáp (Thầy) không phải tự kể lể.
- **K2. Đổi người nói nhanh, chen một câu cụt để đổi nhịp.** @nhacomeo.mut đổi vai mỗi 1–2s (VTT 0:00–0:04). @nhile_n lặp nhịp «ra lệnh → làm → vặn lại» trong khoảng 2s/lượt (0:02–0:12) rồi mới giải thích ở 0:38. @meomeoread đọc tin nhắn hai vai qua lại. Áp vào D1: câu Omi ngắn (L08 «Họp đứng luôn hả Thầy?»), Thầy không nói liền quá 2 câu.
- **K3. Dạng podcast/danh sách được lưu (save) nhiều. Dạng skit được chia sẻ (share) nhiều.** Save/play: @hatmamnho20 4,6%, @thediaryofaceofanpodcast 3,9%, @vuilenreview 2,6% ([link](https://www.tiktok.com/@vuilenreview/video/7532327044391128338)), @chongchongtre20s 2,4%, @chinhicorner 2,2%. Skit/đọc tin nhắn: @meomeoreadcoment save 0,3% nhưng share 2,3%; @phuong183cobao ([link](https://www.tiktok.com/@phuong183cobao/video/7642565100225727765)) save 0,2%, share 2,3%. Có cả câu mời nghe nền hoặc lưu lại: @chongchongtre20s «cứ vứt tao ở đâu đó rồi bật…» (0:00–0:04); @sabito_0668 «lưu lại nhé» (606.000 play, 14.200 share; [link](https://www.tiktok.com/@sabito_0668/video/7670995147995237640)). Nghĩa là nếu clip có dẫn chứng/cách làm (D1, D5) thì CTA nên mời lưu; nếu là skit (D4) thì mời gửi cho bạn.
- **K4. Đánh số tập / «trả lời @» và nhá phần sau.** @meomeoreadcoment «Tập 4»; @chongchongtre20s «Podcast 24»; @thediaryofaceofanpodcast «Part 02»; @cici_channel88 «Trả lời @… P3» và câu chốt 0:31 «…ở phần 4» (159.200 play; [link](https://www.tiktok.com/@cici_channel88/video/7697330701036686613)); @huylaconmeo777 «Trả lời @…» (94.000 play, 3.176 share; [link](https://www.tiktok.com/@huylaconmeo777/video/7694905374146710802)); @nhahang5sao «trả lời bình luận quý khách phần 18» (comment/play cao nhất mẫu 3,99%, nhưng chỉ 3.781 play; [link](https://www.tiktok.com/@nhahang5sao/video/7697983010695695637)). Đây là nền cho D3 và D6.
- **K5. Caption mời bổ sung, CTA là câu hỏi mở.** Data cũ 16/10: @hoaquynh0000 «Còn tư duy nào nữa không mn? Comment để học hỏi nào?» (1.400.000 play, 538 cmt; [link](https://www.tiktok.com/@hoaquynh0000/video/7680893073684958482)), @iamuyenvu «Bạn nào còn thêm kinh nghiệm…» (459.100 play, 205 cmt; [link](https://www.tiktok.com/@iamuyenvu/video/7635280411198901520)). Lưu ý: comment/play của mọi clip trong mẫu đều thấp (0,01–0,11%, trừ @nhahang5sao), nên **không có bằng chứng** CTA comment làm clip lên xu hướng. Chỉ thấy đây là cách các clip này mời tương tác.

**Anti-pattern trong data:**
- Hỏi–đáp mà trả lời bằng cách mắng: @biquyetdodaihoc «lười cái gì mày…», like/play 8,6%. Clip vẫn sống nhưng trái L-053, không dùng.
- Hoạt hình dạy đạo lý độc thoại, hook vào trễ: @hoaquankhoai mở lời ở 0:08, like/play chỉ 0,9%. @quatangcuocsong543 dạng mẹ–con 52s chỉ 15.300 play.
- Hook giả khan hiếm «xoá video sau 24 tiếng» (đã ghi trong `patterns.md` 20/10).

---

## 3. Đề xuất định dạng thử đầu tiên: D1 — Hỏi–đáp Thầy–Omi 45–60s

Lý do:
1. Hook có câu hỏi ở giây 0 (K1) đúng luật kênh (L-057/L-058). Câu hỏi do Omi nói, nên Thầy không phải chê người xem (L-053).
2. Ít việc mới nhất trên pipeline: vẫn comic, vẫn F5 hai giọng đã có, vẫn ≤ 60s, không cần Podcastfy hay TTS mới. Podcastfy chỉ là tuỳ chọn để nháp, bản chính vẫn viết tay qua gate Hiệp.
3. Mỗi câu của Thầy đối chiếu được với một dòng fact-lock, nên kiểm bịa fact dễ hơn D4 hay D5.
4. Sau này bọc thành D6 («Tập n» theo phần 4) hoặc D3 khi kênh có comment thật.

**Transcript mẫu:** `research/agents/podcastfy-sample-transcript-2026-10-20.md`. Dùng **mục 4.5** (phần 4, «Trước họp gửi chương trình… họp đứng được thì họp đứng»; mức B; Leach và cộng sự 2009, Bluedorn và cộng sự 1999). Bản mẫu có 11 lượt thoại, khoảng 240 âm tiết, ước 48–54s lời. File có trích nguyên văn item, fact-lock F1–F10, cột đối chiếu từng câu và dòng credit. Mục này chưa nằm trong 30 slot của `content/theme-map.md`.

Cần lưu ý: Omi chỉ được xuất hiện từ tuần 5 (L-011). Nếu thử sớm hơn, Hiệp quyết định đổi vai.

Credit (thẻ cuối + caption): Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/

---

## 4. Không tìm được / giới hạn
- **Không tìm thấy** clip comic hoặc hoạt hình hỏi–đáp hai nhân vật về năng suất ở VN có số liệu tốt trong mẫu 30 clip. Các clip hoạt hình tìm được đều là chuyện đạo lý trẻ em, tương tác thấp.
- **Không có dữ liệu giữ chân người xem** (watch time, completion, loop). Apify không trả về các số này, nên không đánh giá được kỹ thuật loop. Trong mẫu cũng không thấy clip nào cố ý làm loop.
- **Không có số liệu thật cho YouTube và Spotify** ở lượt này (không gọi thêm nguồn). Phần D5 cho nền tảng ngoài TikTok chỉ dựa trên đặc điểm định dạng, chưa có bằng chứng trend.
- Chưa lấy comment cho các clip mới (để giữ chi phí nhỏ), nên chưa rút được câu nỗi đau từ comment.
- Mẫu nhỏ (30 clip mới + khoảng 6 clip cũ), tìm theo từ khoá, không phải bảng xếp hạng trend. Tỉ lệ save/share ở K3 là quan sát trên mẫu này, chưa phải quy luật.
- VTT tự động của TikTok sai chính tả nhiều. Các câu trích hook ở trên đã sửa chính tả nhẹ cho dễ đọc; bản gốc xem `vtt/`.
