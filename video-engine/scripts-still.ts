import {readFileSync} from "node:fs";
import path from "node:path";
import {getBundle} from "./src/rendering/render";
import {validatePlan} from "./src/validation/validate";
// render one still per scene: usage tsx scripts-still.ts <plan.json> <outPrefix>
const file = process.argv[2], prefix = process.argv[3] ?? "/workspace/doodle-meaning";
const planRaw = JSON.parse(readFileSync(file,"utf8"));
const v = validatePlan(planRaw);
if(!v.ok){ console.error(v.issues); process.exit(1); }
console.log("validate ok", v.issues.map(i=>i.message));
const serveUrl = await getBundle();
const {selectComposition, renderStill} = await import("@remotion/renderer");
const {findBrowser} = await import("./src/rendering/render");
const browserExecutable = findBrowser() ?? null;
let frameOffset = 0;
for (let i=0;i<v.plan.scenes.length;i++){
  const scenePlan = {...v.plan, scenes:[v.plan.scenes[i]]};
  const comp = await selectComposition({serveUrl, id:"ComicVideo", inputProps:{plan:scenePlan}, browserExecutable});
  const out = `${prefix}-frame${i+1}.png`;
  await renderStill({serveUrl, composition:comp, inputProps:{plan:scenePlan}, output:out, frame:45, browserExecutable});
  console.log("still", out);
}
