#!/usr/bin/env python3
"""Generate SRT subtitle file from timing.json.

Usage:
    generate_srt.py <timing.json> [--output <path>]

The SRT contains English captions synced to the Vietnamese TTS timing.
English captions are used because they're what's displayed on screen
and provide the most utility when uploading to platforms like TikTok/YouTube
that can use sidecar subtitle files for accessibility and discovery.

Derives timing from the same caption segments the renderer uses (timing.json),
ensuring no drift from the rendered video.
"""
import json
import sys
import os
from pathlib import Path


def format_srt_time(seconds):
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    if seconds < 0:
        seconds = 0
    
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def escape_srt_text(text):
    """Escape text for SRT format.
    
    SRT allows basic text and some HTML tags, but we keep it simple.
    No special escaping needed for commas in timestamps (they're in the time field).
    """
    if not text:
        return ""
    # Replace problematic characters that might break parsers
    text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
    # Collapse multiple spaces
    text = ' '.join(text.split())
    return text


def generate_srt_from_timing(timing_data):
    """Generate SRT content from timing.json data.
    
    Args:
        timing_data: Parsed timing.json dict
        
    Returns:
        str: Complete SRT file content
        
    Raises:
        ValueError: If timing data is invalid or has overlaps
    """
    lines = timing_data.get("lines", [])
    
    if not lines:
        raise ValueError("No lines found in timing data")
    
    srt_entries = []
    
    for idx, line in enumerate(lines, start=1):
        # Use English caption (what's displayed on screen)
        caption = line.get("en", "")
        if not caption:
            # Skip lines without captions (shouldn't happen, but be defensive)
            continue
            
        start_time = line.get("t", 0)
        duration = line.get("dur", 0)
        end_time = start_time + duration
        
        # Validate timing
        if duration <= 0:
            raise ValueError(f"Line {idx} has non-positive duration: {duration}")
        if start_time < 0:
            raise ValueError(f"Line {idx} has negative start time: {start_time}")
            
        srt_entries.append({
            "index": len(srt_entries) + 1,  # SRT uses 1-based indexing
            "start": start_time,
            "end": end_time,
            "text": escape_srt_text(caption)
        })
    
    # Verify monotonic timing (each entry starts after or at the previous end)
    for i in range(1, len(srt_entries)):
        prev = srt_entries[i - 1]
        curr = srt_entries[i]
        if curr["start"] < prev["start"]:
            raise ValueError(
                f"Non-monotonic timing: entry {curr['index']} starts at "
                f"{curr['start']:.3f}s before entry {prev['index']} at {prev['start']:.3f}s"
            )
    
    # Build SRT content
    srt_lines = []
    for entry in srt_entries:
        srt_lines.append(str(entry["index"]))
        srt_lines.append(
            f"{format_srt_time(entry['start'])} --> {format_srt_time(entry['end'])}"
        )
        srt_lines.append(entry["text"])
        srt_lines.append("")  # Blank line between entries
    
    return "\n".join(srt_lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    timing_path = sys.argv[1]
    
    # Default output: same directory as timing.json, named after the clip
    output_path = None
    if "--output" in sys.argv:
        output_idx = sys.argv.index("--output")
        if output_idx + 1 < len(sys.argv):
            output_path = sys.argv[output_idx + 1]
    
    if not output_path:
        # Infer output path: timing.json is in final/, output SRT to final/out/
        timing_dir = Path(timing_path).parent
        out_dir = timing_dir / "out"
        
        # Extract clip name from path (e.g., clip-01-implementation-intention)
        # Path structure: content/{clips,archive}/clip-NN-slug/final/timing.json
        clip_dir = timing_dir.parent
        clip_name = clip_dir.name
        
        output_path = out_dir / f"{clip_name}.srt"
    
    output_path = Path(output_path)
    
    # Load timing data
    try:
        with open(timing_path, 'r', encoding='utf-8') as f:
            timing_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Timing file not found: {timing_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {timing_path}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Generate SRT
    try:
        srt_content = generate_srt_from_timing(timing_data)
    except ValueError as e:
        print(f"Error generating SRT: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write SRT file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    
    print(f"Generated SRT: {output_path}")
    print(f"  {len(timing_data.get('lines', []))} subtitle entries")
    print(f"  Duration: {timing_data.get('total', 0):.1f}s")


if __name__ == "__main__":
    main()
