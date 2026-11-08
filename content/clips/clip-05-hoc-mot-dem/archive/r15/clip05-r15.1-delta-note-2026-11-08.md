# r15 → r15.1 PATCH1 — delta note, không verdict craft

Đã đọc TOÀN review actual cập nhật. Steering mới nhất thu hẹp lỗi chắc cònK1/S01. Báo cáo trên đĩa còn ghiK2/S18; **không tự sửaS18**, để Deep chấm diễn đạt trênSHA mới. Giữ conceptE, không reset L095, không mổ thân.

## Delta thực tế

### S01 — thay
Trước:
> Sinh viên đọc lại cùng đoạn, hai ngày sau vẫn nhớ ít ý hơn so với đoạn đã tự viết từ trí nhớ.

Sau:
> Trong thí nghiệm, đọc lại thua tự viết về số ý sinh viên nhớ đúng sau hai ngày, ở hai đoạn khác nhau.

Bỏ “cùng đoạn”; có “hai đoạn khác nhau”. Đưa phép so đọc lại/tự viết lên trước sinh viên, nhưng giới hạn nó ngay trong một câu có “thí nghiệm”, “số ý…nhớ đúng”, “sau hai ngày”. “Thua” chỉ kết quả phépso này, không “đọc lại làm quên”/mọi người/mọi thời gian. Chưa kết luận nghe một lần đã hết lỗ nghĩa.

### S03 — KHÔNG thay sau steering thu hẹp
> Có, tự viết vẫn hơn ở mốc một tuần trong thí nghiệm năm 2006 này.

S01giờ đã giới thiệu thí nghiệm, nên “thí nghiệm…này” có antecedent trong chính lời. Không báo giả đã thay hai câu. Bản r15gốc và mọi payload S02,S03,S04–21 giữ nguyên bytes; không sửa S18/câu hỏi/promise/payoff/bridge/method.

## Năm mở câu đã tự thử — cùng nhịp ƯỚC2.9, không TTS/người thật

Ba giây tương đương8.7whitespaceunits. Cột đầu3sghi8unitsđãhoàn tất; unit9 có thể đang được nói, không mặc định đã nghe hết.

| # | Nguyên mở câu | 8unitsđầu | Độ dài / soát nghĩa |
|---|---|---|---|
| 1 | Trong một thí nghiệm, đọc lại thua tự viết về số ý sinh viên nhớ đúng sau hai ngày. | Trong một thí nghiệm, đọc lại thua tự | 19units, ngắn hơn, nhưng 8unitsđầu kết thúc ở “tự”, tớiunit9mới hoàn tất phépso; chưa nêu hai đoạn riêng. |
| 2 | Trong thí nghiệm, đọc lại thua tự viết về số ý sinh viên nhớ đúng sau hai ngày, ở hai đoạn khác nhau. | Trong thí nghiệm, đọc lại thua tự viết | 23units, chọn: nguồncaseởđầu, phépso hoàn tấtunit8, ai/outcome/delay/haiđoạn có trong cùng câu. Không cùngđoạn vôquychiếu. Không phải câu shock rồi đính chính. |
| 3 | Đọc lại thua tự viết về số ý sinh viên nhớ đúng sau hai ngày trong một thí nghiệm với hai đoạn khác nhau. | Đọc lại thua tự viết về số ý | 24units; so sánh đến sớm nhưng nguồncaseđến cuối, dễ nghe thành khái quát trước khi được giới hạn; không chọn. |
| 4 | Trong một thí nghiệm, sinh viên nhớ ít ý hơn ở đoạn đọc lại so với đoạn tự viết sau hai ngày. | Trong một thí nghiệm, sinh viên nhớ ít | 22units; có người và outcome, nhưng đầu3s mới tới “ít”, chưa ra so sánh hai thao tác; thiết kế hai đoạn còn kém rõ. |
| 5 | Trong một thí nghiệm, đọc lại thua tự viết từ trí nhớ về số ý sinh viên nhớ đúng sau hai ngày ở hai đoạn khác nhau. | Trong một thí nghiệm, đọc lại thua tự | 27units; rõ tựviếtlàrecall, nhưng dài hơn và phépso hoàn tấtunit9. Không cần thêm trínhớ vào hook vì S07–08giữ nguyên làm rõ thao tác. Không chọn. |

**Mốc chữ của câu chọn:** scope“Trong thí nghiệm” hoàn tấtunit3≈1.03s; “đọc lại thua tự viết” hoàn tấtunit8≈2.76s; “số ý” unit11≈3.79s; người“sinh viên” unit13≈4.48s; “nhớ đúng” unit15≈5.17s; “sau hai ngày” unit18≈6.21s; “hai đoạn khác nhau” hếtunit23≈7.93s. Những số này chỉ phépchia đơn vị, **không timing giọng hoặc chứng minh người nghe hiểu trong3s**. Không tăng tốc để nhét ai/outcome/delay vào3s. Rủi ro3sđược nâng bằng việc đưa phépso sớm, chưa tự đóng craft.

## Các cặp câu thay đổi/nghĩa quy chiếu
- S01→S02: “sau hai ngày / đọc lại thua tự viết” → “Sau một tuần / tự viết còn hơn đọc lại”: cùng phépso, đổi mốc.
- S02→S03: “còn hơn…không?” → “Có…vẫn hơn ở mốc một tuần”; “thí nghiệm…này” trỏ “thí nghiệm”S01, năm2006là định danh thêm.
- S03→S04: trả chiều → hứa phépso cụthể và câu hỏi; giữ nguyên. S04–21giữ mọi mối nối đã được reviewer đóng.

## Checksum bảo toàn

- Requested aggregate S02,S04–S21 (LF nối câu, giữLFcuối): `7a66e8992b4d0a77f8ad685d07dfb797b70ee4c189aede3596e189c64f3175ff`; trước=sau, assert bytes thật.
- Toàn bộ tail sauS01, gồm separator vàS02–21vàLFcuối: `400e4b394f1d57a65775ed96ca38d788aeb04806caa45c569f070b9bbc1cf696`; trước=sau. Đây là kiểm mạnh hơn vì cảS03cũng nguyên bytes.
- S03riêng, UTF8khôngLF: `c2338af663b583215a3fce824f2fe47d5a231ece82ca9935eed706ca12d16e67`.
- Hash riêng từng câu được ghi trong structured counts-auditJSON; chỉS01đổi. Đã assert thay S01mới vềcũ khôi phục **toàn payload r15 cũ**, không chỉ số câu.

## Counts / trạng thái
433whitespaceunits,21câu,9beat; EN62chunks, max8words. ƯỚC179.01sở2.9và202.90sở2.5, giữ11.7snghỉ/4stransition/14sendcard. Không ép nhịp; target120–180chỉcảnhbáo, tổng thành phẩm strict<300sphảiđothậtsauChốt.

ExactspokenSHA256: `ee0e5aa879d3e2fa373e9aa3edab91d2a84d0f7c42c519755d718f40c5750652`. Bytes sau TOÀNdòngopeningmarker+LF, trướcclosingmarker, giữLFcuối. FileSHAđược ghi ngoài draft sau hai modechecker.

Nghĩa/craft CHƯAPASS; Deep/SocialexactSHA CHƯAKIỂM; người thật/actualtiming CHƯAKIỂM. Không contact/repo/commit/media/nguồn mới.

FileSHA256 cuối: `57322fba5e105ae0e81c290d0aefbb0d9b4ceef12449d2a01ff4d39b3c60183c`. Hai mode đã chạy: --subjects0error/0warning; --l0880error/1warningngoàiclipdir, rawvàauditcùngthưmục.
