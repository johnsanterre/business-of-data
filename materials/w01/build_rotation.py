"""Render the rotation calendar page from rotation.py's schedule.

python3 build_rotation.py

Reads the exact 16-student, 4-seat, 12-week schedule out of planning/rotation.py
and the four named roles out of each week page, then writes rotation.html.
Regenerate after any change to the roles on a week page.
"""
import os, re, sys, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, "..", ".."))
STUDENTS, SEATS, WEEKS = 16, 4, list(range(2, 14))

spec = importlib.util.spec_from_file_location(
    "rotation", os.path.join(SITE, "planning", "rotation.py"))
rot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rot)

schedule = rot.affine_16()                       # [{seat_index: student}, ...] per week
seat_name = "ABCD"


def week_meta(w):
    """Title, case, and the four role names, taken from the week page itself."""
    t = open(os.path.join(SITE, f"week{w}.html")).read()
    title = re.search(r"<h1>(.*?)</h1>", t, re.S).group(1).strip()
    case = re.search(r"Case: <b>(.*?)</b>", t)
    roles = re.search(r"<b>Live session roles</b>(.*?)</p>", t, re.S)
    rl = [r.strip() for r in roles.group(1).split("&middot;")] if roles else []
    return title, (case.group(1) if case else ""), rl


rows, per_student = [], {s: [] for s in range(1, STUDENTS + 1)}
for w, assign in zip(WEEKS, schedule):
    title, case, roles = week_meta(w)
    if len(roles) != SEATS:
        sys.exit(f"week {w} lists {len(roles)} roles, expected {SEATS}")
    seats = [(seat_name[i], assign[i], roles[i]) for i in range(SEATS)]
    rows.append((w, title, case, seats))
    for letter, student, role in seats:
        per_student[student].append((w, letter, role, case))

# invariants, re-checked here so the published page cannot drift from the claim it makes
turns = {s: len(v) for s, v in per_student.items()}
assert set(turns.values()) == {3}, turns
assert all(len({l for _, l, _, _ in v}) == 3 for v in per_student.values()), "seat repeat"
pairs = {}
for _, _, _, seats in rows:
    ids = sorted(s for _, s, _ in seats)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            pairs[(ids[i], ids[j])] = pairs.get((ids[i], ids[j]), 0) + 1
assert max(pairs.values()) == 1, "partner repeat"

out = ["""<title>Role rotation calendar</title>
<link rel="stylesheet" href="../../course.css">

<header>
  <div class="wrap">
    <div class="crest">
      <a class="uc" href="../../index.html">Berkeley</a>
      <span class="prog">The Business of Data</span>
      <span class="term">Winter 2027</span>
    </div>
    <div class="mast-week">
      <a class="back" href="../../week1.html">&larr; Week 1</a>
      <p class="wknum">Rotation</p>
      <h1>Role rotation calendar</h1>
      <p class="role">Three panels each, twelve weeks, no repeated seat and no repeated partner.</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap doc">
    <p>Sixteen students, four roles a week, twelve case weeks. Every student sits on three
      panels, holds a different role each time, and never shares a panel with the same
      classmate twice.</p>
    <p>Those three properties hold exactly rather than approximately. Arrange sixteen
      students in a four by four grid, and the rows, the columns and the broken diagonals are
      three parallel classes of the affine plane of order four. Any two of those blocks meet
      in exactly one point, which is the same statement as no two students meeting twice.</p>
    <p><b>Find your number below and note your three weeks now.</b> Panel weeks are heavy and
      the weeks between them are light, which mirrors real work and wrecks a student who
      discovers four days out that their panel week collides with another course's midterm.</p>

    <h2>By week</h2>
"""]

out.append('    <div class="wide"><table class="plain">\n      <tr><th class="num">Week</th><th>Case</th>')
for i in range(SEATS):
    out.append(f'<th>Seat {seat_name[i]}</th>')
out.append("</tr>\n")
for w, title, case, seats in rows:
    out.append(f'      <tr><td class="num">{w}</td>'
               f'<td><a href="../../week{w}.html"><b>{html.escape(case)}</b></a>'
               f'<br><span class="muted">{title}</span></td>')
    for letter, student, role in seats:
        out.append(f'<td><b class="num">{student}</b><br><span class="muted">{role}</span></td>')
    out.append("</tr>\n")
out.append("    </table></div>\n")

out.append("""
    <h2>By student</h2>
    <div class="wide"><table class="plain">
      <tr><th class="num">You are</th><th>First panel</th><th>Second panel</th><th>Third panel</th></tr>
""")
for s in range(1, STUDENTS + 1):
    out.append(f'      <tr><td class="num">{s}</td>')
    for w, letter, role, case in per_student[s]:
        out.append(f'<td><b>Week {w}</b> &middot; {html.escape(case)}'
                   f'<br><span class="muted">{role}</span></td>')
    out.append("</tr>\n")
out.append("    </table></div>\n")

out.append(f"""
    <div class="prov" style="margin-top:36px">Generated by
      <code>materials/w01/build_rotation.py</code> from <code>planning/rotation.py</code>,
      with the roles read from each week page. Verified on generation:
      {min(turns.values())} turns for every student, zero repeated seats, zero repeated
      partners across all {len(pairs)} pairings that occur.</div>
  </div>
</section>

<footer>
  <div class="wrap">
    <b>The Business of Data</b> &middot; Week 1 &middot;
    <a href="../../week1.html">Back to week 1</a> &middot;
    <a href="panel-guide.html">Preparing a role</a>
  </div>
</footer>

<script data-goatcounter="https://johnsanterre.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
""")

open(os.path.join(HERE, "rotation.html"), "w").write("".join(out))
print(f"rotation.html written: {len(rows)} weeks, {STUDENTS} students, "
      f"{min(turns.values())} turns each, 0 seat repeats, 0 partner repeats")
