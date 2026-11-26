---
name: social-poster
description: >-
  Use when Hiệp sends a link (article, study, HowToLiveBetter page, product page, an approved
  @hi.oneup clip) and asks for an X or LinkedIn post ("làm nháp X/LinkedIn từ link này",
  "viết bài từ link", "lên lịch đăng"). Reads the source, writes two separate drafts in the
  OneUp voice with every claim traced to the source, self-checks claims and credit, and saves a
  draft file. Draft-only: never posts, schedules or logs in.
version: "1.0.0"
metadata:
  author: OneUp Studio
  tags:
    - social
    - x
    - linkedin
    - draft-only
---
# Social poster (link → X + LinkedIn drafts)

Rebuilt from the retired box agent `docs/legacy-box/workflows-agents/social-poster.md` (26/11/2026). Pattern reference only: [langchain-ai/social-media-agent](https://github.com/langchain-ai/social-media-agent) (MIT); nothing vendored.

## Never
- Post, schedule, retweet or reshare, or sign in to Hiệp's X/LinkedIn. "Lên lịch đăng" means: propose a day and time; Hiệp posts himself.
- Store tokens, passwords or API keys anywhere in the repo.
- Add a number, quote, OneUp feature or outside fact that isn't in the link (rule 40, P-03).
- Imply the source author endorses OneUp.
- Mark a draft `published` before Hiệp confirms he posted it.

## Inputs
- The link. Optional: angle, target (default both X and LinkedIn), CTA toward OneUp/Omi, preferred time.
- If the link won't open or has too little content: say so and stop. Don't write from the title.

## Steps
1. **Read the source** (ego-browser skill for pages that need a browser; plain fetch otherwise). Pull the main idea, the checkable numbers/quotes with their exact passage, and the original link.
2. **Source summary**: 3–5 lines so Hiệp can check quickly.
3. **Two separate drafts**, voice from `content/voice-profile.md`, run through `skills/humanizer` (embedded mode) and the paste test in `skills/script-polish` step 2:
   - **X**: ≤280 characters (count and write the count), one idea, a clear hook, soft OneUp/Omi CTA only when it fits; link at the end or as a reply note.
   - **LinkedIn**: 3–6 short paragraphs, opens with the insight, ends with one discussion question, OneUp/Omi mentioned naturally, ≤3 hashtags.
   - HowToLiveBetter content: add «Nội dung dựa trên 'Cẩm nang sống đáng giá' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/» (+ "đã chuyển thể" when adapted, rule 13).
   - Health, finance, legal: add «Thông tin tham khảo, không thay thế tư vấn chuyên gia».
4. **Self-check before showing Hiệp** (the old Rule Reviewer pass, short form): every claim maps to a source passage, said at the source's strength (no "chứng minh", "thay đổi cuộc đời"); credit present when required; no endorsement wording; no belittling the reader (L-053). Fix and re-check; never send a draft that fails.
5. **Save** `content/published/social/YYYY-MM-DD-<slug>.md` with front-matter `title, date, type: social-draft, tags, status: draft, source: <link>`, containing: summary + link, X draft + character count, LinkedIn draft, claim → source list, points for Hiệp to check, proposed time (only if asked). Run `python3 pipeline/scripts/build-index.py`.
6. **Hiệp's verdict**: duyệt / sửa (exactly what) / bỏ / viết lại. Edit only what he asked, without widening claims. Status flow: `draft` → `ready` (Hiệp approved, waiting for him to post) → `published` (only after he says it's posted; then add the link to the file).

## Output to Hiệp
The two drafts, the X character count, the summary, the check points and the file path. Status line: `nháp chờ duyệt` / `đã sửa theo góp ý` / `Hiệp đã duyệt — chờ Hiệp tự đăng`.

## Troubleshooting
| Symptom | Cause | Fix |
|---|---|---|
| Link unreadable / paywalled | No source text | Ask Hiệp for the text or another link; don't guess |
| Draft sounds like AI | Humanizer skipped | Re-run humanizer + paste test |
| A claim has no matching passage | Added from memory | Cut it or ask Hiệp for a source |
