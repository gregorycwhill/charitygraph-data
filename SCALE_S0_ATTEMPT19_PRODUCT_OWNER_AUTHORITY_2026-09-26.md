# Scale S0 Attempt 19 product-owner authority — 2026-09-26

**Authority ID:** `CG-S0-PO-ATTEMPT19-2026-09-26`
**Status:** canonical current Data control-plane authority; allocated and A3-pending, therefore non-executable
**Precedence:** subordinate to the S0 mandate and A1–A5 policy; supersedes Attempt 18 only as current attempt authority.

## Subject-binding authority

The governed subject scope is **registered charity legal entity**. The complete, machine-readable current binding set is [locator-subject-bindings-v1.yaml](policies/scale-s0/locator-subject-bindings-v1.yaml). It is supported by `SCALE_S0_MANDATE_AUTHORISED_V2.yaml`, `policies/scale-s0/population-v1.yaml`, and the corresponding frozen ACNC ranking records at `rankings/acnc-2024-ais-donation-ranking-top10000.json`.

| Frozen order | Governed locator subject ref | Label | External lookup identifier |
| --- | --- | --- | --- |
| 1 | `locator-subject:v1:sha256:feffa6a25be21b2b1d33b354527a04c23df721c140adde9d86bddbb9d7e4b673` | Medecins Sans Frontieres Australia Limited | `{scheme: ABN, value: "74068758654"}` |
| 2 | `locator-subject:v1:sha256:3b1572b93346698c736b056b5aab8975d980ec3b0d7e74d0139e17ee162a7d21` | SUNRISE FOUNDATION LIMITED | `{scheme: ABN, value: "37646526132"}` |
| 3 | `locator-subject:v1:sha256:74447923f7388e6018709179e39ea8c2b9bf1a8e47e6886875835582cc955573` | Noongar Boodja Trust | `{scheme: ABN, value: "47613674461"}` |

Each ABN is an external lookup identifier only. It is never a CharityGraph subject, subject reference, primary key, or universal identifier. Historical ABN-valued fields remain immutable historical evidence/compatibility material; future live authority MUST load the governed bindings above and MUST NOT load legacy `subject_ids` as live subject identity.

## Allocator and exact authority

The S0 allocator is canonical-authority-only, append-only and monotonic. Blocked and zero-crossing attempts consume a number; numbers are never inferred by an executor, reused, or renumbered. `attempt:s0:N` binds one-to-one with `run:s0:attempt-N`.

Attempts 17 and 18 are consumed immutable history. Attempt 17 had one historical provider crossing and an unresolved, unreconciled USD 0.10 held exposure. Attempt 18 was a zero-crossing blocked attempt (zero provider crossings, zero reservations and zero new provider exposure); it is obsolete and non-resumable because of that block and the Builder identity change.

Accordingly canonical authority allocates exactly `attempt:s0:19` / `run:s0:attempt-19` to the three governed bindings above, and no other subject or identifier. It binds Builder `92683f96bc5fbe50e71a82466919380b0293f108` and requires a canonical Data lineage descending from `3e216ee748d4a21fee791153fff308ffd368cc9f`.

Provider project is exactly `proj_vnAuU8uxocL0Rosg3SulgmRI`. The maximum new Attempt-19 exposure is USD 0.30, assuming USD 0.10 per governed subject reservation under existing S0 policy. Conservative aggregate exposure is USD 0.40, including the held Attempt-17 USD 0.10. Existing tighter/other S0 controls remain in force.

## Material and non-execution boundary

The frozen material is limited to bounded S0 locator execution for these governed subjects and stated lookup identifiers. It authorises no source acquisition, evidence promotion, public release, Top100, S1, retry, or resumption of Attempts 17 or 18. `reality_slice1` is deprecated, non-canonical development-only code and is not a current live S0 CLI/path.

Attempt 19 is non-executable until this authority is published on canonical Data main and a fresh matching A3 is observed. A3 must be recorded by Greg for this exact authority, project, Builder SHA, canonical Data merge SHA and frozen material; `Share inputs and outputs with OpenAI` must be observed `Disabled`, timezone-aware and less than 60 minutes old at every send boundary. This record creates neither an A3 nor a reservation, checkpoint, provider call, source acquisition, or release.

## Provider-free derivation

At Builder `92683f96bc5fbe50e71a82466919380b0293f108`, the canonical locator body for each frozen query is JSON with `model: gpt-5.6-luna`, `input: <query>`, `tools: [{type: web_search}]`, `tool_choice: {type: web_search}`, `store: false`, and `include: [web_search_call.action.sources]`; canonical serialization is UTF-8, sorted-key, compact JSON. The authoritative query sequence per binding is exactly `"<label>" "<ABN>"`, then `"<label>"`; no additional anchors are approved. The frozen material JSON SHA-256 is `1fad79df64f13b1c33ee9f8fc95a056d5a4f7d81b788868b6e2b1e2981358303`. Canonical request-body SHA-256 values in frozen order are `9d795311b3bf9922b5c1a541bb3f0360f708c549ee2bc9fe9119065b41e495af`, `448b1c79d9e53aaa51961c88eb4f187ce74be1722b14a650ac850d8377a97fdc`, `7039e374dcb2210ef00c9bfe9fcc9b116708211d6f3d8094f4785e923d58f8c6`, `a1c00edc91bbf8fbdc4e9ef8f74e8bcb2b022eb11a7289cc340a7bb689a8187e`, `b95df8a5c4a0776d1be26d9a98398006f56a8acff1e95ee2c85a8d6af913f13c`, and `996c2d09c93940e566d60fd59846acc98b89e57ee140ed6db0fdbac5f1145368`. Packet, request, checkpoint, delivery and client-request hashes are intentionally not precomputed: Builder binds each to the fresh A3 execution authority and reservation, neither of which exists.
