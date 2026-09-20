# Scale S0 execution identity binding certification — 2026-09-18

## Status

`S0_EXECUTION_IDENTITY_BINDING_CERTIFIED`

The original Attempt-2 halt was read-only audit evidence: `S0_EXECUTION_IDENTITY_BINDING_INCONCLUSIVE` because live reservation existence, durable reservation equality, caller-economics authority, canonical eight-subject materialisation, and destructive cross-attempt coverage were not all proven. This bounded repair closes those gaps. Attempt 2 remains historical halt evidence (`S0_HALTED`) and was not resumed; no Attempt 3 exists.

## Root cause and design

The prior runtime persisted an opaque run `configuration_hash` but did not explicitly and durably bind a live execution attempt to the exact Builder implementation and Data authority state. Migration 19, `durable_scale_s0_execution_attempt_identity`, adds the append-only `scale_s0_execution_attempts` table. It binds an immutable attempt ID to mandate ID/hash, slice, run ID, Builder repository/SHA, Data repository/SHA, bridge certification/version, schema version, recovery-authority reference, status, timestamp and material hash.

The mandate remains unchanged. The attempt identity is execution-specific authority. Luna selected a bounded **Model D** design: an append-only attempt root plus explicit attempt lineage on live bridge artefacts. Model A (adding the identity to every object) was more invasive; Model B (run-only transitivity) left source-plan ownership implicit; Model C (source-plan transitivity) did not protect packets and reservations without additional edges. Registering identical material is idempotent; changed implementation, Data, run, mandate or slice material conflicts fail closed. A run cannot be reused by a second execution attempt. Unknown mandate/run references fail closed. Existing migration 18 bridge fixtures and non-S0 runs remain compatible through explicit offline mode. Bitemporal canonicalisation is unchanged: source knowledge valid-time precision and knowledge-at reconstruction remain governed by the existing architecture.

## Enforcement and restart proof

Live source-plan persistence accepts an execution-attempt ID and rejects missing, unknown or mismatched bindings before source-plan material is created; the ID is persisted in source-plan material and table lineage. Snapshots, representations, corpora, bundles and packets carry the same durable edge. Live reservation binding now requires an existing canonical `budget_reservations` row, the attempt-owned run/cohort, exact mandate/slice/task linkage, and usable active/partially-consumed non-expired status. Provider-send gating rechecks packet, corpus, snapshots, representations, bundle, attempt, run/configuration hash, reservation binding, canonical reservation, task linkage and status immediately before the preflight return. Live `from_catalog` reconstructs economics from durable state and rejects caller-supplied economics. Governed transport requires the durable plan-to-attempt edge at network crossing. The catalog can be closed and reopened to recover the exact binding without caller memory. Historical synthetic fixtures must explicitly opt into offline mode.

Offline certification bound:

- Builder fixture: `6d24cc695feedfa8286f85b80b55425c4e3690d6`
- Data fixture: `366509f6bf8a723058353e69402625a1b0ded3b2`
- Mandate: `D00C4B3FEE234B96DB133C40C59D0206B00D5277F075DCF1384F9376DD74E632`
- Bridge: `S0_ACQUISITION_PACKET_BRIDGE_CERTIFIED`
- Migration: 19
- Population: exact authorised eight-subject mandate population

The exact-eight certification is one coherent local-only proof using `MandatePopulation.from_mandate(...)`, canonical bridge persistence, synthetic governed acquisitions, source plans, source snapshots, representation records, frozen corpora, task applicability, frozen packets and physical bundles. It creates a real local canonical reservation through `reserve_cost`, links the exact task key, creates the S0 binding, closes/reopens SQLite, reconstructs the attempt/run/SHAs/mandate/corpus/packet/reservation/economics, and proves the correct `SendRequest` passes the provider preflight gate without transport. Destructive coverage is 19 required substitution/absence/drift cases, all fail closed, including cross-attempt plan/snapshot/representation/corpus/packet/bundle claims, wrong-task and wrong-run reservations, missing and unusable reservations, attempt-less live binding, economics injection, unbound packet reconstruction, hash/SHA drift, and same-run second-attempt reuse. The bitemporal regression covered sub-day valid-time precision, superseded missingness/current-belief behaviour, historical knowledge-at reconstruction, and combined K/V filtering. Targeted coverage collected 55 tests and passed 55. The full Builder suite collected 919 tests and passed 918 with 1 skip. The exact tested Final-004 material is now remotely published and independently reverified: Builder PR #81 is open/unmerged on `scale-s0-execution-identity-binding` at `918de807eb557a48cb1d6448b20e1800529671e6`, and Data PR #38 is open/unmerged on `scale-s0-execution-identity-certification` at `aa31524f5e0851d8670bf812877253f4b9975abc`. Both PRs report clean mergeability. This is bounded execution-identity binding certification and remote publication certification only; it is not S0 execution or production completion.

The fixture SHAs above are pre-merge certification bases only. A future live Attempt 3, if separately authorised, must bind the final canonical Builder/Data main SHAs after PR #81 and PR #38 are merged; this certification does not claim the fixture SHAs as a future live Attempt-3 identity. Current S0 status remains `S0_AUTHORISED_NOT_YET_EXECUTED`; no Attempt 3 exists.

No live source acquisition, external charity network call, provider call, real provider reservation, semantic execution, candidate, review, promotion, S0 resume, top-100 execution or public release occurred. PR #34 and halted PR #37 remain separate historical records and are unchanged. Migration 19, the canonical execution-configuration hash, Model D, policy/mandate/routing/review/promotion authority and immutable v0.5 remain unchanged. The remote publication/reverification closeout did not merge either PR and did not execute S0.
