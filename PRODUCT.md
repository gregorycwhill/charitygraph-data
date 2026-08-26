# CharityGraph product contract

**Status:** Canonical shared product contract

**Version:** 2.0-draft

**Date:** 24 August 2026

**Applies to:** Builder, Data and Viewer

## 1. Public promise

> **CharityGraph is the one-stop shop for structured, governed Australian charity data.**

CharityGraph integrates public information about Australian charities, their legal and operating identities, programs, services, activities, populations, geography, participation, fundraising, finances, relationships, governance, workforce, capability, capacity, ethos, commitments, conduct, notability, outcomes and evidence.

It turns fragmented public material into structured, source-aware, versioned, contestable and reusable data for people, analysts, developers and AI systems.

“One-stop shop” means one governed discovery and interpretation layer. It does not mean:

- one source;
- one table;
- one stored mega-card;
- one taxonomy;
- equal depth for every charity;
- real-time completeness;
- a universal score; or
- a claim that every interpretation is beyond reasonable disagreement.

## 2. Product purpose

Australian charity information is distributed across regulators, tax records, annual reports, websites, public inquiries, service directories, government award systems, research, media and specialist sector sources. Even when public, it is expensive to locate, join, read, interpret and compare.

CharityGraph reduces that cost through:

```text
sources and observations
        ↓
source-native evidence
        ↓
structured candidates and mappings
        ↓
governed judgments and corrections
        ↓
immutable public projections
```

Its distinctive value is broad semantic coverage with inspectable provenance. It does not merely mirror sources and does not hide them behind synthesis.

## 3. Product strategy

### 3.1 Coverage before forensic perfection

The product will not succeed by achieving forensic confidence over a negligible fraction of the sector.

CharityGraph therefore:

- establishes inexpensive authoritative reach across the national charity population;
- uses cohort-specific LLM budgets to deepen useful coverage;
- invests additional defensibility according to consequence, ambiguity and claim risk;
- preserves a universal machine-captured provenance floor;
- tolerates transparently represented uncertainty and incompleteness in the long tail; and
- treats excessive abstention on well-evidenced low-risk classifications as failure.

### 3.2 Open-data curation

CharityGraph publishes useful governed judgments at meaningful scale, explains how they were produced and provides pathways to challenge them.

The community may contribute evidence, corrections, mappings and source updates. A governed review may amend, qualify, withdraw or uphold the existing record. A successful correction is product success, not necessarily evidence that publication should have been deferred.

Coverage and reach create the value that motivates community investment; community scrutiny then improves quality and methods.

### 3.3 Simple experience over a rich model

The internal model is intentionally sophisticated because developers, software agents and LLMs need precise semantics. Public users receive restrained, purpose-built organisation, program, service and evidence views.

Cards and pages are projections from governed knowledge, not Builder’s internal source of truth.

## 4. Anchor user and first-class users

### 4.1 Analyst or consultant

The analyst or consultant is the anchor design user. This includes philanthropic advisers, foundation staff, service-system planners, social-purpose consultants, researchers, journalists and charity advisers.

They need to:

- construct a defensible cohort;
- determine who does what, for whom and where;
- distinguish legal purpose from current operations;
- compare periods and scopes without false equivalence;
- map service supply, availability and delivery relationships;
- trace grants, contracts, donations and other resource flows;
- examine participation, fundraising, governance and organisational capability;
- separate regulator facts, first-party claims, direct observations and evaluations;
- identify changes, conflicts and gaps;
- export governed data to spreadsheets, SQL, Python, R and BI tools; and
- explain conclusions to another decision-maker.

### 4.2 Funders and service planners

Funders use CharityGraph for discovery, comparison and diligence. Service planners use it to ask not only where need exists but how that need is being met, by whom, with what capacity, dependencies and geographic reach.

CharityGraph supplies the charity-side supply and ecosystem map. Demand forecasting, causal funding optimisation and formal procurement decisions require appropriate external evidence and downstream analysis.

### 4.3 Downstream agents

A downstream personal or institutional agent may apply a principal’s explicit mandate, exclusions and tolerances.

CharityGraph supplies evidence-backed, mandate-adjudicable ingredients including legal status, cause, program scope, geography, population, ethos, conduct, notable context and uncertainty. It does not silently impose a universal mandate, execute a donation or provide personal financial advice.

### 4.4 Product builders

Builders use stable identities, schemas, releases, bulk distributions, provenance, coverage, taxonomies, relationships and corrections as a charity-intelligence layer.

### 4.5 Charities and contributors

Charities inspect their representation, follow evidence, supply attributed information and challenge errors or stale interpretations. They do not receive editorial control over supported independent observations.

Researchers, sector experts and public contributors may submit evidence and proposed corrections. Contributions are reviewed under public rules rather than accepted by vote or prominence.

### 4.6 Public users

Public users receive an accessible Viewer for organisation, program, service and evidence discovery. It is a reference interface, not a marketplace, league table or donation platform.

## 5. Question scales

CharityGraph supports:

- **Organisation:** understand one operating organisation and its legal identities.
- **Program or service:** understand a scoped body of work or offering.
- **Portfolio:** compare a governed cohort while preserving scope, period and comparability.
- **Ecosystem:** analyse programs, relationships, flows, geography, supply and coverage gaps.
- **Corpus:** study classifications, methods, sources and sector-wide patterns.

Question scale is independent of channel.

## 6. Delivery channels

- public Viewer and crawlable pages;
- JSON and Markdown subject representations;
- bulk JSONL, CSV and Parquet distributions where declared;
- spreadsheets, SQL, Python, R and BI workflows;
- general-purpose LLM retrieval and citation;
- downstream data products; and
- future API or MCP access when demand warrants operational complexity.

Static public artefacts remain the durable baseline.

## 7. Canonical product question

CharityGraph should progressively answer:

> Which Australian organisations, programs or services work on problem X, for population Y, in geography Z, through what activities or interventions; how are they structured, funded, governed and raising resources; what participation, capacity, ethos, notable context and evidence may matter; and what source, time, uncertainty and coverage qualify the answer?

## 8. Subject identity and scope

CharityGraph uses opaque internal `subject_id` values and authority-scoped external identifiers. It does not fabricate a universal public organisation identifier from its brand.

The subject stack supports:

- legal entity;
- operating organisation;
- organisational unit;
- program;
- service;
- project;
- campaign and appeal;
- participation opportunity;
- site, facility, creative and placement where independently material; and
- approved public-interest person or governing-position records.

Subjects are connected through governed relationships, not hard-coded nesting alone.

An assertion is attached to the lowest scope supported by evidence. Program facts do not automatically become organisation facts; partner conduct does not propagate through association; and legal purpose does not prove current operational activity.

## 9. Knowledge model

Builder separates:

- source profile and acquisition;
- evidence artefact and evidence span;
- source-native record;
- observation;
- candidate assertion or mapping;
- identity and relationship decision;
- governed acceptance, edit or rejection;
- conflict and correction;
- current-view selection;
- publication eligibility; and
- release projection.

The public dataset is a governed projection, not an archive or runtime dump.

## 10. Product domains

### 10.1 Identity and regulatory status

Names, external identifiers, legal and operating identity, registrations, DGR/tax status, lifecycle, groups, succession and source bindings.

### 10.2 Purpose, subjects, programs and geography

Legal purpose, stated mandate, cause/subject, operational activity, intervention, program, service, population roles, place and role-specific geography.

### 10.3 Participation

Volunteering, membership, governance, co-design, consultation, lived-experience contribution and other participation opportunities, relationships, episodes and aggregate measures.

CharityGraph is initially a structured-data and discovery product, not a volunteer marketplace.

### 10.4 Fundraising and resource mobilisation

Campaigns, appeals, creatives, placements, solicitation mechanisms, communication channels, physical settings, resources sought, donor relationship stages, instruments, delivery parties, compensation models and direct observations.

Residential door-knocking, public-place fundraising and shopping-centre/private-site activity remain distinct. Charity-shop drop-off, donation bins, organised pick-up and goods drives remain distinct.

### 10.5 Finance and resource flows

Source-faithful reports, statements, line items, notes, assurance, normalised concepts, grants, contracts, donations, restrictions, funds, allocations, calculations and reconciliations.

Reported or assured financial facts remain distinct from fundraiser, platform or vendor claims about ROI, uplift, lifetime value or social return.

### 10.6 Governance, workforce, capability and capacity

Governing instruments, bodies, positions, appointments, management and service governance; employees, contractors, volunteers and other contributors; skills, credentials, assets, service offers, access conditions, capacity, availability, waitlists and constraints.

### 10.7 Relationships and ecosystems

Control, affiliation, funding, commissioning, contracting, implementation, referral, membership, scheme, assurance, knowledge, coalition, shared-brand, auspice, predecessor and successor relationships.

Every substantive relationship is qualified by direction, roles, scope, time and evidence. Graph centrality is not organisational importance.

### 10.8 Ethos, conduct, commitments and notability

Values, positions, commitments, implementation evidence, scheme participation, complaints, allegations, investigations, findings, sanctions, responses, remediation and descriptive notability signals.

Notability is not merit. Allegations are not findings. Absence of public evidence is not neutrality or non-compliance.

### 10.9 Outcomes, impact and evaluation

Need, theory of change, activity, output, outcome, indicator, observation, evaluation study, finding, effect estimate, qualitative evidence, synthesis and economic/social-value claim.

Change, contribution and causation remain distinct.

### 10.10 Sources, evidence and publication

Source authority, acquisition, rights, evidence, transformations, model tasks, decisions, quality, corrections, releases, catalogues and public provenance.

## 11. Taxonomy strategy

CharityGraph uses a governed multi-facet system rather than one universal classification.

CharityGraph is taxonomy-plural by design. There is no single master CharityGraph taxonomy and no product dependency on one external scheme. Named, versioned schemes provide different lenses over the same governed subjects and assertions; incompatible external taxonomies are not silently merged into a proprietary hierarchy.

Approved direction includes:

- retain ACNC and ATO classifications as source- or authority-reported facts;
- use UN Sustainable Development Goals as a multi-label alignment lens;
- use ABS geography and relevant statistical classifications with explicit editions;
- develop CharityGraph-native operational-activity, participation and fundraising vocabularies where external schemes are inadequate;
- treat CLASSIE Subject and Population as optional external schemes, deferred pending rights/permission review;
- support future researcher, innovator, government, foundation and custom schemes under independent governance; and
- publish decisions for schemes adopted, profiled, incorporated, crosswalked, adapted, deferred, rejected or superseded.

Restricted third-party taxonomy payloads may remain content-hashed and versioned in private runtime storage. Generic open-source code may load conforming schemes and create governed assignments without committing protected labels or definitions. Dynamic loading does not establish legal permission. If an external scheme is disabled, independent CharityGraph evidence, subjects, relationships, native classifications and other scheme assignments remain valid; only dependent derived objects and publication projections are withheld or regenerated.

CLASSIE is not foundational to source acquisition, subject identity, program/service modelling, operational activities, SDGs, regulatory facts or the underlying graph.

Model-assessed assignments are useful governed judgments. Ordinary semantic disagreement is represented through confidence, ranking, alternatives and correction—not routine abstention.

## 12. Evidence, judgment and provenance

CharityGraph distinguishes:

- authority-reported fact;
- first-party claim;
- independent report;
- direct observation;
- transcription or extraction;
- calculated result;
- taxonomy mapping;
- model-assessed judgment;
- human-reviewed judgment; and
- disputed or corrected record.

Every published assertion retains a machine-captured provenance floor. Expensive forensic depth is risk-tiered.

For a well-evidenced low-risk semantic classification, the system should make the best-supported judgment. It should not return `unknown` solely because an adjacent classification is arguable.

## 13. Coverage and cohort economics

Initial scheduled LLM allocations are:

- AU$100 for the first 100 charities;
- AU$100 for the next 1,000;
- AU$100 for the next 10,000; and
- no routine per-charity LLM allocation for the remaining tail initially.

Cohort processing is risk-aware and revisable. Claim risk, user demand, correction, ambiguity, public scrutiny or material consequence may trigger deeper processing regardless of cohort.

Success is measured through reach, claim-family coverage, sampled correctness, false promotion, abstention, review burden, cost and right-tail performance—not provenance depth alone.

## 14. Open curation and corrections

Every public record should be challengeable through a stable assertion or field reference.

Contributors may propose:

- corrected values;
- alternate taxonomy assignments;
- new or newer sources;
- identity or relationship changes;
- qualifications or missing context; and
- privacy or rights concerns.

Review may accept, edit, partially accept, uphold, defer, reject or withdraw. Decisions preserve evidence and lineage. Published releases remain immutable; corrections appear prospectively.

## 15. Neutrality and editorial independence

Neutrality is procedural. CharityGraph:

- does not sell ranking or preferred classification;
- distinguishes evidence roles rather than flattening them;
- preserves contrary and procedural information;
- publishes methodology and scheme decisions;
- applies claim-family rules consistently;
- permits correction without granting subjects editorial control; and
- keeps private user mandates outside canonical evidence.

## 16. Product boundaries

CharityGraph does not initially provide:

- donation execution;
- personalised recommendations;
- volunteer matching;
- universal impact, trust, ethos, risk or efficiency scores;
- demand forecasting or funding optimisation;
- causal conclusions unsupported by evaluation evidence;
- person-level donor, participant or beneficiary data;
- unrestricted publication of all acquired source bodies;
- a real-time operational service directory guarantee; or
- hosted distributed orchestration, API or MCP as a prerequisite.

## 17. Release model

Public releases are immutable, versioned and catalogue-described. A future release may contain coordinated subject, program, assertion, relationship, finance, taxonomy, coverage and evidence distributions rather than one enormous nested record.

The Viewer provides simple entry points. Developers and agents may traverse the richer linked distributions.

Public contract 0.5 remains immutable compatibility authority until a separately approved future contract is implemented.

## Semantic architecture and provenance

CharityGraph is model-assisted by default for open-ended semantics. Python owns acquisition, stable parsing and segmentation, exact joins, source-native preservation, evidence bundles, validation, scheduling, caching, persistence, lineage, policy and release compilation. LLMs routinely own semantic relevance, entity/program/service interpretation, durability and boundary judgment, prose fact extraction, activity and population interpretation, taxonomy and SDG alignment, ambiguity and bounded rationale.

First-party websites, annual reports and grant materials are strategically authored evidence: they may establish source-native propositions, but their vocabulary is not taxonomy authority. Lexical occurrence or frequency is not semantic proof. Semantic provenance is reconstructible from source artefact through evidence bundle, task and prompt policy, provider/model, output, validation, governed disposition and release lineage. It does not require token-level causal explanations or expose internal model reasoning.
