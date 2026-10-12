#!/usr/bin/env bash
# Join a Remotion story beat (with Omi voice audio) and a HyperFrames explainer beat (silent)
# with one ffmpeg xfade. No music (rule-21). Usage: join-beats.sh story.mp4 explainer.mp4 out.mp4 [xfade=slideleft] [dur=0.35]
set -euo pipefail
A="$1"; B="$2"; OUT="$3"; FX="${4:-slideleft}"; D="${5:-0.35}"
DA=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A")
DB=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$B")
OFF=$(python3 -c "print(round($DA-$D,3))"); TOT=$(python3 -c "print(round($DA+$DB-$D,3))")
HASA=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$A" | head -1)
if [ -n "$HASA" ]; then AUD="[0:a]aresample=48000,apad,atrim=0:$TOT,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]"; else AUD="anullsrc=r=48000:cl=mono,atrim=0:$TOT[a]"; fi
ffmpeg -loglevel error -y -i "$A" -i "$B" -filter_complex \
 "[0:v]fps=30,format=yuv420p,setsar=1[v0];[1:v]fps=30,format=yuv420p,setsar=1[v1];[v0][v1]xfade=transition=$FX:duration=$D:offset=$OFF,format=yuv420p[v];$AUD" \
 -map "[v]" -map "[a]" -c:v libx264 -profile:v high -crf 18 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -r 30 \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
echo "joined → $OUT (${TOT}s)"
