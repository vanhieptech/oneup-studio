---
title: "clip-05 archive: clip05-r11.4-plan-update2-rule-review-2026-11-07"
date: 2026-11-07
type: review
tags: [clip-05, r11, archive]
status: archived
source: "/workspace/clip05-r11.4-plan-update2-rule-review-2026-11-07.md (archived as-is in commit 0d569da; author Rule Reviewer)"
---
# Clip05 r11.4 plan-update2 — Rule Reviewer delta
07/11/2026, Asia/Saigon. Chỉ đọc/soát, ghi scratch; không sửa lời/spec/code/repo, tin nhắn, nghiên cứu nguồn, ảnh/audio/render.

## Verdict
**Hai conflict R16/R54 của update1 đã sửa ở mức grammar và nghĩa đề xuất trên plan. Không thấy fault mới buộc sửa lời hay đòi outline/rewrite. Không phải patch3.** Đủ tiếp tục gate còn thật; chưa phải toàn gói gate1 PASS. Nghĩa cover trên chữ giảm đúng nguy cơ phủ định bare rereading; không chứng nhận ảnh/ONLY-readability hay thay Deep xác nhận fact mới.

## Identity độc lập
D `/workspace/opencreator-clip05-script-r11.4-draft-2026-11-07.md`: **dc42247775b8fdd0d6c5a6958e074a829e899f431efcc826516f61e21c53dd0e** bất biến.
J `/workspace/opencreator-clip05-spec-r11.4-plan-update2-2026-11-07.json`: **325f53b2f114ceb3ec255f627f04018c45b3b7e45a1136f7e55540677b309182** đúng expected.
B `/workspace/opencreator-clip05-storyboard-r11.4-plan-update2-2026-11-07.md`: **2d78cd305e408c10b5db580d23fbb7a48b93851524d68280c5d12f0742c9ef28** đúng report.
Independentchecks `/workspace/clip05-r11.4-plan-update2-reviewer-checks-2026-11-07.txt`: D23–29==J7beats;150=[24,18,21,11,28,27,21];50trướcmethod;23caption bindings nguyên dict so update1; end_card và mock_comparison_plan nguyên dict. Không chạy492check writer làm bằngchứng semantic, không chạy engine/checkfinal/TTS lênplanning_only.

## 1. Luật actual trên đĩa và delta
Nguồn `/workspace/oneup-studio/rules/video-rules.md` đọc lại exact lines bằng rg, không chỉ dựa reportwriter:
- **R16:41:** “caption và tiêu đề chỉ tiếng Anh… Ngoại lệ: bubble thoại và hộp dẫn chuyện trong beat comic… viết tiếng Việt”.
- **R54:181:** “hero 2–4 chữ (chữ thói quen cũ bị gạch → chữ mới trong pill ink)”, CoverdirectionA, tagseries+sốtập, chibi/logo/theme/safezone290–1600.

|Mục|Actualrefs|Kết luận|
|---|---|---|
|HFtitle/header|J4595/4639/4661; B38/40–41/95: COMPARE YOUR RETELLING / SOURCE PAGE / YOUR RETELLING|**PASS planR16**: English, đúng hai đối tượng đối chiếu. Không còn titleHFViệt được gọi né thành object. ProvenancelabelVI riêng B37/39 vẫn khác title/caption; không áp English-only lên toàncredit/mock. Glyph/ảnh CK.|
|Oldhabit→newpill|J1534–1548/1570–1575/4350–4377; B7/85/89–94: REREAD ONLY→SELF-TEST, strike0/accent1|**PASS grammarR54 ở mô tảplan**: oldhabit là chỉ dựa đọc lại, toàncụm bịgạch; newpracticepill;3herowords trong2–4. Không cần ngoại lệ no-strike nhưupdate1. Grammar không bắt oldhabit phải baretêntechnique, không tựthay bằng misconception trừutượng. Actualtemplate/ảnh CK.|
|Ý nghĩa phủ định|J1573–1574; B85–87: ONLY cùngstring/font126/hàng/gạch; LOW/HIGHUTILITYseries|**PASS conditional plansemantic**, xem mục2. Không nói img/factgate tổng PASS.|
|Geometry|B90–93; J1586/4381–4409: hero+14px, strikeleft70 thay native56; rig[-40,-70],bbox[350,930,660,660]|**PASS declaredarithmetic** trong strict60–1020/290–1600. Heroreserve[60,420,960,380], old[70,420,940,140], pill[80,568,910,180]; kếtthúc≤1020/800. **CK adapter/raster**: chưaimplement, khôngenginepass.|
|Minh họa/payoff|B16–17/37/39/44–45/51–53; Jmockmodelunchanged|**PASS preservedlogic**: sourceFood+Rent bấtbiến; sourceRent uncover, chỉ objectretellingRent append ởphầnkể. Nhãnbiêntập hiện trongplan. Khôngfinancialadvice/realperformancepromise. Visibility/realcue CK.|
|AIconditional/endcard|B19/46–50/97–106; Jendcardidenticalupdate1|**PASS preservedconsistency**: row5/togglechỉactualAIvoice=true; khôngcógiọnghiệnnay; khôngthêmcaption/lời. Readability3s/actualbranch/post CK.|
|Full9columnfile|B10–19 có7beats+endcard|**PASS file-completeness delta**: endcard nay đã trong bảngchung, sửa thiếu ởupdate1. Actualbảntrìnhvàpreview CK.|

## 2. Coversemantic — không bắt nguồn mới, không fake visualpass
Deep `/workspace/clip05-r11.4-factcheck-2026-11-07.md`:32 PASS main;34/57/67 giới hạn cover không được phát nghĩa “đọc lại vô dụng”, chỉ utilitythấp/cao;45–47 là review10kỹthuật, khôngtrialđơnlẻ/điểmđotrựctiếp. Report này không xác nhận coverupdate2 đãđượcDeepduyệt.

**Qualifier ONLY là sửa nghĩa thật trênplan**, khôngnote nhỏ chữa disclaimer: nguyênstring REREAD ONLY được gạch, cùngfont/cùnghàng/cùngblock B85; phủđịnh oldhabitđộctôn cáchđọc lại chứ không xóabảnthân đọc lại. PillSELF-TEST là lựa chọnkhuyếnnghị đãcótrong main. Vì vậy không còn căn cứ tựbáo “bareREREAD bịphủđịnh” nhưupdate1/covergốc, cũng không buộc ngoại lệR54.

LOW/HIGHUTILITY là nhãnnhómhữuích, khôngsốđo hoặc lời “REREAD ONLY đãđượcthửnghiệmvớiSELF-TEST”. Nhãnserieskhông được nângthành measuredscore hoặc causereadonly→forgetting; currentJ1574/B86 nói rõ category/editorialhabit. Không gánkhángiả/texthipparticipants cóoldhabitnày. Khôngphủđịnhđọcvui/pilsa. **Không xác định claimfactmới vượtlock cần nghiêncứu mới.** Giữsourceowners: mainDeep/SocialscopedPASS đúngD_SHA; nếuDeep còn phải đóng coverinterpretation theo phâ nvai thì chỉ xem coverfields/hashmới, khôngkiểmlạilờibytegiữnguyên hay đòitrialriêng reread-only.

**Visualsemantic còn CK trước staticpreview đượcduyệt:** ONLY phải nổi đúngcỡ/khôngcrop/khôngbịstrikecheđếnmấtchữ; LOW/HIGH khôngtrởthành “LOW=NONE”; strikephải bao toànoldphrase, khôngđọng lại bareREREADgạch khi nhìnnhanh. Đây là tiêu chí xácnhậnảnhthiếtkế đãđềxuất, không yêu cầuviếtmẫucovermới. Nếupreview làm mấtONLY thì plansemanticpass không cứu đượcảnh; failảnhđúnglúc, khôngkếtluận trước đãrender sai. Khônglấyseriesnhỏ/disclaimercuốiclip đểchữaảnhsai.

## 3. Gate đúng pha / bước còn hữu hạn
**Trước duyệt lời:** readaloud/one-listen/stranger đúngD_SHA vẫn **CHƯA KIỂM** (B115/121). Nguồn: L089/C170 “đọc to…làm ĐẦU TIÊN”; L091/C172 “nghe một lần là hiểu”; P16/C38/L064 yêu cầu người lạ nói lại câuđầu. Không tựpass từ150words/492checks. Sourceowners đãđóngscope lời; khôngcallback/release04blocker khiactualkhôngclaimrelease(B114).

**Trước trình fullgate1:** preview **chưaảnh**, registry/storage **MỞ/FAILriêng** B116–117. R35:79 “Storyboard trước khi duyệt script…kèmcontactsheet…gửi cùngscript”; R34:78≥2vòngtựsoát; R54:183 covernháp cótronggate1; C90 thêm3cover/grid. Adapterhero+14/rig−40−70 cầnthực hiện đủ staticpreview khiđượcphép; khôngJSONbbox=ảnh. R48:139 còn✖khôngtrình; R59:244/R65:234 registry/archivecanonical qua luồngsanctioned, khôngbypass/đổiID/checker. Đây khôngsourcepainfail và khôngcấm songsong chuẩnbị. Bảngfileđãđủendcard, khôngcòn lỗi thiếucộtendcardcũ.

**SauChốt:** F5/realwordtiming/STT/prosody/actualcaption-hitresnap/HF/videoengine/render/mix/finalpost/platformQA. R48:138 gate1→render→finalchecks/STT→gate2; R45:114 validate trước khi render; R46:124–127 giọng/timing/STT. Không biến nhữngbước này thành điều kiệnwordingphảiđạtngay. Staticfont/coverwrap/labelvisibility kiểmđểduyệtpreview; realreadability3s và video/audioQA sauproduction, khôngbịađãđo. planning_only=true/renderable=false không phải enginefail.

**Nextsmallest theo vai:**
1. OC/Reviewer thực hiện1lượtkiểmlời/ngườilạ cònthiếu, khôngoutline/newconcept/patchwordingnếukhônglỗithật.
2. Visual/production triểnkhaistaticadapter đãchỉđịnh và duyệtảnhONLY/cropping/headers/label/covergrid2vòng khiđượcphép; Deepchỉđóngnghĩacovermới nếuvaiownercần, khôngresearchmới/khôngrecheckmainlặp.
3. News/điềuphối xửlýsanctionedregistry/storage vàrerunlookup, songsongvớipreview. Giữfailuremáyđúngscope, khôngallgreenclaim.
4. SauChốtđúngphạmvi mớivoice/render/productionQA. Reportkhônglàlệnhthực hiện.

Không còn lỗi grammarR16/R54 ở đềxuất này phải trảthêmmộtvònglờimới. **Delta plan được chấpnhận để đi tiếp; fullgate1 và visualreadability vẫn chưađóng.**
