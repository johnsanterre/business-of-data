---
title: The classification choice
series: business-of-data
week: 2
module: How an asset is carried
section: 3
target_seconds: 900
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Follows sections 1 and 2."
method_note: >
  Contrasting cases open with three institutions holding the identical bond and
  reporting three different results. The misconception is that a fall in value must
  appear somewhere. Vantage points are the treasurer who picks the label, the
  supervisor who reads the note, and the counterparty who cannot see it. Two regimes
  are covered deliberately, because held-to-maturity and available-for-sale are
  securities classifications and do not apply to equipment. Sets up week 13.
constraint: "Must not reference the week's case."
status: draft 2026-09-07, rebuilt for the ear
---

## Script

[P1] Three institutions each hold the same bond. Same issuer, same coupon, same maturity, and each of them paid one hundred million dollars for it on the same day. Two years later, interest rates have risen, and that bond would now sell for eighty-eight million. Twelve million dollars of decline, identical for all three.

[P2] Now look at what each of them reports. The first institution reports a twelve million dollar loss, which flows through the income statement and reduces its profit for the year. The second reports no effect on profit at all, but its equity is twelve million lower, in a section of the accounts below net income that most readers skip. The third reports nothing. Its balance sheet still shows the bond near one hundred million, its profit is untouched, and the twelve million appears only as a line in a note, several hundred pages into the annual report.

[P3] Every one of those three treatments is correct. Every one was audited. None of them is aggressive, and none of them is a loophole. The difference between them was fixed on the day each institution bought the bond, by a label somebody applied in a system.

[P4] Here is the assumption that makes this confusing, and it is worth stating precisely because it is exactly backwards. Most people assume that a fall in the value of something a company owns has to show up somewhere, and that the only question is where. Perhaps in profit, perhaps in equity, perhaps in a footnote, but somewhere, and the accounts are in some sense keeping score. That is not the arrangement. Whether a movement is recognised at all is a matter of classification, and classification is a matter of stated intention.

[P5] Before I go further I have to separate two regimes, because they are constantly confused and the confusion produces real errors. Held to maturity and available for sale are classifications for debt securities. Bonds, notes, and similar instruments. They do not apply to equipment, and if you hear somebody say a company classified its machinery as held to maturity, they have muddled two different parts of the standards. Equipment and other long-lived assets have their own classification question, which is simpler and which we will get to. Both regimes answer the same underlying question about whether market movements reach the accounts. They answer it differently, and knowing which regime you are in is the first move.

[P6] Take the securities regime first, because the mechanism is starkest there. There are three buckets. A security classified as **trading** is marked to market every reporting date and the movement goes straight through profit. That is the first institution. A security classified as **available for sale** is also marked to market, so the balance sheet carries it at eighty-eight million, but the movement is parked in equity rather than run through profit. That is the second institution. A security classified as **held to maturity** is not marked at all. It sits at amortised cost, near the original hundred million, and the eighty-eight million appears only as a disclosure. That is the third.

[P7] Notice what the three buckets are actually sorting on. They are not sorting on the security, because the security is identical. They are sorting on what the institution says it intends to do with it. Trading means I intend to sell it soon. Available for sale means I might sell it. Held to maturity means I intend to hold it until it matures and get my hundred million back, in which case today's price is irrelevant to me and marking it would introduce noise rather than information.

[P8] That last argument is a good one, and I want to give it its full weight before we start looking for problems. If an institution genuinely will hold a bond to maturity, then the eighty-eight million is not a loss in any economic sense. It is a snapshot of what somebody else would pay today, and the institution is not selling today. Marking it would make the accounts swing around on movements the institution will never realise. Held to maturity accounting is not a trick. It is a considered answer to a real problem.

[P9] But the classification comes with a condition, and the condition is where everything interesting happens. To use held to maturity, an institution must have both the **intent** and the **ability** to hold until maturity. Intent is an assertion by management. Ability is a question about liquidity, and it is the one that bites, because an institution that might be forced to sell in order to raise cash does not have the ability, no matter what it intends.

[P10] The classification also has teeth built into it. If an institution sells a meaningful portion of what it had designated held to maturity, it can be barred from using that classification for a period, which forces the remainder of the portfolio into a bucket where the losses become visible. The industry calls this tainting. It exists specifically to stop an institution from designating a portfolio as held to maturity when convenient and quietly selling out of it when convenient. So the label is not a description. It is a commitment, and breaking it is expensive by design.

[P11] Now hold that structure in your head, because it produces a very specific failure mode and it is the reason this segment exists. An institution with a large held-to-maturity portfolio that has fallen substantially in value is carrying an unrecognised loss. It is disclosed but not booked. As long as the institution holds, that is fine, and it is exactly what the classification is for. But the moment it is forced to sell, the loss becomes real, immediate, and public.

[P12] Trace the sequence, because the ordering is the whole thing. The classification depends on the ability to hold. The ability to hold depends on liquidity. So when liquidity goes, the accounting goes with it, in the same moment, and the institution announces both at once. The classification never reduced the loss. It deferred recognition, and it deferred it in a way that coupled the accounting to the thing most likely to fail at the worst time. We will spend an entire week on a version of this in week thirteen.

[P13] Let me take the vantage points, because three people see this arrangement very differently. Start with the treasurer, who applies the label. On the day of purchase this is close to a clerical decision. The treasurer knows the institution's funding profile, knows this bond is part of a portfolio intended to sit there and earn a spread, and designates it held to maturity because that is what is true. The treasurer is not doing anything clever. They are recording an intention that is genuine on the day they record it.

[P14] Now the supervisor, or any regulator reading the same accounts. The supervisor's problem is that the institution's stated intent is exactly the thing that stops being true under stress, and the accounts by construction report the intent rather than the stress. So the supervisor cannot rely on the balance sheet for this. It has to go to the disclosure, compare the amortised cost against the fair value, and form its own view of what the institution would look like if it had to sell. That number is available. It is in the notes, it is required, and reading it is a deliberate act that somebody has to choose to perform.

[P15] Third, the counterparty. A depositor, a lender, a large customer. This person almost certainly cannot see any of it. They are looking at a balance sheet that shows a hundred million, and the twelve million gap requires them to know that the disclosure exists, to find it, and to understand what it means. In practice they run on the headline, and when they eventually learn about the gap they learn about it from a news report, all at once, along with everybody else. The speed at which that group changes its mind is the mechanism that turns a disclosed gap into a failure.

[P16] Now the other regime, for equipment and other long-lived assets, and it is much simpler. There is no held to maturity here and no available for sale. There are two states. An asset is **held for use**, or it is **held for sale**. Almost everything is held for use, which is the default, and a held-for-use asset is carried at cost less accumulated depreciation, exactly as the first two segments described. Market movements do not touch it. If the aircraft Northline paid fifty million for is now worth forty-one, the accounts continue to show whatever the depreciation schedule says.

[P17] Held for sale is a narrow classification with a specific trigger. To use it, the company must be committed to a plan to sell, the asset must be available for immediate sale, and a sale must be probable within about a year. Once an asset moves into held for sale, two things change at once. Depreciation stops, because the asset is no longer being consumed in operations. And the asset is measured at the lower of its carrying amount or its fair value less costs to sell, which means for the first time the market can force the number down.

[P18] So here is the second contrast for this segment. Two manufacturers each own an identical plant, each carried at sixty million, and each worth about forty million if sold. The first intends to keep operating it, so it stays at sixty. The second has decided to close and sell it, so it moves to held for sale and is written down to forty, and that twenty million charge lands in the period of the decision. Same plant, same market, same forty million. One of them books a twenty million loss and the other does not, and the difference is a decision about the future.

[P19] For assets that stay held for use, the only route by which market reality reaches the accounts is impairment, and it is worth being precise about how high that bar is, because people assume it is more sensitive than it is. The usual test has two steps. First, compare the carrying amount against the total **undiscounted** cash flows the asset is expected to generate over its remaining life. Undiscounted means you simply add up the future cash without reducing it for the time value of money, which is a deliberately forgiving comparison. Only if the carrying amount exceeds that sum do you go to the second step and measure the write-down against fair value.

[P20] Work the consequence through, because it explains a lot. An asset carried at sixty million that generates six million a year for another fifteen years has ninety million of undiscounted future cash flow. Ninety is comfortably above sixty, so the test passes, and it passes even if the asset would only fetch forty million today. The test is not asking about market value. It is asking whether the asset will pay for itself, without discounting. Which is why the gap between carrying value and market value can persist for years in exactly the companies where it matters most.

[P21] Let me work that test with numbers, because the arithmetic is where it becomes obvious. A haulage company owns a distribution terminal carried at sixty million. The terminal generates six million a year of cash and has fifteen years of life left. Step one asks whether sixty million exceeds the undiscounted future cash flows. Fifteen years at six million is ninety million. Ninety is greater than sixty, so the test passes and there is no impairment, and we never reach step two.

[P22] Now suppose a buyer would pay forty million for that terminal, which is twenty million below what it is carried at. Does anything change? No. The test never asked about the buyer. The company continues to carry the terminal at sixty, reports depreciation on sixty, and is entirely compliant. For the test to fail, the terminal's expected cash generation would have to fall below sixty million in total, which at six million a year means the remaining life would have to drop below ten years. The market price could halve again without moving the accounts by a dollar.

[P23] Here is a fourth party worth adding, because they are the ones who eventually close this gap: the acquirer. When one company buys another, the acquirer records the assets it has bought at fair value on the acquisition date, not at whatever the seller was carrying them at. So an acquisition resets every carrying value in the target to the market's view in one step. This is why acquirers frequently record charges in the years after a deal that the target never had to record, and it is one of the few mechanisms in the system that forces a whole balance sheet to face the market at once.

[P24] Pull the two regimes together, because the shared structure is what to remember. In both, a classification made at acquisition determines whether later market movements are recognised. In both, the classification that defers recognition rests on a statement of intent by management. And in both, the deferral is entirely legitimate while the intent holds and collapses when it does not. Securities held to maturity become a realised loss when liquidity forces a sale. Equipment held for use becomes a write-down when a sale is planned or when the cash it generates stops covering what it is carried at.

[P25] So two questions travel together whenever you read a balance sheet. First, which classification is each significant asset in, and what did that classification require the company to assert about its own intentions? Second, what is the gap that the classification is holding out of the accounts, and can you find it in the notes? Very often you can. It is disclosed somewhere that affects no headline number, which is precisely the point of the classification, and it is available to anybody who goes looking.

[P26] The next segment is where this stops being an accounting matter. So far, a classification or an estimate has moved numbers around inside a document. Next we look at what happens when somebody lends money against those numbers, and writes a contract that says the company is in default if they move the wrong way.

## Slides
