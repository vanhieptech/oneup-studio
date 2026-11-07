# Audit trend clip-05 — 07/11/2026

## Phạm vi và kết luận
Chỉ đọc repo /workspace/oneup-studio và tải một VTT công khai; không viết script, sửa repo, commit, chạy actor hoặc mua dữ liệu. Phạm vi nội dung hiện tại là **23.14 tự kiểm tra**, không phải 23.15 học dồn dù tên thư mục còn clip-05-hoc-mot-dem.

**Kết luận:** @gonaox là ứng viên mới hơn có tương tác lớn tại snapshot 06/11 và transcript thực sự chứa tự nhớ lại. Chỉ phần tự kiểm phù hợp 23.14; không nhận nguyên công thức 3–2–1 làm khuyến nghị khoa học. Chưa có comment của clip này, chưa có chuỗi tăng trưởng hay nhiều tài khoản để khẳng định trend đang hot. Không ép cầu nối.

## VTT mới kiểm trực tiếp
- Clip: https://www.tiktok.com/@gonaox/video/7702426588662598920
- VTT: https://api.apify.com/v2/key-value-stores/sIQXBij3ttUwrYwhT/records/subtitle-gonaox-20261030114907-7702426588662598920-vie-VN.vtt
- File tải: `/workspace/gonaox-7702426588662598920-vie-VN-retrieved-2026-11-07.vtt`
- Tải thành công qua curl lúc **07/11/2026 12:51:27 (Asia/Saigon)**; WebFetch cũng đọc được toàn văn. SHA256: `566aa9e5aaaa68b776d71e6bf8b0a072285f06da7209aebdebd39e50aa0ee862`.
- Đây là **ASR vie-VN**, không phải bản chép tay đã đối chiếu âm thanh; chưa xem/nghe video. Toàn bộ phụ đề dài 00:00.080–02:48.600 đã được đọc.
- Hook nguyên văn ASR (00:00.080–00:01.960): “ghi nhớ bất cứ thứ gì nhanh đến mức khó tin”.
- Sau đó so người học ba tiếng với bạn học 40 phút, hứa học kỹ thuật trong năm phút; hỏi người xem thường đọc lại hay viết ra giấy.
- Phương pháp thật: **3 lần đọc** (lần đầu lấy cấu trúc, hai lần sau chi tiết); **2 vòng giải thích thành tiếng khi gấp sách/cất ghi chú**; **1 lần viết từ trí nhớ trên giấy trắng rồi so bản gốc, tìm và lấp chỗ thiếu**. Bối cảnh học sinh/học bài; ví dụ sinh học về hệ miễn dịch và virus.
- Câu then chốt 01:28.200–01:33.640: “gấp sách lại cất ghi chú đi … và giải thích những gì các bạn vừa đọc … thành tiếng từ trí nhớ”.
- Cuối clip 02:41.321–02:44.840: “so những gì các bạn viết với bản gốc … các bạn sẽ thấy lỗ hồng hãy lấp chúng lại”.

### Sai số và claim không được kế thừa
- ASR viết hoa bất thường BA/AI/SAO/Chi/Cho/Theo; “AI đó”, “không có AI nhìn” ở ngữ cảnh này nhiều khả năng là “ai”, không phải trí tuệ nhân tạo. “lỗ hồng” nhiều khả năng là “lỗ hổng”. Chưa đối chiếu audio nên không âm thầm sửa bản gốc.
- Không thấy trích nghiên cứu/tác giả trong VTT. Không kế thừa các hứa hẹn: nhớ bất cứ thứ gì, học 40 phút hơn ba tiếng, sau lần ba từ tự tuôn ra, con số 3–2–1 tối ưu, viết không thể tự lừa, lỗ hổng chính là thứ sắp quên và nay được “khóa lại”.
- **Fit 23.14:** đóng tài liệu, tự nói/viết điều nhớ, mở lại kiểm và bổ sung. Dẫn chứng phải lấy từ fact package của Deep Research, không lấy độ viral làm chứng minh phương pháp.
- **Không fit 23.15:** không có phân bổ nhiều ngày/khoảng giãn giữa các buổi; 3 lần đọc không tự động là spaced practice.
- Không bê ví dụ sinh học vào clip (L-087). Chưa có comment để xác nhận người xem thật đang mắc đúng nỗi đau đọc rồi không kể được.

## Provenance và tương tác @gonaox
Nguồn repo: `research/trends/2026-11-06/apify/clockworks-search-raw.json`, `clips.json`, `runs.json`, `README.md`; commit tạo gói **9a4e548**. Đăng **30/10/2026 18:49:07 (Asia/Saigon)**. Snapshot lưu ngày 06/11: 1.400.000 view, 164.000 like, 24.300 share, 66.640 save, 685 comment, dài 168 giây. Không đo lại các số này hôm 07/11.

Discovery: actor clockworks/tiktok-scraper, run `U4Q4IU8uOOEibxDxV`, dataset `RVDekZrlSHVeA5Vsy`, KV `sIQXBij3ttUwrYwhT`. Dataset discovery chứa metadata clip, **không phải dataset comment**; raw ghi commentsDatasetUrl=null; bản normalize top_comments=[] và caption_fallback. VTT tải hôm nay lấp khoảng trống transcript, không làm mới metrics.

Đã kiểm toàn bộ `research/trends/2026-11-06/apify/comments-raw.json`: 54 comment chỉ thuộc @kiwilamdep/7704503079500139777, @amateurpsychology/7693909106041703713 và @nghemoi.official/7640877396073188629. README gắn comments run `B4eASt8kYPF5bR1U9`; runs.json không ghi dataset comment. **Không có comment @gonaox trong tập này, không có địa chỉ dataset comment riêng của @gonaox được xác nhận.** Không chạy actor mới để lấy.

## Gói chuyên biệt clip-05 đang dùng nhưng cũ
- `research/trends/2026-10-30/clip-05-v9-trend.md`, commit tạo **7fb1e4b**, snapshot ghi **30/10 18:25 (Asia/Saigon)**.
- `content/clips/clip-05-hoc-mot-dem/script-v10-draft-opencreator.md`, commit tạo **0d20d38**, vẫn dùng x-2114817316420805048 và trục 23.14.
- https://x.com/alexeixbt/status/2114817316420805048 — bài 26/10; Markdown ghi 5.825 like, 664 repost, 2.235 bookmark, khoảng 238k view. Không tìm thấy raw JSON của bài trong research. Đủ ghi nhận tương tác snapshot cũ, không đủ gọi hot 07/11.
- https://x.com/phrog_lmao/status/2115086418192089298 — bài 27/10, nói không nhớ những gì đọc, 0 like.
- https://x.com/yusrahscloset/status/2115675683485557166 — bài 29/10, 22 like, 658 view, đọc trước ngủ rồi quên sáng hôm sau.
- https://x.com/Nascan23/status/2116032457174868150 — bài 30/10, 0 like, đọc xong quên.
- https://x.com/Nguyenn259373/status/2112478702873497958 — bài 20/10, rất thấp, không ghi số cụ thể.
- Các bài dưới 25 like chỉ là ví dụ cá nhân, không gọi hot/đại diện đông đảo. Không kế thừa claim đọc chữa brain rot.
- `research/trends/2026-10-31/digest.md`, commit **575e161**, còn nhắc cần đồng bộ final/trend-signals.md khi chốt v9: không mặc định bản final đang đồng bộ v10.

## Ứng viên mới hơn nhưng không ép sang 23.14: #texthip
`research/trends/2026-11-05/digest.md`, commit **4014ab3**, snapshot 05/11, bài báo 04/11:
- https://www.vietnam.vn/trao-luu-nang-tam-van-hoa-doc-bo-phim-ngan-cua-gen-z-han-quoc
- https://www.koreatimes.co.kr/lifestyle/trends/20261104/viral-text-hip-trend-boosts-bookstore-sales-brings-literature-to-food-aisles
Bằng chứng báo chí về người trẻ Hàn đọc thay lướt. Không có clip/comment TikTok tương ứng trong gói. Số khảo sát 74,5%→75,3% chưa kiểm bản gốc, không dùng. Bridge đã lưu B-texthip-01 thuộc 4.15 giới hạn video ngắn, chưa được kiểm cho 23.14; cần bằng chứng nhu cầu nhớ lại nếu muốn nối.

## Gốc học dồn — lưu để phân biệt, không đề xuất cho scope 23.14
`research/trends/2026-10-20/digest.md`, `apify/` — **9254e06**; `social-research/tiktok-page-stats-2026-10-20.json` — **55939e0**.
https://www.tiktok.com/@ng__phanh/video/7532553338664045831 — đăng **30/07/2025 00:14:08 (Asia/Saigon)**, không mới năm 2026. Snapshot 20/10: 1,1 triệu view, 107.100 like, 55.300 share; Apify 695 comment, page-stats 700, không gộp hai số. Caption “Học 1 đêm mới hiểu sao kiến thức được dạy trong 1 kỳ”; không lời, caption fallback, không có VTT cho clip này.
Comment thật trong clips.json/raw-comments.json/comments-merged.json: “Sách mới tinh kh vết gấp mà😭” 3.269 like; “Tôi và quyển giáo trình gặp nhau lần đầu tiên tại quán photo trước 2 tiếng vào thi” 213; “Ko sao mình nhét ba môn cả kì trước 3 tiếng thi…” 132. Discovery run jRLleUhL5eClvRAgR; comments gm8VC17Ft1iCBacpv. Chỉ pattern cũ, không chứng minh quên sau một tuần hay hot hiện tại; nghiêng 23.15 nên không ép vào 23.14.

## Luật và fact phải giữ
Đã đọc phần liên quan của logs/lessons.md: L-037 (TikTok-native/subtitle/comment), L-084/088 (trend hiện trong hook, nguồn Social Research + fact Deep Research), L-087 (ví dụ đời thường), L-090 (đọc patterns + ba digest mới nhất, trend nói thành lời, cảnh báo >7 ngày, ví dụ có evidence), L-092/096 (không nối giả hai chủ đề, không dựng cảnh bàn trend). Digest 05–07/11 loại brain stacking vì bão hoà; không hồi sinh tên này.
`content/clips/clip-05-hoc-mot-dem/evidence-lines-v10.md`, **780bd6d**, ngày 31/10: Dunlosky 2013 đánh giá tự kiểm high utility và đọc lại low utility, không phải đọc lại vô dụng. Yang không phải so trực tiếp với đọc lại. Nghiên cứu không chứng minh trend hoặc công thức 3–2–1.
Digest 07/11 (**b60c888**) chưa cung cấp ứng viên cram/recall mới đã kiểm đầy đủ. AI reading fatigue không tự động hợp ghi nhớ; không chuyển cầu nối đã bị Deep Research bác thành kết luận.

## Git và tính bất biến snapshot
Audit local: origin/main=`b60c88820557c2ac0a79ef4f2c064ec4dc66dbd0`; HEAD=`8ddb986164fd58b295fbdb3c722e5534d0ad7047`, ahead 1/behind 0, b60c888 là tổ tiên HEAD. Commit ahead là FLUX kit, không phải gói trend. Các commit nghiên cứu nêu trên thuộc mốc b60c888.
News báo GitHub đã xác nhận b60c888 lúc 12:40 ngày 07/11 (Asia/Saigon); đây là thông tin được báo, **không phải audit này tự đọc remote**. Cuối audit thấy logs/lessons.md, logs/rule-checklist.md sửa chưa commit và media untracked; không do audit sửa, không báo toàn repo sạch.
Metrics, comment và ngày snapshot giữ nguyên theo bản lưu; tải ASR hôm 07/11 không nâng ngày snapshot tương tác. Không xác nhận tính hiện thời của link bài X/báo vì chưa refresh các stream đó.

## Khoảng trống còn lại / bàn giao
1. Đối chiếu ASR với audio @gonaox trước khi dùng trích dẫn chính xác trên màn hình.
2. Chưa có comment clip @gonaox; chỉ có tổng đếm 685 tại snapshot, không được dựng comment.
3. Chưa có tăng trưởng theo thời gian, nguồn độc lập hay phản hồi nhu cầu của người xem để gọi trend đang hot.
4. Nếu dùng 23.14, chỉ nghiên cứu phần tự nhớ + kiểm bản gốc; cần Deep Research kiểm claim, Rule Reviewer kiểm fit. Không chấp nhận nguyên công thức hay hứa hẹn của clip.
5. Gói chuyên biệt cũ cần đánh giá lại độ mới; #texthip chỉ là ứng viên có điều kiện, không phải bridge được duyệt.

File này nằm ngoài repo để parent bố trí ghi repo theo cơ chế được phép; chưa commit/push. Không viết script hoặc làm giọng/render.
