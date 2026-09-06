# CharityGraph Builder vNext Implementation Plan

**Status:** Canonical implementation sequence, version 2.2-draft

**Active scope:** Phase 4 — cross-domain semantic packaging and economics

The former Phase 3 closeout sequence below is retained as completed history.

**Authoritative immediate scope:** Phase 4 - cross-domain semantic packaging and economics. The legacy immediate-scope label below is superseded and retained only as historical wording.

**Immediate scope:** Phase 3 closeout — integrated complete-card graph and private projection

## 1. Delivery rule

Native overlay induction and promotion constraints are governed by [CHARITYGRAPH_NATIVE_ARCHITECTURE.md](CHARITYGRAPH_NATIVE_ARCHITECTURE.md); no V4 implementation or completed facet lifecycle is implied by the parked V1–V4R experiments.

Implement in bounded, substantive PRs that each close a meaningful vertical or infrastructural question. Do not implement the entire conceptual model, migrate the archaeology tree or publish vNext in one tranche. Do not turn every repair into a giant implementation tranche.

Absorb local implementation defects inside the tranche when experimental integrity remains intact; do not turn every repair into a new project checkpoint.

After two consecutive implementation/debugging tranches produce no new product, semantic or architectural learning, explicitly reassess whether the work remains on the critical path.

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

Experiment orchestration belongs outside the importable production package unless a component has earned promotion into reusable Builder infrastructure. An illustrative layout is `experiments/semantic_labs/` and `experiments/native/`, with exact paths adapting to repository conventions. Existing Native experiment modules under `src/charitygraph/` are **EXPERIMENT LOCATION DEBT — FIX BEFORE MERGE / MILESTONE CLEANUP**. That cleanup is not part of this tranche.

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
| Model-assisted | Constrained extraction/mapping/classification against substantially specified structure; or judgement/abstraction involving ambiguity, semantic quality, boundary adjudication or constructive abstraction | Program extraction, relevant evidence, permitted external/native taxonomy and SDG assignment; CLASSIE is optional and rights-gated |
| Human-reviewed | Consequence, cultural authority or unresolved contradiction | High-risk conduct, Indigenous governance, material disputes |
| Deferred | No sufficient value or evidence in the slice | Full outcome scoring, sector-wide direct observation |

A field may move method only through a documented decision and evaluation result.

Current working evidence is that lower-cost models are suitable defaults for high-volume constrained semantic work, while stronger-reasoning models should be preferred or tested for difficult adjudication and constructive abstraction. Python owns deterministic identity, provenance, schema, persistence and invariants. Human review owns high-consequence, cultural-authority and unresolved cases, plus product priority and stopping. Named models such as Luna, Terra and Sol remain configurable implementation choices, not permanent product policy. Route by task difficulty, not pipeline stage.

A bounded V5RR lesson is: a null from a constrained lower-capability model is valid output, but on a constructive abstraction task it is not automatically strong negative evidence about the underlying corpus. This does not establish that Terra is superior for every abstraction task.

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

For the immediate integration closeout, first use approximately 2–3 already-rich reality charities with frozen evidence and reusable valid outputs rather than acquiring a fresh broad cohort. Retain the broader varied-charity cohort as the eventual Phase 3 reality-cohort design.

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

A local defect is not an experiment stop if it can be fixed without corrupting evidence, identity, billing, holdout isolation or production state. Reserve true stops for material conditions such as corpus corruption, campaign-scale identity corruption, ambiguous duplicate billing/resend risk, hard budget breach risk, holdout leakage, private/public contamination or production contamination.

## 8. Cost controls

- dry-run task plans before paid execution;
- use fake/recorded providers for implementation tests;
- content-hash prompts and evidence inputs;
- cache only when task contract, model policy and inputs permit reuse;
- reserve before calls and persist actuals/credits;
- cap experimental runs separately from production cohort envelopes;
- print a projected/actual cost report for every run;
- never commit credentials or provider payloads containing private material.

Optimise useful semantic/product learning per unit of total cost of intelligence: model, agent and human attention, not minimum token cost. A more capable model at a narrow judgement bottleneck may be economically preferable if it avoids repeated implementation or supervision loops.

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

The integrated slice must also demonstrate coherent cross-domain subject/scope ownership; directed relationships and roles surviving persistence and projection; governed information plus explicit missingness across the North Star projection; a private projection compiled from governed knowledge rather than stored as a mega-record; and operator, deliverer, funder, sponsor, partner, auspice and network-context roles where evidence supports them.

Builder/Data projections must preserve those missingness distinctions before
any Top-100 scale decision. They must not collapse them into one null, false,
`unknown` or generic `failed` state, although a given experiment need not
exercise every state.


## Classification-layer implementation authority

Builder vNext uses six distinct, versioned lenses rather than one taxonomy: ACNC Registration (separate purpose/subtype and beneficiary facets), ATO DGR (separate regulatory profile, including scoped endorsements), ACNC CLASSIE (AIS-year/profile-specific source reporting), UN SDG (program-first alignment), CharityGraph Native (multi-grain operational knowledge) and CharityGraph CLASSIE (independent program-first assessment against the selected Our Community release). ACNC CLASSIE and Our Community CLASSIE are never assumed version-identical; any relationship requires an explicit ConceptMapping.

Reporting-group is scope structure, not a classification lens. Assertions attach to the lowest evidence-supported group, legal entity, program or service and do not propagate automatically. Embeddings support retrieval and candidate mapping only.

Private CLASSIE payloads may be loaded, hashed and processed by Builder when lawfully injected at runtime. Taxonomy assignments carry independent publication eligibility and default to withheld. If publication permission is denied, CLASSIE tasks stop and dependent projections are withheld while native, ACNC, ATO, SDG, program/service and evidence knowledge remains intact.

CharityGraph Native remains optional, sparse, facet-based and experimental. The real V5RR quality/workshop lifecycle executed through catalogue freeze: 135 clean training overlays received real Terra quality review; operational activity, participation and fundraising mode qualified mechanically and substantively for workshop entry; six Luna/none discovery calls returned zero concepts; final catalogues were empty; four Luna holdout-extraction calls over 36 canonical holdout objects returned zero overlays; transfer therefore remained untested. No Native production catalogue or product exposure is implied. Native is parked, not an active Phase 3 blocker.

## Complete-card architecture and sequencing rule

Acquire broadly once; preserve source-native evidence; freeze a reusable charity evidence corpus; assemble task-specific semantic packets; apply cost-efficient semantic passes; persist independently governed domain knowledge; compile analyst/public projections. Acquisition is charity/source oriented and semantic interpretation is domain/profile oriented. A physical request may bundle compatible logical tasks, but task identity, schema/profile, scope, evidence, validation, lineage and governed disposition remain independent. **BUILDER DOESN'T DO DISCOVERY:** semantic consumers use persisted reusable representations and do not invoke raw-document parsing or external search as an escape hatch. Do not create a giant opaque charity-analysis contract.

## Completed Phase 3 bounded pressure work

- Sections 6/11/13: boundedly pressure-tested.
- Section 15: architecture-validated, semantic-boundary-tested, parked and not production-complete.
- Section 16: bounded high-consequence representation/review path pressure-tested.
- Section 18: generic Compact → specialist architecture reality-tested and parked.
- Section 19 Native: overlay/workshop lifecycle reality-tested through freeze; holdout eligibility was zero under the current contract; transfer was untested; parked.

Phase 3 is complete at bounded reality-test level, not production-complete.
PR #57 established the canonical North Star projection, explicit
subject-specific missingness, the 20 × 3 private coverage matrix and
quarantine of incompatible historical section IDs. PR #58 established real
retained Australian Red Cross `operator` evidence for Australian Red Cross
Society →operator→ Telecross and Telechat, durable source/service subjects,
typed directed relationship persistence/reload preserving direction, role,
scope, evidence and lineage, and durable Section 12 projection without
duplicating canonical state. Native remains parked and experimental.

The following integrated Phase 3 sequence is completed historical record; the
active Phase 4 sequence appears below the historical steps.

## NEXT IMPLEMENTATION SEQUENCE — INTEGRATED PHASE 3 CLOSEOUT

### Step 1 — Select 2–3 rich existing reality charities

Use frozen existing evidence and reusable valid results. No fresh broad paid cohort.

### Step 2 — Assemble existing governed knowledge across the North Star

Inventory valid existing knowledge across Sections 1–20. Reuse compatible prior results rather than rerunning them.

### Step 3 — Persist the actual cross-domain graph

Stress subject/scope ownership and relationships across programs, populations/geography, participation, finance, governance/workforce, capability/access, ecosystem relationships, schemes, commitments/conduct/outcomes and classifications wherever evidence exists. Preserve operator, deliverer, funder, sponsor, partner, auspice and network-context roles where supported.

### Step 4 — Compile the private North Star inspection projection

Every section should project one or more governed states such as:

- governed knowledge;
- candidate/review required;
- source silent;
- unavailable;
- not acquired;
- not processed;
- not applicable;
- withheld/risk-gated;
- stale; or
- other governed missingness.

The projection is compiled, not stored as canonical truth.

### Step 5 — Diagnose actual gaps

New specialist/domain work becomes **gap-triggered**. Fundraising, workforce, ethos, notable context and other comparatively light North Star areas are not an automatic sequential Lab queue. Only authorise a specialist tranche when the integrated card exposes a material representation, scope, semantic or projection problem.

### Step 6 — Close Phase 3 or run one targeted repair tranche

If integrated cards satisfy the Phase 3 gate, close Phase 3. If a material cross-domain structural problem prevents closure, run the smallest substantive targeted tranche necessary, then repeat the integrated projection.

### Step 7 — Phase 4 cross-domain packet economics

Move packet/bundling experiments after integrated-card proof. Only then compare large multi-domain packets, compatible bundles and narrow tasks. Measure semantic yield per dollar and total supervision burden, not merely call count.

### Step 8 — Coverage/economics/review report

Report source/claim-family coverage, semantic success, review load, corpus reuse, model cost, failure classes, cross-domain synergies and operational/supervision burden.

## ACTIVE IMPLEMENTATION SEQUENCE — PHASE 4 CROSS-DOMAIN SEMANTIC PACKAGING AND ECONOMICS

### Step 1 — Select existing rich frozen corpora

Use already-acquired and reusable evidence where possible. Do not begin with a
fresh broad cohort.

### Step 2 — Define logical semantic tasks independently

Each domain/profile retains task identity, schema, subject/scope, source and
evidence contract, validation, lineage and governed disposition.

### Step 3 — Construct packaging variants

Compare only evidence-justified variants: one large cross-domain packet, a
small number of compatible bundles and narrower task-specific packets. Fewer
calls are not assumed to be better.

### Step 4 — Route models by task difficulty

Use lower-cost capable models for constrained/high-volume semantic labour;
stronger reasoning for difficult adjudication or abstraction where justified;
Python for deterministic mechanics; supervisory reasoning for integration; and
humans for purpose, high-consequence review, sufficiency and stopping. Named
models are implementation choices, not product policy.

### Step 5 — Measure total cost of intelligence

Report provider spend, semantic yield, precision/recall where assessable,
validation failures, review load, agent/Codex intervention, human supervision,
latency where useful, reuse/caching, failure modes and cross-domain
synergy/interference.

### Step 6 — Select a bounded Factory candidate

At Phase 4 end, recommend the simplest packaging/routing pattern justified for
the subsequent Top-100 full-card build. Do not start Phase 5 here. Keep
interruption-safe execution a prerequisite before paid cohort scaling.

No Phase 4 experiment is authorised by this documentation closeout.

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

Experiment-specific machinery such as Native catalogue reload, freeze and reconciliation layers is not automatically production infrastructure. Promote such mechanisms only when independently required by production semantics.
