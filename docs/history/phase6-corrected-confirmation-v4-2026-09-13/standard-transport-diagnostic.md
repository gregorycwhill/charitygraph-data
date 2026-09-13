# Standard transport regression diagnostic — 13 September 2026

**Classification:** Internal historical diagnostic. This record covers transport only. The two Smith Family V4 attempts remain ambiguous and unchanged; the six remaining V4 semantic requests remain frozen and unattempted.

## Finding

The retained records do not contain the nested Python exception for either Smith attempt, so their exact socket error cannot be recovered and neither attempt is reclassified. The first POST began at `2026-09-13T08:34:32.324179+00:00` and its ticket was closed at `08:34:32.408087+00:00` (83.908 ms). The Smith repeat began at `10:54:40.290179+00:00` and its ticket was closed at `10:54:40.395993+00:00` (105.814 ms). Both have no response headers or server request ID. The first has no persisted client trace ID; the second retains `cgpa-aa9736f66217455cb535f8f18d5c1a2f635eb6bafa0156f3c386b97f9459182a`. The only retained exception text is the generic `Standard POST connection outcome is ambiguous`. No status line, response body, provider model, usage, or cost is known. The original full manual Support packets remain in the private V4 run directory.

A separate authenticated GET from the ordinary restricted process was denied in 74 ms with `PermissionError [WinError 10013]` before an HTTP response. The same request succeeded when run through the explicitly authorized network-enabled command context. This directly demonstrates a local socket permission boundary in the ordinary process context. It is consistent with the fast Smith failures but does not prove their original exception; the missing nested exception is a historical observability gap. No CharityGraph request body or source data was used in either connectivity check.

## Historic and current path comparison

The retained 24-response Phase 6 run record proves 24 completed attempts and 24 provider POSTs, each recorded with one POST. Its files do not pin the exact Builder commit, execution script, socket timings, or full request headers. The recoverable tracked Standard Responses helper is `src/charitygraph/openai_client.py`; the Phase 6 execution driver used for the 24-response run is not present in the retained run folder, so attribution to an exact executed code revision is not independently verifiable.

| Behavior | Recoverable successful path | V4 path before this repair |
|---|---|---|
| HTTP stack / endpoint | Python standard-library `urllib.request.urlopen`; Responses API | Same `urllib` stack; `https://api.openai.com/v1/responses` |
| Method / body | POST; UTF-8 JSON from compact `json.dumps`; no SDK dependency | POST; pre-certified UTF-8 canonical JSON bytes with sorted keys |
| Authentication / headers | `OPENAI_API_KEY` as Bearer token; `Content-Type: application/json` | Same environment credential; `Content-Type: application/json; charset=utf-8`; added `X-Client-Request-Id` |
| Timeout | The run artifact does not retain a configured timeout. The tracked helper defaults to 60 seconds; bounded semantic callers elsewhere explicitly use 300 seconds. | One 120-second `urlopen` timeout applied to connect and individual socket operations |
| Retries | The tracked helper supports a caller-selected retry count (default 2); the retained run ledger records one POST for each of its 24 successful physical attempts but cannot establish failure-path retry settings. | One direct `urlopen` call per physical attempt; no retry |
| Capture / persistence | Raw response bodies and usage were retained; no client trace ID is in the 24-row ledger | Raw response retained; trace ID persisted before crossing; response headers/server request ID captured |
| Connection lifecycle | `urlopen` call per request; no persistent session | Same; no persistent session |
| Library versions | The client is Python stdlib; the historical Python version is not recorded. `openai` and `httpx` were not installed in the current diagnostic environment. | Python 3.13.7, OpenSSL 3.0.16; `openai`, `httpx`, and `requests` are not installed |

The retained successful response objects report server-side `created_at` to `completed_at` intervals of 11–28 seconds (median 20.5 seconds). These are provider timestamps, not client-observed network latency. The V4 failures completed ticket handling in under 106 ms, far below either timeout; there is no evidence they were response timeouts. The 120-second value was shorter than the tracked bounded semantic callers' 300-second setting, so it is restored to 300 seconds as a bounded per-socket inactivity timeout. `urllib` does not expose separate connect, write, read, or overall deadlines through this call; the 300 seconds is not a total wall-clock bound.

No proxy variables (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY`) or custom CA variables (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) were set. `urllib.request.getproxies()` returned no proxies and Windows WinHTTP reports direct access. The default Python SSL context uses the installed OpenSSL 3.0.16. No operating-system or network configuration was changed. IPv4 versus IPv6 selection was not separately measured.

## Repair

The deterministic defect established by the diagnostic was exception collapse: the transport caught `URLError`/`OSError` and replaced the underlying exception with a generic message, and the ticket/audit writer persisted only that message. A pre-connect local socket denial therefore could be mislabeled as an ambiguous provider crossing. The transport now retains the outer and root exception types, root errno where available, elapsed duration, response-header state, and a transport category. Known DNS, connect, TLS-setup, and Windows socket-permission failures are recorded as pre-provider failures. Timeouts and resets remain ambiguous because `urllib` cannot identify which socket phase failed. Response-body read or parse failures after headers have arrived are recorded as provider-response failures with the known status and request ID. V4 records pre-provider and response-body failures separately from provider rejections and stops the campaign on systemic failures.

The timeout was raised from 120 to the bounded 300 seconds used by existing semantic callers. Automatic retries remain disabled for governed POSTs. `X-Client-Request-Id` remains a troubleshooting trace, not an idempotency key. The authenticated models probe returns metadata and bytes directly; it is not a `StandardProviderResponse` and cannot be reconciled into the semantic candidate path.

## Authorized transport checks

| Check | Result | Trace / evidence |
|---|---|---|
| Restricted-process GET invocation | Local socket permission denial before HTTP; 74 ms; no provider crossing | Client `cgdiag-models-678652ff6daf4a9f8a3f18abfbaae539`; `WinError 10013`; no server request ID |
| Network-enabled authenticated `GET /v1/models` | HTTP 200; 0.912297 s; 21,060 response bytes | Client `cgdiag-models-4aa34162416849169d3003741a2fe3a6`; server `1c44cbfe-ead8-4be2-a38c-e21e696b7d07`; raw SHA-256 `781fc073e4f12776b491c553b15ff55eaeb67ef4d1a39f6a9429e3c58de4c17a` |
| Luna Standard canary 1 | HTTP 200; `completed`; model `gpt-5.6-luna`; 12 input / 5 output / 17 total tokens; estimated USD `0.0000084` | Physical `diagnostic-physical-attempt:canary-1:4841e4f638e94af38d0687d97f7de455`; client `cgpa-10ab1a7db2d242056db2c7c225fc0a83290a776bc649270afe30af3b7fb02e8c`; server `req_81b1b841d87a46cb8fbf39ff12cfc947`; exact transport latency was not captured by the first invocation; command duration was 2.844 s including interpreter startup |
| Luna Standard canary 2 | HTTP 200; `completed`; model `gpt-5.6-luna`; 12 input / 5 output / 17 total tokens; 1.311252 s transport time; estimated USD `0.0000084` | Physical `diagnostic-physical-attempt:canary-2:49677ab1cb634e9c9fd5f60ac92e9985`; client `cgpa-afa5f18b1267c5d97c0e2d90484c0e0c8059d0fa55737d97e0f18e3bb790d32c`; server `req_1d614846c7d34ee9a589a01caed7ff93`; response ID `resp_076bc84e97483675016aa68713fc1c87d0b68ff6545011be03` |

Canary 1's response ID is `resp_043d0a95e2ef7d7a016aa686db799487d0ab03a78307902530`. Both canary prompts were exactly `Return exactly the word OK.`. Each had a distinct physical attempt ID and client trace ID, `store: false`, and no source or CharityGraph content. Raw diagnostic response bytes and detailed metadata are held only in the local temporary diagnostic directory, not in a semantic run or candidate ledger. The two canaries cost an estimated USD `0.0000168` combined (about AUD `0.000026` at the retained 1.52 FX rate).

## Readiness and unchanged boundaries

Both canaries completed unambiguously, so Standard transport is **provisionally ready for a separately authorized semantic resume when run in a network-enabled execution context**. The ordinary restricted context still blocks sockets. This diagnostic does not authorize resuming V4 and does not alter its campaign state.

Semantic Phase 6 calls: **0**. Diagnostic generation calls: **2**. Outbound authenticated models GETs: **1** (plus one local invocation denied before opening a socket). New source acquisitions: **0**. Governed promotions: **0**. V4 retries or new Smith attempts: **0**. Runtime campaign mutations: **0**. Push/merge: **0**.
