# Clip05 r11.4 plan-update1 — delta Rule Review
07/11/2026, Asia/Saigon. Review-only; không sửa lời/spec/code/repo, không research nguồn, không tin nhắn, không ảnh/audio/render.

## Kết luận
**Delta giải quyết đúng ba vấn đề nghĩa/mapping đã bàn giao ở mức kế hoạch; không đổi lời, không tính patch3. Chưa thể gọi toàn gói gate1 đạt.** Có hai xung đột luật hình thực cần đóng: tiêu đề HF bằng tiếng Việt (R16) và cover bỏ strike bắt buộc của templateA (R54). Không phải lỗi fact/lời chính, không yêu cầu viết lại script.
Không còn blocker “chưa Deep/Social kiểm lời” hay callback/release04. Không lấy thiếu engine/render cuối làm lý do vô hạn không cho duyệt lời. Gate đọc/người lạ còn thật; preview và registry/storage vẫn thuộc trước trình gate1 theo luật hiện hành, không được âm thầm miễn.

## 1. Identity độc lập
D = `/workspace/opencreator-clip05-script-r11.4-draft-2026-11-07.md` SHA **dc42247775b8fdd0d6c5a6958e074a829e899f431efcc826516f61e21c53dd0e** giữ nguyên.
J = `/workspace/opencreator-clip05-spec-r11.4-plan-update1-2026-11-07.json` SHA **778539ad707a810cd387445a9a9c2f79e1fc2ad0f3157b65077432a93ef0788e** khớp.
B = `/workspace/opencreator-clip05-storyboard-r11.4-plan-update1-2026-11-07.md` SHA **819b038bfd970088c1fe8a006ab39a62999563cd90941e6d6191cecc480bcf49** khớp manifest.
Independent checks: `/workspace/clip05-r11.4-plan-update1-reviewer-checks-2026-11-07.txt`.
Parse actual:7speechbeats khớpD23–29;150=[24,18,21,11,28,27,21];50từ sauhook trước method.23caption bindings nguyên dict so spec trước; các text/marked_text/caption/phrases_plan giữ nguyên. Không cộng labels/endcard vào lời hoặc dựng caption24. Đây là identity/plan check, không engine/craft/ảnh pass. Không cần chạy lại chuỗi sửa lời/novelty để chấm visualdelta; các textchecker status của đúngSHA ở review r11.4 vẫn giữ, trendFAIL không bị che.

NguồnR/C/L: `/workspace/oneup-studio/rules/video-rules.md`, `logs/rule-checklist.md`, `logs/lessons.md` đã đọc trong chuỗi review, exactrefs dưới. L094 L208 “Sau ≥3 vòng vá cùng một bản…” không áp thànhpatch3 vì lời không đổi và đây là bổ sung visualplan sau ownercheck, không vòng vá wordingB mới.

## 2. Owner verdict đã cập nhật — không tự kiểm nguồn
Deep report `/workspace/clip05-r11.4-factcheck-2026-11-07.md`:8/12 đúngSHA;32 PASS lời chính+minh họa trong2locks;42/45/49–53 giải thích scope;56/69 bỏ callbackblocker vì actual không releaseclaim. Social15:26 Asia/Saigon scopedPASS trend/pain theo ownerhandoff; không có Socialreport riêng để tựgán đã đọc. Không cần chờ sourceowners kiểm lại lời bytekhôngđổi.
Deep cover/label/disclosure pending ở report34/57–58/65–67 là cơ sởdelta, không tự kế thừa PASS hình mới. Không causaltexthip, không cùngtrendpainrequirement, không hot/rawlive/Yang/hai nhóm mới. Pain mộtindividual archive chỉ làm căn cứ giới hạn phát triển minh họa đọc; không channelviewer/đámđông/test/efficacy.

## 3. Delta pass/fail/chưa kiểm
|Delta / actualref|Status đúng phạmvi|
|---|---|
|Mocklabel thành object: B6/16–17/28–29/36/38; J4515–4533/4555–4573|**PASS mapping/intention**: exact “MINH HỌA BIÊN TẬP CỦA KÊNH”, b05 từ Ví dụ24.748889s, giữ b06. Không còn chỉ note không hiện. Font/wrap/glyph/contrast/ảnh **CHƯA KIỂM**. Không gọi Vietnamese prose-note auto visible.|
|Hai cột/source bất biến: B37–44/51–52; J4655–4699|**PASS logicplan**: sourceFood+Rent có sẵn, sourceRent chỉ uncover tiềnthuênhà31.971111s; objectRent khác append vào phầnkể35.304445s, sourcekhôngsửa/xóa/move. Không phải ngân sách tốt hơn hay successfulrealaction. Thời gianước, motion/frame **CK**.|
|Coverutility: B7/79–87; J1534–1548/4321–4359|**PASS nghĩa nguồn trên chữ**: STUDY UTILITY giữ phạmvi, REREAD:LOW/SELF-TEST:HIGH là nhóm hữuích, không%/rank1–10/directscore/đọclạivôdụng. Bbox giữ1010/1590 trong1020/1600; không fakeảnh. **FAIL compatibility vớiR54 mandatorystrike**, xem dưới. Native nullstrike/transform/rig/textfit **CK**.|
|AIconditional: B8/45–49/88–97; J1474–1491/1601–1603/4808; D296|**PASS consistencyplan**: base4credit giữ, row5 exactAIHiệp/F5 chỉ khi actualai_voice_used=true, noAI khôngrow5/toggle. Không claim audiođãcó. Productionbranch/post/togglethật/readability **CK** theoR46:126/R53. Không thêm lời/caption.|
|Main script/sources/callback|**UNCHANGED/PASS scoped owners**; readaloud/one-listen/stranger **CK**; callbackkhôngclaimkhôngblocker B105. Không mở lại source scope.|

### Hai conflict hình thật, không sửa lời
**F1 — tiêu đề motiongraphics tiếng Việt.** R16:41 nguyên văn: “caption và tiêu đề chỉ tiếng Anh… Ngoại lệ: bubble thoại và hộp dẫn chuyện trong beat comic… viết tiếng Việt”. J4535–4553 đặt object `comparison-title-text` “SO PHẦN KỂ VỚI TRANG MINH HỌA”, parent`comparison-heading`, trong b06 HyperFrames (B17/29/37). Đây là title HF thật, không thuộc ngoại lệ comic. Nhãn “visual-object…NOT caption” ởJ4549 không làm tiêu đề thành ngoại lệ. Cần OC/visual đưa title về tuânR16 hoặc Hiệp cho ngoại lệ hẹp tiêu đề b06 tiếng Việt. Các header J4575–4613/B39–40 cũng là heading mới cần xử lý nhất quán. Không kết luận mọi chữ Việt trong mock/credit đều cấm: labelprovenance và endcardsafety là vai khác, không inventEnglish-only cho toànmọitext. Không đưa câu dịch/thay sẵn.

**F2 — no-strike vs templateA rule.** R54:181 nguyên văn: “hero 2–4 chữ (chữ thói quen cũ bị gạch → chữ mới trong pill ink)”. J1540 strike=null, B80 nói no strike; đây là thay grammar bắt buộc, không chỉ adapterchưacó. Deep cấm suyđọclạivôdụng nhưng không ra quyền miễnR54. Cần visual/OC chọn mapping tuân cả nghĩa low/high vàR54; nếu giữ no-strike thì ngoại lệ nhỏ nhất Hiệp cần duyệt: **riêng coverclip05 được thay old→newstrike bằng đối chiếu hai nhómutility khônggạch; các slotA/brand/safezone/series/ep/credit giữ**. Khôngđòi user chọntrend/concept lại; không ép gạch để sai fact. Đây là quyết định grammarcover hữu hạn, không lỗi mainwording.
Không gọi R16/R54 conflict là failnghiêncứu; không coi điều này đòiviết lạihook. Nullstrikeengine support riêng **CK**, không engineđãfail.

## 4. Trước Chốt lời vs production — exactrule, không kéo hậu kỳ vào gate lời
Không có quy tắc riêng trong nguồn nói “duyệt words-only = đã hoàn tấtgate1”. Hiệp có thể quyết định riêng wording; reviewer không được báo đạt gate1/cho chạyvoice khi các yêu cầu trước trình hiện hành còn thiếu. Phân biệt rõ:

### A. Kiểm lời trước duyệt — chưa làm, không giảpass
- **L089/C170**: “đọc to b01→CTA… làm ĐẦU TIÊN, trước khi chấm bất kỳ luật nào”; “Trượt cổng = CHƯA ĐẠT dù bảng luật đạt.” **L091/C172** “nghe một lần là hiểu”; **P16/C38/L064:81** “Hook đạt phải qua kiểm tra người lạ”. Cần một lượt thật trên đúngSHA; hiện CK. Không yêu cầu tạoF5 để đáp ứng — **P12/C34/L072:89** “Không voice… trước khi chốt”, kể cả thử. Tai/stranger không được suy từ150từ/469checks.
- Fact/trend main đãscopedPASS; không lặp requestsource mới. Mạch23→24→25 vẫn là chỗ cầntai; không tựkết luận trượt vì contextkhôngcausal.

### B. Gate trước trình/xinChốt đầy đủ — nguồn thật bắt buộc
- **R35:79** “Storyboard trước khi duyệt script…1 frame1080×1920…kèmcontactsheet…gửi cùngscript”; **R34:78** tựxem/sửa ít nhất2vòng; **R54:183** “bản render nháp của cover phải có trong gói gate1”; **C80/C90** còn3hướngcover+grid. Vì vậy preview không phải bước chỉsaurenderfinal. B2/107 xác nhận chưaảnh; **FAIL đủgóigate1**, không gọiBMarkdown=screenshot. Nếu Hiệp chỉduyệt lời táchảnh thì phải gọi rõ phạmvi đó/ngoại lệ quytrình, không tựwaive nguồn.
- **R48:139**: “lỗi(✖) thì không gửi Hiệp duyệt và không renderfinal”; **L090:180** checkerlookuprepo; **R59:244** “Mọiassetdựán…trongrepo…Khônglưuởthưmục riêng trênbox”; **R65:234** canonicalstorage. Registry✖ và scratchstorage vẫn **FAIL trước fullgate1**, dù SocialprovenancePASS. Không biến thành sourcecontentfail hoặc cấm chuẩnbị. Luồngsanctioned archive dođiềuphối; không bypass/đổiID/checker.
- **W04/C108** bảntrình đủ9cột; B10–18 có7beats nhưng khôngendcard trong cùng bảng này (endcard có riêng B31/45–49/88–97). Trước trình gộp đúngbảntrình gồmendcardtheoC108; không đòisửa mainMD byte-lock hay lời. Fileplan chi tiếtđủkhôngthaytintrình.

### C. Triểnkhai/QA production — không làm blocker lời mới
- **R45:114** validateplan “trước khi render”; **R46:124–127** timing/prosody/STT theoaudio; **R26:62** caption theo thời lượng TTS; **R48:138** “gate1…→render→check-rules --final + soátframe+STT→gate2”. Engineproduction/schema/HFlint/realcue/miệngenvelope/mix/LUFS/finalpost/platform là **NA/CK sauChốt**, không yêu cầu thực hiện nay đểduyệtwording.
- Adapter label/nullstrike/covertransform và font/wrap/geometry có hai phần: **phải đủ triểnkhai cho staticpreview trước gate1** nếu giữquytrình; phầnvideo/realcaptionresnap/frameactual sauChốt. Không gọi enginepass nhờbbox, cũng không bắt hoànthành toànvideoengine mới đượcchốtlời.
- Nhãnprovenance đọcđược, title/coverfit và endcardreadability: staticpreview kiểmmộtphần trướcgate1; **đọcđược trong3s thật**, syncrealvoice/captions và finaldelivery saudựng. B89 nói3sước chưađo; không bắt audio/rendertrướcChốt đểthửURLreadability. Khôngtựpassrealreadability từfont/bbox.

## 5. Các bước nhỏ nhất hữu hạn theo vai
1. **OC/Reviewer:** hoàn tất một lượt đọcto/one-listen và người lạ trên lờiSHAgiữnguyên; khôngoutline/research/viếtlạinếukhônglỗithật. Nguồnmain đãđóngscope, khôngrequestlạiDeep/Social vì visualupdate.
2. **OC/visual:** đóng hai conflictR16title/R54cover theo đúngnguồn; no-strikegiữthì xin đúngngoạilệcoverhẹp, khôngphát minhwaiver. Sau đó mapping/ảnhpreview theoquyềnđượcgiao; lượt này khôngtạoảnh. GiữRentbổsungphầnkể, utilitylabels và disclosureconditional.
3. **News/điềuphối:** sanctionedregistry/archive+runchínhchecker sauđồngbộ; chuẩn bịbảntrình9cột cóendcardvàgóipreview. Khôngsửa ID/code nécheck. Việc này songsong, khôngkhóa hếtchuẩnbịnộidung.
4. **SauHiệpChốt đúngphạmvi:** voice/render/engineQA/STT/timing/mix/post nhưR48. Khôngaiđượcnhận report này là lệnhthực hiện haychứngnhậnảnh/audio.

Không sửa gì ngoài report và independentchecks scratch. Không mở lại lựa chọnC, khôngcallbackblocker, khôngcountpatch3, khôngkếthừa469checks thành PASSngườixem.
