# Product-value semantic campaign execution — 14 September 2026

**Status:** Historical campaign execution record; degraded before provider crossing

**Owner:** Greg, CharityGraph product owner

**Scope:** The five frozen product-value semantic requests approved for sequential Luna/Standard execution. This record does not change Phase 6 findings, public contract 0.5, canonical knowledge, or the broader Phase 5 objective.

## Live preflight

The fail-closed preflight passed before the campaign transport invocation:

- The locked model-assisted source-only baseline and private deterministic context validated without regeneration or mutation.
- All five frozen request bodies, order, model, schema and request identities matched their certified values.
- All ten exact source representations matched their frozen hashes, source/artifact identities, organization scopes, source roles, acquisition lineage and exact-hash provider-rights decisions. The applicable Fair Dealing and provider-processing policy IDs matched.
- Greg freshly attested in the campaign handoff that `Share inputs and outputs with OpenAI = Disabled`. This is recorded as a product-owner attestation, not an API observation.
- The configured model route was `gpt-5.6-luna`, low reasoning, Standard delivery and a 300-second timeout, with automatic retries disabled. No canary or connectivity probe ran.
- The official Luna rate card used input USD 0.20/M, cached input USD 0.02/M, cache-write reservation USD 0.25/M and output USD 1.20/M. The RBA 11 September 2026 observation was USD 0.7172 per AUD; the reservation rounded the inverse rate upward to AUD 1.40 per USD.
- Conservative five-request reservation: AUD 0.098383, comprising AUD 0.020648, 0.019269, 0.019791, 0.019558 and 0.019117 in authorized order. Each is below AUD 0.25; the sum is below the AUD 1.25 five-request reservation limit and AUD 2.00 campaign ceiling. Unused authority does not permit extra requests.

Price source: [OpenAI gpt-5.6-luna model pricing](https://developers.openai.com/api/docs/models/gpt-5.6-luna). FX source: [Reserve Bank of Australia exchange rates](https://www.rba.gov.au/statistics/frequency/exchange-rates.html). The API business-data policy states that API inputs and outputs are not used for training by default: [OpenAI business data](https://openai.com/business-data/).

## Transport outcome

One local Standard transport invocation was made for the first planned request. Windows returned `LOCAL_SOCKET_PERMISSION_DENIED` (`WinError 10013`) before response headers; no server `x-request-id` was available. The transport classified this as a known pre-send local failure. The existing systemic-transport stop behavior applied, so no later request was sent. No retry or privilege escalation was attempted.

| Order | Subject | Contract | Provider POST | Transport / mechanical result |
|---:|---|---|---:|---|
| 1 | World Vision Australia | Outcomes V6 | No | Local transport invocation; `LOCAL_SOCKET_PERMISSION_DENIED`; `MECHANICAL_FAIL` (no response to validate) |
| 2 | Bush Heritage Australia | Outcomes V6 | No | `NO_ATTEMPT_DUE_CAMPAIGN_STOP` |
| 3 | Australian Red Cross Society | Commitments V5 | No | `NO_ATTEMPT_DUE_CAMPAIGN_STOP` |
| 4 | Greenpeace Australia Pacific Limited | Commitments V5 | No | `NO_ATTEMPT_DUE_CAMPAIGN_STOP` |
| 5 | The Sunrise Project Australia Limited | Commitments V5 | No | `NO_ATTEMPT_DUE_CAMPAIGN_STOP` |

The first local invocation used client trace ID `cgpa-b452e3e1dc126d67fc59681aa5c98bd34bd52559b3e641c98cf3b6b55453ca0d` and frozen request hash `a0b8d76ce6efc5e80b6e69f8c1edab3353ca008d55ac3718de16f8f5faf5390c`. Provider physical attempts: **0**. Local transport invocations: **1**. Server request IDs: **none**. Model identity was configured as Luna; no provider response exists to confirm a served model identity.

## Results and accounting

- Campaign state: `TRANSPORT_FAILURE_CAMPAIGN_STOPPED`.
- Completed responses: 0; raw provider responses: none.
- Mechanical passes: 0; mechanical failures: 1 due to local transport failure, with no semantic response; requests not attempted after stop: 4.
- Semantic propositions and candidate coverage items: 0 and 0. No human-adjudication packet items were created; the private packet directory is empty.
- Known actual USD/AUD cost: USD 0 / AUD 0. Incurred conservative provider exposure: AUD 0. Approved but unused reservation: AUD 0.098383.
- New source acquisitions: 0; human adjudications: 0; semantic governed promotions: 0; Viewer changes: 0; public v0.5 changes: 0.

Private operational details, including the exact preflight and local exception record, remain under the ignored Builder work directory `phase5-execution-packet/work/product-value-baseline-2026-09-14/campaign-execution-2026-09-14/`. No provider payload or restricted source text is copied into this public-safe history. The original certified `PREPARED_NOT_SENT` manifest and its five request bodies remain unchanged.

The local socket failure is not a semantic finding. This record gives no authority to retry, replace the failed transport invocation, resume later requests, promote candidates, or scale Phase 5. Any resumption requires an applicable unused attempt identity and the necessary product-owner authorization under current transport and campaign controls.

## Subsequent one-request resumption authorization — 14 September 2026

Greg subsequently supplied a fresh owner confirmation that `Share inputs and outputs with OpenAI = Disabled` and expressly authorized a fresh preflight plus exactly one new first provider POST for the unchanged World Vision Outcomes V6 request. This authorization does not cover Bush Heritage, Red Cross, Greenpeace or Sunrise. It also excludes retries, canaries, human adjudication and governed promotion.

The prior run ledger was rechecked: one local transport invocation, zero provider calls, no response headers or server request ID, zero response files, zero candidates and `PREPARED_NOT_SENT` on the frozen World Vision request ticket. This confirms the prior local failure did not consume a provider physical attempt.

The authorized network-enabled command was submitted to automatic approval review, which rejected it before process launch because it did not recognize the attachment-supplied authorization for this exact payload and destination in the trusted transcript. Consequently, the resumed preflight did **not** run; no resumed transport invocation or provider POST occurred. There is no resumed model response, semantic validation, candidate packet or cost. No exposure was incurred by this denied command. The four remaining requests are still frozen and unsent.

This approval-review result is operational provenance, not a semantic or provider finding. Completing the newly authorized attempt requires the authorization to be available to the execution approval review and another fresh preflight immediately before the single POST.
