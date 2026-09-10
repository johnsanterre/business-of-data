---
title: How the regime fails
series: business-of-data
week: 4
module: Model risk management
section: 6
target_seconds: 600
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. This is the segment they should be able to apply to their own employer."
method_note: >
  The two failure modes are given equal weight and the second is argued to be worse,
  against the intuition that an absent control is the more dangerous one. The
  argument is that a documented control produces evidence of diligence, which
  displaces the scrutiny that an obvious absence would attract. Closes with the six
  questions, which is the deliverable of the whole module.
constraint: "Must not reference the week's case. Running example is aviation software certification."
status: draft 2026-09-09
---

## Script

[P1] Everything in this module describes a regime that works. It has been refined over decades, it is enforced by supervisors who arrive in person, and firms operating under it still fail in ways it was designed to prevent. So the last segment is about how, and there are two shapes.

[P2] The first is that the role sits empty. There is no model risk function, or there is one person with a title and no team, or the function exists in one division and not in the three others that also deploy models. The regime is absent, and its absence is visible to anybody who looks.

[P3] This version is bad and it is honest. A firm with no validation function has not claimed to have one. A supervisor examining it finds nothing, which is a finding. The gap is detectable in an afternoon by asking for the inventory and receiving a blank look.

[P4] It occurs for ordinary reasons rather than through negligence. A firm grows past the point where informal oversight works and does not notice, because there is no day on which informality stops being adequate. Or a firm expands into an activity its framework was not built for, and the framework covers the old business thoroughly while the new one operates outside it. Or the function was cut in a cost programme two years ago and nobody has raised it since.

[P5] The second shape is that the role is occupied by somebody with no authority to stop anything, and I want to argue that this is worse. That is counterintuitive, because a control that exists must be better than one that does not.

[P6] Here is the argument. An absent control produces an obvious gap that attracts attention. A present but powerless control produces documents. Validation reports, a populated inventory, committee minutes, a finding register. Every one is genuine. And their existence answers the question that would otherwise have been asked, which is whether anybody is checking.

[P7] So the powerless control does not merely fail to prevent the failure. It displaces the scrutiny that the absence would have attracted, from the board, from a supervisor, from a customer's procurement process. The firm passes the diligence questionnaire because the answer to every question is yes, and every yes is true.

[P8] There is a second mechanism worth naming. A powerless control absorbs the concern of the people who might otherwise escalate. Somebody worried about a model raises it with validation, validation records it as a finding, the finding is accepted by the business, and the worried person has discharged their responsibility. The concern has been processed. Nothing has changed, and the person who saw the problem has been given a legitimate reason to stop pushing.

[P9] Now how a function ends up in that state, because nobody sets one up this way deliberately. It happens through four ordinary decisions, each defensible on its own day.

[P10] The reporting line. When the function was created, putting it inside the division seemed sensible: that is where the expertise sits and the alternative was a central team with no context. Nobody decided to compromise its independence, and it was compromised at the moment of creation.

[P11] The resourcing. The function is given four people. Four people cannot validate nine hundred models, so they triage, and the triage is reasonable and produces a firm where most models are reviewed rarely. Nobody decided to make validation shallow. The headcount decided it.

[P12] The timing. Validation is scheduled to conclude close to the launch, because scheduling it earlier means validating something that is still changing. Perfectly sensible, and it places the review after the point where its findings can change anything.

[P13] The precedent. Once, a finding was raised and the business overrode it and shipped, and nothing bad happened. That event taught everybody watching what a finding is worth, and it did not require a policy change to do so.

[P14] Notice that none of the four is a decision to weaken oversight. Each is a decision about organisational design, headcount, scheduling, or a single case. The function's powerlessness is the aggregate, and no meeting ever discussed the aggregate.

[P15] The aviation parallel is worth a last mention because that industry has had this argument publicly and at length. Delegating certification work to engineers employed by the manufacturer is efficient and it is the only way the regulator covers the workload. Whether the protections around those engineers are sufficient, in a company under commercial pressure with a schedule, is a question that has been asked repeatedly and answered differently at different times.

[P16] The reason to raise it here is not to draw a conclusion about aviation. It is that the argument in that industry is conducted at a level of specificity that model governance rarely reaches. Nobody there asks whether the reviewer is independent in general. They ask who appoints them, who can remove them, what they must report, to whom, and what happens if they are overruled. Those are the right questions and they are answerable.

[P17] There is one more thing worth taking from that industry, which is what it does after a failure. An investigation is conducted by a body that is separate from the regulator and from the manufacturer, it publishes, and the finding is a chain of contributing factors rather than a cause. The output is a set of recommendations addressed to named parties, and whether those were implemented is tracked publicly.

[P18] Almost none of that exists for model failures. An investigation is conducted internally, its output is privileged, the findings are shared with a regulator and not published, and the industry learns nothing. Every firm therefore encounters each failure mode for the first time, which is a large part of why the same failures recur.

[P19] The reason is not that anybody prefers ignorance. It is that the incentives run against publication, because a published account is an admission and an exhibit. So the sector that has the most data about how these systems fail is structurally prevented from sharing it, and that is worth holding on to when somebody argues that firms should be trusted to learn from experience.

[P20] So here are the six I would take into any firm, and they are the deliverable of this module.

[P21] One. How many models are in the inventory, and how many quantitative methods drive decisions here. If the second number is much larger, the scope is set by the goodwill of the people being overseen.

[P22] Two. Who does the head of model risk report to, and does that chain pass through a business before it reaches the top. This is one question and it is the most informative.

[P23] Three. When does validation conclude relative to the point of no return. If it finishes after the date is fixed and the resources committed, it can describe problems and cannot prevent them.

[P24] Four. In the finding register, what is the ratio of findings closed by remediation to findings closed by acceptance, and how old is the oldest open item. A register dominated by acceptances is a function that documents rather than one that changes anything.

[P25] Five. What happened the last three times this function said no. Not the policy. The events.

[P26] Six. For the most consequential model here, what is its documented purpose, and where would somebody using it encounter its limitations. If the answer is that the limitations are in a report in a repository, they are not enforced, they are remembered, and remembering is the part that fails.

[P27] Those six can be asked in twenty minutes and they will tell you more than a framework document runs to a hundred pages of. Ask them of your own employer this week, and be prepared for the answers to be worse than you expect, because they usually are and the people involved are usually competent.

[P28] One closing point, because I do not want the module to land as cynicism about oversight. The regime works. It is the reason a category of failure that used to be routine is now unusual in the institutions that operate under it properly. What fails is not the design.

[P29] What fails is the gap between having a control and the control having force, and that gap is made of reporting lines, headcount, schedules and precedent rather than of anybody's intentions. Which is good news, because those four are all things a firm can change deliberately, on a Tuesday, without anybody having to become a better person.

[P30] In the live session you will hold four roles inside a firm that had a model, had a process, and lost a great deal of money. Before you read the packet, decide which of the two shapes you expect to find, and then notice what you had to ignore to make the case fit it.
