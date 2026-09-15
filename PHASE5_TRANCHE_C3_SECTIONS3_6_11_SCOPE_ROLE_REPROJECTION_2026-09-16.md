# Phase 5 Tranche C3 — §§3/6/11 retained-evidence scope/role reprojection

**Status:** completed bounded retained-corpus architecture and semantic review

**Projection:** `north-star-v0.2` only

**Authority:** This records a retained-evidence review and deterministic representation decision. It does not acquire sources, run a provider, promote candidates, change public v0.5, or establish current operational facts.

## 1. Boundary and starting point

The review started from Builder `21b30eea9c606e1d52d0ee6ae87cf175032c483d` and Data `fcd06a0677078383121e1afd0fc349fd56368fc3`. C1 (§7) and C2 (§14) were complete. Historical outputs, including v0.1 numerical labels, were inspected as retained evidence and never treated as active section assignments.

The question was whether retained evidence can be assigned to §§3, 6 and 11 without conflating program identity, participation, service capacity, scale, and capability. The answer is bounded: existing generic primitives preserve envelopes, but a small v0.2 predicate adapter is needed to preserve the semantic role and to make non-propagation mechanical.

## 2. Frozen retained cohort

The cohort was frozen before adjudication. It is deliberately small and includes positive and adverse cases.

| Subject / retained artefact | Why included | Bounded use |
|---|---|---|
| Australian Red Cross Society, ABN `50169561394`; `archive/processed/reality-spike/2026-08-10/report-extracts/50169561394-2022-23.json`, pp. 2–5, SHA `c4f75bf25ad3481d964057cc4def56bcd23a5cf5e0b88bad616859cd8f6cb8d3`; retained volunteer page `web-extracts/50169561394-2026-08-10.json` | Operating division versus program; opportunity, eligibility, mixed participation total, volunteer hours, workforce scale and scheme counterexample | Lifeblood is an operating division, not a program; page opportunity is not participation; counts retain their mixed population and period |
| Merri Creek Management Committee, ABN `13025599242`; retained web extract `web-extracts/13025599242-2026-08-10.json`, source file `e246624d86adc352d86836d6749193ac86c078ce3e661233b531bbbfd8494b03.html`; FY2024–25 report `report-extracts/13025599242-2024-25-full.json`, pp. 3, 6, SHA `e8523d9595a9a7c354298d667de369b980c12f4fc3459bc222808d8e86cc0252` | Named WaterWatch scope, coordination versus ownership, opportunities, workshop/survey episodes and shared-page attribution | MCMC coordinates WaterWatch in named catchments; it does not prove ownership or operation of every group/event on a shared page |
| Fitted for Work, ABN `78126256862`; FY2023–24 report `report-extracts/78126256862-2023-24-full.json`, pp. 9–10, SHA `ce225c4ca50abb663922ed2eba272dbac6627d779e611ba8213f96a133adf4dd` | Service labels and reported delivery counts versus durable identity, participation or capability | Client and service-instance totals remain historical recipient/output measures; HRIS investment is a resource fact |
| Bush Heritage Australia; source-only packet `archive/processed/phase6-outcomes-independent-review-2026-09-13-private-v3/condition-a-source-only/outcomes__78053639115.json`, AIS locator `locator:a514be10970040a2e18c0e51cbdab8a73d835c2070f4a41e20fd5ab7ff3525f6`, source `srcrec:7cb70d6c23be8e1003453ff5db1c627f9af0c0ff6ca31a396c4d9a7804af2d63`; annual-report locator `locator:a975b4943f90fa686d4d96791819ea1fb30e5655ed19feba12426dd07c8bb362`, pp. 3–5 | Source-listed program scopes; FY2024 workforce numbers; resource/scale measures; first-party capability language | Named AIS programs remain non-durable scopes; FTE/headcount and resource quantities are measures, while `leading` / `best science` remain attributed claims |
| C1 §7 decision record `PHASE5_TRANCHE_C1_SECTION7_REPROJECTION_2026-09-15.md` | Capacity-to-capability adverse control | It records no retained positive capacity case; its synthetic fixture proves architecture only and cannot become §11 evidence |

The Red Cross benchmark `cohort/scoped_benchmark_v2.json` cases `sbv2:red_cross:lifeblood:Lifeblood` and `sbv2:red_cross:lifeblood-as-program:Lifeblood as ordinary program` is a retained counterexample, not a new source.

## 3. Primary Terra inventory

Terra reviewed 26 material propositions and controls: **11 `ACCEPT`, 8 `NARROW`, 5 `REJECT`, 2 `KNOWABILITY_ONLY`**. These are review dispositions, not governed knowledge promotions.

### §3 Programs / services

- Bush Heritage FY2024 AIS named `Programs[]`: `NARROW` to source-native program scopes. They do not create durable program subjects, prove current delivery, or prove ownership.
- ARC Lifeblood: `REJECT` as a program. Annual-report p. 2 describes it as an operating division. Its facts stay at an historical division scope and cannot propagate to the whole Society.
- MCMC WaterWatch: `NARROW` to a named scope and source-attributed coordination statement. No durable subject, ownership or operator relation is established.
- Fitted service-table rows: `NARROW` to FY2024 source-reported service scopes/output labels. Generic job-readiness activity is `REJECT` as durable service identity.

### §6 Participation

- ARC volunteer page: `ACCEPT` only as an advertised opportunity, named roles and stated eligibility. It is no count or episode.
- ARC annual p. 4: `18,450 members and volunteers` is `ACCEPT` only as a FY2023 mixed-population aggregate. It is not a volunteer count. `4,000 hours of support from volunteers` is `ACCEPT` as contribution-hours, not people or episodes.
- MCMC p. 6: approximately 50 partner representatives at workshops and approximately 200 survey responses are `ACCEPT` as historical, episode-scoped measures. Partners are not relationship endpoints or volunteers by implication.
- Fitted `2,605` clients and `6,502` services are `REJECT` for §6: recipients and service instances are not participation.
- ARC ACFID Code signatory status is `REJECT` for §6: it is scheme/accreditation context.

### §11 Scale / capability

- ARC `1,639 staff` and Bush Heritage FY2024 162.97 FTE / 131 full-time / 52 part-time / 544 unpaid volunteers are `ACCEPT` as direct organisation-scale measures only. A §10 workforce view requires an independently explicit projection; neither count proves capability.
- Bush Heritage land/project/paper quantities and Fitted's HRIS investment are `ACCEPT` as bounded resource/infrastructure facts, never scores or effectiveness evidence.
- Bush Heritage `leading` / `best science` and ARC `world-class blood service` are `NARROW` to first-party qualitative capability claims with source-interpretation basis. No CharityGraph capability judgment is supported.
- Financial size, age, recipient/output totals and C1 service capacity are `REJECT` as organisational capability. There is `KNOWABILITY_ONLY` evidence for any CharityGraph-assessed qualitative capability and for a positive retained C1 service-capacity example.

## 4. Adversarial Terra review and changes

A separate Terra pass attempted to falsify assignments using the cohort. It returned a **conditional go** and required two changes:

1. WaterWatch changed from a proposed coordinator role to `coordination_source_reported`: the retained page supports MCMC coordination at a named scope, but neither ownership nor an operator/ownership `RelationshipStatement`.
2. Lifeblood changed from a possible program-like scope to a non-durable `other` scope carrying the explicit `operating_division` role and FY2023 time. It is not a program or a new subject.

The review additionally required closed predicate-to-section mapping, positive-evidence time/source/locator/lineage binding, separate missingness, combined-population preservation, and hard rejection of scheme membership, recipient/output, §7 capacity and v0.1 numerical mappings. It found no basis to alter the other primary dispositions.

## 5. Representation inventory and implementation decision

| Concept | Classification | Decision |
|---|---|---|
| §3 child scope and parent organisation | `ALREADY_EXPLICITLY_REPRESENTABLE` | `ScopeRecord` plus `Observation`; no subject promotion is implied |
| Durable program/service identity | `ALREADY_EXPLICITLY_REPRESENTABLE` | `ProgramCandidate` followed by governed promotion, which C3 does not perform |
| Ownership | `NOT_EXPLICITLY_REPRESENTABLE` | Controlled relationship roles omit ownership; do not infer or add it |
| Division scope | `AMBIGUOUS` | Preserve Lifeblood as `other` plus explicit v0.2 `operating_division` role; no generic-contract change |
| §6 opportunity and aggregate measure | `ALREADY_EXPLICITLY_REPRESENTABLE` | Direct Service V1.2 has related types, but historical assignment cannot be numerically reused |
| §6 role, episode, participant category and contribution-hours | `NOT_EXPLICITLY_REPRESENTABLE` | New v0.2 predicates retain these distinctions |
| §6 scheme exclusion | `ALREADY_EXPLICITLY_REPRESENTABLE` | Existing scheme type is explicitly non-projectable to §6 |
| §11 raw value/time/evidence | `REPRESENTABLE_WITH_EXISTING_GENERIC_PRIMITIVE_WITHOUT_LOSS` | Existing `Observation` envelope is reused |
| §11 scale/resource/attributed-capability roles | `NOT_EXPLICITLY_REPRESENTABLE` | New v0.2 predicates preserve the role and claim basis |
| §7 separation | `ALREADY_EXPLICITLY_REPRESENTABLE` | C1 remains §7-only and no C3 predicate accepts capacity |

Builder adds a small deterministic adapter over `Observation`, `CardEvidence` and `CoverageInput`, not a domain mega-record. Its closed predicates project to one section only: program/service scope, coordination or operating division to §3; opportunity, role, episode, aggregate measure or contribution-hours to §6; scale measure, resource fact or attributed capability claim to §11. Positive inputs require exact scope, source role, locator, source record, lineage and time. The adapter has no predicate for recipients, outputs, scheme/accreditation, capacity, ownership, a capability assessment or v0.1 assignment.

## 6. Cluster and overall dispositions

| Section | Clusters | Overall |
|---|---|---|
| §3 | scope identity `SUPPORTED`; subject/promotion `PARTIAL`; ownership/operator `KNOWABILITY_ONLY`; lifecycle/current delivery `PARTIAL`; missingness `SUPPORTED` | `PARTIAL` |
| §6 | opportunity `SUPPORTED`; role/episode `PARTIAL`; aggregate measure `SUPPORTED`; volunteer/member distinction `SUPPORTED`; missingness `SUPPORTED` | `PARTIAL` |
| §11 | quantitative scale `SUPPORTED`; resource/infrastructure `SUPPORTED`; source-attributed qualitative claim `SUPPORTED`; assessed capability `KNOWABILITY_ONLY`; §7 separation `SUPPORTED` | `PARTIAL` |

## 7. Residuals

**Representation residuals:** ownership remains absent from controlled relationship roles; `ScopeRecord` has no dedicated operating-division kind, retained here through explicit v0.2 role on `other`; no governed capability-assessment rule exists. These are not silently filled with free text.

**Empirical residuals:** the cohort contains no evidence establishing a durable independent program identity, MCMC ownership of WaterWatch, current delivery from historical service labels, a pure ARC volunteer headcount, a positive retained C1 capacity measure, a viable capability score, or a CharityGraph qualitative-capability assessment.

**Product/governance residuals:** future durable program promotion, a dedicated operating-division scope kind, ownership semantics, a current-delivery policy, and any capability assessment require separate authority. None is decided here.

## 8. Outcome and boundaries

Scope/role conflations were found and corrected in the design: division/program, coordination/ownership, opportunity/episode, mixed member-volunteer total/volunteer count, recipient/output/participation, workforce/participation, scale/capability and service-capacity/organisational-capability. No retained evidence justifies a CharityGraph qualitative capability conclusion. C1 §7 capacity is explicitly excluded from §11.

Provider calls: `0`. Source acquisitions: `0`. Semantic provider executions: `0`. Candidate generation: `0`. Promotions: `0`. Canonical runtime mutations: `0`. Top-100: `0`. Phase 6 reopening: `0`. §13 finance tranche: not started.

## 9. Recommended product-owner decision

Accept the bounded §§3/6/11 projection vocabulary and retain all three sections as `PARTIAL`; choose later whether any empirical expansion is worth authorising to test durable identity, current delivery, dedicated division semantics or a governed capability assessment. No such follow-on is started by this record.
