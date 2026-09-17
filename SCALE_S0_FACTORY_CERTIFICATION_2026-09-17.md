# Scale S0 Factory certification — 17 September 2026

**Status:** offline Factory certification record. No mandate is approved, no S0
population is selected, and this record authorises no source acquisition,
provider transmission, semantic execution, promotion, publication, merge, or
Phase 6 work.

## Historical chronology and durability repair

The preceding certification at Builder
`58e9465ee2518b35a4dd2dd63c7ea049ed22e4a8` and Data
`16c5bf73404a93b6111cf4d6e9c9bb1788adc714` recorded
`S0_FACTORY_CERTIFICATION_INCONCLUSIVE`. Its specific blocker was that the
mandate, frozen packet, semantic candidate, review identities, and promotion
state were guard inputs only. A fresh process could not reconstruct the
authority needed to make the same send/no-send or promotion decision.

This repair retains the existing canonical stores for physical provider
attempts/requests/responses, reservations/accounting, durable halts, and
governed observations. Migration 17 adds only the missing Scale S0 authority
records: immutable mandate snapshots, frozen packet identities, immutable
candidate bindings, review items, append-only decisions, and promotion
authorisation/result references. These records contain control-plane material
and hashes, never source bodies, provider responses, credentials, or a second
knowledge store.

The migration also stores a mandate/slice/task-scoped reference to the existing
reservation/accounting state. It does not copy the ledger: restart preflight
loads the bound reservation identity and current durable economics material,
and fails closed when no active binding exists.

The mandate record stores complete canonical mandate material plus the task
registry, routing policy, policy artifacts, and source-authorisation snapshot
needed to reconstruct preflight. The packet binds its mandate/slice, task and
schema/profile, subject/scope, sources and snapshot hashes, route, provider
request identity, content hash, and freeze time. Candidate material binds its
packet/mandate, semantic payload, predicate, evidence and source-record IDs,
lineage, task/scope, epistemic basis, times, representation, processing state,
and classification status. Same ID with identical material replays safely;
same ID with different material is a conflict.

Review items bind the exact candidate material hash and review context.
Decisions are append-only, exact-candidate-bound, and derive one effective
decision; contradictory terminal decisions fail closed. `NARROW_OR_CORRECT`
requires a different candidate that explicitly supersedes the original. The
original remains historical and cannot promote under that decision. Promotion
first records an idempotent authorisation, then its deterministic governed
artifact reference. A restart before the result safely completes it; a restart
after it reuses the one result. This is a reference to the existing governed
observation authority, not another canonical knowledge store.

## Durable inventory

| Artefact | Classification and runtime authority |
|---|---|
| Scale mandate and policy/task/source snapshot | `DURABLE_ARTEFACT_NEEDED`; migration 17 immutable mandate snapshot |
| Frozen population identity | `DURABLE_REFERENCE_NEEDED`; mandate population reference/hash |
| Task/contract selection | `DURABLE_REFERENCE_NEEDED`; embedded immutable registry snapshot |
| Frozen semantic packet | `DURABLE_ARTEFACT_NEEDED`; immutable packet record |
| Reservation/accounting | `ALREADY_DURABLE_REUSE`; existing reservation and cost ledger authority |
| Physical request/attempt/transmission/response | `ALREADY_DURABLE_REUSE`; existing provider attempt/request/response ledger |
| Semantic candidate | `DURABLE_ARTEFACT_NEEDED`; immutable candidate binding |
| Review item and decision | `DURABLE_ARTEFACT_NEEDED`; item plus append-only decision records |
| Promotion and governed observation | `DURABLE_REFERENCE_NEEDED`; idempotent promotion reference to canonical observation |
| Halt | `ALREADY_DURABLE_REUSE`; migration 16 halt controller |

## Offline restart and destructive results

The executable synthetic, provider-free restart matrix covers all thirteen
boundaries: mandate registration; task registry selection; packet freeze;
reservation/preflight; pre-attempt replay; prepared attempt; ambiguous
transmission refusal; persisted response reuse; candidate registration; pending
review refusal; effective decision reconstruction; authorisation-before-result;
and persisted-result reuse. At each restart, the mandate, policy hashes,
packet/candidate/review bindings, active halt, and no-provider-replay rule are
re-evaluated from the durable catalog. No caller-created packet, candidate, or
review decision can substitute for its recorded material.

The destructive offline suite passed the previous 27 authority attacks plus
durability registration/conflict, packet/source/profile/schema/route drift,
candidate payload/evidence drift, review staleness/conflict, correction
lineage, promotion replay, halt restart/recovery, policy drift, and SQLite
orphan/cross-binding controls. A deterministic source-native path remains
limited to a registered audited deterministic task and source-fact provenance;
semantic material cannot relabel itself as deterministic. Discovery signals
remain non-evidentiary under the existing C9/C10 controls.

Critical halt checks cover task, subject, and slice halts before a send, after a
response, and before promotion. A halt survives restart; recovery is a separate
auditable event and itself survives another restart. Provider sends remain
blocked after a transmitted or ambiguous state. Existing completed promotion is
retained after a later halt, while a new promotion is blocked.

## Freeze and result

Builder was amended from `58e9465ee2518b35a4dd2dd63c7ea049ed22e4a8` and Data
was amended from `16c5bf73404a93b6111cf4d6e9c9bb1788adc714`; the exact frozen
heads are recorded in the final certification handoff after the post-freeze
destructive run. Parent PRs #77 and #30 were not changed. The stacked PR base
and mergeability were not inspected for repair, retargeted, or merged.

`S0_FACTORY_CERTIFIED_FOR_PRODUCT_OWNER_DECISION`

This closes only the mechanical Factory blocker. Before an executable S0
mandate can be drafted, Greg must still decide the population/ranking/snapshot
and group treatment; slice size and selection; source universe, specialist and
rights policy; route/escalation and budget ceilings; review/sampling,
promotion, halt/recovery, freshness, and maximum-output policy. The mandate
template remains non-executable and no unresolved choice has been filled in.

## Validation and hard zeros

Targeted Builder durability, migration, halt, persistence, and existing S0
authority tests passed. The full Builder suite, SQLite integrity, Data link and
encoding checks, immutable v0.5 manifest verification, 349 SHA/size checks,
non-executable mandate template check, and `git diff --check` are recorded in
the final handoff.

Provider calls, source acquisition/refetches, external semantic executions,
real S0 or Top-100 execution, real cohort selection, real-data candidate
promotion, public v0.5 changes, Phase 6 reopening, parent changes, merges, and
product-owner decisions: all `0`.
