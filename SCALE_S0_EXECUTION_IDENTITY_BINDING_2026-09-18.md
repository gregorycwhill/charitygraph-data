# Scale S0 execution identity binding certification — 2026-09-18

## Status

`S0_EXECUTION_IDENTITY_BINDING_INCONCLUSIVE`

This certification repairs the capability gap recorded by the halted second authorised attempt. Attempt 2 remains historical halt evidence (`S0_HALTED`) and was not resumed; no attempt 3 exists.

## Root cause and design

The prior runtime persisted an opaque run `configuration_hash` but did not explicitly and durably bind a live execution attempt to the exact Builder implementation and Data authority state. Migration 19, `durable_scale_s0_execution_attempt_identity`, adds the append-only `scale_s0_execution_attempts` table. It binds an immutable attempt ID to mandate ID/hash, slice, run ID, Builder repository/SHA, Data repository/SHA, bridge certification/version, schema version, recovery-authority reference, status, timestamp and material hash.

The mandate remains unchanged. The attempt identity is execution-specific authority. Terra selected a bounded **Model D** design: an append-only attempt root plus explicit attempt lineage on live bridge artefacts. Model A (adding the identity to every object) was more invasive; Model B (run-only transitivity) left source-plan ownership implicit; Model C (source-plan transitivity) did not protect packets and reservations without additional edges. Registering identical material is idempotent; changed implementation, Data, run, mandate or slice material conflicts fail closed. Unknown mandate/run references fail closed. Existing migration 18 bridge fixtures and non-S0 runs remain compatible through explicit offline mode.

## Enforcement and restart proof

Live source-plan persistence accepts an execution-attempt ID and rejects missing, unknown or mismatched bindings before source-plan material is created; the ID is persisted in source-plan material and table lineage. Snapshots, representations, corpora, bundles and packets carry the same durable edge. Certified preflight reconstruction requires the packet's attempt edge and validates the stored Builder/Data/mandate/run/configuration identities before provider use. Governed transport requires the durable plan-to-attempt edge at network crossing. The catalog can be closed and reopened to recover the exact binding without caller memory. Historical synthetic fixtures must explicitly opt into offline mode.

Offline certification bound:

- Builder: `f3ea027c6159344d82b075304e5d33bf0b30c7c7`
- Data: `870fe92502583a85133005bc5ebab62154920e22`
- Mandate: `D00C4B3FEE234B96DB133C40C59D0206B00D5277F075DCF1384F9376DD74E632`
- Bridge: `S0_ACQUISITION_PACKET_BRIDGE_CERTIFIED`
- Migration: 19
- Population: exact authorised eight-subject mandate population

The offline tests prove attempt binding → run registration → exact identity recovery → source-plan gate and unbound-packet fresh-process rejection; snapshot, representation, corpus, and packet registration now derive and verify inherited attempt ownership. The existing bridge suite covers the exact eight-subject synthetic source→snapshot→representation→corpus→packet→preflight chain. Drift, substitution, duplicate-ID conflict, unknown references, configuration mismatch, mixed-attempt lineage, and pre-attempt source-plan creation all fail closed. No reservation or provider crossing is performed. Final certification remains inconclusive until the full Builder suite can complete in a writable test environment; the implementation-specific tests pass, while the suite-wide run was blocked by Windows temp-directory permissions/path creation in an unrelated v0.5 release fixture.

No live source acquisition, external network call, provider call, reservation, candidate, review or promotion occurred. PR #34 and halted PR #37 remain separate historical records and are unchanged.
