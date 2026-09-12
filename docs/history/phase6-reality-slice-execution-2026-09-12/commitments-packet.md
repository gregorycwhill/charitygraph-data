# Phase 6 Commitments reality slice — execution packet

Status: completed provider run; all outputs are semantic candidates; human adjudication pending.

No candidate is promoted. Source retrieval timestamps are absent from the selected clean corpus manifests unless source text itself states a date. Treat dates and availability as source-bounded; do not infer present-day status.

## Subject and missingness register

| ABN | Subject | Request attempts | Candidate propositions | Explicit unavailable sources | Mechanical request status |
|---|---|---:|---:|---|---|
| `32565549842` | St George Community Housing Limited | 1 | 6 | none recorded | pass |
| `50169561394` | Australian Red Cross Society | 2 | 11 | none recorded | fail, fail |
| `61002643852` | Greenpeace Australia Pacific Limited | 1 | 10 | none recorded | fail |
| `61426486715` | Cancer Council Victoria | 1 | 8 | none recorded | fail |
| `65069482829` | The Trustee for Channel 7 Telethon Trust | 2 | 14 | {"artifact_ids":["srcblob:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"],"coverage_state":"source_unavailable","reason":"no usable retained bytes or source record; no replacement","recorded_state":"partial","source_family":"official_website"} | fail, fail |
| `65159324697` | The Sunrise Project Australia Limited | 1 | 9 | none recorded | pass |

## Review procedure

Use `commitments-adjudication.csv` as the proposition-level worksheet. The original structured model outputs are in `raw-candidates/`; each row links by logical and physical attempt identity. Preserve separate replicate rows and make an explicit disposition for each proposition. `failure_category` remains pending until the reviewer assigns one.

The CSV records exact source locator IDs, source/artifact identity, source role, source date and capture-time status, quoted evidence, scope, candidate proposition, explicit missingness, mechanical checks, usage, and accounting. Mechanical validity is not semantic acceptance. Review against the approved slice rubric and failure taxonomy in [Phase 6 slice designs](../../../PHASE6_REALITY_SLICE_DESIGNS_2026-09-12.md).

## Analyst usefulness evaluation

See the shared `analyst-task-pairs.md`. The task pair materials are prepared only; no analyst task was run and no usefulness threshold is claimed.
