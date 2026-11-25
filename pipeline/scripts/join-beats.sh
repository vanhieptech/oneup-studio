#!/usr/bin/env bash
# Join two beat MP4s (e.g. story + explainer) with one ffmpeg xfade (standalone helper; canonical full-clip builder is pipeline/scripts/build-final.py).
# No music (rule-21). DL-072 defaults: linear -14 LUFS + alimiter=0.78, CRF 16, bt709.
# Usage: [FPS=30] [CRF=16] join-beats.sh story.mp4 explainer.mp4 out.mp4 [xfade=slideleft] [dur=0.35]
set -euo pipefail
A="$1"; B="$2"; OUT="$3"; FX="${4:-slideleft}"; D="${5:-0.35}"
FPS="${FPS:-30}"; CRF="${CRF:-16}"
FFMPEG="${FFMPEG_BIN:-$( [ -x /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg ] && echo /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg || echo ffmpeg )}"
FFPROBE="${FFPROBE_BIN:-$( [ -x /opt/homebrew/opt/ffmpeg-full/bin/ffprobe ] && echo /opt/homebrew/opt/ffmpeg-full/bin/ffprobe || echo ffprobe )}"
DA=$("$FFPROBE" -v error -show_entries format=duration -of csv=p=0 "$A")
DB=$("$FFPROBE" -v error -show_entries format=duration -of csv=p=0 "$B")
OFF=$(python3 -c "print(round($DA-$D,3))"); TOT=$(python3 -c "print(round($DA+$DB-$D,3))")
HASA=$("$FFPROBE" -v error -select_streams a -show_entries stream=index -of csv=p=0 "$A" | head -1)
if [ -n "$HASA" ]; then
  GAIN=$(python3 -c "import re,subprocess; s=subprocess.run(['$FFMPEG','-hide_banner','-i','$A','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr; m=re.findall(r'I:\s+(-?[\d.]+)\s+LUFS',s); print(f'{-14.0-float(m[-1]):.2f}' if m else '0.00')")
  AUD="[0:a]aresample=48000,apad,atrim=0:$TOT,volume=${GAIN}dB,alimiter=limit=0.78:attack=1:release=30:level=disabled,aresample=48000[a]"
else
  AUD="anullsrc=r=48000:cl=mono,atrim=0:$TOT[a]"
fi
"$FFMPEG" -loglevel error -y -i "$A" -i "$B" -filter_complex \
 "[0:v]fps=$FPS,scale=in_color_matrix=bt709:out_color_matrix=bt709,format=yuv420p,setsar=1[v0];[1:v]fps=$FPS,scale=in_color_matrix=bt709:out_color_matrix=bt709,format=yuv420p,setsar=1[v1];[v0][v1]xfade=transition=$FX:duration=$D:offset=$OFF,format=yuv420p[v];$AUD" \
 -map "[v]" -map "[a]" -c:v libx264 -profile:v high -crf "$CRF" -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -r "$FPS" \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
echo "joined → $OUT (${TOT}s, ${FPS}fps, crf=${CRF})"
