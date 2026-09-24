# Scale S0 Attempt 9 Option A terminal closure — 2026-09-24

**Closure record:** `S0_ATTEMPT9_OPTION_A_TERMINAL_CLOSURE_2026-09-24`
**Status:** approved execution-history record; creates no execution authority
**Scope:** immutable private Attempt 9 closure only

## Decision and terminal outcome

Attempt 9 is an immutable `BLOCKED_ZERO_SEND` attempt. The product owner selected
Option A: preserve its immutable execution identity; do not supersede, reconcile
or rebind it. A fresh Attempt 10 may be created only after the hardened Builder
locator-search repair is canonical, and must bind from birth to the then-canonical
Builder and Data `main` SHAs. This record neither creates Attempt 10 nor permits
its execution.

Attempt 9 was born bound to Builder
`86d6a717099b499314ed019c41ad53d18d39e559`. Lawful locator-search execution
requires tracked Builder changes after that SHA. Immutable execution identity
therefore prevents Attempt 9 from using those changes.

## Immutable binding and zero-send proof

| Field | Value |
| --- | --- |
| Runtime attempt / run | `attempt:s0:9` / `run:s0:attempt-9` |
| Builder / Data binding | `86d6a717099b499314ed019c41ad53d18d39e559` / `226c3ab26451b4c0606d69eaba780e5419caefa6` |
| Attempt material hash | `c541939f3e18d35ba04b28f40f61f66828613473971e10496004bcb92cc33ee1` |
| Configuration hash | `d2a2c9c6cdae45f5e150c8a246736563efdd2626c109aa475309933af8ff0f67` |
| Provider calls / physical sends / receipts / reservations | `0 / 0 / 0 / 0` |
| Spend | `USD 0.00` |
| Historical cohort correction | `USD 8.00`; preserved history, not send permission |

The private append-only closure artefact is
`C:/CharityGraph-runtime/cg-s0-attempt9-preprovider-macro-001/ATTEMPT9_OPTION_A_TERMINAL_CLOSURE.json`,
SHA-256 `562ebea659618abbf6b9fa54e0d032907609323d9853cf92eb8803b3d95eb3ba`.
Its corroborating database is `attempt9.sqlite3`, SHA-256
`122bc4db9712d8a223bd0721c6f49d6566099b38227c385210c95a4c1606e5c2`.
Earlier Attempt 9 evidence is retained unchanged.

## Boundaries and precedence

This additive history record is subordinate to
`SCALE_S0_PRODUCT_OWNER_AUTHORISATIONS_2026-09-22.md` and preserves its exact
A1--A5 controls, cohort, USD 8.00 total / USD 4.00 strong-model / 150-call /
USD 0.25 reservation ceilings, source and rights authority, and public-release
prohibition. It changes no public v0.5 bytes, source/evidence record, mandate,
budget authority, A3 rule, or Attempt 8 history. It supersedes only the
temporal implication that Attempt 9 remains a future executable identity.
