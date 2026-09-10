---
title: What counts as a model
series: business-of-data
week: 4
module: Model risk management
section: 1
target_seconds: 600
model: "seconds = words/3.68 + paragraphs * 4.27"
register: narrator, professional adult audience
audience_note: "MIDS working professionals. Most have built models and none have registered one."
method_note: >
  Contrasting cases: two systems performing the same function, one inside the regime
  and one outside it, differing only in what somebody typed into an inventory. The
  misconception is that the regime applies to things that look like machine learning,
  and it is dismantled with the regulatory definition, which turns on function, not technique. Closes on the incentive that governs scope, since the party
  deciding what is in scope is usually the party being regulated by the answer.
constraint: "Must not reference the week's case. Running example is aviation software certification."
status: draft 2026-09-09
---

## Script

[P1] Two systems at the same insurer, both setting prices. The first is a gradient boosted model trained on twelve years of claims, owned by a data science team, and it sets premiums for motor policies. The second is a spreadsheet maintained by two people in the underwriting department, with about four hundred rules in it, and it sets premiums for small commercial property.

[P2] The first is registered in the firm's model inventory. It has a documented purpose, a named accountable owner, a validation report produced by people who did not build it, an annual review, and a monitoring process that flags when its inputs drift away from the data it was fitted on. Changing it requires approval.

[P3] The second is a spreadsheet. It has no owner in any formal sense, it has never been validated, nobody has documented what it assumes, and one of the two people who maintain it is retiring in March. It prices about the same amount of premium as the first one.

[P4] Nothing about that difference reflects a judgment that the spreadsheet is safer. It reflects the fact that somebody filled in an inventory, and when they did, the first system looked like a model and the second looked like a spreadsheet. That is the entire mechanism, and this segment is about why it decides so much.

[P5] Let me name the belief that produces this, because almost everybody in a technical role holds it. The belief is that model risk management is a regime for machine learning, that it exists because statistical systems are opaque, and that a set of explicit rules a human wrote is by its nature outside the concern. Every part of that is wrong, and the regulatory definition is the fastest way to see why.

[P6] The supervisory definition, which has been stable for well over a decade, describes a model as a quantitative method that applies statistical, economic, financial or mathematical theories, techniques and assumptions to process input data into quantitative estimates. Read it again and notice what is absent. There is no reference to learning, to fitting, to a training set, or to opacity. There is no threshold of complexity.

[P7] The definition has three components and it is worth holding them separately, because failures attach to different ones. There is an information input component, which delivers assumptions and data. There is a processing component, which turns inputs into estimates. And there is a reporting component, which translates the estimates into something a business uses. Most people think the processing component is the model. The regime treats all three as the model, which is why a technically flawless system can fail on how its output was interpreted.

[P8] Under that definition, our spreadsheet is a model. So is a lookup table with judgment baked into the bands. So is a vendor tool the firm bought and cannot see inside. So is a heuristic somebody wrote in a notebook that now runs in production. And so, importantly, is a human process that applies a documented quantitative method, because the definition is about the method rather than about who executes it.

[P9] The aviation parallel is exact and it is worth having, because you will see the same structure repeatedly this week. In aircraft certification the question is not whether something is software. It is what the consequence is if the function fails. A system is assigned a design assurance level according to whether its failure is catastrophic, hazardous, major, minor, or of no effect, and the level determines how much evidence you must produce before anybody will certify it.

[P10] So the same lines of code, doing the same thing, require radically different work depending on what happens if they are wrong. A display that shows cabin temperature and a display that shows airspeed are both displays. They are not both the same certification problem, and nobody in that industry finds this confusing.

[P11] Model risk management makes the same move. The question is not what technique was used. It is what decision the output drives and what happens if the output is wrong. A simple method driving a consequential decision is squarely in scope, and a sophisticated method driving nothing much is not the priority.

[P12] Which produces the criterion worth carrying: the regime should attach to the consequence rather than to the technique. If you want to know whether something is in scope, do not ask what it is made of. Ask what decisions it drives, at what volume, and what it would cost if it were systematically wrong for six months before anybody noticed.

[P13] Now the part that determines outcomes in practice, which is who decides. The inventory is a list. Somebody puts things on it. In almost every firm, the people who identify what should be registered are the people who built and operate the things, which is to say the population being regulated by the answer.

[P14] Consider what registration costs that person. Their system acquires a documentation requirement, a validation cycle performed by people who will find problems, an annual review, a change control process that slows their release cadence, and a party with standing to object. None of those makes the system better in a way that appears on their scorecard, and all of them cost time.

[P15] Now consider what registration costs the firm if it does not happen. The system operates unvalidated and undocumented, its assumptions are known only to the people who wrote it, and when it fails the firm will describe the failure as a surprise. That cost is real, it is larger, and it lands on somebody else, later.

[P16] So the incentive at the point of registration points away from registering, and the person facing that incentive is not being asked to do anything dishonest. They are being asked whether their spreadsheet counts as a model, and there is a defensible answer that saves them six weeks. Firms with excellent frameworks and empty inventories are common, and the emptiness was assembled one reasonable answer at a time.

[P17] There are three specific gaps worth learning to look for, because they recur. The first is the vendor model. A firm buys a system from a supplier, the supplier will not disclose the internals, and the firm concludes it cannot validate what it cannot see. The regime says the opposite: the firm using the model owns the risk of the model, and if the vendor will not permit validation, that is a fact about the purchase decision rather than an exemption.

[P18] The second is the tool that grew. Somebody writes an analysis to answer a question once. It is useful, so it runs monthly. Then it is scheduled. Then a downstream system consumes its output. At no point was there a decision to deploy a model, so at no point did anybody ask whether to register one, and the thing now sets prices.

[P19] The third is the model used outside its purpose. A model validated for one population is applied to another, because it was available and it seemed close enough. The registered model is fine. The use is not, and the inventory records the model rather than the uses, so nothing in the system notices.

[P20] That third one is worth dwelling on because it is the most common and the least visible. A model has a documented purpose, and the documentation describes the conditions under which the estimates are reliable. Using it outside those conditions is not a technical failure and the model does not signal it. It returns a number of the same shape, with the same confidence, computed from an assumption that no longer holds.

[P21] Here is a way to test any firm quickly, and you can use it in the live session. Ask how many items are in the model inventory. Then ask how many quantitative methods drive decisions at that firm. If the second number is knowable and much larger than the first, you have found the shape of the problem before looking at a single model.

[P22] The second test is about the definition itself. Ask who at the firm decides what counts as a model, and whether that person can compel a team to register something over the team's objection. If nobody can, the scope of the regime is set by the goodwill of the people it constrains.

[P23] One caution, because the opposite failure exists and it is not harmless. A firm that registers everything produces an inventory of four thousand items, of which sixty matter, and a validation function that spends its year on the wrong ones. Scope discipline is not about maximising the list. It is about being right regarding which items would hurt if they were wrong, which requires the judgment that the regime exists to make explicit.

[P24] So the first question of this module is a scoping question and it is decided before any of the interesting work begins. Whether something is in the regime determines whether anybody independent will ever examine it, and that determination is made by people with a reason to prefer one answer.

[P25] The next segment is about the structure that is supposed to counteract exactly that, the three lines of defence, and about why the structure works on paper considerably more often than it works in a building.
