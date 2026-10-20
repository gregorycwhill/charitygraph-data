# Gate 3 closure and Gate 4 activation — 20 October 2026

**Status:** Approved Product Owner decision and canonical handoff

**Version/date:** 1.0 / 20 October 2026

**Publication:** `LOCAL_ONLY` — no push, merge, PR, or publication is claimed.
**Scope and supersession:** Builder-to-65k gate state and the bounded Gate 3 evaluation. This record supersedes earlier gate-state/progress snapshots for the current status; it does not change product, source, semantic, or release policy.

This is the final Gate 3 decision. Gate 3 is not reopened and no new Gate 3 evidence is commissioned by this handoff.

## Decision and Gate 3 exit evidence

On 20 October 2026, Greg explicitly approved Gate 3 closure as `CLOSED`, accepted with limitations. Gate 3's existing exit criterion is evidence of governed knowledge quality against a bounded human/reference set and expanding Semantic Demand tests, with corrections and missingness governed. The final independent review assessed all 36 original frozen question–subject pairs against the certified independent oracle by exact question identity.

The evaluation yielded 21 correct outcomes (including correctly bounded partial answers), 14 partially correct outcomes, one unsupported conclusion, and zero identified material factual hallucinations. Thirty-five of 36 outputs were mechanically valid; the remaining raw output was retained unchanged. There were 36 successful provider requests, zero retries, and US$0.194115 actual expenditure. Gate 3 is closed on this bounded evidence; no broader acceptance threshold was introduced retrospectively.

## Accepted limitations

- QFT-D02A expressed a partial conclusion too strongly as `SUPPORTED`; this was an outcome-strength defect, not a fabricated fact.
- QFT-D01B was structurally invalid because an extra record had empty answer text, although its substantive answer was correct.
- Builder received only 72 rights-admitted records: 36 ACNC Register and 36 ACNC AIS records. The oracle used a broader research universe.
- The v1.5.1 executable interface was implemented after question selection. The frozen question–subject cohort and wording were preserved.
- The oracle's aggregate status counts are inconsistent with its 36 case records: its manifest/certification aggregate reports 16 `SUPPORTED`, 13 `PARTIAL`, and 22 `NOT_ESTABLISHED` (51 total), while the case rows report 1, 13, and 22 respectively (36 total). The review used exact case rows and disclosed the unreconciled aggregate.
- This result does not establish adequacy of all seven Source Universe v1 families, population-scale quality, or production readiness.

## Reproducible evidence identities

- Execution-result SHA-256: `be632cdcc89e214a733d465d69001b3a9a43544c675e7ba2ccda27e0c94c7f7e`
- Execution-plan SHA-256: `31834cc1e133d6c4c80c80ae787e3cab00a5819d15c84c26353618c801095efc`
- Independent review inventory SHA-256: `ecd9f091598f43aa5e9afc97fa39ae0a1d66edc3e2f321ad0c329098efd60445`

The local Builder review packet is under `evidence/gate3-final-semantic-review/`; the immutable execution is under `C:\CharityGraph-runtime\g3fresh36-semantic-execution-v1.5.1-authoritative-bound-sample-20261020-v4\`. These locations are evidence references, not publication claims.

## Landed, reported, and publication state

| Item | Identity/state | Verification and publication status |
|---|---|---|
| Builder v1.5.1 implementation | `3a784129e550564acdd19fcc67bdcdf595e846be` | Verified in the inspected local Builder repository and is an ancestor of its checked-out branch HEAD. This confirms local landing only, not remote publication or merge to a canonical branch. |
| Subsequent execution HEAD | `ca6aeb01cb02b0ae76ea6b6dbe52aac2c3c7c9ef` | Verified as the checked-out local Builder HEAD on `gate3-cg406-remediation`. No remote publication is claimed. |
| Evaluation artifacts | Result and review packet exist in the local runtime/Builder paths above; hashes are recorded here | Locally available evidence. Builder Git reports 239 untracked paths, including all five final-review dossier files; it also warns that `CharityGraph-runtimecg405-pytest/` could not be opened. The review packet is separate from frozen generation artifacts; no external publication was verified. |
| This Data handoff and pointer updates | This documentation commit | `LOCAL_ONLY` until separately authorised and published. |

Local commit ancestry and current HEAD were verified read-only. Local Git state does not establish whether either commit or the evidence has been pushed, merged, or otherwise published; publication remains unverified and this Data handoff is `LOCAL_ONLY`.

## Environment and workflow issues

The following retrospective is **user-reported**, not a new engineering finding: the previously extended tranche bridge failed and manual Greg-as-bus operation resumed; roughly 150 manual interventions occurred, with approximately 5% requiring genuine Product Owner judgment; there were excessive short Terra-High runs; and end-to-end integration checking was incomplete. These reports motivate Gate 4 priorities but do not establish a measured incident root cause. Any causal explanation for the bridge failure remains a hypothesis unless separately evidenced.

The review packet is present in the local Builder workspace and was not included in this Data documentation commit. Its external publication status is unverified. No Gate 3 limitation is presumed resolved merely by activating Gate 4.

## Gate 4 entry

Gate 4 is `ACTIVE`, weight 20%, and not yet earned. Its existing canonical objective remains **Builder industrialised**: evidence model/cost routing, batches, concurrency, restart/resume, idempotence, scheduling, monitoring, failure isolation, and cost telemetry. The immediate operating priorities are autonomous substantial engineering runs, efficient default model routing, durable execution/recovery, integration-instance integrity, and exception-only Product Owner escalation. The failed bridge is not declared fit for use. Gate 4 must earn its own exit evidence; this handoff does not imply that every Gate 3 limitation has been fixed.

## Progress

| Gate | Status | Weight | Earned |
|---|---|---:|---:|
| 1. Product and semantic contract | `CLOSED` | 12% | 12% |
| 2. Source and evidence sufficiency | `CLOSED` | 13% | 13% |
| 3. Governed knowledge quality | `CLOSED` — accepted with limitations | 15% | 15% |
| 4. Builder industrialised | `ACTIVE` — not yet earned | 20% | 0% |
| **Earned / remaining** |  |  | **40% / 60%** |
