import React from "react";
import { BRAND } from "./theme";

/** Rounded, ink-on-paper comic sets. Drawn in 1080-wide design space; h = design height. */
export const Background: React.FC<{ kind: string; h: number; t: number; theme: "light" | "dark"; floorY: number }> = ({ kind, h, t, floorY }) => {
  const { ink, paper, soft } = BRAND;
  const dots = (
    <pattern id="halftone" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="11" cy="11" r="2.4" fill={ink} opacity="0.09" />
    </pattern>
  );
  const halftoneCorner = <path d={`M0,0 L560,0 Q300,120 0,520 Z`} fill="url(#halftone)" />;
  const floor = (
    <g>
      <rect x={0} y={floorY} width={1080} height={h - floorY} fill={soft} />
      <path d={`M0,${floorY} L1080,${floorY}`} stroke={ink} strokeWidth={8} />
    </g>
  );
  switch (kind) {
    case "ink":
      return (
        <g>
          <rect width={1080} height={h} fill={ink} />
          <circle cx={540} cy={floorY - 330} r={430} fill={paper} />
          <ellipse cx={540} cy={floorY + 10} rx={330} ry={34} fill={paper} opacity={0.12} />
        </g>
      );
    case "grid":
      return (
        <g>
          <defs>{dots}<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><circle cx="30" cy="30" r="3.2" fill={ink} opacity="0.16" /></pattern></defs>
          <rect width={1080} height={h} fill={paper} />
          <rect width={1080} height={h} fill="url(#grid)" />
        </g>
      );
    case "desk": {
      const sway = 4 * Math.sin(t * 1.2);
      return (
        <g>
          <defs>{dots}</defs>
          <rect width={1080} height={h} fill={paper} />{halftoneCorner}
          {/* window */}
          <rect x={620} y={360} width={330} height={400} rx={40} fill={soft} stroke={ink} strokeWidth={10} />
          <path d="M785,360 L785,760 M620,560 L950,560" stroke={ink} strokeWidth={8} />
          <circle cx={700} cy={450} r={30} fill={paper} stroke={ink} strokeWidth={6} />
          {/* shelf + books */}
          <rect x={110} y={520} width={320} height={22} rx={11} fill={ink} />
          {[0, 1, 2, 3].map((i) => <rect key={i} x={140 + i * 52} y={410 - (i % 2) * 18} width={40} height={110 + (i % 2) * 18} rx={12} fill={i === 2 ? soft : ink} stroke={ink} strokeWidth={6} />)}
          {/* plant */}
          <g transform={`translate(360 ${floorY}) rotate(${sway})`}>
            <ellipse cx={0} cy={-230} rx={40} ry={78} fill={ink} transform="rotate(-24 0 -230)" />
            <ellipse cx={34} cy={-210} rx={34} ry={66} fill={ink} transform="rotate(30 34 -210)" />
          </g>
          <rect x={300} y={floorY - 150} width={120} height={150} rx={30} fill={soft} stroke={ink} strokeWidth={9} />
          {floor}
          {/* desk */}
          <rect x={500} y={floorY - 330} width={520} height={34} rx={17} fill={ink} />
          <rect x={540} y={floorY - 300} width={30} height={300} rx={15} fill={ink} />
          <rect x={950} y={floorY - 300} width={30} height={300} rx={15} fill={ink} />
          <rect x={860} y={floorY - 430} width={40} height={100} rx={20} fill={ink} />
          <path d={`M820,${floorY - 470} Q880,${floorY - 520} 940,${floorY - 470} Z`} fill={ink} />
        </g>
      );
    }
    case "plate": return null; // pre-rendered HyperFrames motion-graphic plate (SceneRenderer <OffthreadVideo>)
    case "room": {
      // clip-04 v18: desk room without the fixed window (window/time marker = "window" prop, y 250–550, clear of bubbles/title).
      return (
        <g>
          <defs>{dots}</defs>
          <rect width={1080} height={h} fill={paper} />{halftoneCorner}
          <rect x={110} y={600} width={300} height={22} rx={11} fill={ink} />
          {[0, 1, 2, 3].map((i) => <rect key={i} x={140 + i * 52} y={490 - (i % 2) * 18} width={40} height={110 + (i % 2) * 18} rx={12} fill={i === 2 ? soft : ink} stroke={ink} strokeWidth={6} />)}
          {floor}
        </g>
      );
    }
    case "bed": {
      const twinkle = 0.6 + 0.4 * Math.sin(t * 3);
      return (
        <g>
          <rect width={1080} height={h} fill="#E9E7E1" />
          <rect x={120} y={330} width={380} height={440} rx={190} fill={ink} />
          <circle cx={360} cy={480} r={70} fill={paper} />
          <circle cx={392} cy={458} r={62} fill={ink} />
          <circle cx={200} cy={420} r={7} fill={paper} opacity={twinkle} />
          <circle cx={250} cy={620} r={5} fill={paper} opacity={1 - twinkle * 0.5} />
          <circle cx={430} cy={660} r={6} fill={paper} opacity={twinkle} />
          <text x={700} y={560} fontFamily="Be Vietnam Pro" fontWeight={700} fontSize={96} fill={ink} opacity={0.85}>z</text>
          <text x={770} y={470} fontFamily="Be Vietnam Pro" fontWeight={700} fontSize={70} fill={ink} opacity={0.6}>z</text>
          <rect x={0} y={floorY} width={1080} height={h - floorY} fill={soft} />
          <path d={`M0,${floorY} L1080,${floorY}`} stroke={ink} strokeWidth={8} />
          {/* bed */}
          <rect x={20} y={floorY - 330} width={60} height={330} rx={30} fill={ink} />
          <rect x={40} y={floorY - 150} width={1040} height={130} rx={50} fill={paper} stroke={ink} strokeWidth={10} />
          <rect x={90} y={floorY - 210} width={230} height={90} rx={45} fill={paper} stroke={ink} strokeWidth={10} />
          <path d={`M520,${floorY - 150} Q760,${floorY - 210} 1080,${floorY - 160} L1080,${floorY - 20} L520,${floorY - 20} Z`} fill={soft} stroke={ink} strokeWidth={10} strokeLinejoin="round" />
        </g>
      );
    }
    default:
      return (
        <g>
          <defs>{dots}</defs>
          <rect width={1080} height={h} fill={paper} />{halftoneCorner}
          {floor}
        </g>
      );
  }
};
