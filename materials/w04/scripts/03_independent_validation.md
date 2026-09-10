---
title: Independent validation
series: business-of-data
week: 4
module: Model risk management
section: 3
target_seconds: 1200
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Most have tested a model; few have been validated by somebody else."
method_note: >
  Opens on the distinction between a review and a validation, which is the whole
  segment compressed, then builds the three components of validation in the order a
  validator works through them. The aviation parallel supplies the idea of a
  certification basis, which is the piece students find hardest: that you validate
  against a stated intended use rather than in general. Closes on effective
  challenge, and on what a validator does when the honest answer is that nobody knows.
constraint: "Must not reference the week's case. Running example is aviation software certification."
status: draft 2026-09-09
---

## Script

[P1] A team finishes a model and sends it for validation. Six weeks later a report comes back. It is forty pages, it reproduces the team's results, it confirms the accuracy figures, it notes that the documentation is thorough, and it concludes that the model is fit for its intended purpose.

[P2] That report may be a validation and it may be a review, and the difference is not visible in the document. The test is whether the person who wrote it could have concluded otherwise. Not whether they had the technical ability, but whether an unwelcome conclusion would have survived contact with the organisation.

[P3] So I want to start with the definition and then spend the segment on what it demands. Validation is an evaluation of a model, performed by parties who did not build it, competent to assess it, and positioned such that they can reach a conclusion the business does not want. Remove any one of those three and you have a review.

[P4] The first element, not having built it, is the easiest to satisfy and the one people fixate on. It matters because a builder cannot see their own assumptions. They are not concealing them. They made a hundred choices, most of them reasonable and most of them unremembered, and asking somebody to enumerate their own invisible decisions does not work.

[P5] The second element, competence, is harder than it looks and it produces a real dilemma. A validator who does not understand the technique cannot challenge it, and the only people who understand a novel technique are frequently the people using it. So the validation function either lags the first line technically, in which case its challenge is superficial, or it recruits from the same pool, in which case its independence is social rather than merely structural.

[P6] The third element is the one we spent the previous segment on and I will not repeat it, except to note that it is the element most likely to be missing and the least likely to be documented.

[P7] Now what validation actually examines. There are three components and they are examined in order, because a failure at the first makes the others moot.

[P8] The first is conceptual soundness. Is the approach appropriate for the problem, are the assumptions defensible, is the theory sound, and does the design match what the model is for. This is a judgment about the choice of method rather than about its execution, and it is where the most consequential findings come from.

[P9] Here is a concrete version. A model predicts whether a customer will default, trained on five years of data. Conceptually, that data covers a period in which interest rates never rose and unemployment never exceeded a certain level. The model may be executed flawlessly and it has learned relationships that were never tested against the conditions the firm most needs it to handle. That finding does not come from checking the code.

[P10] The second component is ongoing monitoring. A model is not validated once. It is deployed into a world that changes, and validation must establish what will be measured while it runs, at what frequency, against what thresholds, and what happens when a threshold is breached.

[P11] That last clause is where most monitoring plans fail. A plan that says performance will be monitored monthly, without a number at which somebody must act, is a plan to observe a decline rather than to respond to one. A monitoring threshold with no defined action is a thermometer in a room with no heating.

[P12] The third component is outcomes analysis. Compare what the model predicted with what happened. This sounds elementary and firms are surprisingly bad at it, for a specific structural reason: the prediction and the outcome are usually held by different systems, separated by months, and nobody's job is to join them.

[P13] There is a subtler problem underneath, which is that acting on a prediction changes the outcome you get to observe. If a model says a customer will default and the firm declines them, the firm never learns whether they would have. The observed data is filtered by the decisions the model itself drove, which means naive outcomes analysis measures the model against a world the model created.

[P14] Validation is supposed to catch that and frequently does not, because catching it requires either holding out a control group, which costs money and is sometimes unlawful, or reasoning carefully about the selection, which requires the kind of statistical care that the schedule does not allow.

[P15] Alongside those three sits benchmarking, which asks a question that sounds obvious and rarely gets asked. It is how this model performs against a simple alternative. Not against nothing, against a credible baseline: the previous model, a logistic regression, a rule a domain expert would write.

[P16] The reason to insist on it is that a great deal of complexity is unjustified and the justification is never tested. A model that beats a well-tuned simple baseline by two per cent on a metric, at ten times the operational complexity and no interpretability, is a choice that somebody should have to defend. Validation is the only point in the process where anybody has standing to ask.

[P17] Now the aviation parallel, and this one supplies a concept that has no clean name in the model world and should.

[P18] In aircraft certification, before anybody tests anything, the regulator and the applicant agree a certification basis. It states which regulations apply to this aircraft, which special conditions attach to novel features the regulations did not anticipate, and what the intended function of each system is. Everything afterwards is evidence against that basis.

[P19] Notice what that accomplishes. It fixes the target before the work begins. You are not demonstrating that the aircraft is safe in general, which is unfalsifiable. You are demonstrating that it meets a specified standard for a specified function under specified conditions, and both parties agreed the specification before either had an interest in the answer.

[P20] Model validation needs the same thing and often lacks it. If the intended use is not written down before validation begins, the validator is assessing the model against a purpose that can be adjusted in response to the findings. A weakness in one population becomes acceptable if the intended use quietly narrows to exclude it, and the narrowing happens in a meeting rather than in a document.

[P21] So the first question a validator should ask is not about the model. It is what this is for, who will act on it, and under what conditions the estimates are claimed to hold. If those are not written down, the validation has no fixed target and its conclusion means considerably less than it appears to.

[P22] There is a practical version of that question worth carrying, because it works even when you have no technical access. Ask what population this model will serve, then ask what population it was fitted on, then ask who checked whether those are the same. In a surprising number of firms the third question has no answer, and it is the question that most often precedes a large loss.

[P23] The reason it has no answer is organisational rather than technical. The team that built the model knows the training data. The team that deploys it knows the population it will meet. Those are frequently different teams, in different divisions, and the comparison between the two is on neither team's task list. It is a seam, in exactly the sense from week one.

[P24] There is a second thing aviation supplies, which is the idea of a limitation that travels with the artefact. An aircraft has a flight manual with a limitations section: speeds not to be exceeded, weights not to be exceeded, conditions not to be entered. Those limitations are not advisory and they are attached to the aircraft rather than held in the manufacturer's files.

[P25] The model equivalent is the statement of a model's valid operating range, and it is routinely produced and routinely lost. The validation report says the model is reliable for this population, this range of values, this period. Then the report goes into a repository, the model goes into production, and the person deciding six months later to apply it to an adjacent population has never read the report and has no reason to know it exists.

[P26] That gap is worth stating as a design failure rather than a discipline failure. The limitation lives in a document and the model lives in a system, and nothing connects them. A firm that surfaces a model's valid range at the point of use has solved a problem that most firms address by asking people to remember.

[P27] Now the phrase that carries the weight in this whole regime, which is effective challenge.

[P28] Before the definition, it is worth noticing what the phrase is doing. Regulators could have written that validation must be thorough, or independent, or documented, and all three would be checkable and none would guarantee anything. Instead the standard is written in terms of an outcome, which is unusual and deliberate.

[P29] Supervisory language describes what validation must produce as critical analysis by objective, informed parties who can identify limitations and produce appropriate changes. The word doing the work is effective. Challenge that cannot produce a change is not challenge, and the standard is deliberately written to make the outcome part of the definition rather than the effort.

[P30] Three things are required for challenge to be effective, and they are worth separating because firms usually have one or two.

[P31] Incentive. The challenger must have a reason to challenge and no reason not to. If raising a finding costs them a relationship they need, the incentive points the wrong way and no amount of professionalism reliably overcomes it.

[P32] Competence. They must understand the model well enough that a finding survives a technical response. A challenger who can be dismissed with an explanation they cannot evaluate has no standing, and everybody involved knows it within one meeting.

[P33] Influence. The finding must reach somebody who can act, and acting must be a live possibility. That means the timing question from the previous segment: if validation concludes after the point of no return, its influence is zero regardless of the other two.

[P34] Here is the validator's dilemma, stated plainly, because you may hold this role on a panel and it is the honest description of the job. The validator is asked to assess a model in six weeks that took nine months to build, using documentation written by the builders, with access to data the builders curated, on a technique the builders know better than they do, before a date the validator did not set.

[P35] Under those conditions the validator has three available strategies and each has a cost. They can go deep on one aspect, which produces a strong finding on a narrow question and leaves the rest unexamined. They can go broad, which produces a competent survey and no finding that will change anything. Or they can focus on process compliance, which is fast, defensible, and detects almost nothing that matters.

[P36] The third strategy is the one the incentives reward and it is the one that fills the industry with validation reports that identified no material issues in models that later failed. Nobody chose to do worthless work. The strategy that survives an audit of the validator is not the strategy that finds the problem.

[P37] Which gives a practical thing to look for. Read a validation report and ask what it would have taken for it to conclude that the model was unsuitable. If you cannot construct that scenario from the document, the report was written to be complete rather than to reach a conclusion, and its finding of no material issues carries no information.

[P38] The same test applies to the process rather than the report. Ask the validation function when it last concluded that a model was unsuitable for its intended use, and what happened next. A function that has never reached that conclusion is either overseeing unusually good models or is not equipped to reach it, and the second is far more common than the first.

[P39] There is a variant worth watching for, which is the conclusion that arrives with an escape hatch attached. The model is suitable subject to the following conditions, and the conditions are then accepted by the business as findings. That construction lets the validator record a concern and lets the business proceed, and both parties can describe their own conduct accurately afterwards. It is the most common form of a validation that changed nothing.

[P40] There is a specific failure that follows from all this and it is worth naming because it is the most common one. Validation confirms that the model does what the builders said it does. The builders said it predicts a quantity accurately. Validation checks the accuracy. Both parties are satisfied.

[P41] And nobody asked whether predicting that quantity accurately produces the business outcome the firm wants. A model can be accurate and the decision it drives can be wrong, because the quantity being predicted is a proxy for the thing that matters and the proxy was chosen early, by somebody who is no longer involved, for reasons that are no longer written down.

[P42] So the highest-value validation question is frequently not about the model at all. It is what decision this drives, and whether accuracy on this quantity is the right condition for that decision to be good. That question is outside the technical scope of most validation functions and it is where the largest findings live.

[P43] Now what a validator should do when the honest answer is that nobody knows. This arises constantly with newer systems and it is worth having a position on before you are asked.

[P44] The wrong response is to approve because the evidence of harm is absent. Absence of evidence is what you have when nobody has looked, and a validator who treats an unexamined question as a resolved one has converted their own ignorance into an approval, which is the most damaging thing this function can do.

[P45] The other wrong response is to block on the grounds of uncertainty, because uncertainty is the permanent condition and a function that blocks on it will be removed from the process within a year. Neither approving nor blocking is right when the answer is unknown.

[P46] The right response is to name the uncertainty precisely, state what would resolve it, specify what compensating control makes the exposure tolerable meanwhile, and put a date on revisiting it. That converts an unknown into a managed position with an owner, which is the actual product of a good risk function and it is neither a yes nor a no.

[P47] Notice that this requires the firm to have somewhere to put such a statement, and somebody whose job is to revisit it. Most of the value of the whole regime is in that unglamorous machinery. The analysis is often the easy part. Ensuring that a conclusion reached in March is acted on in November, by somebody who was not in the room in March, is where the work actually is.

[P48] One more thing about revisiting, because it is the part that decays. A finding accepted with a review date in nine months creates an obligation on a person who will probably have moved role by then, recorded in a system that person does not read. Firms that make this work do one specific thing: the review date generates a task with an owner, and the owner is a role rather than a name, so that the obligation survives the individual.

[P49] That sounds trivial and it is the difference between a risk that is managed and a risk that was noted. When you read a case and find that a known issue went unaddressed for two years, the question worth asking is not why nobody cared. It is what mechanism was supposed to bring it back, and whether that mechanism depended on a particular person remembering.

[P50] One more element and it will come up in the case. Validation applies to vendor models, and the argument that a firm cannot validate what it cannot see is not accepted. The firm using the model owns the risk of the model. If the supplier will not permit sufficient examination, the firm's options are to obtain what it needs contractually, to build compensating controls around a system it cannot inspect, or not to use it.

[P51] In practice firms take a fourth option, which is to use it and document that validation was limited by vendor constraints. That sentence appears in a great many validation reports. It is honest, it is a description of a decision rather than a constraint, and reading it should prompt the question of who accepted that limitation and whether they understood what they were accepting.

[P52] So the summary is this. Validation is defined by whether an unwelcome conclusion could survive, not by the quality of the analysis. It examines conceptual soundness, ongoing monitoring, and outcomes, and it needs a fixed statement of intended use before it begins or its target moves. Effective challenge requires incentive, competence, and influence, and firms usually have two.

[P53] The next segment is the machinery that makes all of this durable rather than a moment: the inventory of what the firm has deployed, the documentation that travels with each item, and the change control that decides when something must be looked at again.
