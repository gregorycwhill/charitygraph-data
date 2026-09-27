# S0 immutable identity lineage repair

Status: approved identity repair; no execution or publication authority.

The product-owner decision following CG-S0-IDENTITY-LINEAGE-REPAIR-TERRA-093
fixes the successor IDs as `scale-s0-shadow-balanced-v3` and
`scale-s0-authorised-balanced-v3`. Attempt 20 binds the authorised successor
only. The shadow successor remains non-executable proposal material.

[The machine-readable lineage](SCALE_S0_IDENTITY_LINEAGE_V1.json) selects and
pins current and historical packages. Successive numeric versions follow the
existing policy and mandate convention:

| Layer | Retained historical artifact | Current successor |
| --- | --- | --- |
| Population | population-v1 | population-v2 |
| Rights/transmission | rights-transmission-v2 | rights-transmission-v3 |
| Locator bindings | locator-subject-bindings-v1 (Attempt 19) | locator-subject-bindings-v2 (Attempt 20) |
| Balanced bundle | bundle-v1 | bundle-v2 |
| Shadow mandate | shadow-balanced-v2 | shadow-balanced-v3 |
| Authorised mandate | shadow-balanced-v2 (historical ID) | authorised-balanced-v3 |

The binding registry filename versions the artifact; its unchanged schema
version still describes the same schema. The current population points to
registry-v2. Subject refs, ABN lookup values, queries, budgets and substantive
policy rules are unchanged. Rights-v3 carries the already-adopted open-web
rules under a fresh identity because rights-v2 was previously edited in place.

The historical package is restored exactly from Data
`0f73f399b0d5feeff75b0716fc31da07866b6d14`. Its runtime authorised mandate hash
remains `6050d7dd652385dbe1f84136110d06e3d1f396b63bf4ef4de9c55e83b0fd6e33`.
Rights-v2 retains the exact post-open-web bytes consumed by that package;
the earlier conflicting revision is referenced by exact Git commit and path.
Historical shadow-v2 reused the authorised v2 ID with different material.
That proposal is explicitly quarantined as historical evidence, never a
second executable definition. Its exact digest is checked by Builder.
Past conflicting revisions are evidence of the defect, not alternative
current definitions. Git commit/path references preserve their original bytes
without assigning retroactive successor identities to historical execution.

Attempts 8, 17, 18 and 19 retain their original evidence and bindings.
Historical loading is explicit and reconstructs the original package; current
loading selects the pinned successors. Missing artifacts, digest drift,
unregistered artifacts and duplicate definition IDs with different material
fail closed. Attempt 20's structured authority includes the authorised mandate
ID/hash and population/bundle hashes, checked at the durable checkpoint.

The committed authority retains a pre-merge Data anchor. Runtime must derive
the effective published Data merge binding and recompute authority/checkpoint
hashes; no commit embeds its own SHA. The 24-hour A3 requirement and the
conservative USD 0.40 exposure (including Attempt 17's unresolved USD 0.10)
remain unchanged. No A3, reservation, send or production mutation is created.
