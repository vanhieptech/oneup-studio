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
| `@UClHVl2N3jPEbkNJVx-ItQIQ` | youtube | `en` | `global_niche_source` | 2 | 1,806,410 | How To Defuse Procrastination And Be Productive (Without Using Willpower); Why You Can’t Stop Scrolling (End-Stage Screen Addiction) |
| `@UCAuUUnT6oDeKwE6v1NGQxug` | youtube | `en` | `global_niche_source` | 1 | 62,311,532 | Inside the Mind of a Master Procrastinator / Tim Urban / TED |
| `@UCJ24N4O0bP7LGLBDvye7oCA` | youtube | `en` | `global_niche_source` | 1 | 11,381,770 | I learned a system for remembering everything |
| `@UCsooa4yRKGN_zEE8iknghZA` | youtube | `en` | `global_niche_source` | 1 | 11,143,218 | Why you procrastinate even when it feels bad |
| `@UCL2QpphEeZFYwk6-WXD6hpA` | youtube | `en` | `global_niche_source` | 1 | 6,041,870 | Why People with ADHD Procrastinate (And 4 Brain-Based Ways to Get Started) |
| `@UCoOae5nYA7VqaXzerajD0lg` | youtube | `en` | `global_niche_source` | 1 | 857,257 | How To Remember Everything You Learn |
| `@UCsT0YIqwnpJCM-mx7-gSA4Q` | youtube | `en` | `global_niche_source` | 2 | 437,080 | Why You Procrastinate - and How to Stop it for Good / Elyssa Smith / TEDxBabsonCollege; 3 Steps to Memorize Everything. FAST. / Henry Hildebrandt / TEDxUniMannheim |
| `@UCHZO-4-l3XgfXdb4cE-gp7w` | youtube | `en` | `global_niche_source` | 1 | 558,839 | How to remember what you read / Nishant Kasibhatla |

## Snippet sẵn dán vào `pipeline/trends/radar.yaml`

```json
{"handle": "UClHVl2N3jPEbkNJVx-ItQIQ", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/channel/UClHVl2N3jPEbkNJVx-ItQIQ", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "UCAuUUnT6oDeKwE6v1NGQxug", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/channel/UCAuUUnT6oDeKwE6v1NGQxug", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "UCJ24N4O0bP7LGLBDvye7oCA", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/channel/UCJ24N4O0bP7LGLBDvye7oCA", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "UCsooa4yRKGN_zEE8iknghZA", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/channel/UCsooa4yRKGN_zEE8iknghZA", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
{"handle": "UCL2QpphEeZFYwk6-WXD6hpA", "platform": "youtube", "lang": "en", "role": "global_niche_source", "format_compatibility": "story_metaphor", "url": "https://www.youtube.com/channel/UCL2QpphEeZFYwk6-WXD6hpA", "followers": 0, "niche": ["productivity", "tu-duy"], "niche_verified": true},
```
