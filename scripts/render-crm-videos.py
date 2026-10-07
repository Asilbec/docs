"""Render short help clips from the saved Recordly capture (no live app access).

Requires ffmpeg and Pillow. Run with --recording pointing at the original
recording-1791359950444.mp4. Timings below refer to that October 7 capture.
"""

import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


CLIPS = {
    "today": [
        (1, 12, "Choose Replied to find drivers waiting for your response."),
        (25, 33, "Open a lead to read its details and recent activity."),
    ],
    "callback": [
        (50, 56, "Open the lead's Next follow-up menu."),
        (62, 75, "Choose Pick date, then select the day you promised."),
        (85, 91.4, "Click Set. Check that Next follow-up shows your promise."),
    ],
    "manager": [
        (98, 105, "Owners and Admins: open Team, then choose View as."),
        (112, 123, "Review the recruiter's leads and details in read-only mode."),
    ],
}


def run(*args):
    subprocess.run([str(x) for x in args], check=True)


def stamp(seconds):
    ms = round(seconds * 1000)
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02}.{ms % 1000:03}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recording", type=Path, required=True)
    parser.add_argument("--background", type=Path, required=True)
    parser.add_argument("--font", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "videos/crm")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype(str(args.font), 28)
    small = ImageFont.truetype(str(args.font), 21)

    with tempfile.TemporaryDirectory(prefix="vocal-crm-video-") as temp:
        for name, segments in CLIPS.items():
            # A bottom caption sits outside the product recording. The recording
            # crop removes Safari chrome and Recordly's floating capture HUD.
            filters = []
            inputs = ["-i", str(args.recording), "-loop", "1", "-i", str(args.background)]
            total = 0
            cues = ["WEBVTT", ""]
            for i, (start, end, caption) in enumerate(segments):
                card = Image.new("RGBA", (1824, 58), (255, 255, 255, 0))
                draw = ImageDraw.Draw(card)
                draw.rounded_rectangle((0, 0, 1823, 57), radius=12, fill=(255, 255, 255, 248))
                draw.text((22, 12), caption, font=font, fill="#080808")
                draw.text((1655, 17), "Example data", font=small, fill="#5B5B5C")
                path = Path(temp) / f"{name}-{i}.png"
                card.save(path)
                inputs += ["-loop", "1", "-i", str(path)]
                cues += [f"{stamp(total)} --> {stamp(total + end - start)}", caption, ""]
                total += end - start
            labels = "".join(f"[s{i}]" for i in range(len(segments)))
            filters.append(f"[0:v]split={len(segments)}{labels}")
            for i, (start, end, _) in enumerate(segments):
                filters.append(f"[s{i}]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}]")
            joined = "".join(f"[v{i}]" for i in range(len(segments)))
            filters.append(f"{joined}concat=n={len(segments)}:v=1:a=0,crop=2648:1576:0:116,scale=1824:1086,setsar=1[video]")
            filters.append("[1:v]scale=1920:1200:force_original_aspect_ratio=increase,crop=1920:1200,setsar=1[background]")
            filters.append("[background][video]overlay=48:30:shortest=1[framed]")
            elapsed = 0
            previous = "framed"
            for i, (start, end, _) in enumerate(segments):
                duration = end - start
                current = f"caption{i}"
                filters.append(f"[{previous}][{i + 2}:v]overlay=48:1128:enable='gte(t,{elapsed})*lt(t,{elapsed + duration})'[{current}]")
                previous = current
                elapsed += duration
            target = args.output / f"{name}.mp4"
            run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs,
                "-filter_complex", ";".join(filters), "-map", f"[{previous}]", "-an",
                "-t", str(total), "-r", "30", "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "22", "-pix_fmt", "yuv420p", "-movflags", "+faststart", target)
            run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", "1",
                "-i", target, "-frames:v", "1", "-q:v", "3", args.output / f"{name}.jpg")
            (args.output / f"{name}.vtt").write_text("\n".join(cues))
            print(f"{name}: {total:.1f}s, {target.stat().st_size / 1024 / 1024:.2f} MiB", flush=True)


if __name__ == "__main__":
    main()
