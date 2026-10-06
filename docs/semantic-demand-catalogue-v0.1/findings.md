# Pilot curation and review findings

## Curation

- Broad temporary pool: **78** semantic candidates; retained: **36**.
- Tier distribution: **A 9**, **B 18**, **C 9**. Single-domain: **0**; workflow-derived cross-domain: **36** (two to six domains). The single-domain count is zero because even atomic demands retain the evidence/coverage domain where material; tiers describe decision composition, not a domain-count quota.
- Adversarial/non-inference: **12**. All 20 North Star v0.3 domains occur in retained questions.
- Answer states intentionally permitted by every template: `supported`, `bounded_partial`, `tested_missingness`, `unresolved`; positive support is never presumed.

Signatures group `persona + decision intent + subject/scope + proposition family + operation + joins + temporal mode + evidence bar + forbidden inference`.  Candidates were grouped on that tuple before wording review.

| Rejected candidate | Disposition | Why |
|---|---|---|
| “Which charities serve {POPULATION} in {GEOGRAPHY}?” | duplicate of `SDC-03` | Same cohort/filter, program/service population/geography scope and coverage bar; different wording only. |
| “Which organisations have programs in {GEOGRAPHY}?” | duplicate of `SDC-04` | Same service-map workflow but less precise because it erased operating/delivery role. |
| “Rank charities by efficiency.” | low value | Implies a universal normative metric; period, allocation and scope make it semantically unsafe. |
| “Is {ORGANISATION} a good charity?” | low value | No bounded proposition, user-owned rule, evidence bar or output semantics. |
| “What is the next dollar spent on?” | retained only as `SDC-20` adversarial | The unconstrained version falsely derives marginal destination from historical financial statements. |

## Independent critique and bounded corrections

Review found two local defects and corrected them: (1) an early service question used “available” without a date and is now `SDC-11` with an as-of date and `unresolved` option; (2) an early fundraiser question equated donation revenue with channel proceeds and is now `SDC-18`, explicitly requiring an appeal/channel-to-financial-line join. No ontology/schema expansion was proposed for either defect.

Residual risks: signature judgment remains partly human; actual coverage distributions may later expose rare but important demand; a benchmark needs separately adjudicated real instances; and policy-sensitive mandate rules need user-owned rule parameters. None warrants an ontology change merely because a question is currently difficult.

## Publication metadata

Proposed later remote branch: `cg-semantic-demand-catalogue-pilot`; proposed PR title: `docs: add semantic demand catalogue v0.1 pilot`; no remote or PR action was performed.

## Decision

**PILOT_METHOD_READY_FOR_SCALE** — scale only after retaining this schema, demand-signature curation, typed-slot discipline and answerability outcomes; it does not authorise runtime, ontology, public-contract or evidence changes.
