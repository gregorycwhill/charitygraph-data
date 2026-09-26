# Scale S0 Attempt 18 product-owner authority — 2026-09-26

**Authority ID:** `CG-S0-PO-ATTEMPT18-2026-09-26`

**Status:** historical, consumed and non-resumable. Superseded as current attempt authority by `CG-S0-PO-ATTEMPT19-2026-09-26`; retained below as Attempt-18 history.

**Historical scope:** `attempt:s0:18` / `run:s0:attempt-18`; no other execution or product scope

> **Supersession note (2026-09-26):** Attempt 18 was blocked with zero provider crossings, zero reservations and zero new provider exposure. Its number remains consumed. It is obsolete and must not be resumed, because of that terminal zero-crossing block and the Builder identity change. This note does not rewrite the historical record below.

**Authority precedence:** this narrow, attempt-specific authority is subordinate to `SCALE_S0_AUTHORISATION_DECISION_2026-09-18.md`, `SCALE_S0_MANDATE_AUTHORISED_V2.yaml`, `SCALE_S0_PRODUCT_OWNER_AUTHORISATIONS_2026-09-22.md`, and `SCALE_S0_LIVE_LOCATOR_ACTIVATION_2026-09-22.md`. It does not modify those authorities except to supply the expressly approved fresh Attempt 18 identity, cohort, maximum new exposure and project binding below.

## Controlling human statement — preserved verbatim

> I authorize a new S0 live locator execution under `attempt:s0:18` / `run:s0:attempt-18` for ABNs `74068758654`, `37646526132`, and `47613674461`, with maximum new exposure of USD 0.30. Attempt 17 remains immutable and its unresolved USD 0.10 remains held and unreconciled. This is a new attempt, not a retry or resumption of Attempt 17. Use OpenAI project `proj_vnAuU8uxocL0Rosg3SulgmRI`.

## Exact binding and limits

| Binding | Exact value |
| --- | --- |
| Attempt / run | `attempt:s0:18` / `run:s0:attempt-18` |
| Cohort | `74068758654`, `37646526132`, `47613674461` — and no others |
| Maximum new exposure | USD 0.30 total, with each new locator reservation at most USD 0.10 |
| Provider / project | OpenAI / `proj_vnAuU8uxocL0Rosg3SulgmRI` |
| Locator model and route | `gpt-5.6-luna` through the governed Responses web-search locator route |

Attempt 17 is immutable historical evidence. Its one physical crossing and unresolved USD 0.10 reservation remain held and unreconciled. They are not released, reconciled, retried, resumed, rebilled, or counted as any part of the USD 0.30 new Attempt 18 authority. Attempt 18 is a new attempt, not a retry or resumption.

The existing S0 limits continue unchanged: total provider spend at most USD 8.00, strong-model spend at most USD 4.00, at most 150 provider calls, and no durable reservation above USD 0.25. The narrower USD 0.10 per new Attempt 18 locator reservation and USD 0.30 maximum new exposure are additional limits, not a revision of those rules. Budget headroom is not authority.

## Mandatory gates and preserved controls

No send is permitted unless this authority is published and merged into the canonical Data `main`, the fresh attempt is bound to the then-canonical Data main and exact authority material, and Greg supplies a fresh A3 attestation for this exact authority, project and Attempt 18. A3 must record the observed `Share inputs and outputs with OpenAI` setting as `Disabled`, be timezone-aware and valid for less than 60 minutes. The repaired fresh-clock and send-start checks remain mandatory; expiry, backwards clock, or a setting/account/project/authority/frozen-material change invalidates the window and requires a fresh human observation. This document neither creates nor renews A3.

One-physical-crossing ownership, durable receipt-before-parsing, actual/release idempotency, ambiguity holding, and no blind retry semantics remain mandatory. Locator output (including search results, snippets, citations and provider source metadata) is discovery metadata only, never evidence, source facts, frozen-corpus evidence, observations, candidates or semantic support.

This authority does not authorise source acquisition, semantic extraction, promotion, public release, Top-100 work, S1, additional subjects, a provider call, a reservation/accounting mutation, or any mutation of Attempt 17.

## Publication and execution boundary

At its historical recording time this record was pending publication; it never created execution authority. It is now superseded, consumed and non-resumable. Publication/merge alone would never have authorised a send: fresh human A3 and every existing preflight, rights, packet, budget, reservation, exactly-once and halt control remained required.
