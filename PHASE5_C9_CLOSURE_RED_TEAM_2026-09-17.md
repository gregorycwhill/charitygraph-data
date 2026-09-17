# Phase 5 C9 closure red-team

**Status:** retained-evidence architecture review on the unmerged specialist campaign branch. This record does not declare Phase 5 complete or authorise Top-100, provider, source, runtime, public-v0.5 or Phase-6 work.

## Issues found and amendments

| Finding | Risk | Amendment |
|---|---|---|
| Specialist positives accepted only predicate/role/provenance metadata | A traceable observation could say no substantive WHAT | Activity, fundraising practice/campaign, ethos, affiliation, commitment, claimed implementation, observed practice and verified completion now require source-faithful substantive detail for supported positives. |
| Discovery signal used `source_fact` | Retrieval output could be treated as source truth | C6/C7 uses local `derived_signal`, requires method, signal type, query/profile and upstream artefact, remains non-effective, and cannot create CardEvidence. |
| All taxonomy statuses could become card evidence | Candidate/rejected/abstained/superseded could look like current classification | Audit history remains an observation. Only accepted and narrowed assignments are effective; narrowed means the stated narrowed concept/scope only. |
| Several adapters used `created_at` as `observed_at` | CharityGraph processing time could become a real-world date | C1-C8 active projection paths require explicit observation time. `created_at` remains record metadata. |
| C3/C5/direct-service roles could be positive without a WHAT | Type labels could masquerade as facts | Qualitative C3 roles, C5 role observations, and supported direct-service propositions now require substantive detail/value. Finance measures and typed statements retain their existing substantive requirements. |

## Decisions not to amend

No global epistemic taxonomy was introduced. `derived_signal` is limited to the specialist C6/C7 adapter because the defect occurs there. No workflow engine or taxonomy-history store was created: the bounded adapter preserves audit observations and filters effective card assignments.

No source-reported SDG statement is automatically duplicated. A source statement belongs to section 4 when it describes an activity/program lens. An independently governed assignment belongs to section 19. Two views require two explicit propositions or explicitly authorised projection behaviour; neither is inferred from the other.

## Adversarial controls

The C9 suite rejects role-only activity, fundraising, ethos and lifecycle claims; commitment timing without an action/object; naked classifications; non-effective taxonomy states as card content; discovery score as evidence; created-at fallback; source silence or processing failure as absence; scope broadening; historical-as-current presentation; parent ethos on a child; newer source as correction; unresolved endpoint; and shared-domain relationship inference.

## All-section readiness matrix

| Section | Representation | Empirical state | Policy state | Scale state |
|---:|---|---|---|---|
| 1 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 2 | REPRESENTATION_PROVEN | positive retained case available | no additional policy needed | bounded only |
| 3 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 4 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 5 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 6 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 7 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | no positive retained capacity case | bounded policy needed for current-state claims | bounded only |
| 8 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 9 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 10 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 11 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 12 | REPRESENTATION_PROVEN | positive operator case available; other roles architecture-only | no additional policy needed | production breadth residual |
| 13 | REPRESENTATION_PROVEN | partial retained breadth | no additional policy needed | bounded only |
| 14 | KNOWABILITY_REPRESENTATION_SUFFICIENT | partial retained breadth | bounded policy needed for dependency assessment | bounded only |
| 15 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 16 | KNOWABILITY_REPRESENTATION_SUFFICIENT | no positive retained case | no additional policy needed | bounded only |
| 17 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth | no additional policy needed | bounded only |
| 18 | REPRESENTATION_PROVEN | positive retained case available | no additional policy needed | bounded only |
| 19 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | partial retained breadth; no quality result | production policy only | production/scale residual |
| 20 | REPRESENTATION_PROVEN_WITH_BOUNDED_FIX | no positive correction/dispute case | bounded policy needed only for current-state freshness claims | production/scale residual |

## Residual decision

Freshness policy does not block bounded completion: a card may state observation/reporting time and stale or unknown freshness without claiming current state. Positive correction/dispute material does not block bounded completion: typed representation, adversarial proof and explicit no-positive-case coverage prove the bounded contract. Relationship breadth does not block section 12 representation because the directed typed contract and real operator control prove the common mechanics; role semantics remain architecture-only where no retained case exists. Section 16 does not require misconduct to pass. Section 7 may retain unknown availability/capacity. Section 14 may state source facts and absence of a dependency-assessment rule. Section 19 search-quality measurement is a later product/scale evaluation.

Remaining residuals are empirical (breadth, correction/dispute example, role prevalence, current capacity), policy/governance (freshness for current-state claims and dependency assessment), or scale/production (search-quality evaluation, production freshness and broader cohorts). No known material representation defect remains.

**Readiness:** `READY_FOR_REAL_COMPLETION_GATE`.
