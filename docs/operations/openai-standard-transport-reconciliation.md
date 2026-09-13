# OpenAI Standard transport traces and ambiguity handling

This guidance applies to bounded CharityGraph OpenAI Standard API attempts. It records operational policy; a client trace identifier does not establish provider acceptance, response completion, or billing.

## Client trace identifier

Before every physical POST, derive and persist one immutable `X-Client-Request-Id` from the physical-attempt identity. The Builder mapping is `cgpa-` followed by the lowercase hexadecimal SHA-256 of the exact ASCII physical-attempt ID. It is unique per physical attempt, ASCII, and below the 512-character limit. The same physical attempt must keep the same mapping; a separately authorized physical attempt has its own identity and mapping.

Send this value as the `X-Client-Request-Id` HTTP header, outside the frozen semantic request body. Persist it in the execution ledger with the request-body hash, endpoint, send timestamp with timezone, physical-attempt ID, response-header receipt status, server `x-request-id` when returned, response identity, reported model, usage, and transport outcome. Keep request and response bodies in their private run store.

The client ID is a troubleshooting trace identifier, not an idempotency key. Never use it to justify retrying a request whose provider crossing is ambiguous. OpenAI documents that a client request ID can help Support locate a request when a timeout prevents receipt of the server `x-request-id`; Support contact remains a manual product-owner decision. See [OpenAI API request IDs](https://platform.openai.com/docs/api-reference/backward-compatibility#request-ids).

## Crossing states and cost

Use distinct ledger states equivalent to `NOT_SENT`, `LOCAL_PRE_SEND_FAILURE`, `DNS_FAILURE`, `CONNECT_FAILURE`, `TLS_SETUP_FAILURE`, `LOCAL_SOCKET_PERMISSION_DENIED`, `PROVIDER_CROSSING_AMBIGUOUS`, `PROVIDER_REJECTED`, `PROVIDER_RESPONSE_BODY_READ_FAILURE`, `PROVIDER_RESPONSE_BODY_PARSE_FAILURE`, `PROVIDER_RESPONSE_RECEIVED`, and `COMPLETED`. A send-started ticket that loses the process before an outcome is durably recorded is quarantined as ambiguous and is never replayed.

An ambiguous crossing is terminal for that physical attempt. Retain its full reserved conservative exposure in the campaign worst-case total until an approved reconciliation resolves it. Other independently authorized attempts may proceed only after their own identity, request bytes, schema, evidence rights, provider-policy attestation, route, and cost gates pass, and the whole remaining worst-case exposure stays inside the existing authority. A second ambiguity in a resumed campaign trips its transport-health circuit breaker: stop later POSTs and return the campaign to the product owner.

A definite provider rejection remains distinct from an ambiguous crossing and follows the campaign's existing rejection and capability-stop rules. A local failure before the provider boundary has zero provider posts; repair requires a valid unused ticket and the applicable authorization.

## Standard timeout and exception records

The current one-shot Standard client uses Python's `urllib.request.urlopen` with a bounded 300-second socket timeout. This matches the 300-second setting used by existing semantic callers and is longer than their retained 11–28 second provider-side generation intervals. `urllib` applies one socket timeout to connection and individual socket operations; this is not a total wall-clock timeout and it cannot separately configure connect, write, and response-read deadlines. A timeout or connection reset therefore remains ambiguous when provider receipt cannot be excluded.

Persist the outer and root exception types, root errno when available, elapsed time, transport category, and whether response headers were received. Known DNS resolution, refused/unreachable connect, TLS setup, and local socket permission failures occur before the provider request can be sent and must be distinguished from a provider rejection. Preserve ambiguity for timeout/write/disconnect errors whose phase is unavailable. If HTTP headers arrived but reading or parsing the body fails, record that provider-response failure separately with HTTP status and server request ID; do not label it a pre-connect error or a provider rejection. Do not store credentials or unredacted proxy values in diagnostics. Standard POST retries remain disabled.

Python `urllib` inherits proxy settings from its process environment/platform configuration. Record only whether proxy configuration was present and a redacted endpoint, never credentials or full URLs containing sensitive material. Do not change host proxy or certificate configuration as part of a campaign repair.

## Manual reconciliation packet

For a possible Support lookup, prepare a local packet with any available client trace ID, physical-attempt and request-ticket identities, exact endpoint, safe project reference if known, timezone-aware send timestamp, request-body hash, requested model, transport exception, whether response headers arrived, and server `x-request-id` if present. State explicitly when acceptance or billing remains unknown. Do not include API keys, Authorization headers, or other secrets, and do not contact Support automatically.
