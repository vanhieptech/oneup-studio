---
title: "Sổ nguồn văn nói và kiến thức cho kịch bản"
date: 2026-11-26
id: resources.vn-spoken.sources
type: resource
status: ready
updated: 2026-11-26
tags: [resources, spoken-vietnamese, sources, license]
source: "Nghiên cứu 26/11/2026 (TinyFish search; link kiểm ngày 26/11)"
---
# Sổ nguồn văn nói và kiến thức

Mỗi nguồn ghi giấy phép và được dùng tới đâu. Lời thật (giọng Hiệp, comment, phụ đề) quý hơn sách hay từ điển; sách và từ điển chỉ để tra thuật ngữ và kiểm từ.

## Luật dùng
- Kiến thức, số liệu: lấy từ nguồn gốc, nói lại bằng lời mình; HowToLiveBetter luôn credit CC BY 4.0.
- Lời của người khác (comment, phụ đề, podcast): chỉ rút **cụm ngắn** (< 10 chữ) để học cách nói, ghi link. Không chép câu dài vào script, không lưu bản chép đầy đủ trong git.
- Không tải sách/từ điển từ nguồn lậu. Thành ngữ dùng ít, chỉ để chốt ý.
- Comment: không ghi tên người comment.

## A. Cách nói tự nhiên (xếp theo giá trị)
| # | Nguồn | Dùng để | Cách lấy | Giấy phép / phạm vi |
|---|---|---|---|---|
| 1 | Voice memo của Hiệp | Giọng kênh thật | Hiệp thu 3–5 memo 1–2 phút → faster-whisper local (`pipeline/paths.py` `ASR_PYTHON`) → `content/voice-profile.md` §4 | Của Hiệp |
| 2 | Comment TikTok dưới clip top cùng chủ đề | Người xem tự nói nỗi đau → hook | `pipeline/trends/apify-run.py` (actor `clockworks/tiktok-comments-scraper`) | Chỉ cụm ngắn + link, không tên người |
| 3 | Phụ đề creator cùng ngách | Nhịp giải thích 60–90s | Apify (`subtitle_or_transcript`), `templates/clip-teardown.md` mục 4 | Học nhịp, không chép câu, không commit nguyên phụ đề |
| 4 | Podcast: «Phát triển bản thân» (Fonos), The Present Writer (Chi Nguyễn), Tri Kỷ Cảm Xúc, On Balance, Have A Sip, Mây Podcast | Kể chuyện cá nhân → bài học | Nghe; ghi chú ở `research/references/explainer-moves.md` | Có bản quyền: ghi cách làm, không lưu bản chép |
| 5 | Edutainment: Kiến Không Ngủ (TikTok ~2,3 triệu follow), Minh Xin Chào, Khánh Vy, Spiderum, Giang Ơi | Biến kiến thức khô thành câu dễ nghe | Như trên | Như trên |
| 6 | Từ Nam Bộ: Đáng Nhớ «260 từ ngữ thông dụng của dân Sài Gòn» (đã dùng trong `phrase-bank.md`); «Từ điển Từ ngữ Nam Bộ», Huỳnh Công Tín, NXB KHXH 2007 | Từ địa phương đúng nghĩa | Từ điển: mua bản giấy / mượn thư viện; **không tải các bản PDF trôi nổi** | Từ điển từng bị phản ánh một định nghĩa sai (2022) → tra chéo |
| 7 | Thành ngữ: Wiktionary tiếng Việt «Thể loại:Thành ngữ tiếng Việt» | Chốt ý, dùng ít | Tra khi cần | CC BY-SA; thành ngữ dân gian không ai giữ quyền |
| 8 | Tần suất từ: FrequencyWords `vi` (Hermit Dave, OpenSubtitles 2018) | Đo một từ có hay được *nói* | `resources/vn-dict/vi_50k.txt` → `check-rules.py --bookish` | Dữ liệu CC BY-SA 4.0, code MIT; chỉ dùng trong checker nội bộ, ghi nguồn |
| 9 | Kho giọng nói ASR (danh mục «awesome-vietnamese-speech-datasets»; VIVOS CC BY-NC-SA) | — | Không dùng | Chủ yếu giọng đọc hoặc bộ thương mại; giá trị thấp cho việc viết |

**Lỗ hổng:** đa số podcast/creator ở trên nói giọng Bắc (học nhịp, không học từ địa phương). Chưa có creator miền Nam cùng ngách đã kiểm → chờ Hiệp gợi ý 2–3 kênh.

## B. Kiến thức chủ đề (nói đúng)
| Nguồn | Dùng để | Giấy phép / phạm vi |
|---|---|---|
| HowToLiveBetter «Cẩm nang sống đáng giá» (chuanman2707) | Nguồn kiến thức chính | CC BY 4.0, credit như hiện tại |
| Paper gốc (vd Lally et al. 2010) | Số liệu + giới hạn | Mở bản gốc để kiểm (make-video §4b) |
| Bản dịch tiếng Việt: «Atomic Habits – Thói quen nguyên tử», «Sức mạnh của thói quen» (Duhigg) | Biết người Việt quen gọi khái niệm bằng chữ gì («vòng lặp thói quen: tín hiệu – hành động – phần thưởng») | Có bản quyền: chỉ biết thuật ngữ, không chép, không lưu nội dung |
| Vietcetera (vd «Lầm tưởng thông thường của chúng ta về tự kỷ luật») | Cách giải thích nghiên cứu bằng tiếng Việt phổ thông | Có bản quyền: đọc tham khảo |
| Wikipedia tiếng Việt | Tra tên khái niệm | CC BY-SA, chỉ tra |

## C. Công cụ lấy nguồn
| Công cụ | Dùng cho | Không dùng cho |
|---|---|---|
| TinyFish `search` / `fetch` (miễn phí, CLI `tinyfish` + MCP) | Tìm clip TikTok (link, caption, ngày), báo, YouTube, bài và paper | Đọc trang clip TikTok (bị chặn, đã thử 26/11) |
| Apify (gói free, 5 USD/tháng) | Số liệu, phụ đề, comment TikTok cho link đã tìm | Tìm kiếm rộng (để TinyFish làm) |
| Gemini CLI | Xem + nghe video để phân tích nhịp, hình, âm thanh | Viết lời |
