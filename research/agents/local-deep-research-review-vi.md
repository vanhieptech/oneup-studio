---
title: "Nghiên cứu: local-deep-research cho kiểm chứng fact"
date: 2026-10-19
source: "agent research 19/10/2026 (goc o /workspace, da gom vao repo)"
id: research.local-deep-research
type: research
status: reference
updated: 2026-10-19
tags: [research, fact-check, deep-research]
---
# Đánh giá Local Deep Research (LDR) cho kiểm chứng fact trước khi viết script TikTok @hi.oneup

- Ngày đọc: 19/10/2026 (Asia/Saigon)
- Repo: https://github.com/LearningCircuit/local-deep-research
- Phạm vi: chỉ đọc README, LICENSE, docs/ và SECURITY.md qua WebFetch. Không cài đặt, không clone. Mọi claim dưới đây truy tới URL cụ thể; chỗ không tìm thấy ghi rõ "không thấy trong repo".

## 1. Giấy phép — kết luận trước

- **License chính xác: MIT License, Copyright (c) 2025 LearningCircuit.**
  - File: https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/LICENSE
  - Trang repo tương ứng: https://github.com/LearningCircuit/local-deep-research/blob/main/LICENSE
  - README xác nhận lại: "MIT License - see [LICENSE](LICENSE) file." tại https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/README.md (mục `## 📄 License`)
- Nội dung MIT trong LICENSE cho phép: use, copy, modify, merge, publish, distribute, sublicense, and/or sell, với điều kiện giữ copyright notice + permission notice trong copies/substantial portions. Phần mềm cung cấp "AS IS", không bảo hành.
- README còn ghi: "Dependencies: All third-party packages use permissive licenses (MIT, Apache-2.0, BSD, etc.)" (cùng README ở trên). Đây là tuyên bố của repo, không phải kiểm toán license độc lập của từng dependency/model/search API.
- **Đánh giá thương mại cho kênh/agency:** Về mặt license của chính LDR, MIT là permissive, không phải copyleft (không GPL/AGPL) và không thấy điều khoản non-commercial trong LICENSE đã đọc. Do đó dùng nội bộ, dùng thương mại cho kênh/agency, sửa đổi/phân phối lại đều không bị LICENSE này cấm, miễn là giữ notice khi phân phối copies/substantial portions.
- **Cảnh báo tách lớp:** MIT của LDR không tự động cấp quyền cho (a) model LLM tải về (mỗi model có license riêng — repo không liệt kê license cho từng model trong các file đã đọc), (b) nội dung web/bài báo/paper lấy về (copyright của nguồn gốc), (c) API cloud/premium search (điều khoản + phí của nhà cung cấp), (d) dữ liệu OpenAlex/DOAJ/arXiv/PubMed... được liệt kê ở mục Acknowledgements trong README với license/terms riêng (ví dụ OpenAlex CC0, Semantic Scholar có Terms riêng). Trước khi dùng thương mại ở quy mô agency, phải kiểm tra riêng 3 lớp này. Không thấy trong repo cam kết indemnity/SLA thương mại.

## 2. LDR là gì, tính năng chính

Theo README (https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/README.md):

- "AI-powered research assistant for deep, agentic research" — "Performs deep, agentic research using multiple LLMs and search engines with proper citations".
- Luồng: đặt câu hỏi phức tạp → tự tìm kiếm trên web, academic papers và tài liệu của bạn → tổng hợp thành report có citations.
- Chiến lược nổi bật `langgraph-agent`: LLM tự quyết định search gì, dùng engine chuyên biệt nào (arXiv, PubMed, Semantic Scholar...), khi nào tổng hợp; README nói đây là strategy đứng sau kết quả ~95% SimpleQA được công bố.
- Knowledge base/Library: download sources vào encrypted library, extract text, index & embed, rồi search lại trên chính tài liệu đó kết hợp live web.
- Research modes (README + docs/features.md https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/features.md):
  - Quick Summary: 30 giây–3 phút, có citations (README); features.md nói automatic query decomposition, parallel search, citation tracking.
  - Detailed Research: phân tích sâu, section-based, cross-reference validation (features.md).
  - Report Generation: report có sections, table of contents, export PDF/Markdown (README + features.md).
  - Document Analysis: search tài liệu riêng bằng vector semantic search (features.md).
  - Chat Mode: experimental, multi-turn, luôn chạy quick mode v1 (features.md + faq.md).
- Export: PDF/Markdown (README); features.md liệt kê thêm JSON, plain text, HTML.
- Khác: REST API, Python API (`quick_query`, `LDRClient`, `quick_summary`), MCP server cho Claude Desktop/Code (8 tools: search, quick_research, detailed_research, generate_report, analyze_documents...), Benchmarking (SimpleQA), Analytics Dashboard, Journal Quality System (README).

### Benchmark mà repo tự công bố — phải đọc kèm caveat

README (mục Benchmarks): dùng `langgraph-agent` + Serper (cloud) search + model local Ollama:

| Model | SimpleQA | xbench-DeepSearch |
|---|---|---|
| Qwen3.6-27B | 95.7% (287/300) | 77.0% (77/100) |
| Qwen3.5-9B | 91.2% (182/200) | 59.0% (59/100) |
| gpt-oss-20B | 85.4% (295/346) | không thấy số |

Repo tự ghi caveat ngay dưới bảng: "Caveats: small samples, LLM-grader noise, and SimpleQA contamination risk on newer base models." Đầu README cũng ghi "~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090)".

=> Không được dịch con số này thành "đúng 95% mọi fact cho TikTok tiếng Việt". Không thấy trong repo benchmark riêng cho tiếng Việt, cho nội dung TikTok, hay cho fact-check báo chí Việt Nam.

## 3. Cách cài / chạy: local vs cloud

Nguồn: README mục Quick Start + Supported LLMs; docs/faq.md https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/faq.md

### 3.1 Ba cách cài (README)

1. Docker Run (Linux): chạy Ollama + SearXNG + LDR bằng Docker; mở http://localhost:5000. Lưu ý `--network host` chỉ native Linux, Docker Desktop Mac/Windows/WSL2 sẽ lỗi port/localhost.
2. Docker Compose: CPU-only (mọi platform) hoặc kèm GPU override (NVIDIA Linux).
3. `pip install local-deep-research` rồi `python -m local_deep_research.web.app` (localhost:5000). Vẫn cần Ollama (hoặc OpenAI-compatible endpoint) + SearXNG theo pip guide.

### 3.2 Local LLM

README mục Supported LLMs — Local Models:
- Ollama (native API, mặc định http://localhost:11434)
- LM Studio (OpenAI-compatible server, mặc định http://localhost:1234/v1)
- llama.cpp qua `llama-server` OpenAI-compatible endpoint (mặc định http://localhost:8080/v1)
- Model phổ biến nêu: Llama, Mistral, Gemma, DeepSeek, Qwen.
- "No API costs for locally-run models" và inference chạy trên hardware của bạn khi model thật sự chạy local.

### 3.3 Cloud LLM

README liệt kê: OpenAI, Anthropic Claude, Google Gemini, 100+ models qua OpenRouter, 100+ qua Requesty. Custom endpoints: OpenAI-compatible (vLLM, llama.cpp, gateways) và Anthropic-compatible tự host.

faq.md xác nhận chi phí phát sinh chỉ khi dùng cloud LLM, premium search API, hoặc cloud hosting; local Ollama + free search thì không tốn các chi phí đó ("Is LDR really free?").

### 3.4 Phần cứng / yêu cầu hệ thống

faq.md mục "What are the system requirements?":
- Python 3.10+, RAM 8GB minimum (16GB recommended cho model lớn hơn)
- GPU VRAM cho Ollama: 7B cần 4GB, 13B cần 8GB, 30B cần 16GB, 70B cần 48GB
- Disk: 100MB cho LDR, 1–2GB SearXNG, 5–15GB mỗi Ollama model
- OS: Windows, macOS, Linux

README bổ sung: CPU x86-64 cần AVX (Intel Sandy Bridge / AMD Bulldozer 2011 trở mới hơn), ARM64 supported; thiếu AVX có thể crash `Illegal instruction` với pandas/scikit-learn wheels.

## 4. Nguồn dữ liệu / search engines / RAG tài liệu cá nhân

Nguồn chính: docs/search-engines.md https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/search-engines.md và README mục Search Sources.

### 4.1 Free (không API key theo search-engines.md)
- Academic: arXiv, PubMed, Semantic Scholar
- General: Wikipedia, SearXNG (meta-search, aggregate Google/Bing/DuckDuckGo...)
- Technical: GitHub, Elasticsearch
- Archive: Wayback Machine qua `fetch_archive` cho URL đã biết
- News: The Guardian (search-engines.md ghi "Requires API key (free tier available)" — tức không hoàn toàn key-free), Wikinews

### 4.2 Premium (cần API key)
- Tavily, Google qua SerpAPI, Google Programmable Search Engine, Brave Search. search-engines.md cho ví dụ biến môi trường dạng `LDR_SEARCH_ENGINE_TAVILY_API_KEY=...`, `LDR_SEARCH_ENGINE_WEB_SERPAPI_API_KEY=...`, `LDR_SEARCH_ENGINE_WEB_GOOGLE_PSE_API_KEY=...` + `..._ENGINE_ID=...`, `LDR_SEARCH_ENGINE_WEB_BRAVE_API_KEY=...`.

### 4.3 Custom / local docs / RAG
- Local Documents: PDF, TXT, MD, DOCX, CSV "and more"; Collections trong Web UI, upload, indexing, "Search All Collections" (Library RAG) — faq.md mục Local Document Search và search-engines.md mục Custom Sources.
- LangChain retrievers: FAISS, Chroma, Pinecone, Weaviate, Elasticsearch và mọi LangChain-compatible retriever (README mục Bring Your Own Knowledge Base).
- Library vòng khép kín: Research → Download Sources → Library → Index & Embed → Search Your Docs → quay lại Research (README).

### 4.4 Cách trích dẫn nguồn trong output
- README: report "with proper citations"; Quick Summary "Get answers in 30 seconds to 3 minutes with citations"; Report Generation có bibliography/sections (features.md).
- features.md: Quick Summary có "Citation tracking", Detailed có "Detailed citation management", Report có "Bibliography management", Export Markdown "with citations".
- search-engines.md (Wayback): kết quả giữ original URL, archive URL và actual capture timestamp UTC; hướng dẫn "cite the actual capture date rather than the requested date".
- Giới hạn cần hiểu: repo mô tả cơ chế citation tracking/bibliography, nhưng không thấy trong các file đã đọc một cam kết rằng mọi câu trong output đều có citation đúng, hay citation không bị LLM gán sai nguồn. Vì vậy citation của LDR là điểm khởi đầu để kiểm chứng, không phải bằng chứng cuối cùng (xem checklist mục 7).

## 5. Dữ liệu có rời máy không? — tùy cấu hình, đây là điểm quan trọng nhất

Nguồn: README mục Security / Egress control / Privacy & Data; SECURITY.md https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/SECURITY.md

Repo tự tuyên bố:
- "Local Deep Research contains no telemetry, no analytics, and no tracking." Network calls duy nhất là do bạn khởi tạo: search queries tới engine đã cấu hình, LLM API calls tới provider đã chọn, notifications nếu tự setup Apprise.
- Mỗi user có SQLCipher database riêng, AES-256, key derive từ password (PBKDF2-HMAC-SHA512, 256,000 iterations theo SECURITY.md), password không lưu; per-user LLM API keys nằm encrypted trong DB cá nhân.

Nhưng repo cũng tự cảnh báo rõ các đường dữ liệu vẫn rời máy:
1. **Search luôn ra internet nếu dùng web search.** README: "A self-hosted SearXNG still forwards your search queries to its upstream engines on the internet." faq.md: offline chỉ với local LLM + local documents; "web search requires internet".
2. **Cloud LLM = prompt rời máy.** Chọn OpenAI/Anthropic/Gemini/OpenRouter/Requesty là gửi nội dung truy vấn + ngữ cảnh tới provider đó.
3. **Local endpoint có thể trá hình.** README + SECURITY.md: LDR đánh giá locality chủ yếu theo provider + endpoint address, không theo nơi model thật chạy; Ollama cloud model hoặc LiteLLM/OpenAI-compatible proxy local đứng trước hosted API "can still send your prompts off the machine without being detected".
4. **Egress scope chỉ là best-effort guardrail, không phải air gap.** README + SECURITY.md (Egress Policy Module): "in-process correctness guardrail, NOT a hard security boundary", có known gaps (DNS rebinding TOCTOU, forward proxy, code chạy trong cùng process...). Muốn hard boundary phải thêm firewall/container egress filtering.
5. Egress modes (README bảng): Adaptive (default, theo primary engine), Public only (web/academic công khai, loại private collections), Private only (chỉ local sources, forced local inference, cloud bị refuse), Strict (chỉ primary engine, cloud thường fail), Unprotected (mặc định bị khóa, cần operator bật `LDR_POLICY_ALLOW_UNPROTECTED_EGRESS=true`).
6. MCP server (README): thiết kế local-only qua STDIO, "no built-in authentication or rate limiting. Do not expose over a network..."

Kết luận riêng tư: chỉ khi cấu hình đồng thời (local LLM thật chạy trên máy + Private only/Adaptive-private + chỉ search collections/library local) thì nội dung nghiên cứu mới ở lại máy theo thiết kế của repo. Ngay khi bật SearXNG/web search hoặc cloud LLM, truy vấn/nội dung liên quan sẽ rời máy tới engine/provider tương ứng.

## 6. Giới hạn / rủi ro nổi bật đã nêu trong repo

1. **Docs tự nhận có thể không chính xác.** faq.md, search-engines.md, features.md đều mở đầu: "This documentation is maintained by the community and may contain inaccuracies... please verify critical information". README là nguồn đáng tin hơn docs phụ, nhưng vẫn phải đối chiếu khi quyết định quan trọng.
2. **Benchmark mẫu nhỏ, grader noise, contamination risk** — repo tự ghi (README Benchmarks). Không suy ra độ chính xác cho chủ đề tiếng Việt/y tế/tài chính/pháp lý.
3. **Trang chặn bot sẽ không fetch được.** README: LDR tôn trọng robots.txt, tự nhận diện honestly, "no stealth or anti-detection techniques... a page that blocks automated access won't be fetched". Hệ quả fact-check: nguồn gốc có thể thiếu, phải mở tay để đối chứng.
4. **Search engine fail có thể im lặng.** search-engines.md mục Temporarily Disabled Engines mô tả chi tiết cooldown/disable, đồng thời ghi nhiều engine "fail silently per request: they return empty results, stay available, and are never disabled". Thiếu kết quả không đồng nghĩa fact sai/không tồn tại.
5. **Rate limit / captcha / SearXNG cấu hình.** faq.md: captcha từ search engines, SearXNG localhost bị block mặc định từ v1.10.3 (SSRF protection) cần operator allowlist/env-lock; "Search snippets only" phải bật cho SearXNG.
6. **Bảo mật vận hành nếu tự host.** SECURITY.md: credentials ở plaintext trong process memory khi session active (repo giải thích đây là industry-wide reality, có mitigation session-scoped + core dump exclusion); bản fallback `LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=true` không verify password, "unsuitable for shared deployments" (README). Chỉ fix security cho latest release ("Security fixes are only provided for the latest release").
7. **Nâng cấp có rủi ro khóa DB.** README mục Upgrading: bản FastAPI mới không rollback trực tiếp về v1.10.7 trên DB đã upgrade, phải backup `encrypted_databases/backups/` ra ngoài data dir ngay sau lần đăng nhập đầu. Vận hành agency nhiều user cần quy trình backup trước upgrade.
8. **Không thấy trong repo:** hỗ trợ/độ chính xác tiếng Việt được cam kết; workflow TikTok; cơ chế tự động phân định tin giả tiếng Việt; SLA hỗ trợ thương mại; license của từng model gợi ý. Các điểm này phải tự kiểm chứng bằng pilot, không suy diễn từ README.

## 7. Đánh giá phù hợp cho @hi.oneup: kiểm chứng fact + nghiên cứu sâu trước khi viết script

### Nên dùng chế độ nào ở giai đoạn đầu?
**Khuyến nghị: GO có điều kiện — pilot 2–3 tuần, hybrid, chưa thay thế kiểm chứng tay.**

- **Nếu máy có GPU NVIDIA ~16GB VRAM trở lên (mốc 30B theo faq.md) hoặc chấp nhận model nhỏ 7–13B:** bắt đầu bằng Docker Compose + Ollama local + SearXNG, strategy `langgraph-agent`, egress Adaptive. Lý do: đúng thế mạnh repo thiết kế (local inference, không phí API, benchmark local tốt nhất repo công bố là Qwen3.6-27B trên RTX 3090), dữ liệu nháp script chưa công khai không phải gửi cloud LLM. Nhưng nhớ search query vẫn ra internet qua SearXNG upstream.
- **Nếu chưa có GPU phù hợp:** đừng mua phần cứng ngay theo benchmark. Pilot bằng CPU Docker Compose + cloud LLM (OpenAI/Anthropic/OpenRouter theo README) ở egress Public only, chỉ đưa chủ đề công khai (không đưa tài liệu nội bộ agency, số liệu chưa công bố, hồ sơ khách hàng). Mục tiêu pilot là kiểm tra chất lượng citation + tốc độ + khả năng tiếng Việt thực tế — thứ repo không cam kết. Đạt ngưỡng mới đầu tư GPU/local.
- Với chủ đề nhạy cảm (y tế, tài chính, pháp lý, chính trị, claim về người thật): bắt buộc thêm nguồn học thuật/gốc (arXiv/PubMed/Semantic Scholar nếu liên quan, hoặc nguồn sơ cấp ngoài LDR) và người duyệt; không dùng riêng Quick Summary để kết luận.

### Vì sao phù hợp
- Đúng bài toán "từ câu hỏi → nhiều nguồn → report có citation → export Markdown/PDF" để làm brief trước script.
- Nhiều engine học thuật + web + Wayback giúp kiểm chứng chéo và xem bản lưu trữ theo thời gian.
- Library/RAG cho phép xây kho nguồn đã kiểm chứng của kênh (paper, bài gốc đã download) để các số sau tái sử dụng, thay vì search lại từ đầu.

### Đâu là rủi ro riêng cho kênh
- Bịa nguồn/gán sai citation: repo không cam kết citation luôn đúng (mục 4.4). Script TikTok nói nhanh, sai một số liệu là lan truyền ngay.
- Nguồn tiếng Việt: không thấy trong repo cam kết bao phủ báo/site Việt Nam; SearXNG phụ thuộc upstream engines. Phải tự test với claim Việt Nam cụ thể trong pilot.
- Copyright nội dung nguồn: MIT chỉ phủ phần mềm LDR. Dùng lại câu chữ/hình ảnh từ nguồn fetch về cho video thương mại là vấn đề riêng, cần paraphrase + dẫn nguồn, không sao chép nguyên văn dài.
- Vận hành: tự host = tự chịu backup, upgrade (rủi ro DB ở mục 6.7), giữ latest release để nhận security fix.

## 8. Quy trình mẫu: 1 chủ đề → báo cáo → script

### Input Hiệp cần đưa (mỗi chủ đề 1 brief ngắn)
1. Claim/câu hỏi trung tâm viết thành câu khẳng định có thể sai được (ví dụ: "X làm giảm Y Z% trong N tuần").
2. Bối cảnh: nguồn gốc claim (link TikTok/bài báo/người nói), vì sao kênh muốn làm, khán giả mục tiêu.
3. Phạm vi: thời gian, địa lý, đối tượng (Việt Nam hay quốc tế), mức nhạy cảm.
4. Nguồn bắt buộc nếu có: paper, trang gốc, tài liệu nội bộ (đánh dấu private/public cho collection).
5. Output mong muốn: góc script dự kiến + độ dài + hạn nộp.

### Các bước kiểm chứng chéo
1. Chạy LDR Detailed Research hoặc `langgraph-agent` (không chỉ Quick Summary) với primary `searxng`; với claim khoa học/y tế, bật/tra thêm arXiv, PubMed, Semantic Scholar theo search-engines.md.
2. Tách output thành từng atomic claim. Mỗi claim phải có ít nhất 2 nguồn độc lập, trong đó ưu tiên 1 nguồn sơ cấp (paper gốc, cơ quan ban hành, dữ liệu gốc). Hai bài cùng chép một nguồn chỉ tính là 1.
3. Mở trực tiếp URL gốc (không tin snippet/summary của LDR): kiểm tra tác giả, ngày, ngữ cảnh, số liệu có bị cắt khỏi điều kiện áp dụng không. Claim về quá khứ/thay đổi theo thời gian: dùng Wayback `fetch_archive` và ghi actual capture date (search-engines.md).
4. Đối chiếu số liệu giữa các nguồn: đơn vị, mẫu n, khoảng thời gian, định nghĩa. Khác nhau thì ghi mâu thuẫn, không tự chọn số đẹp hơn cho script.
5. Kiểm tra journal/source quality nếu là paper: repo có Journal Quality System (README), nhưng vẫn tự kiểm tra predatory journal/retraction ngoài LDR khi claim quan trọng.
6. Người duyệt (không phải model) ký duyệt các claim mức "dùng trong script". Claim không đủ nguồn thì hạ xuống "ý kiến/cần nói rõ chưa chắc chắn" hoặc bỏ.

### Output format đề xuất (bảng bắt buộc cho mỗi chủ đề)

| Claim (viết đúng sẽ nói trong script) | Nguồn (URL + ngày/capture date) | Mức tin cậy | Ghi chú cho script |
|---|---|---|---|
| ... | Nguồn sơ cấp + nguồn đối chứng độc lập | Cao / Trung bình / Thấp / Mâu thuẫn | Cách diễn đạt an toàn, điều kiện áp dụng, câu không được nói quá |

Kèm cuối báo cáo: (a) danh sách nguồn đã mở tay, (b) claim bị loại và lý do, (c) điểm còn chưa biết, (d) bản Markdown/PDF export từ LDR để lưu cùng brief.

Mức tin cậy gợi ý: Cao = ≥2 nguồn độc lập có nguồn sơ cấp, số khớp; Trung bình = 1 nguồn sơ cấp hoặc 2 nguồn thứ cấp uy tín; Thấp = chỉ snippet/một nguồn/báo lá cải; Mâu thuẫn = nguồn uy tín không thống nhất → không khẳng định trong script.

### Checklist chống bịa (dán vào cuối mỗi báo cáo)
- [ ] Mọi con số trong script đều truy được tới URL đã mở tay, không chỉ tới summary của LDR.
- [ ] Đã kiểm tra ngày xuất bản/capture date; số liệu không bị hết hạn hoặc bị rút (retraction/correction).
- [ ] Ít nhất 1 nguồn sơ cấp cho claim trung tâm; 2 nguồn độc lập cho claim gây tranh cãi/nhạy cảm.
- [ ] Đã đọc ngữ cảnh quanh số liệu (điều kiện, đối tượng, n) — không cắt câu đổi nghĩa.
- [ ] Phân biệt rõ: fact / diễn giải của tác giả / ý kiến — script không biến diễn giải thành fact.
- [ ] Claim tiếng Việt đã được test nguồn Việt hoặc ghi rõ chỉ có nguồn quốc tế.
- [ ] Không sao chép nguyên văn dài từ nguồn; đã paraphrase và chuẩn bị dòng dẫn nguồn/on-screen text.
- [ ] Claim mức Thấp/Mâu thuẫn đã bị bỏ hoặc nói kèm mức không chắc chắn; có người duyệt ký tên + ngày (Asia/Saigon).

## 9. Kết luận go / no-go

**GO có điều kiện cho pilot**, không go cho việc tự động tin output:
- Điều kiện 1: pilot đo thực tế trên 5–10 claim tiếng Việt của kênh (tỷ lệ citation mở được, tỷ lệ claim đủ 2 nguồn, thời gian mỗi báo cáo) trước khi đưa vào quy trình chính thức.
- Điều kiện 2: cấu hình riêng tư rõ ràng — local LLM + Private only cho tài liệu nội bộ; cloud chỉ cho chủ đề công khai. Ghi cấu hình đã dùng vào mỗi báo cáo.
- Điều kiện 3: giữ LDR ở latest release, backup DB trước upgrade, không bật unencrypted fallback cho môi trường dùng chung, không expose MCP/Web UI ra internet khi chưa có lớp bảo vệ riêng (repo cảnh báo MCP local-only).
- Nếu pilot cho thấy nguồn tiếng Việt yếu hoặc citation sai nhiều: **no-go cho fact-check tiếng Việt**, chỉ giữ LDR cho nghiên cứu nền quốc tế/học thuật và kiểm chứng tay cho claim Việt Nam.

## Nguồn đã đọc (link trực tiếp)

- LICENSE (MIT, Copyright (c) 2025 LearningCircuit): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/LICENSE — bản trên GitHub: https://github.com/LearningCircuit/local-deep-research/blob/main/LICENSE
- README chính (tính năng, Quick Start, benchmarks + caveats, search sources, Supported LLMs local/cloud, Security, Egress control, Privacy & Data, MCP, Upgrading, License): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/README.md — bản trên GitHub: https://github.com/LearningCircuit/local-deep-research/blob/main/README.md
- docs/search-engines.md (free/premium/custom engines, API keys, local documents, Wayback citation, engine fail/cooldown, giới hạn fetch): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/search-engines.md
- docs/faq.md (system requirements, offline, chi phí, SearXNG, local document search, lỗi/captcha/rate limit): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/faq.md
- docs/features.md (research modes, citation tracking/management, export, Chat Mode experimental): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docs/features.md
- SECURITY.md (SQLCipher, in-memory credentials, egress policy module là guardrail không phải hard boundary, locality best-effort, supported versions): https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/SECURITY.md
- Trang repo (mô tả ngắn, links Issues/PRs): https://github.com/LearningCircuit/local-deep-research

Ghi chú trung thực: các file docs trên đều có disclaimer của repo rằng community-maintained và "may contain inaccuracies"; báo cáo này ưu tiên README/LICENSE/SECURITY.md khi có khác biệt. Chưa đọc sâu từng file trong docs/ (ví dụ docs/egress-modes.md, docs/CONFIGURATION.md, docs/installation.md) và chưa kiểm tra Issues mở — ghi rõ là chưa đọc, không suy diễn.
