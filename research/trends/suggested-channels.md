---
title: "Đề xuất kênh mới nên theo dõi (2026-11-28)"
date: 2026-11-28
id: trends-suggested-channels
type: trend-digest
status: active
updated: 2026-11-28
tags: [trends, discovery, radar, global-channels]
source: "pipeline/scripts/channel-discover.py (zero-token auto-discovery)"
---
# Đề xuất Kênh Mới Nên Theo Dõi (2026-11-28)

Các kênh ngoài `pipeline/trends/radar.yaml` có video đạt lượt xem cao hoặc lặp lại nhiều lần trong kết quả quét gần đây. Hiệp duyệt dòng nào thì dán snippet JSON vào `radar.yaml`.

| Kênh | Nền tảng | Ngôn ngữ | Vai trò gợi ý | Hits | Max Views | Video mẫu |
|---|---|---|---|---:|---:|---|
| `@TED` | youtube | `en` | `global_niche_source` | 1 | 62,311,640 | Inside the Mind of a Master Procrastinator / Tim Urban / TED |
| `@TEDEd` | youtube | `en` | `global_niche_source` | 1 | 11,143,291 | Why you procrastinate even when it feels bad |
| `@JustinSung` | youtube | `en` | `global_niche_source` | 1 | 10,322,503 | How to Remember Everything You Read |
| `@TEDx` | youtube | `en` | `global_niche_source` | 1 | 437,080 | Why You Procrastinate - and How to Stop it for Good / Elyssa Smith / TEDxBabsonCollege |
| `@easywayactually1` | youtube | `en` | `global_niche_source` | 1 | 128,158 | How To Remember Everything You Read — 4 Science-Backed Steps |

## Snippet sẵn dán vào `pipeline/trends/radar.yaml`

```json
{"handle": "TED", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/@TED/shorts", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "TEDEd", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/@TEDEd/shorts", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "JustinSung", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/@JustinSung/shorts", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "TEDx", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/@TEDx/shorts", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "easywayactually1", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/@easywayactually1/shorts", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
```
