# Phase 6 mechanical triage and adjudication packet (2026-09-13)

This is a derivative triage of the 24 completed Phase 6 attempts recorded in the parent execution packet. It uses only the transmitted request records, preserved provider outputs, retained source references, and local mechanical checks. It made no provider calls, acquired no source, and promoted no candidate.

The parent `attempts.json`, `execution-manifest.json`, `raw-candidates/`, per-slice adjudication exports, and original `replicate-comparisons.json` remain the immutable execution record. This directory does not overwrite or reconcile them. Request-body hashes and provider output-text hashes were independently recomputed and matched for all 24 attempts. All 24 outputs remain strict-schema valid.

## Results

The original gate reported 4/24 whole outputs and 137/203 propositions mechanically passing, with 71 failure events. Triage applied eight deterministic scope-ID corrections to two derivative candidate files. Those corrected propositions had exact request-bound organisation scope evidence: each affected request supplied one subject-matched organisation candidate; the output had the same scope kind, exact subject label and resolved-candidate state, with only a mistyped identifier. No semantic field changed. The provider outputs remain untouched and are still the source of record.

The post-repair gate replay parsed and hash-checked all 24 outputs, revalidated each task's strict response schema, request subject/slice identity, evidence presence, request-bound locator/artifact/role bindings, and organisation scope binding across all 203 propositions. It matched the recorded per-proposition failures after removing only the eight repaired scope-ID events. The 56 quote failures were checked individually against each cited transmitted locator and retained representations; the original per-locator mechanical outcomes remain preserved in the parent attempt records.

After the derivative-only repairs, 4/24 whole outputs and 142/203 propositions pass the same mechanical gate. Eight scope events were cleared; 63 mechanical failure events across 61 propositions remain. All propositions still require human semantic adjudication. The 142 mechanically clean propositions are separately available for review; the 61 unresolved propositions remain conspicuously separated and must not be treated as evidence-valid or semantically accepted.

The 56 quote failures were individually checked against the supplied locator text and retained representation objects. None was an exact quote, a unique harmless whitespace/Unicode normalization, or a safely correctable page binding. The pattern is:

- 33 quotes are unsupported by the cited transmitted representation;
- 22 preserve a case-folded contiguous word sequence but are not exact: 14 differ in punctuation or whitespace, 6 also differ in case, and 2 have non-unique occurrences in the cited text;
- 1 quote occurs uniquely in another supplied source rather than the cited source.

No quote was rewritten, normalized, or rebound. A punctuation, capitalization, extent, or locator change could change meaning or evidence attribution. No validator defect was found: the Phase 6 path used a task-specific strict JSON schema and checker; the Builder V1.2 wire DTO/converter was not invoked. Raw provider output, parsed candidate, and committed candidate hash agree, so the observed defects were not introduced by conversion.

Eight private organisation scope ID mismatches were model identifier transcription errors, not internal/provider ID mapping, prompt leakage, or checker expectation errors. Three occurred in The Smith Family's output and five in Bush Heritage Australia's output. The request establishes the unique intended candidate ID, so only these IDs are corrected in the two files under `repaired-candidates/`. `repairs.json` records original and derivative hashes and JSON pointers. Original raw candidates remain byte-identical.

Five propositions had no evidence item in the raw provider output. Four are coverage-state propositions emitted alongside known missingness; they have no locator to attach. One is a current-availability claim with no cited support. No evidence was attached retrospectively. The two artifact/locator error events concern one proposition: its raw output points to an unavailable zero-byte website artifact while using `text_quote` for a request-bound structured-field locator. Both errors are retained for review.

## Files

- `summary.json` — original and post-triage counts, by slice and integrity totals.
- `failure-ledger.json` / `failure-ledger.csv` — one row per failure event, with root cause, repair status and remaining review requirement. The single proposition with both artifact and locator-kind errors has two distinct events.
- `repairs.json` and `repaired-candidates/` — derivative-only scope-ID repair lineage.
- `triaged-attempts.json` — per-attempt post-triage gate result, retaining original hashes.
- `mechanically-clean-propositions.jsonl` — 142 mechanically passing candidate propositions.
- `unresolved-propositions.jsonl` — 61 candidate propositions with unresolved mechanical failures.
- `replicate-comparisons-triaged.json` — expanded mechanical comparisons for six repeat pairs. It reports exact agreement, unique same-type/scope differing-value comparisons, evidence differences, ambiguous anchors and one-sided propositions; it performs no semantic pairing, reconciliation or adjudication.

Reviewer identity, decision, notes, and semantic disposition fields are empty. No proposition is accepted. The packet is ready for human review with mechanical status visible; reviewers should begin with the mechanically clean subset and treat all flagged propositions as unresolved until their evidence defects are adjudicated.

## Counts

| Slice | Outputs pass | Propositions pass |
|---|---:|---:|
| Outcomes | 1/8 | 56/70 |
| Commitments | 2/8 | 40/58 |
| Capacity | 1/8 | 46/75 |
| **Total** | **4/24** | **142/203** |

Remaining failure events: 56 quote mismatches, 5 propositions without evidence, 1 artifact ID mismatch and 1 locator-kind mismatch. Provider calls: 0. New source acquisitions: 0. Governed promotions: 0.
