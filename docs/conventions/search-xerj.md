---
title: "Tìm kiếm bằng XERJ: repo + repo tham khảo"
date: 2026-10-28
source: "oneup-studio (soạn trong repo); https://xerj.org/llms.txt"
id: search-xerj
type: convention
status: active
updated: 2026-11-26
tags: [search, xerj, reference-coding, reuse-first]
---
# Tìm kiếm bằng XERJ: repo + repo tham khảo

XERJ (https://xerj.org, binary Rust, cài ở box: `~/.local/bin/xerj`, bản `v1.0.0-rc.100`) là **công cụ tìm mặc định** trong repo này.
`rg` / `git grep` chỉ là phương án dự phòng (node chưa chạy, cần regex chính xác, hoặc file vừa sửa chưa index lại).

## Luật: tìm repo tham khảo trước khi viết code pipeline mới
Trước khi viết code mới trong `pipeline/`, `video-engine/` hoặc script render/TTS/phụ đề:
1. `xerj search --prefix work-oneup-studio "..."`: repo mình đã có chưa (reuse-first, GUIDE.md).
2. `xerj search --prefix ref "..."` / `xerj def --prefix ref "<tên hàm>"`: các dự án gần nhất đã giải bài này thế nào.
3. Trích `path:line` của đoạn đã đọc vào commit/PR hoặc ghi chú. Kiểm giấy phép (bảng dưới) trước khi chép: **AGPL / UNLICENSED chỉ đọc cách làm, không chép code**.
4. Không có kết quả liên quan thì nói rõ, rồi làm bình thường. Thư viện phổ biến mà mình đã thuộc thì không cần tra.

## Lệnh
```sh
export PATH="$HOME/.local/bin:$PATH" XERJ_DISABLE_FEEDBACK=true
pipeline/scripts/xerj-index.sh            # bật node nếu chưa chạy + index lại cả hai (project|ref|all)
xerj search --prefix work-oneup-studio -k 5 "f5 word timestamps prosody"     # repo này
xerj search --prefix ref   -k 5 "subtitle word boundary srt"      # repo tham khảo
xerj def    --prefix ref   "create_subtitle"                      # đi tới định nghĩa
```
- **Prefix repo này: `work-oneup-studio`**, ghi ở `.xerj-prefix` (gốc repo, nguồn duy nhất). Không dùng `oneup` (trên Mac đã thuộc repo khác `~/work/oneup`) hay `oneup-studio` (thuộc một checkout cũ đã xoá). XERJ không cho hai thư mục chung một prefix, và không được xoá index của thư mục khác để giành prefix.
- Node (Mac local): chạy bằng `xerj-ensure` (launchd `org.xerj.server`, data `~/xerj-data`, loopback 127.0.0.1:9200), **có auth**: `export XERJ_API_KEY="$(cat ~/xerj-data/admin.key)"` trước mọi lệnh `xerj`. Hook SessionStart `~/.claude/hooks/tools-ready.sh` tự bật node, đồng bộ index chạy nền và báo prefix cho agent ở đầu mỗi phiên. Data dir phải nằm **ngoài** thư mục được index.
- Index lại sau khi sửa nhiều file: chạy lại script (có journal, không nhân đôi). Exit `3` = xong, có file rác bị bỏ qua = **thành công**.
- Chế độ embed mặc định là **lexical** (BM25 + hashing), không phải neural: hãy hỏi bằng đúng từ/tên hàm trong code. (MiniLM neural chỉ tiếng Anh nên không bật.)
- Loại trừ: `.xerjignore` ở gốc repo (secret `.env*`, khoá, media wav/mp3/mp4/png/jpg, font, `node_modules`, venv, `media/`, `.vtt`, `.log`) + `.gitignore`.
- MCP (tuỳ chọn, cho agent có MCP): `{"mcpServers":{"xerj":{"command":"xerj","args":["mcp"]}}}` (`xerj` trong `PATH`, thường `~/.local/bin`).
- **Không** gửi field report / `xerj feedback --submit` / `hub feedback` (gửi dữ liệu ra ngoài): luôn đặt `XERJ_DISABLE_FEEDBACK=true`. Không bật `rerank` (gửi nội dung ra bên thứ ba).
- Không `DELETE` index; xoá một thư mục đã index bằng `xerj autoindex remove --prefix <p>`.

## Repo tham khảo (`~/oneup-tools/reference-repos/`, prefix `ref`)
Clone nông (`--depth 1`, sparse, bỏ media/font/model), nằm **ngoài** repo, không commit (xem `resources/refs/README.md`).

| Repo | Commit | Giấy phép | Vì sao gần pipeline của mình |
|---|---|---|---|
| krillinai/OpenCreator | d17bdc16 | Apache-2.0 | agent OpenCreator của nhóm; phụ đề, căn câu theo từ (`runtime/krillinai/internal/service/audio2subtitle.go`) |
| harry0703/MoneyPrinterTurbo | fd5127e8 | MIT | pipeline script → TTS → phụ đề → ghép video; SRT từ WordBoundary (`app/services/voice.py`) |
| YILS-LIN/short-video-factory | 6c98d090 | **AGPL-3.0** (chỉ đọc) | app tạo video ngắn tự động (Electron) |
| SWivid/F5-TTS | 45868aba | MIT (code; model CC-BY-NC) | engine giọng mình đang dùng (`pipeline/tts/f5tts_gen.py`) |
| remotion-dev/template-tiktok | a6263081 | **UNLICENSED / Remotion License** (chỉ đọc) | caption kiểu TikTok theo word timestamp trên Remotion |
| m-bain/whisperX | 5d3678b8 | BSD-2-Clause | forced alignment cho word timestamp (`whisperx/alignment.py`) |

Clone lại trên Mac:
```sh
mkdir -p ~/oneup-tools/reference-repos && cd ~/oneup-tools/reference-repos
for r in krillinai/OpenCreator harry0703/MoneyPrinterTurbo YILS-LIN/short-video-factory SWivid/F5-TTS remotion-dev/template-tiktok m-bain/whisperX; do
  n=${r#*/}; git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/$r $n
  printf '/*\n!*.png\n!*.jpg\n!*.gif\n!*.mp4\n!*.mp3\n!*.wav\n!*.ttf\n!*.ttc\n!*.woff2\n!*.zip\n!*.pt\n!*.safetensors\n!*.onnx\n' | git -C $n sparse-checkout set --no-cone --stdin
  git -C $n checkout -q
done
REPO="$(git -C <đường-dẫn-repo-oneup-studio> rev-parse --show-toplevel)"
cp "$REPO/.xerjignore" .xerjignore && printf '*.ttc\n*.node\n*.lock\npackage-lock.json\n' >> .xerjignore
"$REPO/pipeline/scripts/xerj-index.sh" ref
```
