# CharityGraph Builder-to-65k plan on a page

**Status:** Canonical active plan and progress scorecard
**Version:** 1.1
**Scope:** Builder-to-65k production-readiness path; complements, and does not replace, product, semantic, source-governance or release authorities.

This is the one canonical plan-on-a-page for Builder progress toward an accepted
full-population run across approximately 65,000 Australian charities. It is the
authoritative scorecard and high-level activity plan for future development
sessions. `DOCUMENT_AUTHORITY.md` records its precedence and relationship to
`CURRENT_STATE.md`, `ROADMAP.md` and `DEVELOPMENT_METHOD.md`.

## Objective and endpoint

Build a trustworthy, governed Builder that can execute and accept the full
approximately 65k Australian charity/corpus run. The 100% endpoint is the
accepted full-population Builder/corpus run. Public distribution,
commercialisation and ecosystem growth are downstream outcomes and are outside
this scorecard.

Progress is earned only when a gate closes against its exit evidence. Work on a
later stage may proceed opportunistically when it does not distract from the
active dependency path, but earns no percentage until that gate closes.

**Current position: Gate 1 CLOSED; Gate 2 ACTIVE; 12% complete / 88% remaining.**

Source Universe v1 is a documentation prerequisite for Gate 2, not Gate 2
evidence and not fractional progress. Its seven admitted routine Builder
families and bounded acquisition rules are canonical in
`SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md`.

## Supervisory spine and gate state

The durable supervisory chain is **product objective -> 65k gate/evidence state -> tranche -> run/campaign/tasks -> handoff evidence -> semantic review -> Product Owner/Sol gate decision -> next tranche**. This plan is the canonical definition of that chain; bridge documents describe transport and execution only.

Each gate is `OPEN`, `ACTIVE`, `CLOSED`, or `REOPENED`. Exactly one normal critical-path gate is `ACTIVE`; later-gate work may accumulate evidence opportunistically but cannot earn progress. Earned progress is the fixed sum of weights of `CLOSED` gates only: there is no fractional activity credit. A gate cannot close while a critical dependency or exit-evidence item remains unsatisfied. A materially invalidated closed gate may be `REOPENED`; its weight is immediately removed from earned progress until it is closed again. The live state remains **Gate 1 CLOSED; Gate 2 ACTIVE; 12% earned; 88% remaining**.

The contract-level gate-evidence ledger records, per gate: satisfied exit evidence; outstanding exit evidence; invalidated or weakened evidence; supporting tranche/run references; closure recommendation; closure decision; closure authority; and decision date. This is a documentation contract only: the runtime does not yet store or enforce this ledger.

Work is classified as `gate_advancing`, `enabling`, `maintenance`, `incident`, or `publication`. Gate-advancing and enabling work name their gate and exit-evidence target. Maintenance, incident, and publication work earns zero product progress unless it directly satisfies an already-defined gate exit criterion.

The intended future tranche `progress_context` is: `gate_id`, `gate_title`, `critical_path_dependency`, `exit_evidence_target`, `expected_product_delta`, `earned_progress_before`, `closure_authority`, and `work_class`. It is not part of the current runtime schema; subsequent harness propagation must add or version runtime support and enforcement explicitly.

## Tranche, handoff, review, and publication contract

A tranche is the authorised outcome/product-intent unit. One substantial Luna run is the default for settled coherent implementation. A campaign is justified only by genuine dependencies, independent work products, mixed model routing, restart boundaries, or valuable uncertainty reduction. Child tasks are execution decomposition, never independent product authority. Children may recommend successors, but cannot change the active gate, close or reopen a gate, admit a source class, publish, or enqueue successors.

Tranche aggregation and semantic review must answer what gate-relevant evidence was added, what prior evidence was weakened or invalidated, which exit criteria remain unsatisfied, and the recommended disposition: `NO_CHANGE`, `READY_FOR_REVIEW`, `DECISION_REQUIRED`, or `REOPEN_RECOMMENDED`. The semantic lifecycle is `AUTHORISED -> EXECUTING -> EXECUTION_COMPLETE_PENDING_REVIEW -> ACCEPTED | PARTIAL | REJECTED | DECISION_REQUIRED`. Bridge/Codex `COMPLETE` is process evidence only and is not semantic acceptance.

Canonicality is separate from acceptance and has exactly these states: `LOCAL_ONLY`, `PUBLICATION_CANDIDATE`, and `CANONICAL_PUBLISHED`. No current runtime claim should imply that these states are stored or enforced.

Gate closure is conservative. Product, semantic, and source-policy gates require Greg's explicit Product Owner decision after Sol's recommendation. Operational closure may be delegated to Sol certification only later, and only after Greg explicitly approves objective closure criteria and the delegation. Luna, Terra, Codex, and harness execution may never close or reopen a gate autonomously. A source-policy gap is `DECISION_REQUIRED`, not permission for autonomous acquisition or source-class admission.

`status` leads with 65k progress, active gate, active tranche, satisfied and outstanding exit evidence, decision owner, and canonicality before transport telemetry. `propose` derives one highest-value tranche from unresolved active-gate exit evidence and does not dispatch it. `continue` pursues the authorised tranche to a real decision, global-stop, or execution-review boundary; after execution completion it performs or requests semantic review and never silently starts a successor.

## Fixed weighted scorecard

| Gate | Weight | Concise closure condition |
|---|---:|---|
| 1. Product and semantic contract | 12% | Product boundary, North Star, semantic-losslessness and least-specific-defensible-truth contract are accepted. |
| 2. Source and evidence sufficiency | 13% | The admitted source/evidence universe is sufficient for the agreed claims across representative charities, with gaps and limits explicit. |
| 3. Governed knowledge quality | 15% | Quality is evidenced against a bounded human/reference set and expanding Semantic Demand tests, with corrections and missingness governed. |
| 4. Builder industrialised | 20% | Model/cost routing, batch execution, concurrency, restart/resume, idempotence, scheduling, monitoring, failure isolation and cost telemetry are evidenced. |
| 5. Representative 30-charity pilot | 5% | Accepted pilot covers 10 Top100 + 10 Top1,000 + 10 Top10,000, including deliberately awkward cases. |
| 6. Analyst consumption surface | 5% | Analysts can use the governed output through a usable, inspectable consumption surface. |
| 7. Real-user validation | 8% | Real users validate the surface and material findings have an accepted disposition. |
| 8. Scale and right-tail proof | 10% | Progressive approximately 100 -> 1,000 -> 10,000 runs evidence right-tail quality, cost, throughput and operational limits. |
| 9. Production corpus operations | 7% | Manifests, durable storage, stable IDs, releases/versioning, refresh/change detection, correction lifecycle and observability are ready. |
| 10. 65k production run accepted | 5% | The approximately 65k full-population Builder/corpus run executes and is accepted against the agreed evidence. |
| **Total** | **100%** | **Accepted full-population Builder/corpus run** |

## High-level activity sequence and unlocks

The activity plan is distinct from the scorecard: it describes dependencies and
decisions that can earn gate closure; it does not itself earn credit.

1. **Close the product/semantic contract.** Dependency: approved North Star,
   semantic-losslessness and least-specific-defensible-truth boundaries.
   Unlock: Gate 1 closure and the claims/evidence contract for Gate 2.
2. **Prove approved-source/evidence sufficiency.** Work across representative
   charities inside the closed-by-default Builder source universe. Open-web
   evaluation is permitted only as Product Owner reconnaissance for candidate
   source classes; only the Product Owner may admit a new source class. Unlock:
   accepted Gate 2 evidence and the governed quality test set.
3. **Prove governed knowledge quality.** Use a bounded human/reference set and
   expanding Semantic Demand tests, with provenance, missingness, correction
   and review boundaries explicit. Unlock: Gate 3 closure and a trustworthy
   production-like sample path.
4. **Industrialise Builder.** Evidence model/cost routing, batches,
   concurrency, restart/resume, idempotence, scheduling, monitoring, failure
   isolation and cost telemetry. Unlock: Gate 4 closure and repeatable sampling.
5. **Produce the representative 30-charity pilot.** Run 10 Top100, 10 Top1,000
   and 10 Top10,000 charities, including awkward cases. Dependency: Gates 1-4.
   Unlock: Gate 5 closure and the representative corpus needed by Gate 6.
6. **Expose the analyst consumption surface.** Dependency: the accepted pilot
   corpus and governed outputs. Unlock: Gate 6 closure and usable workflows for
   real-user validation.
7. **Conduct real-user validation.** Dependency: Gates 5 and 6. Feed material
   findings back into earlier gates; such findings may reopen Gates 1-6.
   Unlock: accepted validation and Gate 7 closure.
8. **Scale and prove the right tail.** Progress approximately 100 -> 1,000 ->
   10,000, measuring quality, right-tail behaviour, cost and throughput.
   Dependency: accepted validation. Unlock: Gate 8 evidence.
9. **Prepare production corpus operations.** Finalise manifests, durable
   storage, stable IDs, releases/versioning, refresh/change detection,
   correction lifecycle and observability. Dependency: Gate 8 evidence. Unlock:
   Gate 9 closure.
10. **Execute and accept the approximately 65k production run.** Dependency:
    Gate 9. Unlock: Gate 10 closure and 100% completion.

The dependency spine is therefore **1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 ->
9 -> 10**, with the explicit feedback loop from real-user validation back to
any materially affected earlier gate. Opportunistic later-stage work remains
non-credit-bearing until its gate closes.

## Anti-drift and session grounding

Preserve North Star v0.3, semantic-losslessness, least-specific-defensible
truth, Product-Owner-only source-class admission, and the closed-by-default
Builder evidence universe. Do not turn a source gap into permission to search,
acquire or admit a source class. Do not create a detailed backlog here or use
this plan to introduce product semantics.

Every future development tranche/campaign must state:

- the current gate it advances;
- the exit evidence it is intended to produce;
- its dependency on prior work; and
- its expected product delta.

The next tranche is selected from **current gate -> earned progress -> unresolved exit evidence -> next highest-value tranche**. This is the standing North Star and Builder-to-65k grounding rule for future sessions.

Each session must ground itself in this canonical plan and report **current
gate, earned progress, unresolved exit evidence and next highest-value
tranche**. Work not traceable to the active gate or dependency path is
presumptively backlog/tangential. `CURRENT_STATE.md`, `ROADMAP.md` and
`DEVELOPMENT_METHOD.md` may provide context, but this document is the sole
Builder-to-65k scorecard and activity-plan authority.
