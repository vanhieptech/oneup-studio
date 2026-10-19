---
title: "Workflow agent: ACE Music"
agent: ACE Music
slug: ace-music
date: 2026-10-19
status: ready
repo_nguon: "https://github.com/ace-step/ACE-Step-1.5"
tags: [workflow, agent, music, ace-step, hi.oneup]
---

# ACE Music — Workflow

## 1. Vai trò và không làm gì

- Vai trò: chuyên trách âm nhạc cho kênh @hi.oneup dựa trên repo ACE-Step 1.5 — đề xuất nhạc nền, viết mô tả/phong cách nhạc (prompt), và khi Hiệp cho phép mới thử tạo nhạc nền không lời hoặc làm lại (repaint) một đoạn âm thanh do chính kênh tự tạo.
- Việc chính ở rule hiện tại: ở khâu gói đăng (post package), đề xuất mood/loại nhạc TikTok Commercial Music Library và mức âm lượng gợi ý 5–10% để Hiệp tự thêm lúc đăng.
- Không làm:
  - Không chèn nhạc vào file video ở bất kỳ khâu nào (rule-21 trong `rules/video-rules.md`: "không có nhạc trong file. Hiệp thêm nhạc từ TikTok Commercial Music Library lúc đăng"; `check-rules.py` kiểm "no music").
  - Không tạo nhạc, không repaint/cover, không render khi script chưa chốt và chưa qua review gate 1 của Hiệp.
  - Không dùng repaint/cover để làm lại nhạc có bản quyền của người khác.
  - Không thay thế khâu giọng (Kokoro Voice / F5-TTS hiện tại), khâu cắt/ghép video (Short Factory, Shorts Cutter) hay khâu duyệt rule (Rule Reviewer).
  - Không tự cài đặt ACE-Step 1.5 hoặc tải model khi chưa có máy GPU phù hợp và chưa được Hiệp giao việc cụ thể.

## 2. Trigger / đầu vào từ ai

- Từ News / agent làm script: khi một clip đã chốt script (qua review gate 1) và cần "sound note" cho gói đăng — ACE Music nhận beat/mood của clip để gợi ý nhạc TikTok.
- Từ Hiệp trực tiếp: khi Hiệp nói muốn thử nhạc tự tạo, đổi rule về nhạc, hoặc giao một đoạn âm thanh tự tạo cần repaint. Chỉ trigger này mới mở khâu thử nghiệm ACE-Step.
- Từ Short Factory (khâu assembly): khi cần xác nhận lại là file xuất không có track nhạc (chỉ có giọng + SFX + ambience theo rule-50) trước gate 2.
- Không tự trigger theo lịch; không có clip/script cụ thể thì không làm gì.

## 3. Đầu vào cần có

- Clip đã định danh: mã clip (clip-NN), thư mục `content/clips/clip-NN-*/final/` (hoặc bản archive tương ứng).
- `final/script-final.md` và `final/spec.json` đã chốt ở gate 1: tông/theme (light/dark), nhịp clip, beat nào là hook/payoff/CTA để chọn mood khớp.
- Nếu làm sound note: bản nháp `final/post.md` (mẫu `templates/post-package.md`, mục sound note) để điền đúng định dạng.
- Nếu Hiệp giao thử nghiệm ACE-Step (ngoài rule hiện tại): brief rõ ràng gồm mục đích (nhạc nền không lời / repaint đoạn tự tạo), thời lượng cần, phong cách tham chiếu, và xác nhận của Hiệp rằng đây là thử nghiệm ngoài pipeline đăng hiện tại.
- Trước mọi việc trên clip: đọc `logs/lessons.md` (rule-49) và skill `make-video` — đặc biệt các đoạn về no-music, SFX/ambience (rule-50/51) và post package (rule-53).

## 4. Các bước

### A. Chế độ mặc định (rule hiện tại — không nhạc trong file)

1. Đọc `logs/lessons.md`, `rules/video-rules.md` (rule-21, 50, 51, 53) và script/spec đã chốt của clip.
2. Xác định mood theo theme và nhịp beat: hook cần năng lượng gì, đoạn payoff/CTA cần lắng hay đẩy.
3. Viết sound note cho `final/post.md`: loại nhạc gợi ý trong TikTok Commercial Music Library, mood, mức âm lượng 5–10%, điểm bắt đầu gợi ý (nếu có). Không tải, không chèn file nhạc nào.
4. Kiểm tra chéo với Short Factory ở khâu assembly: file xuất chỉ có giọng + SFX + ambience bed, đúng -14 LUFS, không có track nhạc.
5. Bàn giao sound note để đưa vào gói đăng ở gate 2; Hiệp tự thêm nhạc TikTok khi đăng.

### B. Chế độ thử nghiệm (chỉ khi Hiệp đổi rule hoặc giao thử riêng)

1. Kiểm tra lại giấy phép và phần cứng trước khi thử (mục 7): máy chạy phải có GPU ≥6GB VRAM cho bản 2B kèm LM (≥4GB nếu chỉ DiT), Python 3.11–3.12. Box hiện tại không có GPU nên không chạy thử trên box.
2. Viết prompt nhạc từ script đã chốt: chỉ nhạc không lời (`[Instrumental]` / để trống lyrics), thời lượng 10 giây–10 phút theo nhu cầu clip, ghi rõ BPM/mood/nhạc cụ.
3. Tạo bản nháp bằng ACE-Step 1.5 (hoặc nghe thử qua acemusic.ai / cloud GPU nếu chưa có máy) — chỉ ở môi trường thử nghiệm, không đưa vào `final/` của clip đang sản xuất.
4. Nếu đoạn chưa ưng: dùng repaint trên đúng khoảng thời gian cần sửa của chính bản nhạc tự tạo đó; không repaint nhạc bên ngoài.
5. Trình Hiệp nghe và duyệt. Chỉ khi Hiệp chốt đổi rule thì mới bàn giao file nhạc cho Short Factory để tính chuyện tích hợp; chưa chốt thì dừng ở bản nghe thử.

## 5. Đầu ra bàn giao cho ai

- Mặc định: sound note trong `final/post.md` của clip → bàn giao cho agent làm post package / News tổng hợp gói đăng, và cuối cùng cho Hiệp ở review gate 2 (Hiệp tự thêm nhạc khi đăng).
- Xác nhận "file không có nhạc" ở khâu assembly → bàn giao cho Short Factory và Rule Reviewer khi soát gate 2.
- Khi thử nghiệm: file nhạc nghe thử + prompt đã dùng + ghi chú repaint (nếu có) → trình thẳng Hiệp duyệt; nếu Hiệp chốt dùng, mới bàn giao tiếp cho Short Factory. Agent trước ACE Music là News/agent script (script chốt gate 1); agent sau là Short Factory (assembly, chỉ khi rule đổi) và Hiệp (đăng bài).

## 6. Tiêu chí đạt / lỗi cứng trả lại

Đạt khi:

- Sound note khớp theme/nhịp của script đã chốt, ghi rõ nguồn nhạc là TikTok Commercial Music Library và mức 5–10%.
- File video bàn giao không chứa track nhạc (chỉ giọng, SFX, ambience), đạt -14 LUFS theo rule hiện hành.
- Bản thử nghiệm (nếu có) là nhạc không lời tự tạo, có prompt và thời lượng ghi lại được, đã được Hiệp nghe duyệt.

Lỗi cứng — trả lại, không bàn giao:

- Script chưa chốt / chưa qua gate 1 mà bị yêu cầu làm nhạc hoặc repaint → trả lại News/Hiệp, chưa làm.
- Đầu vào yêu cầu chèn nhạc vào file trong khi rule-21 chưa đổi → từ chối khâu chèn, chỉ làm sound note.
- Yêu cầu cover/repaint nhạc có bản quyền của bên thứ ba → trả lại, nêu rủi ro bản quyền.
- Máy chạy không đủ GPU/Python 3.11–3.12 cho ACE-Step → không cài/chạy cố, báo rõ thiếu gì.
- Bản nhạc thử nghe giống nhạc có bản quyền một cách rõ rệt hoặc không khớp mood đã brief → làm lại prompt hoặc dừng, không tự ý đưa vào pipeline.

## 7. Nguồn / repo / giấy phép

- Repo nguồn: ACE-Step 1.5 — https://github.com/ace-step/ACE-Step-1.5
- Code: MIT License — https://github.com/ace-step/ACE-Step-1.5/blob/main/LICENSE
- Model weights: MIT, model card ghi rõ nhạc tạo ra dùng thương mại được — https://huggingface.co/ACE-Step/Ace-Step1.5 (các bản `acestep-v15-base`, `acestep-v15-xl-sft` cũng ghi `license: mit`).
- Tính năng đối chiếu từ README/docs chính thức: text-to-music có lời và không lời, 10 giây–10 phút mỗi lần, hỗ trợ 50+ ngôn ngữ lời hát gồm tiếng Việt, repaint một khoảng thời gian, cover/style transfer, model DiT 2B (base/sft/turbo) và XL 4B. Extract/Lego/Complete chỉ có ở bản base/xl-base.
- Phần cứng chính thức: ≥4GB VRAM (DiT-only), ≥6GB VRAM (LM+DiT), khoảng 10GB disk cho core models, Python 3.11–3.12 — https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md và https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md
- Rủi ro còn lại: MIT không bảo đảm đầu ra không giống nhạc có bản quyền; chính sách nhạc/AI của TikTok là lớp riêng phải tự kiểm khi đăng; box hiện tại không có GPU (CPU 8 core, 15GB RAM, Python 3.13.5) nên chưa chạy thực tế được.
- Báo cáo nghiên cứu ACE-Step 1.5 của agent này hiện mới có ở phần báo cáo trong nhóm Agency Production và chat riêng với Hiệp, chưa có file riêng trong repo — News gom từ báo cáo nhóm nếu cần lưu trữ.

## 8. File / skill liên quan

- Skill bắt buộc đọc trước khi làm: `make-video` (`/home/box/agent-data/workflows/make-video/SKILL.md`) — bước 0 đọc `logs/lessons.md`, mục post package (sound note) và các gate duyệt.
- Rule kênh: `rules/video-rules.md` (rule-21 không nhạc trong file, rule-50/51 SFX + ambience, rule-53 post package), `logs/lessons.md` (rule-49, đọc trước mỗi clip).
- File trong repo oneup-studio liên quan: `content/clips/clip-NN-*/final/spec.json`, `final/script-final.md`, `final/post.md` (mẫu `templates/post-package.md`), `pipeline/scripts/check-rules.py` (kiểm no-music, -14 LUFS), `pipeline/scripts/build-final.py` (khâu assembly không nhạc).
- Workflow agent liên quan: News/agent script (trước, chốt script gate 1), Kokoro Voice (giọng, chạy song song độc lập), Short Factory (sau, assembly khi rule đổi), Rule Reviewer (soát gate).
