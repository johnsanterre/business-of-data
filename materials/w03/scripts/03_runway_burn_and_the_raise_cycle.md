---
title: Runway, burn, and the raise cycle
series: business-of-data
week: 3
module: Liquidity, duration, concentration
section: 3
target_seconds: 900
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Many will have run or sat near a runway calculation."
method_note: >
  Contrasting cases: two developers with identical cash, identical burn and identical
  projects, where the only difference is the month in which each began raising. The
  misconception is the runway number itself, which is arithmetically correct and
  operationally misleading, so the dismantling cannot proceed by finding an error. It
  proceeds by separating the cash-out date from the decision date. The three
  assumptions inside the calculation are then taken in order of how much control the
  firm has over each, ending on the one it controls least, and the segment closes by
  showing the three are not independent.
constraint: "Must not reference the week's case. Running example is commercial property development and lending."
numbers: "All figures computed in w03-numbers.py, output in w03-numbers.txt."
status: draft 2026-09-09
---

## Script

[P1] Two property developers, Kestrel and Marlow, are building comparable logistics parks about forty miles apart. Both broke ground in the same quarter. Both hold forty-eight million dollars of cash. Both are spending six million dollars a month on construction, land payments, staff and interest. Both take in about one and a half million dollars a month from an earlier phase that is already let. Their projects will complete within a month of each other, and neither has a tenant problem.

[P2] Eighteen months later Kestrel has completed, let, and refinanced its park. Marlow's site was handed to its lender, who sold the half-built asset for about seventy cents on the dollar of what had been spent on it. The equity in Marlow was wiped out. Both projects were, and still are, good projects. The one that was taken away was finished by somebody else and let successfully within the year.

[P3] The only material difference between Kestrel and Marlow is the month in which each of them started trying to raise the next round of money. That is the whole of it. It is not the loans, not the sites, not the contractors, and not the tenants, and I want to spend this segment on why a decision about timing outranks all of those.

[P4] Start where both firms started, with a calculation that every one of you either has done or will do. Runway is cash divided by the rate at which cash leaves. Kestrel and Marlow both have forty-eight million dollars. Both are spending six and receiving one and a half, so the net rate at which money leaves is four and a half million dollars a month. Forty-eight divided by four and a half is ten point seven, so both firms have ten point seven months of runway. Both boards saw that number and both boards were told, correctly, that the firm had money into the autumn of the following year.

[P5] I want to be careful about what is wrong here, because nothing in that paragraph is wrong. The arithmetic is right. The inputs are right. The conclusion, that the money runs out in ten point seven months, is right, and it turned out to be right for both firms almost to the week. This is not a case where somebody made an error and a more careful analyst would have caught it. It is a case where a correct number was used to answer a question it does not answer.

[P6] The question the number answers is when the cash reaches zero. The question the firm needs answered is when it must act, and those are different dates because acting takes time. So the useful way to hold the runway figure is as two dates rather than one. There is a cash-out date, which the arithmetic gives you. And there is a decision date, which is the cash-out date minus however long it takes to change the situation, and it is the second one that governs behaviour.

[P7] For a raise, the interval between those dates is long and it holds steady across firms and cycles. From the first serious conversation to money actually in the account is around seven months. There are introductions, there is a first meeting, there is diligence, there are two or three parties who go a long way and then decline, there is a term sheet, and then there is documentation and conditions, and the last stretch is the one that takes longer than anyone plans for because it involves lawyers on both sides and a bank.

[P8] Put those together and the picture changes character. Ten point seven months of runway, less seven months to complete a raise, leaves a decision date at month three point seven. Not month ten. Month three point seven. The firm has to be in the market before a third of its runway has been spent, and the usable portion of that ten point seven month figure is thirty-four per cent of it. Roughly two thirds of the runway on the slide is not available for deciding anything. It is the time the raise itself consumes.

[P9] Kestrel began raising in month three. Marlow began in month seven, which felt prudent to Marlow's board because seven months of spending still left three and a half months of cash, and three and a half months sounds like a margin. It is not a margin. It is four months less than the process requires, and Marlow spent the last of those months negotiating with people who could see the bank balance and knew exactly how long it had.

[P10] That is the second half of the timing problem, and it deserves its own statement. Your negotiating position in a financing is not a function of the quality of the asset. It is a function of how much runway you have left when you sit down, because the alternative to agreeing is what determines the price, and a firm with two months of cash has no alternative. The same site, the same tenants and the same numbers will be priced completely differently depending on whether the person across the table thinks you can walk away.

[P11] So a raise begun at month three is a negotiation and a raise begun at month eight is a liquidation with extra steps. Marlow did receive offers. They were priced at a level that would have left the existing equity with almost nothing, which the board rejected in month nine as unacceptable, and then it accepted a worse one in month ten, and then that one failed its conditions and there was no time to start again. None of those decisions was stupid. All of them were made from a position that had been fixed months earlier by a decision about when to start.

[P12] Now I want to take the runway calculation apart, because underneath that single number are three separate assumptions, and it is worth seeing them individually before seeing what they do together. The number assumes the burn stays where it is. It assumes the revenue arrives as forecast. And it assumes that at the end of the runway there is a next round available on terms the firm would accept. Each of those can break, and they break in a particular order of severity.

[P13] Take the burn first, because it is the one the firm controls and therefore the one people assume is safe. It is not stable. Burn is a consequence of decisions made three to six months earlier. The staff on the payroll were hired in the spring. The contractor was mobilised under a contract with a notice period. The lease on the site office runs to a date. What a firm is spending this month is the output of commitments it made before it knew what this month would look like.

[P14] Which means the burn also has a decision date, and this is the piece that surprises people the first time they meet it. Cutting spending takes about as long as creating it did. A hiring decision made in March produces salary cost from May and cannot be unwound before a notice period runs. So the firm that decides in month eight to reduce its burn does not have a lower burn in month eight. It has a lower burn in month ten, plus redundancy costs in month eight, and in the near term the cut makes the cash position slightly worse.

[P15] The arithmetic of an overrun is unforgiving in a way that is worth seeing directly, because the leverage runs through the net figure. Suppose gross burn comes in twenty per cent above plan, at seven point two million rather than six. Revenue is unchanged. Net burn goes from four and a half to five point seven, and the runway falls from ten point seven months to eight point four. A twenty per cent overrun on spending has removed two point two months, which is more than half of the entire decision window we computed a moment ago.

[P16] Second assumption, the revenue. Kestrel and Marlow both booked one and a half million a month from the completed earlier phase, and both treated it as reliable, which it largely was. But run the case where it goes to zero, because a tenant fails or a lease ends and is not renewed. Net burn becomes the full six million and the runway falls from ten point seven months to eight. That is two point seven months gone from a loss of income that is, in absolute terms, small relative to the spending.

[P17] The asymmetry there is worth naming. Revenue enters the calculation through the denominator, so a small revenue number attached to a large burn number has an outsized effect on the date. One and a half million against six million of spending looks like a rounding item on an income statement and is worth almost three months of survival. Firms consistently underweight the small revenue line for exactly this reason: its importance does not show up where they are looking at it.

[P18] Third assumption, and the one that actually kills firms: that a next round exists. Notice what is different about this one. Burn is inside the firm. Revenue is mostly inside the firm's relationships. But the availability of capital in month eleven is a property of the outside world, and no amount of good execution makes it true. A firm can hit every operational target it set and find that the market it planned to raise into has closed.

[P19] It is worth being concrete about what closing means, because it is rarely a formal event. What happens is that the parties who would have led the round decide to support their existing positions instead of adding new ones, diligence periods stretch from six weeks to four months, and the terms on offer shift from growth pricing to structured downside protection. Nobody announces any of this. The firm experiences it as meetings that go well and then go quiet, which is indistinguishable from ordinary rejection until the fourth time it happens.

[P20] There is a version of this that catches firms which believe they have already solved it, and it turns on the difference between money committed and money received. A construction facility is typically agreed once and drawn in tranches, and each drawdown is conditional. The lender requires a surveyor's certificate that the works have reached a stage, or a valuation above a threshold, or a covenant to be met on the day of the draw. A firm that says it has a hundred million dollars committed has a hundred million dollars of conditions.

[P21] The conditions are the problem, and specifically that they are tested repeatedly rather than once. A facility agreed in good conditions is drawn in whatever conditions prevail on the drawdown date, and the tests are written in terms of exactly the quantities that move when things go wrong. A loan-to-value test fails when values fall. An interest cover test fails when rates rise. A material adverse change clause is deliberately broad and is invoked when the lender wants out.

[P22] So the conditional funding is correlated with everything else on the list, and correlated in the same unhelpful direction. The conditions bind when the firm needs the money, and are satisfied comfortably when it does not. A facility of this shape is not a buffer against a bad outcome. It is a facility that works in the states of the world where the firm was going to be fine anyway.

[P23] Which suggests a change to how the runway calculation should be laid out, and it is a small change with real consequences. Compute the runway from unconditional cash only. Then show conditional money as a separate line with two things attached to it: the date each condition is tested, and an honest view of whether it holds under the same stress you applied to burn and revenue. A firm that reports one number combining the two has hidden its actual position inside an average, and the board reading that number cannot see the hiding.

[P24] And now the point I want to leave you with, because it is the same structural point as the previous segment in different clothes. Those three assumptions are not independent of one another. The economic conditions that cause a tenant to fail are the conditions that cause construction costs to overrun and the conditions that cause capital to withdraw. The three inputs to the runway calculation are correlated, and they are correlated positively, which is the worst direction.

[P25] So the sensible-sounding practice of stressing one input at a time understates the risk by a wide margin. A firm that models a twenty per cent burn overrun gets eight point four months. A firm that models revenue going to zero gets eight. Both feel like conservative planning. But the world does not deliver one of those at a time. It delivers both, alongside a funding market that has become slower and more expensive, and the combination lands well inside the seven month window the raise requires.

[P26] Let me put this from the position of the person on the other side of the table, because it explains behaviour that otherwise reads as predatory. An investor being asked to fund a firm with three months of cash is not evaluating the asset. They are evaluating a firm that has no alternative, and they know that if they decline and come back in six weeks the price will be lower. Waiting is a rational strategy that costs them nothing, and the firm's deteriorating position is the mechanism that makes waiting profitable. That is why late raises do not merely price badly, they stall.

[P27] From the board's position the failure is usually a failure of what gets escalated rather than of judgment. The board sees a runway number monthly. That number is a cash-out date, and unless somebody has done the subtraction in front of them, the decision date is not on the page. A board can watch a runway figure fall from eleven months to eight to six, discussing it each time, and never once be shown the month in which its options close, because the report was built to answer the question that has an arithmetic answer.

[P28] Here is one to work. Thornbury Estates holds thirty million dollars. It spends five million a month and receives two. It has a term sheet from an existing investor for a further forty million, subject to a planning consent which the council will decide in four months, and the investor's commitment expires two months after that. Tell me Thornbury's runway, tell me its decision date, and tell me what the actual exposure is.

[P29] Runway is thirty divided by three, which is ten months. The decision date, if the firm had to run a fresh raise, would be month three. But Thornbury does not have a plain runway problem, it has a conditional one, and the condition is held by a planning committee. If consent arrives on schedule the firm is funded with six months to spare. If consent slips by three months, which is ordinary for planning, the commitment expires and the firm is at month seven with three months of cash and no time to raise from anybody else.

[P30] So the real exposure is not the ten month figure, it is that Thornbury has made its survival conditional on the calendar of a body it does not control, and has no fallback that can be started late. The single most valuable thing its board could do is decide, now, in month one, what it will do if consent slips, and start whatever that is in parallel rather than sequentially. The cost of running a second process it may not need is a few hundred thousand dollars. The cost of not having one is the company.

[P31] One thread runs through all three segments so far. Meridian's depositors, Calder's rate exposure, and Marlow's funding market were each a single event arriving at many places at once, and each firm had counted the many places and believed itself covered. The next segment is about that counting, and about why four hundred separate exposures can behave as though there were four.
