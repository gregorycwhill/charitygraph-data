# Phase 5 Tranche C1 — North Star v0.2 section 7 retained-evidence reprojection

**Status:** Completed bounded retained-evidence reprojection; no execution authority.
**Date:** 15 September 2026. **Active projection:** `north-star-v0.2`.

## Question and boundary

This tranche answers whether already retained evidence can be projected into
section 7, *Direct service / capacity*, without converting a service offer,
eligibility or access statement into current availability or capacity. It is a
deterministic reprojection test. It does not reopen Phase 6 Capacity, acquire a
source, call a provider, generate candidates, or promote knowledge.

The starting commits were Builder
`23a937711f034a6691e4b144833d0199eecfe818` and Data
`23212d916363b539e4e4f9cd7274eccdcdcb0511`. The historical v0.1 section
numbers were not used as mappings: every new assignment explicitly names
`north-star-v0.2` section 7.

## Retained evidence universe

| Retained artefact | Availability and use |
|---|---|
| Direct Service V1.2 final report | Available locally at the recorded runtime location; SHA-256 `588707746dee2de90a14ed099d13235a34d3b18bf88e9f43008c22712c047777`. It records 14 completed V1.2 responses, 49 retained propositions and zero V1.2 section/type violations. |
| V1.2 standard result records | 13 locally retained result files plus the retained corrected canary interpretation. The 13 response records contain 45 `capability_access_availability` propositions: 25 `service_offer`, 3 `eligibility`, 16 `access_pathway`, one `current_availability`, and zero `capacity_measure`. |
| Corrected canary interpretation | Available locally; records three directly-valid V1.2 capability/access/availability propositions, but its compact retained interpretation does not add a positive capacity finding. |
| Product-value sparse controls | [Product-value adjudication](docs/history/product-value-adjudication-and-evaluation-2026-09-14.md) retains scoped `not_processed` states for St George Community Housing, RFDS Queensland and the Leukaemia Foundation. |
| Phase 6 coverage contract | [Phase 6 closeout](docs/history/phase6-closeout-2026-09-14.md) preserves finite-universe `not_processed`, `source_silent`, `source_unavailable`, `not_acquired`, `processing_failed` and `unknown` distinctions. |

Raw provider payloads remain outside Git. This record uses only opaque request,
scope, locator and artifact identifiers plus aggregate results.

## Fixed cohort and reproducible replay

The cohort was fixed before evaluation and was not expanded to seek a preferred
answer.

| Cohort member | Retained item exercised | Result |
|---|---|---|
| V1.2 `requestitem:365bfdbe130e7ae396ae75aaab8deb1ec05d72103cbbf1a60076896e1fc6de02` | Supported organisation-scoped service offer with an evidence locator | Reprojects to v0.2 section 7 only. |
| V1.2 `requestitem:a866913def4eec7875a3e079fd3dbf08f55a3c4b8f87909642242fd52ee0ad3f` | Supported organisation-scoped eligibility and access-pathway items; its supported current-availability item has no retained temporal binding | Eligibility and access reproject independently. Untimed availability fails closed and is not projected positively. |
| St George Community Housing | Scoped service availability/capacity/eligibility `not_processed` coverage | Preserved as section-7 `NOT_PROCESSED`, never silence or unavailability. |
| RFDS Queensland | Scoped section-specific service availability/capacity/eligibility `not_processed` coverage | Preserved as section-7 `NOT_PROCESSED`; Queensland scope remains distinct from national RFDS. |
| Leukaemia Foundation | Scoped service availability/capacity/eligibility `not_processed` coverage | Preserved as section-7 `NOT_PROCESSED`. |

The deterministic harness is
`pytest -q tests/contracts/test_section7_reprojection.py` in Builder. It uses
compact fixtures derived from retained opaque V1.2 IDs and locators; it does not
read, copy, or transmit raw payload text. Four retained propositions and three
retained coverage states are directly exercised. The aggregate 45 typed V1.2
propositions were inspected solely to establish the retained-evidence
distribution above.

The companion bounded Builder implementation began at
`87465a269db401f2ba4f5cab9aba7accc93f867b` and is amended by the v0.2-only
predicate repair at `288e545e999a4b0cf86459fa82120f28f79416f9` and the
governed-observation binding repair at
`cf7d27a9de4474792edb72b5d8467f207db44e40`.

## Mechanical reprojection result

The bounded Builder helper
`charitygraph.section7_reprojection` accepts only the five Direct Service
types that belong to section 7. It assigns each accepted item explicitly to
`north-star-v0.2` section 7 and produces no automatic section-11 assignment.

| Required assertion | Result |
|---|---|
| Active contract is explicit | Pass: assignments are `north-star-v0.2` / section 7. |
| v0.1 numerical equivalence is not reused | Pass: historical v0.1 section 7 remains empty for the C1 fixture. |
| Service offer is not availability or capacity | Pass: type remains `service_offer`. |
| Eligibility and access are independent | Pass: each retains its original typed proposition. |
| Positive availability is time-bound | Pass: the one retained positive availability candidate has no time and fails closed. |
| Positive capacity requires value, unit, scope and retained time | Pass mechanically; no retained positive capacity item exists. |
| Missingness stays non-negative | Pass: `not_processed` compiles as finite-universe coverage with no observation IDs. |
| Locator, source lineage and scope survive | Pass: the replayed item retains opaque locator, source-record reference and organisation scope. |
| Section 7 does not duplicate into section 11 | Pass: section 11 has no assignment from the replay. |
| Historical v0.1 remains unchanged | Pass: the replay produces no v0.1 assignment. |

The helper is a representation guard. It does not make V1.2 output governed
knowledge, alter historical output, or establish live directory information.

## Representation inventory and v0.2-only repair

This inventory was performed against current Builder contracts before the
repair. `DirectServicePropositionType` and the V1.2 wire contract remain
historical: neither has been changed, and no retained V1.2 response has been
relabelled.

| v0.2 §7 distinction | Inventory result before this amendment | Existing primitive assessed | C1 result |
|---|---|---|---|
| Advertised availability | `NOT_EXPLICITLY_REPRESENTABLE` | Historical `current_availability` is a different V1.2 role; a generic observation predicate would not establish an explicit §7 role. | New explicit `advertised_availability` predicate. |
| Operating hours | `AMBIGUOUS` | Historical Phase 6 `AccessInformation(service_hours)` preserves text but is a slice DTO, not a v0.2 projection predicate with §7 identity. | New explicit `operating_hours` predicate. |
| Throughput | `AMBIGUOUS` | Historical Phase 6 capacity DTO includes `maximum_throughput`, which conflates throughput with capacity for this purpose. | New explicit `throughput` predicate requiring value and unit. |
| Waitlist status/measure | `AMBIGUOUS` | Historical Phase 6 availability can carry `waitlisted`, but cannot distinguish a waitlist state from a waitlist measure in the active projection. | New explicit `waitlist` predicate; optional measure remains distinct from capacity. |
| Staffing constraint | `NOT_EXPLICITLY_REPRESENTABLE` | Workforce measures can record FTE/headcount but not a constraint as a distinct §7 semantic role. | New explicit `staffing_constraint` predicate. |
| Other resource constraint | `NOT_EXPLICITLY_REPRESENTABLE` | Resource measures can record resources but not a constraint as a distinct §7 semantic role. | New explicit `resource_constraint` predicate. |
| Delivery evidence | `NOT_EXPLICITLY_REPRESENTABLE` | `service_offer`/`ServiceExists` describe a service; neither establishes delivery evidence. | New explicit `delivery_evidence` predicate. |

The repair is a compact v0.2 predicate vocabulary in
`charitygraph.section7_reprojection`, not a service mega-record and not a
semantic extractor. Each supported future predicate carries subject, lowest
supported scope, source role, locator IDs, source-record IDs, lineage IDs,
observation time, coverage state and `north-star-v0.2` assignment. Existing
`ObservationTime`, scope, `CardEvidence` and `CoverageInput` primitives are
reused without loss. The added predicates cannot become current availability,
capacity, service offer or section 11 merely through projection.

The vocabulary is now proven through the governed path, not just as a DTO:
`Section7V02ProjectionInput` deterministically creates an append-only
`Observation`, whose predicate and value preserve the v0.2 role, provenance,
time, coverage and freshness qualification. `CardEvidence` accepts that
created observation object only after checking subject, scope, predicate,
time, locators, source-record IDs, lineage and deterministic method. The
integrated tests pass representative advertised availability, throughput,
staffing constraint and delivery evidence observations through `IntegratedGraph`
and the active North Star projection. They appear only in v0.2 §7, not §11 or
historical v0.1. An unrelated observation is rejected at the binding check.

The prior architectural gaps for these seven distinctions are therefore
closed through the integrated governed-observation path. This is architecture
evidence only: the synthetic tests below are not retained empirical evidence
and do not create positive §7 findings.

### Freshness boundary

An observation time records when availability or another time-sensitive fact
was observed or reported. It does not make the fact fresh today. The v0.2
predicate vocabulary records `unassessed`, `stale`, or `fresh` separately; a
`fresh` state requires an explicit policy ID. No canonical North Star v0.2
freshness interval or policy was found. The historical owner-approved Phase 6
availability policy is not adopted here. Freshness policy remains a Section 20
governance issue, and C1 makes no fresh-current claim.

## Cluster evaluation

| Section-7 cluster | Disposition | Retained basis and exact limit |
|---|---|---|
| Service offer/function and delivery evidence | PARTIAL | A retained organisation-scoped service offer reprojects with locator, lineage and scope. It remains a service offer only; delivery evidence is now explicitly representable but has no retained positive example. |
| Eligibility/referral/intake/access | SUPPORTED | Retained eligibility and access-pathway examples reproject as distinct types. This does not establish that clients are currently accepted. |
| Advertised versus current availability/hours | PARTIAL | The sole retained positive current-availability candidate lacks a time binding and is correctly rejected. Advertised availability and hours are now explicit predicates, but no retained positive examples exist. |
| Capacity/throughput/waitlist/constraints | PARTIAL | No positive `capacity_measure` appears in the 45 typed retained V1.2 propositions. Throughput, waitlist and staffing/resource constraints are now explicit predicates, but no retained positive examples exist. |
| Unknown/unavailable/not-acquired/not-processed handling | KNOWABILITY_ONLY | Three sparse controls demonstrate scoped `NOT_PROCESSED`; the coverage contract preserves other non-positive states without asserting absence. |

## Section decision and residual gap

**Section 7 remains `PARTIAL`.** The reprojection and repair close the
architecture/representation gaps for all stated v0.2 §7 distinctions, while
preserving historical V1.2 and v0.1 meaning. They do not supply an admissible
retained positive current-availability example, positive capacity measure, or
positive retained examples for advertised availability, hours, throughput,
waitlist, constraints or delivery evidence.

The residual is two separate things. The **representation residual is closed**:
the seven formerly absent or ambiguous roles now have explicit v0.2 predicates.
The **empirical residual** is absence from the authorised retained universe of
(1) a temporally bound, scope-appropriate current-availability statement, (2)
a bounded capacity measure with value, unit, time and scope, and (3) positive
examples for the other newly explicit roles. Existing organisation-scoped
positive examples also do not demonstrate program/service-scoped capacity.

No provider call or source acquisition would add decision-relevant information
*within this authorised reprojection*. The next decision is for the product
owner: decide whether this honest partial result is sufficient for the later
bounded North Star gate, or whether a future naturally retained evidence cohort
should be separately authorized to test those two positive evidence conditions.
No such work is authorized by this record.

## Boundaries and validation

This tranche made **0** provider calls, source acquisitions, semantic
executions, candidate generations, promotions, runtime mutations, Viewer
changes, public-v0.5 changes, Top-100 executions and Phase 6 reopenings. It did
not start any later Tranche C action.
