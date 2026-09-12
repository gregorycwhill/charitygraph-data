# Phase 6 Capacity reality slice — execution packet

Status: completed provider run; all outputs are semantic candidates; human adjudication pending.

No candidate is promoted. Source retrieval timestamps are absent from the selected clean corpus manifests unless source text itself states a date. Treat dates and availability as source-bounded; do not infer present-day status.

## Subject and missingness register

| ABN | Subject | Request attempts | Candidate propositions | Explicit unavailable sources | Mechanical request status |
|---|---|---:|---:|---|---|
| `23082732027` | St Catherine's Aged Care Services | 1 | 7 | none recorded | fail |
| `32565549842` | St George Community Housing Limited | 2 | 18 | none recorded | fail, fail |
| `57057493017` | The Leukaemia Foundation of Australia Limited | 1 | 11 | none recorded | fail |
| `77054038872` | St Vincent's Hospital Sydney Limited | 2 | 22 | {"artifact_ids":[],"coverage_state":"source_unavailable","reason":"no usable retained bytes or source record; no replacement","recorded_state":"unavailable","source_family":"annual_report"} | fail, pass |
| `80009663478` | Royal Flying Doctor Service of Australia (Queensland Section) | 1 | 7 | none recorded | fail |
| `80931522157` | Starlight Children's Foundation Australia | 1 | 10 | none recorded | fail |

## Review procedure

Use `capacity-adjudication.csv` as the proposition-level worksheet. The original structured model outputs are in `raw-candidates/`; each row links by logical and physical attempt identity. Preserve separate replicate rows and make an explicit disposition for each proposition. `failure_category` remains pending until the reviewer assigns one.

The CSV records exact source locator IDs, source/artifact identity, source role, source date and capture-time status, quoted evidence, scope, candidate proposition, explicit missingness, mechanical checks, usage, and accounting. Mechanical validity is not semantic acceptance. Review against the approved slice rubric and failure taxonomy in [Phase 6 slice designs](../../../PHASE6_REALITY_SLICE_DESIGNS_2026-09-12.md).

## Analyst usefulness evaluation

See the shared `analyst-task-pairs.md`. The task pair materials are prepared only; no analyst task was run and no usefulness threshold is claimed.
