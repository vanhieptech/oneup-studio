# Clip05 r11.4 plan-update2 — R16/R54/Deep mapping
## Phạm vi và identity
Đã đọc FULL /workspace/clip05-r11.4-plan-update1-rule-review-2026-11-07.md và đọc lại FULL /workspace/clip05-r11.4-factcheck-2026-11-07.md; đọc nguyên văn R16/R54 hiện hành và toàn Cover.tsx để rà khả năng mapping thật. Không nghiên cứu nguồn mới.
Script MD giữ nguyên BYTE, cả metadata: SHA trước=sau dc42247775b8fdd0d6c5a6958e074a829e899f431efcc826516f61e21c53dd0e. 7beat/23caption nguyên dict;150từ/50trướcmethod; nhấn/phrases/voice refs/timing estimates không đổi. Old update1 giữ nguyên hash. Không lời mới, không patch3.
## Luật nguyên văn — không waiver
R16 — /workspace/oneup-studio/rules/video-rules.md:41
16. **Chữ chính trên màn hình:** caption và tiêu đề chỉ tiếng Anh, khớp với lời nói, highlight từ khoá. Ngoại lệ: bubble thoại và hộp dẫn chuyện trong beat comic là lời nhân vật nên viết tiếng Việt (giọng luật 41).
R54 — /workspace/oneup-studio/rules/video-rules.md:180–184 (dòng181 quy định grammar)
    - Mọi clip dùng `Cover` direction A (`video-engine/src/composition/Cover.tsx`): tag series + số tập, hero 2–4 chữ (chữ thói quen cũ bị gạch → chữ mới trong pill ink), chibi tạo dáng riêng với biểu cảm mạnh, logo +1, theme theo luật 17, mọi slot nằm trong y 290–1600 (lưới 3:4).
Deep — /workspace/clip05-r11.4-factcheck-2026-11-07.md:34,57,67: “Nếu strike được thể hiện như phủ định tuyệt đối ‘đọc lại vô dụng’, sẽ vượt nguồn”; yêu cầu hiểu utility thấp/cao, không phủ nhận toàn bộ giá trị đọc lại. D45–47 chỉ tổng quan10kỹthuật/high-low grouping, không%/directtrial; main đã scopedPASS. New cover không được tự kế thừa PASS này.
## Hai delta nhỏ nhất
| Conflict | Update1 | Update2 / vị trí | Gate còn thực |
|---|---|---|---|
| R16 HF title/headers | Title/header tiếng Việt ở HF | visual_objects_plan: COMPARE YOUR RETELLING; SOURCE PAGE; YOUR RETELLING, language=en/role HFtitle/columnheading. Mapping b06-e1 giữ nguyên. | Glyph/contrast/ảnh; không dùng nhãn NOTcaption để miễn title rule |
| R54 grammar + Deep | strike=null, đối chiếu utility nhưng bỏ gạch oldhabit | cover: A, hero=[REREAD ONLY, SELF-TEST], strike0, accent1, series LOW/HIGH UTILITY.3hero words. Gạch TOÀN cụm thói quen chỉ đọc lại, kể cả ONLY; không gạch bare REREAD. | Independent semantic review và staticpreview phải kiểm ONLY cùng size/khôngcrop, LOW không bị hiểu NONE; chưa ảnh |
Nhãn MINH HỌA BIÊN TẬP CỦA KÊNH giữ provenance role đã được Reviewer phân biệt với title/caption; không tự tuyên bố mọi text HF là ngoại lệ. Mock source Food+Rent bất biến; Rent append vào phần kể YOUR RETELLING. AI disclosure conditional giữ nguyên, không voice.
R54 cho “chữ thói quen cũ bị gạch”, không bắt oldhabit phải chính tên kỹ thuật đơn lẻ. REREAD ONLY đề xuất thói quen chỉ dựa vào đọc lại khi lựa chọn cách học; đây là lựa chọn biên tập đối chiếu phương pháp hiện có, KHÔNG khẳng định người theo #texthip/nguồn pain/khán giả thực sự có thói quen ấy hoặc vì vậy quên. LOW/HIGH UTILITY gắn với nhóm kỹ thuật theo Dunlosky, không nhận là thử nghiệm riêng REREAD ONLY. Không chê đọc thưởng thức/pilsa; không guarantee.
Đây là mapping để review độc lập, không tự đóng nghĩa hình/Deep/grammar tổng. Không xin Hiệp ngoại lệ, không coi một belief trừu tượng tự nhiên là oldhabit được rule cho phép.
## Feasibility đọc actual source, không engine test
Cover.tsx:11–15 typed hero:string[], strike?:number, accent:number;45–53 tính font và so i===p.strike / i===p.accent, render nguyên w rồi gạch nguyêncomponent.60–71 directionA map từng string thành Word, y420/x66/gap22/base196, series/logo/rig fixed. Vì vậy REREAD ONLY là một block gạch duy nhất, không gạch riêng REREAD rồi thả ONLY thành note.
Native core props tương thích grammar: hero hai string, strike0, accent1. fit heuristic old11chars→126px, new9chars→141px; native nominal heights126/172,gap22→row2y568. Không chạy TypeScript/React/HF/render, không đo glyph.
Nguồn có strike left/right−10: native x66 có thể ra x56, trái strictx60. Plan dịch riêng hero+14px→x80, stroke bắtđầux70. Phần này cần adapter staticpreview, chưa có native prop và chưa implement. Adapter rig−40/−70 cũ cũng chưa implement. Không gọi core grammar native support là mọi geometry đã native.
Hero parent reserve [60,420,960,380] trong strict; oldphrase+stroke reserve[70,420,940,140], newpill[80,568,910,180]. Chỉ nới reserve hero trong strict để chứa stroke, không dời rig/logo/series; rig giữ[350,930,660,660]→1010/1590. Cả LOW/HIGH header và ONLY phải nhìn rõ trong preview, không dùng disclaimer cuối clip cứu cover.
Cover text39characters nếu cộng series+2hero+native #05, hero3words trong2–4. Không đổi font brand; no new asset/doodle/motion. Size/heuristic và reserve không chứng nhận real wrap/crop/ONLY legibility.
## Phương án đã loại — không che conflict bằng adapter
| Phương án | Vì sao loại |
|---|---|
| Title HF tiếng Việt, gọi visual-object/notcaption | Vẫn là title, trái R16:41; chỉ comicbubble/narration được ngoại lệ ấy |
| Null strike / bỏ gạch giữ high-low | Trái grammar bắt buộc R54:181, không chỉ engine support |
| Gạch bare REREAD → SELF-TEST | Có thể phát nghĩa đọc lại vô dụng, trái giới hạn Deep34/57/67; utilitynote nhỏ không tự cứu |
| Gạch một hiểu lầm trừu tượng → utility | R54 chỉ ghi oldhabit, không có câu cho phép thay bằng misconception; không tự tạo waiver |
| GUESS → CHECK | Chèn hành vi cũ không bám main; dễ biến pain thành guess/cause chưa có nguồn |
Mapping hiện chọn là oldhabit có qualifier ONLY, không kỹ thuật bị phủ định. Không phát hiện conflict logic buộc phải xin ngoại lệ ở mức proposal này; nếu Reviewer/preview thấy ONLY không giữ nghĩa độc quyền hoặc mapping không chấp nhận thì ghi đúng vấn đề hẹp, không sửa main hoặc xin waive tự động.
## Validation thực
Final: 492 checks, errors=[]. Scope: identity/text/mapping/declared geometry/rule quotes/source tokens/fit arithmetic. KHÔNG semantic/craft/image/human/engine PASS.
10 input hashes trước/sau không đổi (MD,update1 artifacts/review,Deep,rules,Cover source).7beats/23caption/150/50/ENmax8 giữ nguyên. Cover wholephrase strike/countedhero and ENheading assertions có trong validator. Source simulation nguồn không sửa, chỉ retelling nhận Rent.
Scratch validator có2lỗi harness trước khi chạy xong (thiếu dấu cách else; key path tươngđối/tuyệtđối); đã sửa chính helper ngoàirepo và rerun. Không phải engine/script lỗi, không sửa checker. Final report không dùng các lần exception làm PASS.
Không chạy lại novelty/textchecker trên lời không đổi. Kết quả đúngMD SHA từ r11.4/update1 vẫn giữ: trend registry FAIL; fresh cùngbase FAIL như review đã phân loại, không tự ép rewrite. New visual proposal chưa độc lập review.
## Gate đúng pha
TRƯỚC CHỐT LỜI: đọc to/nghe1lần/người lạ đúng SHA vẫn MỞ; nguồn main đã scopedPASS, không yêu cầu lại Deep/Social cho speech bytekhôngđổi. Không release04blocker vì actual không releaseclaim.
TRƯỚC TRÌNH FULL GATE1: staticpreview/storyboardPNG/contactsheet/cover/grid/hai vòngmắt, thực thi adapter đủ ảnh, registry/sanctioned storage vẫn MỞ. CHƯA CHUẨN BỊ ẢNH; không lấy fileMD/bbox làm preview.
SAU CHỐT: AIvoice nếu dùng, realtiming/STT/prosody/actualcaptions/HF/videoengine/render/mix/finalpost/platformQA; không dùng thiếu các bước hậu kỳ làm blocker wording mới. Không thực hiện chúng ở lượt này.
Planning_only=true/renderable=false/locked=false; timing tất cả ƯỚC. Không tự PASS/Chốt. Không repo/commit/push/messages/images/audio/render.
## Deliverables
- /workspace/opencreator-clip05-spec-r11.4-plan-update2-2026-11-07.json SHA256 325f53b2f114ceb3ec255f627f04018c45b3b7e45a1136f7e55540677b309182
- /workspace/opencreator-clip05-storyboard-r11.4-plan-update2-2026-11-07.md SHA256 2d78cd305e408c10b5db580d23fbb7a48b93851524d68280c5d12f0742c9ef28
- /workspace/clip05-r11.4-plan-update2-validation-2026-11-07.json SHA256 893cc4843ecf8ec42abf069170c3b87961ad3ce0b268c81f4cb0b0461f9cbec5
- /workspace/clip05-r11.4-plan-update2-manifest-2026-11-07.json
