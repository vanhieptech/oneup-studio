#!/usr/bin/env bash
# clip-05 v4: Reels/Shorts MP4 = cover.png 0.5s (15 frames, L-083) + plan-reels render (layout reels) muxed with the same final mix as TikTok.
# Audio: final/out/mix.wav when present, else the audio track of the delivered clip-05-v4-tiktok.mp4 (= that mix; out/ is gitignored and can vanish on resync).
# Then the L-033 per-frame scan (RR round 2): a caption-less twin render gives the exact caption mask → clearance to every object + right frame edge.
# Run after clip-05-reels-plan-v4.py.  Usage: bash pipeline/scripts/clip-05-reels-assemble-v4.sh
set -euo pipefail
R=$(cd "$(dirname "$0")/../.." && pwd); F=$R/content/clips/clip-05-hoc-mot-dem/final; VE=$R/video-engine
TOTAL=$(python3 -c "import json;print(json.load(open('$F/timing.json'))['total'])")
MIX=$F/out/mix.wav
if [ ! -f "$MIX" ]; then mkdir -p "$F/out"; ffmpeg -loglevel error -y -i "$F/clip-05-v4-tiktok.mp4" -vn -ac 1 -ar 48000 -c:a pcm_s24le "$F/out/mix-from-tiktok.wav"; MIX=$F/out/mix-from-tiktok.wav; fi
python3 - "$F/out/plan-reels.json" "$F/out/plan-reels-nocap.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1])); p["id"] += "-nocap"
for s in p["scenes"]: s.pop("caption", None)
json.dump(p, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
PY
(cd "$VE" && npx tsx src/cli.ts validate "$F/out/plan-reels.json" && npx tsx src/cli.ts render "$F/out/plan-reels.json" "$F/out/plan-reels-nocap.json" --out-dir out)
ffmpeg -loglevel error -y -loop 1 -framerate 30 -t 0.5 -i "$F/cover.png" -i "$VE/out/clip-05-final-reels.mp4" -i "$MIX" \
  -f lavfi -t 0.5 -i anullsrc=r=48000:cl=mono -filter_complex \
  "[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1,trim=end_frame=15,setpts=PTS-STARTPTS[c];\
[1:v]trim=0:$TOTAL,setpts=PTS-STARTPTS,fps=30,scale=out_range=tv,format=yuv420p,setsar=1,noise=alls=4:allf=t,format=yuv420p[b];\
[2:a]aresample=48000,atrim=0:$TOTAL,asetpts=PTS-STARTPTS[m];[c][3:a][b][m]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -profile:v high -crf 20 -maxrate 14M -bufsize 28M -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -r 30 -c:a aac -b:a 192k -ar 48000 -ac 1 -movflags +faststart \
  "$F/clip-05-v4-reels.mp4"
echo "reels → $F/clip-05-v4-reels.mp4"
python3 "$R/pipeline/scripts/scan-reels-clearance.py" "$VE/out/clip-05-final-reels.mp4" "$VE/out/clip-05-final-reels-nocap.mp4" "$F/out/plan-reels.json" --final "$F/clip-05-v4-reels.mp4" | tee "$F/out/reels-clearance.txt"
