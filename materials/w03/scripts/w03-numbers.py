"""Every quantitative claim spoken in the week 3 lectures, computed rather than asserted.

python3 w03-numbers.py > w03-numbers.txt

Segment 2 needs bond duration and the price move for a rate shock.
Segment 4 needs the effective-independent-exposures result for a correlated book.
Segment 3 needs the runway arithmetic including the decision date.
"""

def pv_bullet(face, coupon_rate, years, y):
    """Price of an annual-pay bullet loan: coupon each year, principal at maturity."""
    c = face * coupon_rate
    return sum(c / (1 + y) ** t for t in range(1, years + 1)) + face / (1 + y) ** years


def macaulay(face, coupon_rate, years, y):
    c = face * coupon_rate
    price = pv_bullet(face, coupon_rate, years, y)
    wsum = sum(t * (c / (1 + y) ** t) for t in range(1, years + 1))
    wsum += years * (face / (1 + y) ** years)
    return wsum / price


print("=" * 66)
print("SEGMENT 2 — DURATION")
print("=" * 66)

FACE, CPN, YRS, Y0 = 100.0, 0.05, 10, 0.05
p0 = pv_bullet(FACE, CPN, YRS, Y0)
d_mac = macaulay(FACE, CPN, YRS, Y0)
d_mod = d_mac / (1 + Y0)
print(f"Ten-year bullet loan, five per cent annual coupon, priced at par yield {Y0:.0%}")
print(f"  price                {p0:8.2f}")
print(f"  Macaulay duration    {d_mac:8.2f} years")
print(f"  modified duration    {d_mod:8.2f}")

for shock in (0.02, 0.03):
    y1 = Y0 + shock
    p1 = pv_bullet(FACE, CPN, YRS, y1)
    actual = (p1 - p0) / p0
    approx = -d_mod * shock
    print(f"  rates +{shock:.0%}: price {p1:6.2f}  actual {actual:+.1%}  "
          f"duration estimate {approx:+.1%}")

# The overnight-funded liability: duration of money repayable on demand.
print("\nLiability side")
print("  demand deposit, repayable tomorrow: duration ~0.003 years (about one day)")
print(f"  duration gap for a book of these loans funded by deposits: "
      f"{d_mac - 0.003:.2f} years")

# Meridian, from segment 1, sized against the book.
BOOK, LIAB = 940.0, 800.0
for shock in (0.02, 0.03):
    y1 = Y0 + shock
    loss_pct = (pv_bullet(FACE, CPN, YRS, y1) - p0) / p0
    loss = BOOK * loss_pct
    print(f"\n  A {BOOK:.0f}m book of these loans, rates +{shock:.0%}:")
    print(f"    market value falls to    {BOOK + loss:7.1f}m  (loss {-loss:5.1f}m)")
    print(f"    against liabilities of   {LIAB:7.1f}m")
    print(f"    equity                   {BOOK + loss - LIAB:7.1f}m  "
          f"(was {BOOK - LIAB:.1f}m)")

print()
print("=" * 66)
print("SEGMENT 3 — RUNWAY")
print("=" * 66)

CASH = 48.0          # millions
GROSS_BURN = 6.0     # millions per month
REVENUE = 1.5        # millions per month
net = GROSS_BURN - REVENUE
runway = CASH / net
print(f"cash {CASH:.0f}m, gross burn {GROSS_BURN:.1f}m/mo, revenue {REVENUE:.1f}m/mo")
print(f"  net burn        {net:.1f}m per month")
print(f"  stated runway   {runway:.1f} months")

RAISE_LEAD = 7.0
print(f"  a raise takes   {RAISE_LEAD:.0f} months from first meeting to money in")
print(f"  decision date   month {runway - RAISE_LEAD:.1f}, not month {runway:.1f}")
print(f"  usable runway   {runway - RAISE_LEAD:.1f} months, "
      f"{(runway - RAISE_LEAD) / runway:.0%} of the number on the slide")

# What a 20 per cent burn overrun does, holding everything else fixed.
for over in (0.10, 0.20):
    n2 = GROSS_BURN * (1 + over) - REVENUE
    r2 = CASH / n2
    print(f"  gross burn +{over:.0%}: net {n2:.2f}m/mo, runway {r2:.1f} months "
          f"({runway - r2:.1f} months lost)")

# And what happens if revenue simply does not arrive.
r3 = CASH / GROSS_BURN
print(f"  revenue goes to zero: runway {r3:.1f} months "
      f"({runway - r3:.1f} months lost)")

print()
print("=" * 66)
print("SEGMENT 4 — CONCENTRATION")
print("=" * 66)


def effective_n(n, rho):
    """Independent-equivalent count for n equal exposures with common pairwise correlation rho.

    Var(mean) = sigma^2 * [rho + (1-rho)/n]; set equal to sigma^2 / n_eff.
    """
    return 1.0 / (rho + (1.0 - rho) / n)


N = 400
print(f"A book of {N} equal loans. Diversification depends on correlation, not count.")
for rho in (0.0, 0.05, 0.10, 0.25, 0.50):
    print(f"  pairwise correlation {rho:4.2f} -> behaves like "
          f"{effective_n(N, rho):7.2f} independent loans")

print("\nThe floor, stated as volatility rather than as a count.")
print("sd of the book average, as a fraction of one loan's sd:")
for rho in (0.0, 0.05, 0.10, 0.25):
    sd = (rho + (1 - rho) / N) ** 0.5
    print(f"  correlation {rho:4.2f} -> {sd:6.3f}  ({sd * 100:5.1f} per cent of a single loan)")
sd_ind = (1 / N) ** 0.5
sd_25 = (0.25 + 0.75 / N) ** 0.5
print(f"  the 0.25 book is {sd_25 / sd_ind:.1f} times as volatile as the "
      f"independent book of the same size")

print("\nHerfindahl on an unequal book (share of total exposure):")
books = {
    "looks concentrated": [0.40, 0.25, 0.15, 0.10, 0.10],
    "looks diversified ": [1.0 / 400] * 400,
}
for name, w in books.items():
    h = sum(x * x for x in w)
    print(f"  {name}: H = {h:.4f}, effective names = {1/h:6.1f}")

h_flat = sum(x * x for x in books["looks diversified "])
print(f"\n  The 400-name book scores {1/h_flat:.0f} effective names on Herfindahl,")
print(f"  which counts only size. At correlation 0.25 it behaves like "
      f"{effective_n(N, 0.25):.1f}.")
print("  Herfindahl sees the size distribution and is blind to the common cause.")
