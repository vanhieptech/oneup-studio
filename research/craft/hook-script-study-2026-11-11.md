---
title: "Học lại hook và mạch script từ 15 video giáo dục ngắn thật (VI/EN), đối chiếu clip05 r15.3 và r16"
date: 2026-11-11
type: craft-study
tags: [craft, hook, script, retention, clip05, r15.3, r16, L-101, treg, tiktok]
status: draft
source: "Treg (ScrapeCreators) 25 call, $0.047, lấy 11/11/2026 09:45–09:48 Asia/Saigon: 6 tìm kiếm TikTok + 19 chi tiết video kèm transcript WEBVTT do nhà cung cấp trả; ảnh bìa tải từ URL trong metadata. Đối chiếu: r15.3 S01–S03 (clip05-r15.3-full-draft-2026-11-08.md), r16 C1–C3 (clip05-r16-hook-concepts-2026-11-10.md, sha dbbdcd91…). Chỉ để tham chiếu: research/trends/patterns.md và digest 2026-11-11 @8b227f9."
---
# Học lại hook và mạch script từ video thật (11/11/2026)

**Lý do làm:** Hiệp bác hook r15.3 («Hook xàm», 10/11 18:40) rồi bác cả ba concept r16 (11/11 9:43), qua lời Rule Reviewer chuyển. Theo yêu cầu, OpenCreator ngừng mọi bản nháp clip-05 để học lại cách viết hook và mạch script từ video thật. **File này không có concept clip05 mới.**

**Trạng thái:** bản nghiên cứu của OpenCreator, chờ Rule Reviewer kiểm. Chưa phải luật và chưa sửa skill. Phần đề xuất sửa skill nằm ở mục 7.

---

## 0. Cách lấy dữ liệu và giới hạn (đọc trước)

- **Nguồn:** Treg MCP, nhà cung cấp ScrapeCreators. `scrapecreators.tiktok.search.videos` ($0.00188/call) được gọi với `date_posted=last-3-months`, `sort_by=most-liked`, `trim=true`. Region VN cho truy vấn tiếng Việt và US cho truy vấn tiếng Anh. `scrapecreators.tiktok.video.detail` ($0.00188/call) được gọi với `get_transcript=true`. Mình đã đọc giá và schema bằng `catalog_get` trước khi gọi.
- **Chi phí:** 25 call. Balance $0.90972 → $0.86272, tức **$0.047**, khớp 25 × $0.00188. Sổ call ở mục 9.
- **Thời điểm lấy:** 11/11/2026, khoảng 09:45–09:48 (Asia/Saigon). Lượt xem, like, share và save là **số tại thời điểm lấy**, đúng như Treg trả. Lượt xem trọn đời không chứng minh video đang lên hay «hot». File này không gắn nhãn hot hay trend cho video nào.
- **Cách chọn:** truy vấn sắp theo like, nhưng nhà cung cấp ghi rõ `sort_by` và `date_posted` «not reliably enforced». Đây chỉ là các ứng viên lấy từ tìm kiếm, không phải bảng xếp hạng và không phải mẫu đại diện. `region` chỉ đặt vị trí proxy. Mình chọn tay những video nói thành lời, chủ đề gần kênh (học/nhớ, đọc, tiền, ngủ, thói quen, năng suất) và dài từ 34 giây trở lên. Video quảng cáo hoặc có claim vô căn cứ bị để riêng ở mục 2.3.
- **Transcript:** cả 19 video đều có WEBVTT do nhà cung cấp trả (nhận dạng giọng tự động). Các trích dẫn bên dưới **giữ nguyên văn**, kể cả lỗi nhận dạng và kiểu viết hoa lạ («BA», «Cho», «SAO», «AI» = «ai»). Mốc giây lấy theo cue VTT, không phải đo tay. Transcript của freya.loren bị trống từ 00:03 đến 00:15 (có thể là nhạc), nên phần đó ghi THIẾU.
- **Hình:** mình **CHƯA XEM VIDEO**. Mình chỉ xem **ảnh bìa** (cover HEIC đã đổi sang PNG, gom thành `/workspace/hookstudy/covers-sheet.jpg`). Ảnh bìa không phải khung hình giây 0–3, nên cột «hiện gì» chỉ ghi ảnh bìa, và 3 giây đầu ghi CHƯA XEM HÌNH.
- **Không kiểm fact:** con số và cơ chế mà các video nói (40%/61%, «50% trong 1 giờ», hippocampus…) **chưa được kiểm**. File này chỉ học cách kể, không lấy claim nào làm nguồn cho kênh. Nếu dùng, Deep Research phải kiểm trước.
- **Tỷ lệ xem hết:** Treg không trả retention hay completion. Phần «giữ người xem tới cuối» bên dưới là **phân tích cấu trúc lời**, không phải dữ liệu xem hết.
- Raw JSON (đã che cookie/token nếu có), VTT và ảnh bìa nằm ở `/workspace/hookstudy/` trên box. Thư mục này **ngoài repo, chưa commit**.

---

## 1. Danh sách video (15 phân tích: 8 VI, 7 EN)

| # | Ngôn ngữ | Link | Xem | Like | Share | Save | Đăng (UTC+7) | Dài | Chủ đề |
|---|---|---|---|---|---|---|---|---|---|
| V01 | VI | https://www.tiktok.com/@ai.cbap/video/7701123645476703508 | 263,807 | 36,335 | 7,644 | 7,850 | 2026-10-27 | 71s | đọc lại vs tự nhớ |
| V02 | VI | https://www.tiktok.com/@finroom2010/video/7703452025895324949 | 216,096 | 25,781 | 3,588 | 9,365 | 2026-11-02 | 135s | đọc đi đọc lại vs tự viết (có thí nghiệm) |
| V03 | VI | https://www.tiktok.com/@gonaox/video/7702426588662598920 | 1,559,935 | 174,941 | 26,481 | 70,781 | 2026-10-30 | 169s | ghi nhớ, công thức 3-2-1 |
| V04 | VI | https://www.tiktok.com/@davoslingo/video/7686472761044192520 | 307,570 | 38,080 | 4,495 | 9,230 | 2026-09-17 | 64s | đường cong quên, ôn giãn cách |
| V05 | VI | https://www.tiktok.com/@parentlab3/video/7684183085755190548 | 492,836 | 48,395 | 8,573 | 20,947 | 2026-09-11 | 50s | quy tắc 3 lần nhớ |
| V06 | VI | https://www.tiktok.com/@tiendauroiofficial/video/7701530214861376789 | 524,563 | 26,683 | 9,837 | 5,014 | 2026-10-28 | 290s | khoản chi dưới 200 nghìn |
| V07 | VI | https://www.tiktok.com/@kienthuctaichinh.svg/video/7690815396881911092 | 1,689,653 | 75,652 | 15,224 | 3,236 | 2026-09-29 | 73s | trả cho mình trước 5 triệu/tháng |
| V08 | VI | https://www.tiktok.com/@minheetv146/video/7704566318715997460 | 822,051 | 76,811 | 89,971 | 5,407 | 2026-11-05 | 34s | truyện hài «ngủ gối sách» (hư cấu, chỉ học khung) |
| V09 | EN | https://www.tiktok.com/@freya.loren/video/7697624662632697121 | 130,408 | 24,628 | 674 | 8,233 | 2026-10-17 | 51s | spaced retrieval |
| V10 | EN | https://www.tiktok.com/@phoebespublicdiary/video/7681904564890553631 | 525,428 | 71,864 | 2,249 | 32,434 | 2026-09-05 | 79s | blurt + tô màu chỗ thiếu |
| V11 | EN | https://www.tiktok.com/@mindshiftdaily022/video/7694037081273781518 | 1,124,677 | 114,849 | 7,384 | 40,826 | 2026-10-08 | 357s | ngủ: 3 lời khuyên |
| V12 | EN | https://www.tiktok.com/@ceo.of.napping/video/7685508973918768414 | 579,830 | 63,964 | 1,861 | 19,133 | 2026-09-15 | 414s | khó dậy buổi sáng |
| V13 | EN | https://www.tiktok.com/@readerscut/video/7701904380995456263 | 30,995 | 5,289 | 93 | 1,102 | 2026-10-29 | 183s | từ lướt điện thoại sang đọc sách |
| V14 | EN | https://www.tiktok.com/@nedwagner/video/7682056141680938254 | 576,123 | 56,533 | 12,149 | 32,088 | 2026-09-05 | 134s | 10 thói quen kỷ luật |
| V15 | EN | https://www.tiktok.com/@winwithkt/video/7703414386395712798 | 181,226 | 29,998 | 2,820 | 11,634 | 2026-11-02 | 133s | 6 việc quan trọng nhất (phản ví dụ: không có hook) |

Ghi chú: V08 là truyện hư cấu, claim sai sự thật, nên chỉ học khung mở và không học nội dung. V13 có lượt xem thấp (31k), được giữ làm đối chứng EN có hook dạng hành trình. V15 không có hook, được giữ làm phản ví dụ.

---

## 2. Phân tích từng video

Cột «3 giây đầu nói gì» là nguyên văn cue VTT trong khoảng 00:00 đến khoảng 00:03. «Hiện gì»: CHƯA XEM HÌNH 0–3 s, chỉ ghi chữ hoặc hình trên ảnh bìa.

### 2.1 Tiếng Việt

**V01 · @ai.cbap (264k xem)**
- **3 giây đầu:** «bạn đã đọc bài năm lần nhưng vẫn không nhớ nổi một nửa» [00:00–00:03]. Ảnh bìa có chữ «BẠN ĐÃ ĐỌC BÀI NĂM LẦN».
- **Nỗi đau:** nằm ngay câu đầu, gồm công sức (năm lần) và kết quả tệ (không nhớ nổi một nửa) trong một câu. Khoảnh khắc bị lộ: «bạn tin rằng mình đã thuộc nhưng khi giáo viên đặt câu hỏi [00:11] đầu óc trống rỗng».
- **Trả lời:** ở 00:13, «tại SAO bởi bạn đã luyện nhận Ra đáp án [00:15] chứ chưa luyện tự nhớ lại nó». Câu hỏi «tại sao» được trả lời sau 13 giây, bằng một câu đối lập.
- **Giữ người xem:** một ẩn dụ 12 giây («trí nhớ là một khu rừng… đứng trước tấm bản đồ… nhìn thấy ngôi nhà ấy hàng trăm lần [00:26] nhưng điều đó không có nghĩa bạn biết đường đến đó»), rồi 3 thao tác, rồi một việc làm hôm nay: «hãy thử dành 10 phút cuối buổi học để tự kiểm tra».

**V02 · @finroom2010 (216k xem). Cùng họ chủ đề với clip05, nên đọc kỹ nhất**
- **3 giây đầu:** «bạn không học chậm [00:01] bạn đang học bằng cách AI cũng dùng mà kém hiệu quả [00:04] đọc đi đọc lại». Ảnh bìa có chữ «HỌC NHANH GẤP ĐÔI» và «Gập sách lại, NÓI TO điều bạn nhớ».
- **Nỗi đau:** câu 1 gỡ lỗi cho người xem, câu 2 gọi tên thủ phạm là phương pháp. Từ 00:06 có ba cảnh đời thường, mỗi cảnh một dòng: «tối qua bạn ngồi với cuốn sách tô vàng gần kín cả trang», «sáng nay trước buổi họp bạn mở ghi chú Ra đọc lại thêm một lần nữa», «khóa học online mua từ đầu năm bạn đã xem lại bài một đến lần thứ BA». Điểm đau ở 00:22: «vậy mà BA hôm sau có người hỏi lại đầu bạn trống trơn».
- **Trả lời:** 00:26 «không phải vì bạn kém mà vì cảm giác quen mặt chữ đang đánh lừa bạn». 00:30 hứa «có một thí nghiệm Cho thấy đọc ít lần hơn lại nhớ lâu hơn và cách làm đơn giản đến bất ngờ». Bằng chứng ở 00:36–01:03 kể như chuyện hai nhóm: «nhóm đọc 14 lần nhớ được 40% nhóm chỉ đọc BA lần mà tự viết Ra nhớ được 61% [01:00] trớ trêu nhất là nhóm đọc nhiều lại tự tin hơn dù nhớ kém hơn». *(Số liệu chưa kiểm. Nghe giống Roediger & Karpicke 2006 thí nghiệm 2, mà lock hiện tại của kênh để Exp2 ngoài phạm vi. Không được dùng nếu Deep chưa kiểm.)*
- **Giữ người xem:** câu chốt cơ chế ngắn («não không nhớ thứ nó được nhìn lại [01:07] não nhớ thứ nó phải tự lôi Ra»), 3 bước, rồi mở rộng sang đời sống («học tiếng anh học Excel hay học một nghề mới») và hệ quả tiền (tăng lương). Có **callback** về hình mở đầu: «quay lại trang sách tô vàng kín mít lúc đầu [01:49] màu vàng làm bạn thấy mình đang học [01:51] còn trang giấy trắng bạn tự viết Ra [01:53] mới là thứ ở lại trong đầu». Kết bằng bài thử ngay trong video: «tắt màn hình nói to BA điều bạn vừa nhớ… ghi con số dưới bình luận».

**V03 · @gonaox (1,56M xem)**
- **3 giây đầu:** «ghi nhớ bất cứ thứ gì nhanh đến mức khó tin [00:02] các bạn học BA tiếng bạn của các bạn học 40 phút». Ảnh bìa có chữ «GHI NHỚ BẤT CỨ THỨ GÌ NHANH ĐẾN MỨC KHÓ TIN» cùng hình vẽ người và não.
- **Nỗi đau/bất ngờ:** so sánh với người bên cạnh ở 00:02–00:07: «hôm sau nó nhớ hết các bạn nhớ gần như không gì». Lật nguyên nhân ở 00:07: «đây không phải là khoảng cách về tài năng mà là khoảng cách về kỹ thuật».
- **Trả lời:** hứa ở 00:10 «kỹ thuật này chỉ mất năm phút để học BA bước». Hai vòng mở: «bước đầu tiên nghe như phí thời gian / bước cuối cùng chính là lý do các bạn quên hết mọi thứ». Câu trả lời trải dài 3 bước (00:26–02:47).
- **Giữ người xem:** mỗi bước có tên dễ nhớ («giảng Cho bức tường», «viết như không có AI nhìn»). Mỗi bước kết bằng điểm yếu dẫn sang bước sau («nhưng nói có một điểm yếu… đó là lý do các bạn cần bước BA»). Có ẩn dụ học lời bài hát. Có hỏi bình luận sớm ở 00:17, kiểu chen giữa mà kênh không nên chép.

**V04 · @davoslingo (308k xem)**
- **3 giây đầu:** «có bao giờ bạn học một cái gì đó xong [00:01] đụng một cái mấy ngày hôm sau bạn quên hết sạch luôn hông». Ảnh bìa có chữ «LÝ DO BẠN HAY QUÊN (VÀ CÁCH NHỚ LÂU)», người nói nhìn thẳng camera.
- **Nỗi đau:** câu hỏi nỗi đau mà người xem tự trả lời «có» trong đầu, ở 00:00–00:03. Gỡ lỗi ngay ở 00:03: «não của bạn không có vấn đề gì đâu chỉ là nó được thiết kế để làm như vậy thôi».
- **Trả lời:** hứa ở 00:08 «bạn xem hết video này để biết cách khắc phục nha». Nguyên nhân bằng Ebbinghaus (số chưa kiểm). Cách làm ở 00:43–01:01.
- **Giữ người xem:** 3 bước có mốc ngày. Ngôn ngữ nói rất đời («đánh đá Ra khỏi chuồng gà»). Không có callback và không có CTA thử ngay.

**V05 · @parentlab3 (493k xem)**
- **3 giây đầu:** «học mãi không vào thử quy tắc BA lần nhớ này». Ảnh bìa có chữ «HỌC MÃI KHÔNG VÀO? THỬ QUY TẮC "3 LẦN NHỚ" NÀY!».
- **Nỗi đau:** gói trong 4 chữ «học mãi không vào», nằm cùng câu với lời hứa. Câu 2 nói rõ hơn: «có những kiến thức tưởng rằng đã học rất kỹ [00:04] nhưng chỉ vài ngày sau lại quên». Câu 3 gỡ lỗi cho người xem: «không hẳn vì khả năng ghi nhớ kém mà có thể vì cách học chưa tạo đủ cơ hội để não bộ ghi nhớ».
- **Trả lời:** từ 00:11, mỗi lần một nhiệm vụ («học để hiểu / để nhớ / để vận dụng»).
- **Giữ người xem:** danh sách 3 mục ngắn, kết bằng câu đảo «mục tiêu cuối cùng của việc học không phải là đã học bao nhiêu mà là có thể sử dụng được bao nhiêu».

**V06 · @tiendauroiofficial (525k xem, 290s)**
- **3 giây đầu:** «những khoản làm cạn túi một gia đình [00:02] thường không phải chiếc xe hay cái túi hàng hiệu». Ảnh bìa: hình vẽ người đứng cạnh xe máy, phụ đề «anh chạy xe máy cũ không mua đồ hiệu».
- **Nỗi đau/bất ngờ:** lật kỳ vọng ở 00:00–00:10: «đó là những khoản dưới 200.000 lặp lại nhiều tới mức không AI còn để ý».
- **Trả lời:** kể chuyện hai người «anh vàng với anh xanh cùng 32 tuổi… cùng thu nhập». Người «tự nhận là người sống tiết kiệm» mở sao kê ở 00:41. Mỗi khoản có số cụ thể, cộng dồn ở 01:57: «cộng hết 3.000.000 chín một tháng [01:59] một năm gần 47.000.000 gấp BA lần cái máy giặt nhà anh xanh». Cách làm là ba luật của anh xanh (02:34–03:16).
- **Giữ người xem:** câu hỏi treo «còn nhà anh xanh thì SAO». Lật thêm lần hai: «nghe tới đây tưởng cứ mua đồ xịn đồ bền là khôn chỗ này cũng có cái bẫy». CTA thử ngay: «anh chị thử mở SAO kê tháng rồi cộng tất cả những khoảng dưới 200.000». Có câu an toàn «nội dung trên kênh chỉ mang tính chất tham khảo».

**V07 · @kienthuctaichinh.svg (1,69M xem)**
- **3 giây đầu:** «mỗi tháng cất đúng 5.000.000 [00:01] sau năm năm nhìn lại tài khoản giật mình cỡ nào». Ảnh bìa có chữ «MỖI THÁNG CẤT ĐÚNG 5 TRIỆU: SAU 5 NĂM NHÌN LẠI TÀI KHOẢN GIẬT MÌNH CỠ NÀO?», ảnh tay đếm tiền.
- **Bất ngờ:** con số đi kèm **hệ quả** người xem tò mò («giật mình cỡ nào»), không phải số trơn.
- **Trả lời:** 00:11 là thao tác («thay vì đợi cuối tháng còn thừa bao nhiêu mới cất… gửi ngay 5.000.000đ… ngay khi vừa nhận lương»). 00:21 trả kết quả («sau khoảng 20 tháng… 100.000.000đ… năm năm… 300.000.000đ»).
- **Giữ người xem:** thêm chuyên gia đặt tên nguyên tắc («trả Cho bản thân trước»), rồi câu đảo «đừng đợi có nhiều tiền mới tiết kiệm mà hãy tiết kiệm để có nhiều tiền». CTA gắn đúng thời điểm: «tháng này nhận lương bạn đã sẵn sàng bấm chuyển khoản trả Cho mình trước chưa».

**V08 · @minheetv146 (822k xem, 90k share). Hư cấu, chỉ học khung**
- **3 giây đầu:** «đêm trước kỳ thi học kỳ cả lớp bạn thức tới 2 giờ sáng [00:03] còn bạn đi ngủ lúc 8 giờ tối». Ảnh bìa có chữ «NGỦ GỐI LÊN SÁCH LÀ THUỘC BÀI?».
- **Bất ngờ:** đặt «cả lớp» cạnh «bạn» ngay câu đầu, với «bạn» là nhân vật chính. Không có dàn dựng.
- **Trả lời/giữ người xem:** chuỗi leo thang trong 30 giây, kết bằng twist phi lý. Nội dung sai sự thật nên kênh **không được** dùng. Chỉ học một điều: đối lập «mọi người vs bạn» đặt trong câu đầu.

### 2.2 Tiếng Anh

**V09 · @freya.loren (130k xem)**
- **3 giây đầu:** «You're studying for [00:01] it all. [00:01] You're not bad at studying [00:03] you just don't know how.» Từ 00:03 đến 00:15 transcript THIẾU. Ảnh bìa: người nói cầm sticker «Study Smarter, Not Harder».
- **Nỗi đau:** gỡ lỗi cho người xem rồi đổ cho phương pháp ngay trong 3 giây.
- **Trả lời:** 00:16 nêu nguyên nhân («The longer we go without revisiting information the easier it is to forget»). 00:21 hứa («Here's how to beat it»). 00:25–00:43 là thao tác có lịch («Got it wrong… retry tomorrow… struggled… 3 days… confidently… 7 days»).
- **Giữ người xem:** quy tắc rẽ nhánh theo màu, mỗi nhánh một câu.

**V10 · @phoebespublicdiary (525k xem)**
- **3 giây đầu:** «So I'm gonna give you my best study tip [00:02] that will literally give you the best grades.» Ảnh bìa có chữ «THE BEST STUDY METHOD».
- **Nỗi đau:** không nêu. Hook dựa vào lời hứa và uy tín cá nhân («My bio professor actually mentioned this»).
- **Trả lời:** thao tác ở 00:27–01:05. Lời giải thích nằm ở cuối: «you're not just blindly reading notes, you're actually actively recalling».
- **Giữ người xem:** chủ yếu nhờ giọng thân mật của creator. Đây là kiểu kênh **chưa có**, vì kênh chưa có gương mặt hay uy tín cá nhân.

**V11 · @mindshiftdaily022 (1,12M xem, 357s)**
- **3 giây đầu:** «so if you've done any amount of research on sleep [00:02] you've probably encountered the same three pieces of advice». Ảnh bìa có chữ «It Sucks for 3 Days, But it's Enough», hình vẽ phòng ngủ.
- **Bất ngờ:** nhắc lại lời khuyên quen thuộc (00:05–00:10) rồi đập: «all of these are technically correct but they're also kind of useless». Có ví von «just go to the gym bro».
- **Trả lời:** cảnh đời thường ở 00:40 («you're watching a movie and all of a sudden… brain quietly checks out… lying in bed at three in the morning actively wanting to sleep»). Đổi câu hỏi ở 01:29: «the question you really are looking for is not how to fall asleep but instead how do I calm my rash». Hứa ở 01:35: «three solid advice… stay until the end».
- **Giữ người xem:** mỗi lời khuyên mở bằng một tiêu đề gây tò mò («2:00am Motivation is the sign you screwed up», «stare at a wall during a lunch») và một cảnh «picture this». *(Nhiều cơ chế như «orsin» hay «RAS» chưa kiểm và có thể sai. Chỉ học cấu trúc.)*

**V12 · @ceo.of.napping (580k xem, 414s)**
- **3 giây đầu:** «If it's so hard for you to get out of bed in the morning, [00:02] please watch this.» Ảnh bìa có chữ «HOW TO GET OUT OF BED IN THE MORNING».
- **Nỗi đau:** gọi thẳng người đang gặp vấn đề ngay câu đầu. Creator tự nhận cùng nỗi đau («I have such bad sleep inertia»).
- **Trả lời:** hứa ở 00:24 («from alarm going off to out of bed in, like, 20 minutes»). Thao tác bắt đầu từ 00:39 bằng «picture this. Your alarm goes off in the morning, you reach over and you snooze it.»
- **Giữ người xem:** chuỗi việc theo đúng thứ tự thời gian của buổi sáng. Kết bằng điểm yếu thật («the hardest part is actually remembering to do them in the morning») và một giải pháp nhỏ (danh sách dán lên điện thoại).

**V13 · @readerscut (31k xem)**
- **3 giây đầu:** «This is how I went from doomscrolling to reading for hours.» Ảnh bìa có phụ đề «here are five steps I used to rebuild my attention span».
- **Nỗi đau:** trước và sau ngay câu đầu. Kể chi tiết ở 00:07: «I used to pick up my phone every five minutes when I was reading.» Gỡ lỗi cho người xem: «There is absolutely no shaming in here.»
- **Trả lời/giữ người xem:** 5 bước, có ẩn dụ phòng gym, có câu lật niềm tin «I used to think that I had no attention span, but I actually had just unlimited access to the most distracting thing ever.» Lượt xem thấp nên **không** dùng làm bằng chứng là cách này hiệu quả.

**V14 · @nedwagner (576k xem)**
- **3 giây đầu:** «Here are 10 out of 10 habits to build extreme discipline. [00:03] But they get progressively harder.» Ảnh bìa có chữ «10/10 habits to build extreme discipline (but they get progressively harder)».
- **Bất ngờ:** không có nỗi đau. Hook là lời hứa cộng thêm một **luật leo thang** khiến người xem muốn xem mục cuối.
- **Giữ người xem:** danh sách có độ khó tăng dần, mục cuối được báo trước là «the most important of all». *(Claim như «If you can't make your bed… no chance at winning in life» là kiểu tuyệt đối mà kênh tránh.)*

**V15 · @winwithkt (181k xem). Phản ví dụ**
- **3 giây đầu:** «as I want you to grab a pad of paper» (00:00–00:05). Ảnh bìa có chữ «How to be more productive and get things done», một người lớn tuổi mặc vest nói trên podcast.
- **Nỗi đau:** không có. Video đi thẳng vào thao tác, lượt xem có lẽ dựa vào uy tín người nói (suy luận, chưa kiểm). Không rút được bài học hook từ video này. Nó chỉ nhắc rằng lượt xem cao không chứng minh hook tốt.

### 2.3 Đã lấy nhưng loại khỏi phân tích (vẫn tính trong chi phí)

| Link | Xem | Lý do loại |
|---|---|---|
| https://www.tiktok.com/@nikki.study/video/7693200468280921362 | 1,826,421 | quảng cáo app. Hook «cách học giỏi đến mức mà giáo viên cũng nghĩ là bạn gian lận» là lời hứa phóng đại |
| https://www.tiktok.com/@cuukechuyen.ne/video/7697528024480140545 | 405,948 | mẹo tâm linh (kim chỉ trong ví), không có căn cứ |
| https://www.tiktok.com/@christynasnotes/video/7675863586631109902 | 2,223,071 | hook đùa («always choose the correct answer») rồi quảng cáo app |
| https://www.tiktok.com/@improvewithkate/video/7682831804662959392 | 647,457 | «listen… once and it will stay in your brain forever», cơ chế não chưa kiểm, cuối là quảng cáo |

Quan sát phụ: bốn video có lượt xem rất cao này đều hứa phóng đại hoặc là quảng cáo. Kênh có luật nguồn nên **không chép kiểu hứa này**. Lượt xem của chúng không phải mục tiêu để so.

---

## 3. Bảy nguyên tắc hook và mạch script (rút từ 15 video)

### NT1. Câu đầu tiên là nỗi đau người xem tự nhận ra, với chủ ngữ «bạn», nói trọn trong khoảng 3 giây, không dàn dựng trước
Công sức và kết quả tệ nằm **trong cùng một câu ngắn**. Người xem không phải chờ vế sau mới hiểu chuyện gì hỏng.
- V01: «bạn đã đọc bài năm lần nhưng vẫn không nhớ nổi một nửa» (00:00–00:03)
- V04: «có bao giờ bạn học một cái gì đó xong đụng một cái mấy ngày hôm sau bạn quên hết sạch luôn hông» (00:00–00:03)
- V05: «học mãi không vào thử quy tắc BA lần nhớ này» (00:00–00:02)
- V12: «If it's so hard for you to get out of bed in the morning, please watch this.» (00:00–00:02)

### NT2. Chọn nỗi đau phổ biến và có cái giá thật, rồi đặt nó vào khoảnh khắc bị lộ
Video tốt chọn chuyện **nhiều người gặp** (quên sau vài ngày, tiền mất không biết vì sao, không dậy nổi), và cho thấy lúc cái giá hiện ra: bị hỏi mà trống rỗng, mở sao kê, nằm 3 giờ sáng không ngủ.
- V02: «vậy mà BA hôm sau có người hỏi lại đầu bạn trống trơn» (00:22)
- V01: «bạn tin rằng mình đã thuộc nhưng khi giáo viên đặt câu hỏi [00:11] đầu óc trống rỗng»
- V06: «cuối năm anh vàng ngồi mở SAO kê ngân hàng Ra coi [00:45] không có khoản nào lớn nhưng có rất nhiều khoản nhỏ»
- V11: «lying in bed at three in the morning actively wanting to sleep» (00:48)

### NT3. Ngay sau nỗi đau, gỡ lỗi cho người xem và lật một niềm tin: thủ phạm là cách làm, không phải con người
Câu thứ hai hoặc thứ ba là một **khẳng định rõ ràng, hơi bất ngờ**, không phải «chưa chắc».
- V02: «bạn không học chậm [00:01] bạn đang học bằng cách AI cũng dùng mà kém hiệu quả [00:04] đọc đi đọc lại»
- V03: «đây không phải là khoảng cách về tài năng [00:09] mà là khoảng cách về kỹ thuật»
- V04: «não của bạn không có vấn đề gì đâu chỉ là nó được thiết kế để làm như vậy thôi»
- V09: «You're not bad at studying you just don't know how.»
- V11: «all of these are technically correct but they're also kind of useless»

### NT4. Trong khoảng 10 giây đầu, hứa một kết quả cụ thể và mở một vòng tò mò
Người xem được biết họ sẽ nhận **kết quả gì** (nhớ lâu hơn, ra khỏi giường trong 20 phút), mất bao nhiêu bước hay bao lâu, và có một chi tiết treo để chờ.
- V03: «kỹ thuật này chỉ mất năm phút để học BA bước [00:12] bước đầu tiên nghe như phí thời gian [00:14] bước cuối cùng chính là lý do các bạn quên hết mọi thứ»
- V02: «có một thí nghiệm Cho thấy đọc ít lần hơn lại nhớ lâu hơn [00:34] và cách làm đơn giản đến bất ngờ»
- V14: «Here are 10 out of 10 habits to build extreme discipline. But they get progressively harder.»
- V12: «to help me get from alarm going off to out of bed in, like, 20 minutes»

### NT5. Bằng chứng kể như chuyện hai nhóm hoặc hai người, có chiều kết quả rõ và một hệ quả người xem cảm được. Số chỉ xuất hiện khi người xem đã muốn biết
Số không đứng một mình. Nó luôn là **so sánh** (nhóm A vs nhóm B, anh vàng vs anh xanh) hoặc được đổi sang một thứ nhìn thấy được (gấp ba lần cái máy giặt).
- V02: «nhóm đọc 14 lần nhớ được 40% [00:56] nhóm chỉ đọc BA lần mà tự viết Ra nhớ được 61% [01:00] trớ trêu nhất là nhóm đọc nhiều lại tự tin hơn dù nhớ kém hơn» (bằng chứng tới ở giây 36, sau nỗi đau và lời hứa)
- V06: «cộng hết 3.000.000 chín một tháng [01:59] một năm gần 47.000.000 gấp BA lần cái máy giặt nhà anh xanh»
- V07: «5.000.000 mỗi tháng nghe có vẻ nhỏ [00:21] nhưng sau khoảng 20 tháng [00:22] chị Hương đã tích lũy được 100.000.000đ»

### NT6. Giải thích cơ chế bằng một hình ảnh đời thường trong 1–2 câu
Phải là hình người xem đã từng làm (hát theo bài hát, tập gym, nhìn bản đồ), không phải thuật ngữ. *(Ở kênh, ẩn dụ là minh họa biên tập, có nhãn, và không được nói quá điều nguồn đã chứng minh.)*
- V01: «bạn có thể đứng trước tấm bản đồ [00:24] và nhìn thấy ngôi nhà ấy hàng trăm lần [00:26] nhưng điều đó không có nghĩa bạn biết đường đến đó»
- V03: «các bạn không ngồi đọc đi đọc lại các bạn hát Theo Sai vài từ rồi thử lại [00:51] đến lần thứ BA từ ngữ tự tuôn Ra»
- V13: «I kind of think of it like going to the gym. You don't walk in one day and Just lift your heaviest weight.»

### NT7. Giữ người xem bằng các bước có tên, mỗi bước để lộ một chỗ hở dẫn sang bước sau. Cuối video quay về hình mở đầu và cho một việc thử ngay
- V03: «nhưng nói có một điểm yếu [02:13] nói nhanh… [02:19] đó là lý do các bạn cần bước BA»
- V02, callback: «quay lại trang sách tô vàng kín mít lúc đầu… còn trang giấy trắng bạn tự viết Ra mới là thứ ở lại trong đầu»
- V02, thử ngay: «tắt màn hình nói to BA điều bạn vừa nhớ [02:01] bạn nhớ được mấy điều [02:02] ghi con số dưới bình luận»
- V06, thử ngay: «anh chị thử mở SAO kê tháng rồi [02:21] cộng tất cả những khoảng dưới 200.000»
- V06, lật lần hai giữa video: «nghe tới đây tưởng cứ mua đồ xịn đồ bền là khôn [03:25] chỗ này cũng có cái bẫy»

**Quan sát độ dài:** các video VI cùng chủ đề dài 50–290 giây. V02 (135s), V03 (169s) và V06 (290s) giữ mạch dài bằng các bước có vòng mở. Điều này khớp mục tiêu 2–3 phút của Hiệp, với điều kiện mỗi beat thêm một điều mới.

---

## 4. Đối chiếu từng nguyên tắc với r15.3 S01–S03 và r16 C1–C3

Văn bản đối chiếu:
- **r15.3** S01: «Đã đọc lại, sinh viên chỉ nhớ đúng trung bình 54 phần trăm số ý sau hai ngày trong một thí nghiệm.» S02: «Con số ấy đã đủ để chọn đọc lại cho mốc một tuần chưa?» S03: «Chưa, thí nghiệm năm 2006 ấy còn so đọc lại với tự viết từ trí nhớ ở các mốc đo khác nhau.»
- **r16 C1:** «Bạn đọc hết cả cuốn sách, mà mấy hôm sau viết vài dòng giới thiệu cũng phải lật ra coi lại. Vậy lúc vừa gấp sách, bạn nên làm gì để mấy hôm sau tự viết được?», trả lời: «Một việc đáng thử là gấp lại rồi tự viết ra điều còn nhớ, và năm 2006 có một thí nghiệm đã so đúng việc ấy với đọc lại thêm một lượt.»
- **r16 C2:** «Bạn chụp màn hình đoạn hay gửi bạn thân, tưởng vậy là nhớ, mà mấy hôm sau bạn phải mở ảnh ra mới kể lại được. Vậy xem lại tấm ảnh thêm vài lần có giúp bạn tự kể được không?», trả lời: «Chưa chắc, vì xem lại cũng là một kiểu đọc lại…»
- **r16 C3:** «Tối nào bạn cũng đọc truyện cho con, mà con đòi kể lại chuyện tuần trước thì bạn phải lật sách ra coi. Vậy có phải tại bạn đọc cho con chưa đủ kỹ không?», trả lời: «Chưa chắc là tại bạn đọc chưa kỹ. Năm 2006, một thí nghiệm đã so hai việc…»

| NT | r15.3 S01–S03 | r16 C1 / C2 / C3 |
|---|---|---|
| **NT1** nỗi đau của «bạn» trong 3 giây | **Hỏng.** Chủ ngữ là «sinh viên… trong một thí nghiệm», không phải người xem. Câu đầu là báo cáo 22 chữ với 4 lớp rào («trung bình», «số ý», «sau hai ngày», «trong một thí nghiệm»). Người lướt không thấy chuyện của mình. | **Hỏng ở thời điểm.** Cả ba mở bằng vế công sức hoặc dàn cảnh, và vế đau chỉ tới ở giây 5–8 (chính file r16 tự ước). So với V01: «bạn đã đọc bài năm lần nhưng vẫn không nhớ nổi một nửa» chứa trọn công sức và thất bại trong 3 giây. |
| **NT2** nỗi đau phổ biến, có giá thật | **Hỏng.** Không có nỗi đau, chỉ có một tỷ lệ. | **Hỏng nặng nhất ở đây.** Ba tình huống được chọn để *khác các bản bị bác* (L-088/L-095), không phải vì người xem hay gặp. Viết giới thiệu sách (C1) là việc ít người làm. Mở ảnh (C2) và lật sách (C3) chỉ tốn vài giây, nên không có cái giá nào đáng sợ. Con đòi kể chuyện tuần trước (C3) là cảnh hẹp và hơi lạ. Video thật chọn «hỏi lại thì trống trơn», «mở sao kê», «3 giờ sáng chưa ngủ». |
| **NT3** gỡ lỗi + lật niềm tin bằng khẳng định | **Hỏng.** S02 hỏi một câu người xem không bao giờ tự hỏi («đủ để chọn đọc lại cho mốc một tuần chưa»), tức câu về tham số kỹ thuật (L-101). S03 «Chưa» chỉ dẫn tới một thiết kế nghiên cứu, không lật niềm tin nào. | **Hỏng.** C2 và C3 trả lời bằng «Chưa chắc», C1 bằng «Một việc đáng thử». Đây là lời rào, không phải khẳng định, nên không có gì bất ngờ để người xem ở lại. C3 có ý gỡ lỗi («có phải tại bạn…»), nhưng đặt trên một tình huống hẹp, và câu trả lời không đổ rõ cho phương pháp như V02 («không phải vì bạn kém mà vì cảm giác quen mặt chữ đang đánh lừa bạn»). |
| **NT4** hứa kết quả cụ thể + vòng tò mò | **Hỏng.** Lời hứa (S04 giữ nguyên) là «phép so cụ thể và một câu hỏi dùng ngay»: hứa một *phép so*, trong khi người xem muốn *nhớ được*. Không có vòng tò mò. | **Hỏng.** Cả ba câu trả lời đều hứa «năm 2006 có một thí nghiệm so…», tức lại hứa một thiết kế nghiên cứu, không hứa kết quả. 15 giây đầu không có thông tin mới nào. So với V02: «đọc ít lần hơn lại nhớ lâu hơn và cách làm đơn giản đến bất ngờ». |
| **NT5** số = so sánh + hệ quả, đến sau khi người xem muốn biết | **Hỏng.** Con số 54% đến **trước** mọi lý do để quan tâm. Nó không được so với gì trong câu, nên người nghe không biết 54% là tốt hay xấu (thậm chí nghe khá ổn cho phía đọc lại). Đây là đúng «số không có hệ quả». | Không mở bằng số (đúng hướng). Nhưng phần bằng chứng vẫn để tận S10–S11, sau một chuỗi thiết kế (S06–S09), nên người xem nghe thiết kế trước khi biết kết quả đáng chờ. |
| **NT6** ẩn dụ đời thường | Không có. | Không có. Cả ba dùng cảnh minh họa nhưng không giải thích *vì sao* đọc lại tạo cảm giác đã nhớ. |
| **NT7** bước có tên, lộ chỗ hở, callback, thử ngay | Thân bài S04–S21 có CTA và câu hỏi dùng ngay, nhưng không có bước nào để lộ chỗ hở dẫn sang bước sau. Callback về hình mở không làm được, vì phần mở không có hình. | Không áp dụng (chỉ là concept phần mở). Rủi ro: hook đổi sang sách, ảnh hay truyện thì thân bài nói «bài», nên callback bị lệch quy chiếu (file r16 đã tự ghi). |

### Tóm lại, vì sao hỏng (nói thẳng)
1. **r15.3 mở bằng báo cáo về người khác.** «Sinh viên… 54%… trong một thí nghiệm» là câu của bài báo khoa học, không phải câu người ta nói với nhau. Câu hỏi tiếp theo lại hỏi về tham số của phương pháp. Người xem không có lý do dừng.
2. **r16 sửa sai chỗ.** Mình bỏ con số nhưng giữ cách nghĩ cũ. Mình chọn tình huống để *né các bản bị bác và đạt bảng fit P/F*, không chọn vì người xem gặp nhiều và thấy đau. Kết quả là ba nỗi đau hiếm, rẻ và tới muộn.
3. **Cả bốn bản đều trả lời bằng rào đón hoặc thiết kế nghiên cứu** («Chưa», «Chưa chắc», «Một việc đáng thử», «năm 2006 có một thí nghiệm so…»). Video thật trả lời bằng một khẳng định bất ngờ có phạm vi rõ, rồi mới đưa nghiên cứu.
4. **Câu quá dài** (26–33 chữ ở r16, 22 chữ ở r15.3 S01) vì nhồi điều kiện cho đúng nguồn. Các cue mở đầu trong video thật chỉ là mệnh đề 5–12 chữ nối nhau.
5. **Quy trình viết từ checklist ra người xem, thay vì ngược lại.** File r16 dành phần lớn chỗ cho bảng fit, L-088 và kết quả checker. Không chỗ nào hỏi «người lạ nghe câu đầu có gật đầu "đúng tôi" không». Checker và bảng fit đều đạt, nhưng điều đó không nói gì về hook (đúng như L-098 và L-101).

---

## 5. Cách áp dụng cho kênh (không phải concept clip05)

1. **Thử câu đầu trước khi viết tiếp:** một câu, chủ ngữ «bạn», chứa *việc người xem đã làm* và *kết quả tệ*, nói trọn trong khoảng 3 giây (ƯỚC). Hỏi: người lạ nghe một lần có tự nói «đúng là tôi» không? Không thì bỏ, đừng vá chữ.
2. **Chấm nỗi đau theo hai câu hỏi:** (a) trong tháng qua, bao nhiêu người xem đã gặp chuyện này? (b) cái giá là gì (xấu hổ, mất tiền, mất giờ, mất ngủ)? Nỗi đau hiếm hoặc rẻ thì loại, kể cả khi nó «mới».
3. **Câu 2–3 là khẳng định lật niềm tin, đổ cho phương pháp.** Không dùng «chưa chắc» làm câu trả lời hook. Muốn đúng luật nguồn thì thu hẹp phạm vi («trong thí nghiệm này…»), đừng rào cả câu.
4. **Trong 10 giây đầu, hứa kết quả người xem muốn** (nhớ được, kể lại được, giữ được tiền), không hứa «phép so» hay «một thí nghiệm».
5. **Đưa nghiên cứu vào như chuyện hai nhóm**, nói chiều kết quả trước rồi mới tới chi tiết thiết kế cần cho đúng nguồn. Con số luôn có vật so hoặc hệ quả.
6. **Một ẩn dụ đời thường**, có nhãn minh họa, không nói quá cơ chế mà nguồn cho phép (W-16).
7. **Kết bằng callback về hình câu đầu và một việc thử ngay trong video**, đúng luật một CTA của kênh.
8. **Câu nói ngắn:** mỗi mệnh đề khoảng 5–12 chữ và vẫn giữ chủ ngữ (W-09). Các video tiếng Việt thật cho thấy câu ngắn mà đủ chủ ngữ hoàn toàn làm được.

**Chỗ có thể xung đột với luật kênh. Mình không tự quyết, Rule Reviewer hoặc Hiệp quyết:**
- **L-087 (không lấy ví dụ môn học):** phần lớn video VI về học là chuyện đi học. V02 cho thấy cách chuyển sang đời sống: «học tiếng anh học Excel hay học một nghề mới», hệ quả là tăng lương. Kênh cần làm đúng việc chuyển này.
- **L-088 và L-095 (khác các bản trước):** cần làm rõ rằng «khác» là khác *lời và khung kể*, không phải bỏ nỗi đau phổ biến để chọn nỗi đau hiếm. r16 hỏng một phần vì hiểu «khác» theo nghĩa thứ hai.
- **Khoảnh khắc «bị hỏi lại»:** V01 và V02 dùng đúng khoảnh khắc này, và nó chạy tốt. Các bản clip-05 v8–v9 có khung «bị hỏi lại» từng bị bác. Cần Reviewer xác định lúc đó bị bác vì *khung* hay vì *cách viết*, trước khi ai đó né hay dùng lại.
- **Con số 40%/61% trong V02:** nghe giống RK 2006 Exp2, mà lock hiện tại để Exp2 ngoài phạm vi. Muốn dùng phải qua Deep Research. Mình không đề xuất dùng.

---

## 6. Đối chiếu với patterns.md (chỉ tham chiếu)
- NT1/NT2 gần với **P10** (picture-this effort paradox), nhưng các video thật **nén** «công sức + thất bại» vào một câu ≤3 giây, còn template P10 mở bằng «Tưởng tượng:», nên nỗi đau tới chậm. Đề xuất Social Research ghi chú điều này vào P10 nếu thấy hợp. Mình không sửa patterns.md.
- NT3 gần **P03** (ai cũng nói X, sự thật là Y) và **P06** (actually-method).
- NT5 (số kèm so sánh và hệ quả) khác **P04** (number shock): video thật không mở bằng số trơn. V07 mở bằng số nhưng kèm ngay hệ quả («giật mình cỡ nào»). Đây đúng là chỗ r15.3 dùng sai P04.

---

## 7. Đề xuất thêm vào skill `short-video-script-craft` (CHƯA sửa skill, chờ Reviewer/Hiệp)

Đề xuất chèn một mục mới sau «## 2. Structure», viết tiếng Anh cho khớp ngôn ngữ của skill:

```markdown
## 2b. Hook and retention from real videos (study 2026-11-11, research/craft/hook-script-study-2026-11-11.md)
Before scoring any rule, check the opening as a stranger hearing it once:
1. Line 1 = the viewer's own pain, subject "bạn", effort + bad result in ONE short sentence, fully heard within ~3 s (estimated). No setup clause before the pain. A study result, percentage or other people ("sinh viên trong thí nghiệm") is never line 1.
2. Pick a pain that many viewers had this month AND that costs something (embarrassment, money, time, sleep). Show the exposure moment. Reject rare or cheap pains even if they are "fresh"; freshness (L-088/L-095) applies to wording and frame, not to giving up a common pain.
3. Lines 2–3 = a clear, scoped claim that clears the viewer and blames the method ("không phải vì bạn kém, mà vì…"). Never answer the hook with a hedge ("chưa chắc", "một việc đáng thử") or with a study design ("năm 2006 có một thí nghiệm so…").
4. Within ~10 s promise the result the viewer wants (remember, retell, keep money), plus one open loop (number of steps, a surprising step). Never promise "a comparison".
5. Evidence = a two-group/two-person story: direction of result first, a felt consequence, then the design details needed for source accuracy. A number always has a comparator or consequence.
6. At most one everyday metaphor for the mechanism, labelled as editorial illustration, never beyond the source (W-16).
7. Named steps where each exposes the gap the next one fixes; end with a callback to the line-1 image and one try-it-now action (single CTA).
Spoken clauses ~5–12 words, each with its subject. Record for each hook: (a) the pain line and its estimated second, (b) why a stranger says "that's me", (c) whether the hook question is one the viewer would ask themselves (L-101). Checker/pattern-fit passes never substitute for this.
```

Mình cũng đề xuất thêm một dòng vào mục 5 (Critique loop): «Khi chọn 3 concept sau một lần bị bác, trước hết xếp hạng nỗi đau theo độ phổ biến và cái giá, rồi mới làm bảng fit P/F. Không chọn tình huống chỉ vì nó khác các bản bị bác.»

---

## 8. Giới hạn dữ liệu
- Chưa xem video. Chỉ có ảnh bìa và transcript tự động. Nội dung hình ở giây 0–3 của cả 15 video: CHƯA XEM HÌNH.
- Không có dữ liệu retention hay completion. «Giữ người xem» là phân tích cấu trúc lời.
- 15 video là ứng viên lấy từ tìm kiếm (sắp theo like, không đảm bảo), không phải mẫu đại diện hay bảng trend. Lượt xem trọn đời không chứng minh video đang tăng.
- Transcript nhận dạng tự động, có lỗi chữ. Trích nguyên văn, không sửa. Có một đoạn THIẾU (V09, 00:03–00:15).
- Fact và cơ chế trong các video chưa kiểm. Không claim nào được chuyển thành nguồn cho kênh.
- Phần lớn video VI về học là chuyện đi học, nên L-087 đòi chuyển sang đời sống khi áp dụng.
- Chưa có người thật đọc to hay nghe thử bất kỳ đề xuất nào: CHƯA KIỂM.

---

## 9. Sổ call Treg (11/11/2026, Asia/Saigon)

| # | Endpoint | Input | Call id | Cost |
|---|---|---|---|---|
| 1 | scrapecreators.tiktok.search.videos | «cách học nhớ lâu», VN | 1f79492002334098bde01439b138756d | $0.00188 |
| 2 | 〃 | «mẹo tiết kiệm tiền», VN | 9bdadadcc6e644a18e986d86dcc504e0 | $0.00188 |
| 3 | 〃 | «thói quen thay đổi cuộc sống», VN | 9ea34eacb26d4dfda159d428be16f6c7 | $0.00188 |
| 4 | 〃 | «how to remember what you read», US | 1539a0b530ae4883809c34a4ba186244 | $0.00188 |
| 5 | 〃 | «study tips that actually work», US | f0509b8bd79645778c940103440a8d68 | $0.00188 |
| 6 | 〃 | «productivity habits sleep money tips», US | f759dab25ede4ac787c7a515c6d29b38 | $0.00188 |
| 7 | scrapecreators.tiktok.video.detail (get_transcript) | @gonaox 7702426588662598920 | ea64ee58fad44019b99e1a0990fe7511 | $0.00188 |
| 8 | 〃 | @minheetv146 7704566318715997460 | 4435fdb2b4ea4058ad8dc958d649e642 | $0.00188 |
| 9 | 〃 | @davoslingo 7686472761044192520 | f13d885b717b43178fc7e701e5081f31 | $0.00188 |
| 10 | 〃 | @ai.cbap 7701123645476703508 | d178216e29974d03a4ba9081787e1330 | $0.00188 |
| 11 | 〃 | @finroom2010 7703452025895324949 | 737fd000db3743d5b1c8660deef8d027 | $0.00188 |
| 12 | 〃 | @parentlab3 7684183085755190548 | 975dcbe976d44794ae1adc13f7ba2d7b | $0.00188 |
| 13 | 〃 | @tiendauroiofficial 7701530214861376789 | edf18270479448758e39a7cb948273f9 | $0.00188 |
| 14 | 〃 | @kienthuctaichinh.svg 7690815396881911092 | 53e5f748b2634cf59c01c4bc631c0741 | $0.00188 |
| 15 | 〃 | @cuukechuyen.ne 7697528024480140545 | c796369cf3b0429e9b5b8b5f8af6a055 | $0.00188 |
| 16 | 〃 | @nikki.study 7693200468280921362 | 15098c3f4e9e408aa62d3bfe02d31237 | $0.00188 |
| 17 | 〃 | @improvewithkate 7682831804662959392 | 4723649b228a409f820b33ec561b40c9 | $0.00188 |
| 18 | 〃 | @freya.loren 7697624662632697121 | 56bd6829f3c74613a87449401ab52d6f | $0.00188 |
| 19 | 〃 | @ceo.of.napping 7685508973918768414 | b3327c4c3a23415aafc666326d64d85d | $0.00188 |
| 20 | 〃 | @phoebespublicdiary 7681904564890553631 | 73fd9e5f3dcc49db96b2feb022557a9a | $0.00188 |
| 21 | 〃 | @readerscut 7701904380995456263 | 2f27ba03025d4128a96f8ebf385e17b6 | $0.00188 |
| 22 | 〃 | @nedwagner 7682056141680938254 | 0c1d2a545f524264ad977d926fd58a67 | $0.00188 |
| 23 | 〃 | @christynasnotes 7675863586631109902 | 272b245a7dd74eb48a7b4fdd38df93fc | $0.00188 |
| 24 | 〃 | @winwithkt 7703414386395712798 | ed30b2fe694a46588e742aeaed34c430 | $0.00188 |
| 25 | 〃 | @mindshiftdaily022 7694037081273781518 | 7929e46c25c84587a778d3a52eafcaa0 | $0.00188 |

Tổng: 25 call, $0.047. Balance $0.90972 → $0.86272. Không dùng Apify, không gọi comment.
