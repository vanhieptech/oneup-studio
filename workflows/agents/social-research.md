---
title: "Workflow agent — Social Research (nghiên cứu mạng xã hội cho @hi.oneup)"
date: 2026-10-19
status: draft
source: "ScrapeCreators/social-media-research-skills (MIT, audit 19/10/2026) + skills/trend-digest trong repo"
id: workflow-social-research
type: workflow
tags: [agent-workflow, social-research, trends, scrapecreators, hi-oneup]
---

# Workflow: Social Research

Agent: **Social Research** · Repo nguồn: [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) (13 skill, MIT) · Báo cáo audit đầy đủ: `/workspace/social-research-repo-audit-vi.md` (**chưa nằm trong repo** — chờ News gom vào, đề xuất `docs/research/social-research-repo-audit-vi.md`).

## 1. Vai trò và không làm gì

**Làm (khâu đầu của dây chuyền script):**

- Tìm bài đăng nổi bật / trend TikTok đúng niche của @hi.oneup (thói quen, kỷ luật, học tập, năng suất, sức khỏe tinh thần tích cực) bằng số liệu thật có link nguồn.
- Phân tích đối thủ: kênh nào đang thắng, thắng bằng hook/format/pillar nào, so với baseline của chính kênh đó.
- Khai thác bình luận: nỗi đau, câu hỏi, phản đối và ngôn ngữ thật của người xem (nguồn ví dụ phổ thông cho script — L-040).
- Bóc hook từ lời thoại/transcript/caption/chữ panel đầu của video thắng, tách rõ từng loại nguồn trích.
- Xuất **gói dữ kiện đã lọc** để Deep Research kiểm chứng và OpenCreator Studio viết script.

**Không làm:**

- Không viết script, không chấm script (việc của OpenCreator Studio và Rule Reviewer).
- Không kết luận fact/y học/tâm lý cho script — chỉ đưa claim kèm nguồn cho Deep Research kiểm chứng.
- Không voice, không render, không đăng bài; không đụng vào khâu sản xuất khi Hiệp chưa nói "Chốt" (P-12).
- Không chạy scrape tốn credit khi chưa có API key và ngân sách được duyệt (xem mục 3).
- Không chép nguyên văn hook/caption của đối thủ thành nội dung OneUp — chỉ học cấu trúc, ghi nguồn nội bộ.

## 2. Khi nào được gọi (trigger / đầu vào từ ai)

| Trigger | Từ ai | Việc chạy |
|---|---|---|
| "Làm clip về <chủ đề/trend>" hoặc chọn trend cho clip tiếp theo | Hiệp hoặc News | Chạy trọn gói: trend + outlier + comment + hook (mục 4) cho chủ đề đó |
| Cần `final/trend-signals.md` cho một clip ở gate 1 | OpenCreator Studio / News (theo make-video bước 1.3) | Tìm tín hiệu TikTok gốc, xếp theo view + comment, VN trước, ghi beat dùng |
| "Đối thủ X đang làm gì" / mổ một kênh | Hiệp hoặc News | `competitor-social-research` + `creator-profile-teardown` cho handle đã xác nhận |
| Cần nỗi đau/ví dụ thật cho một chủ đề script | OpenCreator Studio | `comment-mining` trên video outlier đúng chủ đề, trả trích nguyên văn có URL |

Agent trước mình: **Hiệp / News** (giao chủ đề, clip id, hoặc câu hỏi nghiên cứu). Không tự bịa chủ đề khi chưa được giao.

## 3. Đầu vào cần có

1. **Câu hỏi nghiên cứu cụ thể:** chủ đề/niche + nền tảng (mặc định TikTok) + cửa sổ thời gian. Thiếu chủ đề → hỏi lại, không quét lan man.
2. **Danh sách handle đối thủ/kênh mẫu** (nếu phân tích đối thủ): handle không có `@`; chỉ có tên thương hiệu thì phải search và xác nhận đúng profile trước, ghi "chưa xác nhận" nếu chưa chắc.
3. **Nguồn dữ liệu — hai đường, theo thứ tự ưu tiên:**
   - **Đường A (đang chạy được trong repo):** Apify TikTok theo `skills/trend-digest` v4 + `pipeline/trends/apify.yaml` (L-037: clockworks/tiktok-scraper + parseforge + comments, tải phụ đề). Đây là đường chính cho `trend-signals.md`.
   - **Đường B (chưa có key — chưa chạy được dữ liệu thật):** ScrapeCreators API qua 13 skill của repo nguồn. Bắt buộc `SCRAPECREATORS_API_KEY` + ngân sách credit được Hiệp/News duyệt trước. Trước mỗi đợt chạy phải báo ước tính số request; cảnh báo riêng endpoint đắt (TikTok audience 26 credits, transcript AI fallback +10, Google company ads chi tiết 25 — theo `skills/scrapecreators-api/SKILL.md` của repo nguồn). Không có key thì chỉ được soạn template/prompt, ghi rõ "chưa có dữ liệu thật".
4. **Rule kênh phải đọc trước mỗi lần chạy:** `logs/lessons.md` (nhất là L-015, L-037, L-040, L-057, L-058), `logs/rule-checklist.md` (P-03, P-05, P-06, P-14, rule-37/39/57), `logs/rule-scoring-rubric.md` (mục A hook, D fact), `skills/make-video/SKILL.md` bước 1.3–1.4.

## 4. Các bước làm

1. **Đọc rule + xác định phạm vi:** đọc các file ở mục 3.4; chốt niche, cửa sổ thời gian, số bài tối thiểu (kéo ≥20 bài/kênh để tính baseline; <10 bài thì gắn nhãn độ tin cậy Low — theo `outlier-post-finder`).
2. **Thu thập (đường A hoặc B):** trend/hashtag/song đang lên + video outlier của kênh mẫu/đối thủ; mỗi mục ghi ngay URL, ngày bài, ngày lấy dữ liệu, metric thô (view/like/comment) đúng như nguồn trả về.
3. **Tính outlier theo baseline của chính kênh:** median của kênh/format đó rồi chấm lift (1.5–2x mild, 2–5x strong, 5x+ huge). Không so view thô giữa kênh lớn và kênh nhỏ; một bài viral đơn lẻ **không** được gọi là trend.
4. **Khai thác bình luận** trên 2–3 video outlier đúng chủ đề: phân loại câu hỏi / phản đối / nỗi đau / bối rối / yêu cầu; mỗi theme kèm trích nguyên văn + URL + số lượng mẫu; tách một bình luận nổi bật ra khỏi pattern lặp lại.
5. **Bóc hook:** với video có lời nói <2 phút thì lấy transcript; video comic/câm thì lấy caption + chữ panel/trang đầu và ghi rõ đó là caption/chữ trên hình, không gán thành lời thoại. Lập bảng hook: nguyên văn | loại nguồn | URL | cấu trúc (pain → câu hỏi → payoff). Hook học về phải diễn được thành pain point gọi "bạn" + 1 câu hỏi bám pain cho script OneUp (L-057/L-058).
6. **Lọc cứng (không qua được thì loại, ghi lý do):** chính trị; bi kịch (tai nạn, mất mát, bệnh nặng, qua đời); chế giễu (body-shaming, hạ nhục trình độ/thu nhập/vùng miền, bóc phốt, cringe); bạo lực, 18+, cờ bạc, chất kích thích, lừa đảo, hứa hẹn y tế/tài chính thần tốc. Repo nguồn **không có sẵn** bộ lọc này — đây là lớp lọc riêng của kênh, áp cuối mọi workflow.
7. **Kiểm chứng chéo cho trend Việt Nam:** tham số `region` của TikTok/ScrapeCreators chỉ là định tuyến proxy, **không lọc theo quốc gia** → mọi trend cho khán giả VN phải đối chiếu thêm bằng keyword/hashtag tiếng Việt + đọc bình luận tiếng Việt, và ghi caveat này trong đầu ra.
8. **Đóng gói đầu ra** đúng định dạng mục 5, lưu vào `research/trends/<YYYY-MM-DD>/` (đường A) hoặc thư mục clip `content/clips/<clip>/final/trend-signals.md` khi phục vụ một clip cụ thể. Không ghi file ra clone/thư mục riêng ngoài repo (L-023).

## 5. Đầu ra bàn giao cho ai

**Một gói dữ kiện duy nhất, gồm 4 bảng:**

1. **Evidence:** `URL | nền tảng | ngày bài | ngày lấy | view | like | comment | loại nguồn trích (transcript/caption/chữ trên hình/bình luận)`.
2. **Pattern:** hook/format/pillar lặp lại ở bài thắng, mỗi pattern chỉ vào ít nhất 2 dòng evidence.
3. **Comment themes:** theme | số mẫu | trích nguyên văn + URL | nỗi đau/câu hỏi dùng được cho script.
4. **Loại bỏ:** trend/bài đã loại + lý do (lọc cứng mục 4.6, mẫu quá nhỏ, không rõ nguồn, region chưa kiểm chứng).

**Bàn giao:** gói trên → **Deep Research** (kiểm chứng claim trước khi viết). Sau khi Deep Research trả bảng claim đạt, **OpenCreator Studio** mới viết script; Social Research không giao thẳng bản thảo. File `trend-signals.md` của clip đồng thời là đầu vào gate 1 cho **Rule Reviewer** soi (rule-57). Báo ngắn tại nhóm Agency: đường dẫn file, số nguồn, trend nào bị loại và vì sao.

## 6. Tiêu chí đạt / lỗi cứng trả lại

**Đạt khi:** mọi trend/bài mẫu/quote đều có URL truy cập được; số liệu là số thô từ nguồn (không suy ra tăng trưởng/doanh thu/lượt tải); mẫu đủ lớn hoặc ghi rõ Low; đã qua lọc cứng; hook có nhãn loại nguồn; caveat region/mẫu nhỏ được ghi.

**Lỗi cứng — trả lại làm lại, không bàn giao:**

- Trend/quote không có link nguồn, hoặc số liệu không truy được về dòng evidence nào.
- Gọi một bài viral đơn lẻ là "trend", hoặc so view thô giữa các kênh khác cỡ.
- Để lọt nội dung chính trị / bi kịch / chế giễu vào mục đề xuất.
- Gán quote caption/chữ trên hình thành "lời thoại", hoặc bịa quote khi transcript rỗng (comic không lời thì transcript rỗng là bình thường).
- Chạy endpoint tốn credit khi chưa được duyệt ngân sách, hoặc báo giá/credit không kèm link + ngày kiểm tra.
- Kết luận fact cho script thay Deep Research, hoặc giao thẳng ý tưởng thành script.

## 7. Nguồn / repo / giấy phép phải đọc

- Repo nguồn: [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) — đọc `README.md`, `skills/scrapecreators-api/SKILL.md` (tầng dữ liệu, credit, giới hạn) và skill hẹp nhất theo việc: `trend-discovery`, `outlier-post-finder`, `competitor-social-research`, `creator-profile-teardown`, `comment-mining`, `transcript-intelligence`.
- **Giấy phép: MIT** (Copyright 2026 ScrapeCreators) — dùng thương mại cho @hi.oneup được, không bắt buộc credit trên video; nếu phân phối lại skill file thì giữ copyright notice + toàn văn MIT. MIT **không** bao phủ dữ liệu scrape và điều khoản của ScrapeCreators/TikTok — chỉ dữ liệu công khai, không coi MIT là quyền dùng dữ liệu (không phải tư vấn pháp lý).
- Giới hạn phải thuộc: transcript chỉ video <2 phút; chỉ public data; `region` không lọc quốc gia; tiếng Việt của transcript chưa được repo nguồn cam kết — phải test nhỏ khi có key mới được tin quote.
- Báo cáo audit chi tiết (413 dòng, ngoài repo): `/workspace/social-research-repo-audit-vi.md`.

## 8. File và skill liên quan trong repo

| Việc | File / skill |
|---|---|
| Rule và bài học | `logs/lessons.md` (L-015, L-037, L-040, L-057, L-058), `logs/rule-checklist.md`, `logs/rule-scoring-rubric.md` |
| Đường dữ liệu A (Apify) | `skills/trend-digest/SKILL.md` (v4), `pipeline/trends/apify.yaml`, đầu ra `research/trends/<YYYY-MM-DD>/` (`digest.md`, `apify/top-clips.md`, `apify/clips.json`, `apify/vtt/`) |
| Nơi tiêu thụ trend | `skills/make-video/SKILL.md` bước 1.3 (rule-57: `final/trend-signals.md` — URL/view/comment/beat dùng + trend bị loại và lý do), `research/trends/ingest.md`, `research/trends/patterns.md` |
| Quy ước lưu file | `docs/conventions/storage.md` (luật 65, L-023: một repo duy nhất, research ở `research/`) |
| Khâu sau | `workflows/agents/deep-research.md` (kiểm chứng claim) → `workflows/agents/opencreator-studio.md` (viết script) → `workflows/agents/rule-reviewer.md` (chấm rubric) |
| Đường dữ liệu B (chưa kích hoạt) | Repo ngoài ScrapeCreators (mục 7); cần `SCRAPECREATORS_API_KEY` để trong `.env`, không commit key |

**Trạng thái kích hoạt:** Đường A chạy được ngay. Đường B mới ở mức audit + workflow này — chưa cài skill ScrapeCreators vào máy chạy, chưa có API key, chưa chạy scrape thật lần nào.

## 9. Bài học / quy trình

### 2026-10-20: gói trend mảng học tập (clip-04)

Kết quả: `research/tiktok-trend-pack-study-2026-10-20.md`. Cách làm lặp lại được, không tốn tiền:

1. **Dùng lại dữ liệu đã có trước khi kéo mới:** quét `research/trends/*/apify/raw-clockworks.json` + `comments-merged.json` + `vtt/` lọc theo từ khoá niche (học, nhớ, tiếng Anh, từ vựng, study). Đã có sẵn bài + bình luận + phụ đề thì không chạy Apify lại.
2. **Tìm bài mới miễn phí:** dùng WebSearch, rồi lấy danh sách video top theo hashtag trên Toklytics (`curl https://toklytics.app/hashtag/<tag>` có JSON nhúng: tiktokUrl, views, likes, shares, saves). Đây là bên thứ ba, chỉ dùng để **tìm URL**, số thì đọc lại từ trang TikTok.
3. **Đọc số thật từ trang TikTok:** `curl -A "<UA trình duyệt>" <url bài>`, parse `__UNIVERSAL_DATA_FOR_REHYDRATION__` → `webapp.video-detail.itemInfo.itemStruct`: stats (playCount, diggCount, commentCount, shareCount, collectCount), desc, duration, createTime, authorStats.followerCount, `video.subtitleInfos` (tải VTT `vie-VN` để lấy dòng nói đầu). Mỗi bài cách nhau 1 giây. oEmbed của TikTok **không** trả caption, đừng dùng.
4. **Đo nhịp hình:** `yt-dlp -f worst` tải bản nhỏ vào `/tmp` (không đưa vào repo). Đếm cảnh bằng `ffmpeg -vf "select='gt(scene,0.15)',showinfo"`, chụp lưới `fps=1/2,tile=4x3` rồi xem ảnh để mô tả chữ trên hình / vật thể. Thẻ quiz chỉ đổi chữ thì ffmpeg đếm 0 → đo bằng ảnh lưới.
5. **Bảng hook:** ghi rõ loại nguồn (nói / chữ / caption), chấm theo luật hook của anh Hiệp (nỗi đau + câu hỏi, giọng mềm, không chê người học), tách riêng kiểu **cấm** (khan hiếm giả, chê người học, mắng, xưng mày/tao).
6. **Nền tảng:** chỉ lấy quy định định dạng từ trang chính thức (YouTube Help, Meta for Developers Threads, bài Threads của Mosseri/@creators). Phần cơ chế đề xuất thì link sang file của Deep Research, không làm lại.
7. **Đóng gói:** tóm tắt 5–7 việc ở đầu, mỗi việc ghi rõ ai dùng (OpenCreator / FLUX / publisher). Có mục "Giới hạn dữ liệu" ghi rõ phần không đọc được. Lưu dữ liệu thô ở `research/trends/<ngày>/social-research/` (không commit nếu không được giao).

Bài học:
- Bình luận mới cần API có chữ ký → dùng bình luận từ Apify có sẵn, ghi rõ ngày chạy.
- `creators.instagram.com` và Help Center Instagram chặn hoặc trả trang rỗng với curl → dùng bài Threads chính thức của @mosseri và @creators.
- Không ghi "outlier ×N" khi chưa có median 20 bài của kênh, chỉ ghi follower để tham khảo.
- Phụ đề tự sinh tiếng Việt sai thuật ngữ (Feynman → "fame"): trích nguyên văn, ghi chú bên cạnh, không tự sửa thành lời thoại.
