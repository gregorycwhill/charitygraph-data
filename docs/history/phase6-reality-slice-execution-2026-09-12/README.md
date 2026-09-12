# Phase 6 reality slices — bounded execution record (2026-09-12)

The three approved reality slices were run against the already-retained, frozen Top-100 corpus. The execution used `gpt-5.6-luna`, low reasoning, Standard Responses, sequentially, with one POST per physical attempt. No source was acquired.

All 24 planned physical attempts completed (8 per slice); there were no economic exclusions, local pre-send failures, terminal provider failures, or ambiguous attempts. All responses reported model identity `gpt-5.6-luna` and status `completed`.

Provider usage: 198,933 input tokens, 69,179 output tokens, 268,112 total tokens. Actual cost at the retained Luna price snapshot and AUD/USD 1.52: USD 0.122647 / AUD 0.186433. Sum of conservative pre-send exposures: AUD 0.483599 (programme cap AUD 3.00; per-request cap AUD 0.25).

Mechanical validation passed for 4/24 complete request outputs and 137/203 propositions. Checks covered strict JSON structure, frozen cohort/source locator binding, byte-exact or whitespace-normalized exact quote matching against the cited supplied representation/page, scope-ID rules, source-role binding and locator shape. Whitespace normalization collapses whitespace only; punctuation or word differences are not accepted. This is not semantic acceptance.

| Slice | Attempts / completed | Propositions | Mechanical pass (request / proposition) | Input / output tokens | Actual AUD |
|---|---:|---:|---:|---:|---:|
| outcomes | 8 / 8 | 70 | 1/8 / 51/70 | 66,938 / 23,957 | 0.064052 |
| commitments | 8 / 8 | 58 | 2/8 / 40/58 | 71,309 / 21,367 | 0.060475 |
| capacity | 8 / 8 | 75 | 1/8 / 46/75 | 60,686 / 23,855 | 0.061906 |

Mechanical failure events (some propositions have more than one): {'evidence:quote_not_exact_in_supplied_representation': 56, 'evidence:none': 5, 'scope:private_organisation_id_mismatch': 8, 'evidence:artifact_id_mismatch': 1, 'evidence:locator_kind_mismatch': 1}. These include 56 evidence quote mismatches, 8 private organisation-scope ID mismatches, 5 propositions without attached evidence, and 2 remaining artifact/locator-kind mismatches. These are provisional mechanical findings for human review, not semantic dispositions.

Same-model repeat groups: 6. Four of six groups share no exact candidate signature under the documented comparison; two groups share one each. These exact-signature comparisons are descriptive only and are retained without reconciliation in `replicate-comparisons.json`. Human adjudication remains pending for every proposition; no advancement threshold is claimed.

## Slice packets

- [Outcomes packet](outcomes-packet.md)
- [Commitments packet](commitments-packet.md)
- [Capacity packet](capacity-packet.md)
- [Paired analyst-task materials](analyst-task-pairs.md)
- [Execution manifest](execution-manifest.json)
- [Replicate comparisons](replicate-comparisons.json)

Input handling: request bodies and source content remain outside the Data repository. The committed raw-candidate files preserve only the exact Structured Output text. The experiment applied the recorded local privacy screen; this bounds what the model saw and must be considered during review.

Explicitly unchanged: public v0.5, Viewer, governed knowledge, source corpus, and Phase 5 broader Top-100 objective. Product-value work remains downstream of adjudication.
