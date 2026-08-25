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
| CG-D025 | CharityGraph is taxonomy-plural: external and custom schemes are independently versioned, rights-governed, removable lenses over governed knowledge. CLASSIE Subject/Population are optional and deferred pending rights approval; restricted payloads may be private/runtime-loaded; disabling an external scheme does not invalidate independent knowledge. Builder enriches governed charity/program knowledge and is not a general-purpose arbitrary-text or grant-application taxonomy-classification service. | Approved | Generic taxonomy loading and governed assignments remain supported; CLASSIE is not foundational; future researcher/innovator schemes can be evaluated without selecting a replacement now. |

## Open implementation decisions

The following require bounded design before their implementation slice, not speculative resolution now:

- exact cohort-ranking features and refresh cadence;
- canonical storage root layout and retention periods;
- public vNext assertion/provenance projection schemas;
- correction submission channel and identity/privacy controls;
- model/provider routing thresholds;
- precise first versions of participation, fundraising, operational-activity and ethos vocabularies;
- Indigenous data-governance review mechanism;
- future public API/query format beyond downloadable Data and static Viewer.

Each decision should receive an ADR or amendment before code depends on it.
