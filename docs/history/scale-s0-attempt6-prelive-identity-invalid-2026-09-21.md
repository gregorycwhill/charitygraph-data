# Scale S0 Attempt 6 pre-live identity-invalid record — 21 September 2026

**Status:** Historical trace record; `PRELIVE_IDENTITY_INVALID`
**Scope:** One local pre-live execution-attempt identity only. This is not an
execution authority, recovery authority, source authority, retry approval,
or public-contract change.

## Finding

The sole Attempt 6 identity, `attempt:s0:6`, was registered before any source
or provider boundary. Its append-only attempt material recorded
`created_at` as `2026-09-21T10:55:47Z`, while the SQLite indexed column used
by restart reconstruction was the equivalent instant rendered as
`2026-09-21T10:55:47+00:00`.

The stored attempt-material hash and a hash recomputed from the retained
material both equal
`608b4ed8048076546aa3633f3cb307eee7ee4c7e2d77c97ef1b1dcc0aae9ebe4`.
Rebuilding the identity from the durable indexed columns instead produces
`275003e5e5d54ca4c9f90142aa27971448f97931a45e68c48fe17e1c4eaba08f`.
Therefore the original material and restart-reconstructed identity are not
the same canonical material, despite denoting the same instant.

The attempt database is preserved without mutation. Attempt 6 is
`PRELIVE_IDENTITY_INVALID`, non-resumable and non-retryable. It cannot be
used as a valid basis for an S0 crossing, packet, reservation, attestation,
candidate, promotion or release. This record does not create Attempt 7 or
authorise a replacement attempt.

## Boundary evidence

At the time of classification, Attempt 6 contained one mandate, cohort, run
and execution-attempt identity, together with its pre-live source-authority
and source-plan control material. It contained zero source records,
acquisition receipts, artefacts, source snapshots, representations, corpora,
packets, reservations, provider calls, candidates, review items, promotions
and public-release changes. No evidence payload was acquired.

The affected schema is migration 22, `durable_scale_s0_source_runtime_authorities`,
with checksum
`d6405f2365982cf6087dfbe97ed08e1bbb81761e6b50b512d648d93ac9873b22`.
The migration was not changed by the repair.

## Repair relation and immutable boundaries

The local Builder repair canonicalises all S0 append-only runtime timestamps
before hashing and persistence, and fails closed when a persisted execution
attempt material is not already canonical. It is recorded in local Builder
commit `065c96dee91d893b61d89b50114a4cdd3237bd1c`, based on Builder main
`78989bc9dd66d9a9c2a2e09ab97cf23e209e3a56`.

This historical record is based on Data main
`c662682a66ce59ae60b21864e7ecc83991354620`. It does not alter the immutable
public contract 0.5 release, its schemas, manifests or bytes. It does not
modify the authoritative S0 mandate or source-rights policy.

## Next safe action

No execution follows from this record. Any later attempt would require a
separate explicit authorisation and a fresh identity bound to integrated,
canonical Builder and Data revisions, followed by its own current exact
durable source authorities and every applicable S0 gate. Attempt 6 must stay
historical and untouched.
