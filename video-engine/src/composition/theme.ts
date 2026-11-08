export const BRAND = { ink: "#111111", paper: "#F7F7F5", soft: "#E4E2DD", muted: "#8A8A86", accent: "#FF5A36" } as const;
export const FRAMING = {
  wide: { scale: 1.1, groundY: 1390 },
  medium: { scale: 1.15, groundY: 1390 },
  closeup: { scale: 1.8, groundY: 1700 },
  reels: { scale: 0.9, groundY: 1390 }, // Reels/Shorts medium (×0.78, head ≈320px): fits between the narrow caption box (x≤648) and the frame edge (x 1046) with ≥16px each side at push ≤0.02
} as const;
export const DESIGN_W = 1080;
