---
title: What this course covers
series: business-of-data
week: 1
module: Introduction
section: 1
target_seconds: 600
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Most have built models; almost none have sat in these rooms."
method_note: >
  The contrasting case is two accounts of one event, an engineering account and a
  business account, which describe the same launch and share almost no facts. The
  misconception is that this is a course about artificial intelligence, and it is
  attacked by showing that the decisions in scope are not made by the people who
  built the thing. Closes on what the format asks, because the students need to know
  by the end of this segment what a panel week will feel like.
constraint: "No case is used this week. This module is the map of the other twelve."
status: draft 2026-09-09
---

## Script

[P1] Here are two descriptions of the same event, and I want you to notice how little they share. The first: a team fine-tuned a model on a curated dataset, evaluated it against internal benchmarks, cut latency by forty per cent, and shipped it behind a feature flag to five per cent of traffic before a full rollout in March. The second: the company committed to a three-year purchase of specialised hardware, took a position on whether its training data was lawfully obtained, priced the feature below cost to hold a market it was losing, and disclosed none of the three in the quarter it happened.

[P2] Those are the same launch. Everybody quoted in the first description would recognise the second as accurate, and would not consider it their department. Nobody quoted in the second could tell you what the latency was.

[P3] This course lives in the second description. Not how a model is built, but how one gets released, and what has to be decided by whom for that to happen. The decisions are financial, legal, organisational, and political, and almost none of them are made by the people who trained the thing. That is not a complaint about engineers. It is a description of where the authority actually sits, and the reason it matters to you is that you are going to spend a career producing work that passes through those hands.

[P4] I want to name the assumption most people bring, because it is reasonable and it will get in the way. The assumption is that a course with data in the title is a course about models, and that the business material around it is context. Here it is the reverse. The model is the context. What we examine is the set of decisions that determine whether a working system becomes a product, and those decisions are made by people who mostly cannot evaluate the system and are accountable for it anyway.

[P5] Twelve people sit around a table at one company. Each week you take one of their roles. A controller who decides what an asset is worth on the books. A chief financial officer who decides how the firm is funded and over what term. A general counsel who decides what may lawfully go into the product. A chief risk officer accountable for what could go wrong. Eight more. The next four segments introduce them in four groups, and the reference sheet listing all twelve is the document you will keep open all semester.

[P6] Each one gets introduced with three facts: what they own, what they are measured on, and what they cannot see from where they sit. The third is the one doing the work. It is why a panel of four students produces an argument rather than a consensus, and it is why almost every failure in this course happens in a blind spot rather than in a decision.

[P7] That last claim is the thesis, so let me put it plainly. Business failures are almost never one bad decision. They are a decision made correctly inside one role's frame that turns out to be catastrophic in another's, with nobody owning the seam between the two. When you read a case in this course and find yourself thinking that somebody was an idiot, you have almost certainly not yet found the constraint they were under. Keep reading until you do.

[P8] The course runs in two tracks that do different jobs, and it is worth knowing which is which. This asynchronous module, and the twelve after it, teach the machinery: how depreciation works, what a duration gap is, what independent validation requires, what fair use turns on. Those are durable. They will be true in ten years and they never mention the week's case.

[P9] The live session is the other track and it is where the course actually happens. Ninety minutes a week, one real company, one real decision, argued by four students holding roles with conflicting interests. The reason the modules never mention the case is that cases rot in about two years and concepts do not, so the cases get swapped and this library stays.

[P10] Here is how a case week runs, because it is unusual and you should know the shape before you are in it. Five days ahead, two versions of the case go out. The room's version stops at the decision point and contains no outcome. The panel's version includes what happened, why, and what followed.

[P11] So four students spend five days preparing to defend a decision that the rest of the room has not been told the result of. The questions from the room are genuine, because the people asking do not know the answer. The outcome comes out through cross-examination rather than through anybody announcing it, and the last fifteen minutes are the reveal.

[P12] The assignment for the panel is specific and it is harder than it sounds. Justify what the real people actually did, from inside the role you are holding, with what was known on that date. Not what you would have done. Hindsight makes nearly every decision on this list look obvious, and a student who is allowed to say what they would have done gets to posture instead of thinking. A student who has to defend the decision as taken has to reconstruct the constraints first, and you cannot defend a decision you have not understood.

[P13] For the eleven weeks you are not on a panel, you submit three written questions before class, answerable from the room's packet. A question whose answer is a fact is worth nothing. A question that forces a panelist to expose an assumption is worth the grade. The questions come to me rather than to the panel, which keeps the panel live rather than rehearsed, and means I arrive holding several dozen questions from which to build the session. In a real sense the class writes the lesson plan.

[P14] Sixty per cent of the grade is live work in the room on weeks you cannot outsource. Three panel weeks are thirty per cent, the questions and participation across the other eleven are another thirty, and the final project is forty. There is no exam. I am telling you the weighting in the first segment rather than burying it in a syllabus because it should change how you allocate your attention.

[P15] The final is a case your group writes, sourced from somebody's own world. A decision one of you watched, a company one of you worked at, an industry one of you has access to. The requirement is access rather than fame, and an obscure decision with real documents beats a famous one with only news coverage. Groups form in week three and pitch in week five, and the week five pitch is about whether you can actually obtain the material.

[P16] A word about vocabulary, because this field uses several terms loosely and the looseness hides real disagreements. Training cost and inference cost are different things with different shapes. Training is a large one-off spend that produces an asset. Inference is a cost per request that scales with how many people use the product. A firm can have a spectacular training bill and a healthy business, or a modest one and an unprofitable product, and conflating the two makes most cost arguments in this industry incoherent.

[P17] The other term is open, which is used for at least three different things. Open weights means the parameters are downloadable. Open source means the licence permits use, modification and redistribution without meaningful restriction, which many published model licences do not. Open access means you can reach the system through somebody's interface, which is the weakest of the three and is regularly described with the other two words.

[P18] We settle definitions for those in the first live session and then hold each other to them for twelve weeks. That is not pedantry. At least one case in this course turns entirely on which of the three a company meant, and on whether the ambiguity was accidental or was the point.

[P19] One thing that follows from the format and is worth saying early. Conceding a good point scores. A panel that never yields is a panel that is not listening, and stonewalling is visible from the first minute. Knowing your material well enough to grant a fair objection and then explain why the decision still went the way it did is the strongest thing you can do in the room.

[P20] The other thing worth saying early is about tone. Several of these cases involve real people who made decisions that ended badly and are still working. Some of them involve harm to people who had no say in it. Reconstructing why an intelligent person did something is not the same as endorsing it, and the discipline of this course is holding both at once. If you cannot argue the position, you have not understood it well enough to criticise it.

[P21] Last, a note on what a good week looks like from your side, because the shape of the work is unusual. On a non-panel week the job is to read the packet, find the three assumptions that carry the most weight with the least support, and write a question about each. That is a couple of hours, and it is genuinely a couple of hours rather than a nominal one, because a question that exposes an assumption requires understanding the packet well enough to know which parts are load-bearing.

[P22] On a panel week the job is considerably heavier and it front-loads. You receive your role brief with the packet, five days out. The mistake every first-time panelist makes is preparing a summary of the case. The room has the case. What you are preparing is a position, which means knowing your own constraint well enough to explain why the obvious alternative was unavailable, and knowing the other three roles well enough to predict what they will accuse you of.

[P23] You get three panel weeks across the semester, in three different roles, and you never sit with the same classmate twice. The rotation calendar is published this week rather than announced week by week, so look at it now and note your three, because a panel week that collides with another course's midterm is a problem you can solve in September and cannot solve in November.

[P24] The next four segments introduce the twelve roles, three at a time, in the groups you will remember them in: the functions responsible for money, for risk, for what goes into the product, and for the firm's relations outside itself.
