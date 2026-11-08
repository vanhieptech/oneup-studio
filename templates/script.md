---
title: "<Clip NN vX: tiêu đề = thông điệp mục HTB>"
date: YYYY-MM-DD
type: script
tags: [script, <trụ>, howtolivebetter-<phần.mục>]
status: draft
source: "<HowToLiveBetter phần.mục (+ mục liên kết) · nguồn sơ cấp · trend/audio · callback clip trước>"
id: clip-NN.script-final
version: vX
supersedes: archive/script-v<X-1>.md
template: templates/script.md
---

**L-099 — Hiệp 08/11/2026 13:00 (Asia/Saigon), Rule Reviewer chuyển lời:** áp cho clip đang viết lại và clip mới. Tổng video **strict <300s**, gồm **end card, khoảng nghỉ và chuyển cảnh**; **120–180s chỉ là mục tiêu/cảnh báo**, không phải minimum. Bỏ quota từ toàn bài/beat/đoạn trước phương pháp; giữ đủ ngữ cảnh và nguồn + so sánh + kết quả/giới hạn, không kéo dài bằng lặp ý và không tăng tốc đọc để nhét. Trước Chốt ghi **ƯỚC/estimate** theo nhịp đọc tự nhiên (kèm end card/nghỉ/chuyển cảnh); chỉ đo thời lượng thật từ audio/video sau Chốt. Đây **không phải Chốt**, không miễn **W-16**; chưa Chốt: không hình/voice/render/publish.
# <Clip NN vX: tiêu đề>

Chuẩn từ clip-02 v16/v17 (Hiệp duyệt cấu trúc 16/10/2026). Bắt buộc cho mọi script mới (make-video §2).

**Thông điệp (nói thành lời ở beat Thông điệp):** <tiêu đề mục HTB, gần nguyên văn> · **Dấu hiệu/cơ chế:** <2–3 ý nguồn> · **Cách làm:** <động tác nguồn + mục liên kết, ví dụ cụ thể giờ/chỗ/việc>
**ƯỚC thời lượng tổng:** <đọc tự nhiên + nghỉ chủ ý + chuyển cảnh + end card = …s; target 120–180s chỉ cảnh báo; strict <300s>. Spec có thể ghi `estimated_pauses_s` / `estimated_transitions_s` cho nghỉ/chuyển cảnh thêm ngoài nhịp đọc tự nhiên; số từ không là gate.

**Ký hiệu:** `|` tách phrase (một lần F5/phrase) · `{nhấn: …}` chữ stem/ruột nhấn cao, to, kéo dài · câu stem rơi giọng cuối (L-036). Giọng: <nhân vật = F5 preset, speed, semitone>.

## Khung beat theo mạch ý (120–180s là mục tiêu, tổng strict <300s; L-099)

Cột giây bên dưới là **ƯỚC**, thay bằng đọc tự nhiên của bản lời hiện tại, gồm end card/nghỉ/chuyển cảnh; không áp nhịp mẫu cũ. Beat có thể chia nhiều shot mà giữ nguyên câu/nguồn.
| Beat | Giây | Vai trò | Bắt buộc |
|---|---|---|---|
| b01 Hook | ƯỚC mở đầu | pain/câu hỏi rõ nghĩa, chữ to frame 0 | `{nhấn:}` 1 chữ, hit SFX frame 0 |
| b01b Hook (cut) | ƯỚC tiếp hook | vế còn lại, cut cứng hình đối lập | ≥ 1 cut + ≥ 2 hit trong 0–3s (rule-55) |
| b02–b06 Vấn đề | ƯỚC theo lời | stem meme / tình huống ×3 + chen ngang 1–2s | mỗi stem tách stem \| ruột \| đuôi, nhấn chữ ruột (L-036) |
| b07 Bằng chứng | ƯỚC theo lời | "Nghe quen hông?" + nguồn + số thật + 2–3 dấu hiệu | đúng fact lock, nói "kết quả"/"lượt" đúng loại số |
| b08 Thông điệp | ƯỚC theo lời | tiêu đề mục HTB nói thành lời + 1 câu mức chứng cứ nhẹ (tương quan…) | nhân vật phụ phản ứng 1 câu |
| b09 Cách làm 1 | ƯỚC theo lời | động tác nguồn: hỏi/đổi → ví dụ siêu nhỏ | không mắng, ví dụ cụ thể |
| b09c Cách làm 2 | ƯỚC theo lời | mục liên kết (nếu-thì giờ/chỗ, chia nhỏ, tự đặt ngày…) + callback clip trước nếu tự nhiên | đủ ngữ cảnh, không quota từ |
| b10 CTA | ƯỚC theo lời | lặp thông điệp 1 vế + câu hỏi + "Comment một chữ" | loop về hook, 1 CTA |

## Biến thể: Độc thoại chia sẻ (clip concept meme «bản chất», L-039)
- **Một người nói** từ b01 tới b10 (mặc định Thầy; cột «Người nói» chỉ một tên). Không đối thoại, không nhân vật phụ chen ngang.
- Bỏ beat chen ngang (b02, b05); phản ứng ở b08 thành một câu của chính người nói («Mà … hóa ra là …»); CTA cũng do người đó nói.
- Nhân vật khác (chibi Hiệp…) chỉ diễn trong cột Hình: dán, ôm đầu, gật, tròn mắt.
- Giữ nguyên stem «Thì cái bản chất… / Thứ nhất / Thứ hai / Và cuối cùng» + `{nhấn:}` (L-036).

## Ví dụ phải phổ thông (L-040)
- Hook và ví dụ chính lấy từ nỗi đau đa số người xem có: dọn nhà/phòng bừa, ôn thi/học tiếng Anh, làm báo cáo/luận văn, tập gym/giảm cân, tiền cuối tháng…
- Ưu tiên nỗi đau có thật trong comment/trend (`research/trends/<date>/apify/top-clips.md`, `final/trend-signals.md`), ghi nguồn + số like ở front-matter `source`.
- Không lấy ví dụ ngách của creator/dev (làm app, code, AI, deploy) trừ khi chủ đề clip là chính việc đó.

## Kịch bản
| Beat | Giây | Người nói | Lời thoại | Hình / caption EN |
|---|---|---|---|---|

## Thay đổi so với bản trước
## Fact lock
## Caption + hashtag

## Hook câu hỏi mở về nỗi đau nhức nhối (L-043)
- Câu đầu tiên (≤ 3s) là **câu hỏi mở** về một nỗi đau ai cũng có, lặp đi lặp lại, dai dẳng (lấy từ comment thật, L-040). Ví dụ: «Sao cái phòng mình hứa dọn hoài… mà ba tháng rồi vẫn y chang vậy ta?»
- Có cảm xúc (bực, thở dài) + tiểu từ Nam Bộ (*ta, hả, hà*). Hình frame 0 cho thấy nỗi đau, không chữ tiêu đề.
- Sau hook là **diễn giải**: nguyên nhân (người xem nhận ra mình) → bằng chứng (motion graphics, không bịa số) → thông điệp HTB nói thành lời → 2 ví dụ đời thường → callback → 1 CTA (loop về hook).
- Stem meme («bản chất»…) chỉ dùng khi tự nhiên với câu hỏi; nếu làm chậm vào nỗi đau thì bỏ.
- Ghi 2 hook câu hỏi dự phòng. Mục tiêu 120–180s không phải minimum; tổng gồm end card/nghỉ/chuyển cảnh strict <300s; không quota từ/beat, shot ≤8s không giới hạn câu; xen 1–3 từ tiếng Anh quen (task, deadline).

## Nói liền mạch, không chặt vụn (L-044)
- Mỗi beat là 1–2 câu nói tự nhiên, tách `|` thành **2–4 phrase** (tối đa 5), mỗi phrase ≥ 3 chữ; không chặt thành chuỗi mảnh 2–3 chữ.
- Beat sau mở bằng từ nối với beat trước (Vì…, Mà khoa học cũng thấy…, Còn…, Vậy thì…, Lấy … làm thử nha, … cũng vậy, Giống clip trước…, Thấy chưa…).
- Beat cần dài để rõ nghĩa/đủ nguồn thì chia nhiều shot (≤8s/shot), không cắt câu hay tăng tốc để nhét.
- check-rules `L-044` cảnh báo khi bảng script vi phạm.

## Bằng chứng cụ thể, ít tiểu từ, ví dụ ngôi «mình» (L-045)
- Beat bằng chứng nói đủ 3 ý: **ai** (tác giả/loại nghiên cứu) · **làm gì** (cho người ta làm gì, so nhóm nào, tổng hợp bao nhiêu loại nghiên cứu) · **thấy gì**. Đối chiếu với nguồn HTB (`book/` + `docs/核实记录/`): chỉ nói tới mức đã xác minh, bỏ «hơn hẳn», «chứng minh» nếu nguồn chỉ có hướng/tương quan.
- Suy luận của người nói (vd «việc to thường là việc mình ngán nhất») nói thành ý của mình, không gán cho nghiên cứu.
- Tiểu từ nha/nè/á: tối đa ~1 lần mỗi 2–3 beat; CTA được 1 «nha».
- Beat ví dụ nói ngôi «mình» làm mẫu («Như mình nè, «dọn phòng» mình chia ra…»), không ra lệnh cho người xem.
