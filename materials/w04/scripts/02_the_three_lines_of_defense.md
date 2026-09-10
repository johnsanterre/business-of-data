---
title: The three lines of defense
series: business-of-data
week: 4
module: Model risk management
section: 2
target_seconds: 1200
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Many work inside a structure like this and have never seen it named."
method_note: >
  Contrasting cases: two firms with identical structures on the organisation chart
  and different reporting lines, where the difference is invisible in every document
  either one publishes. Each line is then built from what it is for rather than what
  it does, so the learner can derive why a third line is necessary before being told.
  Closes on the four tests that distinguish a real structure from a drawn one, which
  is the tool students take into the case.
constraint: "Must not reference the week's case. Running example is aviation software certification."
status: draft 2026-09-09
---

## Script

[P1] Two firms, both with a risk function, both with internal audit, both with the same three boxes on the same organisation chart. If you read their published governance documents side by side you could not tell them apart, and the documents would be accurate in both cases.

[P2] At the first firm, the head of model risk reports to the chief risk officer, who reports to the chief executive and has a private session with the board audit committee at every meeting with no executives present. Their budget is set at group level. Their team's promotions are decided inside the risk function.

[P3] At the second firm, the head of model risk reports to the chief operating officer of the division that builds the models. Their budget is a line in that division's cost base. Their team's next career step is a business-facing role in the same division, and the person who approves that move is the person whose models they are reviewing.

[P4] Those two firms have the same structure and are not the same institution. Everything in this segment is about the difference, and the difference does not appear in any document either firm produces.

[P5] Start with why a structure exists here at all, because the reasoning generalises well beyond models. A business unit is under pressure to produce a result. It has better information about its own activity than anybody else does. And it has an interest in a particular answer. Those three facts together mean that self-assessment is unreliable in a specific direction, and the unreliability is systematic rather than random.

[P6] The standard response is to separate the doing from the checking. That is the whole idea, and everything else is detail about how to make the separation survive contact with a real organisation, where the checker and the doer eat in the same canteen and their bonuses come out of the same pool.

[P7] The first line is the business. In model terms, it is the people who develop the model, the people who implement it in production, and the people who use its output to make decisions. All three are the first line, which surprises people who assume the first line means the developers.

[P8] The first line owns the risk. That phrasing is deliberate and it is not a euphemism. The people running the business are accountable for the models they use, which means the failure of a model is their failure and not the risk function's. A firm where the business believes model risk belongs to the model risk department has already lost, because the first line is the only party with enough contact to notice most problems.

[P9] What the first line actually owes is specific. Develop the model soundly and document how. Test it before it goes live. Monitor it while it runs. Report when it drifts. Use it only for what it was built for. Every one of those is a first-line obligation, and none of them is discharged by sending the model to validation.

[P10] The first line is measured on business results, on time to market, and on the quality of what it ships. Notice that only the third of those points toward doing this work, and that the third is the hardest to measure and the slowest to appear. A team under schedule pressure will do the parts of the list that are checked and defer the parts that are not.

[P11] The second line is the oversight function. In model terms this is model risk management: a group that sets the standards the first line must meet, decides what those standards require for a given model, performs or oversees validation, and maintains the inventory.

[P12] The essential feature is that the second line does not report through the first. That is the whole of its independence and it is a structural property rather than a cultural one. A second line reporting into the business it oversees is a first-line quality function with a different name, and everybody in the building understands which it is regardless of the diagram.

[P13] What the second line owes is standards, challenge, and a record. Standards means writing down what is required, by model tier, so that requirements are known in advance rather than negotiated per model. Challenge means asking the questions the first line has an incentive not to ask itself. And the record means that a decision to accept a limitation is documented, with a name against it.

[P14] That last one carries more weight than students expect. Much of what a second line produces is not a prohibition but a documented acceptance. The model has this weakness, here is the compensating control, here is who accepted it, here is the date it will be revisited. Six of those accumulate into a picture of the firm's actual exposure that exists nowhere else.

[P15] The second line is measured on whether losses occurred, on audit findings against it, and on regulatory outcomes. All three are lagging, all three are about absence, and none of them rewards being right early. We saw the same incentive shape in the first week and it is worth recognising again here, because it explains why second lines drift toward process compliance: process compliance is the only part of their work that is legible in the short run.

[P16] There is a second thing the second line owes that is easy to miss, which is consistency across the firm. Two teams building similar models should face the same requirements, and without a central function they will not, because each will negotiate its own. Consistency sounds bureaucratic and it is what makes the standards enforceable: a requirement that was waived for one team is not a requirement.

[P17] It also produces the only firm-wide view of model risk that exists anywhere. Each business knows its own models. Only the second line can say that four separate systems in three divisions all depend on the same vendor feed, or all assume a relationship that held for a decade and stopped holding last year. That aggregation is a large part of the value and it is invisible to everybody who supplies the inputs to it.

[P18] Now the question that makes the structure interesting. Something has to check the second line, because the second line has its own reporting destination and its own interest in a quiet year.

[P19] The answer is the third line, internal audit, and its subject matter is not the risk. Internal audit does not revalidate the models. It examines whether the second line is doing its job: whether the standards exist, whether they are applied consistently, whether the inventory is complete, whether findings are closed rather than aged, and whether validation is reaching conclusions or producing paperwork.

[P20] The structural feature that makes the third line possible is that it reports to the board rather than to management. That is the entire basis of its independence, and it is why the reporting line is worth checking first in any firm you are assessing. A third line reporting to the chief executive can examine everything except the thing most likely to matter.

[P21] So the shape of the whole arrangement is three separations, each one addressing the fact that the layer below reports to somebody with a reason to want a particular answer. The business reports to people who want the result. The second line, if it reports into the business, wants what the business wants. And the third line, if it reports to management, wants what management wants. Each line exists because of a conflict in the one below.

[P22] It is worth being explicit that this is not a hierarchy of seniority. The third line is not senior to the second, and the second does not manage the first. They are three different jobs with three different reporting destinations, and treating them as a chain of command is the most common misreading. A second line that behaves as though it outranks the business will be resisted, and it is not entitled to give instructions. It is entitled to set standards and to report the truth about whether they were met.

[P23] The distinction matters for what an escalation looks like. When the second line and the business disagree, the second line does not overrule. It documents the disagreement, states its assessment, and sends both to whoever holds the decision, which is usually a committee with the authority to accept the risk. The decision to proceed over an objection is legitimate and it is supposed to leave a trace with a name on it.

[P24] That trace is the thing worth looking for in every case this term. When something has gone wrong, the question is rarely whether anybody objected. It is whether the objection was recorded, who accepted it, and whether that person understood what they were accepting. A firm where objections are resolved in conversation has no trace, and the absence is usually reported afterwards as nobody having raised a concern.

[P25] The aviation parallel maps closely and it will help you hold this. The manufacturer designs the system and is the first line: it is responsible for the aircraft being safe, and no certification process relieves it of that. The regulator is the outside check. And because the regulator cannot examine everything itself, a portion of its work is delegated to designated engineers, who are employed by the manufacturer and act on the regulator's behalf for specific determinations.

[P26] Sit with that last arrangement for a moment, because it is the second line problem in its sharpest form. The person making the determination is paid by the party being examined, works in that party's building, and their career progresses inside that party. The response has been to specify the appointment, the reporting obligation, and the protections around it in exhaustive detail. Whether that is sufficient is a live argument in that industry and has been for years.

[P27] The reason to bring it up here is that the structure of the problem is identical and the stakes make it easier to see. Nobody in aviation believes that writing independent on a diagram makes somebody independent. The question is always what specifically prevents the examined party from influencing the examiner, and the answer has to be a list of mechanisms rather than an assurance.

[P28] So let me give you the four mechanisms, because they are the practical test and you should apply them to every firm in this course.

[P29] First, the reporting line. Trace who this person's manager reports to, and whether that chain reaches the business being overseen before it reaches the top. If it does, everything downstream is weaker than it appears. This is the single most informative fact and it takes one question to obtain.

[P30] Second, compensation. Establish whose results determine the size of this person's bonus pool. If the answer is the division whose models they review, then the reviewer is paid more when the models are approved faster, and that is true regardless of anybody's integrity.

[P31] Third, career path. Find out where somebody in this function goes next. If the standard next step is a business role in the unit they oversee, then every review is conducted by somebody applying for a job with the person being reviewed. Firms rarely think of this as a control and it is one of the strongest.

[P32] Fourth, and the one that settles it, consequence. Establish what happens when this function says no. Not what the policy says. What happened the last three times. If a negative finding was overruled by somebody senior and the reviewer remained in post with reduced standing, the firm has communicated the real rule to everybody watching, and there were people watching.

[P33] Those four are the difference between the two firms I opened with, and none of them appears in a governance document. That asymmetry is worth naming: the things that determine whether a control works are almost entirely absent from the documents that describe the control.

[P34] Before the failure modes, one more mechanism that firms use and that is worth understanding because it is the cheapest of the four to implement. It is the private session. Once a quarter the audit committee meets the head of internal audit with no executives in the room, and asks whether there is anything they should know. It sounds like theatre and it is the single channel through which a board hears something management would prefer it did not.

[P35] The equivalent for the second line is rarer and it is a strong signal when present. A chief risk officer with a standing right of access to the board, exercisable without the chief executive's agreement, has a form of protection that no reporting line alone provides. Ask whether it exists and whether it has ever been used, and note that the second answer is usually the more informative one.

[P36] Now the failure modes, of which there are three worth knowing and they are distinct.

[P37] The first is the collapsed line, where two of the three are effectively the same group. The most common version is a second line staffed by people who transferred from the first line, in the same division, reporting through it. They know the models well, which is genuinely valuable, and they are not independent, which is the point of the role. The firm gets competent review and loses challenge, and from outside it looks fine because the reports are technically excellent.

[P38] The second is the overloaded line, where the structure is right and the staffing is not. A second line with four people and nine hundred models in the inventory will produce a validation calendar in which most models are reviewed rarely and the review is shallow. Nothing in the governance documents is false. The function exists, has independence, applies standards, and cannot possibly do the work.

[P39] The overloaded case has a signature you can look for. Ask how many models are overdue for their scheduled review, and how long the oldest overdue item has been waiting. Firms track this and rarely publish it, and it is the fastest way to distinguish a functioning second line from a nominal one.

[P40] The third is the ceremonial line, where every step happens and none of it can change anything. Validation is performed, findings are raised, findings are logged, findings are accepted by the business, and the model ships on the original date. The paperwork is complete and the process has no coupling to the outcome. This is the most dangerous of the three because it produces the strongest evidence of diligence.

[P41] A concrete version helps here. A validation report lands three weeks before a launch date and raises two findings. The first is that the model has not been tested on the segment that will account for a third of its volume. The second is that the monitoring plan has no threshold at which anybody is required to act.

[P42] The business accepts both, notes that the segment will be monitored closely after launch, and ships on the date. Every step in that sentence is permitted. Validation was independent, the findings were real and were raised, and an accountable executive accepted them in writing. The model goes live untested on a third of its volume with no defined trigger for intervention.

[P43] What made that outcome available was the date. Three weeks was not enough time to test the segment, so the only options on the table were accept or slip, and slipping was not on the table because it had been decided months earlier by somebody who was not in this meeting. The validation was scheduled to conclude at a point where its findings could not change anything, and that scheduling decision was the real control failure.

[P44] Which gives you a question worth asking of any process, and it generalises well beyond models. Ask when the independent review concludes relative to the point of no return. If the review finishes after the date is fixed, the resources committed, and the announcement drafted, then the review can describe problems and cannot prevent them, whatever authority it nominally holds.

[P45] There is a specific artefact worth learning to read here, which is the finding register. Every second line maintains one. What matters is not how many findings it contains but the distribution of their ages and how they were closed. Findings closed by remediation are one thing. Findings closed by acceptance are another, and a register dominated by acceptances is a function that documents rather than one that changes anything.

[P46] Now a caution in the other direction, because I have been describing what goes wrong and there is a failure of excess. A second line that blocks everything is not safe, it is bypassed. Teams route around a function that says no reflexively, by not registering things, by calling them experiments, by keeping them in a notebook. The function's authority is spent every time it is used, and a second line with no sense of proportion loses the ability to stop the thing that actually matters.

[P47] That is why tiering exists and why it is more than administrative convenience. Models are ranked by consequence, and the requirements attach to the tier. A high-tier model gets full independent validation before deployment and an annual cycle. A low-tier model gets a lighter review and a longer interval. The function preserves its capacity, and its objections stay expensive enough to be taken seriously.

[P48] One more point about the first line, which is the one most often neglected in these discussions. Everything above concerns whether the checking works. The largest determinant of model risk is not the quality of the checking. It is whether the people who build and use models understand that they own the outcome.

[P49] A first line that believes validation is a hurdle to clear will build to the hurdle. A first line that believes the model is theirs, and that its failure is their failure, will find most of the problems itself, before anybody external looks, because they are the only people close enough to see the small things that precede a large one. No amount of second line quality compensates for the absence of that.

[P50] So the summary of the segment is that the structure is necessary and is not sufficient, that its effectiveness is determined by four things that appear in no published document, and that its three failure modes each produce paperwork indistinguishable from success.

[P51] The next segment goes inside the second line's central activity, which is independent validation. What it actually examines, what independence requires in practice, and why a validator who cannot reach an unwelcome conclusion is performing a review rather than a validation.
