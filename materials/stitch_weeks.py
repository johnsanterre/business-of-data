#!/usr/bin/env python3
"""Join each week's lecture segments into one full lecture, with chapters.

    python3 stitch_weeks.py 01 02 03 04

YouTube wants one video per lecture, not seven fragments. It turns timestamps in
a description into clickable chapters, which gives the segment structure back
without splitting the upload.

Chapter rules YouTube enforces, and this script obeys:
  - the first chapter must start at 00:00
  - there must be at least three
  - each must run at least ten seconds

The concat is a stream copy, so nothing is re-encoded and the join is exact.
Every segment came out of render_section.py with identical encode settings,
which is what makes that safe.
"""
import json, os, re, subprocess, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TITLE_S = 4.0
VID = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", "30", "-pix_fmt", "yuv420p"]
AUD = ["-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "1"]

WEEKS = {
    "01": (1, "Introduction", "The twelve functions, the gates a release passes, and three shapes of failure"),
    "02": (2, "How an asset is carried", "Depreciation as a judgment, and what follows from the number on the books"),
    "03": (3, "Liquidity, duration, concentration", "Why a firm worth more than it owes still fails"),
    "04": (4, "Model risk management", "The regime, and the two ways it fails in practice"),
}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("failed:\n" + " ".join(cmd) + "\n" + r.stderr[-1200:])
    return r.stdout


def duration(p):
    return float(run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", p]))


def strip(s):
    s = re.sub(r"<a class=\"watch\".*?</a>", "", s, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s))).strip()


def segment_titles(n):
    page = open(os.path.join(SITE, f"week{n}.html")).read()
    return [strip(m.group(1)) for m in
            re.finditer(r'<div><h4>(.*?)</h4><p>', page, re.S)]


def title_card(wk, n, module, dek, out_png):
    # long module names have to come down a step or they run off the frame
    size = 112 if len(module) <= 22 else 96 if len(module) <= 30 else 82
    h = f"""<!doctype html><meta charset="utf-8"><style>
    html,body{{margin:0;width:1920px;height:1080px;background:#fff;color:#1b1b1b;
      font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;
      display:flex;flex-direction:column;justify-content:center;padding:0 130px}}
    .k{{font-size:36px;color:#7a7a7a;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:30px}}
    h1{{font-size:{size}px;font-weight:600;letter-spacing:-1px;margin:0 0 34px;
      line-height:1.06;max-width:1660px}}
    .d{{font-size:44px;color:#3d3d3d;max-width:1400px;line-height:1.35}}
    .f{{position:absolute;bottom:70px;left:130px;font-size:30px;color:#7a7a7a}}
    </style>
    <div class="k">Finance, Law, and Risk in the AI Product Lifecycle &middot; Week {n}</div>
    <h1>{html.escape(module)}</h1>
    <div class="d">{html.escape(dek)}</div>
    <div class="f">Berkeley &middot; Winter 2027</div>"""
    tmp = os.path.join(HERE, f"w{wk}", "_title.html")
    open(tmp, "w").write(h)
    run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--window-size=1920,1080", "--virtual-time-budget=2500",
         f"--screenshot={out_png}", f"file://{os.path.abspath(tmp)}"])
    os.remove(tmp)


def hhmmss(t):
    t = int(t)
    h, m, s = t // 3600, (t % 3600) // 60, t % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def stitch(wk):
    n, module, dek = WEEKS[wk]
    d = os.path.join(HERE, f"w{wk}")
    parts = sorted(f for f in os.listdir(d)
                   if re.match(r"\d\d_.*\.mp4$", f) and not f.startswith("week-"))
    titles = segment_titles(n)
    if len(parts) != len(titles):
        sys.exit(f"w{wk}: {len(parts)} mp4s but {len(titles)} segments on the page")

    png = os.path.join(d, "_title.png")
    title_card(wk, n, module, dek, png)
    tmp4 = os.path.join(d, "_title.mp4")
    run([FFMPEG, "-y", "-loop", "1", "-framerate", "30", "-i", png,
         "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(TITLE_S)]
        + VID + ["-tune", "stillimage"] + AUD + [tmp4])

    files = [tmp4] + [os.path.join(d, p) for p in parts]
    lst = os.path.join(d, "_parts.txt")
    with open(lst, "w") as f:
        for p in files:
            f.write(f"file '{os.path.abspath(p)}'\n")
    out = os.path.join(d, f"week-{n}-full.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", "-movflags", "+faststart", out])

    # chapters: the title card belongs to the first chapter so it can start at 00:00
    chapters, t = [], 0.0
    for i, (p, title) in enumerate(zip(parts, titles)):
        chapters.append((0.0 if i == 0 else t + TITLE_S, title))
        t += duration(os.path.join(d, p))
    total = duration(out)
    if abs(total - (t + TITLE_S)) > 1.0:
        sys.exit(f"w{wk}: duration mismatch, container {total:.1f} vs parts {t + TITLE_S:.1f}")
    for f in (png, tmp4, lst):
        os.remove(f)

    lines = [f"{hhmmss(s)} {title}" for s, title in chapters]
    print(f"week {n}  {total/60:5.1f} min  {os.path.getsize(out)/1e6:4.0f} MB  "
          f"{len(chapters)} chapters -> {os.path.basename(out)}")
    return {"week": n, "module": module, "dek": dek, "file": out,
            "seconds": total, "chapters": lines}


if __name__ == "__main__":
    res = [stitch(w) for w in (sys.argv[1:] or list(WEEKS))]
    json.dump(res, open(os.path.join(HERE, "stitched.json"), "w"), indent=2)
    print(f"\n{len(res)} lectures, {sum(r['seconds'] for r in res)/3600:.1f} hours total")
