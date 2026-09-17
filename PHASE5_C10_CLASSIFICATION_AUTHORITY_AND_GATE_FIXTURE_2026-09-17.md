# Phase 5 C10 classification authority and gate fixture — 17 September 2026

## Purpose

C10 repairs the classification-authority defect recorded by Gate Attempt 1 and materialises the fixed retained cohort into a deterministic offline gate fixture. Attempt 1 remains historical evidence with result `PHASE5_NORTH_STAR_COMPLETION_GATE_FAIL`.

## Authority repair

`source_reported_classification_observed` now means only that the identified source reported the stated taxonomy/version/concept. It requires `epistemic_basis: source_fact` and `classification_authority: source_reported`; it carries source, locator, lineage, method and observation time, has no assignment status and never carries `effective_assignment`.

`assessed_classification_observed` means a governed CharityGraph assessment. It requires `epistemic_basis: governed_event`, `classification_authority: charitygraph_assessed`, taxonomy/version/concept, method and an assignment status. Only `accepted` and `narrowed` are effective; `narrowed` is effective only for its stated final concept and scope. Candidate, rejected, abstained and superseded records remain traceable history and cannot become card evidence.

The dual-evidence adversarial control preserves a source-reported SDG 4 statement and an independently assessed SDG 5 assignment as distinct propositions. It makes no reconciliation, dishonesty, or truth-supremacy inference.

## Materialised retained gate cohort

The deterministic test fixture contains exactly these seven organisation subjects: Australian Red Cross Society, Environmental Justice Australia, Fitted for Work, APNIC Foundation Limited, World Vision Australia, Tweed and Local Buying. Lifeblood is an operating-division scope of Australian Red Cross, never a second organisation subject.

The fixture transcribes one existing C1–C9 retained governed control for each subject without changing its semantics. Each positive contains the retained-control basis, source identifier, evidence locator, subject, organisation scope, explicit observation time, method and a deterministic fixture producer. World Vision’s retained SDG control is source-reported and carries `classification_authority: source_reported`.

The fixture has seven real retained positive transcriptions and 133 explicit `NOT_REVIEWED` coverage states. Its literal matrix therefore accounts for `7 subjects × 20 sections = 140` states. It creates no positive claim for an empty section and introduces no source, extraction, semantic execution, candidate, promotion or runtime data.

## C10 result

C10 is a bounded adapter and test-fixture change. It does not yet declare the Phase 5 completion gate passed. Gate Attempt 2 freezes the post-C10 heads before evaluation, and permits no production-code repair after that freeze.
