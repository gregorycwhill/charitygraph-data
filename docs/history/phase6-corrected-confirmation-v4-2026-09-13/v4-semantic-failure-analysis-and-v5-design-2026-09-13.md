# Phase 6 V4 semantic-failure analysis and V5 contract design — 13 September 2026

## Status and boundary

This is an offline diagnostic and design record. It analyses the six completed V4 responses retained privately under the V4 rights policy. It does not execute V5, acquire a source, retry either Smith request, create a candidate, promote knowledge, or change V4 bytes. V5 is a versioned Builder contract proposal, not current product authority or execution authorization.

The authoritative private retention artifact is `archive/processed/phase6-v4-rights-minimized-2026-09-13-private-review.tar`, SHA-256 `904ce684d9ba53df7b3cb9f63db68a38e5d3d08ad49be2acfb92c0bf9cd1dc8f`. It contains the frozen campaign materials and six raw response files. The archive is ignored and is not a repository artifact.

## Observed failure ledger

All six responses bound their declared locators and source roles to the frozen task source list. One Red Cross response passed V4 (three propositions). Five responses had 17 identical validator failures: `first-party epistemic class conflicts with source role`.

| Subject / response | Proposition indexes | Types and epistemic classes | Carrier role | Count | V5 disposition |
|---|---|---|---|---:|---|
| World Vision / `c3bc…12d5` | 3–4 | reach / first-party measure | historical frozen regulator material | 2 | carrier rule corrected; replay passes |
| Bush Heritage / `bc49…86ce` | 0–4 | activity / first-party claim | historical frozen regulator material | 5 | carrier rule corrected; replay passes |
| Bush Heritage / `bc49…86ce` | 7–10 | output or reach / first-party measure | historical frozen regulator material | 4 | carrier rule corrected; replay passes |
| Sunrise / `8ad6…bb84` | 0 | commitment / first-party claim | historical frozen regulator material | 1 | carrier rule corrected; replay passes |
| Sunrise / `8ad6…bb84` | 1–2 | reported implementation activity / first-party claim | historical frozen regulator material | 2 | carrier rule corrected; replay passes |
| Greenpeace first attempt / `3534…3491` | 3, 5 | commitment or reported implementation activity / first-party claim | historical frozen regulator material | 2 | carrier rule corrected; replay passes |
| Greenpeace repeat / `8fd5…a160` | 4 | reported implementation activity / first-party claim | historical frozen regulator material | 1 | carrier rule corrected; replay passes |

The source family for every failed binding is the retained ACNC AIS bundle. Its source role identifies the record carrier. It does not establish that the regulator originated, independently observed, or endorsed the organisation's reported assertion.

## Diagnosis

V4 conflated four separate dimensions:

| Dimension | Required interpretation |
|---|---|
| A. proposition type | What is asserted: activity, output, reach, outcome, commitment, or implementation. |
| B. epistemic class | Assertion status: source-native record, organisation-reported claim or measure, independent finding, or causal claim. |
| C. source role | The carrier/record family holding the cited representation. |
| D. evaluation or adjudication | Human decision about whether the proposition is sufficiently supported and useful. |

The generic V4 validator required a first-party carrier role whenever B was `first_party_claim` or `first_party_measure_reported`. That made C a proxy for B. The prompt required the model to preserve source role but did not state the carrier/claimant distinction, so faithfully bound ACNC material was mechanically rejected. This is a contract and prompt defect, not evidence that the cited assertions are independent findings.

Red Cross is a limited positive control: its annual-report carrier passed the V4 role check. Its `implementation_outcome_reported` shape, however, used people-reached and donation figures without V5's named indicator, unit, measurement period, and evidence-strength fields. It demonstrates V4 satisfiability, not semantic adequacy for an implementation outcome.

World Vision's failed records are reach, not outcomes; Bush retains activity/output/reach distinctions. Neither case supports output-to-outcome, contribution, or causal promotion. The two Greenpeace responses differ in proposition selection and are repeat drift for human adjudication; replay does not score stability or choose between them.

## V5 correction

V5 preserves V4 and adds only two changes.

1. An organisation-reported claim or measure may cite either a direct first-party record or `historical_frozen_regulator_material` carrying the organisation's report. It remains organisation-reported and cannot become an independent finding, source-native regulator fact, contribution, or causation claim through that carrier.
2. `implementation_outcome_reported` requires a population, indicator, measured result, unit, measurement period, and evidence strength. Organisation-reported and independent-evaluation strengths are mutually constrained by the epistemic class and source role.

The V5 schema and prompt explicitly name proposition type, epistemic status, and record carrier separately. Capacity is intentionally unchanged. No lexical or semantic heuristic has been added.

## Exact offline replay

The unmodified response JSON was replayed locally through the V5 compatibility parser. It retains the V4 contract echo and performs the same task identity, scope, locator, role binding, date, and verbatim-source checks. It does not transform a response into V5 output or write a candidate.

| Result | Responses | Propositions |
|---|---:|---:|
| V5 replay passes under corrected carrier rule | 5 | 31 |
| V5 replay remains rejected | 1 (Red Cross) | 3 |
| V4 carrier-rule errors explained | 17 | — |

Red Cross remains rejected only because the historical V4 response lacks the new V5 implementation-outcome measurement fields. That failure is intended: a V5 provider response must supply the fields; replay may not invent them.

## Recommendations and execution gate

- **Outcomes:** `CONTRACT_READY_FOR_HUMAN_REVIEW_WITHOUT_NEW_PROVIDER_CALL`. The existing replay establishes the carrier repair, while reviewers must still adjudicate outcome/reach boundaries and any outcome candidate.
- **Commitments:** `V5_PROVIDER_CONFIRMATION_WARRANTED` only if separately authorized. V5 needs a new provider response to test the tighter implementation-outcome shape; no historical response may be relabelled or completed offline.
- **Capacity:** unchanged: `CONFIRMATION_NOT_EXECUTED_INSUFFICIENT_AUTHORIZED_EVIDENCE` and `REPEAT_AFTER_SEMANTIC_FIX`.

Before any V5 provider execution, the product owner must authorize the exact V5 packet, cost/exposure ceiling, cohort, and adjudication path. A human reviewer must decide whether each replayed proposition is semantically acceptable; mechanical replay alone never advances it.
