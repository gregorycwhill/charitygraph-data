# RC4 Release Ownership Repair

> **Authority status:** Historical release-ownership record. Immutable RC4 provenance is retained; current authority is `PUBLIC_CONTRACT_0_5.md` and `DOCUMENT_AUTHORITY.md`.

**Status:** Completed archival/ownership repair — RC4 content unchanged
**Authoritative Data path:** `releases/rc4-2026-08-14`
**Dataset version:** `phase2b-2026-08-14-rc4-fundraising-projection-correction`
**Accepted Viewer source commit:** `77d84befa90c1079346e146f82504ff2ef0d9f26`

CauseBase Data now owns the immutable RC4 release. It was imported from the accepted Viewer `public/data` tree without card regeneration or semantic edits. The shorter directory name is necessary on Windows because the accepted percent-encoded sidecar names exceed the path limit when nested under the full dataset-version name; the manifest retains the exact dataset version.

Verification before and after import checks the manifest's declared file sizes and SHA-256 hashes, 120 JSON cards, 228 source-native sidecars, taxonomy/schema/bulk artefacts, card IDs and selected EJA values. The imported manifest SHA-256 is `4eb7087dbb6a4104f8b659477cd1bbfecee53c541118596aeda204329239b220`.

Viewer reproduction uses `npm run prepare-from-data` with an explicit `CAUSEBASE_DATA_RELEASE_DIR`; it neither fetches “latest” nor deploys. The command prepares a self-contained static bundle and fails for an incomplete or unvalidated Data release.

Product decisions closed in the approved design direction are recorded in `PUBLIC_CONTRACT_CONSOLIDATION_PROPOSAL.md`: basis versus extraction, coverage availability, financial signs, source-payload policy, capability registry, current-financial pointers, identity continuity, sparse summaries and derivative lineage.

No vNext schema migration, card regeneration, model call, corpus expansion or deployment occurred.
