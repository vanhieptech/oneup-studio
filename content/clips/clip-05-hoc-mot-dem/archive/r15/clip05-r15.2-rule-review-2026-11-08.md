# Rule Review — clip-05 r15.2 PATCH2, review delta (chỉ đọc), 08/11/2026 ~14:33 giờ VN
- File: `/home/box/agent-data/agents/315819de-26d8-48c8-a4a6-e2f7a5d3545a/handoffs/clip05-r15.2-full-draft-2026-11-08.md`
- File SHA `87885dd3f4e0b1d847e7971c0476878f85691e3178b55ff7cbae6f6a096f7dc2`, tự tính khớp.
- Lời SHA `3a6f280daede0ea30db9d095643deb7f77868981ea22b804991b3b425cf7a78e`, tự tính khớp (sau cả dòng marker mở + LF, trước marker đóng, giữ LF cuối); 439 đơn vị.
- Diff lời so với r15.1 (SHA lời `ee0e5aa879d3e2fa373e9aa3edab91d2a84d0f7c42c519755d718f40c5750652`): chỉ đổi S18. Non-S18 aggregate `00a768f35d801d65895cdb0a56e0016b8e240b99a72557927e842d71454c3b53` trước = sau. Vế sau dấu phẩy của S18 giữ nguyên bytes (SHA `72d95e19e2dd55403b7d2ea822e5e9ff06de2fa5445b7e7a09a06db56d5c3b5b`). S01 không đổi.
- OC ghi «prepared pending owner coordination approval» và chưa gửi kênh ngoài; bản đã đủ trong thư mục handoff nên review như draft chưa chấm, không coi đây là Chốt.
- Luật/skill: lessons/checklist mtime 13:06; make-video 13:02; craft 13:02; motion-picks 12:40 — không đổi từ review 14:24. Working tree local có thêm L-097 (chưa commit so với HEAD `8ff7698`); không có L-100. Đối chiếu L-094 (đây là PATCH2 trên nền E/r15, chưa đủ 3 vòng vá), L-098, L-099.

## Kết luận: K2 ĐÓNG ở mức văn bản. ĐỦ CHUYỂN GATE NGUỒN (Deep trên SHA lời mới). KHÔNG phải PASS tổng. Không gửi Hiệp.

Nghĩa/craft của đúng một chỗ còn mở đã đóng ở lời. Đạt máy hay nguồn của SHA cũ không phải PASS bản này (L-098). Nghe một lần / người lạ / đọc to người thật: CHƯA KIỂM.

### K2 craft — ĐÓNG ở mức văn bản (S18, file dòng 40 khối lời và dòng 137 mục lục)
Trước: «Tự viết nhỉnh hơn ở mốc này, nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.»
Sau: «Tự viết cho tỷ lệ ý nhớ đúng cao hơn ở mốc này, nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.»

- Không còn «nhỉnh hơn», nên không còn từ mang nghĩa hơn một chút khi nhắc lại 56/42.
- «Cao hơn» chỉ chiều so, không thu nhỏ và không gắn «đáng kể / vượt trội» hay số hiệu ứng mới.
- Đối tượng là «tỷ lệ ý nhớ đúng», khớp chỉ số «ý nhớ đúng» vừa nêu ở S17 (file dòng 40, nửa câu trước: 56 phần trăm so 42 phần trăm).
- «Ở mốc này» trỏ «sau một tuần» ở S17, cùng đoạn.
- «Kết quả ấy» và «không phải nhớ hết nội dung» giữ nguyên: nói 56 phần trăm không phải nhớ toàn bộ, khác với mô tả độ chênh là nhỏ.
- Cùng khuôn «cho tỷ lệ ý nhớ đúng cao hơn» với S10 (đã đạt, đọc lại hơn ở năm phút). S10 không đổi byte, nên bản này không biến tự viết thành luôn hơn mọi mốc.
- Khớp S03 «vẫn hơn» ở cùng chiều, không thu nhỏ khi nhắc lại.

S17→S18 nối bằng chữ có sẵn: 56/42 và «ý nhớ đúng» → «tỷ lệ ý nhớ đúng cao hơn»; «sau một tuần» → «ở mốc này»; 56 phần trăm → «kết quả ấy» / «không phải nhớ hết». S18→S19 giữ mối nối đã chấp nhận ở r15.1 (giới hạn nhớ hết → câu hỏi chuẩn bị kể); không mở lại.

Caption tiếng Anh S18 (file dòng 201): bốn chunk, lần lượt 6 / 7 / 4 / 7 từ, không vượt 8.

### K1 — vẫn ĐÓNG ở mức văn bản
S01 không đổi byte so với r15.1.

### Nguồn — chưa chấm đúng SHA lời mới
- Deep và Social của r15.1 gắn SHA lời `ee0e5aa8…0652`. Không thừa kế verdict nguồn đó cho SHA `3a6f280d…a78e`.
- Phần trend/S05 không đổi byte (aggregate non-S18 giống r15.1). Caption tiếng Anh đổi ở S18, không gắn text hip với nhớ/quên/hiệu quả. Không mở lại Social cho phần trend.
- S18 đổi cách nói chiều so 56/42: chuyển Deep fact-check đúng SHA mới. Không tự khóa effect size, không làm fact thay Deep.

Mac CHƯA ĐỘC LẬP KIỂM. Local HEAD `8ff7698` khác live `origin/main` `a32f51f` (commit CapCut CLI, không phải luật clip-05). Không nói toàn repo đã sync.

### Không mở lại
Các mục «Đạt» ở `/workspace/clip05-r15-rule-review-2026-11-08.md` (trừ K2 cũ) và review delta `/workspace/clip05-r15.1-rule-review-2026-11-08.md` / `/workspace/clip05-r15.1-source-gate-review-2026-11-08.md` vẫn giữ với các câu không đổi byte. R1/R2 vẫn là rủi ro nghe, không chặn.

### Máy / thời lượng / hình
- OC đã chạy `--subjects` 0 lỗi và `--l088` 0 lỗi, 1 cảnh báo bản nháp ngoài thư mục clip. Checker đầy đủ trong thư mục clip: CHƯA CHẠY; không chặn cổng lời lần này.
- ƯỚC 181,08s ở 2,9 đơn vị/s và 205,30s ở 2,5 đơn vị/s, gồm nghỉ / chuyển cảnh / end-card: vượt target 180s nhẹ ở nhịp 2,9 — chỉ cảnh báo; tổng <300s. Timing thật: CHƯA KIỂM.
- Không ảnh / voice / render / publish trước Chốt.

## Việc tiếp
- Deep: fact-check SHA lời `3a6f280daede0ea30db9d095643deb7f77868981ea22b804991b3b425cf7a78e`, tập trung S18 mới. Không thay cổng craft.
- OpenCreator: đứng chờ gate nguồn trên SHA này. Không đụng S01 và các câu đã đạt. Không viết media / spec / stageplans. Đây là PATCH2 trên nền E/r15; chưa tới ngưỡng ≥3 vòng vá của L-094.
- Không gửi Hiệp ở lượt này.
