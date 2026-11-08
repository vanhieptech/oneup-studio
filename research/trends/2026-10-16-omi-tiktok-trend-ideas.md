# Omi TikTok — ý tưởng theo trend (Apify scrape 16/10/2026)

**Nguồn:** `clockworks/tiktok-scraper` · hashtag productivity / habittracker / selfimprovement / studymotivation / năngsuất / thóiquen · proxy VN  
**Lưu ý:** Creative Center trends (clockworks-trends + Explore VN) **fail/timeout** lần này → dùng hashtag hot thay vì “trending board”.

## Pattern đang ăn (rút từ data)

| Pattern | Ví dụ | Góc Omi |
|---------|--------|---------|
| List “X thói quen phá đời/năng suất” | bimthu 141k like · lean… 816 like nhưng share cao | Omi đếm 5 thói quen + tick đỏ |
| Demo habit tracker (sheet/app) | lifestylebanker 617k · youarelovedtemplates | Screen Omi check-in 1 ngày |
| Dopamine / 3 bước học | mewmi.cuti 80k · repost hàng loạt VN | Omi kể 3 bước, ngắn comic |
| Study motivation ngắn + sound | studywithme2am (13/10), cut.the.noise5 | Omi: “dậy học đi” 10–15s |
| Challenge + CTA app | adamthedunker push-up + app | “Tick 1 thói quen → Omi khen” |
| Quote/edit cảm xúc | wisdoomer / Mel Robbins | Omi voice-over 1 câu |

## 5 clip sẵn làm (comic Omi + Hiệp chibi)

### 1. “5 thói quen khiến bạn giảm 80% năng suất” (list)
- Hook: Omi: “Hiệp ơi, tối nay lại dính bao nhiêu cái?”  
- 5 beat: điện thoại trên giường · multitask · không giờ ngủ · skip vận động · mua sắm impulse  
- CTA: mở OneUp tick 1 cái bỏ hôm nay  
- Hashtag: `#thóiquen #năngsuất #productivity #oneup #omi`

### 2. “Não không lười — não đói dopamine” (3 bước, ~45–60s)
- Bám format mewmi (đang viral VN): 30’ giảm kích thích → hình dung phần thưởng → pomodoro + khen nhỏ  
- Omi là “người khen” sau mỗi 25’  
- Soft CTA: OneUp = log phần thưởng nhỏ  

### 3. Habit tracker 8 giây (demo UI)
- Style youarelovedtemplates: zoom sheet/app, ASMR tick  
- Chỉ 1 habit: “ngủ trước 23:30” hoặc “1 clip TikTok”  
- Omi: “+1 rồi đó”  

### 4. Toxic study soft (15s)
- Text: “Nếu đang cuộn feed — đây là dấu hiệu dậy làm việc”  
- Omi kéo Hiệp chibi khỏi giường  
- Sound: studymotivation đang dùng tuần này (xem clip studywithme2am 13/10)  

### 5. Challenge 7 ngày (series)
- Ngày 1: Omi giao 1 habit  
- Format adam: challenge + code/app trong caption  
- Mỗi ngày 1 clip 10s: fail/comic → tick  

## Việc tiếp theo
1. Chọn 1 trong 5 → render comic tuần này  
2. Khi cần sound/hashtag “mới lên”: chạy lại Apify **search PAST_WEEK** (run keyword đang chậm) hoặc Creative Center khi API ổn + cookie  
3. Comment scrape top clip dopamine VN để lấy nỗi đau caption  

Dataset hashtag: Apify run `CuQcpOEjpDB20BfdW` / dataset `YdNKg5ApvKiBSZoXU`

---

## Retry combo 16/10 ~00:55 ICT

| Actor | Kết quả |
|-------|---------|
| clockworks/tiktok-trends-scraper VN+US | Fail 0 item (Creative Center chết) |
| lexis hashtags | Fail exit 91 — **cần cookie ads.tiktok** |
| lexis trending videos VN (no cookie) | OK **4** nhưng toàn ads Sting/BUPNON/nấu ăn |
| parseforge keyword VI | Fail (keyword page không tồn tại) |
| parseforge URL + transcript + comments | **OK 3 clip** — slideshow/edit thường **không có transcript**; caption + comments dùng được |
| clockworks comments | Abort (đã có comment từ parseforge) |

### Nỗi đau comment (mewmi 1.2M view)
- Ngồi bàn → buồn ngủ / ngáp
- Điện thoại = phá kỷ luật (có đt vs không đt)
- Học 5p thưởng 3h TikTok (trớ)
- Khó bắt đầu, bắt đầu rồi khó dừng
- 30 tuổi bắt đầu lại còn kịp?
- Nhạc học? / laptop thì sao?

### Góc Omi ngay
1. Slideshow dopamine 3 bước + Omi = người khen sau 25’
2. “Ngồi bàn là buồn ngủ” — Omi kéo Hiệp dậy 15s
3. Phone-on-bed → Omi cấm điện thoại giường (đúng pain thật)
