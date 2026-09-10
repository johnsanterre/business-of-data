#!/usr/bin/env python3
"""Point the week pages at YouTube instead of local mp4 files.

    python3 embed_youtube.py 1 2 3 4

Each week is one YouTube video with chapters, so a per-segment link becomes a
timestamped link into the full lecture rather than disappearing. The offsets come
from materials/stitched.json, which stitch_weeks.py measured from the finished
files, so nothing here is retyped and the timestamps cannot drift from the video.

The embed uses youtube-nocookie.com, which does not set tracking cookies until
the viewer presses play.

Idempotent. Running it twice leaves the pages unchanged, because the second run
finds no .mp4 links and no missing embed.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
STITCHED = os.path.join(HERE, "stitched.json")

VIDEOS = {
    1: "VNaCSVsYdgc",
    2: "Coo6hAVgdKI",
    3: "UkhdsBVUoLo",
    4: "6-6eIDzoKXQ",
}

EMBED = """    <div class="lecture">
      <iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="{title}"
              loading="lazy" allowfullscreen
              allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe>
    </div>
    <p class="lecture-note">The full lecture runs {mins} minutes in {n} chapters. Each
       segment below links to its own starting point in the video.
       <a class="watch" href="https://youtu.be/{vid}">Open on YouTube</a></p>
"""


def seconds(stamp):
    """'1:06:18' or '9:53' to an integer number of seconds."""
    parts = [int(p) for p in stamp.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def rewrite(week, record):
    vid = VIDEOS[week]
    path = os.path.join(SITE, f"week{week}.html")
    page = open(path, encoding="utf-8").read()

    offsets = [seconds(c.split(" ", 1)[0]) for c in record["chapters"]]
    links = re.findall(r'href="materials/w\d\d/\d\d_[^"]+\.mp4"', page)

    if not links and 'class="lecture"' in page:
        print(f"week {week}: already done, unchanged")
        return False
    if len(links) != len(offsets):
        sys.exit(f"week {week}: {len(links)} video links but "
                 f"{len(offsets)} chapters, refusing to guess")

    # Replace in document order, so link N gets chapter N's offset.
    it = iter(offsets)
    page = re.sub(r'href="materials/w\d\d/\d\d_[^"]+\.mp4"',
                  lambda m: f'href="https://youtu.be/{vid}?t={next(it)}"', page)

    anchor = '    <div class="segs">'
    if anchor not in page:
        sys.exit(f"week {week}: no segment list found, cannot place the embed")
    block = EMBED.format(vid=vid, title=f"The Business of Data, week {week}",
                         mins=round(record["seconds"] / 60), n=len(offsets))
    page = page.replace(anchor, block + anchor, 1)

    if ".mp4" in page:
        sys.exit(f"week {week}: an mp4 link survived the rewrite")
    open(path, "w", encoding="utf-8").write(page)
    print(f"week {week}: {len(offsets)} links repointed, embed added, "
          f"video {vid}")
    return True


def rewrite_subpages(week, record):
    """The per-segment slide and script pages link the same mp4 files.

    Each filename starts with its segment number, so the chapter offset comes
    from the same list the week page uses. The relative depth differs between
    slides/NN/ and scripts/, which is why the path is matched loosely and only
    the filename is read.
    """
    vid = VIDEOS[week]
    offsets = [seconds(c.split(" ", 1)[0]) for c in record["chapters"]]
    root = os.path.join(HERE, f"w{week:02d}")
    pat = re.compile(r'href="[^"]*?/?(\d\d)_[^"/]+\.mp4"')
    touched = 0

    for dirpath, _, files in os.walk(root):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            page = open(path, encoding="utf-8").read()
            if ".mp4" not in page:
                continue

            def sub(m):
                n = int(m.group(1))
                if not 1 <= n <= len(offsets):
                    sys.exit(f"{path}: segment {n} has no chapter")
                return f'href="https://youtu.be/{vid}?t={offsets[n - 1]}"'

            new = pat.sub(sub, page)
            if ".mp4" in new:
                sys.exit(f"{path}: an mp4 link survived the rewrite")
            if new != page:
                open(path, "w", encoding="utf-8").write(new)
                touched += 1

    print(f"week {week}: {touched} slide and script pages repointed")
    return touched


if __name__ == "__main__":
    records = {r["week"]: r for r in json.load(open(STITCHED))}
    weeks = [int(a) for a in sys.argv[1:]] or sorted(VIDEOS)
    changed = sum(rewrite(w, records[w]) for w in weeks)
    subs = sum(rewrite_subpages(w, records[w]) for w in weeks)
    print(f"\n{changed} week pages and {subs} sub-pages changed")
