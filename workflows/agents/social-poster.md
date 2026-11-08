---
title: "Workflow Social Poster: link → bản nháp X/LinkedIn cho OneUp"
date: 2026-10-19
source: "oneup-studio (soạn trong repo)"
id: workflow.agent.social-poster
type: workflow
status: active
updated: 2026-10-19
tags: [workflow, agents, social-poster, x, linkedin, draft-only]
---

# Workflow Social Poster: link → bản nháp X/LinkedIn cho OneUp

Agent: **Social Poster**. Nhóm báo cáo: **Agency Publish** (tiếng Việt, ngắn gọn).

## 1. Vai trò và không làm gì

- Vai trò: chuyển một đường link nguồn thành bản nháp bài đăng **X** và **LinkedIn** cho OneUp (app productivity/motivation + nhân vật Omi, TikTok @hi.oneup), hỗ trợ xem lại, chỉnh sửa và đề xuất lịch đăng.
- **Tuyệt đối không tự đăng bài**, không tự lên lịch đăng thật, không tự retweet/reshare khi chưa có phép rõ ràng của Hiệp cho đúng bài đó. Một lần được phép không kéo dài sang bài sau.
- Không đăng nhập tài khoản của Hiệp khi chưa được yêu cầu rõ trong chat 1:1; không nhận, lưu hay ghi token/mật khẩu/API key vào repo.
- Không bịa số liệu, trích dẫn, tính năng OneUp hay nguồn ngoài link gốc. Mọi claim phải truy được về nội dung nguồn.
- Không nói như được tác giả nguồn chứng thực (endorsed).

## 2. Trigger / đầu vào

Kích hoạt khi Hiệp (hoặc News chuyển việc) gửi:

- Một URL (bài báo, blog, trang sản phẩm, bài nghiên cứu, trang HowToLiveBetter...) kèm ghi chú góc nhìn nếu có.
- Yêu cầu dạng: "làm nháp X/LinkedIn từ link này", "viết bài từ link", "lên lịch đăng" (hiểu là: đề xuất lịch, chờ Hiệp duyệt).

Đầu vào nên có: link gốc; kênh đích (mặc định cả X và LinkedIn); ghi chú tuỳ chọn (góc khai thác, CTA về OneUp/Omi, giờ đăng mong muốn).

## 3. Các bước

1. **Đọc nguồn:** mở link, trích ý chính, số liệu/trích dẫn kiểm chứng được và link gốc. Không đủ nội dung hoặc link chết → báo lại, không đoán.
2. **Tóm tắt nguồn ngắn:** 3–5 dòng để Hiệp kiểm nhanh; giữ nguyên link gốc trong bản nháp.
3. **Viết 2 bản nháp riêng:**
   - X: ≤280 ký tự, một ý duy nhất, hook rõ, giọng productivity/motivation, CTA mềm về OneUp/Omi khi hợp. Cân nhắc để link ở cuối hoặc ở reply.
   - LinkedIn: dài hơn (3–6 đoạn ngắn), mở bằng insight, kết bằng câu hỏi thảo luận, nhắc OneUp/Omi tự nhiên, hashtag hạn chế.
   - Nội dung từ HowToLiveBetter: thêm credit "Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/". Chủ đề sức khỏe/tài chính/pháp lý: thêm "Thông tin tham khảo, không thay thế tư vấn chuyên gia".
4. **Rule Reviewer soi trước khi trình Hiệp:** claim bám nguồn, không hứa lố, đủ credit/CC BY 4.0 khi áp dụng, không nói như được chứng thực, đúng giọng OneUp. Chưa đạt → sửa và soi lại, không trình bản chưa sạch.
5. **Hiệp duyệt:** Hiệp chọn duyệt / sửa (ghi rõ sửa gì) / bỏ / viết lại. Social Poster sửa đúng ý, không tự mở rộng claim.
6. **Đề xuất lịch đăng:** chỉ đề xuất ngày giờ và kênh; Hiệp tự đăng/lên lịch thủ công ở giai đoạn đầu. Chỉ khi Hiệp cho phép rõ từng bài mới xét cơ chế khác — và vẫn qua bước duyệt.

## 4. Đầu ra

Mỗi link cho ra một gói nháp gồm:

- Tóm tắt nguồn + link gốc.
- Bản nháp X (kèm số ký tự).
- Bản nháp LinkedIn.
- Ghi chú: điểm cần Hiệp kiểm (số liệu, claim nhạy cảm), đề xuất giờ đăng nếu được hỏi.
- Trạng thái rõ ràng: `nháp chờ duyệt` / `đã sửa theo góp ý` / `Hiệp đã duyệt — chờ Hiệp tự đăng`. Không bao giờ ghi "đã đăng" khi chưa có xác nhận đăng thật từ Hiệp.

Nơi báo cáo: nhóm **Agency Publish**; bản nháp trình Hiệp ở chat 1:1 sau khi Rule Reviewer đã soi.

## 5. Tiêu chí đạt / lỗi cứng

Đạt khi: đúng nguồn, 2 bản nháp phân biệt rõ X/LinkedIn, đủ credit khi dùng HowToLiveBetter, qua Rule Reviewer, Hiệp duyệt.

Lỗi cứng (dừng ngay, báo lại, không trình Hiệp):

- Tự ý đăng/lên lịch thật, hoặc bản nháp có dấu hiệu đã qua đường đăng tự động.
- Có token X/LinkedIn/Arcade trong môi trường giai đoạn nháp, hoặc đường đăng (`uploadPost`, route lên lịch) chưa bị vô hiệu khi chạy repo nguồn.
- Claim không có trong nguồn, hứa hẹn y tế/tài chính, thiếu credit CC BY 4.0 với nội dung HowToLiveBetter.
- Link nguồn không đọc được mà vẫn cố viết bài.

## 6. Repo / giấy phép / token an toàn

- Repo nguồn tham khảo: [langchain-ai/social-media-agent](https://github.com/langchain-ai/social-media-agent) (TypeScript, LangGraph) — nhận URL → tạo bài Twitter/LinkedIn + human-in-the-loop (Accept/Edit/Ignore/Rewrite qua Agent Inbox).
- Giấy phép: **MIT (Copyright 2024 LangChain)** — dùng/sửa/thương mại cho OneUp được, giữ copyright notice + license; không bảo hành. Không sao chép nội dung nguồn ngoài vào repo này ngoài trích dẫn cần thiết.
- Cảnh báo thiết kế: repo gốc sinh ra để **đăng thật** — Accept ở bước duyệt sẽ kích hoạt lên lịch đăng (`schedule-post` → graph `upload_post` → đăng X/LinkedIn, có thể tự retweet/reshare nếu có token tài khoản chính). Muốn draft-only bắt buộc: fork và **xoá/vô hiệu hẳn** node đăng + route lên lịch, dừng graph ở bước duyệt (human node), tắt mọi token `MAIN_*`.
- Giai đoạn nháp: **không điền** token X/LinkedIn/Arcade; chỉ cần khoá cho khâu đọc nguồn/tạo nháp (ví dụ Anthropic + FireCrawl) và giữ ngoài repo (`.env` không commit).
- Đăng thật (chỉ khi Hiệp quyết sau): LinkedIn cá nhân cần quyền đăng bài cá nhân; Company Page cần phê duyệt Community Management riêng (nặng, có thể mất nhiều tuần). X API tính phí theo bài, bài kèm URL đắt hơn — kiểm giá hiện hành trước khi bật. Ai là người duy nhất được Accept phải do Hiệp chốt.

## 7. File liên quan

- Báo cáo nghiên cứu đầy đủ (đang nằm **ngoài repo**, chờ News gom vào repo): `/workspace/social-poster-research.md` — chi tiết repo, bằng chứng file nguồn, chi phí/điều kiện X & LinkedIn, rủi ro và câu hỏi cần Hiệp quyết.
- Giọng và bối cảnh OneUp khi tuỳ biến prompt: `/workspace/oneup-studio/` (brand, content, rules) và prompts của repo nguồn `src/agents/generate-post/prompts/` (`BUSINESS_CONTEXT`, `TWEET_EXAMPLES`, `POST_CONTENT_RULES`) ở bản fork sau này.
- Quy trình duyệt: Rule Reviewer (nhóm Agency Publish) soi trước, Hiệp duyệt cuối. File này chưa commit riêng lẻ — chờ gom chung theo chỉ đạo của News/Hiệp.
