# Scale S0 offline shadow run — 18 September 2026

**Status:** provider-free simulation from retained metadata. It did not acquire, fetch, transmit, execute, create a real candidate, promote, publish, or authorise S0.

## Preflight result

The shadow uses Option B from `SCALE_S0_POLICY_CALIBRATION_2026-09-18.md`. Its eight ABNs are proposal identifiers only. Every required policy, task, cohort, source, routing, review, promotion, freshness, halt and economic field is populated in `SCALE_S0_SHADOW_MANDATE.yaml`. It deliberately fails `ScaleMandate.validate()` at `authorizing_actor_ref: UNAPPROVED_PRODUCT_OWNER` with `mandate is missing required frozen policy/reference`. Replacing that field alone is not authorised; a future approval must bind the immutable hashes specified in the decision packet.

## Simulated workload

| Measure | Option A rank-first | Option B diversity/stress (simulated) | Option C replay-heavy |
|---|---:|---:|---:|
| Proposed subjects | 8 | 8 | 8 |
| Baseline source attempts | 48–64 | 56–72 | 48–64 |
| New acquisitions / provider transmissions | 0 / 0 | 0 / 0 | 0 / 0 |
| Claimed acquired sources | 0 (shadow does not create acquisition facts) | 0 | 0 |
| PDF / visual-PDF risk | unknown / unknown | 0 observed in shadow; 2–4 policy-risk slots | unknown / unknown |
| Logical tasks | 160 | 160 | 160 |
| Physical calls | 0 observed; 80–104 conditional | 0 observed; 48–120 conditional | 0 observed; 72–96 conditional |
| Luna routes | 104–128 | 120–136 | 112–136 |
| Terra escalations | 8–24 | 16 base; 40 stress ceiling | 8–20 |
| Deterministic outputs | 24 | 24 | 24 |
| Semantic candidates | 136 | 136 | 136 |
| Rights-adjusted review | 0 observed; 6 deterministic audits to 142 conditional reviews | 0 observed; 6 deterministic audits to 142 conditional reviews | 0 observed; 6 deterministic audits to 142 conditional reviews |
| Promotion result | 0 under candidate-only; 24 deterministic + reviewed semantic only under hybrid | same | same |
| Rights-adjusted cost | USD 0 observed; USD 0–8 conditional ceiling | USD 0 observed; USD 0–8 conditional ceiling | USD 0 observed; USD 0–8 conditional ceiling |

Source applicability is a plan, not an acquisition result: ACNC Register/AIS are mandatory; ABR/DGR, official website and annual report are conditional; fundraising registry and specialist sources are trigger-bound; Wikipedia is excluded. The shadow retains prior-output metadata for workload comparison only and never labels it a new production result.

Expected unresolved areas are missing or blocked annual reports/websites, unbound transmission rights, visually material documents, current availability, workforce/governance freshness, relationship endpoints, dependency assessments, conduct completeness, outcomes causation and classification boundaries. The main operational bottleneck is mandatory review capacity, not a predicted provider throughput limit.

## Failure injection results

| Injected retained-realistic condition | Expected certified policy response | Result |
|---|---|---|
| missing annual report; blocked website | Record source-unavailable/not-acquired coverage; no absence inference | pass |
| visually material PDF | Require page-rendered representation or not-processable state | pass |
| schema rejection or malformed Luna output | Mechanical invalidity; one bounded repair then same-family threshold | pass |
| ambiguous billing/send | Immediate slice halt; no retry/replay | pass |
| rights denial | Immediate halt before transmission | pass |
| group identity / relationship endpoint ambiguity | Scoped candidate and mandatory human review; no proposition propagation | pass |
| taxonomy boundary or source conflict | Terra escalation where task permits plus mandatory review | pass |
| budget exhaustion or review backlog | Stop new send/promotion at hard ceiling/backlog | pass |

No Factory defect was found. The shadow exercised policy interpretation and the already-certified offline controls; it did not alter Builder code or Factory semantics.
