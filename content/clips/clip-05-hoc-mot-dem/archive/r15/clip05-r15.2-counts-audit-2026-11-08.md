# r15.2 PATCH2 — final counts / exact preservation audit

**PREPARED PENDING OWNER COORDINATION APPROVAL.** Không contact/gửiReviewer/Deep/Social/News/Hiệp/nhờbotkhác; không commit/archive/repoedit/research/media/spec/stageplans. Không coi tinReviewer là đồng ý phối hợp của owner.

## SHA256
- File: `87885dd3f4e0b1d847e7971c0476878f85691e3178b55ff7cbae6f6a096f7dc2`
- Exactspoken: `3a6f280daede0ea30db9d095643deb7f77868981ea22b804991b3b425cf7a78e`
- Frozenr15.1file: `57322fba5e105ae0e81c290d0aefbb0d9b4ceef12449d2a01ff4d39b3c60183c`; đã assert file gốc vẫn nguyên.
- Extraction: UTF8 sau TOÀN dòngopeningmarker+LF, trước dòngclosingmarker, giữLFcuối; khôngstrip/normalize.

## Delta duy nhất
S18: “Tự viết cho tỷ lệ ý nhớ đúng cao hơn ở mốc này, nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.”

“Cao hơn” chỉ tỷ lệ ý nhớ đúng tại mốc1tuần ởS17. Không mứcđộnhỏ/lớn/đángkể/vượtrội/sốhiệuứng; không mọi mốc. S10đọc lại hơn5phút vàS17nofeedback/F5đều nguyênlời.

## Exact assertions đã thực hiện
- Changed sentence IDs = [S18]. MọiSxxkhác giữbytes, gồmS01/S03/S17/S19–21.
- ThayS18mới→cũ khôi phục toànpayloadfrozenr15.1, gồm separators/LFcuối.
- Sau dấu phẩyspace ởS18 giữ nguyên: “nhưng ngay cả kết quả ấy cũng không phải nhớ hết nội dung.”. TailSHA256(UTF8khôngLF): `72d95e19e2dd55403b7d2ea822e5e9ff06de2fa5445b7e7a09a06db56d5c3b5b`.
- NonS18aggregate orderedS01–17,S19–21,LFnối+LFcuối trước=sau: `00a768f35d801d65895cdb0a56e0016b8e240b99a72557927e842d71454c3b53`.
- Per-sentence hashes trongJSON; index21câu/beatwordcounts/cộtnguyênlờisau bỏnhấn/captionmapping/adapter9beat đều assert khớp.

## Counts / ƯỚC
439whitespaceVIunits;21câu,9beat;63ENchunks,max8words/chunk.
- 2.9units/s: 151.38s lời+11.7snghỉ+4stransition+14sendcard = 181.08sƯỚC.
- 2.5units/s: 175.60s lời+cùngphầnbù = 205.30sƯỚC.
Khôngtăngtốc/épnhịp; target120–180chỉcảnhbáo; tổng thành phẩmstrict<300sphảiđothậtsauChốt. Nghỉ/transition/endcardcũgiữnguyên, annotationtimingcậpđúngdelta6unitsS18.

## Checker text-safe đã chạy
--subjects: exit0,1check,0error,0warning.
--l088: exit0,6checks,0error,1warningngoàiclipdir: “bản nháp không nằm trong thư mục clip → không tìm được file trend / fact của clip”.
Raw `clip05-r15.2-subjects-2026-11-08.txt` và `clip05-r15.2-l088-2026-11-08.txt`. Chỉ hai mode, khôngfullchecker. NhãnPASStrongraw không là nghĩa/craft/nguồn/ownerapproval.

Nguồn và craft/nghĩa trênSHA mới CHƯA KIỂM; humanđọcto/nghe1lần/ngườilạ/actualtiming CHƯAKIỂM. Không kế thừa tổngPASSr15.1.
