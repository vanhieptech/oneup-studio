---
title: "Nghiên cứu: social-media-research-skills"
date: 2026-10-19
source: "agent research 19/10/2026 (goc o /workspace, da gom vao repo)"
id: research.social-research-audit
type: research
status: reference
updated: 2026-10-19
tags: [social, trend, research]
---
# Báo cáo nền: Audit repo `social-media-research-skills` cho kênh TikTok @hi.oneup (OneUp)

> **Ngày audit:** 19/10/2026 (Asia/Saigon)  
> **Repo được audit:** [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)  
> **Commit đã clone/đọc:** `64ba7b4dea71e130d2712ffb6c1c1024b3b7c4b2` — *Merge pull request #6 from ScrapeCreators/docs/add-mit-license*  
> **Phiên bản plugin khai báo:** `1.0.0` ([`.claude-plugin/plugin.json`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/.claude-plugin/plugin.json))  
> **Đối tượng áp dụng:** TikTok `@hi.oneup` — OneUp, app phát triển bản thân/thói quen, nhân vật Omi, định dạng **comic-only series**.  
> **Phạm vi audit này:** Chỉ đọc/clone repo và tài liệu công khai liên kết từ repo. **Không chạy scrape thật, không dùng API key nào.**  
> **Nguyên tắc xuyên suốt báo cáo (bắt buộc cho @hi.oneup):** Loại bỏ nội dung chính trị, bi kịch, chế giễu; mọi trend/đề xuất phải có link nguồn; không bịa số liệu — số nào không có trong nguồn thì ghi "không có dữ liệu / chưa kiểm chứng".

---

## Tóm tắt điều hành (đọc 2 phút)

| Câu hỏi | Trả lời ngắn |
|---|---|
| Repo gồm mấy skill? | **13 skill**: 1 skill tầng dữ liệu (`scrapecreators-api`) + 12 skill workflow. Xem bảng §2. Nguồn: [README — Available Skills](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md) và thư mục [`skills/`](https://github.com/ScrapeCreators/social-media-research-skills/tree/main/skills) |
| License gì? Dùng thương mại cho @hi.oneup được không? | **MIT License, Copyright (c) 2026 ScrapeCreators**. Được dùng thương mại, sửa, phân phối lại — điều kiện chính là giữ thông báo bản quyền + nội dung license trong các bản sao/phần đáng kể của phần mềm. Xem §3. Nguồn: [LICENSE](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/LICENSE) |
| Có cần API key / trả phí không? | **Có, bắt buộc có `SCRAPECREATORS_API_KEY`** để lấy dữ liệu thật. Repo chỉ hướng dẫn lấy key tại scrapecreators.com, không ghi giá trong repo. Website chính thức (ngoài repo) ghi có gói free credits và các gói pay-as-you-go — giá phải kiểm tra lại tại nguồn tại thời điểm mua, không coi số trong báo cáo này là cam kết. Xem §4. Nguồn repo: [README — Setup](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md); nguồn giá hiện hành: [scrapecreators.com](https://scrapecreators.com) |
| Repo tự scrape hay dựa vào API? | **Dựa hoàn toàn vào ScrapeCreators REST API** (`https://api.scrapecreators.com`) làm tầng dữ liệu. Các skill là file markdown workflow (`SKILL.md`) hướng dẫn agent gọi endpoint nào, phân tích ra sao, xuất artifact gì — không phải code scraper tự vận hành độc lập. Nguồn: [`skills/scrapecreators-api/SKILL.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md) |
| 4 việc chính cho @hi.oneup map thế nào? | (a) Trend/bài nổi bật → `trend-discovery` + `outlier-post-finder` — **khá tốt**; (b) Đối thủ → `competitor-social-research` + `creator-profile-teardown` — **tốt nếu có handle đối thủ rõ ràng**; (c) Comment mining → `comment-mining` — **tốt cho TikTok/YouTube/IG/FB/Reddit có endpoint comments**; (d) Hook từ transcript → `transcript-intelligence` — **tốt cho video nói, hạn chế lớn với comic-only không lời thoại**. Chi tiết §6 |
| Rủi ro/giới hạn chính? | Chỉ dữ liệu công khai; transcript chỉ video <2 phút; một số endpoint rất đắt credit (audience = 26 credits); region trên TikTok trending/search là proxy routing, **không phải lọc theo quốc gia**; không có sẵn bộ lọc chính trị/bi kịch/chế giễu cho OneUp — phải tự thêm lớp lọc thủ công/bằng prompt; nguy cơ tốn credit khi phân trang sâu; không được bịa quote/số liệu. Xem §5, §7, §8 |

**Kết luận go/no-go:** **GO có điều kiện** — dùng được làm nền nghiên cứu cho Social Research agent, *sau khi* (1) có API key và ngân sách credit được duyệt riêng, (2) bổ sung checklist lọc nội dung OneUp ở §7 vào mọi prompt chạy skill, (3) chấp nhận transcript không phải nguồn hook chính cho comic-only — phải kết hợp caption/chữ trên hình (on-screen text) và comments.

---

## 1. Repo là gì, cấu trúc ra sao

### 1.1. Định vị theo chính repo

Repo tự mô tả là *"Practical AI agent skills for social media research, powered by ScrapeCreators"* — bộ skill giúp agent tìm bài đăng vượt trội (outlier), khai thác bình luận, tóm tắt transcript, phân tích đối thủ, phân tích thư viện quảng cáo, và biến dữ liệu xã hội công khai thành artifact dùng được cho kinh doanh. Nguồn: [README](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md).

Nguyên tắc thiết kế repo tự công bố (quan trọng, nên giữ nguyên khi áp cho OneUp):

1. *Workflow-first, API-second* — người dùng hỏi kết quả kinh doanh, không hỏi endpoint.
2. *Public-data only* — chỉ dữ liệu công khai, không hứa dữ liệu đăng nhập/riêng tư.
3. *Cited outputs* — kèm URL nguồn cho bài/vídeo/quảng cáo/bình luận khi có thể.
4. *Baseline-aware analysis* — đánh giá hiệu quả so với mức bình thường của chính tài khoản đó, không chỉ số tuyệt đối.
5. *Exact language matters* — giữ nguyên văn bình luận, hook, caption, câu transcript hữu ích.
6. *Keep outputs actionable* — kết thúc bằng pattern, khuyến nghị, ý tưởng test, hoặc CSV.

Nguồn: [README — Design Principles](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md).

### 1.2. Cấu trúc thư mục (tại commit đã audit)

```text
social-media-research-skills/
├── .claude-plugin/
│   ├── plugin.json          # name, version 1.0.0, license MIT, skills: ./skills
│   └── marketplace.json     # metadata đăng ký marketplace plugin
├── AGENTS.md                # quy ước viết skill, validation
├── CLAUDE.md                # chỉ dẫn chọn skill theo loại việc cho Claude
├── LICENSE                  # MIT License (xem §3)
├── README.md                # cài đặt, setup key, bảng 13 skill, prompt mẫu
├── scripts/
│   └── validate-skills.py   # kiểm tra frontmatter SKILL.md (name, description ≤1024 ký tự, body không rỗng)
└── skills/
    ├── ad-library-teardown/SKILL.md
    ├── audience-research/SKILL.md
    ├── comment-mining/SKILL.md
    ├── competitor-social-research/SKILL.md
    ├── content-repurposing/SKILL.md
    ├── creator-profile-teardown/SKILL.md
    ├── influencer-prospecting/SKILL.md
    ├── outlier-post-finder/SKILL.md
    ├── product-demand-research/SKILL.md
    ├── scrapecreators-api/SKILL.md      # 291 dòng — skill lớn nhất, tầng dữ liệu
    ├── social-listening-brief/SKILL.md
    ├── transcript-intelligence/SKILL.md
    └── trend-discovery/SKILL.md
```

Nguồn trực tiếp: clone tại commit nêu trên; danh sách file khớp với cây thư mục [trên GitHub](https://github.com/ScrapeCreators/social-media-research-skills/tree/main/skills).

**Hiểu đúng bản chất:** Mỗi skill là **một file `SKILL.md`** gồm frontmatter (tên, mô tả kích hoạt, `allowed-tools`, yêu cầu env `SCRAPECREATORS_API_KEY`, license MIT trong metadata của hầu hết workflow skill) + thân markdown mô tả workflow, bảng endpoint, format output, và "common pitfalls". Đây là *hướng dẫn cho AI agent*, không phải thư viện code có hàm chạy độc lập. File Python duy nhất là script validate frontmatter, không phải scraper. Nguồn: từng `SKILL.md` trong [`skills/`](https://github.com/ScrapeCreators/social-media-research-skills/tree/main/skills) và [`scripts/validate-skills.py`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/scripts/validate-skills.py).

### 1.3. Cách cài và dùng (theo README)

```bash
npx skills add ScrapeCreators/social-media-research-skills
```

```bash
export SCRAPECREATORS_API_KEY=sk_...
# Lấy key tại https://scrapecreators.com
```

Repo tuyên bố tương thích với Claude Code, Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, Windsurf, VS Code, và các agent hỗ trợ đặc tả Agent Skills. Nguồn: [README — Install/Setup](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md) (repo dẫn tới https://agentskills.io cho đặc tả).

Cách các skill phối hợp (sơ đồ trong README):

```text
scrapecreators-api          ← tầng dữ liệu (endpoint routing)
        │
        ▼
12 workflow skill           ← mỗi skill ra một artifact: report / brief / table / CSV / swipe file
```

Nguồn: [README — How the Skills Work Together](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md).

`CLAUDE.md` của repo cũng chỉ dẫn chọn skill hẹp nhất theo việc: outlier → `outlier-post-finder`, transcript → `transcript-intelligence`, comment/VOC → `comment-mining`, đối thủ → `competitor-social-research`, quảng cáo → `ad-library-teardown`, tra endpoint thô → `scrapecreators-api`. Nguồn: [CLAUDE.md](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/CLAUDE.md).

---

## 2. Liệt kê đầy đủ 13 skill: tên, mục đích, input, output

Bảng dưới tổng hợp từ README và từng `SKILL.md`. Cột "Khi nào dùng" lấy từ trường `description` và mục *When to Use* của mỗi skill.

| # | Skill | Mục đích (một câu) | Input điển hình cần có | Output cam kết trong skill |
|---|---|---|---|---|
| 1 | [`scrapecreators-api`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md) | Tầng dữ liệu: định tuyến yêu cầu scrape thô tới đúng endpoint ScrapeCreators (repo ghi 110 endpoints, 27+ nền tảng trong frontmatter) | `SCRAPECREATORS_API_KEY`; handle (không có `@`), URL bài/vídeo, query, hashtag (không có `#`) | Lời gọi API (GET + header `x-api-key`), JSON trả về, hướng dẫn phân trang; phải fetch OpenAPI spec từng endpoint trước khi gọi |
| 2 | [`outlier-post-finder`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/outlier-post-finder/SKILL.md) | Tìm bài/reel/short/tweet/vídeo vượt baseline của chính tài khoản, giải thích vì sao hiệu quả | Handle/URL, nền tảng, cửa sổ thời gian/số bài (skill khuyên kéo ≥20 bài, <10 bài thì độ tin cậy thấp) | Bảng outlier có lift (1.5x–2x mild, 2x–5x strong, 5x+ huge), pattern lặp lại, "Hooks to Steal", ý tưởng nội dung |
| 3 | [`transcript-intelligence`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/transcript-intelligence/SKILL.md) | Phân tích transcript video: hook, claim, quote, CTA, "content atoms" | URL video (TikTok/IG/YouTube/Facebook/X/LinkedIn/Rumble/Reddit) hoặc handle để tự tìm video | Báo cáo theo từng transcript + pattern xuyên tập, Hooks Swipe File, ý tưởng repurpose |
| 4 | [`comment-mining`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/comment-mining/SKILL.md) | Khai thác bình luận: câu hỏi, phản đối, pain point, ý định mua, ngôn ngữ khách hàng (VOC) | URL bài/vídeo; phân trang khi cần chiều sâu | VOC report: bảng theme (tần suất × cường độ), câu hỏi, objections, buying intent, trích nguyên văn, ý tưởng nội dung/FAQ |
| 5 | [`competitor-social-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/competitor-social-research/SKILL.md) | So sánh chiến lược social của đối thủ, tìm khoảng trống nội dung | Danh sách handle/URL đối thủ + nền tảng; nếu chỉ có tên công ty phải search & xác nhận profile trước | Competitor brief: snapshot, content pillars, outlier từng đối thủ, gaps/opportunities, content test đề xuất, mục Sources có URL |
| 6 | [`creator-profile-teardown`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/creator-profile-teardown/SKILL.md) | "Mổ xẻ" một creator/kênh brand: positioning, pillars, hook, format, cái nên/không nên copy | Một handle/URL kênh | Teardown: positioning, bảng pillars kèm ví dụ, outlier, hooks/formats to steal, tests for us |
| 7 | [`trend-discovery`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/trend-discovery/SKILL.md) | Tìm trend chủ đề/hashtag/âm thanh/format trong một niche, xếp hạng bằng chứng | Niche, quốc gia/khu vực, nền tảng, độ nhạy thời gian | Trend brief: bảng trend kèm evidence, sounds/hashtags/formats, bài mẫu có link, content ideas, caveats |
| 8 | [`social-listening-brief`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/social-listening-brief/SKILL.md) | Nghe xem cộng đồng đang nói gì về brand/chủ đề/danh mục trên nhiều nguồn | Chủ đề + alias/tên đối thủ + cửa sổ ngày | Brief đa nguồn: theme, sentiment (có caveat), bài đáng chú ý có link, risks/opportunities, hành động đề xuất |
| 9 | [`product-demand-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/product-demand-research/SKILL.md) | Kiểm chứng nhu cầu sản phẩm, pain point, objections từ Reddit/social/comments/transcripts | Ý tưởng/danh mục → chuyển thành query + từ đồng nghĩa | Verdict nhu cầu (Strong/Medium/Weak + confidence), bảng pain kèm exact language & source, alternatives, messaging angles |
| 10 | [`ad-library-teardown`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/ad-library-teardown/SKILL.md) | Phân tích quảng cáo đang chạy Meta/Google/LinkedIn: hook, offer, CTA, transcript video ad | Tên brand/domain/advertiser hoặc page ID | Teardown: messaging angles, hooks/headlines swipe file, offers & CTAs, "họ đang test gì", test đề xuất cho mình |
| 11 | [`audience-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/audience-research/SKILL.md) | Đánh giá độ phù hợp khán giả của creator/brand (địa lý, ngôn ngữ, niche) từ tín hiệu công khai | Creator + thị trường mục tiêu | Audience-fit report: fit score + confidence, bảng evidence/source, ghi chú địa lý/ngôn ngữ, khuyến nghị tài trợ |
| 12 | [`influencer-prospecting`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/influencer-prospecting/SKILL.md) | Lập danh sách creator/influencer theo niche để outreach/UGC/tài trợ | Niche, tiêu chí reach/fit | Bảng/CSV prospect chấm 1–5 theo 6 tiêu chí (niche fit, audience fit, reach, engagement quality, brand safety, contactability), outreach angles |
| 13 | [`content-repurposing`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/content-repurposing/SKILL.md) | Biến video/transcript/bài social thành asset tái dùng: LinkedIn post, X thread, kịch bản ngắn, newsletter | URL/transcript/báo cáo nghiên cứu có sẵn (chạy tốt nhất sau transcript/outlier/teardown) | Content pack: content atoms, bản thảo theo từng format, biến thể |

**Lưu ý phạm vi:** Với @hi.oneup (chỉ TikTok, comic-only), các skill trực tiếp cần là #1–#8. Skill #10 (ads) chỉ hữu ích nếu OneUp chạy/theo dõi quảng cáo app. Skill #11–#12 phục vụ hợp tác creator sau này. Skill #9 hữu ích gián tiếp: đào pain point về thói quen/phát triển bản thân từ Reddit/TikTok để làm kịch bản comic. Skill #13 hữu ích chuyển insight → kịch bản comic, nhưng output gốc thiên về LinkedIn/X/newsletter — cần tùy biến format đầu ra thành "kịch bản comic cho Omi".

---

## 3. Giấy phép (License)

### 3.1. File LICENSE thực tế là gì

Repo **có** file LICENSE. Toàn văn là **MIT License, Copyright (c) 2026 ScrapeCreators**. Nguồn: [LICENSE](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/LICENSE). Plugin manifest cũng khai báo `"license": "MIT"`. Nguồn: [`.claude-plugin/plugin.json`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/.claude-plugin/plugin.json). Hầu hết workflow `SKILL.md` cũng ghi `license: MIT` trong frontmatter (ví dụ `transcript-intelligence`, `comment-mining`).

### 3.2. Điều khoản chính (diễn giải từ toàn văn LICENSE)

- **Được cấp quyền miễn phí, không giới hạn** để: dùng, sao chép, sửa đổi, hợp nhất, xuất bản, **phân phối, cấp phép lại (sublicense), và bán** các bản sao của phần mềm.
- **Điều kiện duy nhất được ghi:** phải giữ lại thông báo bản quyền (*"The above copyright notice"*) và thông báo cấp phép này trong mọi bản sao hoặc phần đáng kể (*substantial portions*) của phần mềm.
- **Không bảo hành:** phần mềm được cung cấp "AS IS", không bảo đảm tính thương mại/phù hợp mục đích/không vi phạm; tác giả/chủ bản quyền không chịu trách nhiệm với khiếu nại, thiệt hại, hay trách nhiệm phát sinh.

### 3.3. Áp cho kênh thương mại @hi.oneup

| Câu hỏi | Đánh giá dựa trên LICENSE |
|---|---|
| Dùng các skill (file markdown workflow) để nghiên cứu nội dung cho kênh TikTok thương mại của OneUp được không? | **Được.** MIT cho phép use/copy/modify và cả sell copies; không có điều khoản cấm thương mại, không có điều khoản giới hạn lĩnh vực trong LICENSE của repo này. |
| Có bắt buộc ghi attribution khi đăng video TikTok không? | **LICENSE không yêu cầu ghi credit trên sản phẩm nội dung đầu ra.** Nghĩa vụ giữ thông báo bản quyền áp cho *bản sao/phần đáng kể của chính phần mềm* (tức nếu phân phối lại repo/skill file thì phải kèm notice + license). Đây là diễn giải văn bản license, không phải tư vấn pháp lý. |
| Nếu fork/sửa bộ skill rồi chia sẻ lại (nội bộ công ty hoặc công khai)? | Phải giữ nguyên dòng `Copyright (c) 2026 ScrapeCreators` và toàn văn MIT trong bản phân phối. |
| License của repo có bao phủ dữ liệu scrape được và điều khoản của TikTok/ScrapeCreators API không? | **Không.** MIT chỉ bao phủ "Software" của repo này (các file skill/tài liệu). Dữ liệu lấy qua API và việc sử dụng dịch vụ ScrapeCreators chịu điều khoản riêng của ScrapeCreators và của từng nền tảng (TikTok, Meta...). Repo không cấp bất kỳ quyền nào đối với dữ liệu của bên thứ ba, và tự tuyên bố chỉ làm việc với *public data*. Nguồn: [README — Design Principles](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md), [`AGENTS.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/AGENTS.md) |

> ⚠️ Đây là audit kỹ thuật/giấy phép ở mức đọc văn bản, **không phải tư vấn pháp lý**. Nếu OneUp phân phối lại bộ skill ra bên ngoài hoặc dùng dữ liệu scrape vào sản phẩm thương mại quy mô lớn, nên cho bộ phận pháp chế rà soát riêng điều khoản dịch vụ của ScrapeCreators và của TikTok.

---

## 4. Nguồn dữ liệu, API key và chi phí

### 4.1. Repo dựa vào nguồn nào

Toàn bộ dữ liệu thật đi qua **ScrapeCreators REST API**:

- Base URL: `https://api.scrapecreators.com`
- Mọi endpoint là GET, xác thực bằng header `x-api-key`, trả JSON.
- Trước khi gọi một endpoint, skill yêu cầu fetch OpenAPI spec của riêng endpoint đó tại `https://docs.scrapecreators.com/{path}/openapi.json` (spec toàn cục tại `https://docs.scrapecreators.com/openapi.json` — file lớn, repo khuyên ưu tiên spec từng endpoint).
- Repo ghi API có **110 endpoints**; frontmatter của skill ghi **27+ nền tảng** (TikTok, Instagram, YouTube, LinkedIn, Facebook, Twitter/X, Reddit, Threads, Bluesky, Pinterest, Snapchat, Twitch, Kick, Truth Social, TikTok Shop, Google, link-in-bio...).

Nguồn: [`skills/scrapecreators-api/SKILL.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md).

Tài liệu API chính thức xác nhận: mọi request đều cần API key trong header `x-api-key`, đăng ký tại `app.scrapecreators.com`, và *"Only public data extraction"*. Nguồn: [docs.scrapecreators.com](https://docs.scrapecreators.com).

**Không có nguồn dữ liệu thay thế trong repo.** Không có endpoint TikTok/Reddit trực tiếp, không có scraper tự chứa (self-hosted), không có chế độ chạy offline. Không có key = các skill chỉ còn là template workflow, không lấy được dữ liệu mới.

### 4.2. API key: bắt buộc

- README: `export SCRAPECREATORS_API_KEY=sk_...`, lấy key tại scrapecreators.com. Nguồn: [README — Setup](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md).
- Frontmatter của `scrapecreators-api` và các workflow skill đều khai báo `requires.env: [SCRAPECREATORS_API_KEY]`, `primaryEnv: SCRAPECREATORS_API_KEY`. Nguồn: ví dụ [`skills/scrapecreators-api/SKILL.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md), [`skills/comment-mining/SKILL.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/comment-mining/SKILL.md).
- `CLAUDE.md` của repo nhắc lại: khi cần dữ liệu social trực tiếp, dùng endpoint ScrapeCreators qua env var này. Nguồn: [CLAUDE.md](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/CLAUDE.md).

### 4.3. Chi phí / credits — tách rõ "repo ghi" và "website ghi"

**Repo ghi (đáng tin cậy trong phạm vi audit này):**

- Hầu hết endpoint tốn **1 credit/request**.
- Ngoại lệ đắt, phải cảnh báo người dùng trước khi gọi:
  - `/v1/tiktok/user/audience`: **26 credits** mỗi lần.
  - `/v1/tiktok/video/transcript`: **+10 credits** khi `use_ai_as_fallback=true`.
  - `/v1/google/company/ads`: **25 credits** khi `get_ad_details=true`.
- Kiểm tra số dư: `/v1/credit/balance`.
- Nguồn: [`skills/scrapecreators-api/SKILL.md` — Credit Costs](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md).

**Repo không ghi:** giá tiền theo gói, số credit miễn phí, hạn mức dùng thử. Bất kỳ con số tiền nào cũng **không được suy ra từ repo**.

**Website chính thức ghi (ngoài repo, kiểm tra ngày 19/10/2026, có thể thay đổi):** trang chủ scrapecreators.com ghi *"Start with 100 free credits"*, *"No credit card required"*, *"Cached results are free"*, *"Credits never expire"*, và liệt kê các gói pay-as-you-go. Nguồn: [scrapecreators.com](https://scrapecreators.com). Docs ghi response `402 Payment Required` khi hết credit. Nguồn: [docs.scrapecreators.com](https://docs.scrapecreators.com).

> **Quy tắc cho Social Research agent:** Chỉ trích dẫn mức giá/số credit miễn phí kèm link scrapecreators.com và ngày kiểm tra. Trước mỗi đợt chạy tốn nhiều request (phân trang comments, nhiều đối thủ, endpoint 26 credits), phải báo ước tính số request và xin duyệt — đúng tinh thần "Warn users before calling expensive endpoints" của repo.

### 4.4. Cách gọi & phân trang (để ước lượng công sức/chi phí)

- Handle truyền **không có `@`** (`charlidamelio`, không phải `@charlidamelio`); hashtag **không có `#`**. Nguồn: [`scrapecreators-api` — Known Limitations](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md).
- Phân trang khác nhau theo nền tảng: TikTok profile videos dùng `max_cursor`, TikTok comments/search dùng `cursor`, YouTube dùng `continuationToken`, Reddit dùng `after`, Instagram posts dùng `next_max_id`, reels dùng `max_id`, v.v. Mỗi trang thêm là thêm request/credit tiềm năng. Nguồn: [`scrapecreators-api` — Pagination](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md).
- Tham số `trim=true` giảm dung lượng response; `region` là mã quốc gia 2 ký tự **chỉ để định tuyến proxy, KHÔNG lọc kết quả theo quốc gia**. Nguồn: [`scrapecreators-api` — Common Optional Params](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md). Điểm này cực kỳ quan trọng khi nghiên cứu trend Việt Nam (xem §5.3).

---

## 5. Giới hạn nguồn dữ liệu theo nền tảng

### 5.1. Nguyên tắc chung repo tự công bố

- **Chỉ dữ liệu công khai.** Không hứa dữ liệu đăng nhập/riêng tư — lặp lại ở README, `AGENTS.md`, và pitfalls của nhiều skill. Nguồn: [README](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md), [AGENTS.md](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/AGENTS.md).
- **Transcript mọi nền tảng: chỉ video dưới 2 phút.** Instagram transcript là AI-powered, mất 10–30 giây, cũng dưới 2 phút; Facebook transcript dưới 2 phút. Nguồn: [`scrapecreators-api` — Transcripts & Known Limitations](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md), [`transcript-intelligence`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/transcript-intelligence/SKILL.md).
- **Không bịa:** skill outlier dặn *"Do not invent transcript quotes"*; transcript-intelligence dặn không hallucinate caption thiếu, quote phải truy được về URL; ad-library dặn không bịa spend/conversion/targeting. Nguồn: từng `SKILL.md` tương ứng ở §2.

### 5.2. Bảng theo nền tảng (chỉ những gì repo ghi)

| Nền tảng | Lấy được gì (endpoint tiêu biểu trong repo) | Giới hạn repo ghi rõ |
|---|---|---|
| **TikTok** | Profile (`/v1/tiktok/profile`), video của profile (`/v3/tiktok/profile/videos`), chi tiết video (`/v2/tiktok/video`), comments + replies, transcript (`/v1/tiktok/video/transcript`, hoặc qua `/v2/tiktok/video?get_transcript=true`), search users/keyword/hashtag/top, trending feed (bắt buộc `region`), popular hashtags/songs/videos/creators, song details/videos, followers/following, audience demographics, live, TikTok Shop | Transcript <2 phút; fallback AI cho transcript tốn +10 credits; audience tốn 26 credits; trending feed bắt buộc truyền region; handle không có `@` |
| **Instagram** | Profile, posts (`/v2/instagram/user/posts`), reels, highlights, chi tiết post, comments (`/v2/instagram/post/comments`), transcript (`/v2/instagram/media/transcript`), reels search, trending reels, hashtag search | Transcript AI 10–30s, <2 phút; play count chỉ tính view IG (không gồm cross-post Facebook); endpoint "song reels" đã deprecated/không hoạt động |
| **YouTube** | Channel, videos, Shorts (`/v1/youtube/channel/shorts`), playlist, chi tiết video, community post, comments + replies, transcript (cũng có sẵn trong response `/v1/youtube/video`), search, hashtag search, trending Shorts | Transcript theo giới hạn chung <2 phút cho endpoint transcript; phân trang bằng `continuationToken`. Lưu ý thực tế cho OneUp: Shorts đối thủ thường <2 phút nên giới hạn này ít cắn hơn so với video dài |
| **Reddit** | Chi tiết subreddit, bài trong subreddit, comments của post (`/v1/reddit/post/comments`), transcript video Reddit, search toàn cục, search trong subreddit, ads search | Tên subreddit **phân biệt hoa/thường** (`AskReddit` ≠ `askreddit`); comment-mining dặn phải đọc cả bài gốc lẫn comments, không tách rời ngữ cảnh |
| **Facebook** | Profile, posts, reels, photos, group posts, chi tiết post, comments + replies, transcript, ad library (search/company/detail/transcript) | Posts chỉ 3 bài/trang (giới hạn API); group posts cũng 3 bài/trang; transcript <2 phút |
| **X/Twitter** | Profile, tweets của user, chi tiết tweet, community + tweets, transcript | Chỉ trả ~100 tweet phổ biến nhất, **không phải mới nhất theo thời gian**; transcript AI-powered và chậm |
| **LinkedIn** | Profile cá nhân, company, company posts, chi tiết post, transcript, ads search/detail | Company posts tối đa 7 trang |
| **Threads** | Profile, posts của user, chi tiết post, search posts/users | Chỉ thấy công khai 20–30 bài gần nhất |
| **Bluesky / Pinterest / Truth Social / Snapchat / Twitch / Kick / Rumble** | Profile, posts, chi tiết post/pin/clip, search (Pinterest), comments + transcript (Rumble) theo bảng routing | Truth Social: chỉ user nổi bật (repo nêu ví dụ Trump, Vance) mới hoạt động công khai; còn lại theo giới hạn chung public-only |
| **Ad libraries (Meta/Google/LinkedIn/Reddit)** | Search ads, ads theo công ty, chi tiết ad, transcript video ad Meta | Không có dữ liệu hiệu quả thật (spend/conversion) trong dữ liệu công khai — skill cấm suy diễn ad "thắng" chỉ vì đang chạy; ad đang chạy/lặp lại chỉ là tín hiệu, không phải bằng chứng performance. Nguồn: [`ad-library-teardown`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/ad-library-teardown/SKILL.md) |
| **Google / link-in-bio / TikTok Shop / khác** | Google search, Linktree/Komi/Pillar/Linkbio/Linkme, Amazon Shop, TikTok Shop (search/products/reviews/showcase), detect age/gender, credit balance | Google company ads +25 credits khi lấy chi tiết; còn lại 1 credit/request theo quy tắc chung (trừ ngoại lệ đã liệt kê) |

Nguồn toàn bảng: [`skills/scrapecreators-api/SKILL.md`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md) (bảng routing Profiles / Posts / Single Post / Comments / Transcripts / Search / Ad Libraries / Trending / Followers / TikTok Shop / Link-in-Bio + mục Known Limitations), đối chiếu chéo với bảng *Data Sources/Comment Sources/Transcript Sources* trong từng workflow skill.

### 5.3. Giới hạn ảnh hưởng trực tiếp tới @hi.oneup (Việt Nam, TikTok, comic)

1. **Trend Việt Nam không được bảo đảm bởi tham số `region`.** Repo ghi rõ `region` chỉ định tuyến proxy, *"does NOT filter by region"*. TikTok trending feed yêu cầu `region` (ví dụ `US` trong tài liệu) nhưng repo không cam kết feed trả về là trend của đúng quốc gia đó theo nghĩa biên tập. Hệ quả: mọi trend brief cho khán giả Việt phải tự kiểm chứng chéo bằng search keyword/hashtag tiếng Việt + comments tiếng Việt, và ghi rõ caveat này. Nguồn: [`scrapecreators-api` — Common Optional Params & Trending](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md); [`trend-discovery` — Common Pitfalls](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/trend-discovery/SKILL.md) (*"Do not ignore region. TikTok trends can be highly country-specific."*).
2. **Ngôn ngữ transcript tiếng Việt không được repo cam kết.** Ví dụ transcript TikTok trong repo dùng `lang=en`; repo không liệt kê danh sách ngôn ngữ hỗ trợ. Với video nói tiếng Việt phải kiểm chứng thực tế khi có key — audit này không khẳng định được.
3. **Comic-only gần như không có lời thoại** → transcript có thể rỗng/không áp dụng. Nguồn hook cho OneUp phải mở rộng sang: caption, chữ trên từng panel/trang truyện, bình luận trích nguyên văn, và hook của *video nói* từ đối thủ/kênh giáo dục — có gắn nhãn nguồn rõ ràng, không gán nhầm quote. Xem §6(d).
4. **Âm thanh trending:** repo có endpoint popular songs, chi tiết bài hát, và video dùng cùng bài hát (`/v1/tiktok/song`, `/v1/tiktok/song/videos`). Đây là đường chính đáng để comic (vốn không lời) bắt trend âm thanh — nhưng vẫn phải qua bộ lọc §7. Nguồn: [`scrapecreators-api` — Trending/Popular](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md).

---

## 6. Đánh giá áp dụng cho @hi.oneup: map 4 việc chính

Thang đánh giá: **Khả thi tốt / Khả thi có điều kiện / Yếu — cần bổ sung ngoài repo**. Mọi đánh giá đều giả định *đã có API key hợp lệ*; chưa có key thì cả 4 việc đều chưa chạy được dữ liệu thật.

### (a) Tìm bài đăng nổi bật / trend

| Khía cạnh | Đánh giá |
|---|---|
| Skill map | Chính: [`trend-discovery`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/trend-discovery/SKILL.md) + [`outlier-post-finder`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/outlier-post-finder/SKILL.md). Hỗ trợ: [`social-listening-brief`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/social-listening-brief/SKILL.md) để nghe chủ đề rộng |
| Cách chạy gợi ý cho OneUp | `trend-discovery`: định nghĩa niche (thói quen, kỷ luật, học tập, sức khỏe tinh thần tích cực), kéo 2–4 nguồn (TikTok trending/search hashtag/keyword, popular songs/hashtags, YouTube Shorts trending khi liên quan). `outlier-post-finder`: với từng kênh mẫu/kênh của mình, kéo ≥20 bài, tính median baseline theo từng nền tảng/format, chấm lift 1.5x/2x/5x |
| Khả thi | **Khả thi tốt** cho TikTok — đây là use case trung tâm của repo (README nêu đầu tiên). Nguồn: [README](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md) |
| Thiếu gì / lưu ý | (1) Một bài viral đơn lẻ **không** được gọi là trend — chính skill trend-discovery cấm điều này. (2) Region Việt Nam không được lọc thật bởi API (xem §5.3). (3) Trend âm thanh/hashtag phải qua bộ lọc §7 trước khi đề xuất cho Omi. (4) Phải xuất **evidence table có URL + ngày + metric thô**; cấm chỉ ghi "đang trending" |

### (b) Phân tích đối thủ

| Khía cạnh | Đánh giá |
|---|---|
| Skill map | Chính: [`competitor-social-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/competitor-social-research/SKILL.md). Hỗ trợ: [`creator-profile-teardown`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/creator-profile-teardown/SKILL.md) (mổ 1 kênh sâu), [`outlier-post-finder`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/outlier-post-finder/SKILL.md) (outlier từng đối thủ), [`audience-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/audience-research/SKILL.md) (fit khán giả — cẩn thận endpoint 26 credits) |
| Cách chạy gợi ý cho OneUp | Lập danh sách handle đối thủ trực tiếp (app thói quen/phát triển bản thân) + đối thủ gián tiếp (comic kể chuyện, kênh học tập/năng suất) trên TikTok trước; mỗi đối thủ: profile snapshot → cửa sổ bài gần nhất ngang nhau → baseline riêng → pillars/formats/hook styles/cadence/CTA → gaps |
| Khả thi | **Khả thi tốt** nếu handle rõ ràng và kênh công khai. Skill có sẵn khung so sánh công bằng: cấm so raw views giữa kênh lớn/nhỏ, bắt buộc lift theo baseline của chính kênh đó, và yêu cầu nói "appears to/suggests" thay vì khẳng định chiến lược là sự thật |
| Thiếu gì / lưu ý | (1) Nếu chỉ biết tên thương hiệu mà không có handle, phải search & xác nhận profile — repo cảnh báo trùng tên. (2) Chuỗi endpoint trong một số bảng của skill competitor dùng dạng cũ (ví dụ `/v1/youtube/channel-videos`, `/v1/twitter/user-tweets`) trong khi `scrapecreators-api` dùng dạng gạch chéo khác (`/v1/youtube/channel/videos`, `/v1/twitter/user/tweets`) — khi chạy thật phải **fetch OpenAPI spec từng endpoint để xác nhận path/params**, đúng chỉ dẫn của chính repo, không gọi theo trí nhớ. (3) Không suy ra doanh thu/tải app từ dữ liệu công khai |

### (c) Khai thác bình luận (comment mining)

| Khía cạnh | Đánh giá |
|---|---|
| Skill map | Chính: [`comment-mining`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/comment-mining/SKILL.md). Hỗ trợ: [`product-demand-research`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/product-demand-research/SKILL.md) (biến pain point thành nhu cầu tính năng OneUp), [`social-listening-brief`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/social-listening-brief/SKILL.md) |
| Endpoint | TikTok comments + replies theo URL video; tương tự YouTube, Instagram, Facebook, Reddit, Rumble. Nguồn: bảng Comment Sources trong `comment-mining` |
| Cách chạy gợi ý cho OneUp | Ưu tiên comments dưới: video outlier của đối thủ, video về thói quen/kỷ luật, và chính video @hi.oneup. Phân loại theo 9 bucket của skill (questions, objections, complaints/pain, praise, confusion, requests, buying intent, controversy/debate, jokes/memes). Mỗi theme phải có **trích nguyên văn + URL + số lượng mẫu**, tách "một bình luận to tiếng" khỏi pattern lặp lại |
| Khả thi | **Khả thi tốt** — đây là nguồn ý tưởng comic trực tiếp nhất cho Omi: nỗi đau thật, câu hỏi thật, ngôn ngữ thật của khán giả về trì hoãn, dậy sớm, học hành, điện thoại... |
| Thiếu gì / lưu ý | (1) Không suy ra "tâm lý thị trường" từ comments của một bài — skill tự cấm. (2) Lọc bot/spam, không lấy thông tin cá nhân dù công khai nếu không cần thiết. (3) Comments chứa bi kịch/chế giễu/chính trị phải bị loại ở tầng lọc §7, không được biến thành chất liệu comic chế nhạo lại nhân vật thật. (4) Phân trang sâu = tốn credit tỉ lệ với số trang |

### (d) Tìm hook từ lời thoại / transcript video

| Khía cạnh | Đánh giá |
|---|---|
| Skill map | Chính: [`transcript-intelligence`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/transcript-intelligence/SKILL.md). Hỗ trợ: [`outlier-post-finder`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/outlier-post-finder/SKILL.md) (chỉ fetch transcript của bài thắng), [`content-repurposing`](https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/content-repurposing/SKILL.md) (biến hook thành kịch bản) |
| Cách chạy gợi ý cho OneUp | Thu thập URL TikTok/Shorts/Reels **có lời nói** của đối thủ/kênh chuyên gia trong niche thói quen; bóc hook mở đầu (3 giây đầu theo cấu trúc hook → setup → claim → evidence → payoff → CTA của skill), lập Hooks Swipe File trích nguyên văn kèm URL |
| Khả thi | **Khả thi có điều kiện — đây là điểm yếu tương đối cho comic-only.** Ba lý do repo tự ghi: transcript chỉ cho video <2 phút; transcript AI (Instagram/X) có thể chậm và chữ có thể sai, phải gắn nhãn "approximate"; cấm bịa quote khi không fetch được transcript |
| Thiếu gì / bổ sung bắt buộc | (1) Video comic/slideshow không lời → transcript rỗng là bình thường, không phải lỗi; hook phải lấy từ **caption + chữ panel đầu tiên** (repo outlier cho phép quote caption/text hiển thị khi không có transcript — và phải nói rõ đó là caption, không phải lời thoại). (2) Chất lượng transcript tiếng Việt chưa được repo cam kết — cần test nhỏ khi có key trước khi tin quote. (3) Hook học từ đối thủ phải *adapt cấu trúc*, không sao chép nguyên văn thành nội dung của mình (pitfall của `content-repurposing`: *"Do not plagiarize. Adapt structure and insight"*). (4) Mọi hook đưa vào kịch bản Omi vẫn qua bộ lọc §7 |

### Bảng tổng hợp map 4 việc

| Việc | Skill chính | Skill hỗ trợ | Mức khả thi cho @hi.oneup | Điều kiện tiên quyết |
|---|---|---|---|---|
| (a) Bài nổi bật / trend | `trend-discovery`, `outlier-post-finder` | `social-listening-brief` | **Tốt** | API key; kiểm chứng region VN thủ công; evidence có URL |
| (b) Phân tích đối thủ | `competitor-social-research` | `creator-profile-teardown`, `outlier-post-finder` | **Tốt** | Danh sách handle xác nhận được; cửa sổ so sánh ngang nhau |
| (c) Comment mining | `comment-mining` | `product-demand-research` | **Tốt** | URL video cụ thể; ngân sách phân trang; bộ lọc §7 |
| (d) Hook từ transcript | `transcript-intelligence` | `outlier-post-finder`, `content-repurposing` | **Có điều kiện** | Chỉ video nói <2 phút; comic-only phải bổ sung caption/on-screen text; kiểm chứng tiếng Việt |

---

## 7. Rule lọc kênh bắt buộc cho @hi.oneup (áp lên mọi đầu ra của skill)

Repo **không có sẵn** bộ lọc nội dung cho thương hiệu OneUp/Omi. Các skill chỉ có guardrail chung (public data, không bịa, brand-safety là một tiêu chí chấm điểm trong `influencer-prospecting`). Do đó lớp lọc dưới đây là **bổ sung bắt buộc của Social Research agent**, gắn vào cuối mọi workflow trước khi đề xuất bất cứ nội dung nào:

### 7.1. Danh sách loại bỏ cứng (hard reject) — gặp là loại, không tranh luận

1. **Chính trị:** đảng phái, bầu cử, chính sách gây tranh cãi, nhân vật chính trị, biểu tình, chiến tranh, xung đột địa chính trị — kể cả khi đang trending mạnh.
2. **Bi kịch:** tai nạn, thiên tai, mất mát, bệnh tật nặng, qua đời, khủng hoảng cá nhân của người thật — không biến thành chất liệu comic dưới bất kỳ hình thức "truyền cảm hứng" nào.
3. **Chế giễu:** mỉa mai, body-shaming, chế nhạo ngoại hình/trình độ/thu nhập/giới tính/vùng miền, "cringe", drama bóc phốt, tranh cãi để câu view. Omi được phép hài tự trào theo hướng đồng cảm, không hạ thấp người khác.
4. **Nội dung nhạy cảm khác:** bạo lực, 18+, cờ bạc, chất kích thích, lừa đảo, cam kết y tế/tài chính gây hiểu lầm (chữa bệnh, giảm cân thần tốc, làm giàu nhanh).

### 7.2. Quy tắc bằng chứng

1. **Mọi trend/bài mẫu/quote phải có URL nguồn** truy cập được. Không có link = không đưa vào mục đề xuất.
2. **Không bịa số liệu:** view/like/comment/ follower phải là số thô từ response API kèm URL và ngày lấy. Không suy ra tỉ lệ tăng trưởng, doanh thu, lượt tải app.
3. **Trích nguyên văn có nhãn:** quote ghi rõ là transcript / caption / chữ trên hình / bình luận + URL.
4. **Độ tin cậy mẫu:** dưới 10 bài = Low (theo rule của `outlier-post-finder`); trend chỉ từ 1 bài không được gọi là trend (theo rule của `trend-discovery`).
5. **Thiếu dữ liệu ghi rõ** "không có dữ liệu công khai / chưa kiểm chứng", không lấp bằng suy đoán.

### 7.3. Checklist áp trước khi đề xuất cho Omi

- [ ] Không thuộc hard-reject 7.1?
- [ ] Có URL nguồn + ngày + nền tảng cho mọi claim?
- [ ] Phù hợp comic-only (không phụ thuộc lời thoại/gương mặt người thật)?
- [ ] Hook có thể diễn bằng panel đầu + chữ trên hình trong 1-3 giây đầu?
- [ ] Nhân vật hư cấu Omi, không dùng hình ảnh/quote người thật kiểu chế giễu?
- [ ] Có ghi caveat mẫu nhỏ / dữ liệu cũ / region?

---

## 8. Rủi ro và giới hạn chính

| # | Rủi ro/giới hạn | Mức độ | Cách giảm thiểu |
|---|---|---|---|
| 1 | Không có API key thì không lấy được dữ liệu thật; key thuộc dịch vụ trả phí theo credit | Cao | Xin duyệt key + ngân sách credit riêng, kiểm tra `/v1/credit/balance`, cảnh báo trước endpoint đắt |
| 2 | Tốn credit khi phân trang / quét nhiều kênh; audience 26 credits, transcript AI fallback +10, Google ads chi tiết 25 | Trung bình-Cao | Giới hạn số bài/trang mỗi lần chạy, dùng `trim=true`, báo ước tính request trước khi chạy |
| 3 | Chỉ dữ liệu công khai; không thấy bài riêng tư, bị xóa, giới hạn tuổi/khu vực | Trung bình | Ghi caveat, kiểm chứng chéo nhiều nguồn, không kết luận quá mức |
| 4 | Transcript chỉ <2 phút; comic không lời thì rỗng; tiếng Việt chưa được repo cam kết | Cao với comic-only | Kết hợp caption/on-screen text/comments; test nhỏ transcript tiếng Việt khi có key |
| 5 | Trend theo quốc gia: `region` chỉ là proxy routing, không lọc quốc gia | Cao cho VN | Search keyword/hashtag tiếng Việt, đọc comments tiếng Việt, ghi rõ giới hạn |
| 6 | Repo là file markdown workflow, không tự bảo đảm chất lượng phân tích của agent; agent vẫn có thể bịa nếu không tuân thủ | Trung bình | Bắt buộc checklist 7.2-7.3, yêu cầu bảng evidence trước khuyến nghị |
| 7 | Khác biệt path endpoint giữa các bảng trong repo (ví dụ dạng `channel-videos` vs `channel/videos`) | Thấp-Trung bình | Luôn fetch OpenAPI spec từng endpoint trước khi gọi, theo đúng chỉ dẫn repo |
| 8 | Điều khoản nền tảng và dịch vụ ScrapeCreators nằm ngoài MIT license của repo | Trung bình | Không coi MIT là quyền dùng dữ liệu; rà soát ToS riêng nếu dùng thương mại quy mô lớn (không phải tư vấn pháp lý) |
| 9 | Sentiment/comment của 1 bài không đại diện thị trường | Trung bình | Ghi sample size + confidence, tách 1 comment nổi bật khỏi pattern lặp lại |
| 10 | Giá/gói credit trên website có thể thay đổi sau ngày audit 19/10/2026 | Thấp | Chỉ trích giá kèm link scrapecreators.com và ngày kiểm tra; kiểm tra lại khi mua |

Nguồn cho các giới hạn kỹ thuật trong bảng: `scrapecreators-api` mục Credit Costs, Known Limitations, Common Optional Params và pitfalls của từng workflow skill đã dẫn ở §4-§6.

---

## 9. Quy trình pilot đề xuất cho @hi.oneup

### Giai đoạn 0 - Chưa có key (làm ngay, chi phí 0)

1. Chuẩn bị template prompt cho 4 việc ở §6, đã nhúng sẵn checklist §7.
2. Lập danh sách ứng viên đối thủ/kênh mẫu TikTok trong niche thói quen/phát triển bản thân và comic kể chuyện (chỉ tên + handle dự kiến, đánh dấu "chưa xác nhận profile").
3. Thống nhất định dạng evidence table: URL | nền tảng | ngày bài | ngày lấy dữ liệu | metric thô | ghi chú lọc §7.

### Giai đoạn 1 - Có key, pilot nhỏ có ngân sách duyệt trước

1. Kiểm tra `/v1/credit/balance` trước và sau mỗi phiên.
2. Kiểm chứng 1 profile TikTok + 20 video gần nhất (`outlier-post-finder`), tính median + lift.
3. Lấy comments của 2-3 video outlier (`comment-mining`), phân loại 9 bucket, trích nguyên văn có URL.
4. Test transcript tiếng Việt trên 3-5 video nói ngắn dưới 2 phút (`transcript-intelligence`); đánh giá độ đúng chữ trước khi dùng làm hook.
5. Test 1 truy vấn trend (`trend-discovery`) với keyword/hashtag tiếng Việt + popular songs; đối chiếu trend feed để kiểm tra mức liên quan Việt Nam.
6. Không gọi `/v1/tiktok/user/audience` (26 credits) khi chưa có lý do và duyệt riêng.

### Giai đoạn 2 - Vận hành

- Mỗi brief bắt đầu bằng mục Evidence (link + số thô) rồi mới tới Pattern, sau đó mới tới Ý tưởng cho Omi đã qua lọc §7.
- Lưu lại số credit tiêu thụ mỗi phiên cạnh output để kiểm soát ngân sách.
- Định kỳ kiểm tra lại docs/OpenAPI spec vì endpoint và credit có thể thay đổi; nguồn: https://docs.scrapecreators.com

### Những việc không làm

- Không chạy scrape thật khi chưa có key và duyệt ngân sách.
- Không hứa dữ liệu riêng tư/đăng nhập.
- Không sao chép nguyên văn hook/caption của đối thủ thành nội dung OneUp; chỉ học cấu trúc và ghi nguồn nội bộ.
- Không biến bi kịch, chính trị, hay bình luận chế giễu thành chất liệu comic.

---

## 10. Kết luận

Repo `social-media-research-skills` ở commit `64ba7b4` là bộ 13 file workflow markdown theo MIT License, dùng ScrapeCreators API làm tầng dữ liệu duy nhất. Nó phù hợp làm nền cho Social Research agent của @hi.oneup cho ba việc: tìm outlier/trend, phân tích đối thủ, và khai thác bình luận. Việc tìm hook từ transcript hữu ích cho video nói của đối thủ nhưng không phải nguồn chính cho comic-only; phải bổ sung caption, chữ panel đầu, âm thanh trending và bình luận.

Điều kiện để dùng thật: có `SCRAPECREATORS_API_KEY` và ngân sách credit được duyệt, tuân thủ cảnh báo endpoint đắt, kiểm chứng riêng cho tiếng Việt/khu vực Việt Nam, và áp bắt buộc bộ lọc loại bỏ chính trị - bi kịch - chế giễu cùng quy tắc mọi trend phải có link nguồn, không bịa số liệu.

**Đường dẫn báo cáo này:** `/workspace/social-research-repo-audit-vi.md`

---

## 11. Nguồn đã dùng trong audit

### Trong repo (commit 64ba7b4dea71e130d2712ffb6c1c1024b3b7c4b2)

- README: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md
- LICENSE (MIT): https://github.com/ScrapeCreators/social-media-research-skills/blob/main/LICENSE
- Plugin manifest: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/.claude-plugin/plugin.json
- AGENTS.md: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/AGENTS.md
- CLAUDE.md: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/CLAUDE.md
- Thư mục skills: https://github.com/ScrapeCreators/social-media-research-skills/tree/main/skills
- scrapecreators-api: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/scrapecreators-api/SKILL.md
- outlier-post-finder: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/outlier-post-finder/SKILL.md
- trend-discovery: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/trend-discovery/SKILL.md
- competitor-social-research: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/competitor-social-research/SKILL.md
- creator-profile-teardown: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/creator-profile-teardown/SKILL.md
- comment-mining: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/comment-mining/SKILL.md
- transcript-intelligence: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/transcript-intelligence/SKILL.md
- social-listening-brief: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/social-listening-brief/SKILL.md
- product-demand-research: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/product-demand-research/SKILL.md
- audience-research: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/audience-research/SKILL.md
- influencer-prospecting: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/influencer-prospecting/SKILL.md
- ad-library-teardown: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/ad-library-teardown/SKILL.md
- content-repurposing: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/skills/content-repurposing/SKILL.md

### Ngoài repo (chỉ cho thông tin API key/giá hiện hành, kiểm tra 19/10/2026)

- ScrapeCreators website (gói, credit miễn phí, pay-as-you-go): https://scrapecreators.com
- Tài liệu API chính thức (xác thực, mã lỗi 402, public data): https://docs.scrapecreators.com
- OpenAPI toàn cục (repo khuyên ưu tiên spec từng endpoint): https://docs.scrapecreators.com/openapi.json

*Hết báo cáo.*
