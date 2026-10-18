import { z } from "zod";

/** Canonical vocabularies. Profiles declare which subset each character supports. */
export const EXPRESSIONS = ["neutral", "happy", "sad", "surprised", "confused", "focused", "despair"] as const;
export const ACTIONS = ["idle", "talking", "thinking", "typing", "walking", "reacting"] as const;
export const POSES = ["standing", "sitting"] as const;
export const TRANSITIONS = ["cut", "fade", "slide", "wipe", "iris"] as const;
export const FRAMINGS = ["wide", "medium", "closeup"] as const;
export const BACKGROUNDS = ["paper", "ink", "desk", "bed", "grid"] as const;
/** Doodle draw-on marks (anidoodle port, L-047). Shared by schema + validate (L-042: one list). */
export const DOODLE_KINDS = ["circle", "underline", "arrow", "check", "cross", "sketch-box", "path"] as const;
export const ENTERS = ["none", "pop", "slide-left", "slide-right", "rise"] as const;

export type Expression = (typeof EXPRESSIONS)[number];
export type Action = (typeof ACTIONS)[number];
export type Pose = (typeof POSES)[number];

const seconds = z.number({ invalid_type_error: "must be a number of seconds" }).finite().nonnegative();
const nonEmpty = z.string().trim().min(1);

export const VideoConfigSchema = z.object({
  width: z.number().int().min(16).max(4096).default(1080),
  height: z.number().int().min(16).max(4096).default(1920),
  fps: z.number().int().min(1).max(120).default(30),
  theme: z.enum(["light", "dark"]).default("light"),
});

export const TimedChange = <T extends z.ZodTypeAny>(value: T) => z.object({ at: seconds, value });

export const CharacterCueSchema = z.object({
  characterId: nonEmpty,
  x: z.number().min(0).max(1).default(0.5).describe("horizontal anchor, 0=left edge 1=right edge"),
  pose: z.string().default("standing"),
  action: z.string().default("idle"),
  expression: z.string().default("neutral"),
  facing: z.enum(["left", "right"]).default("right"),
  enter: z.enum(ENTERS).default("none"),
  exit: z.enum(["none", "fade", "slide-left", "slide-right"]).default("none"),
  expressionChanges: z.array(TimedChange(z.string())).default([]),
  actionChanges: z.array(TimedChange(z.string())).default([]),
  /** Optional walk target (0..1) used by action=walking. */
  toX: z.number().min(0).max(1).optional(),
});

export const DialogueSchema = z.object({
  speaker: nonEmpty,
  text: nonEmpty,
  start: seconds,
  end: seconds,
  style: z.enum(["speech", "thought", "shout"]).default("speech"),
  /** Voice emotion for the TTS step (rule-46). Defaults to the speaker's current expression. */
  emotion: z.string().optional(),
  /** Filled by `npm run voice` (F5-TTS / VieNeu-TTS, characters with a voice preset). src is relative to public/. */
  audio: z.object({ src: nonEmpty, duration: z.number().positive(), envelope: z.array(z.number().min(0).max(1)).default([]), engine: z.string().optional() }).optional(),
});

export const SceneSchema = z.object({
  id: nonEmpty,
  duration: z.number().finite().positive({ message: "duration must be > 0 seconds" }).max(120),
  background: z.object({
    kind: z.string().default("paper"),
    label: z.string().optional().describe("small narration box, e.g. 'MỖI TỐI · 11:48 PM'"),
  }).default({}),
  camera: z.object({
    framing: z.string().default("medium"),
    /** slow push-in amount, 0 = static. Deterministic zoom over the scene. */
    push: z.number().min(0).max(0.3).default(0.04),
  }).default({}),
  transition: z.object({
    type: z.string().default("cut"),
    duration: seconds.default(0.4),
  }).default({}),
  characters: z.array(CharacterCueSchema).default([]),
  dialogue: z.array(DialogueSchema).default([]),
  caption: z.object({ text: nonEmpty, start: seconds.default(0), end: seconds.optional(), highlight: z.array(z.number().int().nonnegative()).default([]),
    /** Optional per-line caption segments synced to voice lines (one segment visible at a time). Overrides text/start/end when present. */
    segments: z.array(z.object({ text: nonEmpty, start: seconds, end: seconds, highlight: z.array(z.number().int().nonnegative()).default([]) })).optional() }).optional(),
  narration: z.object({ text: nonEmpty, start: seconds.default(0), end: seconds.optional() }).optional(),
  sfx: z.array(z.object({ name: nonEmpty, at: seconds })).default([]),
  /** DL-056 comic props (laptop/phone/calendar/cloud/sign/words/vignette), see composition/Props.tsx */
  props: z.array(z.object({ kind: z.enum(["laptop", "phone", "calendar", "cloud", "sign", "vignette", "words"]) }).passthrough()).default([]),
  /** Doodle draw-on marks (anidoodle, Apache-2.0; src/composition/doodle/). Design px, 1080-wide. */
  doodles: z.array(z.object({
    kind: z.enum(DOODLE_KINDS), x: z.number().finite(), y: z.number().finite(),
    w: z.number().positive(), h: z.number().positive(),
    at: seconds.default(0), duration: z.number().finite().positive().default(0.6),
    color: z.string().optional(), seed: z.number().int().default(7),
    width: z.number().positive().default(10),
    points: z.array(z.tuple([z.number(), z.number()])).optional(),
  })).default([]),
  beat: z.string().optional().describe("repo beat id, e.g. clip-01.b02"),
});

export const VideoPlanSchema = z.object({
  version: z.literal(1).default(1),
  id: nonEmpty,
  title: z.string().optional(),
  meta: z.object({ clip: z.string().optional(), week: z.number().int().positive().optional(), source: z.string().optional() }).default({}),
  video: VideoConfigSchema.default({}),
  scenes: z.array(SceneSchema).min(1, "a plan needs at least one scene"),
});

export type VideoConfig = z.infer<typeof VideoConfigSchema>;
export type CharacterCue = z.infer<typeof CharacterCueSchema>;
export type Dialogue = z.infer<typeof DialogueSchema>;
export type Scene = z.infer<typeof SceneSchema>;
export type VideoPlan = z.infer<typeof VideoPlanSchema>;
export type VideoPlanInput = z.input<typeof VideoPlanSchema>;

/** Character profile: reusable across videos, independent of any scene. */
export const CharacterProfileSchema = z.object({
  id: nonEmpty,
  name: nonEmpty,
  rig: nonEmpty.describe("key of the React SVG rig in src/characters/rigs"),
  style: z.string(),
  colors: z.object({ ink: z.string(), paper: z.string(), accent: z.string().optional(), soft: z.string().optional() }),
  proportions: z.object({ heightUnits: z.number().positive(), headRatio: z.number().positive(), headRadius: z.number().positive() }),
  hair: z.string(),
  clothing: z.string(),
  face: z.string(),
  expressions: z.array(z.enum(EXPRESSIONS)).min(1),
  poses: z.array(z.enum(POSES)).min(1),
  actions: z.array(z.enum(ACTIONS)).min(1),
  defaults: z.object({ expression: z.enum(EXPRESSIONS), pose: z.enum(POSES), action: z.enum(ACTIONS), blinkEverySec: z.number().positive() }),
  availableFromWeek: z.number().int().positive().optional(),
  /** Synthetic voice. Only AI characters may have one (rule-46): never a real person, never cloned. */
  voice: z
    .object({
      engine: z.enum(["vieneu-tts", "f5-tts"]),
      preset: nonEmpty,
      synthetic: z.literal(true),
      /** f5-tts only (DL-035): synthetic reference clip (repo-relative) + its transcript. */
      ref: z.string().optional(),
      refText: z.string().optional(),
    })
    .passthrough()
    .refine((v) => v.engine !== "f5-tts" || (!!v.ref && !!v.refText), { message: "f5-tts voice needs ref + refText" })
    .optional(),
  assets: z.array(z.string()).default([]),
  notes: z.string().optional(),
});
export type CharacterProfile = z.infer<typeof CharacterProfileSchema>;
