# OpenAI Standard transport traces and ambiguity handling

This guidance applies to bounded CharityGraph OpenAI Standard API attempts. It records operational policy; a client trace identifier does not establish provider acceptance, response completion, or billing.

## Client trace identifier

Before every physical POST, derive and persist one immutable `X-Client-Request-Id` from the physical-attempt identity. The Builder mapping is `cgpa-` followed by the lowercase hexadecimal SHA-256 of the exact ASCII physical-attempt ID. It is unique per physical attempt, ASCII, and below the 512-character limit. The same physical attempt must keep the same mapping; a separately authorized physical attempt has its own identity and mapping.

Send this value as the `X-Client-Request-Id` HTTP header, outside the frozen semantic request body. Persist it in the execution ledger with the request-body hash, endpoint, send timestamp with timezone, physical-attempt ID, response-header receipt status, server `x-request-id` when returned, response identity, reported model, usage, and transport outcome. Keep request and response bodies in their private run store.

The client ID is a troubleshooting trace identifier, not an idempotency key. Never use it to justify retrying a request whose provider crossing is ambiguous. OpenAI documents that a client request ID can help Support locate a request when a timeout prevents receipt of the server `x-request-id`; Support contact remains a manual product-owner decision. See [OpenAI API request IDs](https://platform.openai.com/docs/api-reference/backward-compatibility#request-ids).

## Crossing states and cost

Use distinct ledger states equivalent to `NOT_SENT`, `LOCAL_PRE_SEND_FAILURE`, `PROVIDER_CROSSING_AMBIGUOUS`, `PROVIDER_REJECTED`, `PROVIDER_RESPONSE_RECEIVED`, and `COMPLETED`. A send-started ticket that loses the process before an outcome is durably recorded is quarantined as ambiguous and is never replayed.

An ambiguous crossing is terminal for that physical attempt. Retain its full reserved conservative exposure in the campaign worst-case total until an approved reconciliation resolves it. Other independently authorized attempts may proceed only after their own identity, request bytes, schema, evidence rights, provider-policy attestation, route, and cost gates pass, and the whole remaining worst-case exposure stays inside the existing authority. A second ambiguity in a resumed campaign trips its transport-health circuit breaker: stop later POSTs and return the campaign to the product owner.

A definite provider rejection remains distinct from an ambiguous crossing and follows the campaign's existing rejection and capability-stop rules. A local failure before the provider boundary has zero provider posts; repair requires a valid unused ticket and the applicable authorization.

## Manual reconciliation packet

For a possible Support lookup, prepare a local packet with any available client trace ID, physical-attempt and request-ticket identities, exact endpoint, safe project reference if known, timezone-aware send timestamp, request-body hash, requested model, transport exception, whether response headers arrived, and server `x-request-id` if present. State explicitly when acceptance or billing remains unknown. Do not include API keys, Authorization headers, or other secrets, and do not contact Support automatically.
