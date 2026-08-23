# CharityGraph Product Contract

**Status:** Canonical shared product contract  
**Version:** 1.1-draft  
**Date:** 2026-08-23  
**Applies to:** Builder, Data and Viewer

## 1. Public promise

> **CharityGraph is the one-stop shop for structured, governed Australian charity data.**

CharityGraph integrates public information about Australian charities, their programs, activities, beneficiaries, geography, finances, fundraising, relationships, organisational character and notable context. It turns fragmented public material into structured, evidence-backed, versioned and contestable data for people, analysts, software and AI systems.

“One-stop shop” means one governed integration and interpretation layer. It does not mean one source, one table, one universal taxonomy, one stored mega-card or complete knowledge about every charity.

## 2. Product purpose

Public charity information is spread across regulators, tax records, annual reports, websites, public inquiries, reference sources and specialist sector sources. Even when technically public, it is expensive to find, join, read and interpret.

CharityGraph reduces that cost through a Python-controlled, model-assisted transformation:

```text
public sources → source-native records → bounded evidence → governed observations → public projections
```

Its distinctive value is broad semantic integration with provenance. It does not merely copy sources and does not hide the sources behind synthesis. LLMs are a routine production component for difficult extraction, semantic judgement and public writing; Python supplies the control plane that makes their use repeatable, economical and testable.

## 3. Anchor user and first-class users

### 3.1 Anchor design user: analyst or consultant

CharityGraph is designed first to support rigorous analytical work by philanthropic advisers, foundation staff, social-purpose consultants, service-system planners, researchers, journalists and charity advisers.

An analyst should be able to:

- construct a defensible universe of organisations and programs;
- determine who does what, for whom, where and through which intervention;
- compare periods and scopes without equating unlike values;
- map service ecosystems and organisational relationships;
- examine financial, funding and fundraising patterns;
- locate evidence, exceptions, gaps and changes;
- reuse the data in spreadsheets, SQL, Python, R and BI tools.

Analyst-grade data is also a strong substrate for funders, consumer LLMs and downstream products. CharityGraph may enable commercial reuse without producing client-specific recommendations, prospect scores or proprietary consulting methods.

### 3.2 Funders and downstream personal agents

Funders use CharityGraph for discovery, comparison and diligence. A downstream personal agent may use it to apply the principal's mandate, exclusions and tolerances.

CharityGraph makes a subject or program **mandate-adjudicable** by supplying evidence-backed ingredients. It does not adjudicate a person's mandate or publish universal fit conclusions.

### 3.3 Product builders

Builders use stable identities, schemas, releases, bulk data, selective representations, provenance, coverage and corrections as a charity-intelligence layer.

### 3.4 Charities and advisers

Charities inspect how public information has been represented, follow the evidence, provide attributed self-description and challenge errors or stale interpretations. They do not receive editorial control over supported independent observations.

### 3.5 Public users

Public users inspect a restrained, evidence-oriented Viewer. The Viewer is a reference interface, not a marketplace.

## 4. Question scales and channels

Question scale and delivery channel are independent.

### Scales

- **Organisation:** understand and inspect one subject.
- **Program/service:** understand a scoped activity, service, unit, appeal or initiative.
- **Portfolio/comparison:** compare a defensible set while preserving scope and period.
- **Ecosystem/corpus:** analyse who works on what, for whom and where, including relationships and coverage gaps.

### Channels

- Viewer and public web pages;
- general-purpose consumer LLMs;
- spreadsheets, SQL, Python, R, BI and Parquet;
- JSON, JSONL and downstream product integration;
- future API or MCP access only when demand justifies it.

Static public artefacts remain useful without specialised integration.

## 5. Canonical product question

CharityGraph should progressively enable this question:

> Which Australian organisations or programs work on problem X, for beneficiary group Y, in geography Z, through what activities or interventions; how are they structured, funded and raising money; what organisational ethos or notable context may matter; and what evidence, recency, uncertainty and coverage qualify the answer?

CharityGraph supplies the charity-side supply map. Population need, unmet demand, causal impact and funding-allocation optimisation normally require external datasets and downstream analysis.

## 6. Subject identity and scope

CharityGraph subjects have stable opaque `subject_id` values independent of ABN, ACNC registration, ACN, name, website or any other external identifier.

Supported subject kinds include organisation, organisation group, legal entity, organisational unit, fund and program. Registrations and tax statuses are roles or observations, not subject kinds.

Source records have identities independent of CharityGraph subjects. A binding records status, basis, confidence, supporting and conflicting evidence, review state and time. A name or domain alone never creates or binds a subject.

Programs, services and organisational units may initially use governed subject-local scope. They become durable subjects only when cross-source identity or another demonstrated use case justifies governed promotion and an explicit relationship.

Artefact lineage is distinct from real-world relationships among organisations, groups, programs, funders, providers, networks and predecessors or successors.

## 7. Knowledge model

Builder's internal canonical knowledge consists of governed typed observations attached to subjects and scopes. A CharityGraph Card is a stable public product object compiled for a specific release from selected observations, coverage assessments and derivatives.

The internal process separates:

- source blob;
- source-native record;
- subject binding;
- evidence fragment;
- candidate observation;
- governed decision;
- canonical observation;
- coverage assessment;
- derivative;
- release projection.

All public representations of one release must agree on shared values, but no single stored card is Builder's universal source of truth.

## 8. Product domains

### 8.1 Identity and regulatory status

Legal, display, operating and former names; external identifiers; registrations; entity and tax/DGR status; lifecycle; and source bindings.

### 8.2 Structure and relationships

Groups, legal entities, units, funds, programs, services, parents, networks, auspice, delivery/funding/provider relationships, merger, split, predecessor and successor.

### 8.3 Work and reach

Activities, beneficiaries, programs/services, causes/problems, interventions/approaches, cause centrality, delivery modes and role-specific geography.

Cause centrality is evidence-backed and uses `primary`, `material`, `incidental` or `unknown`. It is not taxonomy adjacency or a donor-fit score.

### 8.4 Resources and operations

Longitudinal financial statements and metrics, workforce and volunteers, and explicitly reported service volume, capacity, eligibility or operating context where available.

### 8.5 Funding and fundraising

Keep four domains separate:

1. funding source;
2. standing fundraising practice;
3. fundraising campaign;
4. fundraising expenditure.

Source-reported campaign amounts and counts retain their wording, period and scope. They do not silently reconcile to accounts or become CharityGraph ROI, efficiency or causal-attribution measures.

Fundraising expenditure follows the governed ladder: direct disclosure; deterministic reconstruction; defensible bounds or specifically governed interpretation; otherwise unavailable/null. There is no universal prior, peer fill, forced point or automatic midpoint.

### 8.6 Character and context

**Ethos** records worldview, tradition, affiliation or institutional orientation through separately attributed self-description, formal affiliation, external characterisation and historical origin.

**Service or mission orientation** separately records whether and how ethos enters service access, culturally specific delivery, worship, formation, proselytising, advocacy or program design.

Beneficiary identity never supplies an ethos inference.

**`notable_context`** records bounded institutional, historical, legal, regulatory, inquiry, recognition, criticism or relationship facts. It is never a reputation, prestige, controversy, safety or notability score. Sensitive observations require adequate underlying evidence, precise procedural status, a versioned risk policy and expedited correction handling. The policy may require human review, stronger-model adjudication or publication hold; universal human review is not a prerequisite for useful coverage.

### 8.7 Participation and action

Participation is a current core domain and should be populated from initial production processing. It includes donating, volunteering, working bees, membership, public events, boards/committees and other supported engagement modes.

Stable participation modes remain distinct from transient opportunities. Opportunities retain status, effective dates, freshness and verified action destinations distinct from evidence URLs.

CharityGraph structures participation data; it does not operate an engagement or volunteering marketplace.

### 8.8 Taxonomies and semantics

Multiple taxonomies coexist. Each classification records taxonomy, version, stable term, assignment method, scope, evidence and confidence where meaningful.

ACNC purpose and beneficiary classifications remain source-native and distinct from the CharityGraph-native taxonomy. The native taxonomy begins from the governed seven-dimension v0 evidence base—cause/problem, beneficiary, activity, approach, participation, geography and organisational character—but evolves only through versioned governance.

Embeddings and similarity are descriptive navigation artefacts, not recommendations.

## 9. Source model and authority

CharityGraph uses authoritative regulators, organisation self-report, independent sources, community-maintained references, governed contributions, deterministic derivations and approved model-assisted interpretation.

Authority attaches to a proposition and source role, not universally to a publisher.

Evaluated industry shadow registries are first-class sources for the facts their institutional systems establish, including membership or registration status, applicable categories, fees, levies, codes, dates and semantically entailed practices. A code establishes applicable obligations, not compliance. A fee rule establishes the rule, not a member-specific amount or volume without further evidence.

Awards, benchmarks, agency case studies, platforms and listed-provider disclosures may directly establish named campaigns, relationships, reported amounts or events. Promotional effectiveness, uplift, conversion and ROI claims remain source-native/noncanonical unless a separate policy is approved.

Public accessibility does not by itself authorise bulk republication. Every source family has an access, rights, attribution, retention, refresh and public-projection policy.

## 10. Evidence, provenance and time

Material observations identify appropriate source records and evidence. Claim basis explains why CharityGraph can state the proposition; extraction method explains how evidence was recovered. A source fact recovered through OCR, vision or an LLM can remain direct.

Relevant times include retrieval, source publication, reporting period, effective/event time, observation, assessment, generation and release. Current projections never erase history.

Conflicting legitimate observations remain visible with reconciliation status. They are not silently collapsed into one scalar.

## 11. Coverage and sparse knowledge

Every applicable capability has an explicit current state such as observed, not found in assessed sources, unavailable from source, not applicable, retrieval failed, not yet processed, stale or unknown.

`not_found_in_source` is valid only for a defined assessment scope and never means that a practice, characteristic or event does not exist. Missing output is not a negative claim.

Sparse output is correct when public evidence is genuinely sparse or responsible publication is not possible. It is a product failure when recoverable public evidence remains unprocessed because the pipeline optimised for near-zero risk, elaborate local NLP or universal human review instead of useful coverage.

## 12. Corrections and contestability

Published records are generated outputs. Raw correction submissions remain private by default. Moderation may create governed proposals and decisions suitable for public projection.

Accepted corrections change governed inputs or observations and trigger dependent rebuilds. Corrections do not manually overwrite final JSON, Markdown or Viewer content.

History is append-only except where privacy, abuse, legal requirements or accidental sensitive publication require exceptional removal. A material challenge to sensitive context triggers expedited re-review.

## 13. Economics, processing priority and model use

CharityGraph is Python-controlled and LLM-powered. Python performs acquisition, hashing, obvious deterministic extraction, joins, evidence selection, batching, scheduling, caching, validation, cost enforcement and publication. LLMs routinely perform difficult OCR/vision recovery, relevance screening, structured extraction, semantic interpretation, classification and bounded writing. Model-derived outputs remain source-bound, typed, reviewable and correctable.

The initial corpus uses three pooled paid-model budgets. Each budget includes text and vision inference, judgement, extraction, writing, embeddings, retries and escalations:

| Processing cohort | Selection | Total budget | Average planning allowance |
| --- | --- | ---: | ---: |
| first 100 | highest total donations | AUD 100 | AUD 1.00/charity |
| next 1,000 | next highest total donations | AUD 100 | AUD 0.10/charity |
| next 10,000 | next highest total donations | AUD 100 | AUD 0.01/charity |

Total donations is recorded as `donor_decision_exposure_proxy`: a transparent processing-priority proxy for the number and consequence of donor decisions that may rely on CharityGraph. It is not a donor count, a measure of retail donations, charity merit, credibility, effectiveness or recommendation. The highest-exposure cohort receives more model spend and assurance because errors are more likely to encounter active brand/legal scrutiny; later cohorts emphasise economical coverage.

Budgets are pooled within cohorts. Easy subjects may subsidise difficult ones. Cross-cohort transfer requires explicit approval. Builder reserves estimated cost before a request, reconciles actual cost afterwards and stops new paid work before a cohort cap can be exceeded.

Coverage is the optimisation objective; defensibility is a constraint. Prefer a source-linked, method-labelled model interpretation with stated uncertainty to a null selected only because it is legally safer. A high-precision system that publishes almost nothing fails the product contract.

Custom local NER, relevance, taxonomy or summarisation models are not part of the initial build. Deterministic parsing and off-the-shelf OCR remain useful. A custom local NLP component may enter the roadmap only after a benchmark shows lower total cost of ownership, including implementation, labels/evaluation, maintenance and operational complexity—not merely lower API spend.

## 14. Public releases and distribution

Public releases are immutable, versioned and publication-allowlisted. They include schemas, manifests, hashes, provenance, capability definitions, machine-readable formats and stable selective representations.

Builder produces complete validated release candidates. Data owns public release artefacts. Viewer consumes an explicitly selected release and never private Builder state.

Raw reports, website snapshots, model prompts/responses, private correction submissions, credentials, operational databases, caches and spend telemetry are private by default.

## 15. Non-goals

CharityGraph is not:

- a charity recommender, ranker, rater or allocation engine;
- an impact, effectiveness, reputation or fundraising-efficiency scoring system;
- a payment product, wallet, personal agent or telemetry collector;
- a universal definition of mandate fit or charitable worth;
- a donor CRM, consulting product or prospect-scoring service;
- a general web, news or allegations archive;
- a demand, unmet-need or causal-impact model;
- a single universal taxonomy or ontology;
- a guarantee that every public fact has been found.

Downstream users may evaluate, match, recommend, transact or model demand under their own methodology, assumptions, branding and disclosures.

## 16. Product success

Success is measured through:

- national baseline coverage and identity quality;
- ability to answer organisation, comparison and ecosystem questions;
- scope, time and representation consistency;
- provenance and public source-reference resolution;
- summary, program/service, participation, fundraising, ethos/service-orientation and notable-context coverage where supporting evidence exists;
- proportion of processed subjects receiving the intended model-assisted pass and embeddings;
- semantic precision, unsupported-claim rate, recoverable recall and correction rate;
- explicit source-scope and public-evidence gaps;
- human review burden, accepted observations per dollar and accepted observations per subject;
- compliance with the three cohort budgets and transparent donor-exposure processing order;
- equitable baseline coverage across subject strata;
- successful use by analysts, consumer LLMs and downstream products;
- reliable immutable releases and Viewer fidelity.
