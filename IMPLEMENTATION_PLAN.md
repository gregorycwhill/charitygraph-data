# CharityGraph Builder vNext Implementation Plan

**Status:** Canonical implementation sequence, version 2.0-draft

**Immediate scope:** First private reality slice only

## 1. Delivery rule

Implement in small PRs that each close a testable vertical or infrastructural gap. Do not implement the entire conceptual model, migrate the archaeology tree or publish vNext in one tranche.

Every PR begins from current `main`, names its authority documents and declares:

- included behaviour;
- explicit exclusions;
- fixtures/evaluation cases;
- acceptance tests;
- files allowed to change;
- immutable boundaries;
- stop conditions.

## 2. Target architecture

| Layer | Responsibility | Initial technology |
|---|---|---|
| Source registry | Authority, rights, cadence, connector policy | Versioned configuration/models |
| Acquisition | Retrieval and receipts | Python connectors, no semantic interpretation |
| Artefact store | Immutable raw/derived evidence | Content-addressed files |
| Operational control | Cohorts, runs, tasks, attempts, budgets, cache, artefact index | Existing SQLite runtime |
| Knowledge store | Observations, assertions, relationships, assignments, adjudications | SQLite tables plus file references for large payloads |
| Model boundary | Typed semantic tasks/results | Existing provider contracts; fake provider first, real provider later |
| Validation/evaluation | Invariants, golden cases, holdout, metrics | Pytest and deterministic report generation |
| Private projection | Human-reviewable slice result | JSON plus Markdown/HTML report, outside public Data |
| Public publication | Versioned Data bundle and Viewer | Deferred until release-candidate phase |

SQLite is the local control and query plane. Large document bodies, OCR, prompt inputs/outputs and other bulky artefacts remain content-addressed files referenced by the catalogue.

## 3. Initial repository layout

The exact names may adapt to existing conventions, but responsibilities should remain separated:

```text
src/charitygraph/
  runtime/                 # existing SQLite operational catalogue
  sources/                 # registry and bounded connectors
  evidence/                # artefact addressing and evidence locators
  knowledge/               # observations, assertions, relationships, lifecycle
  taxonomy/                # scheme registry, concepts, mappings, assignments
  model_tasks/             # typed semantic task definitions and orchestration
  profiles/                # identity/program/classification profile logic
  projections/             # private review and future public projections
tests/
  contracts/
  runtime/
  sources/
  evidence/
  knowledge/
  taxonomy/
  profiles/
  evaluation/
```

Runtime databases, caches, downloaded bodies, model payloads and generated previews live under configured runtime/archive roots and are ignored by Git. Durable design and small synthetic fixtures belong in Git. Archaeology reports stay where explicitly governed; they are not automatically committed.

## 4. PR sequence

### PR A — Evidence store and source registry

Implement:

- `SourceDefinition`, `SourceAuthorityRole`, rights/privacy/publication policy;
- `AcquisitionReceipt` and acquisition outcome semantics;
- content-addressed artefact paths and metadata;
- evidence locators for structured fields and text spans;
- SQLite migrations/index methods needed for source/evidence references;
- synthetic fixtures and idempotency/integrity tests.

Exclude network retrieval and real archive migration.

**Stop condition:** same content is not duplicated; different material metadata is not silently treated as identical; unsafe paths and secret-bearing provenance are rejected.

### PR B — Knowledge primitives and lifecycle persistence

Implement the minimum slice primitives:

- subject and external identifier;
- subject scope;
- party role;
- observation;
- assertion;
- relationship statement;
- adjudication decision;
- exact directed lineage;
- absence/outcome states.

Reuse current contract semantics. Do not add every domain entity.

**Stop condition:** accepted, edited, superseded, contradicted and withdrawn states reconstruct exactly; append-only history is preserved.

### PR C — Taxonomy registry and assignments

Implement:

- scheme/version/concept registry;
- external identifiers, labels and definitions;
- concept mapping predicates;
- scoped taxonomy assignment assertions;
- assignment method, evidence, rationale and confidence;
- seed fixtures for ACNC/ATO, CLASSIE and SDGs sufficient for the slice;
- version/deprecation tests.

Exclude full scheme harvesting if licensing or stable machine-readable sources require separate work.

**Stop condition:** assignment and mapping cannot be confused; multi-label and program scope work; exact mappings require explicit evidence/review.

### PR D — Identity/program mechanical pipeline

Implement deterministic work only:

- source record ingestion;
- identifier validation and exact joins;
- subject/scope creation;
- bounded program candidate extraction from structured or clearly segmented inputs;
- evidence creation and coverage states;
- replay/idempotency.

Use model-task requests for unresolved language work; do not add general prose heuristics.

### PR E — Typed classification model tasks

Implement task contracts for:

- program decomposition/normalisation;
- CLASSIE subject/population assignment;
- operational-activity assignment;
- UN SDG alignment;
- evidence/rationale selection;
- relevancy screening where needed.

First validate with the deterministic fake provider and recorded fixtures. Then add one real provider adapter behind explicit credentials/configuration and dry-run controls.

Model outputs must be schema-valid, evidence-bound and allowed to make reasonable primary/secondary judgments. Mechanical code may reject invalid structure or impossible references; it must not rewrite semantic conclusions through hidden keyword rules.

### PR F — Reality cohort runner and private preview

Implement:

- versioned ten-charity cohort manifest;
- run/task scheduling through SQLite;
- portfolio budget and per-task reservation use;
- cache and retry policy;
- private JSON and human-readable review projection;
- coverage/economics/evaluation report;
- holdout execution separated from development cases.

No public Data or Viewer changes.

## 5. Method matrix

Before each field is implemented, assign one method:

| Method | Use | Examples |
|---|---|---|
| Deterministic | Stable syntax, exact arithmetic or identifiers | ABN validation, content hashes, exact joins, totals |
| Model-assisted | Open language/visual judgment | Program extraction, relevant evidence, CLASSIE/SDG assignment |
| Human-reviewed | Consequence, cultural authority or unresolved contradiction | High-risk conduct, Indigenous governance, material disputes |
| Deferred | No sufficient value or evidence in the slice | Full outcome scoring, sector-wide direct observation |

A field may move method only through a documented decision and evaluation result.

## 6. Reality cohort design

Select about ten organisations covering:

- simple single-entity charity;
- multi-entity or group structure;
- small volunteer-led organisation;
- Indigenous or culturally governed organisation, with appropriate review boundaries;
- grantmaker;
- advocacy organisation;
- multi-program national organisation;
- service provider with multiple sites;
- fundraising-intensive charity;
- organisation with evaluation or materially adverse evidence.

Use public evidence already lawfully available, plus a carefully selected subset of archaeology evidence. Freeze subject identifiers and expected source families before coding. Do not tune against the holdout subset.

## 7. Error-handling strategy

Classify failures as:

- acquisition/access;
- parsing/format;
- identity/scope;
- insufficient evidence;
- model schema/invalid citation;
- semantic classification;
- persistence/idempotency;
- budget/provider;
- projection/publication;
- policy/review.

Fix a class only when the change is supported by multiple examples or a clear invariant. A novel phrase is not itself a new parser requirement.

## 8. Cost controls

- dry-run task plans before paid execution;
- use fake/recorded providers for implementation tests;
- content-hash prompts and evidence inputs;
- cache only when task contract, model policy and inputs permit reuse;
- reserve before calls and persist actuals/credits;
- cap experimental runs separately from production cohort envelopes;
- print a projected/actual cost report for every run;
- never commit credentials or provider payloads containing private material.

## 9. Documentation in each PR

Each PR updates only the documentation made true or invalid by the code. Architectural changes receive an ADR. Evaluation results are versioned reports with cohort, model/prompt and code identity. Working notes do not silently become product authority.

## 10. Completion definition for the first slice

The slice is complete when a clean environment can:

1. initialise a file-backed SQLite catalogue;
2. register sources and evidence artefacts;
3. process the fixed cohort through typed tasks;
4. create scoped identity, program and classification assertions;
5. show source, prompt/model and cost lineage;
6. distinguish resolved, unknown, not-applicable, not-attempted and failed fields;
7. reproduce a private preview without duplicate artefacts or costs;
8. pass development and untouched-holdout thresholds;
9. preserve contract 0.5 unchanged;
10. stop without modifying Data or Viewer.
