import { TRANSITION_TYPES } from "../composition/transitions"; // L-041: accept tdev-*/mmx-* too
import { ZodError } from "zod";
import {
  ACTIONS, BACKGROUNDS, DOODLE_KINDS, EXPRESSIONS, FRAMINGS, POSES, TRANSITIONS,
  VideoPlanSchema, type VideoPlan,
} from "./schema";
import { defaultRegistry, type ProfileRegistry } from "../characters/registry";

export interface PlanIssue { path: string; message: string; severity: "error" | "warning" }
export type ValidationResult =
  | { ok: true; plan: VideoPlan; issues: PlanIssue[] }
  | { ok: false; plan?: undefined; issues: PlanIssue[] };

const list = (xs: readonly string[]) => xs.join(", ");

/** Structural (zod) + semantic validation. Run before any expensive render. */
export function validatePlan(input: unknown, registry: ProfileRegistry = defaultRegistry): ValidationResult {
  let plan: VideoPlan;
  try {
    plan = VideoPlanSchema.parse(input);
  } catch (e) {
    if (e instanceof ZodError) {
      return { ok: false, issues: e.issues.map((i) => ({ path: i.path.join(".") || "(root)", message: i.message, severity: "error" as const })) };
    }
    throw e;
  }
  const issues: PlanIssue[] = [];
  const err = (path: string, message: string) => issues.push({ path, message, severity: "error" });
  const warn = (path: string, message: string) => issues.push({ path, message, severity: "warning" });

  const { fps } = plan.video;
  if (plan.video.width % 2 || plan.video.height % 2) err("video", `width/height must be even for H.264 (got ${plan.video.width}x${plan.video.height})`);

  const seen = new Map<string, number>();
  plan.scenes.forEach((s, si) => {
    const p = `scenes[${si}](${s.id})`;
    if (seen.has(s.id)) err(`${p}.id`, `duplicate scene id "${s.id}" (also scenes[${seen.get(s.id)}])`);
    seen.set(s.id, si);
    if (Math.round(s.duration * fps) < 1) err(`${p}.duration`, `duration ${s.duration}s is shorter than one frame at ${fps}fps`);
    if (!(BACKGROUNDS as readonly string[]).includes(s.background.kind)) err(`${p}.background.kind`, `unsupported background "${s.background.kind}". Use one of: ${list(BACKGROUNDS)}`);
    if (!(FRAMINGS as readonly string[]).includes(s.camera.framing)) err(`${p}.camera.framing`, `unsupported framing "${s.camera.framing}". Use one of: ${list(FRAMINGS)}`);
    if (!(TRANSITION_TYPES as readonly string[]).includes(s.transition.type)) err(`${p}.transition.type`, `unsupported transition "${s.transition.type}". Use one of: ${list(TRANSITIONS) + " (+ tdev-*/mmx-*)"}`);
    if (s.transition.type !== "cut" && s.transition.duration > s.duration / 2) err(`${p}.transition.duration`, `transition ${s.transition.duration}s is longer than half the scene (${s.duration}s)`);
    if (si === 0 && s.transition.type !== "cut") warn(`${p}.transition`, "first scene transitions in from blank paper");

    const ids = new Set<string>();
    s.characters.forEach((c, ci) => {
      const cp = `${p}.characters[${ci}]`;
      const prof = registry.get(c.characterId);
      if (!prof) { err(`${cp}.characterId`, `no character profile "${c.characterId}". Known: ${list([...registry.keys()])}`); return; }
      if (ids.has(c.characterId)) err(`${cp}.characterId`, `character "${c.characterId}" appears twice in one scene`);
      ids.add(c.characterId);
      const check = (kind: string, v: string, global: readonly string[], allowed: readonly string[], path: string) => {
        if (!global.includes(v)) err(path, `unknown ${kind} "${v}". Known ${kind}s: ${list(global)}`);
        else if (!allowed.includes(v)) err(path, `${prof.name} does not support ${kind} "${v}". Supported: ${list(allowed)}`);
      };
      check("pose", c.pose, POSES, prof.poses, `${cp}.pose`);
      check("action", c.action, ACTIONS, prof.actions, `${cp}.action`);
      check("expression", c.expression, EXPRESSIONS, prof.expressions, `${cp}.expression`);
      c.expressionChanges.forEach((ch, k) => {
        check("expression", ch.value, EXPRESSIONS, prof.expressions, `${cp}.expressionChanges[${k}].value`);
        if (ch.at > s.duration) err(`${cp}.expressionChanges[${k}].at`, `at=${ch.at}s is after scene end (${s.duration}s)`);
      });
      c.actionChanges.forEach((ch, k) => {
        check("action", ch.value, ACTIONS, prof.actions, `${cp}.actionChanges[${k}].value`);
        if (ch.at > s.duration) err(`${cp}.actionChanges[${k}].at`, `at=${ch.at}s is after scene end (${s.duration}s)`);
      });
      if (c.pose === "sitting" && (c.action === "walking" || c.actionChanges.some((a) => a.value === "walking"))) err(`${cp}.action`, "cannot walk while sitting; use pose=standing");
      if (prof.availableFromWeek && plan.meta.week && plan.meta.week < prof.availableFromWeek)
        err(`${cp}.characterId`, `${prof.name} may only appear from week ${prof.availableFromWeek} (plan is week ${plan.meta.week}; rule-11)`);
    });
    if (s.characters.length > 3) warn(`${p}.characters`, "more than 3 characters in a 9:16 frame gets crowded");

    s.dialogue.forEach((d, di) => {
      const dp = `${p}.dialogue[${di}]`;
      if (!ids.has(d.speaker) && d.speaker !== "narrator") err(`${dp}.speaker`, `speaker "${d.speaker}" is not in this scene's characters (${list([...ids]) || "none"})`);
      if (d.end <= d.start) err(dp, `end (${d.end}s) must be after start (${d.start}s)`);
      if (d.end > s.duration + 1e-9) err(`${dp}.end`, `dialogue ends at ${d.end}s but scene is only ${s.duration}s`);
      const sp = registry.get(d.speaker);
      if (d.audio && !sp?.voice) err(`${dp}.audio`, `"${d.speaker}" has no synthetic voice profile in its character profile; AI voice only for characters with a declared VieNeu preset (Hiệp chibi, Omi), never cloned (rule-46)`);
      if (d.audio && d.start + d.audio.duration > s.duration + 0.05) err(`${dp}.audio`, `voice line (${d.audio.duration}s) runs past scene end (${s.duration}s)`);
    });
    (s.caption?.segments ?? []).forEach((sg, gi) => {
      if (sg.end <= sg.start) err(`${p}.caption.segments[${gi}]`, `segment end (${sg.end}s) must be after start (${sg.start}s)`);
      if (sg.end > s.duration + 1e-9) err(`${p}.caption.segments[${gi}].end`, `segment ends at ${sg.end}s but scene is only ${s.duration}s`);
      const prev = s.caption!.segments![gi - 1];
      if (prev && sg.start < prev.end - 1e-9) err(`${p}.caption.segments[${gi}].start`, `segment overlaps the previous one (starts ${sg.start}s < ${prev.end}s)`);
    });
    for (const [k, t] of [["caption", s.caption], ["narration", s.narration]] as const) {
      if (t?.end !== undefined && t.end > s.duration + 1e-9) err(`${p}.${k}.end`, `${k} ends at ${t.end}s but scene is only ${s.duration}s`);
      if (t && t.start >= (t.end ?? s.duration)) err(`${p}.${k}.start`, `${k} start ${t.start}s is not before its end`);
    }
    s.sfx.forEach((x, k) => { if (x.at > s.duration) err(`${p}.sfx[${k}].at`, `sfx at ${x.at}s is after scene end`); });
    s.doodles.forEach((d, k) => {
      const dp = `${p}.doodles[${k}]`;
      if (!(DOODLE_KINDS as readonly string[]).includes(d.kind)) err(`${dp}.kind`, `unsupported doodle "${d.kind}". Use one of: ${list(DOODLE_KINDS)}`);
      if (d.at + d.duration > s.duration + 1e-9) err(`${dp}`, `doodle draw-on ends at ${(d.at + d.duration).toFixed(2)}s but scene is only ${s.duration}s`);
      if (d.kind === "path" && (!d.points || d.points.length < 2)) err(`${dp}.points`, "doodle kind \"path\" needs points[] with at least 2 design-px points");
      if (d.x < 0 || d.y < 0 || d.x + d.w > 1080) warn(dp, "doodle box runs outside the 1080-wide design frame");
      if (d.y + d.h > 1400) warn(dp, "doodle box enters the caption band (design y > 1400, L-038): keep marks above captions");
    });
  });

  const errors = issues.filter((i) => i.severity === "error");
  return errors.length ? { ok: false, issues } : { ok: true, plan, issues };
}

export function formatIssues(issues: PlanIssue[]): string {
  return issues.map((i) => `${i.severity === "error" ? "✖" : "⚠"} ${i.path}: ${i.message}`).join("\n");
}

export class PlanValidationError extends Error {
  constructor(public issues: PlanIssue[]) { super("Invalid video plan:\n" + formatIssues(issues)); }
}

export function assertValidPlan(input: unknown, registry?: ProfileRegistry): VideoPlan {
  const r = validatePlan(input, registry);
  if (!r.ok) throw new PlanValidationError(r.issues);
  return r.plan;
}
