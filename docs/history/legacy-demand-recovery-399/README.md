# CG399 legacy Semantic Demand recovery dossier

## Purpose and boundary

This package recovers historical meaning for the 74 Semantic Demand IDs used by the frozen CG395 benchmark. It is a history/evidence package only: it neither selects current product semantics nor gives any migration disposition, successor mapping, Gate-2 result, or progress award.

The authoring worktree was created detached at `b108746be5f9de7775996533535fe522fa651a88` at `C:\CharityGraph-runtime\cg399-legacy-demand-recovery-data`. Its initial `git status --porcelain=v1` output was empty.

## Search coverage

Read-only archaeology covered:

- all locally available `charitygraph-data` refs/commits and renamed/deleted semantic-demand paths, including `docs/semantic-demand-catalogue-v0.1/pilot-questions.json` (initial pilot commit `2b5a7d77be5d74dac84a0d6a8c85acf2220abc23`) and `docs/semantic-demand-catalogue-v0.2/scenarios.json` (curated commit `587ee2c23734f82e111de292971c01eddb08bf5a`);
- all locally available `charitygraph` Builder refs/path histories matching semantic/demand/catalogue terminology (no `SDC-` catalogue definition was located there);
- the local execution/archive families for CG394, CG395, CG396, CG397 and CG398 where inspectable, especially the frozen CG395 coverage matrix and benchmark manifest; and
- the CG398 candidate/history material. It was used only to locate the original CG395 coverage-matrix provenance, never as a semantic source.

The ledger retains explicit historic material only. For the 53 historical catalogue IDs that survive in CG395, it stores the 2026-10-07 v0.2 curated record (`SDC-0001`…`SDC-0053`). The earlier 2026-10-06 v0.1 pilot has explicit `SDC-01`…`SDC-36` records only; those are also stored as separate variants. The numeric zero-padding correspondence is a mechanical ID-format normalization, not a semantic inference. Any textual/structured difference remains as a separate chronological variant in the ledger.

`SDC-0054`–`SDC-0060` are not in the 74-row CG395 inventory and are deliberately not added as ledger rows. CG395 instead includes `SDC-0061`–`SDC-0081`. For those 21 IDs the searched evidence contains a family label and generic closed-world benchmark question, but not a full per-ID definition. They are therefore `HINT_ONLY`, even where a label sounds descriptive.

## Status counts

- `RECOVERED_EXACT`: 53
- `RECOVERED_PARTIAL`: 0
- `HINT_ONLY`: 21
- `UNRECOVERABLE`: 0

`UNRECOVERABLE` means no explicit evidence at all. None meet that threshold because CG395 explicitly supplies an ID, label and benchmark context. This must not be misread as recovery of a definition.

## Chronology and conflict treatment

The 2026-10-06 pilot precedes the 2026-10-07 curated catalogue. The latter is recorded as later evidence only; it is not silently selected as “correct” or made current authority. Conflicts are not normalized: both complete copied records remain in the `historical_variants` array. The v0.2 curation history explicitly records that former `SDC-0054`–`SDC-0060` clones were removed; the CG395 inventory’s different 74-ID composition is visible rather than reconciled.

## Machine-readable contract

`legacy-demand-recovery-ledger.v1.json` has schema `charitygraph.legacy-demand-recovery-ledger/v1` and stable `legacy_id` primary rows. Every row carries status, confidence, limitations, provenance-bearing variants/hints, the CG395 family label and bound benchmark cell IDs. The permitted evidence status vocabulary is embedded in the document.

`validation.json` records deterministic counts and SHA-256. `scripts/build_legacy_demand_recovery_399.py` is intentionally mechanical: it enumerates, copies explicit fields, hashes and validates. It does not generate semantic wording or use current-candidate content.

## Handoff for t02

Use this commit and the two artifact hashes recorded in `validation.json`. The unresolved legacy semantic gap is precise: `SDC-0061`–`SDC-0081` have only CG395 family/template hints; no full historical definition was recovered. The 53 exact historical scenario records are historical evidence, not an approval to retain, split, merge, replace or retire anything.
