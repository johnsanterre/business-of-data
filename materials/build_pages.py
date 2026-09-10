"""Build the script pages and slide galleries for a week.

    python3 build_pages.py 01
    python3 build_pages.py 01 03 04

Reads the scripts in wNN/scripts and the frames in the give-voice render tree,
writes wNN/scripts/*.html and wNN/slides/NN/index.html plus the jpgs.

Path depth is computed rather than hard-coded: course.css lives only at the repo
root, and hard-coding "../../" is what left twelve week 2 pages unstyled.
"""
import os, re, sys, json, html, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
RENDER = "/Users/john/Dropbox/_/Retrospective/give-voice/render/business-of-data"
TERM = "Winter 2027"

WEEKS = {
    "01": ("Introduction", 7),
    "03": ("Liquidity, duration, concentration", 6),
    "04": ("Model risk management", 6),
}

GOAT = ('<script data-goatcounter="https://johnsanterre.goatcounter.com/count"\n'
        '        async src="//gc.zgo.at/count.js"></script>\n')


def up_to_root(from_dir):
    """How many ../ from this directory to the repo root."""
    return "../" * len(os.path.relpath(SITE, from_dir).split(os.sep))


def crest(from_dir, week, kicker, title, role):
    up = up_to_root(from_dir)
    return f"""<link rel="stylesheet" href="{up}course.css">

<header>
  <div class="wrap">
    <div class="crest">
      <a class="uc" href="{up}index.html">Berkeley</a>
      <span class="prog">Finance, Law, and Risk in the AI Product Lifecycle</span>
      <span class="term">{TERM}</span>
    </div>
    <div class="mast-week">
      <a class="back" href="{up}week{week}.html">&larr; Week {week}</a>
      <p class="wknum">{kicker}</p>
      <h1>{title}</h1>
      <p class="role">{role}</p>
    </div>
  </div>
</header>
"""


def segments(wk):
    d = os.path.join(HERE, f"w{wk}", "scripts")
    out = []
    for f in sorted(os.listdir(d)):
        m = re.match(r"(\d\d)_(.+)\.md$", f)
        if m:
            t = open(os.path.join(d, f)).read()
            title = re.search(r"^title: (.+)$", t, re.M).group(1).strip()
            out.append((m.group(1), f[:-3], title))
    return out


def paragraphs(path):
    body = open(path).read().split("## Script")[1]
    return [(int(n), t.strip()) for n, t in
            re.findall(r"\[P(\d+)\]\s*(.*?)(?=\n\[P\d+\]|\Z)", body, re.S)]


def build_script_page(wk, module, total, num, stem, title):
    d = os.path.join(HERE, f"w{wk}", "scripts")
    paras = paragraphs(os.path.join(d, stem + ".md"))
    week = str(int(wk))
    o = [f"<title>Script: {html.escape(title)}</title>\n",
         crest(d, week, "Script", html.escape(title),
               f"Segment {int(num)} of {total} &middot; {module}"),
         '\n<section>\n  <div class="wrap doc">\n',
         f'    <div class="prov">The narration as written, {len(paras)} paragraphs. '
         'This is the source the audio was generated from.</div>\n']
    for n, t in paras:
        o.append(f'    <p><span class="pn">{n}</span>{html.escape(t)}</p>\n')
    up = up_to_root(d)
    o += ["  </div>\n</section>\n", f"""
<footer>
  <div class="wrap">
    <b>Finance, Law, and Risk in the AI Product Lifecycle</b> &middot; Week {week} &middot;
    <a href="{up}week{week}.html">Back to week {week}</a> &middot;
    <a href="../{stem}.mp4">Video</a> &middot;
    <a href="../audio/{stem}.m4a">Audio</a> &middot;
    <a href="../slides/{num}/index.html">Slides</a>
  </div>
</footer>

""", GOAT]
    open(os.path.join(d, stem + ".html"), "w").write("".join(o))
    return len(paras)


def build_slides_page(wk, module, total, num, stem, title):
    secs = json.load(open(os.path.join(RENDER, f"w{wk}", num, "sections.json")))
    names = []
    for s in secs:
        names += ([s["id"]] if s["frames"] == 1
                  else [f"{s['id']}_{k:02d}" for k in range(s["frames"])])
    dest = os.path.join(HERE, f"w{wk}", "slides", num)
    os.makedirs(dest, exist_ok=True)
    for n in names:
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                        os.path.join(RENDER, f"w{wk}", num, "frames", n + ".png"),
                        "--out", os.path.join(dest, n + ".jpg")],
                       capture_output=True, check=True)
    week = str(int(wk))
    up = up_to_root(dest)
    o = [f"<title>Slides: {html.escape(title)}</title>\n",
         crest(dest, week, "Slides", html.escape(title),
               f"Segment {int(num)} of {total} &middot; {module}"),
         '\n<section>\n  <div class="wrap">\n',
         f'    <p class="intro">{len(names)} slides, in the order they appear in the lecture.</p>\n',
         '    <div class="gallery">\n']
    for i, n in enumerate(names, 1):
        o.append(f'      <figure><img src="{n}.jpg" alt="slide {i}" loading="lazy">'
                 f'<figcaption>{i}</figcaption></figure>\n')
    o += ["    </div>\n  </div>\n</section>\n", f"""
<footer>
  <div class="wrap">
    <b>Finance, Law, and Risk in the AI Product Lifecycle</b> &middot; Week {week} &middot;
    <a href="{up}week{week}.html">Back to week {week}</a> &middot;
    <a href="../../{stem}.mp4">Video</a> &middot;
    <a href="../../audio/{stem}.m4a">Audio</a> &middot;
    <a href="../../scripts/{stem}.html">Script</a>
  </div>
</footer>

""", GOAT]
    open(os.path.join(dest, "index.html"), "w").write("".join(o))
    return len(names)


if __name__ == "__main__":
    for wk in (sys.argv[1:] or ["01"]):
        module, total = WEEKS[wk]
        tp = ts = 0
        for num, stem, title in segments(wk):
            tp += build_script_page(wk, module, total, num, stem, title)
            ts += build_slides_page(wk, module, total, num, stem, title)
        print(f"w{wk} {module:36s} {tp:4d} paragraphs {ts:4d} slides")
