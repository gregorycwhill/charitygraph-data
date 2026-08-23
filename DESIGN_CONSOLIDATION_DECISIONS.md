# CharityGraph Design Consolidation Decisions

**Status:** Approved decision record; propagated into canonical product documents on 2026-08-23  
**Date:** 2026-08-22  
**Responds to:** `DESIGN_CONSOLIDATION_QUESTIONS.md`  
**Inputs:** `ETHOS_AND_NOTABILITY_DESIGN.md`, `AGENTIC_PHILANTHROPY_DATA_STRATEGY.md`, `FUNDRAISING_KNOWLEDGE_DESIGN.md`, `ENRICHMENT_ECONOMICS_DESIGN.md`, current CharityGraph Data product/schema contracts, and the 2026-08-22 consolidation discussion.


**Propagation:** Canonical requirements now live in PRODUCT.md, PRINCIPLES.md, PUBLIC_COMMITMENTS.md, EXPERIENCES.md, ROADMAP.md, IMPLEMENTATION_PLAN.md, TEST_PLAN.md and PUBLIC_CONTRACT_0_5.md. This record retains decision rationale and traceability; it does not supersede those authorities.

## 1. Purpose and authority

This document resolves the cross-product questions raised by Codex after reviewing the four working design documents against the current CharityGraph contract.

It is intended to do two things:

1. remove product/schema ambiguity before the next Builder implementation phase; and
2. move normative product design, schema semantics and evaluation design out of Codex execution prompts and into an explicit CharityGraph Data decision record.

This document does **not** mutate the immutable `v0.5.0-2026-08-15` release and does not by itself authorise publication of new semantic observations. The next implementation phase remains review-only until its human/economic gates are passed.

Where this document conflicts with an older working design, this document governs the next phase. The durable decisions should subsequently be propagated into canonical documents such as `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_SCHEMA_VNEXT_SPEC.md`, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md` as appropriate.

## 2. Product boundary: CharityGraph makes mandates adjudicable; it does not adjudicate them

CharityGraph remains public charity-information infrastructure, not a recommender, payment product or personal-agent policy engine.

The agentic-philanthropy thesis is retained with one terminology clarification:

> **CharityGraph makes a charity or program mandate-adjudicable by supplying the relevant evidence-backed ingredients. A downstream personal agent applies the principal's own mandate, precedents, tolerances and matching rules.**

CharityGraph may expose facts and classifications needed to answer mandate questions, including:

- registration and DGR status;
- cause/problem classifications;
- beneficiaries;
- intervention/approach;
- program or service scope;
- geography;
- organisational ethos;
- service/mission orientation;
- notable public context;
- funding/fundraising observations;
- evidence freshness, coverage and uncertainty.

CharityGraph must not publish a user-independent:

- mandate match percentage;
- `within_scope / outside_scope / borderline` conclusion for a private mandate;
- eligibility recommendation;
- ranked recipient list;
- donation allocation.

A later downstream rule-evaluation product may use CharityGraph ingredients, but that logic is not part of the CharityGraph public data contract.

## 3. Cause centrality: separate centrality from taxonomy adjacency

The earlier `primary / material-adjacent / incidental` language mixes two concepts:

1. how central a classified cause/intervention is to the scoped subject; and
2. how semantically adjacent one taxonomy term is to another.

These must remain separate.

For scoped classifications or observations that need centrality, use the provisional evidence-backed field:

```text
centrality:
  primary
  material
  incidental
  unknown
```

`primary` means the evidence supports the cause/intervention as central to the organisation/program/service. `material` means it is a meaningful, non-incidental part of the scoped activity. `incidental` means the connection exists but is not a material purpose/activity. `unknown` preserves uncertainty.

Taxonomy adjacency or conceptual relationships between causes remain properties of taxonomy/reference mappings. A donor's willingness to treat an adjacent cause as in-scope is a downstream mandate rule.

No centrality score or numerical percentage is required in CharityGraph v1.

## 4. Harm → remedy → intervention graph

Do **not** build a public harm/remedy causal graph in the next development phase.

The concept remains strategically useful for future agentic philanthropy, service planning and intervention retrieval, but it raises separate questions of causal assertion, contested mappings, ontology governance and versioning.

For the next phase:

- strengthen scoped cause/intervention observations and classifications;
- collect empirical pressure on intervention vocabulary;
- treat harm/remedy mappings as future reference-ontology research rather than a blocker for semantic enrichment.

## 5. Program, service and organisational-unit scope

Program-level evidence is in scope now because it materially improves charity understanding and future mandate resolution.

However, **program scope does not require durable subject identity**.

Extend the common observation pattern with an explicit scope object conceptually equivalent to:

```json
{
  "scope": {
    "scope_type": "organisation | program | service | organisational_unit",
    "scope_id": "optional local or durable identifier"
  }
}
```

Rules:

- `organisation` scope refers to the CharityGraph subject itself;
- `program`, `service` and `organisational_unit` may initially use governed subject-local identifiers;
- a nested program/service does not become a CharityGraph subject merely because observations exist about it;
- later promotion to a durable subject requires explicit identity governance and a relationship such as `program_of`;
- name similarity never promotes or binds a nested program to a durable subject;
- fundraising campaigns are not programs by default and use their own campaign observations.

The existing v0.5 typed-domain model remains. This is **not** approval for a generic EAV store or universal claim graph.

## 6. Common semantic observation extension

The current v0.5 observation envelope remains the foundation:

- `observation_id`;
- `subject_id`;
- domain `kind`/typed payload;
- `claim_basis`;
- `extraction_method`;
- `source_record_ids`;
- `evidence_ids`;
- time;
- optional confidence;
- warnings;
- derivation where non-direct.

The next semantic pilot should extend/reuse it with:

- explicit scoped subject/program/service/unit context;
- qualification where needed to preserve material nuance;
- domain-specific observation roles, rather than a generic key/value field;
- source role on evidence/source records;
- explicit assessment scope on coverage.

Typed public domains remain preferable to a generic claim graph. Candidate/review records may contain additional private fields such as raw source phrase, proposed canonical term, alternatives, review disposition and model lineage.

## 7. Ethos is organisational identity/context; service orientation is separate

`Ethos` remains a first-class design construct describing worldview, tradition, institutional orientation or affiliation.

`service_or_mission_orientation` becomes a **separate observation domain/capability** from organisational ethos.

This separation is required because these answer different questions:

- Ethos: *what institutional worldview/tradition characterises the organisation or scoped unit?*
- Service orientation: *whether and how that worldview enters service delivery, formation, worship, evangelism/proselytising or advocacy.*

Beneficiary/community identity remains separate from both.

Core rule:

> **Ethos describes the organisation or one of its scoped programs/units, never the presumed beliefs or ideology of beneficiaries.**

## 8. Ethos evidence and publication policy

Evidence roles remain:

- `self_described`;
- `formal_affiliation`;
- `externally_described`;
- `historical`.

`service_or_mission` moves out of Ethos into the separate service-orientation domain.

Publication posture:

- direct current self-description may be published as self-description when source and scope are clear;
- formal affiliation may be published when constitution/governance/parent-body evidence supports it;
- robust independent secondary characterisation may be published with explicit attribution;
- historical orientation may coexist with current identity rather than replace it;
- disagreement between self-description, formal status and independent description must be preserved where material;
- no descriptor may be inferred from names, photographs, office location, beneficiary demographics, employee/supporter politics, or unsupported LLM impression.

During the first pilot, **all Ethos and service-orientation candidates require human review**.

Later automation may be considered for high-precision direct self-description/formal-affiliation cases. Conflicting, disputed, current political/ideological and other high-risk external characterisations retain mandatory human review unless a later benchmark and policy explicitly changes that rule.

## 9. No parent/network attribute transfer

A parent, denomination, federation, international network or movement is a **related subject**, not a scope on which the child's Ethos observation is stored.

Therefore:

- remove `related_parent_or_network` as an Ethos observation scope for the child;
- preserve the relationship separately;
- the parent/network owns its own Ethos and notable-context observations;
- the Australian affiliate receives an Ethos observation only if evidence about the affiliate itself supports it.

A card may explain that an Australian entity is related to a parent with a particular ethos, but must not silently transfer the parent's attributes onto the affiliate.

The same no-transfer principle applies to adverse/notable context, campaign history and other attributes.

## 10. Public name for Notability

Retain **Notability** as the internal product/design concept if useful.

Use **`notable_context`** as the preferred public construct/field name.

`notable_context` is a collection of sourced contextual observations, not a scalar measure of prestige, reputation or importance.

Prohibited:

- `notability_score`;
- reputation score;
- positive/negative balance;
- prestige rank;
- implication that a charity with no observations is unimportant or reputable.

## 11. Notable-context categories

Continue to evaluate categories such as:

- institutional history;
- founder/founding;
- recognition or award;
- significant event or campaign;
- inquiry/review;
- regulatory/legal matter;
- criticism/controversy;
- merger/split/succession;
- movement/network context;
- notable person relationship;
- other.

These are retrieval/display categories, not significance levels.

Procedural status and time must be precise. `Investigated`, `reviewed`, `charged`, `found in breach`, `settled`, `cleared` and `criticised` are distinct claims.

## 12. Wikimedia policy: two-tier evidence rule

Wikipedia/Wikidata are authorised for a narrower role than broad charity ingestion.

### 12.1 Common rules

- Wikipedia/Wikidata never authoritatively resolve CharityGraph identity by name alone;
- candidate linkage must be corroborated independently;
- article/revision provenance must be retained;
- section/location and inline citation path should be retained where available;
- record whether Wikipedia was used as `discovery` or `support`;
- absence from Wikipedia has no negative meaning;
- no circular provenance/citation laundering.

### 12.2 Lower-risk contextual observations

A revision-pinned Wikipedia statement may remain direct secondary support, subject to review, for relatively stable low-risk context such as:

- founding/history;
- merger/succession;
- movement/network relationship;
- stable institutional milestone;
- independent recognition/award.

Following the underlying citation is preferred and may materially improve provenance.

### 12.3 Sensitive/adverse observations

Before public publication, CharityGraph must follow to an adequate underlying source for:

- inquiry/review findings;
- regulatory/legal matters;
- criticism/controversy;
- allegations;
- contentious living-person claims;
- sensitive external religious/political/ideological characterisation.

Wikipedia remains discovery/editorial-admission lineage for these classes, not the final evidentiary endpoint.

## 13. Corrections and disputed context

Use the existing CharityGraph correction architecture rather than inventing a separate public right-of-reply field.

Rules:

- correction intake remains private by default;
- moderation can produce governed public correction/decision records where appropriate;
- an organisation does not gain editorial veto over supported CharityGraph observations;
- a material challenge to adverse/sensitive context triggers expedited re-review;
- unsupported or materially misleading observations should be corrected/retracted;
- supported observations may remain with improved qualification or updated procedural status;
- historical correction/retraction lineage should be preserved where the public record requires it.

## 14. Fundraising expenditure: no peer imputation

Remove **peer imputation** from the CharityGraph fundraising-expenditure ladder.

For fundraising expenditure, the governed ladder is:

1. direct disclosure;
2. deterministic/mechanical reconstruction from defensible source components/shares;
3. defensible attribution bounds or specifically governed interpretation from selected evidence;
4. unavailable/null when no defensible result exists.

There is:

- no universal fallback percentage;
- no broad prior;
- no peer fill merely to avoid a blank;
- no forced point estimate;
- no midpoint of attribution bounds.

`peer_imputation` may remain a generic derivation vocabulary item for some future separately approved domain, but it is not permitted for CharityGraph fundraising expenditure.

Canonical `PRODUCT.md` and Builder guidance/code should be reconciled accordingly.

## 15. Fundraising knowledge model is approved in four distinct domains

Approve the distinction:

> **funding source ≠ standing fundraising practice ≠ fundraising campaign ≠ fundraising expenditure**

Definitions:

- **funding source**: where money is reported to come from;
- **fundraising practice**: standing/recurrent way the organisation seeks funds;
- **fundraising campaign**: identifiable, normally time/edition-bounded fundraising initiative or event;
- **fundraising expenditure**: public evidence about fundraising-related costs.

These objects may be analysed together downstream but CharityGraph must not infer causal economics between them.

A campaign result such as “raised $2m” remains a source-reported campaign metric and does not silently reconcile into annual donation income.

## 16. Fundraising campaign identity

A fundraising campaign is a **nested observation/object first**, not a durable CharityGraph subject by default.

It may carry:

- local campaign ID;
- name;
- type;
- status;
- time/edition;
- mechanics;
- channels;
- reported target;
- reported dollars spent/raised where explicit;
- reported counts;
- evidence/action URLs.

Recurring campaigns may retain edition-specific observations and a source-local recurrence relationship.

Promotion to a durable CharityGraph subject is deferred until there is a demonstrated cross-source identity/use case and explicit promotion criteria.

## 17. Fundraising provider relationships: include in the private pilot

The earlier tentative deferral is reversed following review of fundraising-industry public sources.

There is sufficiently explicit, fresh and informationally dense public evidence of charity ↔ fundraising-provider relationships to justify a **review-only `fundraising_provider_relationship` candidate** in the first pilot.

Examples of potentially strong evidence include:

- self-regulatory association records naming charity/agency relationships;
- charity-nominated industry awards for consultants/service partners;
- agency case studies naming clients and delivered channels/campaigns;
- fundraising-platform case studies;
- listed-company statutory disclosures naming charity programs/partners.

Provider entities do not need CharityGraph charity IDs. They may initially be external named organisations linked through governed relationship candidates.

Public promotion remains a post-pilot decision.

## 18. Assessment scope becomes compact public coverage metadata

Approve an optional general coverage `assessment_scope` direction.

Conceptually:

```json
{
  "assessment_scope": {
    "source_families": ["organisation_website", "annual_report"],
    "source_roles": ["giving", "bequests_major_giving"],
    "reporting_periods": ["2025"],
    "policy_version": "semantic-enrichment-v1"
  }
}
```

Public cards should eventually expose compact assessment scope sufficient to interpret a `not_found_in_source` result.

Detailed acquisition telemetry, retries, raw URLs, model spend and reviewer notes remain private operational material unless independently useful as public provenance.

`not_found_in_source` never means `does_not_exist`.

## 19. Shared evaluation program: one cohort, not separate pilots

Do not run separate 30–50-case Ethos, fundraising and agentic cohorts.

The next development phase is one **Semantic Enrichment Benchmark v1**.

### 19.1 Core cohort

Use approximately **40 deliberately selected charity subjects** spanning:

- source-rich and source-poor organisations;
- large, medium, small and very small charities;
- complex and simple organisational/program structures;
- multiple religious/ideological contexts;
- fundraising-rich and fundraising-light organisations;
- Wikimedia-rich and Wikimedia-absent cases;
- activity/beneficiary/program/geography edge cases;
- controls where enrichment is genuinely sparse.

Reuse existing Golden Corpus and Knowledge Validation subjects where useful, but the unit here is a charity subject and multiple review cases may exist per subject.

### 19.2 Domains

The shared pilot should generate/review candidates across:

- programs/services;
- activities/beneficiaries as easier controls;
- cause/intervention centrality;
- role-specific geography where available;
- participation;
- fundraising practices;
- fundraising campaigns;
- fundraising-provider relationships;
- Ethos;
- service/mission orientation;
- notable context.

## 20. Economically informed extraction ladder

The production/evaluation architecture should distinguish evidence opportunity from model capability.

Conceptual ladder:

- **P0** — existing structured/regulator baseline;
- **P1** — deterministic/local extraction and source-led indexing;
- **P2** — low-cost LLM interpretation of selected evidence slices;
- **P3** — selective higher-spec model escalation where expected marginal information value warrants it;
- **O** — same-source high-spec oracle used only for benchmark estimation;
- **H1** — human adjudication/reference for selected disagreements;
- **H2** — broader public-source manual audit to measure source-scope gaps.

The purpose is to estimate separately:

- public information genuinely absent;
- information outside acquired source scope;
- acquired information recoverable only with more expensive interpretation;
- governance/publication blocks;
- ordinary not-yet-processed gaps.

## 21. Same-source high-spec oracle priorities

Do not spend oracle calls on easy regulator facts.

Highest initial oracle value is expected for:

- program/scope resolution;
- fundraising practice/campaign interpretation;
- Ethos/service orientation;
- selected notable-context cases.

Use smaller calibration samples for participation, activities and beneficiaries.

The oracle must receive the **same acquired evidence** as the production pipeline so model capability is not confounded with source breadth.

## 22. Production routing thresholds remain empirical

Do not freeze false-precision numeric thresholds before the benchmark.

Every domain must report separately:

- accepted-observation precision;
- critical provenance/identity/scope defect rate;
- reviewer edit/reject burden;
- marginal observations gained by escalation;
- marginal subjects newly enriched by escalation;
- cost per accepted observation;
- cost per newly enriched subject;
- source opportunity/coverage;
- refresh/maintenance cost.

The benchmark should recommend domain-specific routing/stopping rules. Automatic public promotion requires a later explicit product decision and sufficient adjudicated evidence; candidate-generation thresholds can be more permissive because candidates remain review-only.

## 23. Broader-source H2 audit and source-family promotion

H2 remains authorised as a **manual benchmark experiment** for broad public sources such as social media, event platforms, news/trade media and other public web evidence.

H2 does not automatically authorise production crawling.

If H2 or separate source research identifies a repeatable, high-value source family with acceptable rights/freshness/identity economics, that source family may receive a dedicated source-policy decision.

`fundraising_industry` is the first such separately approved **experimental** source category; see `FUNDRAISING_INDUSTRY_SOURCE_DESIGN.md`.

## 24. Source-led acquisition principle

Where a high-value public source enumerates many charities/campaigns, prefer:

> **source-led enumeration → conservative CharityGraph subject binding → targeted detail acquisition → bounded semantic extraction**

over:

> charity-by-charity open-web search.

This is an economics principle, not an authority principle. Candidate source identity never overrides CharityGraph subject-resolution rules.

## 25. Immediate sequencing for development

The next phase should proceed in this order:

1. **Fundraising safety reconciliation**  
   Remove/quarantine obsolete universal fallback-prior code paths and reconcile stale Builder instructions with current Data policy. Add regression tests.

2. **Close existing Knowledge Validation human gate**  
   Use its adjudication as baseline evidence for semantic candidate quality and boundary handling.

3. **Commit the consolidated design/source policy**  
   Add the four working source design documents if still absent from CharityGraph Data; add this decision record and `FUNDRAISING_INDUSTRY_SOURCE_DESIGN.md`; make only explicitly required canonical-document updates.

4. **Implement Semantic Enrichment Benchmark v1**  
   Shared scoped observation/private-candidate structures, common source-opportunity inventory, ~40-subject review-only cohort and economic instrumentation.

5. **Implement first fundraising-industry adapters**  
   Start with highly structured/semi-structured sources that test campaign, practice and provider semantics cheaply.

6. **Human/economic review**  
   Decide vocabulary/schema promotion and domain routing from empirical results.

7. **Expand economics benchmark toward 120 subjects where warranted**  
   Do not require full human adjudication of all 120 subjects.

8. **Only then change public contract/Viewer or scale semantic publication.**

## 26. What is explicitly deferred

The next phase does not implement:

- a mandate score or mandate evaluator;
- harm/remedy causal graph;
- charity recommendation/ranking;
- fundraising ROI, CPA, ROAS or LTV metrics;
- universal provider/vendor master data;
- broad social-media crawling;
- automatic publication of Ethos/notable context;
- parent/network attribute transfer;
- durable identity for every campaign/program;
- national semantic rebuild;
- major Viewer redesign.

## 27. Decisions mapped to Codex's 21 questions

| Codex question | Decision |
| --- | --- |
| 1 | Mandate-fit ingredients only; downstream agent adjudicates. |
| 2 | Use scoped `centrality = primary/material/incidental/unknown`; taxonomy adjacency is separate. |
| 3 | Harm→remedy graph deferred from next phase. |
| 4 | Program/service/unit scope supported now without requiring durable subject identity. |
| 5 | Service/mission orientation is a separate domain/capability from Ethos. |
| 6 | Direct self/formal evidence may publish as such; robust secondary characterisation must be attributed; sensitive disputed cases require review. |
| 7 | All pilot Ethos candidates human-reviewed; later automate only demonstrated low-risk high-precision classes. |
| 8 | No parent/network attribute transfer. Parent owns its attributes; relationship is separate. |
| 9 | Public name `notable_context`; internal Notability concept may remain. |
| 10 | Wikipedia may support lower-risk context; sensitive/adverse classes require underlying adequate source. |
| 11 | Wikipedia editorial survival is candidate admission, not a significance score; claim-specific evidence rules apply. |
| 12 | Existing moderated correction pathway; no automatic public right-of-reply field. |
| 13 | No peer imputation for fundraising expenditure; unavailable/null is valid. |
| 14 | Approve funding source ≠ practice ≠ campaign ≠ expenditure. |
| 15 | Campaign nested observation first; durable subject only under future explicit promotion criteria. |
| 16 | Include provider relationship as **private pilot candidate** following new source research; public status undecided. |
| 17 | Compact assessment scope should become public coverage metadata; detailed operations remain private. |
| 18 | One ~40-subject cross-domain pilot, then expand economics toward 120 where warranted. |
| 19 | Oracle priority: programs/scope, fundraising, Ethos/service orientation, selected notable context. |
| 20 | Measure domain-specific economics/quality now; production thresholds are empirical and approved after benchmark. |
| 21 | H2 broad sources manual benchmark-only unless a source family receives separate approval; fundraising industry now has that experimental approval. |

## 28. Design principle for the next phase

> **CharityGraph should spend computation where public evidence opportunity exists, preserve epistemic sparsity where it does not, and represent semantic knowledge as scoped, typed, evidence-bound observations rather than scores or recommendations.**
