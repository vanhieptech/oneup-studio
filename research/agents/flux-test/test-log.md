# FLUX.2 test log — vòng 1 (chỉ klein 4B)

- Ngày giờ: 2026-10-20 (Asia/Saigon) — kiểm tra lúc ~00:03 Asia/Saigon, ghi log cùng ngày
- Model: FLUX.2 [klein] 4B ONLY (API `flux-2-klein-4b`, Apache 2.0). Không dùng biến thể Non-Commercial.
- Trạng thái: CHƯA GỌI API — thiếu BFL_API_KEY
- API key: CHƯA CÓ. Đã kiểm tra (không in giá trị): BFL_API_KEY / BFL_KEY / BLACK_FOREST_LABS_API_KEY / FLUX_API_KEY đều missing; không có biến env nào chứa BFL/FLUX; /workspace/.env, /workspace/oneup-studio/.env, ~/.env đều không tồn tại.
- Đã upload sheet lên BFL chưa: CHƯA (không key nên không upload được; Hiệp đã duyệt upload 2 sheet Hiệp/Omi cho vòng này)
- Ảnh test: không có (không bịa kết quả). Đường dẫn dự kiến khi chạy: /workspace/flux-test/flux2-klein4b-test-2026-10-20.png
- Chi phí thực tế: $0 (chưa gọi). Ước tính theo docs cho 1 ảnh 1080x1920 (~2,07MP, làm tròn 3MP): output ~$0,016 (MP đầu $0,014 + 2 MP thêm x $0,001) + xử lý ảnh tham chiếu ~$0,001/MP mỗi sheet — tổng cỡ $0,02-0,03/ảnh. API trả field `cost` (credits, 1 credit = $0,01) khi submit — lấy số đó làm chi phí thực tế.
- Prompt: /workspace/flux-test/prompt.txt (tiếng Anh, không chữ trong ảnh, giấy #F7F7F5 / mực #111111 / accent cam #FF5A36, chibi theo sheet gấp sách + tự ghi ra giấy)
- Script chạy sẵn (chưa chạy): /workspace/flux-test/run_flux_test.py — đọc BFL_API_KEY từ env, base64 2 sheet, POST 1 lần, poll tới Ready, tải ảnh. Thiếu key thì script tự dừng, không gọi API.
- Đánh giá ảnh: chưa có ảnh để đánh giá — tiêu chí khi có (theo workflows/agents/flux-visual.md mục 4-6): giống sheet chibi Hiệp/Omi, truyền nghĩa bằng vật/hành động không cần chữ, 0 chữ lọt, không lỗi tay/mặt/vật, vật >=60% bề ngang, không che caption band y>1400, tự soát >=2 vòng full-size. Đạt/chưa đạt: CHƯA ĐÁNH GIÁ ĐƯỢC.
- Dùng cho final/cover: KHÔNG (test nội bộ, luật workflow: ảnh AI không vào final video/cover).

## Sheet kiểm tra (tồn tại, chưa upload)
| File | Bytes | Kích thước px |
|---|---|---|
| brand/characters/hiep-model-sheet.png | 149830 | 2400x1500 |
| brand/characters/hiep-poses.png | 95787 | 2400x1100 |
| brand/characters/omi-sheet.png | 142102 | 2400x1420 |
| brand/characters/v2/hiep-model-sheet-v2.png | 114368 | 1080x1920 |
| brand/characters/v2/omi-sheet-v2.png | 105889 | 1080x1920 |
Bộ upload đã duyệt cho vòng này: hiep-model-sheet.png (input_image) + omi-sheet.png (input_image_2). hiep-poses.png có sẵn nhưng không nằm trong cặp Hiệp/Omi đã duyệt — không upload ở vòng này.

## Tài liệu BFL chính thức đã đọc
- Endpoint klein 4B: POST https://api.bfl.ai/v1/flux-2-klein-4b, header `x-key: $BFL_API_KEY`, JSON: prompt, input_image..input_image_4 (URL hoặc base64, tối đa 4 reference cho klein), width/height (>=64), seed, safety_tolerance 0-7 (mặc định 2), output_format jpeg/png/webp. Nguồn: https://docs.bfl.ml/api-reference/models/generate-or-edit-an-image-with-flux2-[klein]-4b
- Multi-reference/editing + poll: POST trả {id, polling_url, cost}; GET polling_url với x-key mỗi ~0,5s tới status Ready -> result.sample (signed URL chỉ sống 10 phút, tải ngay). https://docs.bfl.ai/flux_2/flux2_image_editing , https://docs.bfl.ai/api_integration/integration_guidelines
- Giá klein 4B: từ $0,014/ảnh; MP đầu $0,014 + $0,001 mỗi MP output thêm; reference $0,001/MP; 1 credit = $0,01; resolution làm tròn LÊN MP. https://help.bfl.ai/articles/7986977817-what-are-the-costs-associated-with-using-your-models
- Tạo key + nạp credits: dashboard.bfl.ai -> đăng ký/xác nhận email -> org sidebar API -> Credits -> Add Credits (Stripe, docs gợi ý bắt đầu $10-20 để thử; không ghi mức nạp tối thiểu cứng cho 1 ảnh) -> project sidebar API -> Keys -> Add Key, đặt tên, copy key (chỉ hiện 1 lần, định dạng bfl_...), export BFL_API_KEY. https://docs.bfl.ai/quick_start/get_started , https://docs.bfl.ai/account_management/organizations_projects

## Hiệp cần làm tiếp (đúng thứ tự)
1. Vào dashboard.bfl.ai, tạo/xác nhận tài khoản.
2. API -> Credits -> Add Credits (nạp thử $10 theo gợi ý docs là dư cho ~hàng trăm ảnh test cỡ này; 1 ảnh chỉ ~$0,02-0,03).
3. Project -> API -> Keys -> Add Key, copy key (chỉ hiện 1 lần).
4. Đưa key vào box an toàn (env BFL_API_KEY) — không gửi key qua group chat; xong báo FLUX "đã có key" ở chat 1:1.
5. FLUX chạy đúng 1 lệnh: BFL_API_KEY=... python3 /workspace/flux-test/run_flux_test.py -> xem ảnh full-size, chấm đạt/chưa theo mục 6 workflow, ghi log vòng này. Không đăng, không dùng final.

## Vòng 2 — chạy thật 2026-10-20 (Asia/Saigon)
- BFL_API_KEY: có (chỉ kiểm boolean, không in giá trị)
- Lệnh: python3 /workspace/flux-test/run_flux_test.py — chạy đúng 1 lần, không thử lại sau lỗi
- Kết quả: THẤT BẠI ở POST, chưa có ảnh
- Lỗi nguyên văn (không chứa key): urllib.error.HTTPError: HTTP Error 402: Payment Required
- Thời gian: ~1 giây (POST bị từ chối ngay)
- Chi phí thực tế: $0 cho lần này (API từ chối trước khi tạo ảnh; không có field cost trả về). Ước tính cũ $0,02-0,03/ảnh chỉ áp dụng khi có credits và chạy thành công.
- Ảnh: không có file flux2-klein4b-test-2026-10-20.png — không đánh giá được theo tiêu chí mục 4-6 flux-visual.md (giống sheet, chữ lọt, tay/mặt, màu brand, truyền nghĩa)
- Nguyên nhân khả dĩ nhất: tài khoản/project chưa có credits hoặc credits thuộc project khác với key
- Hiệp cần làm: vào dashboard.bfl.ai > project đang tạo key > sidebar API > Credits > Add Credits (nạp thử $10 là dư), kiểm tra key thuộc đúng project đã nạp, rồi báo FLUX chạy lại đúng 1 ảnh. Không gửi key qua group chat.
- Dùng cho final/cover: KHÔNG
