# Phase 5 North Star Completion Gate — 17 September 2026

**Result:** `PHASE5_NORTH_STAR_COMPLETION_GATE_FAIL`

**Status:** gate evaluation record on the unmerged specialist campaign branch. This record does not declare Phase 5 complete, authorise Top-100 work, alter public v0.5, or authorise provider, acquisition, promotion, runtime, or Phase 6 work.

## Frozen candidate

The gate was evaluated before this document was created.

| Repository | Base | Frozen candidate head |
|---|---|---|
| Builder PR #77 | `a83cb6db6a4c24bf51c15994af2651dccf97d5ff` | `04da061f43e727ddee59235663909470fec77151` |
| Data PR #30 | `4bef354f5ad86e060bfe60b40edcdfae9e1a7ed4` | `dfafcd19cdfe160f3cc48b2fd254fd2bf30e3435` |

Both PRs were open, targeted `main`, had the stated bases and heads, contained no unexpected commits, and were cleanly mergeable when frozen. Neither PR was merged.

## Fixed retained cohort and gate method

The evaluated cohort was limited to Australian Red Cross Society, including the retained Lifeblood operating-division control; Environmental Justice Australia; Fitted for Work; APNIC Foundation Limited; World Vision Australia; Tweed; and Local Buying. The card subject is always the resolved organisation subject where available. Lifeblood remains an operating-division scope of Australian Red Cross rather than a separate organisation subject. Program, service, population, reporting-period, funding, and relationship scopes remain the narrow scopes established in their C1–C8 retained controls.

The gate read the active v0.2 card, C1–C8 records, C9 red-team record, dry-run record, ledger, Builder contracts and tests. It exercised the active projection/coverage contract and adapters for the retained control families, inspected all twenty section states, reran adversarial controls, and followed representative positive and coverage paths through projection, CardEvidence or relationship, observation, scope, locator, source record, lineage, method, time, epistemic basis, and coverage state.

The candidate does not contain a materialised seven-subject `IntegratedGraph` made from its retained corpus. Its C1–C9 evidence is represented as retained records plus bounded adapter tests. This is an evaluation-evidence shortfall for the requested literal seven-card compilation, recorded below; it is not the representation defect that determines the result.

## Material gate blocker

### Source-reported classification lifecycle authority is ambiguous

`SpecialistInput` gives both `source_reported_classification_observed` and `assessed_classification_observed` the same `assignment_status` vocabulary: `candidate`, `accepted`, `narrowed`, `rejected`, `abstained`, and `superseded`. For either predicate, `accepted` and `narrowed` project `effective_assignment: true` and can produce CardEvidence.

The source-reported predicate requires `source_fact`, while the assessed predicate requires `governed_event`. That provenance difference is useful but does not make the lifecycle authority unambiguous: the projected card payload does not identify whose acceptance/narrowing decision the status records. `assignment_status: accepted` and `effective_assignment: true` can therefore be read as CharityGraph endorsement of a source statement. The predicate name is insufficient to prevent that material false effective-classification interpretation for a normal consumer of the payload.

This fails Part F1. It affects §4, where source-reported activity/SDG lenses project, and §19, whose contract owns CharityGraph-assessed classification/search governance. It is a **representation defect**, not a missing source or a scale limitation.

The smallest future repair is to separate source statement status from CharityGraph assignment adjudication, or make the issuer/authority and non-endorsement semantics explicit in the projected payload and CardEvidence contract. A durable test must prove that a source-reported statement cannot carry CharityGraph `accepted`, `narrowed`, or `effective_assignment` semantics, while an assessed assignment may do so under governed decision lineage. No repair was made in this gate run.

## Final bounded-gate dispositions

| § | Final disposition | Gate basis |
|---:|---|---|
| 1 | `BOUNDED_COMPLETE_MIXED` | Retained identity controls plus explicit coverage preserve identity/operating-unit boundaries. |
| 2 | `BOUNDED_COMPLETE_SUPPORTED` | Retained purpose/cause proof remains governed and distinct from activity/outcome. |
| 3 | `BOUNDED_COMPLETE_MIXED` | Program/service scope controls and honest coverage hold. |
| 4 | `NOT_COMPLETE_REPRESENTATION_DEFECT` | Source-reported lifecycle status can imply an effective CharityGraph assignment. |
| 5 | `BOUNDED_COMPLETE_MIXED` | Population and geography roles remain atomic and scope-qualified. |
| 6 | `BOUNDED_COMPLETE_MIXED` | Participation distinctions and coverage hold. |
| 7 | `BOUNDED_COMPLETE_MIXED` | Direct-service facts and unknown/not-processed capacity remain distinct. |
| 8 | `BOUNDED_COMPLETE_MIXED` | Fundraising practice/campaign remains distinct from finance and funding. |
| 9 | `BOUNDED_COMPLETE_MIXED` | Governance role and snapshot-time controls hold. |
| 10 | `BOUNDED_COMPLETE_MIXED` | Workforce role, measure, scope and time controls hold. |
| 11 | `BOUNDED_COMPLETE_MIXED` | Scale and source-attributed capability remain distinct from capacity. |
| 12 | `BOUNDED_COMPLETE_MIXED` | Directed operator proof and architecture-only roles remain qualified. |
| 13 | `BOUNDED_COMPLETE_MIXED` | Financial source rows, stages, scope and coverage remain bounded. |
| 14 | `BOUNDED_COMPLETE_MIXED` | Funding facts remain separate from dependency assessment. |
| 15 | `BOUNDED_COMPLETE_MIXED` | Ethos, commitment and implementation semantics remain qualified. |
| 16 | `BOUNDED_COMPLETE_KNOWABILITY` | Conduct architecture records coverage without a clean-record assertion. |
| 17 | `BOUNDED_COMPLETE_MIXED` | Dated event and historical interpretation remain distinct. |
| 18 | `BOUNDED_COMPLETE_SUPPORTED` | Retained outcomes/evaluation proof preserves activity/output/outcome/contribution/causation distinctions. |
| 19 | `NOT_COMPLETE_REPRESENTATION_DEFECT` | The same lifecycle-authority ambiguity affects classification governance. |
| 20 | `BOUNDED_COMPLETE_MIXED` | Coverage and provenance states remain distinct; positive correction/dispute evidence remains absent. |

## Inspect, Compare and Verify findings

Inspect controls found no additional material false positive, false absence, false scope, false current-state, false relationship, or false epistemic claim in the evaluated C1–C9 adapter paths. Supported positives require their expected substantive detail, subject, scope, evidence locator, source record, lineage, explicit observation time and method. Generic missingness rejects `asserted_none` and `observed_absent` for the relevant bounded adapters.

Compare controls preserved the tested distinctions: organisation versus Lifeblood operating division; program/service versus organisation; population versus participation; service capacity versus organisation capability; fundraising practice versus finance; finance versus funding/dependency; relationship ownership versus proposition ownership; commitment versus implementation/practice/completion; source fact versus source interpretation; outcome/change versus causation; and historical fact versus current-state presentation. The classification comparison did not pass because it exposed the lifecycle-authority blocker above.

Representative Verify paths retain projection/CardEvidence or directed relationship, Observation, subject/scope, evidence locator, source record, projected lineage, method, explicit observation time and epistemic basis. Discovery signals correctly terminate as `derived_signal` observations and cannot create CardEvidence. Coverage inputs record a section state and basis without fabricating an observation date.

## Required audits

| Audit | Result |
|---|---|
| False absence | Pass. Source silence, unavailable/acquisition/processing/review states and unknown do not become substantive absence. |
| Subject and scope | Pass for evaluated adapter controls. Organisation, division, program/service and endpoint broadening is rejected. |
| Cross-section leakage | Pass outside the classification blocker. §8/§13/§14, §4/§19 and other tested owners have no automatic propagation. |
| Temporal/current-state | Pass. `created_at` is record metadata and active positive adapters require explicit observation time. Historical evidence does not become current. |
| Missingness review-time versus observation-time | Pass. `CoverageInput` has no observation-time field and does not require a synthetic real-world date; positive observations retain their own time. |
| Epistemic basis | Pass outside the classification-authority blocker. Source fact, source interpretation, governed event, deterministic calculation and derived signal remain distinct. |
| Commitment lifecycle | Pass. Each supported lifecycle proposition requires action and object/result; commitment, claim, practice and completion remain separate predicates. |
| Relationships | Pass. Directed typed relationships retain resolved endpoints, role, scope and time; unresolved endpoints/shared domains cannot create an edge. |
| Taxonomy/adjudication | Fail. Source-report lifecycle vocabulary can look like CharityGraph effective adjudication. |
| Discovery signal | Pass. It is `derived_signal`, carries retrieval provenance, has unknown outcome state and cannot create CardEvidence. |
| Immutable public v0.5 | No candidate changes. The 349 artefact manifest remains the required immutable release check. |

## Residual decisions

The following are not gate blockers for a bounded card because current representation can state them honestly:

* §7 current availability/capacity: retained coverage can be unknown, unavailable, not processed or stale without claiming current availability or capacity.
* §12 non-operator relationship breadth: retained operator proof and typed architecture remain explicit; broader prevalence is empirical/scale work.
* §14 dependency assessment: no receipt, grant category, restriction or concentration measure creates a dependency assessment; an assessment policy remains future governance.
* §16 positive conduct evidence: absent retained conduct material remains coverage, never a clean-record assertion.
* §19 search quality: discovery-quality evaluation is production/scale work; retrieval does not become evidence.
* §20 freshness and correction/dispute material: a freshness policy is needed for current-state claims, and positive correction/dispute cases would extend empirical breadth. Neither forces a false bounded claim when represented as coverage/unknown.

Empirical-only residuals are cohort breadth, current capacity evidence, non-operator role prevalence, a positive correction/dispute case, and broader positive governance/workforce/relationship cases. Policy-only residuals are a current-state freshness policy and a dependency-assessment policy. Production/scale-only residuals are Top-100 scale, production freshness/correction workflows, discovery-quality evaluation and broader relationship prevalence.

## Validation

The C1–C9, integrated-card, direct-service, finance/funding, taxonomy/specialist, commitment/product-value, conduct, outcomes, relationship and persistence targeted selection completed without failures. The full Builder suite completed successfully in the known-good sibling topology. `git diff --check` passed on the frozen candidate before this record. Data link, UTF-8/mojibake/replacement-character, immutable-v0.5 manifest and exact 349 SHA/size checks remain required before any future merge; no public v0.5 artefact was changed by this record.

## Result and next repair

`PHASE5_NORTH_STAR_COMPLETION_GATE_FAIL`

The failure is caused by one known material representation defect: source-reported classification lifecycle status may imply CharityGraph effective-assignment endorsement. The candidate also lacks a materialised all-subject retained `IntegratedGraph`, so a future re-run must exercise the exact fixed-cohort cards after the lifecycle authority contract is repaired. No production repair, schema change, projection change, source addition, provider work, promotion, runtime mutation, public-v0.5 mutation, Top-100 work, Phase 6 work, PR merge, roadmap update, implementation-plan update, current-state update or Phase 5 completion declaration occurred in this gate run.
