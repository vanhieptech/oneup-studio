# Clip05 r15.2 — fact-check mới trên actual frozen

Thời điểm: 08/11/2026 14:36:04 Asia/Saigon (UTC+7). Báo cáo nội bộ standalone, ngoài repo, **CHƯA ARCHIVE**. Đây là verdict mới cho r15.2, không trả lại verdict r15.1. Đã đọc review `/workspace/clip05-r15.2-rule-review-2026-11-08.md` để biết scope; không coi report agent là authority khoa học, owner approval hay Chốt.

## 1. Freeze / delta thực / kiểm trước–sau

Frozen path: `/home/box/agent-data/agents/315819de-26d8-48c8-a4a6-e2f7a5d3545a/handoffs/clip05-r15.2-full-draft-2026-11-08.md`.

| Đối tượng | SHA256 tự tính trước và sau | Verdict |
|---|---|---|
| Toàn file | `87885dd3f4e0b1d847e7971c0476878f85691e3178b55ff7cbae6f6a096f7dc2` | KHỚP expected, không đổi |
| Spoken payload | `3a6f280daede0ea30db9d095643deb7f77868981ea22b804991b3b425cf7a78e` | KHỚP expected, không đổi |

Extraction đúng frozen L275: lấy bytes **sau toàn opening marker line và LF**, trước closing marker line; giữ LF cuối, UTF-8, blank lines, spacing và punctuation nguyên trạng. Không strip/normalize hoặc ghép từ index. Đếm payload bằng `len(spoken.split())`: **439 whitespace units**, khớp report; không phải xác nhận thời lượng đọc.

So sánh actual r15.1 cùng handoff dir (fileSHA `57322fba5e105ae0e81c290d0aefbb0d9b4ceef12449d2a01ff4d39b3c60183c`, spokenSHA `ee0e5aa879d3e2fa373e9aa3edab91d2a84d0f7c42c519755d718f40c5750652`):
- Chỉ có **một lần thay exact S18 cũ bằng exact S18 mới** trong spoken. Phép `old_spoken.replace(old_S18, new_S18) == new_spoken` trả TRUE; mỗi chuỗi S18 xuất hiện đúng một lần. Đây là kiểm trực tiếp toàn phần trước/sau, không dựa lời OC/Reviewer.
- Bỏ đúng bytes S18 (không bỏ space kề bên, không normalize), hash phần còn lại cả hai payload đều: **`7153b793bbcae1e9c540a66dae41ea7b4e4fedb635492fdf40772270af9a6fa9`**. Do đó S01–S17/S19–S21 cùng mọi whitespace ngoài S18 giữ nguyên.
- Reviewer nêu non-S18 aggregate `00a768f35d801d65895cdb0a56e0016b8e240b99a72557927e842d71454c3b53` nhưng review không cung cấp thuật toán serialize/aggregate. **Không tuyên bố tái lập hash ấy**, cũng không gọi là mismatch: hash của phép bỏ bytes S18 bên trên dùng thuật toán được công khai khác. Không đoán delimiter hoặc normalize để ép khớp.
- Vế từ dấu phẩy S18 “, nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.” giữ nguyên bytes, có trong đúng một thay thế đã kiểm. Không kế thừa PASS r15.1 dù phần khác giữ nguyên.

## 2. Source path / latest commit / date / sync — xác nhận trước verdict

Read-only `git ls-remote origin refs/heads/main` lượt này trả **`a32f51f558ff144a8448f6a00eeb900e2ad23542`**. SHA live không đổi so lượt trước nhưng đây là **quan sát ref mới**, không giả dùng snapshot cũ. Commit object này có sẵn local; không fetch/pull/reset/checkout.

`git log -1 <live-pinned SHA> -- <path>` xác minh latest modification trong đúng lịch sử live-pinned; `git show <live-pinned SHA>:<path>` lấy exact blob bytes và so với working tree. Cả ba TRUE:

| Canonical path từ `/workspace/oneup-studio` | Latest modification tại live-pinned commit | Commit time Asia/Saigon | SHA256 pinned blob = working tree |
|---|---|---|---|
| `research/fact-packages/clip05-rk2006-exp1-supplement-lock-2026-11-08.md` | `8ff76986f8b14976c3bc4eb3f2f913a03b09703c` | 08/11/2026 13:10:25 | `ac400b83755c2ede277b6917c47c69e16193280be3d8b8a3c55ce5a934172a64` |
| `research/fact-packages/factcheck-clip05-lock-2026-11-07.md` | `b02dd07f35bccee493009cb38501d9943404d14f` | 07/11/2026 13:25:59 | `72872ec45dacf5b7e94660faf8f2950b3e917b4dd9e00459adb460ecf1c0972e` |
| `research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md` | `d673dd9e3f0d28a2eb6d2f66548c3c9add02fda1` | 07/11/2026 14:07:14 | `c060435a99bfe33e89c4a32f149351265617a93622cb53fa6f909f994025ec3c` |

**Sync phạm vi file:** các packages tồn tại trong commit được live ref trỏ tới, exact pinned blob bytes khớp working tree. Không hash API wrapper; không cần mở bài nghiên cứu mới. Lượt này dùng existing git objects gắn với live-ref SHA; không tuyên bố vừa tải raw remote HTTP bytes lần nữa. GitHub connector lượt trước đã đọc các path tại cùng SHA, nhưng không gọi lại lượt này.

Local checkout HEAD `8ff76986…` khác live-main `a32f51f…`: **không toàn repo synced**. **Mac chưa độc lập kiểm**, không suy từ News/OC. Header PENDING trong supplemental là lịch sử lúc soạn; bằng chứng main/file hiện tại như trên, không sửa header. Live ref có thể thay sau snapshot kiểm này.

## 3. S18 mới — ĐẠT scoped source

**Exact S17 và S18, frozen spoken L40; index S17 L132, S18 L137:**
> “Còn trong thí nghiệm với sinh viên ấy, sau một tuần, tự viết không có đáp án cho trung bình 56 phần trăm ý nhớ đúng, đọc lại là 42 phần trăm. Tự viết cho tỷ lệ ý nhớ đúng cao hơn ở mốc này, nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.”

**Nguồn và quote đã khóa:** RK2006, Experiment1, p.251, Results/Final Test; supplemental §4 L42, Q5 L68–70; existing primary extract `/workspace/clip05-rk2006-primary-text-2026-11-08.txt` L212–214:
> “The tested group recalled 56% of the material, whereas the restudy group recalled only 42%”
Đây là trích đoạn trước thống kê t/d; “material” chấm theo30 idea units/đoạn (supplement §3 L29/L34; primary p.250 Scoring L157–163), không % số người hay nhớ từng từ.

Primary URL đã khóa, **không mở mới**: https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf ; DOI https://doi.org/10.1111/j.1467-9280.2006.01693.x .

Lý do ĐẠT trên chính wording mới:
- **Đúng dimension:** “tỷ lệ ý nhớ đúng” là tỷ lệ idea units trung bình vừa nêu ở S17; không năng lực trí nhớ tổng quát, không %people, không số kỹ năng.
- **Đúng chiều:**56ST >42SS; “cao hơn” chỉ ordering, không gắn label độ lớn nhỏ/lớn, không hiệu ứng “đáng kể/vượt trội”, không số hiệu ứng mới. Không cần suy d=.83 thành một từ chỉ mức độ; không mở lock effect-size hay áp ngưỡng mới.
- **Đúng mốc:** “ở mốc này” quy chiếu **sau một tuần** trong S17 cùng đoạn. Không làm thành luôn hơn; S10 tại L34 vẫn nguyên chiều **reread hơn5phút** (81/75 trong lock).
- **Đúng giới hạn:**56% không100%, nên “không phải nhớ hết nội dung” đúng cho outcome trung bình này. Không có nghĩa mọi sinh viên đều không thể nhớ hết; câu nói kết quả trung bình, không phân bố cá nhân. Không hứa người xem đạt56% hay chênh14điểm.
- S17 giữ **thí nghiệm với sinh viên/no feedback** và S16 L38 tách mở–so–sửa F5. Không gán56/42 cho F5, không biến practice efficacy thành unique mechanism hay causal diagnosis.

Caption S18 **L201**: “At this delay, recall practice yielded / a higher proportion of correctly recalled ideas, / but even that result / did not mean remembering all the content.” Cùng dimension/chiều/mốc; không thêm magnitude. Mapping L139 và plan b07 L170 đồng nhất; thanh0–100 cùng thước56/42 và NOFEEDBACK là plan đúng nguồn, chưa chứng nhận thành phẩm hình.

## 4. Rà exactspoken toàn scope, không chỉ delta

| Câu / dòng spoken | Kết quả rà r15.2 → nguồn/limits |
|---|---|
| S01–S03 / L28–30 | Hai ngày restudy thấp hơn recall, hai đoạn khác nhau, câu hỏi/đáp một tuần; Exp1 năm2006. Đúng supplemental L18/L28–34/L41–42; không sửa thành cùng đoạn hoặc theo dõi cùng người liên tiếp. |
| S04 / L30 | Hứa cung cấp phép so/câu hỏi, không hứa hiệu quả trí nhớ cá nhân; biên tập. |
| S05 / L30 | Trend lifestyle/sharing/kết nối, không memory efficacy hay nguyên nhân quên. Phù hợp ranh giới bridge L10–25/L29–39; provenance Social tách §5. |
| S06–S09 / L32 |120 sinh viên/hai đoạn; mỗi người một đoạn restudy, đoạn kia recall; titlecue/no sourcecontent/no feedback; delay5phút/2ngày/1tuần ở người khác nhau. Đúng supplemental §3 L28–34/L46; N120 là tổng, không120 ở một delay; learning within-person, delay between-person. |
| S10–S11 / L34 |5phút reread cao hơn (SS81/ST75);2ngày thứ tự đảo (ST68/SS54). Đúng lock L40–41/L48; không thiếu chiều5phút. Lời không thêm số ngoài56/42. |
| S12 / L34 |Thao tác luyện→recall trong chính experiment, không cơ chế não/quen mắt/nguyên nhân một cá nhân quên. Đúng supplemental L81–82; không scientific unique mechanism. |
| S13 / L36 |Goal có điều kiện muốn kể nội dung không mở bài; biên tập, không claim kỹ năng xã hội/chia sẻ đã được RK đo hoặc một can thiệp duy nhất cần thiết. |
| S14–S15 / L38 |F5 đóng→tự viết→mở đối chiếu/sửa; fact lock L10–11, bridge L16–17; không outcome RK cho toàn quy trình. |
| S16 / L38 |Bước so/sửa thuộc cẩm nang, không test trong RKExp1 nofeedback; đúng supplemental L33/L84/L91. |
| S17–S18 / L40 |56ST/42SS một tuần/no feedback/average ideaunits và S18 direction-only; ĐẠT, phân tích §3. |
| S19–S20 / L42 |Câu hỏi kênh, “Giả sử” titlecue không mở bài: prompt biên tập, không bài test riêng đã validate hay trích nguyên câu RK; không dựng nhớ thành công sau vài ngày. |
| S21 / L44 |CTA chủ đề; không fact khoa học, không gửi/bình luận thực hiện trong lượt này. |

Không phát hiện Exp2/confidence/Yang/spacing/negation, chẩn đoán người xem, đọc lại vô dụng, self-testing luôn hơn, promise skill transfer hay %tăng trí nhớ. Không có Nam/Lan/case quên giả trong bản này. Exactspoken không nêu mọi detail7phút/10phút/tuổi không tự là sai vì không phủ định phương pháp; audit L221 giữ đúng các detail trong lock, không khẳng định random allocation.

## 5. Social gate và điều chưa xác minh

- S05 không đổi byte; không đánh đồng ba Deep packages với nguồn trend. Handoff Social có sẵn và snapshots Znews L40/L58/L60, Korea Times L39–41 mô tả lifestyle/book clubs/sharing. Đây là nguồn Social về bối cảnh, không thí nghiệm trí nhớ. Không mở public URLs, không xác minh mới hotness hay participant memory.
- Reviewer nói không mở lại Social vì phần trend không đổi: ghi nhận đây là scope quyết định workflow của Reviewer, **không tự phát hành Social-owner verdict trên SHA mới**, cũng không đặt blocker Social mới. Provenance Social vẫn là handoff/snapshots có sẵn, không được nâng thành fresh public verification của tôi.
- Không craft/nghĩaPASS, không Chốt, không user approval; human đọc to/nghe lần đầu, timing thật, full checker và media không thuộc source verdict này.

## 6. Kết luận / handoff

**r15.2 trên hai SHA đầy đủ ở §1: không thấy lỗi fact cần chặn trong phạm vi Exp1/F5; S18 mới ĐẠT source vì nói đúng tỷ lệ, chiều và mốc, không phát sinh magnitude/effect-size/generalization.** Kết luận dựa actual frozen và các packages đã reverify sync trước kết luận, không dùng verdict r15.1 thay thế.

Đã assert file/spoken/ba locks không đổi sau rà. Báo cáo này ngoài repo chưa archive; không đề xuất lời thay, không sửa nguồn/lock/script/repo, không bài mới/research/media/ảnh/voice/render/send.
