---
id: video-engine
type: guide
status: active
updated: 2026-10-13
tags: [video-engine, remotion, comic, characters, pipeline, rule-45]
---
# video-engine: comic character video từ scene plan (Remotion + React + TS)

Hệ thống render video comic có nhân vật cố định (Hiệp, Omi) từ **JSON scene plan** hoặc **script text**. Hoàn toàn tất định: cùng plan → cùng từng frame. Không dùng AI tạo ảnh/video. LLM chỉ là tuỳ chọn để lập kế hoạch cảnh, tắt đi vẫn chạy.

## Setup
```bash
cd video-engine
npm ci            # Node ≥ 18 (đã chạy trên Node 20)
npm run typecheck && npm test
```
- **Bắt buộc:** Node, npm packages trong `package.json` (remotion, @remotion/cli|renderer|bundler, react 18, zod 3), Chrome/Chromium (tự tìm `/usr/bin/google-chrome`, Chromium, Chrome trên macOS; hoặc đặt `REMOTION_BROWSER=/path`). Không có Chrome thì Remotion tự tải Chrome Headless Shell (cần mạng 1 lần).
- **Tuỳ chọn:** `ffmpeg`/`ffprobe` (lệnh `frames`, test e2e), một endpoint LLM OpenAI-compatible (vd. Ollama local, miễn phí) cho `--llm`.
- Font: `public/fonts` là symlink tới `../../brand/fonts` (Be Vietnam Pro, OFL), nạp local bằng `FontFace` + `delayRender`, **không gọi mạng**.

## Lệnh
| Lệnh | Việc |
|---|---|
| `npm run preview` | Remotion Studio (preview, chỉnh props trực tiếp). Composition `ComicVideo` (mặc định = clip-01 story) và `CharacterSheet` (QA mọi biểu cảm). |
| `npm run validate -- examples/*.json examples/*.txt` | Chỉ validate, nhanh, không mở browser. Lỗi kèm đường dẫn và giá trị hợp lệ. |
| `npm run plan -- script.txt --out plan.json [--llm]` | Script text → JSON plan (rule-based; `--llm` chỉ khi có `LLM_BASE_URL` + `LLM_MODEL`). |
| `npm run render -- a.json b.txt ... --out-dir out` | Validate **tất cả** trước, file nào lỗi thì không render gì. Sau đó render từng file thành `out/<plan.id>.mp4` (H.264, CRF 18, yuv420p, không tiếng) dùng chung 1 bundle (cache theo hash `src/`+`examples/` trong `.bundle-cache/`). |
| `npm run frames -- out/x.mp4 --every 0.5` | Trích frame + `contact-sheet.png` để soát hình (luật 34). |
| `npm run build` | `remotion bundle` ra `build/` (kiểm tra bundle production). |
| `RENDER_E2E=1 npm test` | Thêm test e2e: render thật 1 giây, kiểm MP4 bằng ffprobe và kiểm frame không trống. |

Tái tạo ví dụ: `npm run render -- examples/clip-01-story.json examples/debugging-story.json examples/sample-script.txt --out-dir out` (~45s cho 16s video trên box).

## Kiến trúc
```
script.txt ─▶ scenes/textFormat (parse) ─▶ scenes/planner (rule-based)  ┐
            └▶ providers/llm (tuỳ chọn, OpenAI-compatible, fallback) ┘─▶ VideoPlan (JSON)
VideoPlan ─▶ validation (zod + semantic, theo character profiles) ─▶ animation/timing (buildTimeline)
          ─▶ animation/controller (CharacterState mỗi frame, hàm thuần) ─▶ characters/CharacterRenderer → rigs/*.tsx (SVG)
          ─▶ composition/ComicComposition → SceneRenderer (Background, Caption, NarrationBox, DialogueBubble, transitions)
          ─▶ Remotion Studio (preview) / rendering/render.ts (renderMedia → MP4)
```
| Thư mục | Vai trò |
|---|---|
| `src/validation/schema.ts` | Schema zod: VideoPlan, Scene, CharacterCue, Dialogue, CharacterProfile + từ vựng chuẩn |
| `src/validation/validate.ts` | Validate ngữ nghĩa: trùng id, thời lượng, action/expression/pose không hỗ trợ theo profile, thiếu profile, thoại ngoài cảnh, speaker không có trong cảnh, transition/background/framing sai, Omi trước tuần 5 (luật 11), đi khi đang ngồi, kích thước lẻ |
| `src/characters/profiles/*.json` + `registry.ts` | Character profile (dữ liệu), parse 1 lần, dùng lại cho mọi video |
| `src/characters/rigs/` | Rig SVG React: `ChibiHiep.tsx`, `OmiBlob.tsx` (port từ `pipeline/characters-v2/chars.html`) |
| `src/animation/` | `timing.ts` (giây→frame, easing, spring, hash01 có seed, timeline), `controller.ts` (state controller) |
| `src/composition/` | Component video + `CharacterSheet` |
| `src/scenes/` | Định dạng script text + planner rule-based |
| `src/providers/llm/` | Interface `ScenePlannerProvider`, `RuleBasedPlanner`, `OpenAICompatiblePlanner`, `getPlanner`, `planWithFallback` |
| `src/rendering/render.ts`, `src/cli.ts` | Bundle cache, tìm Chrome, render, CLI batch |

**Tất định:** mọi chuyển động là hàm thuần của `useCurrentFrame()`/fps. Không `Math.random`, timer hay đồng hồ thật. Biến thiên mỗi nhân vật dùng `hash01(profile.id)`. Có test so sánh state và SVG markup ở cùng frame.

**Transition:** cảnh sau phủ lên cảnh trước trong `transition.duration` đầu tiên của nó (cảnh trước được giữ thêm đúng số frame đó). Vì vậy tổng thời lượng = Σ duration, không bị trừ.

## Nhân vật và trạng thái hỗ trợ
| | Hiệp (`hiep`, rig `chibi-hiep`) | Omi (`omi`, rig `liquid-omi`) |
|---|---|---|
| Biểu cảm | neutral, happy, sad, surprised, confused, focused | như Hiệp (morph hình dạng thân kiểu chất lỏng giữa các biểu cảm) |
| Hành động | idle, talking, thinking, typing, walking, reacting | idle, talking, thinking, walking, reacting (không có tay nên không typing) |
| Tư thế | standing, sitting | standing (lơ lửng), sitting (đậu xuống đất) |
| Ghi chú | Ngoại hình còn generic, chờ Hiệp tả/gửi ảnh (DL-022) | Chỉ từ tuần 5 (luật 11, validator chặn). Giọng chưa chốt (DL-023) nên chỉ bubble chữ |

Chuyển động có sẵn: thở (squash/stretch), chớp mắt theo chu kỳ riêng mỗi nhân vật + chớp ép khi đổi biểu cảm, blend biểu cảm 0.28s, nhép miệng theo nhịp âm tiết trong khoảng thoại, nghiêng đầu, liếc mắt, vung tay, bước đi tới `toX`, nhảy squash khi reacting, enter (`pop`, `rise`, `slide-left/right`), exit (`fade`, `slide-*`), camera push-in, framing `wide/medium/closeup`.

Thêm nhân vật mới: thêm `profiles/<id>.json` (theo `CharacterProfileSchema`) + rig trong `RIGS` (`CharacterRenderer.tsx`), cộng `RIG_HEAD_TOP`/`RIG_SIZE`. Không phải sửa scene hay composition.

## Định dạng input
### JSON scene plan (nguồn chuẩn, render tất định)
Xem `examples/clip-01-story.json` (clip 01 beat 1–3, chỉ Hiệp, tuần 1) và `examples/debugging-story.json` (Hiệp + Omi, tuần 6). Thời gian tính bằng **giây, tương đối trong cảnh**.
```jsonc
{ "version": 1, "id": "my-video", "meta": { "clip": "clip-01", "week": 1 },
  "video": { "width": 1080, "height": 1920, "fps": 30, "theme": "light" },          // mặc định như vậy
  "scenes": [{
    "id": "b01", "duration": 4, "beat": "clip-01.b01",
    "background": { "kind": "desk" },                 // paper | ink | desk | bed | grid
    "camera": { "framing": "medium", "push": 0.05 },  // wide | medium | closeup
    "transition": { "type": "cut", "duration": 0.4 }, // cut | fade | slide | wipe | iris
    "narration": { "text": "11:48 PM", "start": 0.2 },
    "characters": [{ "characterId": "hiep", "x": 0.4, "pose": "sitting", "action": "typing", "expression": "focused",
                     "expressionChanges": [{ "at": 2, "value": "happy" }], "actionChanges": [{ "at": 1, "value": "idle" }],
                     "enter": "none", "exit": "none", "facing": "right", "toX": 0.6 }],
    "dialogue": [{ "speaker": "hiep", "text": "“**Mai học.**”", "start": 2.05, "end": 3.85, "style": "speech" }], // speech|thought|shout, **đậm** = nhấn
    "caption": { "text": "My study plan… “tomorrow.”", "start": 0.9, "end": 3.9, "highlight": [3] },
    "sfx": [{ "name": "pop", "at": 2.05 }]            // cue cho bước mix sau, video engine không phát âm thanh
  }]
}
```
### Script text (rule-based planner)
Xem `examples/sample-script.txt` và chú thích đầu `src/scenes/textFormat.ts`:
```
# title: Mai hoc demo
@video 1080x1920 30fps light week=1 clip=clip-01
@cast hiep
== night | 4.5s | bed | medium | cut
NARRATION: 11:48 PM
hiep (sitting, thought): Thôi… **mai học**.
hiep (sad): Mai của mình dài cả tuần luôn á.
== turn | 5s | grid | medium | iris:0.5
CAPTION: if… then… [0, 1]
hiep (happy, reacting, shout): Nếu 9 giờ tối, thì mở **listening**!
SFX: ding @2.4
```
Tag đầu tiên của mỗi nhân vật là trạng thái ban đầu, tag sau thành `expressionChanges`/`actionChanges` tại lúc câu đó bắt đầu. Dòng không có tag thì planner đoán biểu cảm từ từ khoá/dấu câu (VI + EN). Thời gian thoại chia theo tốc độ đọc ~15 ký tự/giây. Văn xuôi không có header `==` được tách 1–2 câu/cảnh.

### LLM (tuỳ chọn)
`LLM_BASE_URL=http://localhost:11434/v1 LLM_MODEL=qwen2.5 npm run plan -- script.txt --llm`. Kết quả LLM phải qua cùng validator. Nếu lỗi mạng, JSON hỏng hoặc plan không hợp lệ thì tự quay về rule-based và ghi rõ trong log. Không cài SDK của hãng nào.

## Giọng Omi (luật 46) <a name="voice"></a>
Cài một lần (box/Mac, CPU, miễn phí, không API):
```bash
python3 -m venv /workspace/tts-venv
/workspace/tts-venv/bin/pip install vieneu "onnxruntime==1.22.1"   # 1.31 lỗi external-data với cache HF
export VIENEU_PYTHON=/workspace/tts-venv/bin/python                  # mặc định là đường dẫn này
```
Luồng: `npm run voice -- plan.json` → với mỗi câu của nhân vật có `voice` trong profile (chỉ Omi), gọi `pipeline/tts/vieneu_tts.py` (preset "Kim Thanh", tag cảm xúc + tempo/pitch theo `emotion`, cắt lặng, loudnorm) → `public/voice/<hash>.wav` + `.json` (duration, envelope theo frame) → ghi `plan.voiced.json` (điền `dialogue[].audio`, kéo dài `end` nếu cần) và validate lại. `npm run render -- plan.voiced.json` sẽ tự bật audio (AAC 192k). Validator chặn audio gắn vào người thật. Clip có giọng Omi phải bật nhãn AI khi đăng.

Mẫu đầy đủ (comic + giọng Omi + HyperFrames explainer + ghép): `content/samples/sample-full-w5/README.md`.

## HyperFrames ở đâu (ranh giới)
- **Remotion = engine chính cho beat kể chuyện (comic, luật 42).** Nhân vật là component React dùng lại được, state theo frame, test được bằng vitest.
- **HyperFrames (`templates/hyperframes-base`) giữ cho beat giải thích/motion graphics** (số liệu, sơ đồ, GSAP timeline), như luật 42 và pipeline cũ.
- Không trộn hai engine trong một lần render. Mỗi engine xuất MP4 1080×1920 30fps riêng, ghép ở bước dựng bằng `pipeline/scripts/join-beats.sh` (xfade + −14 LUFS). HyperFrames CLI cần Node ≥ 22 (box: `/workspace/tools/node-v22.20.0-linux-x64/bin`). Browser capture không cần cho render thường; `pipeline/characters-v2/render.js` (puppeteer) chỉ còn là công cụ thử rig cũ.

## Giấy phép
- **Remotion** dùng [Remotion License](https://www.remotion.dev/license): **miễn phí cho cá nhân và công ty ≤ 3 người**. Công ty lớn hơn cần Company License. @hi.oneup hiện là cá nhân nên dùng miễn phí. Nếu sau này OneUp có > 3 nhân sự thì phải xem lại.
- Be Vietnam Pro: SIL OFL (`brand/fonts/OFL-BeVietnamPro.txt`). zod, React: MIT. Không asset hay model AI nào trong đường render.

## Giới hạn đã biết
- Hiệp vẫn là avatar generic (tóc/kính/quần áo chưa xác nhận).
- `sfx` mới là cue dữ liệu, chưa mix. Giọng: chỉ Omi có audio (VieNeu-TTS, luật 46), miệng Omi theo envelope audio thật. Hiệp chưa có bản thu nên miệng Hiệp vẫn nhép theo nhịp chữ.
- Không có lớp grain phim (luật 20) trong engine; comic dùng chấm nền. Thêm grain ở bước ghép nếu Hiệp muốn.
- VieNeu không tất định (sampling); tính lặp lại nhờ cache theo hash, xoá `public/voice/<hash>.*` để tạo lại.
- `facing: "left"` lật cả rig, nên dấu "?" của biểu cảm confused cũng bị lật.
- Background mới có 5 bộ (paper, ink, desk, bed, grid), props cố định (chưa có điện thoại cầm tay, sách...).
- Bubble tự đặt trên đầu speaker. Hai bubble cùng lúc của hai người đứng gần có thể chồng nhau, cần chỉnh `x` trong plan.
- Caption nằm khoảng y 1490–1700 của khung 1920. Phần dưới cùng (~220px) để trống cho UI TikTok, nhưng caption 3 dòng sẽ chạm vùng này.
- Render trên box mất ~2.7s mỗi giây video (CPU). Final vẫn render trên Mac theo luật cũ.
