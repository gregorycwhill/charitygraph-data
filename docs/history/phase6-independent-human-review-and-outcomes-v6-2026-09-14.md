# Phase 6 Independent Human Review and Outcomes V6 Confirmation — 14 September 2026

**Status:** Historical human-review and execution record; not a current semantic contract or independent authority document

This record preserves the independent human-review findings supplied by the product owner and the bounded Outcomes V6 execution that followed. It does not promote model candidates to governed knowledge or settle the independent review of V6.

## Commitments V5 human review

**Disposition:** `ADVANCE_WITH_REPRESENTATION_FIX`

The review covered The Sunrise Project Australia Limited and two Greenpeace Australia Pacific Limited attempts. The aggregate proposition adjudication was 14 `ACCEPT`, 3 `ACCEPT_MINOR_CORRECTION`, and 1 `REJECT` (18 propositions total).

For Sunrise, four propositions were accepted and one was rejected. The rejected proposition converted the organisation's self-reported 2025 implementation statement that it “worked ... to accelerate the transition to clean energy” into a separate `commitment_stated`. The reviewer found this to be activity, not a separately stated commitment. The error was non-critical because the mission commitment and concrete implementation activity were represented elsewhere and the analyst answer did not materially change.

Greenpeace replicate 1 had six accepted propositions and one minor correction: the end-of-century period applies to the climate objective, not indiscriminately to the full mission or charitable purpose. Replicate 2 had four accepted propositions and two minor corrections: environmental campaign objectives were grouped too broadly, and `reported_completed` overstated source wording that activities were “under way” or “aimed at” an objective.

The human repeat judgment was `STABLE_AT_ANALYST_ANSWER_LEVEL`. The attempts differ in proposition granularity but support the same answer: explicit commitments exist; concrete 2025 implementation is self-reported and bounded to the organisation/reporting period; the reviewed evidence does not establish independent verification. Exact proposition inequality was not treated as answer-changing instability.

Representation work required before or within the governed product-value slice:

- expose an explicit reviewed-source coverage state for independent implementation verification not found in reviewed sources;
- expose a separate coverage state for affirmative evidence of non-implementation not found in reviewed sources;
- never present the absence of an independent-evidence proposition as proof that no such evidence exists;
- tighten stated commitment versus retrospective implementation wording; and
- do not overstate ongoing activity as completed.

The precise source wording for the second Greenpeace correction was "undertaking activities aimed at"; `reported_completed` overstated that wording. No further Commitments provider call is authorized by this record.

## Outcomes V5 human review

**Disposition:** `REPEAT_AFTER_SEMANTIC_FIX`

World Vision Australia passed human review. Projects, reach, and participation remained outside observed-outcome classifications. The candidate materially reduced analyst effort while preserving the conclusion that the supplied evidence did not provide a measured beneficiary outcome.

Bush Heritage Australia failed on one critical semantic classification; the other 11 of 12 propositions were otherwise defensible. A claim that Bush Heritage sustained ecosystem health through management was typed `outcome_observed_reported`, although the supplied evidence reported no ecological indicator, measurement method, comparator, structured assessment, or other observation demonstrating that ecosystem health was sustained. This is an outcome/contribution claim linking management activity to an asserted result, not an observed outcome solely because the result is outcome-shaped.

## Outcomes V6 semantic correction and execution

Builder contract V6 requires `outcome_observed_reported` to carry an `observation_basis` (`quantitative_measurement`, `qualitative_assessment`, `monitoring_or_observation_result`, or `evaluation_result`) and nonblank `observation_details` identifying what was observed. A claim-only case is not an observed outcome. Qualitative observation remains possible when the assessment or observation itself is reported. Source role and epistemic status remain separate: a first-party annual report may report an outcome measure, while its status remains first-party unless independent corroboration exists. The provider prompt states the same boundary and gives the rejected Bush-type claim as an adversarial example. No Python language heuristic was added.

Offline replay of the unchanged historical V4 responses under V6 found:

- World Vision: all five propositions remain valid; no observed-outcome proposition was present.
- Bush Heritage: proposition 11 is rejected because `observation_basis` and `observation_details` are absent; the other 11 propositions pass V6 validation.
- No other scope, source-role, locator, date, or V6 semantic failures were found. Historical response bytes were unchanged.

Exactly two new Standard requests were then executed, using `gpt-5.6-luna`, low reasoning, and the already-authorized frozen source representations:

| Subject | Provider posts | Candidate propositions | Input/output tokens | Actual cost USD / AUD | Conservative exposure AUD |
|---|---:|---:|---:|---:|---:|
| World Vision Australia | 1 | 2 | 10,966 / 579 | 0.003437 / 0.005225 | 0.022416 |
| Bush Heritage Australia | 1 | 10 | 8,999 / 2,340 | 0.005058 / 0.007689 | 0.020920 |
| **Total** | **2** | **12** | **19,965 / 2,919** | **0.008495 / 0.012914** | **0.043336** |

Both responses completed and passed strict schema, V6 contract, task identity, scope, locator, carrier-role, epistemic-class, and observation-basis validation. The V6 Bush output classifies its management-linked ecosystem statement as `causal_attribution_claim_reported`, not `outcome_observed_reported`; this is a mechanically validated candidate, not a human finding. World Vision emitted two reach/participation propositions and no observed outcome. No call was retried or ambiguous.

The conservative AUD 0.043336 V6 exposure is below the authorised AUD 0.50 campaign cap and AUD 0.25 per-request cap. The retained V4 reserve was AUD 0.166419; the two historical Smith ambiguities remain separately tracked at AUD 0.042120 and were not used as V6 budget. Provider policy attestation and source-rights lineage remained pinned to their existing identities.

The private, candidate-blind V6 packet is `archive/processed/phase6-outcomes-v6-independent-review-2026-09-14-private-v2/` in the local CharityGraph workspace. Its source-only material, raw V6 outputs, evidence lineage, V4/V5/V6 comparison, analyst-task material, and proposition worksheet are prepared with reviewer fields blank. Packet status is `READY_FOR_HUMAN_REVIEW`; no V6 human adjudication has occurred.

## Capability and programme status

- **Commitments:** `ADVANCE_WITH_REPRESENTATION_FIX`; downstream product-value work must include the representation requirements above. No additional Phase 6 Commitments campaign is planned.
- **Outcomes:** awaits independent human adjudication of the V6 packet; no advancement is claimed.
- **Capacity:** remains `CONFIRMATION_NOT_EXECUTED_INSUFFICIENT_AUTHORIZED_EVIDENCE` and `REPEAT_AFTER_SEMANTIC_FIX`; no source acquisition or provider work occurred.
- **Phase 6:** not complete. The broader Phase 5 Top-100 full-card objective remains active. Product-value work remains downstream and was not started here.

Across this V6 execution there were two provider calls, zero new source acquisitions, zero governed promotions, zero Viewer changes, and zero public v0.5 changes. This historical record does not update public contract 0.5 or define current product semantics beyond the recorded V6 experiment.
