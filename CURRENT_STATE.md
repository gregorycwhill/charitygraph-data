# CharityGraph Current State

**Status date:** 24 August 2026

**Status:** Baseline for the next Builder vNext slice

## 1. Repositories and public deployment

| Component | Repository | Current recorded `main` | State |
|---|---|---|---|
| Builder | `gregorycwhill/charitygraph` | `8e4f2a099f7cb4a004a8ca8785f2f810a7d7d534` | Rebrand, contracts, SQLite ledger and future publication-identity support merged |
| Data | `gregorycwhill/charitygraph-data` | `9650781febfded436c00cbcddf9211a80a5babce` | Governance, brand/reuse and future release metadata merged |
| Viewer | `gregorycwhill/charitygraph-viewer` | `cd6f3720f664a29e0ca7ed8be19797e573fcdfc8` | Branding/reuse changes merged and Pages deployed |

Live Viewer: <https://gregorycwhill.github.io/charitygraph-viewer/>

Recorded successful deployment runs:

- deploy: `32675339409`;
- Pages build: `32675353657`.

## 2. Immutable public release

Public contract 0.5 remains the current immutable release boundary:

- release: `v0.5.0-2026-08-15`;
- 120 cards;
- 228 source records;
- 349 manifest artefacts;
- manifest SHA-256: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

Builder vNext must not rewrite that directory, schema or manifest.

## 3. Builder foundation implemented

The merged Builder includes minimum contracts for:

- canonicalisation and deterministic identifiers;
- knowledge lifecycle and directed promotion lineage;
- model tasks/results and provider boundary;
- deterministic fake provider;
- cost reservations, actuals, credits and reconciliation;
- future publication identity separated from the 0.5 adapter.

The SQLite v1 operational catalogue includes:

- `schema_migrations`;
- `cohorts`;
- `runs`;
- `tasks`;
- `task_attempts`;
- `operation_receipts`;
- `budget_reservations`;
- `reservation_tasks`;
- `cost_entries`;
- `cache_entries`;
- `artifact_index`.

Implemented invariants include attempt-only lifecycle, leases and retry eligibility; cohort/run/task scope; append-only cache events; artefact metadata idempotency; caller-keyed release operations; signed budget exposure; faithful overruns; and rejection of in-memory production catalogues.

## 4. Recorded merged-main validation

- full Builder suite: **203 passed, 1 skipped**;
- focused suite: **12 passed**;
- legacy compatibility: **2 passed**;
- future publication identity: **12 passed, 1 skipped**;
- warning-as-error imports: passed;
- brand lint: passed;
- `git diff --check`: passed.

Data tests were not rerun during the final merge operation under the approved merge instructions. Earlier branch validation passed for future schema/example and negative contract tests. Viewer suite and Pages build passed before deployment.

## 5. Licensing and branding

- Builder and Viewer: MIT;
- Data: CC BY 4.0;
- Data contains canonical brand/reuse guidance;
- licence permission is distinct from brand use and implied endorsement;
- future releases have publication-identity metadata and traversal-safe paths;
- no active public legacy branding remains;
- historical/immutable technical identifiers are preserved only where necessary.

## 6. Archaeology assets

The read-only archaeology identified:

- 3,977 files and approximately 1.435 GB;
- 2,575 structured artefacts;
- 299 model/LLM synthesis-cache files;
- 29 governed/human artefacts;
- 1,491 `legacy_unbound` items across 114 subjects;
- 92 evidence-recoverable but review-required items;
- 1,399 unresolved items;
- zero mechanically rebound or promoted.

These are evidence assets, not a production architecture. They should be indexed, sampled and selectively rebound through governed vNext contracts. Do not copy the whole archaeology tree into each run or treat old final-looking files as canonical without lineage.

Three Builder archaeology reports and Viewer `debug.log` were recorded as pre-existing untracked material and must remain untouched unless a separate approved housekeeping task addresses them.

## 7. What is not implemented

The merged foundation does not yet provide:

- the complete vNext knowledge schema or persistence for assertions/evidence;
- content-addressed evidence-store integration;
- production source registry and acquisition connectors;
- real provider/model execution through the new task contracts;
- cohort ranking and scheduled budget orchestration;
- optional CLASSIE, SDG, participation, fundraising or native activity population; CLASSIE remains rights-gated and non-foundational;
- community challenge workflow;
- a public vNext release or Viewer projection;
- direct-observation collection tooling.

## 8. Immediate readiness conclusion

The project is ready for a small private vertical slice. It is not ready for sector-wide ingestion or public vNext publication. The next task should prove that the contracts, SQLite control plane, evidence storage and model judgment work together on real evidence without rebuilding the old heuristic loop.
