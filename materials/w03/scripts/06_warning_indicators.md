---
title: Warning indicators
series: business-of-data
week: 3
module: Liquidity, duration, concentration
section: 6
target_seconds: 600
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Many will recognise the escalation problem from their own organisations."
method_note: >
  The contrasting pair is drawn from inside the firm rather than between two firms:
  the same indicator, on the same report, read by two people with different authority.
  The misconception is the phrase nobody saw it coming, which is attacked on the
  evidence that somebody almost always did. The segment then separates the
  informational problem from the organisational one, argues the second is the binding
  constraint, and closes the module on the one intervention that survives contact with
  the incentive structure, which is a trigger agreed in advance.
constraint: "Must not reference the week's case. Running example is commercial property lending."
numbers: "Figures reused from w03-numbers.py, output in w03-numbers.txt."
status: draft 2026-09-09
---

## Script

[P1] I want to start inside a single firm rather than with two of them. In the March of the year before it failed, a treasury analyst at Selby Trust produced a monthly funding report containing a line item showing that the four hundred largest depositors accounted for eighty-one per cent of deposits, up from sixty-four per cent two years earlier. The report went to the finance director and to the risk committee. Nobody disputed the number. Nobody acted on it. It appeared again, with a larger figure, every month for eleven months.

[P2] So when this firm failed, the sentence used afterwards was that nobody saw it coming. That sentence was false, and I would like to spend this segment on why it gets said anyway, because it is said after nearly every failure of this kind and the record nearly always contains the warning. The analyst saw it, wrote it down, and distributed it monthly to the people with the authority to change it.

[P3] The natural reading of that is that the recipients were negligent, and I want to set that reading aside, not out of charity but because it is unhelpful. The recipients were reading twenty other indicators in the same pack, most of which were fine. They had been told about this one for eleven months and nothing had happened in any of them. And acting on it meant giving up profitable business today against a loss that might never occur. Under those conditions inaction is the expected behaviour of competent people, which means the problem has to be fixed structurally rather than by asking for more diligence.

[P4] Let me lay out what is actually observable in advance, because the list is shorter than people expect and every item on it comes from the earlier segments. The first is funding concentration, which is the Selby number: what share of the funding comes from parties who would act together, measured by common cause rather than by name count. The second is the share of funding that is uninsured, because insured depositors have no reason to run and uninsured ones have every reason.

[P5] The third is the duration gap, the difference between how long the assets take to return cash and how long the funding is contracted for. The fourth is the unrealised loss sitting inside the portfolio that is carried at cost rather than at market, which is disclosed in a note rather than in the accounts, and which tells you what the equity would be if the firm ever had to sell. Those two together tell you how much of the reported capital is a function of where rates happen to be.

[P6] The fifth is the deposit beta assumption, and it is the one nobody outside the firm can see. Somewhere there is a model asserting that the deposits behave as though they were four-year money, and that assertion is doing more work in the firm's stated position than any other single number. Whether it was estimated on a period containing a genuine alternative for the depositor is the question, and it is answerable in an afternoon by whoever owns the model.

[P7] The sixth is the growth rate of the balance sheet relative to comparable firms, and it deserves separate treatment because it is the most informative and the least welcome. A lender growing at three times the rate of its peers is winning business for a reason, and there are only two reasons available: it is genuinely better at something, or it is charging too little for risk that the others are pricing correctly. Both look identical from inside during the growth period, and both produce the same rising revenue chart.

[P8] The discriminating question is what the firm would say it is better at, in one sentence, without using the word relationship. If there is a real answer, such as an underwriting method or a cost structure the others cannot copy, then the growth is earned. If the answer is that the firm is faster, more flexible, or easier to deal with, then it is being paid for taking risk the others declined, and the volume is the risk rather than the reward. That question can be asked at any board meeting and takes about a minute.

[P9] Notice that every one of those six is available internally, most of them monthly, and three of them are available to an outsider from published disclosure. This is the point I want to make hardest in this segment. These failures are not usually information failures. The information exists, in the building, on a schedule, in a document with named recipients. What fails is the conversion of information into action, and that is a problem about authority rather than about measurement.

[P10] Consider who holds each half. The analyst holds the observation and has no authority to reduce the exposure. The relationship managers could reduce it, by declining the deposits and the loans that create it, and are compensated for increasing it. The finance director could direct them and would have to explain a fall in revenue. The board could instruct the finance director and sees the number once a quarter alongside twenty others, in a pack of two hundred pages, having no independent means of knowing which of the twenty is the live one.

[P11] Authority to act therefore increases as you go up, and specificity of knowledge decreases, and the two curves cross somewhere in the middle where nobody holds enough of either. That is not a flaw in one firm's design. It is the ordinary shape of an organisation, and it means that any control which depends on the right person noticing at the right moment will fail eventually, because the right person is a different person for each half of the task.

[P12] There is a second problem stacked on top, which is what happens to somebody who raises a warning that is not yet correct. A warning about a run is a statement that something may happen and probably will not this year. If they escalate and nothing occurs, which is the likely outcome, they were wrong in a visible way and they cost the firm revenue. If they say nothing and nothing occurs, which is also likely, they were right. If they say nothing and it happens, the failure is collective and the cost to them individually is small.

[P13] So the payoffs facing the person best placed to raise the alarm point away from raising it, in three cases out of four. That is the same structure as the previous segment, where each depositor's individually correct decision produced a collectively fatal outcome, and it should be read the same way: not as cowardice, but as a payoff matrix that will produce silence from competent people until the matrix is changed.

[P14] Which is why the intervention that works has to be decided before it is needed, and has to remove the judgment from the moment. The mechanism is a trigger agreed in advance. The firm states, in the calm period, that if funding concentration passes a stated level, or the duration gap exceeds a stated number of years, then a specified action follows automatically. Not a review, not an escalation, an action: term funding is issued, the swap is put on, the deposit gathering stops.

[P15] The value of pre-committing is that it moves the argument to a time when nobody knows who will lose by it. Agreeing in March that the firm will stop taking a category of deposit at a stated threshold is an abstract discussion about a policy. Agreeing to it in October, when the threshold has been passed and everyone can see which desk will lose the business, is a negotiation between people with known interests, and it is a negotiation the desk with the revenue usually wins.

[P16] The second mechanism worth having is the pre-mortem, which is an exercise done in one meeting. The instruction is to assume the firm has failed eighteen months from now and to write down how it happened, in specific terms, naming the exposure. The framing matters more than it sounds: asking a group what might go wrong produces a polite list, and asking them to explain a failure that has already occurred produces the thing people have been privately worried about, because it is no longer a prediction anybody can be wrong about.

[P17] Something to work, from the outside this time, because most of you will be reading these firms rather than running them. Linfield Group's published accounts show deposits up thirty-one per cent in a year against a sector average of four, a securities portfolio classified almost entirely as held to maturity, a note disclosing unrealised losses on that portfolio equal to a hundred and ten per cent of reported equity, and a statement that ninety-two per cent of deposits are above the insured limit. Rank those four and say what you would ask.

[P18] The unrealised loss and the insured share are the pair that matters, and they matter because of what they do together rather than separately. The loss note says the reported equity is a bookkeeping consequence of not having sold, and would be gone if the firm ever sold. The insured share says almost every depositor has a reason to be early. So the firm is one forced sale away from insolvency, and its funding base is composed of exactly the parties who will move first. The growth rate explains how it got there and the classification explains why nothing appears in the headline numbers.

[P19] The question worth asking is the beta question from earlier: what behavioural life the firm assigns its deposits and over what period that was estimated. Everything else on the list is disclosed. That one is not, it is doing more work than any of the disclosed items, and it is answerable in a sentence by anyone in the treasury function. An analyst who asks it and gets a vague answer has learned more than the accounts contain.

[P20] Both mechanisms address the same target. Neither improves the measurement, because the measurement was adequate. What they do is remove the requirement for an individual to act against their own interest at a moment of uncertainty, which is the step that reliably fails, and replace it with a decision taken earlier by people who did not yet know how it would land on them.

[P21] That closes the module. A firm can be worth more than it owes and fail, because the obligations are dated and the assets are not liquid on those dates. The gap between the two is measurable and is usually not measured. Exposures that appear spread across hundreds of parties can behave as though there were four. The parties who withdraw are behaving correctly rather than badly. And the warning almost always existed, in writing, in the building, addressed to somebody who had a good reason not to act on it.
