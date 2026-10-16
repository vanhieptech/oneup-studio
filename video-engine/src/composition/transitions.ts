import type React from "react";
import { easeInOutCubic } from "../animation/timing";
import { tdevStyle, TDEV_NAMES, type TdevName } from "./transitions/tdev";
import { mmxStyle, MMX_EASE_NAMES, type MmxEaseName, type MmxPresetName } from "./motionmaxxing/mmx";

export const MMX_PRESET_NAMES: MmxPresetName[] = ["mmx-oversize-land", "mmx-cut-on-motion", "mmx-no-dead-frame"];

/** Style for the INCOMING scene during its first transitionFrames. p: 0→1. Deterministic, CSS-only. */
export function transitionStyle(type: string, p: number, w: number, h: number): React.CSSProperties {
  const e = easeInOutCubic(Math.max(0, Math.min(1, p)));
  switch (type) {
    case "fade": return { opacity: e };
    case "slide": return { transform: `translateX(${(1 - e) * w}px)`, boxShadow: "-20px 0 0 #111111" };
    case "wipe": return { clipPath: `inset(0 ${(1 - e) * 100}% 0 0 round 0 60px 60px 0)` };
    case "iris": return { clipPath: `circle(${e * Math.hypot(w, h) * 0.6}px at 50% 45%)` };
    default:
      if (type.startsWith("tdev-")) return tdevStyle(type as TdevName, p);
      if (type.startsWith("mmx-")) return mmxStyle(type as MmxEaseName | MmxPresetName, p); // motionmaxxing measured eases
      return {};
  }
}
export const TRANSITION_TYPES = ["cut", "fade", "slide", "wipe", "iris", ...TDEV_NAMES, ...MMX_EASE_NAMES, ...MMX_PRESET_NAMES] as const;
