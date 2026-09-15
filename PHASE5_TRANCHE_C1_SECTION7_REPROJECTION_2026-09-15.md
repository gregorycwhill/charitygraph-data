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

The companion bounded Builder implementation is
`87465a269db401f2ba4f5cab9aba7accc93f867b`.

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

## Cluster evaluation

| Section-7 cluster | Disposition | Retained basis and exact limit |
|---|---|---|
| Service offer/function and delivery evidence | SUPPORTED | A retained organisation-scoped service offer reprojects with locator, lineage and scope. It remains a service offer only. |
| Eligibility/referral/intake/access | SUPPORTED | Retained eligibility and access-pathway examples reproject as distinct types. This does not establish that clients are currently accepted. |
| Advertised versus current availability/hours | PARTIAL | The sole retained positive current-availability candidate lacks a time binding and is correctly rejected. No admissible positive current-availability/hours example remains. |
| Capacity/throughput/waitlist/constraints | PARTIAL | No positive `capacity_measure` appears in the 45 typed retained V1.2 propositions. The mechanical guard requires value, unit, scope and retained time before positive projection. |
| Unknown/unavailable/not-acquired/not-processed handling | KNOWABILITY_ONLY | Three sparse controls demonstrate scoped `NOT_PROCESSED`; the coverage contract preserves other non-positive states without asserting absence. |

## Section decision and residual gap

**Section 7 remains `PARTIAL`.** The reprojection closes the former
representation question for service offer, eligibility/access, scope, locator,
lineage, section versioning and honest `not_processed` coverage. It does not
supply an admissible retained positive current-availability example or any
positive capacity measure.

The exact residual is therefore not “more evidence needed”: it is the absence
from the authorised retained universe of (1) a temporally bound,
scope-appropriate current-availability statement and (2) a bounded capacity
measure with value, unit, time and scope. Existing organisation-scoped positive
examples also do not demonstrate program/service-scoped positive capacity.

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
