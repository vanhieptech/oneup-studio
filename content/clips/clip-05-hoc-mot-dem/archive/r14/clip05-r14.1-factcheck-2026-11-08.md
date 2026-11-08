# Clip05 r14.1 — fact-check frozen exact spoken

Thời điểm: 08/11/2026 13:23:23 Asia/Saigon (UTC+7). Báo cáo standalone ngoài repo; **CHƯA ARCHIVE**.

## Verdict scoped

**Không thấy lỗi fact trong RK2006 Exp1 / F5 / minh họa Nam trên exact spoken đã hash**, kể cả captions và mapping liên quan. Không phát hiện nhầm thiết kế within-person, đảo chiều 5 phút, sai 68/54% idea units, gán feedback F5 cho Exp1, dữ liệu Exp2, chẩn đoán cá nhân hay hứa skill transfer.

Đây **không phải craft PASS, W-16 toàn bộ PASS, Chốt hay quyền sản xuất**. Claim trend S03 thuộc Social; chỉ đối chiếu handoff có sẵn và ranh giới bridge, không tự xác minh báo gốc/live trend trong lượt này. Live GitHub và Mac **chưa kiểm độc lập lượt này**; agent report archive/live/Mac không biến thành quan sát của tôi.

## 1. Freeze / extraction / hashes trước và sau

Frozen: `/home/box/agent-data/agents/315819de-26d8-48c8-a4a6-e2f7a5d3545a/handoffs/clip05-r14.1-full-draft-2026-11-08.md`.
- File SHA256: `020c410911f8d85163f5448e0e965a1f92371c79ccce1f3224473aaf077433f8` — KHỚP expected.
- Spoken SHA256: `2ed4d15324ac3d3d8d7d12505498c067f87e63f942bd1d72c1a375745be05bea` — KHỚP expected và counts-audit metadata.
- Extraction: bắt đầu **sau toàn dòng** `<!-- SPOKEN_START -->` cùng LF của dòng marker; kết thúc ngay trước opening byte của `<!-- SPOKEN_END -->`; giữ nguyên UTF-8, blank lines giữa beats, spacing/punctuation và LF cuối spoken. Không strip/normalize, không ghép lại index hay beat để ép hash khớp.
- Ghi rõ giới hạn diễn đạt L223 “bytes giữa marker”: nếu lấy substring sau chuỗi token marker nhưng **kèm LF của dòng opening marker**, SHA sẽ là `dfeb04b8759afc2025941a10c919ded713c04017ab837fac1e6958007bdfcfb0`, không phải expected. Hash expected tương ứng nội dung sau **marker line** (L29–47, với LF cuối), không phải cả delimiter newline. Đây là phân định marker line; không thay nội dung spoken. Metadata không có thuật toán extraction chi tiết hơn; không che sự khác biệt delimiter này.
- Đã kiểm lại sau review: file/spoken và ba lock không đổi; hash sau khớp trước (assert bằng code, không chỉ dựa mtime).

## 2. Nguồn canonical, commit và sync thực kiểm

Repo local `/workspace/oneup-studio`:
- Supplemental canonical `research/fact-packages/clip05-rk2006-exp1-supplement-lock-2026-11-08.md`: SHA256 `ac400b83755c2ede277b6917c47c69e16193280be3d8b8a3c55ce5a934172a64` **khớp expected**.
- `git log -1 -- path` trả `8ff76986f8b14976c3bc4eb3f2f913a03b09703c`, commit **08/11/2026 13:10:25 Asia/Saigon**. Local HEAD tại kiểm cũng là commit này. `git show <commit>:<path> | sha256sum` cho cùng hash: **đã tự xác minh file local và bytes trong commit local**, không chỉ nghe OC.
- Dòng ARCHIVE/SYNC PENDING trong supplemental là trạng thái lúc soạn. Nay có bằng chứng local archive commit; **không tự nâng thành live+Mac verified**. News/OC nói live+Mac là agent report chưa độc lập kiểm trong lượt này.
- Hai lock cũ đã đọc, hash local: fact lock `72872ec45dacf5b7e94660faf8f2950b3e917b4dd9e00459adb460ecf1c0972e`; bridge `c060435a99bfe33e89c4a32f149351265617a93622cb53fa6f909f994025ec3c` — khớp snapshot trước, không sửa.
- Hai lock cũ path/commit: `research/fact-packages/factcheck-clip05-lock-2026-11-07.md` @ b02dd07 (07/11 13:25:59 Asia/Saigon); `research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md` @ d673dd9 (07/11 14:07:14 Asia/Saigon). Live snapshot khoảng 13:06 ngày08/11 đã xác nhận có trên main `dfab6f08fb66e55d3d637c7197a6f22c6d70dc6a`; **đây là snapshot cũ, không live mới**.

Nguồn dùng: supplemental canonical §3–6; fact lock L10–11/L24–26/L50–58; bridge L10–25/L29–39. Primary locator đã khóa: RK2006 Exp1 pp.250–251 (thiết kế/procedure/scoring và final test); không mở web/research mới. Social handoff `/workspace/social-clip05-source-confirmation-2026-11-08-1303.md` L34–43 chỉ dùng đối chiếu phạm vi trend và nhãn giả định.

## 3. Claim-by-claim exact spoken

Sxx theo index L50–69 của frozen; “L” cột dưới là dòng **spoken**, không dòng mapping. ĐẠT nghĩa không thấy lỗi trong phạm vi nguồn được nêu, không craft verdict.

| ID / dòng spoken | Claim / loại nội dung | Verdict và đối chiếu |
|---|---|---|
| S01 / L29 | “Giả sử” chỉ nhớ tên bài tại buổi đọc chung | ĐẠT phạm vi minh họa. Tình huống giả định, không self-report người thật hoặc tần suất audience. Mapping L146, mẫu L99 thống nhất. |
| S02 / L31 câu đầu | Đã đọc chuyện gọi mẹ vài hôm trước để chia sẻ | ĐẠT như tình huống tiếp nối “giả sử”, không dữ liệu nghiên cứu, không gán cho người theo trend. |
| S03 / L31 câu sau | Text hip ở một bộ phận người trẻ Hàn, đọc/chia sẻ như sinh hoạt xã hội | **GIỚI HẠN THẨM QUYỀN SOCIAL**. Handoff Social L34/L43 hỗ trợ phạm vi bối cảnh xã hội, không hotness hay hiệu quả. Không thấy xung đột bridge; chưa tự kiểm báo gốc. Không lấy hai lock Deep làm nguồn độc lập cho claim trend. |
| S04 / L33 câu hỏi | Đọc lại có phải lúc nào cũng hơn tự viết? | ĐẠT phạm vi đặt phép so, không khẳng định nguyên nhân cá nhân, không công bố self-testing luôn hơn. Câu trả lời được giới hạn bởi S05. |
| S05 / L33 câu đáp | Exp1 năm2006: reread hơn5phút; written recall hơn2ngày/1tuần | ĐẠT. Supplemental §4 L40–42 và Q3–Q5; đủ chiều ngắn/dài. Không phải số Exp2. |
| S06 / L35 câu đầu | 120 sinh viên, hai đoạn; mỗi người đọc lại một, recall đoạn kia; không nội dung/đáp án sửa | ĐẠT. §3 L28–33: learning condition within-person, title cue có nhưng không nội dung nguồn; lời không nói no-cue. Không kể thành hai nhóm học độc lập. Rút gọn procedure nhưng không mâu thuẫn. |
| S07 / L35 câu hai | Hai ngày: 68% vs54%, tỷ lệ ý nhớ đúng trung bình | ĐẠT. §4 L41/Q4; 68 ST,54 SS; idea units chứ không % người/% tăng trí nhớ. 120 là tổng N ở ba delay, không nói tất cả120 thuộc delay2ngày. |
| S08 / L35 câu ba | Đổi thao tác sau lần đọc tạo khác biệt lượng recall sau vài ngày trong thí nghiệm | ĐẠT giới hạn causal outcome. §6 L81–82 cho phép operational manipulation→outcome; không gọi là unique mechanism/chẩn đoán người xem. |
| S09 / L37 câu đầu | Goal bản kể lời mình để so, không cần thuộc từng câu | ĐẠT như mục tiêu biên tập/F5. Exp1 cũng không đòi nguyên văn (§3 L31), nhưng không lấy goal làm hiệu quả bảo đảm. |
| S10 / L37 câu sau | Mẫu kênh tự viết Nam gọi mẹ, hoa nở | ĐẠT. Nội dung khớp mẫu frozen L93–97; nhãn tự dựng hiện trong lời. Không phải stimulus RK, sách thật hay ca quan sát. |
| S11 / L39 câu đầu | Cẩm nang gợi ý đóng bài, viết điều nhớ | ĐẠT F5 fact lock L11/bridge L16–17; áp vào mẫu là minh họa biên tập. Không gán thử nghiệm Nam cho RK. |
| S12 / L39 câu sau | Mở gốc, đối chiếu và sửa bản kể | ĐẠT F5, không phải feedback protocol Exp1. Nhãn nguồn và ranh giới được S14 nói rõ; không claim tăng kỹ năng gọi điện. |
| S13 / L41 | Hai bản cạnh nhau cho phép kiểm câu chuyện khớp nội dung | ĐẠT kết quả thao tác hiện tại của minh họa, không retention vài ngày. Không hứa bản kể tự động đúng. |
| S14 / L43 câu đầu | So/sửa là hướng dẫn cẩm nang, không được thử trong Exp1 không đáp án | ĐẠT. §3 L33/§6 L84,L91; phân nguồn đúng. |
| S15 / L43 câu sau | Đoạn ngắn/sinh viên không giải thích cá nhân hay bảo đảm lần đọc | ĐẠT giới hạn khái quát §3 L28–29 và §6 L88–91. |
| S16 / L45 câu đầu | Recall trễ cần đợi lần recall sau, bản hôm nay chưa trả lời | ĐẠT sự phân biệt kết quả hiện tại và outcome trễ chưa đo; không dựng thành công sau2ngày. |
| S17 / L45 câu sau | Có thể tận hưởng buổi đọc, chọn chuyện thử lại, không mọi trang thành test | ĐẠT như gợi ý biên tập/quyền lựa chọn; bridge L25 không bắt đọc thưởng thức phải self-test. Không claim đo động lực. |
| S18 / L47 câu đầu | Hỏi chủ đề muốn nhớ sau vài ngày | ĐẠT như CTA, không promise hiệu quả. |
| S19 / L47 câu sau | Bình luận một từ | Không claim khoa học để kiểm. Không thực hiện gửi/bình luận trong lượt này. |

## 4. Mapping / captions / plan — kiểm mâu thuẫn fact rõ

- Caption S05 L113 giữ đủ5phút/2ngày/1tuần; S06 L114 giữ each person và không nhìn content/không corrective answers; S07 L115 giữ đúng2ngày,68/54% và average correctly recalled ideas; S08 L116 chỉ outcome. Không thấy đổi đơn vị sang % người hay mức tăng trí nhớ.
- Caption S10–S16 L118–124: original sample, handbook method, compare/correct không nằm trong experiment, giới hạn cá nhân và trì hoãn chưa biết đều giữ. “flowers” dịch hoa ở mẫu không làm phát sinh claim khoa học; không phải bản dịch nguyên văn stimulus thực nghiệm.
- Beat b04 L80: một người/hai đoạn, hai cột2ngày, IDEAS RECALLED CORRECTLY; **không hai nhóm học độc lập**. Chỉ plan, không kiểm thành phẩm hình.
- Source detail L137–142: N/tuổi,256/275 từ,30ideaunits; within-person/counterbalance; delay between-person; title cue; 7phút Phase1 vs10phút final; 81/75,54/68,42/56 đúng thứ tự SS/ST. Không claim random allocation hoặc cùng người test liên tiếp cả ba delay. L140 không biến7phút thành liều F5 bắt buộc.
- Mapping L149–160 trỏ đúng các mục/line supplemental cho Exp1/F5. L154–157 không biến cẩm nang thành nghiên cứu riêng mẫu Nam; L159 tách feedback. Không thấy mâu thuẫn fact rõ giữa mapping và spoken.
- Mẫu L94 và bản kể L97 giữ đúng người/việc/cốt truyện; không có skill transfer hoặc kết quả sau2ngày (L99–101). Endcard L216–219 ghi Exp1 only và minh họa tự dựng; không chèn Yang/Exp2 vào bằng chứng lời.
- Không kiểm layout, thời gian đọc caption/endcard, human listening hay craft/naturalness. Thiếu nêu mọi chi tiết phương pháp trong spoken không tự là sai fact khi wording hiện có không phủ định chúng; plan cũng phải giữ đúng khi thực hiện sau này.

## 5. Blockers / điều chưa xác minh

1. Social owner vẫn cần verdict trên chính S03/caption/mapping nếu gate đòi xác nhận trend exactspoken; handoff Social cũ là phạm vi nguồn, không verdict craft r14.1.
2. Supplemental **local file+commit verified**; live main/Mac của archive8ff76986 là agent report chưa tự kiểm lượt này. Không kết luận archive fail, cũng không chứng nhận live/Mac complete.
3. Extraction wording L223 có delimiter newline không tường minh; đã công khai cả hai hash ở §1. Content sau marker line khớp expected, không đổi/chuẩn hóa frozen. Nếu workflow đòi byte slice gồm delimiter LF, cần chủ freeze xác nhận định nghĩa, không tự sửa file hoặc expected hash.
4. Chưa craft/W-16 full verdict, human read-aloud, actual timing, sản xuất; không coi source scope thành approval/Chốt.

Không research mới, không đổi frozen/source/repo, không câu thay, không Page/media/render/send. Report ngoài repo chưa commit/archive.
