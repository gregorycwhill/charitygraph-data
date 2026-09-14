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


## Completed one-request resumption - 14 September 2026

After the earlier attachment-supplied handoff was rejected before launch by automatic approval review, Greg supplied fresh inline authorization: `Share inputs and outputs with OpenAI = Disabled`, with permission for a fresh preflight and exactly one new first provider POST for the unchanged World Vision Australia Outcomes V6 request. No other subject or retry was authorized.

The earlier run remains immutable and reconciles to one local transport invocation, zero provider calls, no response headers or server request ID, zero response files and zero candidates. It was a confirmed pre-send socket-permission failure and did not consume a provider attempt.

The resumed fresh preflight passed. It verified the locked source-only baseline and deterministic context without regeneration; the unchanged request body SHA-256 `a0b8d76ce6efc5e80b6e69f8c1edab3353ca008d55ac3718de16f8f5faf5390c`; schema SHA-256 `860f154551286b55e64d25c953ed9371a5ea053ddeeb6043a0dfb466c33d07af`; semantic contract SHA-256 `cdfdb68765641400fac367ec50f95a9ef184b81d6991fc8c31fc5c575243b27d`; both exact source representation hashes and rights lineage; the fresh owner attestation; the one-attempt AUD 0.25 cap; and the Luna pricing and RBA FX reservation. The reserved conservative exposure was AUD 0.020648. No source substitution or acquisition occurred.

Exactly one Standard POST was made for World Vision Australia Outcomes V6 using `gpt-5.6-luna`, low reasoning, a 300-second timeout and no automatic or manual retries. Client request ID: `cgpa-b452e3e1dc126d67fc59681aa5c98bd34bd52559b3e641c98cf3b6b55453ca0d`. HTTP status: 200. Server request ID: `req_af40bdff67df4108b322255cc72271f2`. The provider response identified `gpt-5.6-luna`; existing Outcomes V6 mechanical validation returned `MECHANICAL_PASS`. Usage was 10,966 input tokens and 629 output tokens. Actual cost was USD 0.003497 / AUD 0.004896, below the AUD 0.25 cap. The raw response and complete attempt record are retained privately under the ignored Builder work directory `phase5-execution-packet/work/product-value-baseline-2026-09-14/campaign-execution-2026-09-14-resumed-world-vision-v1/`.

Two propositions are retained as `CANDIDATES` in the private human-adjudication packet at `phase5-execution-packet/work/product-value-baseline-2026-09-14/campaign-execution-2026-09-14-resumed-world-vision-v1/human-adjudication-packet/01-28004778081.json`; candidate coverage count is zero. No human adjudication, experiment-governed promotion, canonical/public promotion or product projection occurred. Greg remains `HUMAN_ADJUDICATOR`; model output is not a human decision.

The resulting state is `FIRST_SEMANTIC_REQUEST_COMPLETED_AWAITING_NEXT_EXECUTION_AUTHORITY`. Bush Heritage, Australian Red Cross, Greenpeace and Sunrise remain frozen and unsent. This one-request result does not authorize a retry, the remaining requests, new sources, Viewer changes, public v0.5 changes or broader Top-100 execution. Phase 5 remains active.


## Four-request campaign preflight and approval-review hold - 14 September 2026

Greg supplied a campaign-level authorization for exactly one at-most-once provider POST per remaining frozen request, in order: Bush Heritage Outcomes V6; Australian Red Cross Commitments V5; Greenpeace Commitments V5; and Sunrise Commitments V5. The attestation was `Share inputs and outputs with OpenAI = Disabled`. No per-request authorization was required for ordinary successful responses, mechanical failures or confirmed pre-send local failures under that handoff. World Vision was excluded from resending.

One fresh campaign preflight passed before any of the four sends. It validated the unchanged source-only baseline lock and private deterministic context, confirmed World Vision's prior response and two candidate propositions exactly once, and verified all four frozen request bodies, schema/contract identities, subject scopes, client request IDs, exact source representation hashes and provider-rights/acquisition lineages. No source was substituted or acquired. Official Luna rates used were USD 0.20/M input, USD 0.02/M cached input, USD 0.25/M cache-write input and USD 1.20/M output. The 14 September RBA USD-per-AUD observation was 0.7149; AUD 1.40/USD was used as the upward-rounded reservation rate. The four-request conservative reservation was AUD 0.077735. Including World Vision's prior AUD 0.020648 conservative exposure, planned campaign exposure was AUD 0.098383, below the AUD 2.00 campaign authority; each remaining attempt was below AUD 0.25.

The first Bush Heritage Standard POST command was rejected by automatic approval review before process launch. The review's reason was that campaign authorization appeared only in a pasted attachment and was not explicit approval in trusted user content; the review prohibited bypassing the rejection through an alternate or indirect route. Therefore this pre-send hold has zero local transport invocations and zero provider POSTs. Bush Heritage, Red Cross, Greenpeace and Sunrise remain unchanged at `PREPARED_NOT_SENT`. The temporary staging copy of request bodies and source text was removed; the durable preflight and hold records remain in the private Builder work directory `phase5-execution-packet/work/product-value-baseline-2026-09-14/campaign-execution-2026-09-14-resumed-remaining-four-v1/`.

The handoff's campaign authority remains recorded, but execution is held pending explicit approval in trusted chat content so automatic review can assess the provider-data transfer. No request was retried or rerouted around review. World Vision remains completed once with `MECHANICAL_PASS`; all five requests' semantic outputs remain candidates awaiting human adjudication. No source acquisition, human adjudication, semantic governed promotion, canonical/public promotion, Viewer change or public v0.5 change occurred in this preflight/hold step.


## Completed four-request campaign continuation - 14 September 2026

After the first POST command was rejected before launch, Greg reiterated in trusted chat that he did not want per-request micro-approvals for the already supplied campaign authority. Execution resumed using the single campaign-level authorization and the passed campaign preflight. No per-request authorization was requested between responses. World Vision was not resent.

Two elevated staging command attempts for Red Cross lacked access to the OneDrive source-metadata file; in both, the sender guard then exited before the Standard transport client ran. They are recorded separately as two local setup failures, with zero Standard transport invocations and zero provider crossings. Normal-context staging succeeded, and the frozen Red Cross request then completed once. No provider request was retried.

| Order | Subject | Contract | POSTs | Client request ID | Server request ID | Result | Input / output tokens | Actual USD / AUD | Conservative AUD | Propositions |
|---:|---|---|---:|---|---|---|---:|---:|---:|
| 1 | World Vision Australia | Outcomes V6 | 1 | `cgpa-b452e3e1dc126d67fc59681aa5c98bd34bd52559b3e641c98cf3b6b55453ca0d` | `req_af40bdff67df4108b322255cc72271f2` | HTTP 200, `MECHANICAL_PASS` | 10,966 / 629 | 0.003497 / 0.004896 | 0.020648 | 2 |
| 2 | Bush Heritage Australia | Outcomes V6 | 1 | `cgpa-5c7bf129b89334c5c89ac6841b32101a5917daa5bb3a32ce3b66c03d8866b042` | `req_ed5d9e9496204e9799c6d561c6975557` | HTTP 200, `MECHANICAL_PASS` | 8,999 / 2,539 | 0.005297 / 0.007416 | 0.019269 | 11 |
| 3 | Australian Red Cross Society | Commitments V5 | 1 | `cgpa-6332763b82967233c4a2e9f55e47ec17f3bb6f69fe7232bf1adf08cb891f1050` | `req_1c806b79d37d40c0b0ba48120b13069c` | HTTP 200, `MECHANICAL_PASS` | 10,201 / 769 | 0.003473 / 0.004863 | 0.019791 | 2 |
| 4 | Greenpeace Australia Pacific Limited | Commitments V5 | 1 | `cgpa-dcc7e2da2d08df548c71dcf43bfdf656b4fce25b763e55e73ed29f0b524b5158` | `req_f47413cd242e411e9f4575f5ac1fa0bf` | HTTP 200, `MECHANICAL_PASS` | 9,526 / 1,507 | 0.004190 / 0.005866 | 0.019558 | 6 |
| 5 | The Sunrise Project Australia Limited | Commitments V5 | 1 | `cgpa-d0eec5da03043a7aa315e984eacff62d5e627482b99cf50431a3e6680e0cfdf3` | `req_af155ac5c0cb4e19b327623f65e73523` | HTTP 200, `MECHANICAL_PASS` | 8,498 / 1,120 | 0.003469 / 0.004857 | 0.019117 | 4 |

Every request used `gpt-5.6-luna`, low reasoning, Standard delivery, a 300-second timeout and zero automatic/manual retries. The four new requests consumed four provider POSTs; total campaign crossings including World Vision: five. Total use: 48,190 input and 6,564 output tokens. Total actual cost: USD 0.019926 / AUD 0.027898. Conservative reserved exposure for all five: AUD 0.098383; each request remained below AUD 0.25 and the campaign remained below AUD 2.00. Ambiguous exposure: AUD 0.

The final state is `SEMANTIC_CANDIDATES_READY_FOR_HUMAN_ADJUDICATION`. The combined private packet is `phase5-execution-packet/work/product-value-baseline-2026-09-14/campaign-execution-2026-09-14-resumed-remaining-four-v1/human-adjudication-packet/combined-campaign-packet.json`. It contains all 25 propositions across five completed responses, exact request/provider lineage, scopes, epistemic classes, evidence locators and authorized private support excerpts, with evidence-strength assessments and all human dispositions blank. There are zero candidate coverage items. Greg remains `HUMAN_ADJUDICATOR`; no ChatGPT human adjudication, source acquisition, semantic governed promotion, canonical/public promotion, Viewer change or public v0.5 change occurred. The original five frozen request bodies, baseline lock and deterministic context remain unchanged.

The public-safe record excludes raw provider responses and supporting source excerpts. Those remain in the ignored private Builder execution work directory. The campaign authorization is consumed: no request has retry authority; any new semantic call requires separate product-owner scope.
