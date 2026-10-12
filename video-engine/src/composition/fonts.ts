import { continueRender, delayRender, staticFile } from "remotion";

/** Be Vietnam Pro for ALL on-screen text (rule-15). Loaded from public/fonts → brand/fonts. No network. */
export const FONT_FAMILY = "Be Vietnam Pro";
const WEIGHTS: [string, number][] = [["Regular", 400], ["Medium", 500], ["SemiBold", 600], ["Bold", 700]];

let started = false;
export function ensureFonts() {
  if (started || typeof document === "undefined") return;
  started = true;
  const handle = delayRender("Loading Be Vietnam Pro");
  Promise.all(
    WEIGHTS.map(([file, weight]) => {
      const f = new FontFace(FONT_FAMILY, `url(${staticFile(`fonts/BeVietnamPro-${file}.ttf`)}) format("truetype")`, { weight: String(weight) });
      return f.load().then((loaded) => { document.fonts.add(loaded); });
    }),
  )
    .then(() => continueRender(handle))
    .catch((e) => { console.error("Font load failed", e); continueRender(handle); });
}
