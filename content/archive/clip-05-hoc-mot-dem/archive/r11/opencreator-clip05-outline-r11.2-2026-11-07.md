---
title: "Clip05 r11.2 — thiết kế lại outline và điểm dừng thật"
date: 2026-11-07
type: outline
status: blocked-at-outline-not-a-script
source: "Các gói Social/Deep được giao và review r11.1; không nghiên cứu ngoài"
tags: [clip05, direction-C, outline, flow, conflict]
---

# Kết quả trước khi viết lời

**Chưa chọn được outline đáp ứng đồng thời độ tự nhiên và các điều kiện còn hiệu lực. Dừng trước bản thoại đầy đủ, không làm một r11.1 đổi đạo cụ.** Đây là đánh giá thiết kế của người viết, KHÔNG phải verdict thay Rule Reviewer; cũng KHÔNG kết luận hướng C tự thân bất khả thi.

Không thay trend, không hỏi chọn lại C. Không sửa repo/checker/metadata, không gửi ai, không voice/render/images. Chỉ tạo hồ sơ ngoài repo theo phạm vi được giao. Không có lời thoại r11.2 nên số từ thoại = **0**, không chạy checker trên outline để tạo PASS giả. Đọc to/người lạ/nghe-một-lần/timing = **CHƯA KIỂM**.

## 1. Đã đọc gì, thông tin nào đang có hiệu lực

- Đọc đầy đủ review r11.1 (204 dòng nội dung), checker r11.1, script r11.1, prep-template r2 và concept-prep 07/11; đọc factcheck r11 để hiểu lỗi nguyên nhân/payoff, không lấy fact PASS r11.1 áp sang câu chưa viết.
- Đọc fresh toàn bộ `logs/lessons.md` tới L097, `rules/video-rules.md`, `logs/rule-checklist.md`, `docs/conventions/storage.md`, `AGENTS.md`, `logs/decision-log.md`, `content/voice-profile.md`.
- Load `make-video` và `short-video-script-craft`. Không load motion-picks vì đã dừng ở outline, không chọn effect/motion hay viết section engine.
- Social: `research/trends/2026-11-07-clip05-texthip-bridge-check.md` @bd53fd3. Deep bridge: `research/fact-packages/clip05-texthip-fact-bridge-2026-11-07.md` @d673dd9. Fact nền: `research/fact-packages/factcheck-clip05-lock-2026-11-07.md` @b02dd07. Chủ nguồn/News đã bàn giao là sync trong hội thoại; lượt này không kiểm live GitHub. Không dùng các dòng trạng thái cũ bên trong gói để tuyên bố mất file/chưa sync.
- Đọc `/workspace/clip05-texthip-metadata-2026-11-07.json`: addendum ngoài repo, chưa commit/sync. Giữ nguyên null cho ví dụ đọc-làm-theo, đọc-quên, tự kiểm và bình luận khán giả.
- Ngày nguồn Znews: 05/11/2026 06:00; snapshot Social 07/11/2026 14:07:28, đều **Asia/Saigon (UTC+7)**. Không gọi thời điểm snapshot là ngày cập nhật trang. Ngày Vietnam.vn 04/11 không thay ngày bài gốc.
- Fingerprint nguồn đã đọc: `/workspace/clip05-r11.2-readonly-source-hashes-2026-11-07.json`. Đây là checksum local, không phải chứng nhận commit/sync.

## 2. Chẩn đoán gốc — vì sao hai lần sửa vẫn hỏng

### 2.1 Có hai câu hỏi biên tập khác nhau bị trộn

1. Gói trend trả lời: **đọc sách đang được mô tả như một phần phong cách sống thế nào?**
2. Mục 23.14 trả lời: **nếu muốn nhớ nội dung để dùng, tự kiểm bằng thao tác gì?**

Deep cho phép nối hai câu hỏi bằng một **điều kiện về mục tiêu của người xem**. Deep không cung cấp quan hệ nguyên nhân, không mô tả vấn đề của người theo trend. Nói điều kiện này rõ không có nghĩa câu trend đã thành một bước của câu chuyện.

r11/r11.1 lại đặt một câu hỏi thứ ba lên đầu: **đang thao tác/đang đi đường thì mắc ở đâu?** Câu này đủ để dẫn thẳng tới kiểm nội dung, không cần hiện tượng đọc sách Hàn Quốc. Kết quả: trend không làm thay đổi lựa chọn, trở ngại hay payoff của nhân vật; trở thành một bản tin chen giữa. Chuyển sang bài mua sắm/chi tiêu mà giữ cùng chuỗi ấy chỉ đổi danh từ.

### 2.2 Hai lỗi phải tách, không lấy lỗi này chữa lỗi kia

- **Flow:** câu trend có công việc thật trong câu chuyện không? Không thể chữa bằng metadata, thêm sách/ly trà vào hình, hay thêm “Vậy/Nhưng”.
- **Chứng cứ ví dụ (L090):** có dữ liệu rằng nỗi đau của ví dụ thực sự là của người xem không? Social xác nhận KHÔNG CÓ. Nhãn minh họa cho biết xuất xứ, không biến một tình huống bịa thành quan sát thật.

Thiếu evidence không chứng minh không thể có flow tự nhiên. Ngược lại, flow hay cũng không tự tạo evidence. Dừng ở đây không phải chờ metadata được lưu hay chờ Hiệp chọn lại trend.

## 3. Ba kiến trúc đã xét trước lời thoại

Đây là ý tưởng/nhãn chức năng, **không phải ba đoạn hook hay script**.

| Phương án | Xương sống | Thật sự đổi điều gì | Vì sao chưa chọn để viết full |
|---|---|---|---|
| A — Đỉnh lúc áp dụng | Mắc một việc đời thường → thông tin text hip → chọn cách nhớ → kiểm → phát hiện lệch | Không đổi được logic gốc của r11.1; chỉ thay giao thông bằng vật khác | Trend vẫn ngoại đề. Loại, không viết tiếp. |
| B — Một cuốn sách, thêm một mục tiêu | Pain học/nhớ chung → text hip đặt bối cảnh đọc có nhiều giá trị → người xem thêm mục tiêu nhớ một nội dung để dùng → ranking → mục tiêu đối chiếu → tự kiểm → phát hiện thiếu trong phần kể | Đổi cơ chế từ “thất bại ngoài đời” sang **thêm mục tiêu vào chính lần đọc**, không phân hai nhóm người | Là hướng C tự nhiên hơn về biên tập, nhưng câu trend vẫn chỉ là bối cảnh độc lập. Muốn vượt phép thử tháo câu trend phải gán một quyết định/động lực cho người xem mà nguồn không ghi, hoặc dựng cảnh bàn trend đã bị L096 bác. Evidence pain vẫn thiếu. |
| C — Trải nghiệm đọc vui, không biến mọi trang thành bài thi | Áp lực phải nhớ tất cả → bối cảnh text hip/đọc tận hưởng → chọn nội dung cần nhớ → tự kiểm tùy mục tiêu | Mở ở xung đột giá trị chứ không “đọc xong quên” | Nguồn không có pain “áp lực phải thuộc mọi trang”; dễ gán cho người theo trend hoặc dựng phản đề rơm. Cũng rời concept2 “Bài đọc để làm theo”, chuyển thông điệp sang chọn lọc/giảm áp lực chưa nằm trong fact lock. Loại. |

**Lựa chọn thiết kế:** B là kiến trúc đáng giữ nếu tiếp tục C, không phải A đổi vật. Nhưng hiện không gọi B đủ sạch để bắt đầu full script theo yêu cầu “trend không tháo rời được”. Phần dưới cụ thể hóa B để người điều phối thấy chính xác chỗ thiếu, thay vì tiếp tục bảy câu vá.

## 4. Outline B — mỗi beat làm gì và liên kết bằng nội dung nào

Một câu nội dung: Trong một lần đọc vừa để tận hưởng vừa để học điều muốn dùng, chỉ với mục tiêu nhớ nội dung, kênh gợi ý tự kể khi tài liệu đóng rồi mở đối chiếu; kết quả minh họa chỉ là nhận ra một phần kể thiếu/sai so với văn bản.

| Beat | Công việc duy nhất | Thứ được kế thừa | Đóng góp mới | Vì sao trend cần có / nguồn | Phép thử bỏ beat |
|---|---|---|---|---|---|
| b01 | Nêu pain học/đọc chung, có “bạn”, không ép bối cảnh ngách; hứa có thể nhìn ra phần kể thiếu | Không | Khoảng trống: làm sao biết phần nào chưa kể khớp sách? | Pain chưa có evidence; không được nói người theo trend gặp nó | Bỏ mất pain/điểm cần trả. Hook chưa viết, chưa kiểm người lạ |
| b02 | Dùng text hip làm bối cảnh đọc như phong cách sống, rồi đổi rõ sang mục tiêu **bổ sung** là nhớ nội dung muốn dùng | Cùng hoạt động đọc ở b01 | Định phạm vi khuyến nghị; một người có thể tận hưởng VÀ học/nhớ | Social 8,38–47; Deep 10,23–25. Không “khác/Not like”, không chê pilsa | Bỏ cả beat sẽ mất phạm vi; **nhưng riêng câu trend vẫn bỏ được mà lập luận phương pháp không mất**. Đây là lỗi chưa giải quyết, không tự ghi đạt |
| b03 | Đối chiếu hai kỹ thuật ở mức ranking để dẫn tới lựa chọn kiểm phần nhớ | Mục tiêu nhớ ở b02 | Dunlosky2013 đánh giá10 kỹ thuật: tự kiểm cao, đọc lại thấp | b02dd07 22–28, không thí nghiệm hai nhóm/không %/không hiệu quả riêng của ví dụ | Bỏ mất lý do có nguồn cho lựa chọn kỹ thuật |
| b04 | Đặt mục tiêu sát thực: biết phần tự kể nào lệch văn bản, không dự đoán sẽ làm được việc | “Tự kiểm” của b03 | Ranh giới điều sắp kiểm | F5; mục tiêu biên tập, không suy từ ranking thành bảo đảm | Có thể gộp mục tiêu với cuối b03, không tạo một beat chỉ nhắc lại |
| b05 | Thực hiện F5: đóng → nói/viết từ nhớ → mở dò | Mục tiêu b04 | Thao tác đủ để làm theo | Deep bridge16–17. Tình huống chỉ nhãn minh họa kênh | Bỏ mất phương pháp |
| b06 | Cho thấy đúng một thiếu/sai trong phần kể khi đặt cạnh văn bản; sửa phần kể | Hai bản ở b05 | Payoff so-văn-bản, không thành công mua sắm/lái xe/khả năng thực hành | Hệ quả đối chiếu của minh họa, không nói “mọi chỗ thiếu” | Bỏ mất kiểm lại lời hứa b01 |
| b07 | Một yêu cầu comment một từ theo điều kiện cụ thể; loop từ khóa hook | Kết quả b06 | Người xem nhận một điều kiện thử, không thêm bài học | Không callback04 như đã phát hành; ≥3 engagement phải bố trí khi có lời | Chưa thể viết CTA chính xác khi chưa chốt hook và ví dụ |

### Ngân sách trước khi viết, không ép mảnh câu

- B01 khoảng 22–28 từ, hứa kết quả trong 35 từ đầu; vế đầu ≤6 từ.
- Từ hết hook tới phương pháp: b02 15–18 + b03 22–25 + mục tiêu gộp 6–7 = **43–50 từ**. Chỉ là budget, không giả số đo bản chưa có.
- Phần còn lại ưu tiên một minh họa có tên điểm thiếu, không thêm tình huống thứ hai. Tổng mục tiêu140–175; nếu không đủ ý trong budget thì bỏ ý, không chặt chủ ngữ.
- Không buộc hook có câu hỏi. Nếu có: cùng pain/mốc, trả lời ngay trước khi nhắc trend (P06/L094); nếu không chứa được quan hệ ấy thì bỏ câu hỏi, không treo điều kiện “nếu giờ”.

## 5. Kiểm quan hệ ý ở đúng chỗ khó nhất

### b01 → b02

Mối nối có thể có: người xem đang nói tới **một lần đọc**; b02 mở rộng rằng lần đọc có thể mang đồng thời niềm vui/phong cách sống và mục tiêu học. Quan hệ này không cần phân nhóm độc quyền.

Điểm chưa đủ: pain b01 là kiểm nhớ; thông tin báo Hàn không giải thích pain đó. Đặt bối cảnh sau pain chỉ có thể là đổi phạm vi biên tập, không là nguyên nhân. Nếu viết như câu trả lời cho pain sẽ phạm fact; nếu viết đúng hai ý độc lập thì vẫn chịu phép thử tháo trend của review.

### b02 → b03

Mối nối thật là **mục tiêu nhớ được thêm vào**, không phải văn hóa đọc Hàn. Ranking trả lời việc chọn kỹ thuật cho mục tiêu nhớ. Đây là bridge có điều kiện Deep cho phép.

Điểm chưa đủ: nếu xóa mệnh đề text hip nhưng giữ điều kiện mục tiêu, b03 vẫn đến đúng chỗ. Không được giấu sự tháo rời này bằng cách để cả hai mệnh đề trong một beat rồi gọi beat ấy “bắt buộc”.

### b03 → b05 → b06

Ranking → mục tiêu → F5 → đối chiếu phần kể là chuỗi khả thi trong giới hạn đã cấp. Không cần nguồn mới về nguyên nhân kẹt thao tác. Nhưng chuỗi này đã là lõi của clip04 và nhiều bản clip05; độ mới phải đến từ câu chuyện/điểm nhìn, không thể đến từ việc bịa thêm kỹ thuật hoặc tuyên bố kỹ thuật mới.

## 6. Xung đột cụ thể, không tuyên bố chung chung “không nối được C”

**Xung đột A — tiêu chuẩn vai trò trend cần được phân biệt:**

- Deep d673dd9 dòng10,23,38: C được phép là **bối cảnh + khuyến nghị độc lập có điều kiện**; không đòi quan hệ nhân quả.
- Review r11.1 dòng15,41–42 và L051/checklist46: câu trend không được là ngoại đề tháo ra mà mạch còn tốt hơn.
- Hai tiêu chuẩn KHÔNG tự động mâu thuẫn trong mọi clip: một bối cảnh có thể có giá trị mở chuyện mà không là nguyên nhân. Tuy nhiên ba kiến trúc trên chưa tìm được vai trò ấy cho **câu chuyện áp dụng/kiểm nhớ hiện tại**. Viết tiếp B mà tự gọi trend “không thể tháo” sẽ báo sai tiến độ. Đây là giới hạn thiết kế hiện tại, không phải bằng chứng rằng mọi cấu trúc C đều bất khả thi.

**Xung đột B — bằng chứng ví dụ chưa có trong gói:**

- L090/checklist171 đòi ví dụ pain có evidence người xem thật; Social10,40–43, metadata22–25 xác nhận không có.
- Dựng minh họa là được phép về nguồn gốc câu chuyện, nhưng không chứng minh L090 manual. Kể cả metadata được lưu đúng, lỗi này vẫn mở. Không tự bỏ L090; cũng không yêu cầu chủ nguồn tìm ví dụ không tồn tại để hợp thức hóa bản đã viết.
- Nếu người điều phối tiếp tục cho viết một bản **minh họa có điều kiện, chưa pass L090**, đó là scope rõ hơn; bản ấy vẫn phải được review flow riêng. Lượt này không tự giả rằng chỉ đạo ghi nhãn minh họa đồng nghĩa đã miễn điều kiện evidence.

**Không phải xung đột:** Dunlosky/L096. Ranking đủ cấu trúc nguồn–so sánh–kết quả theo Reviewer đã chuyển. Không cần đợi A-vs-B thí nghiệm, không thêm Yang. Không phủ định tuyệt đối rằng tổng quan không đánh giá trí nhớ.

## 7. Bảng review issue → xử lý → vị trí → còn chờ

“Xử lý” dưới đây phân biệt **đã sửa quyết định thiết kế** và **chưa thể xác nhận sửa trong lời**, không báo PASS cho script chưa có.

| Issue r11.1 | Xử lý ở r11.2 | Vị trí hồ sơ này | Còn chờ |
|---|---|---|---|
| Trend ngoại đề, vá liên từ | Loại A; thiết kế B và tự làm phép tháo riêng mệnh đề trend | §2–5 | B chưa vượt phép tháo, dừng trước lời |
| Khác/Not like phân đôi | Chỉ cho mục tiêu bổ sung trên cùng một người/lần đọc; không “hai kiểu đọc” độc quyền | §3B,§4b02 | Câu VI/EN thực tế chưa viết/chưa duyệt |
| 76 từ trước method | Budget43–50, gộp mục tiêu, không nêu năm/tác giả/móc riêng lặp | §4budget | Chưa có count thực |
| “tức là” cấm | Không giữ wording cũ; danh sách rule60 là hard constraint, ưu tiên liên hệ nội dung | §8 | Chưa có câu mới để lint |
| P16 / hook_alt | Pain đọc/học chung trước bối cảnh, không bắt câu hỏi; alt phải khác kiểu | §4b01,budget | Hook, alt, người lạ/timing chưa có |
| Doodle vượt gate | Không kế thừa doodle-path/cross/arrow của r11.1; nếu tiếp tục thì chỉ vật có sẵn, không vẽ nét | §8 | Chưa lập motion, không báo gate đã pass |
| Engine b03 lẫn | Không kế thừa cảnh comic mở beat ranking; explainer ranking không có chibi | §8 | Chưa spec engine |
| Cover/storyboard/spec thiếu | Không coi bảng text là storyboard thật; không dựng đồ giả để đủ danh mục | §8–9 | Chưa làm do chưa qua outline; đây là thiếu thật |
| L090 metadata/pain | Giữ ID/nội dung null, tách evidence trend và minh họa; ghi rõ thiếu manual evidence | §1,§6B | Chưa sync addendum; sync không chữa nội dung |
| Nguyên nhân kẹt thao tác | Loại hẳn khung áp dụng-thất bại→vì thiếu nhớ, không đổi thành ví dụ khác | §2,§3A | Không có claim mới cần gỡ |
| Payoff dự báo khó thực hành | Chỉ thiếu/sai trong phần vừa tự kể so-văn-bản | §4b06 | Chưa minh họa cụ thể, không bảo đảm kỹ năng |
| Callback04 chưa posted | Không viết “clip trước/bạn đã xem”; chưa xác nhận phát hành | §4b07 | Cần metadata phát hành ở đóng gói, không blocker nguồn mới |
| Nhấn/caption/CTA/endcard | Đưa thành điều kiện cho draft, không tái dùng plan lỗi cũ | §8 | Chưa có bản thoại/spec để so khớp |
| Giọng/timing/read-aloud | Không tạo audio, không tự báo đã đọc/nghe | đầu file,§9 | CHƯA KIỂM |
| Audit lặp | Không lặp pain→nguyên nhân→mục tiêu bằng ba câu đồng nghĩa; mỗi beat một việc | §4,§8 | Audit ngram chỉ khi có thoại |

## 8. Điều kiện cho bản kế tiếp — không phải spec/motion plan đã hoàn thành

- Fact: một câu Dunlosky đủ nguồn+năm+10 kỹ thuật+hai mức; không %/rank1–10/thử nghiệm chia nhóm, không Yang; bước F5 đúng nguồn. Không bịa pain từ người theo trend, không coi pilsa là retrieval hay làm sai.
- Audit lặp: “đọc” là bối cảnh, “nhớ” là mục tiêu, “dò” là thao tác; tránh nhắc lại cùng insight ở mục tiêu/payoff. Chỉ giữ cụm hook-loop nếu vai trò mới rõ; bỏ các câu hứa tách riêng lặp kết quả. Chưa có ngram/count thực nên không khai mật độ đạt.
- L096 tách ngưỡng: lesson232 không hai câu dưới8 từ liền nhau; đề xuất238 >30% dưới8. Checker/checklist178 hiện ≤10 từ và trần30%. Không thay checker cho khớp draft.
- Mỗi beat phải có đủ người nói, context, time estimate, shot/action/react, thoại markup1–2 nhấn đúng chữ, nghỉ đúng dấu, EN≤8/chunk, motion/SFX/transition, lý do hình, link, claim source, status như prep r2.
- Không doodle. Props có sẵn/chibi Remotion cho chuyện; bảng ranking/đối chiếu HyperFrames riêng. Trước chọn motion mới phải load motion-picks, đọc catalog/effects-log; effect/asset chưa kiểm không tự nhận có. Không viết code engine hoặc tạo SFX mới trong scope này.
- Storyboard ở bước này chỉ FILE KẾ HOẠCH, cần bbox, frame đầu/giữa/cuối, safe-zone, captions tách mặt/props. Không gọi đó là PNG/contact sheet đã kiểm mắt. Spec JSON phải nhãn planning_only/not_renderable, không chạy build-final --stage plans vì có thể gọi giọng.
- Cover đúng template A, EN hero cũ→mới, series/ep/theme/expression/action/emote/tilt, không lấy frame video. Render/cover still chưa được phép trong lượt này.
- ≥3 engagement: comment một từ + loop keyword + relatable-question nằm đúng ngữ cảnh, CTA chỉ một yêu cầu. EN giữ điều kiện giả định; không xin like/follow. Bình luận ghim tiếp challenge, không xin địa chỉ/tài chính thật.
- End card/post bắt buộc: “Thông tin tham khảo, không thay thế tư vấn chuyên gia”; “Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/”; “Đã chuyển thể. Giấy phép: https://creativecommons.org/licenses/by/4.0/”. Chỉ nguồn thật sự được nói: Dunlosky2013 và Znews cho bối cảnh. Không ám chỉ chứng thực. Readability vẫn phải đo, không giả endcard1.5s đủ.

## 9. Bàn giao thật

| Hạng mục | Kết quả |
|---|---|
| Outline trước lời | Đã lưu file này, có3kiến trúc, lựa chọn B và phép thử thất bại được nêu |
| Script r11.2 | **KHÔNG TẠO**; không đổi tên outline thành script |
| Spec r11.2 JSON | **KHÔNG TẠO** vì outline chưa đủ khả thi; không tạo spec rỗng |
| Count và nguyên thoại | **0 từ; không có nguyên thoại r11.2** |
| Text checker | **KHÔNG CHẠY**: không có draft mới; output r11.1 vẫn là output của r11.1 |
| Người thật đọc to/người lạ/timing | **CHƯA KIỂM** |
| Repo/commit/sync của deliverable này | Ngoài repo, không commit/push/sync; không sửa source |
| Gửi tin/voice/render/ảnh | Không thực hiện |

Bước điều phối cần biết: không còn blocker tìm study hay chọn trend. Điểm cần giải quyết là **vai trò biên tập của trend trong câu chuyện**, cộng với cách giữ nguyên trạng thái thiếu evidence L090, chứ không là kỹ thuật thêm liên từ. Không đề nghị Hiệp chọn lại C, không tự giao nghiên cứu mới, không tiếp tục bản chỉ đường.


## Cập nhật quyết định 14:50–14:51 (Asia/Saigon)

Reviewer chọn B để VIẾT FULL; rút điều kiện suy thêm tháo riêng mệnh đề trend. L051 kiểm xóa BEAT. Social cấp nguồn pain độc lập archive7fb1e4b dòng17, không đại diện khán giả kênh/texthip. Theo steering này đã tiếp tục tạo script/spec planning_only/storyboard plan r11.2. Các mục dừng/0từ ở trên là trạng thái TRƯỚC quyết định, không còn là kết quả bàn giao hiện hành. L090 vẫn MỞ; không tự tìm thêm/không bịa raw/live/metadataSHA.
