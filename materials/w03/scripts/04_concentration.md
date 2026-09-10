---
title: Concentration
series: business-of-data
week: 3
module: Liquidity, duration, concentration
section: 4
target_seconds: 1200
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Comfortable with variance; no portfolio theory assumed."
method_note: >
  Contrasting cases with the answer withheld: two loan books that every reader will
  rank confidently and wrongly. The standard measure is then built in full and shown
  to separate them by a factor of a hundred, so the learner has committed to it before
  it is undermined. The undermining is arithmetic rather than rhetorical: the variance
  of an average has a floor set by correlation and not by count, and the two books
  land on the same effective number. Closes on the same structural point as segment
  two, that the measurement is at its most reassuring when it is least reliable.
constraint: "Must not reference the week's case. Running example is commercial property lending."
numbers: "All figures computed in w03-numbers.py, output in w03-numbers.txt."
status: draft 2026-09-09
---

## Script

[P1] Two loan books, and I want you to rank them before I say anything else about either. The first book holds five loans. The largest is forty per cent of the book, the next is twenty-five, then fifteen, then ten and ten. The second book holds four hundred loans, each one a quarter of one per cent of the total, no loan larger than any other, spread across four hundred separate borrowers who have never met.

[P2] Every risk committee in the world ranks those the same way, and so did you. The first book is concentrated, obviously and uncomfortably so, and a regulator looking at it would want a conversation about that forty per cent. The second is the picture of a diversified book. Four hundred names is what diversification looks like when somebody draws it.

[P3] By the end of this segment I am going to show you that under a condition which is ordinary rather than exotic, those two books are the same position. Not similar, not comparable. The same. And the book that will be flagged in the risk report is the first one.

[P4] Before that, let me give the belief its strongest form, because it is not foolish and it is embedded in regulation. The belief is that concentration is about size: that the danger is having too much money with any one party, and that the way to manage it is to count your exposures and cap the largest. Under that belief, a book with four hundred equal exposures has diversified as thoroughly as a book of that size can, and there is no further work to do.

[P5] That belief has a measure attached to it, and the measure is used everywhere, so it is worth building properly rather than dismissing. It is the Herfindahl index. Take each exposure as a share of the total, square each share, and add them up. Squaring is what does the work: it makes a large share count for far more than several small ones summing to the same amount, which is exactly the property you want in a concentration measure.

[P6] Run it on the first book. Forty per cent is zero point four, squared is zero point one six. Twenty-five per cent gives zero point zero six two five. Fifteen gives zero point zero two two five. The two tens give zero point zero one each. Add them and the index is zero point two six five.

[P7] The index on its own is hard to interpret, so it is conventionally inverted, and the reciprocal has a clean meaning: it is the number of equal-sized exposures that would produce the same index. One divided by zero point two six five is three point eight. So the first book, despite holding five loans, behaves for concentration purposes like a book of about three point eight equal loans. That is a genuinely useful thing to know and the measure has earned its place.

[P8] Now run it on the second book. Each share is one four-hundredth, which is zero point zero zero two five. Squared, that is six and a quarter millionths. Four hundred of those sum to zero point zero zero two five. The reciprocal is four hundred. So the second book scores four hundred effective names against the first book's three point eight, and the standard measure separates them by a factor of a hundred and five.

[P9] Hold onto that factor of a hundred, because everything that follows is about the fact that it is an artefact. The Herfindahl index measures the distribution of sizes. That is all it measures, and it does that correctly. The question it is being used to answer is whether the book will move as one thing, and size distribution is only half of what determines that. The other half is not in the input.

[P10] So let me build the other half from the beginning, because the intuition matters more than the formula. Holding many things reduces risk for one reason only. If the things move independently, their errors cancel. When one borrower has a bad year another has a good one, and the average of many independent outcomes is far more stable than any single outcome. This is the only reason diversification works. It is not that you own more things. It is that the things disagree with each other.

[P11] Which tells you immediately what breaks it. If the four hundred loans do not disagree, if they all have a good year together and a bad year together, then averaging them accomplishes nothing at all. Four hundred copies of the same outcome average to that outcome. The count was never the mechanism, and a book of four hundred perfectly correlated loans is arithmetically identical to a book of one loan four hundred times the size.

[P12] Real books sit between those two extremes, and the position between them is what correlation measures. So the honest question about a book is not how many loans are in it but how much of what happens to one of them also happens to the others, and there is a piece of arithmetic that turns that into a number you can put next to the Herfindahl figure.

[P13] Here is the arithmetic in words. Take a book of N equal exposures where every pair moves together to the same degree, and call that degree rho. The variance of the average outcome comes to the individual variance multiplied by a bracket, and inside the bracket you have rho, plus the quantity one minus rho divided by N. Two terms. The second term is the diversification you are buying, and it falls away as N grows. The first term does not have an N in it.

[P14] That is the entire result and it is worth stating plainly. As the number of loans grows, the second term goes to zero and the first term stays exactly where it is. Diversification does not reduce risk toward nothing. It reduces risk toward rho, and rho is a property of what the borrowers have in common, not of how many of them you found. There is a floor, the floor is set by correlation, and no amount of counting gets you underneath it.

[P15] So we can convert any correlated book into the number of genuinely independent exposures that would carry the same risk, which lets us compare like with like. Set the correlated variance equal to the independent one and solve, and the effective count is one divided by that same bracket. That number is directly comparable to the reciprocal Herfindahl figure we computed a moment ago, which is what makes the comparison at the end of this possible.

[P16] Take the four hundred name book and put correlations through it. At correlation zero, the loans are genuinely independent and the effective count is four hundred, which is what the Herfindahl index said. The two measures agree exactly, and they agree in the one case where correlation contributes nothing. So Herfindahl is not wrong. It is the special case, and the special case is the one that does not occur.

[P17] Now move correlation to zero point zero five, which is a mild degree of common movement, the sort you would get from four hundred borrowers who merely operate in the same national economy. The effective count falls from four hundred to nineteen. Four hundred loans, five per cent correlation, and ninety-five per cent of the diversification is gone.

[P18] Take it to zero point one, still low by any standard, the level you might attribute to borrowers in the same broad sector. The effective count is nine point eight. Four hundred names behaving like about ten. And at zero point two five, which is what you would expect from four hundred property borrowers operating in the same city with the same tenants and the same interest rates, the effective count is three point nine seven.

[P19] Three point nine seven. Now go back to the first book, the one with the forty per cent loan that everybody flagged. Its reciprocal Herfindahl was three point eight. The four hundred name book at correlation zero point two five is three point nine seven. Those are the same number. The book everyone in the room called concentrated and the book everyone in the room called diversified are carrying the same risk, and the second one is slightly worse.

[P20] There is a second way to state the floor which lands harder than the count does, because it is denominated in the thing a treasurer actually feels. Instead of asking how many independent loans the book behaves like, ask how volatile the whole book is compared with a single loan in it. For four hundred genuinely independent loans the answer is five per cent: the book is twenty times steadier than any one borrower, which is the whole promise of diversification and it is a large promise.

[P21] Now apply correlation of a quarter to the same four hundred loans. The volatility of the book is fifty point two per cent of the volatility of one loan. Not five per cent. Half. A portfolio of four hundred separate borrowers, none of them large, swings half as much as a single borrower does, and it is ten times as volatile as the four-hundred-loan book the committee believes it owns. Every one of those four hundred credit decisions was made carefully, and the careful work bought a factor of two where the committee had priced in a factor of twenty.

[P22] I want to sit on that rather than move past it. Both books would be reported monthly. The first one would appear on an exceptions list, prompt a discussion, and possibly a cap. The second one would appear in a table of compliant portfolios with a note that the largest exposure is a quarter of one per cent. Nothing in the reporting system is capable of showing that they are the same, because the system was built around a measure that takes sizes as its input and cannot take a common cause as its input at all.

[P23] The correlation comes from anything the borrowers share, and shared things are easy to list once you go looking. A city, because a local employer closing hits every tenant in it. An industry, because a sector downturn arrives everywhere at once. A tenant, because four hundred separate buildings let to branches of one retailer are one exposure wearing four hundred hats. An interest rate, because every borrower on a floating rate is squeezed by the same central bank decision on the same day.

[P24] And a lender, which is the one people miss. If four hundred borrowers all refinance with the same small number of banks, then a decision by those banks to reduce their property exposure hits all four hundred simultaneously, regardless of how each individual building is performing. The borrowers have nothing in common commercially and are nonetheless perfectly linked through their funding, which is a correlation created entirely on the liability side of somebody else's balance sheet.

[P25] Notice that none of these appears in a credit file. A credit file describes the borrower: the covenant, the tenant, the loan to value, the cover ratio. Every one of the shared causes I just listed is a property of the relationship between borrowers, and a system that stores one record per borrower has nowhere to put it. The information is not hidden. It is unstorable in the structure being used.

[P26] The regulation inherits the same blindness, which matters because firms tend to treat compliance as the definition of adequate. Large exposure limits are written per counterparty: no more than some percentage of capital to any one client. That is a rule about the size distribution, which is to say it is the Herfindahl index with a legal threshold attached, and a book of four hundred quarter-per-cent loans satisfies it without effort no matter what those borrowers have in common.

[P27] The rules do make an attempt at the problem, through the idea of connected clients, which requires exposures to be aggregated when borrowers are linked. But read what counts as linked: common ownership, control, or a guarantee running between them. Those are legal relationships, and they are the ones already recorded in a file somewhere. Four hundred borrowers who share a city, a dominant employer, and a refinancing market are connected in every way that determines whether they default together, and connected in none of the ways the rule can see.

[P28] The same arithmetic applies to three other things a firm holds, and it is worth going through them because the first is the one people already watch and the other two are usually watched by nobody. Customer concentration is the familiar one, and it has the same trap: a firm with twenty customers is not diversified if all twenty are venture-funded companies in one sector, because a funding winter cancels twenty contracts on the same afternoon for one reason.

[P29] Funding concentration is the second, and it is what the first segment was about. A firm with four hundred depositors has four hundred names and, if those depositors were acquired through one channel, operate in one industry, and talk to each other, it has an effective count in the low single figures. The same is true of a firm with eight lenders who all use the same rating agency, or a firm with fifteen investors who all sit on each other's boards.

[P30] Supplier concentration is the third and it is usually invisible because it hides one layer down. A firm may buy from six vendors and feel comfortable, when all six assemble the same component from one manufacturer. The firm's own records show six relationships. The exposure is one, and the firm cannot see it from its own purchase orders because the shared dependency is in its suppliers' supply chains rather than in its own.

[P31] The fourth is key-person concentration, which resists measurement most stubbornly because the exposure is not denominated in money. If one individual holds the fundraising relationships, the principal counterparty relationships, and the public identity of the firm, then those are not three separate dependencies. They are one dependency that will fail as a unit, on a day when that person leaves or is discredited, and every one of the three will fail at once because they were the same person all along.

[P32] There is a version of this that is worse than any of the above, and it is the version where the firm manufactures the correlation itself as a by-product of doing something sensible. Consider a lender that wins deposits by offering them to the borrowers it lends to, keeping the operating account where the credit line is. Commercially this is excellent. The deposits are cheap, the relationship is deep, and the cross-selling ratio is a metric somebody is rewarded for.

[P33] But look at what it has built. Every depositor is also a borrower, in one industry, in one city, reachable through the relationship manager who is also their lender. The correlation between the funding base and the loan book is not a market accident that the firm suffered. It was constructed deliberately, one profitable relationship at a time, and each individual decision improved the numbers. Concentration of this kind is generally the residue of a successful strategy, which is why it is defended rather than found.

[P34] Now the reason this is hard to catch in practice, and it is the same reason the deposit models failed in the previous segment. Correlation is not observed, it is estimated, and it is estimated from history. In a calm period the borrowers do not move together much, because nothing is happening to move them, so the measured correlation is low. The estimate is not wrong. It is an accurate description of a period in which the exposure was not being tested.

[P35] Correlation then rises in stress, and it rises because the mechanism that links the borrowers only operates under stress. In an ordinary year the fact that four hundred borrowers share a city is irrelevant, and their outcomes genuinely do look independent. In the year the local economy turns, the shared city becomes the only thing that matters and the correlation goes from zero point zero five to something far higher. The parameter is not stable, and it is at its lowest exactly when you are deciding whether to worry.

[P36] So the measurement is most reassuring when it is least reliable, which is the same sentence I used about deposit behaviour, and the repetition is the point. Both quantities are estimated from a calm past, both are functions of conditions rather than constants, and both revert to their dangerous values on the same day for the same reason. This is what makes these failures feel sudden from inside a firm that was measuring diligently.

[P37] Three things follow for practice, and the first is to stop estimating correlation and start naming the cause. Rather than fitting a number to a quiet history, list what the exposures have in common: the region, the sector, the tenant, the rate, the refinancing market, the currency. Each item on that list is a factor, and the useful question about a book is how much of it sits on each factor. That question can be answered from records the firm already holds, and it does not degrade in calm periods the way an estimate does.

[P38] The second is to stress by scenario instead of by name. A limit framework that caps each borrower answers the question of what happens if one borrower fails. Nobody has ever been closed by one borrower failing. Ask instead what happens if the region turns, if the dominant employer leaves, if the currency moves fifteen per cent, and read off how much of the book is affected in each case. The output is a small number of large exposures rather than a large number of small ones, which is a truer description and a shorter document.

[P39] The third is to set limits on the factors rather than on the counterparties, and this is the one that meets resistance, because a factor limit binds when the business is going well. A limit on exposure to one city constrains the relationship manager who is best at that city. A limit on borrowers funded by one lending market constrains the product that is easiest to sell. Concentration accumulates through success, so any control that works has to bite during the good period, and a control that only binds in a bad period is a description of what has already happened.

[P40] Something to work through. Ashgrove Bank holds three hundred and twenty commercial loans, none larger than half a per cent of the book, in eleven different sectors across one metropolitan area. It is funded by eighteen thousand retail depositors in the same area, of whom the largest holds a hundredth of a per cent of the deposit base. Both sides score superbly on any size-based concentration measure. Tell me what Ashgrove's actual exposure is.

[P41] Ashgrove has one exposure, which is that metropolitan area, and it holds it twice. The eleven sectors are not eleven independent bets if the region has a dominant employer, because eleven sectors serving one payroll are one bet. And the funding is the same bet again: the depositors are the employees and suppliers of the borrowers, so a regional downturn impairs the loan book and withdraws the deposits together, which is precisely the pairing that closed the lender in the first segment. Ashgrove is a leveraged position on one local economy, financed by the same local economy, and no measure in its risk pack contains the word region.

[P42] A shorter one. Brindle Capital lends to forty borrowers in nine countries on four continents, with no sector representing more than fifteen per cent. Its risk committee treats it as thoroughly diversified. Name the one question worth asking, and the answer that would worry you. The question is what currency the loans are denominated in and where the borrowers earn their income. If forty borrowers across nine countries all borrowed in dollars and earn in local currency, then geography has bought nothing, because a strengthening dollar raises the debt burden of all forty at once. Forty names, four continents, one exposure.

[P43] The next segment is about what happens once an exposure like that begins to move, and specifically about why the parties involved act in a way that is individually correct and collectively fatal. A run is not a panic and it is not irrationality, and treating it as either one is what prevents firms from planning for it.
