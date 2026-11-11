# Treg TikTok — 2026-11-11

Treg-first theo quyết định của Hiệp 08/11/2026. Không dùng Apify (không thiếu capability, không lỗi thật).
Fetch: 2026-11-11 khoảng 08:00–08:45 (Asia/Saigon). Balance 0.94007 → 0.90987 = **$0.0302, 17 calls** (khớp đúng).

## Call ledger

| # | Endpoint (provider) | Input | Call id | Cost |
|---|---|---|---|---|
| 1 | treg.tiktok.search (scrapecreators) | san sale 11.11 | 0d1acedbc3494fdc8096e43fbbadc51a | $0.00188 |
| 2 | 〃 | ngu trua 10 phut | dac986a18c71437f88d040edc677cd0c | $0.00188 |
| 3 | 〃 | ca phe buoi chieu mat ngu | 6963c46d44e6460ebc29304704e9d1aa | $0.00188 |
| 4 | 〃 | chup man hinh tin nhan sep | 5e4c16e7d8bd46089e7e57d550f3daf2 | $0.00188 |
| 5 | 〃 | moi ngay 15 phut | 02a837bacf9040df988e4ffe1a49e44b | $0.00188 |
| 6 | 〃 | ngoi van phong ca ngay | e0a57cf32806485f905e7c8de9c9d710 | $0.00188 |
| 7 | 〃 | chot don roi hoi han | f39fd547abb1434283df7a3d730d8137 | $0.00188 |
| 8 | 〃 | uong ca phe mat ngu | ea90440a543a4b388d3b39623c50f0bd | $0.00188 |
| 9 | 〃 | san sale xong het tien | 7476fc18237041f7adb95c6410b9fd33 | $0.00188 |
| 10 | 〃 | gio hang 11.11 | ec381351e42943bfad294921733993a3 | $0.00188 |
| 11 | 〃 | tuoi 20 met moi that bai | 9647d3c1c0d441c093bd37d4d9d1ed97 | $0.00188 |
| 12 | scrapecreators.tiktok.video.detail | @braincorevn 7705277410563951878 | c84e1186325448d397c2c34c1d66c61a | $0.00188 |
| 13 | 〃 | @btvy_office 7705780920220978439 | 128f541a908e4dca91a38d3cb8a575a9 | $0.00188 |
| 14 | 〃 | @carter.selfdev 7704640861753068821 | 57b4dc2c6ee0456ead16858ece6dbd84 | $0.00188 |
| 15 | 〃 | @quocnguyenkieuvi 7705090431322787080 | ad268c36071f4ab4ab4aa40b5a6b45cf | $0.00188 |
| 16 | treg.tiktok.video.comments (tikhub app-v3) | video_id 7704547318439218439 | af69dfe687904900b3f7deb15c059ea0 | $0.001 |
| 17 | treg.tiktok.video.comments (tikhub) | video_id 7705090431322787080 | 6ec05271100c493a96d1cb11756d4aeb | $0.001 |

Search filters: date_posted=this-week, region=VN, trim=true. Comments gửi `video_id` + `X-Treg-Route-Max-Cost: 0.005` để bỏ anyapi (url-only $0.002).

## Coverage / limits
- Videos: 285 dòng chuẩn hoá (`search-normalized.json`), posted 04–11/11. Region field (182 dòng đầu): VN 175, TW 4, ID/PK/FI 1 mỗi nước. region=VN có thể chỉ là proxy, không chứng minh địa lý.
- Comments: 2 clip. trangxitrum5 vô dụng (sticker, bạn bè); quocnguyenkieuvi có comment thật (xem shortlist, mỗi comment = 1 lời tự kể).
- Sound: chỉ từ 4 detail (search trim=true bỏ music); cả 4 là original sound của creator. Metadata ≠ quyền dùng lại. Không gọi sound chart.
- Transcript: 3/4 detail có WEBVTT thật; braincorevn trả null (chỉ caption). btvy_office transcript là nội dung game → drop.
- Feed/search ≠ bảng xếp hạng; lifetime views ≠ độ hot; fetched hôm nay ≠ đăng hôm nay.
- Query yếu/lạc: ngủ trưa, cà phê chiều, chụp màn hình tin nhắn sếp, 15 phút, ngồi văn phòng, chốt đơn hối hận, hết tiền (ra game/giải trí). 11.11: 31/54 dòng là is_ad (livestream, KOL bán hàng).

## Lessons
- Ngày 11.11, search TikTok chủ yếu là quảng cáo/livestream (is_ad); ngôn ngữ nỗi đau phải lấy từ báo hoặc clip không phải ad.
- Clip <1k view: comment là sticker/bạn bè chat → đừng trả tiền comment.
- Raw provider response chứa `cookie` / `tt_chain_token` của provider: đã thay bằng [REDACTED] trước khi commit.
