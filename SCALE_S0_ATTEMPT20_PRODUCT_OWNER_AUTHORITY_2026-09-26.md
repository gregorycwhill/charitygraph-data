# Scale S0 Attempt 20 product-owner authority - 2026-09-26

**Authority ID:** `CG-S0-PO-ATTEMPT20-2026-09-26`<br>
**Status:** allocated, A3-pending and non-executable<br>
**Attempt/run:** `attempt:s0:20` / `run:s0:attempt-20`<br>
**Builder binding:** `17a8ba143358b4e25883449ddbcdcceab192977a`<br>
**Data lineage anchor:** `bee0224e8ad7fa273e9633a08bc4f0ab63985c55`<br>
**Provider project:** `proj_vnAuU8uxocL0Rosg3SulgmRI`

This record supersedes Attempt 19 only as the current future-execution authority.
Attempts 17, 18 and 19 remain immutable history; Attempt 19 is superseded and
must not be reused or resumed. The legacy opaque authority is history-only.

## Current A3 duration amendment — 2026-09-26

The Product Owner has decided that a Greg-observed
`Share inputs and outputs with OpenAI = Disabled` attestation is valid for
exactly 24 hours from `observed_at` at each send boundary. This supersedes the
prior 60-minute S0 duration for future sends only. All existing fail-closed
identity, account/project, execution-authority, structured-authority and
frozen-material binding, setting-change, explicit-invalidation, clock-anomaly,
expiry, reservation, accounting, send-start, one-crossing and restart controls
remain unchanged. This template is not an attestation and creates no execution
authority by itself.

## Governed bindings

The ordered, exact binding set is in
[`policies/scale-s0/locator-subject-bindings-v1.yaml`](policies/scale-s0/locator-subject-bindings-v1.yaml)
and the Builder-compatible structured record is
[`SCALE_S0_ATTEMPT20_STRUCTURED_AUTHORITY_2026-09-26.json`](SCALE_S0_ATTEMPT20_STRUCTURED_AUTHORITY_2026-09-26.json).

| Order | Locator subject ref | Label | Scope | External lookup identifier |
| --- | --- | --- | --- | --- |
| 1 | `locator-subject:v1:sha256:feffa6a25be21b2b1d33b354527a04c23df721c140adde9d86bddbb9d7e4b673` | Medecins Sans Frontieres Australia Limited | registered charity legal entity | `{scheme: ABN, value: "74068758654"}` |
| 2 | `locator-subject:v1:sha256:3b1572b93346698c736b056b5aab8975d980ec3b0d7e74d0139e17ee162a7d21` | SUNRISE FOUNDATION LIMITED | registered charity legal entity | `{scheme: ABN, value: "37646526132"}` |
| 3 | `locator-subject:v1:sha256:74447923f7388e6018709179e39ea8c2b9bf1a8e47e6886875835582cc955573` | Noongar Boodja Trust | registered charity legal entity | `{scheme: ABN, value: "47613674461"}` |

ABNs are lookup seeds only. They are never CharityGraph subjects, subject refs,
primary keys or universal identifiers. Future live loading must use the governed
binding registry and must not load historical ABN-valued `subject_ids` as live
subjects.

## Bounded material and economics

Scope is bounded S0 locator discovery only. Attempt 20 permits exactly three
possible physical calls, one candidate-0 call per governed subject, at USD 0.10
per subject. Maximum new exposure is USD 0.30. Attempt 17's unresolved held USD
0.10 remains included in the conservative aggregate exposure of USD 0.40.
Candidate index 0 is the sole executable candidate for each subject. Alternates
are explicitly non-executable and require distinct authority. The complete
provider-free material, including canonical request bodies and hashes, is
[`SCALE_S0_ATTEMPT20_FROZEN_MATERIAL_2026-09-26.json`](SCALE_S0_ATTEMPT20_FROZEN_MATERIAL_2026-09-26.json).

**Structured authority material hash:**
`f813b11be265566d6bb177c0f7c94f8a090a4f2a91f9c10e3dfd80d45f469aad`<br>
**Frozen material hash:**
`53a68c778e298c91bc9bc2518fae65ecf9fd9082373a9143bea871df9ecddead`

The exact candidate-0 request body hashes, in governed order, are:
`9d795311b3bf9922b5c1a541bb3f0360f708c549ee2bc9fe9119065b41e495af`,
`7039e374dcb2210ef00c9bfe9fcc9b116708211d6f3d8094f4785e923d58f8c6`, and
`b95df8a5c4a0776d1be26d9a98398006f56a8acff1e95ee2c85a8d6af913f13c`.

## Non-execution boundary

This publication creates no A3, reservation, checkpoint lifecycle, provider
call, source acquisition, production accounting state, candidate, promotion,
public release, Top-100 authority or S1 authority. A fresh matching structured
A3 is required after this authority is published on canonical Data and after a
future canonical Data merge SHA is known. The A3 must bind Attempt 20, the final
Builder SHA `17a8ba143358b4e25883449ddbcdcceab192977a`, provider project
`proj_vnAuU8uxocL0Rosg3SulgmRI`, the eventual canonical Data merge SHA and the
runtime checkpoint/frozen-material hashes; it must observe `Share inputs and
outputs with OpenAI = Disabled`, be recorded by Greg, and be no more than 24
hours old at every send boundary.

The exact non-attestation template is
[`SCALE_S0_ATTEMPT20_A3_TEMPLATE_2026-09-26.json`](SCALE_S0_ATTEMPT20_A3_TEMPLATE_2026-09-26.json).

`reality_slice1` remains development-only, deprecated and unreachable from the
current live S0 path.
