import React from "react";
import type { CharacterProfile, Expression } from "../../validation/schema";
import type { CharacterState } from "../../animation/controller";

/**
 * Hiệp chibi rig (port of pipeline/characters-v2 hiep(), extended to the full state set).
 * Local units: feet at (0,0), +y down. ~640 units tall standing.
 */
export const ChibiHiep: React.FC<{ state: CharacterState; profile: CharacterProfile; uid: string }> = ({ state: s, profile, uid }) => {
  const INK = profile.colors.ink, PAPER = profile.colors.paper, SOFT = profile.colors.soft ?? "#E4E2DD";
  const sitting = s.pose === "sitting";
  const drop = sitting ? 96 : 0;               // upper body lowered when sitting
  const outline = { stroke: PAPER, strokeWidth: 7, paintOrder: "stroke" as const };

  // ---- arms (angle 0 = hanging down, + = swing outward) ----
  const shoulderL = { x: -78, y: -132 + drop }, shoulderR = { x: 78, y: -132 + drop };
  let aL = 22 + s.armSwing, aR = 22 + (s.action === "walking" ? -s.armSwing : s.armSwing);
  if (s.action === "typing") { aL = 82 + 6 * Math.sin(s.typingPhase * Math.PI * 2); aR = -70 + 6 * Math.sin(s.typingPhase * Math.PI * 2 + Math.PI); }
  if (s.action === "thinking") aR = -150;
  if (s.action === "reacting") { aL = 120 + s.armSwing * 0.4; aR = 120 + s.armSwing * 0.4; }
  const arm = (sh: { x: number; y: number }, ang: number, side: -1 | 1, key: string) => (
    <g key={key} transform={`rotate(${side * ang} ${sh.x} ${sh.y})`}>
      <rect x={sh.x - 21} y={sh.y - 6} width={42} height={96} rx={21} fill={INK} {...outline} />
      <circle cx={sh.x} cy={sh.y + 92} r={22} fill={INK} {...outline} />
    </g>
  );

  // ---- legs ----
  const legs = sitting ? (
    <g>
      <rect x={-64} y={-62} width={150} height={52} rx={26} fill={INK} {...outline} />
      <rect x={-10} y={-62} width={150} height={52} rx={26} fill={INK} {...outline} />
      <ellipse cx={142} cy={-12} rx={30} ry={20} fill={INK} {...outline} />
    </g>
  ) : (
    <g>
      {[-1, 1].map((side) => {
        const swing = s.action === "walking" ? side * 20 * Math.sin(s.walkPhase) : 0;
        return (
          <g key={side} transform={`rotate(${swing} ${side * 34} -40)`}>
            <rect x={side * 34 - 26} y={-48} width={52} height={44} rx={22} fill={INK} {...outline} />
            <ellipse cx={side * 34 + side * 6} cy={-6} rx={32} ry={17} fill={INK} {...outline} />
          </g>
        );
      })}
    </g>
  );

  const torso = (
    <g transform={`translate(0 ${drop})`}>
      <path d="M-92,-150 C-96,-60 -100,-10 -60,0 L60,0 C100,-10 96,-60 92,-150 C60,-176 -60,-176 -92,-150Z" fill={INK} />
      <path d="M-34,-160 Q0,-128 34,-160" fill="none" stroke={PAPER} strokeWidth={7} strokeLinecap="round" opacity={0.9} />
      <path d="M-14,-140 L-16,-104 M14,-140 L16,-104" stroke={PAPER} strokeWidth={5} strokeLinecap="round" opacity={0.75} />
      <path d="M-50,-58 Q0,-44 50,-58" fill="none" stroke={PAPER} strokeWidth={5} strokeLinecap="round" opacity={0.35} />
    </g>
  );

  const showCur = s.expressionBlend >= 0.5;
  const exprRaw: Expression = showCur ? s.expression : s.prevExpression;
  const despair = exprRaw === "despair"; const expr = (despair ? "sad" : exprRaw) as Expression;  // despair = sad + squeezed eyes, frown-open mouth, 2 tears
  const hy = -300 + drop;

  return (
    <g>
      <ellipse cx={sitting ? 30 : 0} cy={6} rx={sitting ? 170 : 120} ry={16} fill={INK} opacity={0.09} />
      {sitting && <rect x={-110} y={-104} width={220} height={104} rx={40} fill={SOFT} stroke={INK} strokeWidth={8} />}
      {legs}
      {s.action !== "typing" && arm(shoulderL, aL, -1, "l")}
      {s.action !== "typing" && s.action !== "thinking" && arm(shoulderR, aR, 1, "r")}
      {torso}
      <g transform={`translate(0 ${hy + 150}) rotate(${s.headTilt}) translate(0 -150)`}>
        <Head expr={expr} s={s} uid={uid} INK={INK} PAPER={PAPER} SOFT={SOFT} />
      </g>
      {s.action === "thinking" && (
        <g transform={`translate(0 ${hy + 150}) rotate(${s.headTilt}) translate(0 -150)`}>
          <ellipse cx={70} cy={150} rx={30} ry={26} fill={INK} stroke={PAPER} strokeWidth={7} />
          <path d="M52,140 Q70,128 88,140" fill="none" stroke={PAPER} strokeWidth={4} strokeLinecap="round" opacity={0.6} />
        </g>
      )}
      {s.action === "typing" && <Laptop s={s} INK={INK} PAPER={PAPER} drop={drop} />}
      {s.action === "typing" && arm(shoulderL, aL, -1, "lt")}
      {s.action === "typing" && arm(shoulderR, aR, 1, "rt")}
    </g>
  );
};

const Laptop: React.FC<{ s: CharacterState; INK: string; PAPER: string; drop: number }> = ({ INK, PAPER, drop }) => (
  <g transform={`translate(150 ${drop - 30})`}>
    <path d="M-80,-40 L-66,-150 Q-64,-160 -54,-160 L54,-160 Q64,-160 66,-150 L80,-40 Z" fill={INK} stroke={PAPER} strokeWidth={6} strokeLinejoin="round" />
    <circle cx={0} cy={-100} r={12} fill={PAPER} opacity={0.9} />
    <rect x={-110} y={-44} width={220} height={24} rx={12} fill={INK} stroke={PAPER} strokeWidth={6} />
  </g>
);

const Head: React.FC<{ expr: Expression; s: CharacterState; uid: string; INK: string; PAPER: string; SOFT: string }> = ({ expr, s, uid, INK, PAPER, SOFT }) => {
  const despair = (s.expression as string) === "despair";
  const R = 168;
  const blink = s.blink;
  const look = s.look * 10;
  const eyes: React.ReactNode[] = [];
  for (const side of [-1, 1]) {
    const x = side * 58 + look, y = 30;
    if (expr === "happy") {
      eyes.push(<path key={side} d={`M${x - 21},${y + 8} Q${x},${y - 20} ${x + 21},${y + 8}`} fill="none" stroke={INK} strokeWidth={12} strokeLinecap="round" />);
      continue;
    }
    if (despair) {  // squeezed shut eyes (> <)
      eyes.push(<path key={side} d={`M${x - 20 * side},${y - 14} L${x + 16 * side},${y} L${x - 20 * side},${y + 14}`} fill="none" stroke={INK} strokeWidth={11} strokeLinecap="round" strokeLinejoin="round" />);
      continue;
    }
    let big = 1, ry = 26, rx = 19;
    if (expr === "surprised") big = 1.32;
    if (expr === "confused") big = side < 0 ? 0.85 : 1.15;
    if (expr === "focused") ry = 17;
    if (expr === "sad") ry = 22;
    const eRy = Math.max(3, ry * big * (1 - blink)), eRx = rx * big;
    eyes.push(
      <g key={side}>
        <ellipse cx={x} cy={y} rx={eRx} ry={eRy} fill={INK} />
        {blink < 0.55 && <circle cx={x + 6} cy={y - 9 * big} r={6.5 * big} fill={PAPER} />}
        {blink < 0.55 && <circle cx={x - 7} cy={y + 9} r={3} fill={PAPER} opacity={0.8} />}
        {expr === "focused" && <path d={`M${x - 26},${y - 14} L${x + 26},${y - 14}`} stroke={PAPER} strokeWidth={10} />}
      </g>,
    );
  }
  let brows: React.ReactNode = null;
  if (expr === "focused") brows = <path d="M-86,-20 L-36,-6 M86,-20 L36,-6" stroke={INK} strokeWidth={11} strokeLinecap="round" />;
  if (expr === "surprised") brows = <path d="M-82,-38 Q-58,-56 -34,-38 M82,-38 Q58,-56 34,-38" fill="none" stroke={INK} strokeWidth={9} strokeLinecap="round" />;
  if (despair) brows = <path d="M-86,0 Q-64,-10 -36,-34 M86,0 Q64,-10 36,-34" fill="none" stroke={INK} strokeWidth={10} strokeLinecap="round" />;
  else if (expr === "sad") brows = <path d="M-84,-6 Q-62,-12 -38,-26 M84,-6 Q62,-12 38,-26" fill="none" stroke={INK} strokeWidth={9} strokeLinecap="round" />;
  if (expr === "confused") brows = <path d="M-84,-26 Q-60,-44 -36,-30 M36,-8 L84,-10" fill="none" stroke={INK} strokeWidth={9} strokeLinecap="round" />;

  const m = s.mouthOpen;
  let mouth: React.ReactNode;
  if (m > 0.06) {
    const w = expr === "happy" ? 30 : expr === "sad" ? 18 : 22;
    const h = 6 + 22 * m;
    mouth = expr === "sad" ? (  // sad/despair talking: frown-shaped opening (corners down) — never a D-smile (L-026)
      <path d={`M${-w - 4},${104 + h * 0.5} Q0,${92 - h * 0.5} ${w + 4},${104 + h * 0.5} Q0,${100 + h * 0.2} ${-w - 4},${104 + h * 0.5}Z`} fill={INK} />
    ) : (
      <g>
        <path d={`M${-w},96 Q${-w},${96 + h * 1.6} 0,${96 + h * 1.6} Q${w},${96 + h * 1.6} ${w},96 Q0,${expr === "sad" ? 104 : 90} ${-w},96Z`} fill={INK} />
        <ellipse cx={0} cy={96 + h * 1.2} rx={w * 0.5} ry={Math.max(2, h * 0.35)} fill="#E86A5A" opacity={0.9} />
      </g>
    );
  } else if (expr === "happy") mouth = <path d="M-28,92 Q0,130 28,92 Z" fill={INK} />;
  else if (expr === "surprised") mouth = <ellipse cx={0} cy={106} rx={15} ry={19} fill={INK} />;
  else if (expr === "sad") mouth = <path d="M-20,110 Q0,94 20,110" fill="none" stroke={INK} strokeWidth={8} strokeLinecap="round" />;
  else if (expr === "focused") mouth = <path d="M-16,102 L16,102" stroke={INK} strokeWidth={8} strokeLinecap="round" />;
  else if (expr === "confused") mouth = <path d="M-22,104 Q-11,96 0,104 T22,104" fill="none" stroke={INK} strokeWidth={8} strokeLinecap="round" />;
  else mouth = <path d="M-20,96 Q0,114 20,96" fill="none" stroke={INK} strokeWidth={8} strokeLinecap="round" />;

  return (
    <g>
      <clipPath id={`${uid}-hc`}><circle r={R} /></clipPath>
      <circle r={R} fill={PAPER} />
      <g clipPath={`url(#${uid}-hc)`}>
        <ellipse cx={0} cy={-118} rx={210} ry={118} fill={INK} />
        <circle cx={-112} cy={-30} r={52} fill={INK} /><circle cx={-40} cy={-40} r={46} fill={INK} />
        <circle cx={34} cy={-46} r={42} fill={INK} /><circle cx={118} cy={-24} r={56} fill={INK} />
        <ellipse cx={-96} cy={80} rx={30} ry={15} fill={expr === "sad" ? SOFT : "#F2B8A8"} opacity={expr === "sad" ? 1 : 0.85} />
        <ellipse cx={96} cy={80} rx={30} ry={15} fill={expr === "sad" ? SOFT : "#F2B8A8"} opacity={expr === "sad" ? 1 : 0.85} />
      </g>
      <circle r={R} fill="none" stroke={INK} strokeWidth={10} />
      <path d="M-40,-150 Q-20,-204 12,-180" fill="none" stroke={INK} strokeWidth={13} strokeLinecap="round" />
      <path d="M-150,-60 Q-120,-110 -80,-120" fill="none" stroke={PAPER} strokeWidth={7} strokeLinecap="round" opacity={0.35} />
      {brows}{eyes}{mouth}
      {despair && <path d="M-86,62 Q-94,80 -86,88 Q-78,80 -86,62Z" fill="#7FB3E8" stroke={INK} strokeWidth={4} />}
      {expr === "sad" && <path d="M86,62 Q78,80 86,88 Q94,80 86,62Z" fill="#7FB3E8" stroke={INK} strokeWidth={4} />}
      {expr === "surprised" && <g stroke={INK} strokeWidth={9} strokeLinecap="round"><path d="M-150,-190 L-170,-226" /><path d="M-110,-214 L-116,-252" /><path d="M150,-190 L170,-226" /></g>}
      {expr === "confused" && <text x={150} y={-150} fontSize={110} fontWeight={700} fill={INK} fontFamily="Be Vietnam Pro" transform={`rotate(14 150 -150)`}>?</text>}
      {s.action === "thinking" && <g fill={INK}><circle cx={170} cy={-170} r={10} /><circle cx={200} cy={-210} r={15} /><circle cx={240} cy={-260} r={20} /></g>}
    </g>
  );
};
