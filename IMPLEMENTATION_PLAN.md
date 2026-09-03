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

## 4. Foundation PR sequence (historical/superseded as active completion)

PR A–F below record the useful foundation sequence that established the
source, runtime, knowledge, taxonomy, model-task and reality-cohort spine.
They are completed or superseded foundation work where the repository state
supports that claim, not the current vNext completion definition. A fresh
implementation follows the complete-card domain/graph sequence below rather
than assuming identity/program/classification work is the product endpoint.

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
- seed metadata and fixtures for ACNC/ATO and SDGs; load restricted schemes such as CLASSIE only in private runtime when rights permit;
- version/deprecation tests.

Exclude full scheme harvesting if licensing or stable machine-readable sources require separate work.

**Stop condition:** assignment and mapping cannot be confused; multi-label and program scope work; exact mappings require explicit evidence/review.

### PR D - Identity/program mechanical pipeline

Implement deterministic work only:

- source record ingestion;
- identifier validation and exact joins;
- subject/scope creation;
- parsing, segmentation and preservation of explicit structured source-native program records;
- evidence bundles and coverage states;
- replay/idempotency.

PR D does not interpret unrestricted prose semantically or produce unrestricted semantic candidates. PR E owns program/service semantic identification and normalisation/decomposition, activities, SDGs, permitted taxonomy assignments and semantic evidence/relevance. One physical model request may return multiple independently governed logical task outputs when benchmarked; each retains independent validation and lineage.

### PR E — Typed classification model tasks

Implement task contracts for:

- program decomposition/normalisation;
- optional CLASSIE subject/population assignment, rights-gated and removable;
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
| Model-assisted | Open language/visual judgment | Program extraction, relevant evidence, permitted external/native taxonomy and SDG assignment; CLASSIE is optional and rights-gated |
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

## 10. Completion definition for the complete-card reality slice

The active slice is complete when a clean environment can demonstrate, across
representative bounded cases and without requiring every primitive for every
charity or section:

1. initialise a file-backed SQLite catalogue;
2. register sources and evidence artefacts;
3. process the fixed cohort through typed tasks;
4. represent the governed primitives demanded by the North Star as applicable:
   subjects and scopes, observations, assertions, directed relationships and
   roles, measurements, taxonomy assignments, matters/events,
   coverage/missingness states, review/adjudication state, evidence and
   lineage;
5. show source, prompt/model and cost lineage;
6. distinguish material missingness states including asserted none, observed
   absent, not found, source silent, source unavailable, not acquired, not
   processed, processing failed, not reviewed, not applicable, withheld,
   stale and unknown;
7. reproduce a private preview without duplicate artefacts or costs;
8. report development and untouched-holdout evidence without inventing a
   universal acceptance threshold;
9. preserve contract 0.5 unchanged;
10. stop without modifying Data or Viewer.

Builder/Data projections must preserve those missingness distinctions before
any Top-100 scale decision. They must not collapse them into one null, false,
`unknown` or generic `failed` state, although a given experiment need not
exercise every state.


## Classification-layer implementation authority

Builder vNext uses six distinct, versioned lenses rather than one taxonomy: ACNC Registration (separate purpose/subtype and beneficiary facets), ATO DGR (separate regulatory profile, including scoped endorsements), ACNC CLASSIE (AIS-year/profile-specific source reporting), UN SDG (program-first alignment), CharityGraph Native (multi-grain operational knowledge) and CharityGraph CLASSIE (independent program-first assessment against the selected Our Community release). ACNC CLASSIE and Our Community CLASSIE are never assumed version-identical; any relationship requires an explicit ConceptMapping.

Reporting-group is scope structure, not a classification lens. Assertions attach to the lowest evidence-supported group, legal entity, program or service and do not propagate automatically. Embeddings support retrieval and candidate mapping only.

Private CLASSIE payloads may be loaded, hashed and processed by Builder when lawfully injected at runtime. Taxonomy assignments carry independent publication eligibility and default to withheld. If publication permission is denied, CLASSIE tasks stop and dependent projections are withheld while native, ACNC, ATO, SDG, program/service and evidence knowledge remains intact.

## Complete-card architecture and sequencing rule

Acquire broadly once; preserve source-native evidence; freeze a reusable charity evidence corpus; assemble task-specific semantic packets; apply cost-efficient semantic passes; persist independently governed domain knowledge; compile analyst/public projections. Acquisition is charity/source oriented and semantic interpretation is domain/profile oriented. A physical request may bundle compatible logical tasks, but task identity, schema/profile, scope, evidence, validation, lineage and governed disposition remain independent. **BUILDER DOESN'T DO DISCOVERY:** semantic consumers use persisted reusable representations and do not invoke raw-document parsing or external search as an escape hatch. Do not create a giant opaque charity-analysis contract.

## NEXT IMPLEMENTATION SEQUENCE — COMPLETE-CARD REALITY SLICE

### Step 1 — Baseline source-set acquisition / corpus manifest

For each selected charity, attempt ACNC Register/AIS, ATO DGR, official website, latest annual report, Wikipedia/Wikimedia context and applicable fundraising registries. Record acquisition state by source family and claim family; hash retained artefacts; preserve role, time, rights and provenance; freeze a reusable charity-corpus manifest. Do not optimise acquisition for one domain.

### Step 2 — Source-native structured observations

Retain explicit ABN/ACNC identifiers, registration, purposes, DGR, AIS fields, filed financial values and reporting metadata mechanically. Do not route authoritative structured fields through an LLM merely for convenience.

### Step 3 — Stable document segmentation / evidence representations

Create reusable, bounded representations from annual reports, official sites, contextual pages and other retained prose using stable document/markup structure. Do not teach Python English or reacquire the same source per domain.

### Step 4 — Domain task contracts for remaining North Star profiles

Add typed contracts progressively over shared primitives, not twenty disconnected databases. The immediate bounded implementation order is:

1. shared subject/scope plus structured activity and relationship-role semantics
   where needed;
2. a direct-service pressure case covering sections 6/11/13;
3. an authoritative conduct/compliance pressure case for section 16;
4. an evaluation-rich pressure case for section 18;
5. the first bounded CharityGraph Native induction when corpus diversity is
   adequate; and
6. remaining specialist/domain hardening, including fundraising, ethos,
   commitments, governance/workforce/finance depth and other North Star gaps.

Then cover the remaining North Star profiles progressively: populations/geography, participation, fundraising, finance concepts beyond source-native facts, governance, workforce, capability/capacity, relationships, schemes/accreditations, ethos, commitments, context, outcomes/evaluation and appropriately governed conduct candidates. This is a bounded empirical progression, not an instruction to implement all 20 domains at once.

### Step 5 — Cross-domain packet experiments

From the same frozen corpus, compare one multi-domain packet, compatible bundles and narrower task packets only as needed to measure quality/cost trade-offs. Bundling physical calls never merges logical contract, validation or provenance.

### Step 6 — Independently governed logical result persistence

Persist observations, assertions, relationships, measurements, taxonomy assignments, matters/events and coverage observations as appropriate. Never persist one model-produced dossier as canonical truth.

### Step 7 — Whole-charity private dossier projection

Render a private analyst projection against `NORTH_STAR_TARGET_CARD.md`. Each section must show governed information, candidate/review-required information, explicit missingness/coverage, not applicable, or deliberately withheld/risk-gated state.

### Step 8 — Coverage / economics / review report

Report source and claim-family coverage, semantic success, review load, packet/corpus reuse, model cost, failure classes, right-tail effects and cross-domain synergies.

## Propagated complete-card implementation pattern

The selected pattern is: frozen corpus -> reusable representation -> whole-card
high-recall semantic knowledge -> persisted observations and relationships ->
task-specific taxonomy-blind views -> independent semantic lenses -> governed
projections. Structured activity/relationship roles must distinguish operator,
funder, sponsor, delivery partner and network context without semantic Python.
Production waves must be resumable and interruption-safe before sector-scale
execution; cache/reuse and staged QA precede breadth.

## Cross-domain acceptance test

A competent analyst should be able to inspect one charity and answer a broad set of North Star questions without rereading all primary sources, while tracing each material answer to its governed basis. Forcing-function questions include: whether the charity uses/employs/contracts face-to-face fundraisers; how much it spends on fundraising; and whether it is formally religiously affiliated or motivated and on what evidence. These are cross-domain questions, not privileged schema fields.

## Interruption-safe execution requirement

Before cohort scale, execution must be resumable without ambiguity. Durably persist task/measurement identity, authorization, transmission/send-boundary state, provider receipt, usage/cost, raw result receipt, structural validation, evidence-grounding validation and terminal task state. If transmission occurred but response or billing state is ambiguous, fail closed and do not resend merely because a lease expired or an artefact is absent. The halted Top-100 Terra attempt (ABN `48321126727`) is empirical motivation; never invent billed cost from transient output.
