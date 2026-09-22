# Scale S0 Attempt 8 identity reconciliation — 2026-09-22

**Reconciliation record:** `S0_ATTEMPT8_IDENTITY_RECONCILIATION_2026-09-22`
**Principal bridge/supervisor token:** `CG-S0-ATTEMPT8-POST-AUTH-EXECUTION-001`
**Scope:** documentation and execution-history authority only. This record creates no new execution authority.

## Authority and chronology

Attempt 7 remains earlier immutable historical execution evidence. The
September 22 A1–A5 product-owner authorisation initially described
`attempt:s0:7` / `run:s0:attempt-7` as the latest historical attempt before a
fresh post-merge execution. That historical description remains true for the
point in time at which the authorisation was approved; it does not renumber or
rewrite Attempt 7.

Fresh Attempt 8 was subsequently executed under the canonical post-
authorisation Builder and Data execution SHAs recorded below. Attempt 8 is now
the latest immutable S0 execution evidence. Any next live S0 execution after
the locator activation is canonical must use a fresh Attempt 9 identity. This
record does not authorise Attempt 9 before PR #44 is corrected or rebased,
reviewed, published and merged.

## Immutable Attempt 8 binding

The bridge/supervisor run is `CG-S0-ATTEMPT8-POST-AUTH-EXECUTION-001` with:

| Field | Immutable value |
| --- | --- |
| Runtime attempt ID | `attempt:s0:8` |
| Runtime run ID | `run:s0:attempt-8` |
| Mandate ID | `scale-s0-shadow-balanced-v2` |
| Builder repository / execution SHA | `gregorycwhill/charitygraph` / `d4b07799fc6a26ee088cccf8db1295d2e1b1b23e` |
| Data repository / execution SHA | `gregorycwhill/charitygraph-data` / `6cb3d2839331e1aece99ec3f3f5af2d5d8b1376d` |
| Semantic outcome | `S0_ATTEMPT8_PREPROVIDER_READY_FOR_OWNER_ATTESTATION` |

The evidence records `PREPROVIDER_READY`, passed restart/idempotence proof,
matched Register and AIS 8/8, retained one physical Register resource and one
physical AIS resource, and records 16 deterministic observations, 8 corpora,
152 frozen packets and 24 bundles. Discovery coverage is explicitly
nonblocking missingness with zero executable discovery packet. First-party web
records one acquired and seven withheld/blocked with one probe each. Provider
sends, reservations and receipts are zero; A3 attestation windows,
candidates and promotions are zero.

## Evidence files and durable identity/material fields

The immutable local files were read without modification:

| Evidence | SHA-256 |
| --- | --- |
| `C:/CharityGraph-runtime/attempt8/ATTEMPT8_PREPROVIDER_READY_CLEAN.json` | `7d2ccd77e46eaec5c0f536e60ab14b76bdc3be7e83614ac572fe903a9b6167f8` |
| `C:/CharityGraph-runtime/attempt8/state_clean.sqlite3` | `201e1b942ae9e33e4c45e9e33cf564c1358ce7d273bc1fa9b0044feebc3df576` |

The JSON identity/material fields are:

- status `PREPROVIDER_READY`; created `2026-09-22T00:44:12+00:00`;
- mandate hash `6050d7dd652385dbe1f84136110d06e3d1f396b63bf4ef4de9c55e83b0fd6e33`;
- restart proof `same_material_hash=true`, material hash
  `d314438b885723706d46c676ac010d3ac0c9e350148b5288fdcb880ae89a7dd4`, and
  configuration hash `1b3158b7550b15ae9fc216e1e941f2c198d045b5eedc9705d29aff0301c3f7b3`;
- Register resource `8fb32972-24e9-4c95-885e-7140be51be8a`, source bytes
  SHA-256 `af01381cb73ea7cb52e87668aba75a1711fe6e370b79303210e1b7ed130504d6`;
- AIS resource `710630ea-1202-4bbb-95f7-3973a972ddf8`, source bytes SHA-256
  `1d7ec16475b222943297ce3f73a25139665911b04a1cae51beea1541191d1f45`;
- `provider_transmission=false` and `public_release=false`; reconstructed
  packet `packet:a4f668e0f2e8e4b8cd74c5fc022ce8d011b49396081232ab3161bd86e5fafa96`.

The SQLite durable identity/material fields corroborate the JSON: table
`scale_s0_execution_attempts` contains `attempt:s0:8`, mandate
`scale-s0-shadow-balanced-v2`, run `run:s0:attempt-8`, Builder/Data repository
and SHAs above, bridge certification `S0_ACQUISITION_PACKET_BRIDGE_CERTIFIED`,
schema version `22`, recovery reference `recovery:scale-s0-attempt-8`, status
`prepared`, and material hash
`d314438b885723706d46c676ac010d3ac0c9e350148b5288fdcb880ae89a7dd4`.
Table `runs` contains `run:s0:attempt-8`, cohort `cohort:s0:8`, kind `s0`,
status `planned`, the same configuration hash, and run material hash
`182dd564394c30d625930a965d01618b71e1ded932e97e52e80c1a43cedb6f3e`.
The durable source-snapshot rows bind 17 snapshots to `attempt:s0:8`, the
Register/AIS snapshot hashes above, and mandate
`scale-s0-shadow-balanced-v2`.

## Precedence and boundaries

The original Attempt 7 subsection in
`SCALE_S0_PRODUCT_OWNER_AUTHORISATIONS_2026-09-22.md` is preserved as a
point-in-time A1–A5 approval binding. For current/latest execution history,
this additive reconciliation record is subordinate to the controlling A1–A5
policy and supersedes that subsection's temporal implication that Attempt 7 is
still latest. `CURRENT_STATE.md` and `IMPLEMENTATION_PLAN.md` now point to
Attempt 8 as latest immutable history and Attempt 9 as the next fresh identity.

This is history reconciliation only. It does not alter the mandate bytes,
cohort, budgets, A1–A5 substance, A3 rule, locator contract, search-metadata
treatment, public-release prohibition, immutable public v0.5, Attempt 7 or
Attempt 8 evidence, Builder, PR #44, or any runtime/provider/source/public
state. After publication and merge of this repair, PR #44 must be rebased or
otherwise mechanically brought onto the repaired canonical Data `main` and
re-reviewed before any host merge.
