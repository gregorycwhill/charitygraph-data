# CharityGraph Public vNext Decision Log

**Status:** Canonical decision record, version 1.0-draft

**Scope:** Decisions that materially shape Builder vNext and future public Data releases

| ID | Decision | Status | Consequence |
|---|---|---|---|
| CG-D001 | The product promise is a one-stop shop for structured, governed Australian charity data. | Approved | Coverage and cross-domain utility are first-order requirements. |
| CG-D002 | Preserve immutable public contract 0.5 byte-for-byte. | Approved | vNext uses new schemas and releases; compatibility is not retrofitted into 0.5. |
| CG-D003 | Use an assertion-centred knowledge model with explicit subject scope, evidence and lineage. | Approved | Source records, model outputs and published assertions remain distinguishable. |
| CG-D004 | Use SQLite as the local operational catalogue and ledger. | Implemented foundation | It coordinates runs, tasks, attempts, budgets, cache and artefacts; bulk evidence stays in files. |
| CG-D005 | Store bulk artefacts in content-addressed files and use SQLite as their index/control plane. | Approved | Avoid database bloat and per-run evidence duplication. |
| CG-D006 | Prefer coverage under cohort budgets while retaining a universal mechanical provenance floor. | Approved | Forensic depth varies by consequence and cohort. |
| CG-D007 | Approved initial LLM envelopes are AU$100 for the top 100, next 1,000 and next 10,000 respectively. | Approved | Scheduler and reports use portfolio-level controls, reservations and actual costs. |
| CG-D008 | Models should exercise ordinary semantic judgment; `unknown` is not a refuge from reasonable ambiguity. | Approved | Low-risk classifications use evidence, rationale, confidence and primary/secondary labels. |
| CG-D009 | High-risk claim types can override cohort economics. | Approved | Specialist or human review remains available for consequence-heavy assertions. |
| CG-D010 | Community correction is a product capability and success signal. | Approved | Challenges are governed proposals with visible disposition and append-only history. |
| CG-D011 | ACNC/ATO classifications, National Standard Chart of Accounts, UN SDGs, ABS standards and optional external schemes form an independently governed initial portfolio; no listed scheme is mandatory or rights-cleared by inclusion alone. | Approved | External scheme identities and versions are preserved; rights and publication state remain separate. |
| CG-D012 | Participation, fundraising, operational activity, ethos and notability require CharityGraph-native profiles informed by documented external-scheme research. | Approved | Research dispositions are public; native schemes do not obscure their influences. |
| CG-D013 | Industry shadow registries are first-class sources, not experiments. | Approved | Their own membership, fee, code or accreditation propositions may be authoritative. |
| CG-D014 | Participation is populated from the initial build rather than deferred to a future product. | Approved | The model and acquisition plan include participation evidence early. |
| CG-D015 | Fundraising uses faceted method/channel/setting/instrument/audience/campaign modelling. | Approved | Granular direct observations can be added without redesigning a compound hierarchy. |
| CG-D016 | Future direct-observation and advertising sousveillance are accommodated but collection tooling is deferred. | Approved | Evidence model supports time/place/medium/capture and observer protocol. |
| CG-D017 | Notability allocates processing effort and is never charity worth, impact or quality. | Approved | Cohort explanations and feature versions are required. |
| CG-D018 | No universal CharityGraph organisation identifier is invented; preserve legacy compatibility identifiers only where contractually necessary. | Approved | Identity uses scoped subject records and external identifiers. |
| CG-D019 | Current public UX remains simple; rich internals primarily support builders, agents and sophisticated analysts. | Approved | Public projections do not expose every internal abstraction. |
| CG-D020 | Do not teach Python to approximate English via expanding phrase rules. | Approved | Mechanical code validates and orchestrates; model tasks handle open-ended semantics. |
| CG-D021 | Build through bounded vertical reality slices with fixed evaluation sets and holdouts. | Approved | One implementation and one correction pass are normal; repeated conceptual failures trigger redesign. |
| CG-D022 | First slice is identity, programs and classifications for about ten varied charities, ending in a private preview. | Approved | No Viewer or public release change is required for the slice. |
| CG-D023 | Builder/Viewer remain MIT; Data remains CC BY 4.0, subject to distinct brand and endorsement rules. | Implemented | Future releases include identity, attribution and reuse metadata. |
| CG-D024 | The former project name appears only where immutable compatibility or historical explanation requires it. | Approved | Active product language and new identifiers use CharityGraph. |
| CG-D025 | The product uses a taxonomy-plural approach. CLASSIE is optional and deferred pending rights and permission review; restricted payloads may remain private; external schemes remain removable; Builder is not a general arbitrary-text taxonomy classifier. | Superseded | Superseded by CG-D028 and CG-D029, which define the distinct classification lenses and the approved private-processing/public-suppression boundary. |

| CG-D026 | CharityGraph is LLM-first for open-ended semantics. The Semantic Heuristic Gate is ex-ante: ask "Does this diff teach Python English?" and require Greg-approved, registered exception ID before deterministic semantic lexical interpretation. | Approved | Recurring semantic errors change evidence, prompt, schema, model, routing, benchmark or governance rather than accumulating English phrase rules. |
| CG-D027 | Semantic provenance is reconstructible through source artefact, evidence bundle, task/prompt policy, provider/model, structured output, validation, governed disposition and release lineage. First-party language is strategically authored evidence, not taxonomy authority; no token-level causal explanation is claimed. | Approved | Evidence-bundle/document-level inference is legitimate without exposing provider chain-of-thought or treating lexical occurrence as semantic proof. |
| CG-D030 | CharityGraph Playbooks is a fourth first-class product, not a Data or Viewer feature: official Playbooks are governed, parameterised, versioned, corrigible, provider-neutral and openly reusable analytical methods designed for bring-your-own-AI execution. | Approved | Viewer may surface and parameterise Playbooks, but a Playbook definition, invocation and downstream model output remain distinct; only the definition is governed CharityGraph content. |

## Open implementation decisions

The following require bounded design before their implementation slice, not speculative resolution now:

- exact cohort-ranking features and refresh cadence;
- canonical storage root layout and retention periods;
- public vNext assertion/provenance projection schemas;
- correction submission channel and identity/privacy controls;
- model/provider routing thresholds;
- precise first versions of participation, fundraising, operational-activity and ethos vocabularies;
- Indigenous data-governance review mechanism;
- future public API/query format beyond downloadable Data and static Viewer;
- exact Playbook schema and invocation packaging;
- official/community Playbook promotion and contribution workflow;
- Playbook evaluation thresholds and review evidence;
- Viewer handoff mechanics for context and private parameters; and
- production Playbooks release lifecycle and catalogue structure.

Each decision should receive an ADR or amendment before code depends on it.

### CG-D028 — Classification lenses, grain and provenance

**Status:** Approved

CharityGraph uses six non-equivalent classification and regulatory lenses:

1. ACNC Registration
2. ATO DGR
3. ACNC CLASSIE
4. UN SDG
5. CharityGraph Native
6. CharityGraph CLASSIE

Their grains and authorities differ. ACNC CLASSIE and Our Community CLASSIE are not presumed version-identical. Cross-lens use requires an explicit `ConceptMapping`; assignments remain governed in the source lens and are not silently rolled up. Reporting group is structural scope, not a seventh lens. Embeddings are retrieval and representation aids only; they do not create assignments.

This decision supersedes the classification wording previously recorded under CG-D025 without rewriting that historical decision.

### CG-D029 — Private CLASSIE processing / public suppression

**Status:** Approved

Private CLASSIE runtime loading and LLM processing are approved when the payload is lawfully supplied. Local derived storage is approved. Public CLASSIE publication remains permission-gated, and inferred CLASSIE assignments are withheld by default. CLASSIE can be removed without re-extracting CharityGraph Native knowledge or other independent lenses.

This decision supersedes the deferred/rights-pending operational wording previously associated with CG-D025.

### CG-D030 — Playbooks as a fourth CharityGraph product

**Status:** Approved

CharityGraph is a product family comprising Builder, Data, Viewer and Playbooks. Playbooks publishes governed, parameterised, versioned, corrigible and openly reusable analytical methods for use with a user's chosen general-purpose AI. Playbooks are provider-neutral and do not initially host inference. Viewer may discover context-appropriate Playbooks, pre-populate CharityGraph references and generate a portable invocation, but it does not own or govern Playbooks.

A Playbook definition, a parameterised invocation and the external-model output are separate. Only the Playbook definition is governed CharityGraph content; an invocation and downstream output are not canonical CharityGraph knowledge merely because an official Playbook was used. Contribution is extensible and evidence-governed, with Official and Community status distinct. User strategic parameters should be minimised or kept client-side where practical. Data/content, Playbook-method and execution/model/retrieval problems use distinct feedback pathways. A dedicated Playbooks repository and Viewer integration are deferred.

**Implementation note (30 August 2026):** The initial `charitygraph-playbooks` repository and contract were established at commit `6466e04`. The remaining deferral is production catalogue/release work and Viewer integration; this note records implementation state without changing the approved decision.

### CG-D031 — Central sourcing versus section discovery

**Status:** Approved

**BUILDER DOESN'T DO DISCOVERY.** Central sourcing governance defines the
production evidence universe. Builder acquires and processes approved sources
and persisted representations; sections and lenses interpret that evidence
and may expose coverage gaps but do not discover or add sources. Evaluation and
ground-truth work may inspect broader regulator, court, journalism, research or
specialist material, but that material does not enter production automatically.
Repeated gaps may motivate a separate governed proposal for a new source family;
admission is an explicit sourcing decision applying across relevant sections.

### CG-D032 — Semantic Lab versus Factory boundary

**Status:** Approved

Cheap bounded Semantic Lab experiments optimise information gain and may
document uncertainty or tolerate imperfect replay when interpretable. Factory
and scaling work retain stricter restart, identity, duplicate-prevention,
accounting and cost controls; these are not premature Lab blockers. PR #48
remains parked.

### CG-D033 — Domain-specific lens boundaries

**Status:** Approved

Lens contracts are domain-specific precision/recall control surfaces. Each
defines a positive semantic object, anti-uplift boundaries, expected legitimate
cross-domain reuse and zero-candidate meaning. Neither the permissive nor the
corrected Section 15 V1E prompt set is canonical production policy; fan-out is
diagnostic, not a validity or publication rule.

### CG-D034 — Frozen source universe and evidentiary role

**Status:** Approved

The governing sequence is SOURCE UNIVERSE FIRST → ACQUIRE ONCE → FREEZE CORPUS
→ SEMANTICS. Builder does not discover or research new sources from semantic
results. Propositions require an approved source represented according to its
evidentiary role; independent corroboration is claim-family-specific, not a
universal publication prerequisite.
