# Clip05 — supplemental lock RK2006, Experiment 1

Status: **VERIFIED / SOURCE-OWNER SCOPE** (phạm vi nguồn đã xác minh).
Storage status: **ARCHIVE / SYNC PENDING**. Standalone ngoài repo; chưa commit/push. Không sửa hai lock cũ.
Thời điểm lập: 08/11/2026 13:09:55 Asia/Saigon (UTC+7).
Proposed repo path: `research/fact-packages/clip05-rk2006-exp1-supplement-lock-2026-11-08.md`.

## 1. Phạm vi và quyết định rule

Chỉ khóa **Experiment 1** của Roediger & Karpicke (2006), về thao tác học → recall nội dung văn bản sau trì hoãn. **Exp2 và confidence hoàn toàn ngoài scope** bổ sung này: không dùng số, bảng, câu kết luận hay dữ liệu tự tin từ Exp2. Không khóa kịch bản, không viết lời thay người viết.

Đã đọc `/workspace/clip05-w16-operational-cause-decision-2026-11-08.md`: Reviewer kết luận W-16 hợp lệ **có điều kiện** ở cấp nguyên nhân thao tác/kết quả; đòi source-owner lock và archive/sync trước khi coi gate nguồn đầy đủ. Báo cáo Reviewer là quyết định chuyên môn của agent, **không phải user approval, craft PASS hay Chốt**. Bản Reviewer tự ghi khoảng 13:15 giờ VN, muộn hơn timestamp yêu cầu 13:09; không dùng nhãn giờ ấy làm bằng chứng chronology hay approval. Không kiểm lại repo rules để giả định đã duyệt craft.

Về nguồn, so sánh thực nghiệm hỗ trợ tác động của thao tác học tới outcome trong điều kiện đo. Nó **không** chứng minh unique mechanism, không giải thích nguyên nhân cá nhân quên, không chẩn đoán người xem hoặc người theo #texthip. Các điều kiện W-16 về thứ tự lời, pain–hứa–payoff, đủ ai/làm gì/thấy gì và gate trên đúng SHA lời vẫn do Reviewer kiểm; source lock không tự miễn chúng. Target 120–180s, total <300s không là lý do thêm evidence.

## 2. Primary đã xác minh, không nghiên cứu mới

Roediger, H. L., III, & Karpicke, J. D. (2006). *Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention*. Psychological Science, 17(3), 249–255.
- DOI: https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Author-lab full text: https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf
- Extract có sẵn được dùng đối chiếu: `/workspace/clip05-rk2006-primary-text-2026-11-08.txt`.
- Full extraction record có sẵn: `/workspace/clip05-rk2006-extract-2026-11-08.txt`; treg successful call `05c0c6f634074e00b69c48a6cfa01e48`.

Lượt supplemental này không content search, không mở primary mới, không thêm nguồn. Các locator dưới đây theo trang in PDF và dòng file text có sẵn. PDF extraction có lỗi font ký hiệu thống kê; không sao chép ký hiệu hỏng thành dữ kiện mới.

## 3. Experiment 1 — thiết kế khóa

- **N=120** sinh viên Washington University, **18–24 tuổi**; tham gia để hoàn thành một phần yêu cầu môn học (p.250, Subjects; text L111–114).
- **Vật liệu:** hai đoạn từ phần đọc hiểu sách luyện TOEFL: “The Sun” **256 từ**, “Sea Otters” **275 từ**; mỗi đoạn chia **30 idea units** để chấm (p.250, Materials; L116–122). Không phải sách dài, sách kỹ năng hay thử nghiệm #texthip.
- **Thiết kế 2×3 mixed:** learning condition **trong cùng người** (restudy vs test); delay **giữa người** (5 phút, 2 ngày, 1 tuần). Thứ tự conditions và passages được counterbalance (p.250, Design; L124–130). Không gọi toàn bộ thiết kế là hai nhóm độc lập. Không khẳng định random assignment vì phương pháp đã đọc không nêu rõ cách random.
- Mỗi người có bốn kỳ Phase 1: học lần đầu hai đoạn và mỗi đoạn có thêm một kỳ đọc lại hoặc tự nhớ lại. **Mỗi kỳ 7 phút**, cả study lẫn recall ban đầu; trong study đọc đoạn văn; trong recall được sheet có **tiêu đề đoạn** và viết tối đa nội dung nhớ được, không đòi nguyên văn hay đúng thứ tự (p.250, Procedure; L132–144). Không mô tả là hoàn toàn không cue: có title cue, nhưng không có nội dung đoạn để đọc lại.
- Làm phép nhân **2 phút giữa các kỳ**, **5 phút sau kỳ cuối Phase 1**. Phase 2 diễn ra sau **5 phút / 2 ngày / 1 tuần**; recall mỗi đoạn **10 phút**, đánh dấu vị trí theo từng phút (p.250, L143–151).
- Thao tác test là **free recall không feedback**, không cung cấp đáp án để đọc lại/sửa trong test. Exp1 không thao tác bước mở tài liệu đối chiếu và sửa của F5.
- Outcome: chấm **1 điểm mỗi idea unit nhớ đúng, trên 30**. Hai người chấm 40 tests đầu, correlation .95; các bài còn lại một người chấm (p.250, Scoring; L157–163). % là **tỷ lệ idea units nhớ đúng trung bình**, không % người thành công, không % hiểu đúng, không năng lực trí nhớ tổng quát.

## 4. Kết quả khóa — phải giữ đúng chiều so sánh

| Delay của final recall | Study + restudy (SS) | Study + recall test (ST) | Diễn giải trong thiết kế |
|---|---:|---:|---|
| **5 phút** | **81%** | **75%** | Đọc lại hơn test ban đầu |
| **2 ngày** | **54%** | **68%** | Test ban đầu hơn đọc lại |
| **1 tuần** | **42%** | **56%** | Test ban đầu hơn đọc lại |

Nguồn: p.251, Exp1 Results/Final Test, L206–214; Figure 1 pp.250–251. Bài báo nêu d=.52 cho 5 phút, .95 cho 2 ngày, .83 cho 1 tuần. Không cần đưa effect size vào lời; không đổi d thành %. Không dùng 61/40 hay 83/71: đó không phải số Exp1.

Delay là yếu tố giữa người: không kể như cùng một cá nhân/nhóm được đo liên tiếp ở cả ba mốc. Điều kiện học trong cùng người là hai passages đối ứng, không cùng một passage được cả SS lẫn ST ở một người. Không diễn giải ST làm “không quên nữa”; ở delayed tests vẫn có nhiều ý không recall.

**Mốc 5 phút bắt buộc đi cùng thông điệp về hiệu quả theo trì hoãn** theo quyết định Reviewer: đọc lại có lợi ngay lúc đo ngắn hạn, ST có lợi ở hai delay dài hơn. Không bỏ mốc này để tuyên bố test luôn hơn. Không gọi trì hoãn là “suy giảm năng lực trí nhớ”.

## 5. Quote nguyên văn / locator

Giữ tiếng Anh gốc; ký tự xuống dòng và dấu nối ngắt từ trong extract được nối lại, không đổi mệnh đề. URL chung là author-lab PDF ở §2.

**Q1 — within/between design:** p.250, Design; L125–128:
> “Learning condition (restudy vs. test) was manipulated within subjects, and delay of the final test (5 min, 2 days, or 1 week) was manipulated between subjects.”

**Q2 — thời lượng:** p.250, Procedure; L134–138:
> “They were told that Phase 1 consisted of four 7-min periods and that during any given period they would be asked to study one passage for the first time, restudy one of the passages, or take a recall test over one of the passages.”

**Q3 — 5 phút:** p.251, Final Test; L206–208:
> “Post hoc analyses confirmed that on the 5-min retention tests, restudying produced better recall than testing (81% vs. 75%)”
Đây là trích đoạn, dừng trước thống kê t/d, không phải toàn câu.

**Q4 — 2 ngày:** p.251, Final Test; L209–211:
> “After 2 days, the initially tested group recalled more than the additional-study group (68% vs. 54%)”
Đây là trích đoạn, dừng trước thống kê t/d. Từ “group” là cách tác giả viết kết quả; **không** làm thiết kế learning condition trở thành between-subjects.

**Q5 — 1 tuần:** p.251, Final Test; L212–214:
> “The tested group recalled 56% of the material, whereas the restudy group recalled only 42%”
Trích đoạn, dừng trước thống kê t/d. Material được đo bằng idea units như phần chấm điểm, không là từng từ nguyên văn.

**Q6 — no feedback, giới hạn cơ chế:** p.251, Exp1 discussion; L225–231:
> “The crossover interaction observed in Figure 1 is all the more impressive considering that no feedback was given on the tests.”
> “The testing effect on delayed retention tests is not simply due to reexposure to studied material during tests, but rather is due to some other process that has positive effects on retention.”
Tác giả tiếp tục: “We consider candidate processes in the General Discussion.” Điều này không xác định một cơ chế duy nhất. Không kéo thảo luận giả thuyết thành đo lường cơ chế hay chẩn đoán cá nhân.

## 6. Claim lock / limits

### Được phép ở cấp nội dung nguồn, chưa phải lời kịch bản

1. Sau học hai đoạn ngắn trong thiết kế Exp1 với sinh viên, thêm một kỳ tự viết nhớ lại không feedback cho recall sau 2 ngày/1 tuần cao hơn thêm một kỳ đọc lại; ngược lại ở 5 phút đọc lại cao hơn. Nêu đủ mẫu, thao tác, phép so và delay khi dùng số.
2. Có bằng chứng **thao tác cách học tạo khác biệt outcome recall trì hoãn**. Đây là cấp nguyên nhân vận hành được Reviewer chấp nhận có điều kiện, không là cơ chế duy nhất hay lời giải thích mọi quên lãng.
3. Pain phù hợp nguồn là khó nhớ lại **nội dung đã đọc sau vài ngày**. Một tình huống đời thường có thể minh họa pain này nếu gắn nhãn **minh họa biên tập**, không kể là tình huống đã được nghiên cứu hoặc chẩn đoán của nhân vật/người xem.
4. F5 vẫn dựa trên hai lock nền/23.14–23.16 trong phạm vi đã khóa; RK2006 Exp1 chỉ bổ sung so sánh đọc lại–truy xuất. Không coi RK2006 là xác minh độc lập toàn bộ quy trình F5.

### Không được phép

- “Bạn quên vì chỉ đọc”, “vì quen mắt”, “não chưa lưu”, “tự tin gây quên”, hay unique mechanism/chẩn đoán người xem. Không sử dụng Exp2 confidence kể cả để thêm pain.
- “Đọc lại vô dụng/không giúp nhớ/làm hỏng trí nhớ”; “test luôn tốt hơn”; “không test thì không nhớ”; hứa chắc nhớ đúng hoặc hứa tỷ lệ cho cá nhân.
- Đổi 68% vs54% hay 56% vs42% thành % tăng trí nhớ tổng quát; nhầm percentage-point difference với relative percent gain; dùng 14 điểm phần trăm như hiệu quả bảo đảm ngoài thí nghiệm.
- Nói thí nghiệm xác nhận feedback/đối chiếu–sửa của F5, số ba ý, tự nói thành tiếng thay viết, kỹ năng thao tác/vận động hoặc chuyển giao kỹ năng đời thường. Không có bài kiểm skill transfer ở đây.
- Gán kết quả hoặc pain cho người theo #texthip; trend chỉ bối cảnh riêng, không nguyên nhân hay outcome được bài này đo.
- Mở sang spaced learning, học dồn, negation hoặc các nguồn lịch sử ngoài lock. Không thêm evidence vì cần đủ 2–3 phút.

## 7. Hai lock nền — snapshot đã có, KHÔNG live check mới

Dùng evidence từ lượt bàn giao khoảng **13:06 ngày 08/11/2026 Asia/Saigon**, không tuyên bố vừa kiểm GitHub trong lượt này. Snapshot `ls-remote` live main: `dfab6f08fb66e55d3d637c7197a6f22c6d70dc6a`; GitHub đã đọc hai path tại chính SHA này và list_commits lọc path xác nhận latest modification:

| Path repo | Commit latest modification tại snapshot | Ngày commit Asia/Saigon | Sync tại snapshot |
|---|---|---|---|
| `research/fact-packages/factcheck-clip05-lock-2026-11-07.md` | `b02dd07f35bccee493009cb38501d9943404d14f` | 07/11/2026 13:25:59 | Có trên GitHub main tại SHA snapshot |
| `research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md` | `d673dd9e3f0d28a2eb6d2f66548c3c9add02fda1` | 07/11/2026 14:07:14 | Có trên GitHub main tại SHA snapshot |

Nội dung API khớp local sau bỏ trailing whitespace wrapper; **chưa độc lập hash raw remote bytes**. Local SHA256 khi đó: fact lock `72872ec45dacf5b7e94660faf8f2950b3e917b4dd9e00459adb460ecf1c0972e`; bridge `c060435a99bfe33e89c4a32f149351265617a93622cb53fa6f909f994025ec3c`. Không gán hai hash local thành remote hash. Local checkout/tracking khác live main ở lượt đó; **Mac chưa kiểm độc lập**. Không suy sync hiện tại từ snapshot.

## 8. Kiểm đính chính và bàn giao News

Đối chiếu lại extract có sẵn: **không phát hiện sai số Exp1** trong báo cáo source-options: 81/75, 68/54, 56/42 đều đúng chiều như §4. Bổ sung rõ hạn chế dễ kể sai: learning condition là within-subjects; có title cue; delay là between-subjects; 7 phút là mỗi kỳ Phase1, final recall 10 phút. Các quote kết quả §5 là trích đoạn bỏ phần thống kê, không giả là toàn câu. Không phát hiện sai nội dung quote Exp1 trước cần rút; tránh lấy abstract tổng hai experiments làm mô tả riêng Exp1.

**News cần xác minh trước gọi archive complete:**
1. Nhận đúng standalone này và SHA256 bàn giao; lưu **nguyên bytes** theo proposed repo path qua workflow chuẩn. Không sửa hai lock nền; không âm thầm chỉnh file supplemental sau hashing. Nếu cần đổi bytes, trả hash mới.
2. Kiểm hash file đã lưu, path, commit thực sự chứa file; báo commit đầy đủ và ngày/giờ Asia/Saigon. Không dùng commit lock cũ làm commit supplemental.
3. Kiểm live origin/main mới bằng evidence hiện tại: supplemental tồn tại tại đúng ref, commit nằm trên main, nội dung/bytes tương ứng. Phân biệt “đã commit local”, “đã push”, “đã hiện trên live main”.
4. Kiểm **Mac độc lập** theo workflow chuẩn: branch/HEAD, file bytes/hash và sync với live main; nếu chưa kiểm thì ghi CHƯA KIỂM, không gọi Mac synced.
5. Bàn giao latest path/commit/thời điểm/sync và những giới hạn bytes còn lại cho Reviewer/OC. Cho tới đó: **VERIFIED source scope nhưng ARCHIVE/SYNC PENDING**; không coi là đã đáp ứng điều kiện archive trong quyết định Reviewer.

Không gửi ai trong lượt này. Không commit/repo write, không script, hình, voice hoặc render. SHA256 chính xác của file standalone được báo ngoài file sau khi đóng bytes (không chèn hash tự tham chiếu vào chính file).
