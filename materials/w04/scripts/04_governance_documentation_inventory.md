---
title: Governance, documentation, inventory
series: business-of-data
week: 4
module: Model risk management
section: 4
target_seconds: 900
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. The least glamorous segment and the one that decides outcomes."
method_note: >
  Opens on the gap between a firm that has a framework and a firm that can answer a
  question, because the distinction is the whole segment. The inventory, the
  documentation and the change triggers are each built from the question they are
  meant to answer rather than from their contents. The aviation parallel supplies the
  configuration-control idea: that the certified artefact and the deployed artefact
  must be provably the same thing.
constraint: "Must not reference the week's case. Running example is aviation software certification."
status: draft 2026-09-09
---

## Script

[P1] A supervisor arrives at a firm and asks one question. How many models do you have, which of them affect regulatory capital, and when was each last validated. That is the whole examination, in the sense that everything else follows from whether the firm can answer it in an afternoon or in six weeks.

[P2] Most firms have a framework. The document exists, it is well written, and it describes standards, tiering, validation, and roles. Considerably fewer firms can answer the question. The gap between those two facts is what this segment is about, and it is the least glamorous material in the module and the part that most reliably determines outcomes.

[P3] Start with the inventory, which is the list of what the firm has deployed. It sounds administrative. It is the load-bearing artefact of the entire regime, because every other control operates on items that are in it and no control operates on items that are not.

[P4] A useful inventory record holds a small number of fields and each exists to answer a specific question. What is this model for, in a sentence that names the decision it drives. Who owns it, meaning a person rather than a team. What tier is it, meaning what would go wrong if it were wrong. When was it last validated and when is it next due. What does it depend on, upstream. And what depends on it, downstream.

[P5] That last pair is the one firms most often omit and it is the one that turns a list into something useful. A model that consumes a vendor data feed and feeds three downstream systems has a blast radius, and the inventory is the only place that can be recorded. When the vendor feed changes definition, somebody needs to know in an afternoon which models are affected, and without dependency fields that question takes a month of interviews.

[P6] The inventory has a characteristic failure and it is worth naming precisely. It is not that it is inaccurate. It is that it is stale in one direction. Things get added when a project registers them and they are removed rarely, and their attributes are updated almost never. So a mature inventory describes what the firm deployed rather than what the firm runs, and the difference accumulates quietly over years.

[P7] Which produces a specific diagnostic. Ask when each record was last confirmed rather than last updated. A field that has not been touched in four years is not stable, it is unexamined, and the difference matters because the world the model operates in has changed in four years whether or not the record has.

[P8] Now documentation, which is the second component, and I want to start with what it is for, because the usual answer is wrong. Documentation is not written for a supervisor and it is not written to demonstrate diligence. It is written for the person who has to make a decision about this model in three years, when everybody who built it has left.

[P9] That framing changes what goes in it. A document written for an examiner describes what was done. A document written for a successor describes what was decided and why, which is far more useful and much rarer, because the reasons for a choice feel obvious to the person making it and are the first thing lost.

[P10] So the contents follow. The purpose, meaning the decision the output drives. The design, meaning what method was chosen and what alternatives were considered and rejected. The assumptions, stated as claims that could be false rather than as background. The data, including what was excluded and why. The performance, including where it is weakest. And the limitations, meaning the conditions under which the estimates should not be relied on.

[P11] The assumptions section is the one that separates a real document from a produced one. An assumption written as a claim that could be false is testable and reads uncomfortably. The relationship between these variables is stable over time. Applicants who do not respond are similar to those who do. The population this model will serve resembles the population it was fitted on. Each of those can be checked, and each one written that way tells a successor where to look first.

[P12] The limitations section is the one that gets lost, and its loss is the mechanism behind a whole category of failure. A model is valid for a stated range and a stated population. That statement lives in a document. The model lives in a system. Somebody applying the model outside its range six months later never encounters the document, and the system returns a number of the same shape with no indication that anything is wrong.

[P13] The aviation parallel here is exact and it is instructive because that industry solved it. An aircraft's limitations are not held in the manufacturer's records. They are in the flight manual, in the cockpit, with the aircraft, and the crew is required to know them. The constraint travels with the artefact rather than with the organisation that produced it.

[P14] A firm that surfaces a model's valid range at the point of use has done the equivalent, and it is an engineering solution to what most firms treat as a training problem. If calling the model outside its documented range returns a warning rather than a number, the limitation is enforced rather than remembered, and remembering is the part that fails.

[P15] Now the third component, which is change control, and it rests on a single idea worth stating clearly. The thing that was validated and the thing that is running must be provably the same thing.

[P16] Aviation calls this configuration control and treats it with a seriousness that model governance rarely matches. An aircraft is certified in a specific configuration. Every subsequent modification has a process, a classification by significance, and a record. The question of whether the aircraft in front of you is the aircraft that was certified has a documented answer, and answering it is somebody's job.

[P17] For models the same question is frequently unanswerable. A model was validated. Since then, the training pipeline was refactored, a feature was added, a data source changed its schema, a threshold was tuned in response to a complaint, and the library was upgraded twice. Each change was small, each was reasonable, and nobody has asked in aggregate whether the validated artefact and the running artefact are still the same system.

[P18] So change control needs a threshold, and the threshold needs to be written before anybody is arguing about a specific change. Some modifications require revalidation, some require notification, and some require nothing. Deciding which is which in advance is what makes the rule usable, because deciding in the moment always produces the answer that the change is minor.

[P19] There are four triggers worth having explicitly, and you can ask any firm whether it has them. A material change to the model itself. A material change to its inputs, including a vendor changing a definition upstream. A change to how the output is used, which is the one most often missed because it involves no technical change at all. And a change in the environment, meaning the population or conditions have moved away from what the model was fitted on.

[P20] That third trigger deserves its own attention. A model validated to inform a human decision, later wired to take the decision automatically, is a different risk with an identical technical footprint. Nothing about the model changed. The consequence of it being wrong changed entirely, and no code review would surface it because there was no code change in the model.

[P21] The fourth trigger is the hardest because it requires somebody to notice an absence of change. A model quietly becomes less appropriate as the world drifts, and nothing announces it. That is what ongoing monitoring is for, and it is why a monitoring threshold with a defined action is the mechanism that connects the fourth trigger to anybody doing anything.

[P22] There is a second-order problem with all three components that is worth naming, which is that none of them is anybody's primary job. The inventory is maintained by somebody whose main work is something else. Documentation is written at the end of a project by people who have moved on to the next one. Change triggers are evaluated by a team under a deadline. Every one of these is a task that competes with delivery and loses.

[P23] Which suggests the only reliable fix, and it is unglamorous. The machinery has to be wired into work that people are already doing rather than added alongside it. An inventory that updates when a deployment pipeline runs is maintained. An inventory that requires a form is stale within a year, and no amount of reminding changes that.

[P24] Now governance in the narrow sense, which is who decides. Every firm has committees and the interesting question is not their names but three properties.

[P25] Establish what this body can actually decide. A committee that reviews and recommends is a meeting. A committee that approves, and whose approval is required before something goes live, is a control. The distinction is knowable from the terms of reference and is frequently different in practice, which is why the better question is what it has actually stopped.

[P26] Who sits on it, and specifically whether the second line has a vote or an audience. A risk function that presents to a committee of business heads has advisory standing. A risk function whose objection requires a formal override, recorded with a name, has something considerably stronger.

[P27] And trace the escalation path above it. If the committee splits, establish where it goes and whether that route reaches anybody outside the business. A path that terminates inside the division is a path with a predictable destination.

[P28] There is an artefact worth learning to read here, which is the model risk appetite statement. It is a written statement of how much model risk the firm is prepared to carry, and most versions are unusable because they say the firm has a low appetite for model risk, which is not a statement about anything.

[P29] A usable version is quantitative and uncomfortable. No more than a stated number of tier one models overdue for validation. No tier one model in production without a monitoring plan carrying defined thresholds. No model driving automated decisions above a stated exposure without a named accountable executive. Those are testable, and a firm that writes them has committed to something a supervisor can check.

[P30] The reason this matters is that an appetite statement is the only place a firm says in advance what it will not accept. Everything else in the regime evaluates individual cases, and individual cases are always defensible. A limit set in advance is the mechanism that prevents a sequence of defensible individual decisions from arriving somewhere nobody would have chosen.

[P31] Now the failure mode this whole segment is about, which is that all of this machinery is easy to have and difficult to use.

[P32] There is one more artefact that deserves mention because it is the cheapest signal available and almost nobody looks at it, which is the record of who attended. A committee whose senior members send delegates has told you what it is worth, and the attendance sheet says so more reliably than the minutes do.

[P33] The minutes are worth reading for a different reason. Look for whether they record disagreement. Minutes that show unanimous approval of every item across two years are describing a body that ratifies decisions taken elsewhere, and a committee that never disagrees is not deciding anything.

[P34] A firm can hold a framework, an inventory, documentation templates, a validation calendar, a committee, and an appetite statement, and be unable to answer the supervisor's question, because the inventory is stale, the documentation was written for an examiner rather than a successor, the calendar has a backlog nobody reports, and the committee approves what is brought to it. Every artefact exists and none of them is load-bearing.

[P35] The distinguishing test is whether the machinery is used by the firm itself when nobody is watching. Ask whether anybody consults the inventory to answer an operational question, and whether anybody reads a validation report before making a decision about a model. If the artefacts are produced for external consumption and never consulted internally, they are documentation of a process rather than the process.

[P36] One more observation about documentation that will matter in the live session, and it connects to the litigation material from week one. Everything written here is discoverable. A limitations section that plainly describes what a model cannot do is exactly the document that will be quoted if the model causes harm, and everybody writing one knows that.

[P37] So there is a quiet pressure toward documentation that is complete and unhelpful. Long, thorough, technically accurate, and vague at precisely the points where a specific statement would create exposure. That is not dishonesty, a reviewer counting sections will not detect it, and it is one of the reasons the strongest evidence about a firm's culture is the documents nobody expected to be read.

[P38] The next segment turns to the frameworks written specifically for artificial intelligence, which follow this same structure closely enough to be recognisable, and diverge at one point that matters: a bank's model has a documented purpose and a validation set, and a general-purpose system has neither.
