---
title: "Nghiên cứu: social-media-agent (draft-only)"
date: 2026-10-19
source: "agent research 19/10/2026 (goc o /workspace, da gom vao repo)"
id: research.social-poster
type: research
status: reference
updated: 2026-10-19
tags: [social, draft, x, linkedin]
---
# Social Poster — Nghiên cứu repo langchain-ai/social-media-agent (draft-only cho OneUp)
Ngày: 19/10/2026 (Asia/Saigon) | Trạng thái: CHỈ NGHIÊN CỨU — không đăng nhập, không đăng bài, không dùng credential

## 1. Repo & License
- Repo: https://github.com/langchain-ai/social-media-agent — public, TypeScript, default branch `main`, tạo 21/11/2024. Mô tả chính thức (README): "take in a URL, and generate a Twitter & LinkedIn post based on the content of the URL" + human-in-the-loop.
- LICENSE: **MIT License, Copyright (c) 2024 LangChain** — file `LICENSE` tại repo root (GitHub API cũng xác nhận spdx_id: MIT).
  - Hệ quả thương mại cho OneUp: MIT cho phép dùng, sửa, merge, publish, distribute, sublicense, sell — kể cả thương mại — miễn giữ nguyên copyright notice + license trong mọi copy/substantial portion. Không warranty (AS IS). => Được fork/tùy biến cho OneUp thương mại; rủi ro pháp lý thấp, vẫn phải giữ notice. Đây không phải tư vấn pháp lý.
- Cấu trúc chính (git tree, 339 paths):
  - `src/agents/generate-post/generate-post-graph.ts` — graph chính
  - `src/agents/shared/nodes/generate-post/human-node.ts`, `schedule-post.ts`, `rewrite-post.ts`
  - `src/agents/upload-post/index.ts` — node ĐĂNG THẬT lên X + LinkedIn (xem mục 3)
  - `src/agents/verify-links/verify-links-graph.ts`, `src/agents/shared/nodes/verify-general.ts`
  - `src/clients/twitter/`, `src/clients/linkedin.ts`, `src/clients/auth-server.ts`
  - `scripts/generate-post.ts`, `scripts/crons/`, `langgraph.json`, `.env.quickstart.example`, `.env.full.example`
  - `src/agents/generate-post/prompts/index.ts` + `examples.ts` — nơi tùy biến giọng/bối cảnh

## 2. Repo làm gì — có bằng chứng file
- **Lấy nội dung từ link:** `verify-links-graph.ts` phân loại URL (twitter/youtube/github/reddit/luma/general). Link thường -> `verify-general.ts`: FireCrawlLoader mode `scrape`, formats ["markdown","screenshot"], fallback `getPageText(url)`; sau đó LLM kiểm tra relevancy theo BUSINESS_CONTEXT (có cờ `SKIP_CONTENT_RELEVANCY_CHECK` để bỏ). Chặn trùng link đã dùng (`checkIfUrlsArePreviouslyUsed` + store post-subject-urls, cờ `SKIP_USED_URLS_CHECK`).
- **Tạo bài:** verify -> `generateContentReport` (marketing report) -> `generatePost` -> nếu >280 ký tự (sau bỏ URL) thì `condensePost` tối đa lặp -> tìm/tạo ảnh (trừ text-only) -> **humanNode**.
- **Human-in-the-loop (có thật):** `human-node.ts` dùng LangGraph `interrupt()` với HumanInterrupt: allow_accept/edit/ignore/respond=true. Edit/Accept -> `schedulePost`; Response -> router LLM: rewritePost / updateScheduleDate / rewriteWithSplitUrl / unknown quay lại humanNode; Ignore -> END (không đăng). Ngày mặc định: Saturday kế tiếp; định dạng `MM/dd/yyyy hh:mm a z` hoặc P1/P2/P3.
- **Lên lịch/đăng:** `schedule-post.ts` KHÔNG đăng trực tiếp — nó tạo 1 run mới của graph `upload_post` trên LangGraph server với `afterSeconds` (LangGraph delayed run = cơ chế "lên lịch"). `upload-post/index.ts` mới là nơi gọi TwitterClient/LinkedInClient (qua Arcade hoặc API tự host), uploadTweet/uploadThread, createTextPost/createImagePost. ⚠️ Mặc định còn tự retweet/reshare từ "main account" nếu có token MAIN_*.
- **Tùy biến giọng:** README mục Customization chỉ rõ phải sửa `BUSINESS_CONTEXT`, `TWEET_EXAMPLES`, `POST_STRUCTURE_INSTRUCTIONS`, `POST_CONTENT_RULES` trong `src/agents/generate-post/prompts/` — bản gốc đang để giọng LangChain/AI Twitter.

### Yêu cầu môi trường / API keys
- Quickstart (`.env.quickstart.example` + README): `ANTHROPIC_API_KEY` (LLM), `LANGCHAIN_API_KEY`+tracing (LangSmith — README nói cần để chạy LangGraph server local), `FIRECRAWL_API_KEY` (scrape, free 500 credits theo README), `ARCADE_API_KEY` + `USE_ARCADE_AUTH=true`, `TWITTER_USER_ID`, `LINKEDIN_USER_ID`. Chạy: `yarn install`, `pip install langgraph-cli`, `yarn langgraph:in_mem:up` (port 54367), `yarn generate_post`. Xem duyệt qua Agent Inbox (dev.agentinbox.ai hoặc local).
- Full (`.env.full.example`): thêm Twitter dev keys (API_KEY/SECRET, BEARER, CLIENT_ID/SECRET, USER_TOKEN/SECRET, MAIN_*), LinkedIn (CLIENT_ID/SECRET, ACCESS_TOKEN, PERSON_URN, ORGANIZATION_ID, MAIN_*), `GOOGLE_VERTEX_AI_WEB_CREDENTIALS` (YouTube), `SUPABASE_URL/SERVICE_ROLE_KEY` (lưu ảnh, bucket `images` public), `GITHUB_TOKEN`, Slack tokens, `SESSION_SECRET`.
- KHÔNG dùng Typefully trong repo này. Đường đăng: Arcade HOẶC tự host X/LinkedIn dev app — không dùng cả hai cùng lúc (README).

## 3. X & LinkedIn nếu tích hợp thật — phần draft vs phần cần tài khoản
### Chỉ làm bản nháp — KHÔNG cần đăng nhập X/LinkedIn:
- Chạy tới humanNode là đủ: cần Anthropic + FireCrawl (+LangSmith key cho LangGraph server). Không cần Arcade, không cần X/LinkedIn token, không cần OAuth.
- Điều kiện bắt buộc để an toàn: ngắt graph TRƯỚC `schedulePost`/`upload_post` (xem mục 4). Nếu để nguyên, Accept/Edit trong Inbox sẽ kích hoạt đăng thật.

### Cần kết nối tài khoản mới đăng được:
- **Qua Arcade (nhanh nhất theo repo):** OAuth per-user cho X/LinkedIn, provider giữ token. Arcade pricing (arcade.dev/pricing, kiểm 19/10/2026): Free $0 — 2,000 auth events + 2,000 tool calls/tháng; Team $25/tháng + $0.10/auth event + $0.01/tool call. Lưu ý: Arcade lo OAuth cá nhân (w_member_social cho LinkedIn); đăng Company Page vẫn cần quyền org riêng.
- **Tự host X:** Twitter Developer app, permissions Read and write, Web App, callback `http://localhost:3000/auth/twitter/callback`, OAuth qua `yarn start:auth` -> TWITTER_USER_TOKEN/SECRET. **Chi phí X API 2026 (docs.x.com pricing, pay-per-use, mua credits, không subscription): Post Create $0.015/request, Post Create có URL $0.20/request** (rất đáng注意 vì bài OneUp thường kèm link), đọc $0.005/resource. Giá thay đổi — kiểm lại Developer Console trước khi quyết.
- **Tự host LinkedIn:** LinkedIn Developer app + Products "Share on LinkedIn" + "Sign In with LinkedIn using OpenID Connect" -> scope `w_member_social` (đăng cá nhân, self-serve theo Microsoft Learn). Đăng **Company Page**: cần `w_organization_social` qua Community Management API (phê duyệt đối tác, role ADMINISTRATOR/DIRECT_SPONSORED_CONTENT_POSTER/CONTENT_ADMIN, verify company page + app) — nặng hơn nhiều, không tự động có. Repo hỗ trợ qua `POST_TO_LINKEDIN_ORGANIZATION=true` + `LINKEDIN_ORGANIZATION_ID` + sửa scope trong `src/clients/auth-server.ts`.
- Repo cũng cần Twitter dev account riêng nếu muốn upload media lên X, kể cả khi dùng Arcade.

### Phương án thay thế không fork repo (để Hiệp cân nhắc):
- **Typefully API v2** (typefully.com/docs/api): `POST /v2/social-sets/{id}/drafts` tạo draft cho X+LinkedIn, phân biệt rõ quyền WRITE (tạo draft) vs PUBLISH (lên lịch/đăng); `plan_at` = lên lịch "inert" không tự đăng. Free 10 posts/tháng. Đây là đường draft-native, ít phải tự host OAuth hơn, nhưng là SaaS trả phí theo scale và phải kết nối tài khoản vào Typefully.

## 4. Workspace /workspace trên box (chỉ đọc, không sửa)
- **Chưa có** clone của `social-media-agent` (find theo tên thư mục: không thấy), chưa có setup/.env liên quan, chưa có file social-poster-research.md trước bản này.
- Có sẵn liên quan gián tiếp: `/workspace/oneup-studio/` (AGENTS.md, brand/, content/, pipeline/...) — nên lấy giọng OneUp từ đây khi tùy biến prompt; `/workspace/social-media-research-skills/` (skills nghiên cứu, không phải poster); `/workspace/omi-tiktok-trend-ideas-2026-10-16.md`.

## 5. Đề xuất quy trình DRAFT-ONLY an toàn cho OneUp
Nguyên tắc cứng: agent chỉ tạo bản nháp; Hiệp duyệt/chỉnh mới được lên lịch thủ công. Tuyệt đối không tự đăng.

1. **Input:** Hiệp gửi 1 link (+ ghi chú góc nhìn nếu muốn).
2. **Trích xuất + tóm tắt nguồn:** FireCrawl scrape (hoặc fallback đọc web) -> bản tóm tắt nguồn ngắn: ý chính, số liệu/trích dẫn kiểm chứng được, link gốc. Giữ link gốc để Hiệp kiểm tra — không bịa số liệu ngoài nguồn.
3. **Sinh 2 bản nháp riêng** (repo gốc sinh 1 post chung cho cả hai — cần sửa):
   - X: ngắn ≤280 ký tự, hook mạnh, 1 ý duy nhất, giọng productivity/motivation, CTA mềm về OneUp/Omi, link để ở cuối hoặc reply (lưu ý chi phí $0.20/bài có URL nếu sau này đăng qua X API — cân nhắc để link ở reply).
   - LinkedIn: dài hơn (3-6 đoạn ngắn), mở bằng insight/câu chuyện, kết bằng câu hỏi thảo luận + nhắc OneUp/Omi tự nhiên, hashtag hạn chế.
   - Tùy biến trong repo: `BUSINESS_CONTEXT` = OneUp (app productivity/motivation + Omi, TikTok @hi.oneup), thay `TWEET_EXAMPLES` bằng mẫu bài OneUp/Hiệp duyệt, `POST_CONTENT_RULES` cấm hứa hẹn y tế/tài chính, cấm bịa tính năng.
4. **Cổng duyệt (bắt buộc):** qua Agent Inbox hoặc file nháp — Hiệp chọn Accept/Edit/Ignore/nhờ viết lại. 
   - 🔒 **Khóa an toàn khi triển khai:** (a) fork và XÓA/vô hiệu node `uploadPost` + route `schedulePost`->`upload_post`, hoặc chạy graph dừng ở humanNode; (b) không điền ARCADE_API_KEY/TWITTER_*/LINKEDIN_* token trong giai đoạn draft; (c) tắt MAIN_* retweet/reshare; (d) nếu sau này bật đăng: yêu cầu xác nhận rõ ràng từng bài + đặt spending limit X API.
5. **Lên lịch thủ công:** Hiệp tự dán vào X/LinkedIn/Typefully ở giai đoạn đầu. Chỉ khi quy trình ổn mới cân nhắc bật scheduled run — và vẫn qua Accept từng bài.

### Rủi ro
- Repo mặc định THIẾT KẾ ĐỂ ĐĂNG: chỉ 1 click Accept trong Inbox là lên lịch đăng thật (kèm retweet/reshare từ main account nếu có token) — rủi ro lớn nhất, phải ngắt trước khi dùng thật.
- Chi phí ẩn: X API $0.20/bài có URL; FireCrawl/Anthropic theo usage; Arcade Team $25+/tháng nếu vượt free.
- LinkedIn Company Page cần phê duyệt Community Management — có thể mất nhiều tuần hoặc bị từ chối; đăng cá nhân thì dễ (w_member_social).
- Nội dung AI sinh có thể sai lệch nguồn/hứa quá đà — bắt buộc Hiệp đọc lại nguồn gốc trước khi đăng; ảnh từ FireCrawl/Supabase có vấn đề bản quyền cần kiểm.
- Token OAuth lưu trong .env — rò rỉ = mất tài khoản; không commit .env.

## 6. Câu hỏi cần Hiệp quyết trước khi tích hợp
1. Đăng LinkedIn dưới tên cá nhân Hiệp hay Company Page OneUp? (quyết định w_member_social vs Community Management approval)
2. Giai đoạn 1 chỉ draft bằng fork repo (tự host LangGraph+Anthropic+FireCrawl) hay dùng Typefully draft API cho nhẹ?
3. Có chấp nhận chi phí X API pay-per-use ($0.015-$0.20/bài) khi bật đăng thật không, hay luôn đăng thủ công?
4. Giọng mẫu: Hiệp cung cấp 3-5 bài X/LinkedIn mẫu để làm TWEET_EXAMPLES?
5. Ai là người duy nhất có quyền Accept? Có cần lưu lịch sử nháp/link đã dùng ở đâu (repo có sẵn cơ chế chặn trùng link)?

## Nguồn
- Repo + README + LICENSE + file nguồn: https://github.com/langchain-ai/social-media-agent (README.md, LICENSE, .env.quickstart.example, .env.full.example, src/agents/generate-post/generate-post-graph.ts, src/agents/shared/nodes/generate-post/human-node.ts, schedule-post.ts, src/agents/upload-post/index.ts, src/agents/shared/nodes/verify-general.ts)
- X API pricing: https://docs.x.com (pay-per-use, Post Create $0.015 / có URL $0.20)
- LinkedIn: Microsoft Learn "Share on LinkedIn" (w_member_social) & Posts API (w_organization_social, Community Management)
- Arcade pricing: https://www.arcade.dev/pricing | Typefully API: https://typefully.com/docs/api
