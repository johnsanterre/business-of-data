---
title: How a release happens
series: business-of-data
week: 1
module: Introduction
section: 6
target_seconds: 600
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Many have shipped things; few have watched the buyer's side."
method_note: >
  The segment follows one release end to end rather than listing gates, and asks the
  same three questions at each: who signs off, who can stop it, and who finds out
  afterwards. The buyer's parallel sequence is given equal weight because half the
  cases turn on somebody's procurement process and students consistently underrate
  it. Lands on the observation that the person accountable for the date has authority
  over nobody, which reframes every launch argument in the course.
constraint: "No case is used this week. This module is the map of the other twelve."
status: draft 2026-09-09
---

## Script

[P1] A capability becomes a product by passing through a sequence of gates. I want to walk one release through them, and at each gate ask three questions: who signs off, who can stop it, and who only finds out afterwards. Those three answers are rarely the same person, and the gap between them is where most of what we study happens.

[P2] The first gate is internal evaluation. A team has something that works and needs to establish how well, against what, and compared to what. This is the gate that looks most like science and is the most quietly political of all of them, because the evaluation set is chosen by the team being evaluated.

[P3] That is not an accusation. Somebody has to choose, and the people who understand the capability best are the people who built it. But a benchmark is a claim about which failures matter, and a team choosing its own benchmark is choosing which of its failures will be visible. A model can be excellent on the chosen set and unusable for the population it will actually serve, and nothing at this gate will surface that.

[P4] Who signs off is the team's own leadership. Who can stop it is nobody, at this stage, because nothing has been proposed yet. Who finds out afterwards is everybody downstream, and they receive the evaluation as a fact rather than as a choice.

[P5] The second gate is adversarial testing, usually called red teaming. People whose job is to make the system behave badly try to, and what they find gets triaged into things that must be fixed and things that will be accepted.

[P6] The triage is the interesting part, and it is where the word acceptable does a great deal of work. A finding is accepted when somebody decides the residual risk is tolerable, and that decision needs a named owner and frequently does not have one. Findings accumulate in a document, the document is reviewed, and the review consists of the team agreeing with itself unless somebody outside it has standing to object.

[P7] Who signs off varies enormously between firms, which is itself informative. Who can stop it is trust and safety or risk, if either of them has been given that authority, and often neither has. Who finds out afterwards is the customer.

[P8] Third gate, legal review. What is in the training data, what the licence permits, what the product may claim about itself, and what the firm is promising its customers if something goes wrong. That last one is indemnification and it is a bigger commercial issue than most technical people realise, because enterprise buyers increasingly require the seller to carry the legal risk of the output.

[P9] Who signs off is the general counsel's office. Who can stop it is the same office, and it genuinely can, which makes this one of the few gates with real teeth. Who finds out afterwards is usually the engineering team, when a constraint arrives late and is expensive to implement.

[P10] Fourth, the pricing decision. What it costs, on what basis, and what the floor is below which a deal needs approval. We covered why this is hard in the money segment: the cost of serving is falling underneath you, and the buyer wants a predictable annual number that has nothing to do with usage.

[P11] Who signs off is finance and the pricing function together. Who can stop it is nobody, in the sense that a product does not fail to launch over pricing, it launches at the wrong price. Who finds out afterwards is the sales organisation, which will spend a year explaining why the price is wrong.

[P12] Fifth, the launch date. Somebody chooses a day. That choice is made against a conference, a competitor's expected announcement, a quarter end, or an executive's calendar, and it is frequently the single most consequential decision in the whole sequence because every other gate is then measured against it.

[P13] I want to be precise about the mechanism here. Once a date exists, the question at each remaining gate silently changes. It stops being whether this is ready and becomes whether this can be finished by the date. Those are different questions and they have different answers, and nobody announces the substitution.

[P14] Sixth, the communications plan. What is said, what is claimed, what is disclosed about limitations, and what the response is if something goes wrong in the first week. This is also where the firm decides what it will call the thing, and the name is a substantive decision rather than a marketing one, because it sets what users expect the system to do.

[P15] Now the line that I would like you to carry out of this segment, because it explains behaviour that otherwise looks irrational. The person responsible for the launch, usually a product manager, owns the date and has authority over nobody. Every function I have just described can slow the release. The person accountable for it can only ask.

[P16] Sit with that for a moment. It means the coordination is achieved through persuasion and favour-trading rather than through instruction, and it means the person who will be blamed if the date slips cannot compel any of the people who might cause it to slip. That is not a badly designed company. It is nearly every company, and it is why release decisions look like negotiations rather than plans.

[P17] Now the other side, because half the cases in this course turn on somebody's procurement process and technical people consistently underrate how long it takes and how many people can say no.

[P18] The buyer starts with a pilot, which is a small deployment with a friendly team inside the buying organisation. The pilot almost always succeeds, and its success is nearly uninformative, because it was run by enthusiasts on a use case they chose.

[P19] Then security review. The buyer's security function examines where the data goes, who can see it, what is retained, and what happens in the event of a breach. This is a genuine gate with a genuine veto, and answering it well requires documentation that the selling firm may not have written yet.

[P20] Then the buyer's legal review, which is where the indemnification question from earlier arrives with force. The buyer wants the seller to be liable if the output causes harm. The seller wants to disclaim that entirely. Nobody gets what they want, the negotiation takes weeks, and the outcome is a clause that determines the economics of the deal more than the price does.

[P21] Then procurement, which is a separate function from anybody who wants the product, and whose job is to reduce the price and standardise the terms. Procurement is not evaluating whether the product is good. It is comparing your paper to somebody else's paper and asking why yours costs more.

[P22] Then deployment, integration with systems the seller has never seen, training for people who did not ask for this, and a period in which the product is technically live and nobody is using it.

[P23] End to end, nine months is normal. Understand what that means for a seller: the revenue from a product launched today arrives in the third quarter of next year, and the cost of serving it will have moved by a third or more by then. Every one of those steps can also kill the deal, and the people who can kill it are mostly not the people who wanted it.

[P24] There is a step I left out of the buyer's sequence because it deserves its own mention, which is the internal business case. Somebody inside the buying organisation has to justify the spend to their own finance function, in the buyer's own language, against the buyer's own hurdle rate. That document is written by a champion whose expertise is their own organisation rather than your product, using numbers you supplied, and it will be read by people who have never spoken to you.

[P25] So a substantial part of whether a deal closes depends on a document you cannot see, written by somebody you have limited access to, defending an assumption they got from your sales team. The single highest-leverage thing a seller does is make that document easy to write, and most sellers spend their effort on the demonstration instead, which is the part that was never in doubt.

[P26] The other omission is the incumbent. Almost nothing is bought into an empty space. There is a system already doing some version of the job, with people whose expertise is in operating it and whose standing derives from that expertise. Replacing it is not only a purchase, it is a redistribution of competence inside the buyer, and the people who lose by it are frequently on the evaluation committee.

[P27] One asymmetry is worth naming before we finish. On the selling side, most of the gates can be softened by a sufficiently senior person who wants the date met. On the buying side, they cannot, because the security reviewer and the procurement officer do not work for anybody who wants your product. Enthusiasm inside the buyer does not accelerate the parts of the process that take the longest.

[P28] The last segment of this module takes the three shapes that business failure comes in, with examples from outside this industry, so you can see the pattern without the technology getting in the way.
