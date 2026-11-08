# Clip05 r15.1 PATCH1 — counts / preservation audit

Status: nghĩa/craft CHƯA PASS; Deep/Social exactSHA CHƯA KIỂM; người thật/actualtiming CHƯA KIỂM. Không Chốt.

## Exact hashes
- FileSHA256: `57322fba5e105ae0e81c290d0aefbb0d9b4ceef12449d2a01ff4d39b3c60183c`
- SpokenSHA256: `ee0e5aa879d3e2fa373e9aa3edab91d2a84d0f7c42c519755d718f40c5750652`
- Originalr15fileSHA256: `8a1110ae9b715e770b27bfb29879ef969376a948cd1046bf89531c3884752aa2`; file gốc còn nguyên.
- Extraction: sau TOÀNdòngopeningmarker+LF, trướcclosingmarker, giữLFcuối, UTF8khôngnormalize/strip.

## Scope thật
Chỉ S01 thay. Steering mới nhất thu hẹp lỗi chắc K1; S03giữnguyên vì S01đã giới thiệu “thí nghiệm”, S18để Deep chấm từ “nhỉnh hơn”. Không đổi mọi câu hỏi/promise/payoff/method/bridge khác, không resetconcept.

## Bảo toàn bytes
- S02,S04–21aggregate (LFnốicâu+LFcuối): `7a66e8992b4d0a77f8ad685d07dfb797b70ee4c189aede3596e189c64f3175ff`; trước=sau.
- Toàn bộ tail sauS01gồm separators/S02–21/LFcuối: `400e4b394f1d57a65775ed96ca38d788aeb04806caa45c569f070b9bbc1cf696`; trước=sau.
- S03riêng (UTF8khôngLF): `c2338af663b583215a3fce824f2fe47d5a231ece82ca9935eed706ca12d16e67`.
- Hash riêng từng câu trongJSON. Assert thay S01mới bằngS01cũ khôi phục toàn payload r15cũ. Không chỉ so số câu/từ.
- Index21câu/cột lời sau bỏnhấn/caption mapping/adapter9beat đều khớp nguyênpayload; captionnhấnS01cậpnhật, phần còn lại giữ nguyên.

## Counts / ƯỚC
433whitespaceVIunits,21câu,9beat;62ENchunks,max8words. S01vẫn23units nhưng phépso đưa lênunit8≈2.76s; không phải claim người nghe hiểu toàn pain trong3s. Năm mở câu và mốc chữ nằm trongdelta note.

2.9units/s:149.31s lời+11.7snghỉ+4stransition+14sendcard=179.01sƯỚC.
2.5units/s:173.20s lời+cùngphầnbù=202.90sƯỚC.
Giữgiảđịnhnghỉ/transition/endcardcũ. Target120–180chỉcảnhbáo; khôngtăngtốc/épnhịp. Tổngthànhphẩm strict<300sphảiđothậtsauChốt.

## Hai mode checker đã chạy thật
- --subjects: exit0;1check,0error,0warning.
- --l088: exit0;6checks,0error,1warning: “bản nháp không nằm trong thư mục clip → không tìm được file trend / fact của clip”.
- Raw `clip05-r15.1-subjects-2026-11-08.txt`, `clip05-r15.1-l088-2026-11-08.txt`. NhãnPASStrongraw chỉphầnmáy, khôngnghĩa/craft/nguồn.
- Không checkerfull/stageplans/modekhác/media/contact/repoedit/commit/nguồnmới.
