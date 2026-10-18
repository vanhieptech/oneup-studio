---
title: "Doodle style research — học cách người ta làm, chốt ý tưởng trước khi render"
date: 2026-10-18
type: reference
tags: [doodle, whiteboard, motion, remotion, hi-oneup]
status: awaiting-hiep-pick
source: "web research 2026-10-18 (links đã fetch/verify, ghi rõ ở từng mục) + anidoodle vendored + 3 demo bị chê"
id: research.doodle-style
updated: 2026-10-18
---

# Doodle style research — đưa ý tưởng trước, Hiệp chọn mới làm

> **Bối cảnh:** Hiệp đã chê 3 demo doodle (`doodle-demo2` 7 nét trên giấy trơn, `doodle-demo-brand` khoanh/gạch lên khung comic, `doodle-creative-demo` khối→bậc thang người que, `doodle-assets-demo` tick/nối chip trên asset có sẵn) là "xấu / không liên quan / vẽ theo khung có sẵn". Yêu cầu vòng này: **chỉ nghiên cứu, không render, không sửa engine.** File này là danh sách ý tưởng để Hiệp chọn 1–2 hướng; bước sau (nếu được chọn) chỉ làm **still frames trước**, Hiệp duyệt mắt rồi mới tính video.
>
> **Brand khóa:** giấy `#F7F7F5`, mực `#111111`, accent duy nhất `#FF5A36`, font Be Vietnam Pro, asset chibi Thầy/Hiệp + props (sign/words/desk/bed/grid/logo/caption) đã có trong `video-engine/`. Mọi ý tưởng dưới đây đều phải sống được trong brand này — không bê nguyên style ngoài vào.

## 0. Nguồn đã verify (fetch thật ngày 18/10/2026)

| Nguồn | Link đã fetch | Lấy được gì |
|---|---|---|
| RSA Animate (RSA chính thức) | https://www.thersa.org/videos/rsa-animate-changing-paradigms/ | Video mẫu gốc "Changing Paradigms" (Ken Robinson, 14/10/2010) — chuẩn whiteboard draw-on theo lời nói |
| MediaScaleUp — Whiteboard-Style Animation, Done Properly | https://mediascaleup.com/post/whiteboard-style-animation-done-properly-motion | Case study đầy đủ nhất: script khóa trước, vẽ bắt đầu trước keyword 0,3–0,5s, 1 accent, 5–7 element/board, no-hand + pen-tip cursor |
| Adobe — What is whiteboard animation | https://www.adobe.com/creativecloud/video/discover/whiteboard-animation.html | 1 hình/câu ("không 3 hình 1 câu, không 1 hình 1 đoạn"), không shading kiểu truyền thống, storyboard trước |
| AsapSCIENCE (Creator Handbook) | https://www.creatorhandbook.net/how-to-make-fun-educational-content-with-asapscience/ | Quy trình script→storyboard→vẽ marker trên whiteboard→VO riêng→edit sync; hình cartoony simplistic |
| Speedpaint — Duration / Color Fill / Hand Style | https://speedpaint.io/blog/whiteboard-video-settings-duration-color-hand | Fill là "payoff moment" (contour wipe 1–2s), no-hand = designed/premium nhất, hand lớn che hình khi hình dày |
| Kurzgesagt — What we do | https://kurzgesagt.org/what-we-do?visit=videos | "Deliberating over the best visual metaphors for each scene" ở khâu sketch; VO là timing cho animation; nhân vật quirky/relatable |
| Pexo — How to Make a Doodle Explainer Video (2026) | https://pexo.ai/tutorial/how-to-make-a-doodle-explainer-video | Doodle ≠ whiteboard: doodle hiện theo nhịp (không vẽ từng nét), 1 accent trên monochrome, 9:16 phải vẽ lại bố cục dọc chứ không crop, "1 element vẽ kỹ giữa đám nguệch ngoạc phá vỡ toàn bộ" |
| Rough.js | https://roughjs.com/ | Thư viện SVG sketchy: `roughness`, `bowing`, `seed`, fill `hachure/cross-hatch/dots/solid` — copy được nguyên lý vào Remotion/SVG của mình |

Nguồn phụ qua search (chưa fetch sâu, chỉ để biết tồn tại): MinutePhysics (stick figure + shape tối giản, vẽ sync VO), kênh TikTok VN "Vẽ Kể Chuyện" (tranh vẽ tay + giọng kể, >1M follower — chứng minh format vẽ+kể sống tốt ở VN, nhưng là tranh tĩnh kể chuyện, không phải draw-on sync), TikTok `@fawziammache` (100% hand-drawn AI explainer, 881K view — doodle dọc chạy được).

## 1. Bảy ý tưởng

### Ý tưởng 1 — "Bảng lớn, camera đi dạo" (RSA Continuous Canvas)

- **Ngữ pháp hình:** Tất cả các beat nằm trên **một mặt giấy lớn duy nhất** (to hơn khung 9:16 nhiều lần). Camera pan/zoom dọc theo giấy: đang ở góc "phòng bừa" thì trượt xuống góc "3 việc nhỏ", zoom vào chi tiết khi nói tới, zoom ra thấy toàn cảnh ở câu chốt. Không cắt cảnh cứng — người xem luôn biết mình đang ở đâu trên bảng. Đây là cách RSA Animate + anidoodle `motion-grammar.md` mechanism #5 "Continuous canvas" làm: "All the scenes live in one layout bigger than the frame, and the camera travels between them".
- **Tham chiếu:** https://www.thersa.org/videos/rsa-animate-changing-paradigms/ · https://mediascaleup.com/post/whiteboard-style-animation-done-properly-motion (mục camera moves: slide right to clean area, push in on detail, tránh wipe mỗi cảnh)
- **Hợp OneUp không:** Hợp một nửa. Giấy + mực + accent là đúng brand; Thầy chibi đặt ở "trạm" đầu bảng làm người dẫn. **Không hợp:** 9:16 dọc thì canvas lớn dễ thành chữ/hình nhỏ xíu khi zoom out; caption plate + logo cố định của mình sẽ va với camera di chuyển. Phải thiết kế canvas theo chiều dọc (đi xuống, không đi ngang).
- **Effort:** Cao — cần hệ camera canvas trong Remotion + layout lại toàn bộ beat trên một board.
- **Ví dụ clip-03:** Mở đầu camera ở ô "DỌN PHÒNG — cuối tuần làm" (tờ note to), trượt xuống thấy nó nằm đó qua 52 tuần (52 vạch nhỏ), trượt tiếp tới chỗ tờ note bị xé thành 3 mảnh nhỏ xếp dọc, zoom vào mảnh 1 "dọn ghế 15'".

### Ý tưởng 2 — "Một câu, một hình nguệch" (AsapSCIENCE / MinutePhysics)

- **Ngữ pháp hình:** Mỗi câu thoại = **đúng một hình doodle đơn giản** (người que/chibi mini, 1 vật, 1 biểu đồ 3 cột), vẽ nhanh trong lúc câu đang được nói, xong là dừng — hình sau đè/xóa hình trước. Không trang trí, không nền chi tiết; hình nào cũng đọc được trong 1 giây. Adobe gọi đây là nhịp "one symbol per sentence"; AsapSCIENCE làm y hệt bằng marker thật: hình cartoony, nguệch, nhưng **cùng một tay vẽ** nên nhìn có chủ ý.
- **Tham chiếu:** https://www.creatorhandbook.net/how-to-make-fun-educational-content-with-asapscience/ · https://www.adobe.com/creativecloud/video/discover/whiteboard-animation.html
- **Hợp OneUp không:** **Rất hợp về nhịp** (clip của mình 50–85s, mỗi beat 1 ý — đúng cấu trúc này), nhưng phải thay người que bằng **chibi Thầy mini vẽ tay** (đầu tròn + tóc đen + má hồng, nét mực) để không rời brand. Nguy cơ: nếu chibi mini vẽ tay xấu hơn asset chibi xịn, lại bị chê "vẽ lại cái đã có".
- **Effort:** Trung bình — cần bộ chibi-mini + ~15 icon doodle vẽ theo 1 style-sheet (cùng stroke, cùng mức nguệch), tái dùng mọi clip sau.
- **Ví dụ clip-03:** "Nhìn mỗi cái tên việc, mình hay nghĩ chút xíu là xong" → vẽ đồng hồ cát nhỏ xíu; "ghi ra từng bước nhỏ, mình mới thấy nó đâu có ít" → cùng cái đồng hồ **phình ra** đầy cát. Một hình, biến đổi ngay tại chỗ.

### Ý tưởng 3 — "Biến hình" (Morph — Kurzgesagt-adjacent + anidoodle handoff)

- **Ngữ pháp hình:** Không vẽ hình mới, không xóa hình cũ: **hình A biến thành hình B ngay trước mắt** — khối việc to nứt ra thành 4 khối nhỏ, 4 khối tự xếp thành bậc thang, bậc thang gập lại thành tờ checklist. Kurzgesagt gọi khâu này là chọn "visual metaphor" rồi animate có chủ đích ("movement should clarify the concept, not decorate it"); anidoodle có sẵn cơ chế `morph.ts handoff({from,to})`: hình đi, giãn nhẹ giữa đường, thành hình đích và đáp đúng vị trí (lệch ≤2px). Người xem **thấy** "chia nhỏ" xảy ra, không cần ai giải thích bằng chữ.
- **Tham chiếu:** https://kurzgesagt.org/what-we-do?visit=videos · file nội bộ `resources/refs/anidoodle/skills/anidoodle/references/motion-grammar.md` (mechanism #2/#4)
- **Hợp OneUp không:** **Hợp nhất về ý nghĩa** — series của mình toàn ẩn dụ "to→nhỏ, rối→gọn, nặng→nhẹ", morph là cách kể ẩn dụ mạnh nhất mà vẫn giữ giấy/mực/accent. Dùng được asset có sẵn làm hình A/B (sign DỌN PHÒNG morph thành 3 chip việc). **Không hợp:** morph giữa 2 asset bitmap chibi là khó; morph chỉ nên làm giữa hình vector đơn giản (khối, tờ giấy, sợi dây, biểu đồ).
- **Effort:** Trung bình–cao — engine đã có `translateKeyframes/hop` thử nghiệm ở creative demo nhưng chưa có morph path thật; cần làm morph cho shape đơn giản trước.
- **Ví dụ clip-03:** Tờ note "DỌN PHÒNG" (hình A) tự gấp/nứt thành 3 tờ note nhỏ "dọn ghế · lau bàn · đổ rác" (hình B) đúng lúc câu "thay vì ghi dọn phòng, mình ghi ra ba việc" — không tick, không khoanh, chính tờ giấy biến hình.

### Ý tưởng 4 — "Marker comic tô màu phẳng" (anidoodle koiDraw — style đáng copy nhất trong 32 style)

- **Ngữ pháp hình:** Học đúng quy trình anidoodle `koiDraw`: phác nhẹ → **tô màu phẳng (flat cel fill) từng mảng** → bóng cứng (hard shadow) → **nét contour đậm vẽ CUỐI CÙNG**, mỗi nét lớn dần theo centreline. Kết quả không phải "đường viền trống rỗng" như demo của mình, mà là hình **có thịt**: có màu, có bóng, nhìn đã hoàn thiện. Trong 32 style của anidoodle, đây là style gần brand mình nhất (marker comic, màu phẳng, contour đậm) — hai style đáng copy còn lại là *ballpoint sketch* (chỉ 1 màu mực, tone bằng hatching — hợp beat nghiên cứu/bằng chứng) và *blueprint drafting lettering* (chữ viết tay kỹ thuật cho label/số liệu).
- **Tham chiếu:** file nội bộ `resources/refs/anidoodle/skills/anidoodle/references/styles.md` (9 hands, mục 2 Marker comic) + `styles/koiDraw.md`, `styles/pocketWatchDraw.md` · nguyên lý fill payoff: https://speedpaint.io/blog/whiteboard-video-settings-duration-color-hand
- **Hợp OneUp không:** Hợp về đích đến (chibi của mình vốn là flat fill + contour đậm — cùng họ), **không hợp nếu bê cả palette koi** (phải dịch sang giấy/mực/accent + màu chibi sẵn có). Đây thực chất là "nâng cấp nét doodle của mình lên chuẩn marker", không phải style mới hoàn toàn.
- **Effort:** Trung bình — thêm fill-fade/contour-wipe vào doodle system + quy ước thứ tự "fill trước, contour sau"; không cần engine mới.
- **Ví dụ clip-03:** Vẽ phòng bừa: contour bàn/ghế hiện → tô phẳng đống đồ (mảng xám) → contour đậm đóng lại; nói "làm xong một việc" thì mảng màu của việc đó **tô accent** như quẹt marker — màu là payoff, không phải tick rời.

### Ý tưởng 5 — "Sổ tay bút bi" (Ballpoint / Blueprint cho beat bằng chứng)

- **Ngữ pháp hình:** Riêng các beat nghiên cứu (b04 Kruger & Evans, b05 Steel) đổi sang giọng hình "ghi chép nghiêm túc": **một màu mực, nét đều như bút bi, tone bằng gạch hatching, label viết tay kiểu drafting** (anidoodle `pocketWatchDraw`: "tone comes only from WHERE hatching sits", chữ `drafting.ts` viết từng nét). Nhìn như trang sổ tay của người đi học thật — phân biệt rõ "đoạn này là bằng chứng" với đoạn kể chuyện.
- **Tham chiếu:** file nội bộ `resources/refs/anidoodle/skills/anidoodle/references/styles/pocketWatchDraw.md` + `styles.md` mục "explainer → chalkboard, blueprint, ballpoint with drafted labels"
- **Hợp OneUp không:** Hợp beat bằng chứng (series mình hay bị chê "bằng chứng chung chung" — hình sổ tay giúp câu nghiên cứu có trọng lượng), **không hợp làm style toàn clip** (lạnh, ít cảm xúc, xa chibi). Chỉ dùng 10–15s/clip.
- **Effort:** Thấp–trung bình — 1 màu mực sẵn có, cần thêm hatching fill + font label giả viết tay (hoặc Be Vietnam Pro nghiêng nhẹ, tránh font ngoài).
- **Ví dụ clip-03:** b04: sổ tay ghi "Kruger & Evans" → biểu đồ 2 cột gạch hatching: cột "nghĩ: chút xíu" thấp, cột "ghi ra: cả buổi" cao — số/hình hiện đúng lúc nói "thấy nó đâu có ít".

### Ý tưởng 6 — "Hook vẽ ngay frame 0" (TikTok/Shorts doodle dọc)

- **Ngữ pháp hình:** Học short-form: **3 giây đầu đã có hình đang được vẽ dở** (chưa xong nên phải xem tiếp), chữ hook là chữ viết tay to chiếm 1/3 khung dọc, mỗi hình hiện theo **nhịp beat** chứ không vẽ rề rà từng nét (Pexo: doodle "appear in a beat rather than being drawn out stroke by stroke", và 9:16 phải **vẽ lại bố cục cho khung dọc**, không crop ngang). Caption vẫn chạy dưới, nhưng hình hook nằm vùng trên — đúng layout dọc của mình.
- **Tham chiếu:** https://pexo.ai/tutorial/how-to-make-a-doodle-explainer-video (mục Step 5/6 + 5 mistakes) · https://mediascaleup.com/post/whiteboard-style-animation-done-properly-motion (reveal bắt đầu trước keyword 0,3–0,5s)
- **Hợp OneUp không:** **Rất hợp format** (mình chỉ làm TikTok dọc, hook 3s là luật sống còn — rule-55), và không đòi style mới: chỉ đổi **nhịp + bố cục dọc** của doodle hiện có. Không hợp nếu lạm dụng: cả clip mà beat nào cũng "pop" nhanh thì mất cảm giác vẽ tay.
- **Effort:** Thấp — chủ yếu là quy ước timing/bố cục + template hook; engine gần như đủ.
- **Ví dụ clip-03:** Frame 0: tờ note "CUỐI TUẦN LÀM" đang được viết dở chữ "CUỐI TU…" + móc treo vẽ xong; chữ hook hỏi "việc gì để cả năm chưa làm?" — người xem chờ chữ viết xong thì đã qua 3s.

### Ý tưởng 7 — "Sợi mực đi xuyên clip" (Persistent actor — anidoodle ink drop)

- **Ngữ pháp hình:** Một **sợi dây/sợi mực cam duy nhất** xuất hiện từ beat đầu và **đi xuyên suốt clip**: nó là sợi dây treo tờ note, bị cắt, rơi xuống thành đường nối 3 việc nhỏ, uốn thành bậc thang, cuối clip cột lại thành dấu tick. Anidoodle gọi đây là mechanism #2 "Persistent actor": một vật giữ nguyên danh tính qua mọi cảnh, cảnh thay quanh nó — đó là thứ biến các beat rời thành **một câu chuyện**. Khác hẳn demo assets cũ (tick/nối chip trang trí): ở đây sợi mực **là nhân vật chính**, asset chibi chỉ diễn quanh nó.
- **Tham chiếu:** file nội bộ `resources/refs/anidoodle/skills/anidoodle/references/motion-grammar.md` (mechanism #2, `motif.ts`: cùng vị trí/kích thước 2 phía seam, lệch ≤2px) · https://speedpaint.io/blog/whiteboard-video-settings-duration-color-hand (no-hand + pen-tip dẫn mắt)
- **Hợp OneUp không:** Hợp vì accent `#FF5A36` làm sợi mực là đúng vai "màu = thông tin" (MediaScaleUp: accent chỉ cho thứ đang được nói tới); sợi dây cũng đã có trong concept clip-03 (Thầy cắt dây ở b06). **Không hợp:** đòi hỏi kỷ luật tuyệt đối — sợi mực xuất hiện mà không làm gì ở beat nào là thành trang trí ngay (anidoodle cảnh báo đúng câu này).
- **Effort:** Trung bình — path animation đã có (`doodle-path`), cần thiết kế "kịch bản cho sợi dây" theo từng beat + giữ liên tục giữa cảnh.
- **Ví dụ clip-03:** b01 sợi cam treo note "CUỐI TUẦN LÀM" → b06 Thầy cắt, sợi rơi → b07 sợi tự nối 3 chip việc thành đường đi → b10 sợi cột thành nút, note rớt khỏi móc (callback frame đầu).

## 2. Chẩn đoán: vì sao 3 demo của mình xấu

Đối chiếu frame thật của 3 demo (`doodle-demo-brand-frame*.png`, `doodle-creative-frame*.png`, `doodle-assets-frame*.png` ở `/workspace/`) với chuẩn trên:

| # | Điểm xấu cụ thể | Demo nào | Chuẩn người ta | Cách sửa (khi được làm) |
|---|---|---|---|---|
| 1 | **Hình quá nhỏ, giấy quá trống.** Hình vẽ nằm giữa khung, chiếm <20% chiều ngang; trên/dưới là giấy chấm mênh mông. Nhìn như slide lỗi, không như video dọc. | creative (4 ô vuông bé giữa biển chấm), brand | MediaScaleUp: board 5–7 element nhưng **phủ khung**; Pexo: 9:16 vẽ lại bố cục dọc. RSA zoom vào chi tiết đang nói. | Mọi drawing phải chiếm ≥60% bề ngang khung dọc; bỏ nền chấm thưa hoặc dùng nền cảnh thật (desk/bed); zoom/camera vào hình khi nó là nhân vật chính. |
| 2 | **Nét không có "tay".** Nét đều tăm tắp như vector CAD hoặc rung đều như filter; không taper (đầu nét to-nhỏ theo lực bút), không retrace, contour không đậm hơn nét phụ. Trộn với chibi flat-fill xịn đặt cạnh → doodle trông như đồ giả dán lên. | cả 3 | anidoodle: `Medium {nib, taper, pressure, retrace, wobble}` là nửa style; MediaScaleUp: 1 stroke weight chính + phụ = ½, bo tròn đầu nét như marker. Pexo: "loose nhưng **đều** loose — 1 element vẽ kỹ giữa đám nguệch là phá vỡ". | Khóa 1 style-sheet nét: weight chính/phụ, taper 2 đầu, jitter theo seed nhưng **không rung đều**; mọi doodle cùng 1 "tay", không trộn nét CAD sạch với nét rung. |
| 3 | **Không có tô màu/bóng — hình "chưa xong".** Creative chỉ có viền trống; assets thì tick cam rời rạc. Người xem thấy phác thảo dở dang suốt 9–13s, không có khoảnh khắc "xong". | creative, demo2 | Speedpaint: color fill là **payoff moment** (contour wipe 1–2s); anidoodle koi: fill phẳng → bóng cứng → contour cuối. AsapSCIENCE marker luôn tô mảng màu. | Mọi hình chính phải có đích đến: tô phẳng (giấy/xám/accent) sau nét, contour đậm đóng hình. Tick/khoanh chỉ là phụ, không bao giờ là toàn bộ hình. |
| 4 | **Vẽ không khớp lời (demo câm, nhịp tùy tiện).** Các demo không có giọng; nét vẽ chạy theo timer đều đều, không "đáp" vào keyword, không có nhịp dừng sau khi hình xong. Xem vào thấy máy đang trình diễn hiệu ứng. | cả 3 (demo không voice) | MediaScaleUp: reveal bắt đầu **trước keyword 0,3–0,5s**, nhận ra được khi keyword vang lên, hold 0,4–1,0s sau đó. Adobe: 1 hình/câu. | Chỉ đánh giá doodle trên beat **có voice thật**; cue vẽ khóa theo timestamp từ (engine đã có `cue.at`), mỗi hình xong phải có hold; demo sau này bắt buộc lồng đoạn voice tương ứng. |
| 5 | **Doodle không gánh ý — chỉ trang trí/nhắc lại chữ.** Khoanh đúng chữ đã bold, tick đúng việc đã liệt kê: hình không nói thêm được gì ngoài caption. Hiệp chê "không liên quan" là đúng nghĩa đen. | brand, assets | Kurzgesagt: sketch phase là để chọn **visual metaphor**; anidoodle: cơ chế chuyển cảnh phải do câu chuyện đòi, "mascot chỉ đứng xem là trang trí". MediaScaleUp: màu accent = thông tin, không phải trang trí. | Trước khi vẽ hỏi: "bỏ hình này, người xem mất thông tin gì?" — không mất gì thì không vẽ. Doodle chỉ được làm 3 việc: **biến hình (morph), nối nhân-quả, cho thấy tiến triển** — không khoanh lại chữ đã nhấn. |

Thêm một lỗi nền: **không có đầu bút/tay dẫn mắt** — nét tự hiện giữa không trung (cả 3 demo). Người ta hoặc cho tay thật (RSA/AsapSCIENCE), hoặc no-hand nhưng có **pen-tip cursor** ở đầu nét đang chạy (MediaScaleUp/Speedpaint đều khuyên vậy). Mình nên theo no-hand + đầu bút cam nhỏ — hợp brand hơn tay người lạ, và engine làm được ngay.

## 3. Công cụ/kỹ thuật chỉ copy phần làm được trong Remotion/SVG

| Công cụ | Người ta dùng để | Phần copy được cho mình |
|---|---|---|
| VideoScribe / Doodly / Explee | Hand draw-on có sẵn tay + thư viện icon | Chỉ copy **quy ước**: key icon/title vẽ tay, element phụ reveal/fade (VideoScribe entrance animations); không copy tay stock + icon stock (lệch brand ngay) |
| Rough.js | Nét sketchy SVG: `roughness/bowing/seed`, fill hachure/dots | Copy **tham số**: đưa `roughness≈0,8–1,2, bowing nhỏ, seed cố định` + fill hachure vào doodle system của mình thay jitter đều hiện tại |
| GSAP DrawSVG / AE Trim Paths | Reveal nét theo path | Mình đã tương đương bằng strokeDashoffset trong Remotion — giữ, chỉ cần thêm taper bằng 2 nét chồng (dày giữa, mảnh đầu) |
| Procreate Dreams / Rive | Vẽ tay frame-by-frame, interactive | Không copy toolchain; chỉ copy **nguyên tắc**: hình vẽ tay thật vẫn phải storyboard + khóa timing theo VO trước |
| anidoodle (đã vendor) | 32 style + motion grammar 6 cơ chế | Copy có chọn lọc: marker-comic process (Ý tưởng 4), ballpoint/drafting (Ý tưởng 5), morph handoff + persistent actor (Ý tưởng 3/7). Không bê canvas engine (đã quyết L-047) |

## 4. Khuyến nghị: thử 2 hướng này trước

1. **Ý tưởng 3 — Biến hình (Morph).** Lý do: đây là hướng duy nhất trả lời thẳng câu chê "vẽ phải có chủ đích, sáng tạo" — hình tự nó kể chuyện chia-nhỏ mà không cần khoanh/gạch chữ, dùng được asset/vector sẵn có, và khác hẳn cả 3 demo đã bị loại. Nó cũng tái dùng được cho mọi ẩn dụ sau này của series (rối→gọn, nặng→nhẹ, xa→gần).
2. **Ý tưởng 2 — Một câu một hình (AsapSCIENCE nhịp, chibi-mini vẽ tay).** Lý do: rẻ và an toàn nhất để sửa đúng nhịp "1 câu 1 hình + khớp keyword + hold" — lỗi nền của cả 3 demo; bộ icon/chibi-mini làm một lần dùng nhiều clip. Nếu Hiệp thấy chibi-mini vẽ tay không ăn với chibi xịn, hướng này chết sớm ở vòng still — rẻ để biết.

Ý tưởng 7 (sợi mực xuyên clip) là ứng viên số 3: rất hợp clip-03 cụ thể (đã có sợi dây ở b06) nhưng hẹp, khó thành hệ thống cho mọi clip như 3 và 2.

**Bước tiếp theo (chờ Hiệp chọn, chưa làm):** với hướng được chọn, làm **3–5 still frames** (không video, không voice) theo style-sheet nét đã khóa, gửi Hiệp duyệt mắt. Ưng still mới bàn timing/video. Không chọn hướng nào thì dừng ở file này.

## 5. Ngoài phạm vi vòng này

- Không render demo, không sửa `video-engine/`, không đổi L-047/L-048 cho tới khi Hiệp chọn hướng (khi chọn sẽ ghi lesson mới thay cho cách làm cũ).
- Các link TikTok cụ thể (@fawziammache, Vẽ Kể Chuyện) mới ở mức search-result; nếu Hiệp muốn học theo creator nào, vòng sau sẽ fetch/phân tích từng video của creator đó.
