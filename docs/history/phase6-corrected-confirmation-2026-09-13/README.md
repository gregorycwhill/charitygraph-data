# Phase 6 corrected confirmation attempt — 2026-09-13

**Status:** Historical execution record; stopped before producing reviewable candidates
**Date:** 13 September 2026
**Authority:** Executed under the bounded product-owner authorization recorded in the 13 September 2026 Codex task. This record is evidence of that attempt, not current product or schema authority.
**Scope:** Outcomes/evaluation, commitments/implementation, and capacity/availability/access
**Review disposition:** No human adjudication or paired analyst evaluation was performed.

## Result

The corrected confirmation run stopped after one initial provider request in each capability. Each capability had four scheduled physical attempts (three subjects plus its predeclared repeat); the remaining three requests per capability were not sent after the first request failed. Across the full 12-ticket manifest, three requests crossed the provider boundary and nine remained unattempted. There were no retries, ambiguous crossings, or replacement subjects.

| Capability | First subject attempted | First-attempt result | Later requests |
|---|---|---|---:|
| Outcomes/evaluation | The Smith Family | Terminal provider rejection: Structured Output schema contained an unsupported regex lookaround at `ActivityReported.properties.count`. | 3 not attempted |
| Commitments/implementation | Sunrise Project | Provider response received, then strict `Phase6SemanticOutput` validation failed with six errors under `propositions[1]`. No candidate packet was emitted. | 3 not attempted |
| Capacity/availability/access | St George Community Housing | Terminal provider rejection: Structured Output schema contained an unsupported regex lookaround at `CapacityLimitOrMeasure.properties.measure`. | 3 not attempted |

The run therefore produced **0/3 mechanically valid complete outputs** and **zero candidate packets**. Proposition-level pass rate is not reportable: two requests were rejected before a structured output was returned, and the remaining structured output failed whole-output validation. Evidence, scope, source-role, and corrected semantic-invariant acceptance were not reached. No proposition is semantically accepted, and no usefulness gate is claimed.

## Model, accounting, and bounds

The pinned route was OpenAI Responses, `gpt-5.6-luna`, reasoning effort `low`, Standard delivery. The authorized frozen Condition A manifest is `62fa35105741f92fc5f297183745b798062b36eb41653a231a159d5acc3cfd81`. The offline execution manifest SHA-256 is `b63fd31943b7c1859b51a99989d9551e8acfb8dea6ba84a90a559ea253e44514`.

The one completed provider response reported 9,384 input tokens and 1,205 output tokens (10,589 total). At the pinned price snapshot and AUD/USD rate used by the runner, its usage-based estimate is USD 0.003792 / AUD 0.005764. The two schema-rejected calls returned no token-usage records, so their billed cost cannot be verified from this run. The conservative exposure reserved for the three sent requests was AUD 0.065325, within the AUD 0.25 per-request and AUD 1.50 aggregate authorizations. The reported priced amount is a usage-based estimate, not a provider billing-dashboard reconciliation.

| Capability | Sent / scheduled | Not sent | Reported input / output tokens | Usage-based cost known | Conservative exposure reserved |
|---|---:|---:|---:|---:|---:|
| Outcomes/evaluation | 1 / 4 | 3 | 0 / 0 | Not returned | AUD 0.022674 |
| Commitments/implementation | 1 / 4 | 3 | 9,384 / 1,205 | USD 0.003792 / AUD 0.005764 | AUD 0.021299 |
| Capacity/availability/access | 1 / 4 | 3 | 0 / 0 | Not returned | AUD 0.021352 |
| **Total** | **3 / 12** | **9** | **9,384 / 1,205** | **USD 0.003792 / AUD 0.005764 known** | **AUD 0.065325** |

The executor reported three provider calls, zero source acquisitions, and zero governed promotions. The ticket ledger confirms three unique tickets with one post each and nine tickets with zero posts. No Viewer, public v0.5, or runtime product state was changed.

## Request and response lineage

All attempted requests used Builder correction-package commit `7896e6e41423f5a17612eece0d2665e58913fe07`. Source task and source-content hashes are bound in the private execution manifest above. Request IDs, physical attempt IDs, contract hashes, request-body hashes, and response identity are recorded here without copying private source text or model output.

| Capability | Contract hash | Request item | Physical attempt | Source task SHA-256 | Request body SHA-256 | Provider response |
|---|---|---|---|---|---|---|
| Outcomes/evaluation | `92b7ab75db5fc7b32d811817a78ae126322f7fe8aa3daa3eb105133624f4c33f` | `requestitem:4bf431664066ad6e8d5e4f9b85978ed8101e321d3227f8d3e0be8c33570a85d7` | `physicalattempt:a3f39262c620f10979dcdfaf7133779900931b73daf9859f14c88fc3b053c6ac` | `cc6cfaaeb04bc312bb01ea5b2b3bd06f52ad2f2b46ebfaa3dac4a5321d73f1bb` | `8f9de07ddbefc2659cd11883bcef01674cdc092dc3954c0614d61d35236e175e` | Schema rejection; no response ID or usage record |
| Commitments/implementation | `f169a0e1c2926010881097b49c6a3944631c2257553360e9f4f3ccbe7c4c1d4f` | `requestitem:e8c112028822c7c52a43f21051fd1276ac5e1bb7c458f37e20b4622b78768149` | `physicalattempt:c164f3c46a0344f8e393a95327b61a2bfe0c347c4de69b26a071d9400f2518af` | `f366493a33f85551c9b84da55699864e3ce9d8d52f28afc314d8de32a482743a` | `40d0ff6a16fc74e465415d511f2876321dd21c8d13b80cc0220c2163e524d30a` | `resp_0c6fa4b74febec07016aa60dd661e487d08ff316506924987a`; response-body SHA-256 `61e74e589ee66d2e808897613a6f29b51ec95e6825f1871353cad69f3c4cb4ef` |
| Capacity/availability/access | `f7802dde826bf7ae0d67ceb105c88233f7b6b9c5e7a733349cd52a24af91ce99` | `requestitem:ac4cb5ba9d85e24d06eddc90191ae17dfef0a3460bb128d2964845bb7b2b728c` | `physicalattempt:d6b4d8b38cf1d3f8b1da5d07260da108ca48b7dad2653e89356e2e1116a32e17` | `de6465b44202a4290188a9f7ea262b2b877881f32d3d1b8a91b0e9bed25b35fb` | `2b413c488f329fc86f44a9918807e451b71bef993b5e707d5f100c63f82f72ca` | Schema rejection; no response ID or usage record |

## Review materials and limits

Private review materials were generated under the local run directory `cg-phase6-corrected-confirmation-20260913-v2/review-materials`. They contain the nine selected source-only Condition A tasks, nine unadministered paired analyst-task forms with blank answers and dispositions, an empty proposition-adjudication worksheet, and three repeat comparisons marked unavailable. The private directory also retains request and response artifacts needed for local audit; it is outside Git. No candidate packet was produced, so none is ready for independent human review. Reviewer dispositions are blank, the Human Evaluation Guide was not administered, and the paired analyst tasks were not run.

The original 24-output execution and its 13 September triage remain separate and unchanged. This stopped confirmation attempt does not supersede their historical findings or validate the corrected contracts. Further execution would require resolving provider-schema compatibility and strict-output failures, then validating the exact requests before any new provider crossing. No silent output repair or replay of an attempted physical ticket is authorized by this record.

## Subsequent local repair note — 13 September 2026

This note supplements the historical record above; it does not alter its attempt statuses, the 0/3 mechanically valid result, response artifacts, or accounting. Builder contract V3 (`phase6-corrected-contracts-v3`) supersedes V2 for any separately authorized future confirmation. The V3 repair and local readiness evidence are documented in [the Data readiness record](../../../PHASE6_CORRECTED_CONFIRMATION_V3_READINESS_2026-09-13.md); its implementation is local, unpushed Builder commit `3db4d8b`.

The two schema rejections came from unsupported negative lookahead patterns generated for Decimal fields; V3 removes only that provider-facing pattern and preserves local Decimal validation. Commitments' six historical errors comprised four irrelevant union-branch discriminator errors and two valid first-party-claim/source-role invariant failures. Slice-specific V3 DTO dispatch removes the irrelevant errors while continuing to reject the two semantic violations. The exact stopped response remains a failed historical fixture; no candidate was produced.

The captured commitments response-body hash printed in the original table above was incorrect: `61e74e589ee66d2e808897613a6f29b51ec95e6825f1871353cad69f3c4cb4ef` is the adjacent response metadata file's SHA-256. The SHA-256 of the raw response JSON body is `be181868ad75219a1c482337c80faae49e61c60e47aedd6d0d9fcb2ac401bee1`. The response identifier, reported token usage, cost estimate, crossing status, and reservations are unchanged.

An offline V3 preflight certified all 12 scheduled requests (four per capability) across nine distinct schemas, with zero local failures. Provider calls, new source acquisitions, attempt authority consumed, semantic outputs and promotions remain zero for the repair work. V3 execution remains unauthorized and requires separate product-owner authorization.
