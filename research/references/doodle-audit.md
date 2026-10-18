---
title: "Doodle audit: vì sao animation cũ đẹp hơn, và cổng chặt cho doodle (chờ Hiệp duyệt)"
date: 2026-10-18
source: "so sánh clip-01/02/03 locked vs 4 doodle demo; test crack trên clip-03 b06 (2 vòng still)"
id: research.doodle-audit
type: audit
status: "kết luận: zero-doodle cho b06; cổng doodle đề xuất, CHƯA áp vào lessons/SKILL — chờ Hiệp duyệt"
tags: [doodle, animation, audit, L-047, L-048, L-049]
---

# Doodle audit — animation cũ vẫn đẹp hơn

Verdict của Hiệp (18/10): «Quá xấu, không liền mạch, animation cũ vẫn đẹp hơn — hãy
tích hợp một cách phù hợp đúng nội dung thay vì thay đổi cho có.» Audit này kiểm chứng
bằng file thật, không bênh doodle.

Đối tượng so sánh:
- **Hệ cũ (locked):** `content/clips/clip-03-big-task-chunking/final/plan-A.voiced.json`
  (+ clip-01/02 final cùng grammar), `final/contact-sheet.png`, `final/timing.json`.
- **4 doodle demo (giữ nguyên làm rejected reference, không xoá):**
  `video-engine/examples/doodle-demo-brand.json`, `doodle-creative-demo.json`,
  `doodle-assets-demo.json`, `doodle-morph-demo.json` (+ frame `/workspace/doodle-*-frame*.png`).

## 1. Vì sao animation cũ đọc đẹp hơn — điểm cụ thể

1. **Vật thể tồn tại và biến đổi trong cùng grammar cảnh.** Thầy chibi (`hiep`, x≈0.74,
   phải khung) + bong bóng thoại + caption plate dưới + 1 prop chính bên trái là bộ khung
   không đổi suốt clip-03. Prop vào bằng chuyển động có nghĩa rồi *ở lại*: `words` chip
   rơi từng cái (`Props.tsx`: ease 0.12s, scale 1.6→1, squash khi chạm), `sign` pop
   (overshoot sin), lịch xé trang. Người xem bám vào vật cũ mà đọc vật mới.
2. **Ngôn ngữ transition/easing nhất quán, có tên và có số.** Clip-03 locked dùng:
   `cut` (b01–b03, b10), `mmx-soft-land` (b04), `tdev-panel` (b05), `tdev-stagger`
   (b06), `mmx-snap-settle` (b07), `tdev-text-swap` (b08), `tdev-modal` (b09) — tất cả
   0.4s, easing đo được: tdev OUT = cubic-bezier(0.22,1,0.36,1), stagger lệch 40ms/item;
   mmx snap-settle đi 54/84/96/98% ở 10/25/50/75% thời gian. Mọi cảnh "đáp đất" cùng một
   cảm giác vật lý.
3. **Nhân vật gánh cảm xúc.** Mỗi beat đổi expression/action đúng câu nói (surprised →
   despair → confused → focused → happy), miệng nhép theo envelope giọng, thở squash,
   chớp mắt. Cảm xúc nằm trên mặt Thầy, không nằm ở hiệu ứng phụ.
4. **Timing khoá theo cụm từ giọng thật.** Trong `plan-A.voiced.json`, `dropAt`/`at` của
   prop và `sfx.at` trùng nhau từng 0.05s: b06 chip `CHIA NHỎ` rơi đúng 1.65s = sfx
   `snap` 1.65s = lúc nói «chia nhỏ ra»; b07 ba chip rơi 3.95/5.35/6.55s = ba sfx `tick`.
   Hình, tiếng động và lời là một sự kiện duy nhất.
5. **Mật độ và hoàn thiện.** Mỗi khung có đúng: nền giấy chấm, Thầy, bong bóng, 1 prop,
   caption — không khoảng trống chết lớn. Prop là hình *đóng kín*: fill giấy/đen/cam,
   viền mực 8–10px, bóng cứng lệch, bo góc. Nhìn là "đã vẽ xong".

## 2. Vì sao từng doodle demo phá nó — điểm cụ thể

| Demo | Phá ở đâu (bằng chứng) |
|---|---|
| `doodle-demo-brand` (khoanh/gạch) | Đúng brand nhưng vô nghĩa: khoanh/gạch đè lên sign/words có sẵn không nói thêm điều gì lời chưa nói; nét là lớp thứ 6 cạnh tranh với caption highlight đã nhấn cùng từ đó. |
| `doodle-creative` (đá → bậc thang) | 0 nhân vật, 0 thoại, 0 caption trong 13s; hình viền trống không fill ở giữa giấy trống mênh mông (frame2: 4 ô viền chiếm ~15% khung). Đây là *thay* grammar cảnh bằng whiteboard, không phải tích hợp. |
| `doodle-assets` | Asset cũ + tick/connector vẽ thêm, nhưng tick cam vẽ tay đặt cạnh chip `words` đã tự có ✓ trong chữ (`DỌN GHẾ ✓`) → trùng thông tin; connector chạy qua vùng trống, path `smooth:false` vẫn lạc nhịp rơi chip. |
| `doodle-morph` (gần nhất) | Tự chế sign `DỌN PHÒNG` 660px không có trong locked b06, cho nứt rồi *biến mất cứng* (fadeOutAt) và thay bằng 3 note vẽ mới ở vị trí khác — vật không tồn tại tiếp, mà bị thay. b07 vẽ lại 3 note + đồng hồ trong khi locked đã có words/sign làm việc đó; bong bóng che note 1 (đã ghi ở L-049). Transition bị hạ từ `tdev-stagger`/`mmx-snap-settle` xuống `cut`, nhân vật bị đẩy x 0.74→0.80 — tức demo đã lặng lẽ bỏ đúng thứ làm cảnh cũ đẹp. |

Điểm chung: (a) nét stroke-only (7–11px, không fill/bóng) đặt cạnh chibi fill phẳng →
hai ngôn ngữ hình trong một khung; (b) doodleEase `1-(1-p)^2.2` không trùng bất kỳ
easing tdev/mmx nào → nhịp "đáp đất" khác hẳn cảnh; (c) vẽ xuất hiện trong khoảng trống
chứ không mọc ra từ vật đang kể; (d) không beat nào *cần* vẽ tay — lời + prop + sfx đã
nói đủ.

## 3. Khi nào doodle thật sự cộng thêm?

Chỉ khi nội dung của beat *chính là* hành động vẽ/viết/cắt/nối/đi một đường mà prop và
transition hiện có không diễn được. Kiểm chứng ngược: b06 «chia nhỏ ra» — hệ cũ đã có
chip rơi + snap + highlight, thêm nét nứt không cộng thông tin (xem §4). Ví dụ có thể qua
cổng (chưa làm, chỉ là chuẩn xét): một lộ trình/đường đi phải vẽ dần theo lời; một chữ
phải bị gạch *tại chỗ* trên giấy đang tồn tại trong cảnh; một hình phải nứt *và các mảnh
của chính nó* biến thành vật tiếp theo (không biến mất, không thay bằng hình vẽ mới).

## 4. Part B — test crack trên beat locked b06–b07: THUA, zero-doodle thắng

**Sự thật phải nói trước:** beat locked b06 *không có* sign «DỌN PHÒNG». Locked b06 chỉ
có Thầy + `words` [CHIA NHỎ, TÍNH GIỜ, BẮT TAY] rơi ở 1.65/3.45/5.05s trên nền `grid`,
transition `tdev-stagger`. Sign «DỌN PHÒNG» là do demo morph tự chế. Vì vậy "nứt cái
sign có sẵn" không thực hiện được mà không chế thêm vật.

Test đã làm (2 vòng still, spec `video-engine/examples/doodle-integrated-demo.json`,
giữ làm rejected reference): copy nguyên 2 scene b06+b07 từ `plan-A.voiced.json`
(giọng c03v8, timing, transition, vị trí Thầy giữ nguyên), chỉ thêm 1 sign prop có sẵn
(`kind:"sign"`, như locked b03) + 1 cue 3 nét nứt mực ở 1.28s, sign mất lúc 1.60s để
words locked rơi lúc 1.65s.

- Vòng 1 (sign s=0.8): sign nhỏ, nét nứt lệch khỏi mặt sign, chỉ thấy 1 vệt bé.
- Vòng 2 (sign s=1.0, nét canh lại): nét vẫn chỉ lấp ló ở mép trên sign, và lỗi chí mạng
  không sửa được bằng canh nét: **sign biến mất cứng** (`until`) rồi chip CHIA NHỎ hiện
  ở chỗ khác thấp hơn — đúng lỗi "vật bị thay, không biến đổi" của morph. Thêm nữa sign
  nói trước ví dụ «dọn phòng» trong khi lời b06 đang nói chung «việc gì to quá», và ví
  dụ đó thuộc về b07. So với frame locked cùng mốc (1.45s: khung sạch, mắt dồn vào Thầy
  và highlight «chia nhỏ ra»), bản test đông hơn mà nói ít hơn.

**Kết luận Part B: crack accent làm cảnh xấu đi. Zero-doodle là bản đúng cho beat này;
không render bản "integrated demo" final.** File test giữ tại
`/workspace/doodle-integrated-r2-*.png`, `/workspace/locked-b06-*.png` để đối chiếu.

## 5. Cổng doodle đề xuất — CHƯA áp, chờ Hiệp duyệt

Đề xuất thay nội dung doodle trong L-049 (`logs/lessons.md`) và 3 đoạn doodle ở
`skills/make-video/SKILL.md` (dòng 73–75) bằng cổng sau. **Chưa sửa file nào trong hai
file đó ở commit này.**

> **Cổng doodle (đề xuất, thay L-047/L-048/L-049 khi Hiệp duyệt):** Doodle bị CẤM mặc
> định. Chỉ được dùng khi đạt CẢ 4 điều kiện, ghi rõ trong fx table của beat:
> (1) **Nội dung là hành động vẽ/viết/cắt/nối/đường đi** — bỏ nét vẽ đi thì beat mất
> nghĩa, không phải mất "điểm nhấn". (2) **Vẽ trên vật đang tồn tại trong cảnh** —
> không chế vật mới để vẽ lên, không hình vẽ lơ lửng trong khoảng trống, vật được vẽ
> phải tồn tại tiếp hoặc biến thành vật tiếp theo của chính cảnh. (3) **Cùng nhịp với
> cảnh** — dùng easing/timing của transition/prop đang chạy (tdev/mmx), `at` khoá theo
> cụm từ giọng và sfx như `dropAt` hiện tại; không dùng doodleEase riêng. (4) **Tối đa
> 1 khoảnh khắc vẽ mỗi clip**, trừ khi script thật sự đòi hơn và Hiệp duyệt trước.
> Vẫn phải render still trước/giữa/sau và đọc mắt cạnh frame locked cùng beat; still
> nào đông hơn mà nói ít hơn → bỏ doodle, giữ bản cũ. 4 demo doodle hiện tại
> (`doodle-demo-brand`, `doodle-creative-demo`, `doodle-assets-demo`,
> `doodle-morph-demo`) + test crack b06 là rejected reference: giữ để nhớ vì sao bị
> loại, không lấy làm chuẩn.

