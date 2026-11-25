# clip-05 v4 — prosody plan (bản đọc cho F5, News) · rev 1 · 21/10/2026

Nguồn lời: `content/clips/clip-05-hoc-mot-dem/script-v4-LOCKED.md` (91848a3, cùng chữ với 8ec205e, Hiệp «Chốt» 21/10 23:01). **Không đổi chữ nào** (L-072): `mkchunks.py` (voice-work/clip-05-v4) ghép 18 chunk lại và `assert` bằng đúng lời 8 beat của file LOCKED (219 chữ). Phiên âm chỉ áp vào chữ nhập F5; caption/spec giữ chữ gốc.

Giọng: F5 · Thái Sơn (`assets/voice-refs/thai-son.wav`), speed 1.0 (L-074, đọc nhanh), plan A nếu nói thuần ≤ 47,9s, không thì plan B. Mỗi chunk = một lần gọi F5 (L-016), không cắt bên trong output trừ điểm lặng ở ký hiệu nghỉ có sẵn trong lời.

## Ký hiệu nghỉ

| Ký hiệu | Ý nghĩa | Plan A (s) | Plan B (s) | Đạt khi đo |
|---|---|---|---|---|
| `//hook` | nối 2 câu hook b01 (L-027) | 0,08 | 0,08 | ≤ 0,10 |
| phẩy trong hook | dấu phẩy trong c01/c02 (L-027, v18 R8) | ≤ 0,10 | ≤ 0,10 | ≤ 0,10 |
| `/` | dấu phẩy (nối chunk hoặc phẩy trong chunk) | 0,18 | 0,15 | 0,12–0,22 |
| `//breath` | **mới (Hiệp/News 21/10): nghỉ thở ngắn sau số đếm «Một.» và «Hai.» ở dòng 5** | 0,28 | 0,25 | plan −0,04…+0,05 |
| `//` | hết câu trong beat | 0,35 | 0,30 | plan −0,03…+0,05 |
| `//¦` | hết beat | 0,40 | 0,40 | plan −0,03…+0,05 |

Thứ bậc: phẩy < nghỉ thở sau số < hết câu < hết beat. Không nghỉ nào > 0,5s. «Một.»/«Hai.» không đứng một mình trong lần gọi F5 (< 4 âm tiết, L-016): chúng nằm đầu chunk cùng câu sau, rồi được cắt tại điểm lặng thấp nhất giữa «Một»/«Hai» và chữ kế tiếp và đặt đúng 0,28s.

## Chunk

| # | Beat | Lời (gốc) | Chữ nhập F5 (nếu khác) | Nhấn (+≥2 dB, không đổi tempo) | Nghỉ sau | Seed |
|---|---|---|---|---|---|---|
| c01 | b01 Hook | Bạn học dồn một đêm cho cả kỳ, sáng ra vẫn làm được đề. | — | «một đêm» | `//hook` | 6 |
| c02 | b01 | Một tuần sau, bạn còn nhớ bao nhiêu? ↗ | — | «bao nhiêu» | `//¦` | 6 |
| c03 | b02 Ví dụ | Ví dụ mình ôn chương Di truyền ba tiếng liền trước hôm thi giữa kỳ. | — | «ba tiếng liền» | `//` | 3 |
| c04 | b02 | Tới cuối kỳ gặp lại dạng lai hai cặp tính trạng, mình không nhớ cách giải. | — | «không nhớ» | `//¦` | 3 |
| c05 | b03 Nguyên nhân | Một nghiên cứu cho sinh viên đọc một bài hai lần liền. | — | — | `//` | 3 |
| c06 | b03 | Khi kiểm tra ngay, họ có điểm cao hơn người chỉ đọc một lần, | — | — | `/` | 3 |
| c07 | b03 | nhưng hai ngày sau họ không còn hơn nữa. | — | «không còn hơn» | `//` | 3 |
| c08 | b03 | Còn ai đọc lần hai cách một tuần thì hai ngày sau vẫn hơn người đọc một lần. | — | «cách một tuần» | `//¦` | 3 |
| c09 | b04 Mục tiêu | Mình cần là tới cuối kỳ mình vẫn nhớ chương đó. | — | «vẫn nhớ» | `//¦` | 3 |
| c10 | b05 Cách làm | Nên cùng ba tiếng đó, mình làm thế này. | — | — | `//` | 3 |
| c11 | b05 | Một. `//breath` Mình chia ra ba ngày, mỗi ngày một tiếng, theo đúng ví dụ trong cẩm nang. | — | «ba ngày» | `//` | 6 |
| c12 | b05 | Hai. `//breath` Mỗi buổi, mình gấp sách tự kiểm như clip trước. | — | «tự kiểm» | `//¦` | 6 |
| c13 | b06 Bằng chứng | Khi gom 317 thí nghiệm lại, | Khi gom **ba trăm mười bảy** thí nghiệm lại, | — | `/` | 6 |
| c14 | b06 | các nhà nghiên cứu thấy người học muốn nhớ càng lâu thì khoảng cách giữa các lần ôn càng phải dài. | — | «càng phải dài» | `//¦` | 3 |
| c15 | b07 Kết quả | Khi mình làm đủ hai bước đó, | — | — | `/` | 3 |
| c16 | b07 | tới cuối kỳ gặp lại dạng lai hai cặp tính trạng, mình dễ nhớ ra cách giải hơn. | — | «dễ nhớ ra» | `//¦` | 3 |
| c17 | b08 CTA | Còn bạn, môn sắp thi còn cách mấy hôm? ↗ | — | «mấy hôm» | `//` | 6 |
| c18 | b08 | Comment số hôm nha. | Com men số hôm nha. | «số hôm» | (hết thoại → end card) | 6 |

Nhấn: tối đa 1 chỗ/câu, ≤ 2 chỗ/beat (P-08). Chỗ nhấn do News đề xuất (bản LOCKED không đánh `{nhấn:}`) — **Rule Reviewer chấm/sửa được mà không đổi lời**. Câu hỏi c02 («nhiêu», thanh ngang) và c17 («hôm», thanh ngang) không thuộc miễn L-082 → âm tiết cuối phải đo lên ≥ +0,5 st.

## Rủi ro F5 (chỉ chữ nhập, lời giữ nguyên)
- **317** → «ba trăm mười bảy» (Hiệp/News 21/10). STT quy số về chữ trước khi so.
- **clip** (c12) đọc chữ gốc; kiểm STT vi + STT en trên đúng đoạn từ. Nếu nghe ra chữ khác thì thử «cờ líp» (chỉ chữ nhập).
- **Comment** (c18) → «Com men» như clip-04 (R6). STT en trên đoạn từ.
- **«Một.» / «Hai.»** có thể bị F5 đọc liền vào chữ sau, hoặc STT nuốt mất (1 âm tiết đứng đầu): cần STT câu có chữ «một»/«hai» ở đầu; 6 seed.
- **«Mình cần là tới cuối kỳ»** (c09): không lặng sau «là» (như R9 v18).
- **«lai hai cặp tính trạng»** (c04, c16): không ngắt giữa cụm.
- Câu dài c14 (24 âm tiết): không lặng ≥ 0,25s ở chỗ không có dấu câu, đặc biệt «càng lâu thì», «khoảng cách giữa».

## Kiểm sau khi sinh (ghi vào `final/prosody-measure-c05v4.md`)
1. STT từng câu ≥ 0,8 (mục tiêu ≥ 0,9) sau khi quy số/từ EN về cách đọc.
2. Nghỉ đo đúng bảng trên; nghỉ thở sau «Một»/«Hai» 0,24–0,33s.
3. Không lặng ≥ 0,25s giữa cụm (cờ chặn), ≥ 0,12s ở cụm cấm ngắt (cảnh báo).
4. Nhấn ≥ +2 dB so câu và so chữ kề.
5. Câu hỏi c02, c17 lên ≥ +0,5 st ở âm tiết cuối.
6. Tổng giọng ≤ 58s; −14 LUFS ±1; một take/chunk, `intra_output_cuts` chỉ ở ký hiệu nghỉ.
7. **Dừng trước render** — Rule Reviewer chấm giọng trước.

## Kết quả lần sinh 1 (c05v4, 22/10 00:35 UTC+7) — chi tiết ở `prosody-measure-c05v4.md`
- 18 chunk, 101 take F5 (3–10 seed/chunk). Tổng giọng 53,57s (nói thuần 47,44s → plan A), −14,1 LUFS. Cờ chặn còn 1 (c18 STT).
- Nghỉ thở sau «Một» 0,27s, sau «Hai» 0,30s (plan 0,28).
- Phẩy trong chunk chỉnh tại điểm lặng (`voice-work/clip-05-v4/fixcommas.py`, cách làm v18): c01 «kỳ,» 0,20→0,08 (hook L-027) · c04 «trạng,» 0,36→0,18 · c06 «ngay,» 0,23→0,18 · c10 «đó,» chèn tới 0,18 · c11 «ngày,» 0,11→0,18 · c17 «bạn,» chèn tới 0,18.
- **c18 đổi chữ nhập F5** (chỉ chữ nhập): «Com men» và «Comment» STT 0,2–0,6 trên 12 take → «Cô men số hôm nha.» (take c18-11c, STT lúc chọn 0,8, trên file giao 0,6 «Cô mình số hôm nha»). Cần nghe tai.
- STT nghi ngờ, cần nghe tai: «lai» → «like» ở c04/c16 (mọi take, có thể do whisper), «môn» → «muốn» ở c17 (10/10 take), «Di truyền» → «dì truyền» (c03), «cẩm nang» → «cẩm năng» (c11), «chương đó» → «chân đó» (c09 bản giao).
