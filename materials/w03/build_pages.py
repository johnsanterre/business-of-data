"""Build the week 3 site pages from the scripts and the rendered frames.

python3 build_pages.py

Produces, under materials/w03/:
  scripts/NN_name.html      the narration as written, numbered paragraphs
  slides/NN/index.html      the deck as a gallery, plus the jpgs
Copies frames from give-voice/render/business-of-data/w03/NN/frames as jpg.

Idempotent. Matches the week 2 page shapes exactly so the two weeks read alike.
"""
import os, re, json, html, subprocess, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
RENDER = "/Users/john/Dropbox/_/Retrospective/give-voice/render/business-of-data/w03"
WEEK = 3
MODULE = "Liquidity, duration, concentration"
TERM = "Winter 2027"

SEGS = [
    ("01", "01_solvency_and_liquidity", "Solvency and liquidity"),
    ("02", "02_duration", "Duration"),
    ("03", "03_runway_burn_and_the_raise_cycle", "Runway, burn, and the raise cycle"),
    ("04", "04_concentration", "Concentration"),
    ("05", "05_the_mechanics_of_a_run", "The mechanics of a run"),
    ("06", "06_warning_indicators", "Warning indicators"),
]

GOAT = ('<script data-goatcounter="https://johnsanterre.goatcounter.com/count"\n'
        '        async src="//gc.zgo.at/count.js"></script>\n')


def crest(back_href, back_label, kicker, title, role, depth):
    up = "../" * depth
    return f"""<link rel="stylesheet" href="{up}course.css">

<header>
  <div class="wrap">
    <div class="crest">
      <a class="uc" href="{up}index.html">Berkeley</a>
      <span class="prog">The Business of Data</span>
      <span class="term">{TERM}</span>
    </div>
    <div class="mast-week">
      <a class="back" href="{back_href}">&larr; {back_label}</a>
      <p class="wknum">{kicker}</p>
      <h1>{title}</h1>
      <p class="role">{role}</p>
    </div>
  </div>
</header>
"""


def paragraphs(md_path):
    body = open(md_path).read().split("## Script")[1]
    return [(int(n), t.strip()) for n, t in
            re.findall(r"\[P(\d+)\]\s*(.*?)(?=\n\[P\d+\]|\Z)", body, re.S)]


def build_script_page(num, stem, title):
    md = os.path.join(HERE, "scripts", stem + ".md")
    paras = paragraphs(md)
    out = [f"<title>Script: {html.escape(title)}</title>\n"]
    out.append(crest(f"../../../week{WEEK}.html", f"Week {WEEK}", "Script", html.escape(title),
                     f"Segment {int(num)} of 6 &middot; {MODULE}", 3))
    out.append('\n<section>\n  <div class="wrap doc">\n')
    out.append(f'    <div class="prov">The narration as written, {len(paras)} paragraphs. '
               'This is the source the audio was generated from.</div>\n')
    for n, t in paras:
        out.append(f'    <p><span class="pn">{n}</span>{html.escape(t)}</p>\n')
    out.append("  </div>\n</section>\n")
    out.append(f"""
<footer>
  <div class="wrap">
    <b>The Business of Data</b> &middot; Week {WEEK} &middot;
    <a href="../../../week{WEEK}.html">Back to week {WEEK}</a> &middot;
    <a href="../{stem}.mp4">Video</a> &middot;
    <a href="../audio/{stem}.m4a">Audio</a> &middot;
    <a href="../slides/{num}/index.html">Slides</a>
  </div>
</footer>

""")
    out.append(GOAT)
    path = os.path.join(HERE, "scripts", stem + ".html")
    open(path, "w").write("".join(out))
    return len(paras)


def frame_files(num):
    """Ordered frame basenames for one deck, from its sections.json."""
    secs = json.load(open(os.path.join(RENDER, num, "sections.json")))
    names = []
    for s in secs:
        if s["frames"] == 1:
            names.append(s["id"])
        else:
            names += [f"{s['id']}_{k:02d}" for k in range(s["frames"])]
    return names


def build_slides_page(num, stem, title):
    names = frame_files(num)
    dest = os.path.join(HERE, "slides", num)
    os.makedirs(dest, exist_ok=True)
    for n in names:
        src = os.path.join(RENDER, num, "frames", n + ".png")
        dst = os.path.join(dest, n + ".jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                        src, "--out", dst], capture_output=True, check=True)
    out = [f"<title>Slides: {html.escape(title)}</title>\n"]
    out.append(crest(f"../../../../week{WEEK}.html", f"Week {WEEK}", "Slides", html.escape(title),
                     f"Segment {int(num)} of 6 &middot; {MODULE}", 4))
    out.append('\n<section>\n  <div class="wrap">\n')
    out.append(f'    <p class="intro">{len(names)} slides, in the order they appear in the lecture.</p>\n')
    out.append('    <div class="gallery">\n')
    for i, n in enumerate(names, 1):
        out.append(f'      <figure><img src="{n}.jpg" alt="slide {i}" loading="lazy">'
                   f'<figcaption>{i}</figcaption></figure>\n')
    out.append("    </div>\n  </div>\n</section>\n")
    out.append(f"""
<footer>
  <div class="wrap">
    <b>The Business of Data</b> &middot; Week {WEEK} &middot;
    <a href="../../../../week{WEEK}.html">Back to week {WEEK}</a> &middot;
    <a href="../../{stem}.mp4">Video</a> &middot;
    <a href="../../audio/{stem}.m4a">Audio</a> &middot;
    <a href="../../scripts/{stem}.html">Script</a>
  </div>
</footer>

""")
    out.append(GOAT)
    open(os.path.join(dest, "index.html"), "w").write("".join(out))
    return len(names)


if __name__ == "__main__":
    total_p = total_s = 0
    for num, stem, title in SEGS:
        p = build_script_page(num, stem, title)
        s = build_slides_page(num, stem, title)
        total_p += p
        total_s += s
        print(f"{num} {title:38s} {p:3d} paragraphs  {s:3d} slides")
    print(f"   {'total':38s} {total_p:3d} paragraphs  {total_s:3d} slides")
