# CharityGraph and Agentic Philanthropy — product and data strategy

**Date:** 17 August 2026  
**Purpose:** Summarise the most plausible agentic-philanthropy use cases and identify the CharityGraph data needed to support them, including Ethos, Notability, annual-report extraction and Wikipedia-derived context.

## Executive conclusion

The most defensible role for CharityGraph is not to become the donor's personal agent, telemetry collector, social network, payment gateway or universal charity evaluator.

CharityGraph should become the **charity-side semantic and evidence layer used by personal agents**:

> A personal agent knows the principal, interprets the situation and applies the mandate. CharityGraph knows the organisations, programs, interventions, eligibility, ethos, context and evidence.

This directly serves CharityGraph's original mission. Personal agents can guard a principal's money while discovering smaller, unfamiliar charities. That reduces reliance on brand familiarity as a proxy for trust and gives credible right-tail organisations access to donors who would not research them manually.

The highest-value CharityGraph capability is therefore **mandate adjudication**, not payment verification:

> Given this ordinary-language mandate and this proposed recipient/program, is the gift clearly within scope, outside scope or legitimately borderline—and what evidence supports that conclusion?

## 1. Most plausible use cases

### Tier 1: strongly aligned with CharityGraph

#### 1. Guarded discovery

The principal authorises a small autonomous giving budget. Their agent explores unfamiliar charities while enforcing constraints such as:

- current registration and DGR status where required;
- cause, beneficiary, geography and intervention fit;
- religious, ideological and service-delivery preferences;
- exclusions derived from the principal's ethos;
- notable regulatory, legal, governance or reputational context;
- evidence freshness and minimum confidence;
- smaller initial gifts where evidence is thin but no problem is observed.

This is the clearest CharityGraph mission fit: shift charitable discovery from brand recognition to evidence-backed mandate fit.

#### 2. Causal matching with mandate verification

A verified donation by one person triggers a genuinely additional donation under another person's pre-funded rule. CharityGraph's distinctive job is not to prove that the first card payment settled. It is to assess whether the recipient or designated program fits the matcher's natural-language mandate.

Example: “Match environmental causes.”

- core environmental organisation: 100% match;
- Animals Australia unrestricted gift: potentially 50%, depending on the principal's accepted adjacencies;
- RSPCA unrestricted gift: 0% under a conventional environmental mandate;
- a specifically designated habitat-restoration program: separately assessed.

The matching rate is the principal's rule, not an objective percentage assigned by CharityGraph. CharityGraph supplies facts about primary purpose, material activities and program designation; the personal agent applies the principal's precedents.

#### 3. Programmatic giving challenges

Phones, wearables, transaction data and personal agents unbundle charity challenges from the large charity that traditionally owns the campaign. Individuals, families, friends and workplaces can define rules such as:

- match alcohol expenditure during July;
- allocate money per kilometre walked;
- direct savings from avoided purchases;
- match a family member's verified donation;
- trigger a contribution when a group completes a challenge.

CharityGraph resolves the resulting charitable intent into eligible organisations. It does not need the raw health, location or transaction telemetry.

### Tier 2: plausible, but dependent on new geography or external data

#### 4. Travel Giving / Giving Atlas

Travel creates public “giving postcards” and journeys: places visited, causes encountered and organisations supported, with gift amounts private. This has a strong social product loop and avoids making CharityGraph itself a photo-sharing network.

The major CharityGraph requirement is accurate **service and impact geography**, not registered address. Overseas travel additionally requires local-charity data or vetted intermediary relationships beyond the Australian ACNC/DGR universe.

#### 5. Investment offsetting

Where a super fund continues to hold pokies, landmines, tobacco, fossil fuels or other contested exposures despite member lobbying, the principal's agent can direct a bounded amount to countervailing causes.

The investment side requires a separate holdings/corporate-exposure data layer. CharityGraph supplies the counter-harm mapping:

> harm → affected group → remedy → intervention → organisation/program

Offsetting must not be represented as cancelling the investment harm. It complements voice and exit; it does not replace them.

#### 6. See / Say / Do

The personal agent interprets a photograph or spoken observation through the principal's worldview, then queries CharityGraph. Two people can observe rough sleeping and infer entirely different problems: inadequate public safety, spiritual need, emergency accommodation, mental-health-system failure or structural poverty.

CharityGraph must not interpret the image or profile the affected people. It should answer structured queries produced by the personal agent.

### Tier 3: useful personal-agent features, but not core CharityGraph products

#### 7. Pressure-aware giving and moral receipts

The agent helps the principal decline checkout tips, supermarket appeals, street requests or other pressured asks while maintaining a funded giving policy. A green tick, haptic response or chime confirms that the situation was logged, allocated or settled.

This is psychologically attractive, but CharityGraph's contribution is downstream recipient and mandate resolution. The interaction design, screen scanning, transaction sweep and safety logic belong to the personal agent or wallet.

#### 8. Systemic tipping in fair-wage jurisdictions

In Australia and comparable jurisdictions, a user can decline platform-generated tipping prompts and allocate a fixed percentage of hospitality expenditure to worker-support, cooperative-development or structural-reform organisations.

CharityGraph needs an intervention taxonomy for direct relief, legal assistance, organising, advocacy, training and cooperative ownership. Jurisdictional labour-law logic and transaction classification should remain outside CharityGraph.

## 2. Product boundary

### Personal agent owns

- photographs, speech, location, health, transaction and social context;
- the principal's history, values and natural-language mandate;
- interpretation of what a situation means;
- challenge and trigger logic;
- adjudication precedents and matching rates;
- payment authority and budget limits;
- explanations tailored to the principal;
- decisions to donate, report, ask or abstain.

### CharityGraph owns

- canonical charity and program identity;
- registration and DGR observations;
- cause, beneficiary, approach and intervention classifications;
- primary versus material-adjacent versus incidental activity evidence;
- service and impact geography;
- ethos, affiliation and service/mission orientation;
- notable contextual facts;
- organisational and program relationships;
- source provenance, freshness, coverage and uncertainty;
- authentic action/donation endpoints where defensibly verified;
- compact agent-readable projections plus inspectable evidence.

### Other infrastructure owns

- bank, card, receipt and donation settlement verification;
- superannuation holdings and corporate exposure data;
- device telemetry and identity;
- regulated payment custody and execution;
- jurisdiction-specific legal conclusions.

## 3. Review of the current CharityGraph product

The files attached to the conversation are a legacy/minimal pipeline and are not an accurate statement of the current product. The authoritative current product is the `gregorycwhill/CharityGraph-Data` repository and its canonical shared contracts, particularly `PRODUCT.md`, `PRINCIPLES.md`, `CURRENT_STATE.md`, `PUBLIC_SCHEMA_VNEXT_SPEC.md`, `AGENT_DATA_DISTRIBUTION_CONTRACT.md`, `ROADMAP.md` and the implemented immutable release `v0.5.0-2026-08-15`.

CharityGraph v0.5 is already an agent-oriented, evidence-preserving knowledge product. The CharityGraph Card is the conceptual object; JSON, Markdown, CSV, Parquet and Viewer output are projections. The current contract explicitly rejects a one-ABN/one-subject model.

### Existing strengths relevant to agentic philanthropy

- Opaque stable `causebase_id` and explicit subject kinds: organisation, organisation group, legal entity, organisational unit, fund and program.
- ABN, ACNC ID, domains and names are external identifiers, never CharityGraph primary keys.
- Independent source-record identity and governed source-to-subject bindings, including unresolved and conflicting cases.
- Explicit relationships and lifecycle semantics rather than implicit name/brand inference.
- A common governed observation envelope with `claim_basis`, `extraction_method`, source/evidence references, time, confidence, warnings and derivation lineage.
- Longitudinal source and financial observations; current views are pointers/projections rather than destructive overwrites.
- Nested program observations with evidence, status and dates; later promotion to a durable subject requires a governed relationship.
- Evidence-bound activities, beneficiaries, descriptive geography, navigation geography, participation, opportunities, funding sources and fundraising methods.
- Capability-specific coverage states, including observed, not found in source, unavailable, not processed, failed, stale and unknown.
- Source-record sidecars, compact card evidence registries and immutable versioned releases.
- Stable per-subject JSON and Markdown, direct card URLs, manifests, schemas and an explicit agent/data distribution contract.
- A deployed immutable 120-card v0.5 release with 228 source sidecars and a passed 349-artefact manifest.
- A Golden Corpus, real document-stack bake-off, bounded Evidence Engine pilot and active human-gated Knowledge Validation process.
- Clear product guardrails: CharityGraph is descriptive public infrastructure, not a recommendation, rating, payment or persuasion product.

### Remaining gaps for the proposed use cases

These are additive capability gaps, not foundational architectural defects:

1. **Mandate-grade intervention semantics.** The current observation/classification architecture can carry them, but the validated taxonomy still needs stronger intervention, theory-of-change and harm/remedy concepts.
2. **Cause centrality.** Agentic mandate adjudication needs evidence-backed distinctions among primary purpose, material adjacency, designated-program relevance and incidental benefit. This should extend classifications/observations rather than create a universal fit score.
3. **Program and appeal coverage.** The contract already supports nested programs, but causal matching needs broader extraction of named programs, restricted appeals, gift designation and program-specific activity/ethos.
4. **Role-specific geography.** v0.5 correctly separates descriptive from controlled navigation geography. Travel Giving will additionally need explicit service-delivery, beneficiary, impact and program geography, plus locality and confidence.
5. **Ethos and service/mission orientation.** The design exists as a working first-class construct but is not yet part of the implemented v0.5 release contract.
6. **Notable context.** The design exists, but neutral inquiry, legal, regulatory, historical, recognition and controversy observations are not yet a scaled governed capability.
7. **Annual-report enrichment scale.** CharityGraph has a decisive document-stack decision and a bounded seven-PDF Evidence Engine pilot; the remaining issue is governed semantic promotion and progressive corpus scale, not absence of a document pipeline concept.
8. **Selective Wikipedia context.** Broad Wikimedia ingestion was correctly deferred after the ABN-first spike. The Ethos/Notability design now identifies a narrower use as an external editorial filter, citation graph and context-discovery source.
9. **Action/program endpoints.** Participation observations already distinguish action URLs from evidence URLs. Agentic philanthropy may need separately governed donation/program-designation endpoints, without turning CharityGraph into a payment product.
10. **Agentic-philanthropy evaluation cases.** Existing consumer-LLM and Golden Corpus work should be extended with mandate-adjudication fixtures: adjacent causes, ethos exclusions, designated programs, notable-context guardrails and partial matching precedents.

The appropriate next step is therefore to extend the existing v0.5 object model and common observation semantics. A replacement database architecture, EAV model, universal claim graph or return to one-row CSV thinking is neither needed nor consistent with the current product contract.

## 4. Ethos and Notability review

`ETHOS_AND_NOTABILITY_DESIGN.md` is highly aligned with agentic philanthropy and should be treated as a foundation rather than an optional enrichment.

### Ethos

Ethos supports mandate guarding where principals care about religious, political, philosophical, cultural or institutional orientation. The design correctly:

- separates organisational ethos from beneficiary/community characteristics;
- distinguishes self-description, formal affiliation, external characterisation, historical origin and service/mission orientation;
- scopes observations to organisation, program, service, organisational unit or related parent/network;
- prohibits inference from names, demographics, photographs or an LLM's impression;
- preserves disagreements instead of manufacturing one label;
- treats absence of evidence as unknown, not secular or unaffiliated.

For agentic use, `service_or_mission_orientation` may be as important as organisational ethos. A principal may accept a faith-affiliated service that is open regardless of faith but reject a program where worship or proselytising is required. These are mandate facts, not ratings.

### Notability

Notability supports the agent's reputational and contextual guardrails. The design correctly treats it as a set of neutral observations, never a score. Relevant categories include:

- institutional history and founders;
- significant people, movements, events or campaigns;
- awards and recognition;
- inquiries and public reviews;
- regulatory or legal matters;
- public criticism or controversy;
- merger, split, succession or renaming;
- global movement or network context.

Agentic use strengthens the need to preserve procedural status. “Investigated”, “named in an inquiry”, “found to have breached”, “cleared” and “remediated” must never be collapsed. Negative and positive context should use the same observation structure.

### Product implication

Ethos and Notability should remain descriptive evidence. The personal agent decides whether an ethos feature or notable event is disqualifying for its principal. CharityGraph should not create a universal reputation, prestige, scandal or safety score.

## 5. Taxonomies needed for future agentic use

### 5.1 Cause and beneficiary

Retain current goal and beneficiary mappings, but make them hierarchical, multi-valued, versioned and source-linked. Separate:

- primary cause;
- material adjacent causes;
- incidental co-benefits;
- claimed versus observed activities;
- organisation versus program scope.

### 5.2 Intervention / approach

This is the highest-priority new taxonomy. Suggested top-level candidates:

- emergency relief;
- direct service;
- treatment and rehabilitation;
- financial or material assistance;
- education and public awareness;
- research;
- legal assistance;
- advocacy and policy reform;
- organising and movement building;
- enforcement or inspectorate activity;
- infrastructure or capital provision;
- conservation and restoration;
- market/certification intervention;
- cooperative or community ownership;
- grantmaking/intermediation.

### 5.3 Theory of change and time horizon

Represent whether work is aimed at relief, recovery, prevention, system reform or long-term transformation. This enables complementary causal matching and investment offsetting.

### 5.4 Harm → remedy graph

Create a reference structure linking observable or financed harms to affected groups, remedies and interventions. Initial examples:

- gambling → crisis support, financial counselling, treatment, product safeguards, regulatory reform;
- landmines → clearance, survivor assistance, rehabilitation, treaty advocacy, peacebuilding;
- fossil fuels → mitigation, adaptation, transition, restoration, litigation;
- rough sleeping → outreach, crisis accommodation, housing, prevention, legal support, structural reform;
- water pollution → reporting, cleanup, restoration, education, producer responsibility.

### 5.5 Geography

Use explicit geography roles:

- registered/admin address;
- office location;
- service delivery geography;
- beneficiary geography;
- environmental impact geography;
- fundraising geography;
- program/appeal geography;
- locally led/locally registered/operating through partner.

Retain granularity and confidence: country, state, region, LGA, locality and free-text source geography.

### 5.6 Ethos and service orientation

Adopt the observation roles and scopes in the existing design. Test descriptors before freezing a universal hierarchy. Capture service-access conditionality separately.

### 5.7 Notable context

Use the candidate categories in the design document and preserve event date, procedural status, outcome, subject scope, source role and review status.

### 5.8 Organisational relationships

Represent parent, network, federation, program-of, operates-as, predecessor, successor, merger and grantmaking/intermediary relationships explicitly. This prevents a global parent's ethos or controversy being silently attached to an Australian affiliate.

### 5.9 Mandate-fit evidence

Do not publish a universal fit score. Supply dimensions from which a personal agent can adjudicate:

- primary-purpose strength;
- activity materiality;
- program designation;
- causal proximity;
- intervention fit;
- geographic fit;
- ethos/service-orientation fit;
- evidence freshness and confidence.

## 6. Data to extract from annual reports

Annual reports should be a first-priority enrichment source because they contain current, scoped operational detail unavailable from regulator checkboxes.

### Identity and structure

- legal and operating names;
- former names and brands;
- parent, member, federation and network relationships;
- subsidiaries, controlled entities and auspiced programs;
- mergers, successions and organisational changes;
- governance appointment rights and formal affiliations.

### Mission, ethos and service orientation

- current mission, values and worldview language;
- religious denomination/tradition or ideological orientation;
- declared secular or inclusive positioning where explicit;
- historical foundation where stated;
- whether services are open irrespective of faith or identity;
- whether worship, religious participation or evangelism is part of a program;
- cultural or lived-experience leadership claims;
- program-level differences from organisation-wide ethos.

### Programs and activities

- named programs and appeals;
- program descriptions;
- intervention/approach;
- intended beneficiary;
- operating geography;
- program partners;
- restricted versus unrestricted funding;
- current, commenced, concluded or pilot status;
- output and outcome claims with units and reporting period.

### Financial and operational context

- program expenditure where available;
- fundraising and administration disclosures;
- restricted funds and grants;
- employee, volunteer and service-volume metrics;
- dependence on government, major donors or related parties;
- grantmaking versus direct-service role.

### Notable context candidates

- founders and institutional history;
- mergers, renamings and milestones;
- inquiry, regulator or litigation disclosures;
- safeguarding or governance disclosures;
- major awards and public recognition;
- material incidents and remediation;
- significant public campaigns or policy achievements.

Self-promoted awards and achievements should be candidates, not automatically published Notability observations. Annual reports are primary evidence for what the organisation reports, not independent evidence that an award or event is externally notable.

### Extraction requirements

Every extracted observation should retain:

- source document and reporting year;
- page/section locator;
- concise evidence span;
- organisation/program/unit scope;
- source role (`self_described`, formal record, etc.);
- claim basis and extraction method;
- effective/event period;
- confidence and review state;
- coverage state and freshness.

## 7. Data to derive or discover through Wikipedia

Wikipedia is selectively valuable for **external context and source discovery**, not comprehensive coverage and not identity authority.

### Useful Wikipedia-derived candidates

- aliases, former names and operating names for candidate generation;
- founders and notable-person relationships;
- institutional and movement history;
- mergers, splits, successions and global network context;
- significant campaigns, events and policy roles;
- independently recognised awards;
- Royal Commissions, parliamentary inquiries, court and regulatory matters;
- significant criticism or controversy;
- external characterisations of ethos more specific than current promotional language;
- citations leading to inquiry reports, official histories and reliable secondary sources.

### Mandatory safeguards

- independently resolve the CharityGraph entity before attaching context;
- preserve Australian entity versus global parent/network scope;
- pin article revision and retrieval time;
- retain section/anchor and associated inline citations;
- prefer the underlying cited source as final evidence where practical;
- keep Wikipedia as a discovery path when it led to the source;
- prevent circular citation laundering back into Wikimedia;
- never treat absence from Wikipedia as negative evidence;
- do not turn article inclusion into a reputation or notability score;
- use neutral, procedural language and heightened review for contentious claims.

### What annual reports and Wikipedia contribute differently

| Question | Annual report | Wikipedia / cited sources |
|---|---|---|
| How does the organisation describe itself now? | Strong | Secondary |
| What programs operated this year? | Strong | Usually weak |
| Where were services delivered? | Often strong | Selective |
| What is the formal current structure? | Useful, sometimes incomplete | Useful for discovery; verify independently |
| How is the organisation externally characterised? | Weak | Stronger when well sourced |
| What historical context explains the organisation? | Selective/self-framed | Often valuable |
| What inquiries or controversies matter publicly? | May be incomplete | Valuable discovery/filter |
| Are awards externally notable? | Promotional candidate only | Useful editorial admission signal |
| What does absence mean? | Only source coverage | Nothing negative |

## 8. Recommended canonical data model

Do not replace the current canonical model. Extend the implemented v0.5 structures:

1. **Subjects/cards** — retain opaque `causebase_id`, explicit `subject_kind` and structured identity.
2. **Source records and bindings** — retain independent upstream identity, binding status, scope and conflicts.
3. **Common observation envelope** — reuse observation IDs, claim basis, extraction method, evidence/source references, time, confidence, warnings and derivation.
4. **Programs** — extend nested program observations with program/appeal type, gift designation, intervention, geography and scoped ethos; promote to durable subjects only when independently warranted.
5. **Relationships** — extend existing governed relationships where parent, network, program, predecessor/successor, auspice or intermediary structure is material.
6. **Classifications** — add intervention, theory of change, cause centrality and ethos dimensions with taxonomy/version/evidence and assignment method.
7. **Coverage registry** — add capabilities such as `understanding.interventions`, `understanding.ethos`, `understanding.notable_context` and finer program/geography coverage only after their observation contracts are approved.
8. **Evidence/source records** — add annual-report page/section evidence and revision-pinned Wikipedia discovery provenance while retaining source-family publication policy.
9. **Participation/action structures** — extend only where a verified destination or program designation is supported; keep evidence and action URLs distinct.
10. **Derived projections** — produce compact human/agent Ethos, Notability and mandate-fit ingredients with lineage, never universal recommendations or charity scores.

JSON/Markdown cards and sidecars remain the authoritative agent-facing representations. CSV/Parquet remain corpus projections rather than the canonical knowledge object.

## 9. Capture priorities

### Priority 0 — protect the implemented foundation

- treat `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_SCHEMA_VNEXT_SPEC.md` and the immutable v0.5 release as authoritative over legacy attached scripts;
- do not mutate `releases/v0.5.0-2026-08-15`;
- preserve the subject/source/binding/observation distinctions and common epistemic semantics;
- complete the active Knowledge Validation human gate before semantic promotion or corpus expansion;
- add agentic-philanthropy cases to the Golden Corpus rather than bypassing existing governance.

### Priority 1 — mandate-grade semantics

- broader program/service/appeal observations and governed promotion where needed;
- intervention/approach taxonomy;
- primary/material-adjacent/incidental classification strength;
- service/beneficiary/impact/program geography roles;
- harm → remedy → intervention reference mappings;
- use existing observation/evidence/provenance primitives.

### Priority 2 — annual reports

- extend the existing document/evidence pipeline and retained report inventory progressively;
- extract program, geography, intervention, ethos and relationship candidates;
- preserve page-level evidence;
- keep initial publication review-only;
- evaluate precision on a deliberately difficult cohort.

### Priority 3 — Ethos and Notability

- implement the accepted observation roles and scopes;
- test service/mission orientation as a distinct capability;
- run the proposed 30–50 organisation review cohort;
- use Wikipedia for contextual candidate generation and citation routing;
- require human review for contentious Notability in the first release.

### Priority 4 — agent contract

- extend the existing stable JSON/Markdown/manifest distribution contract;
- validate selective retrieval by cause, intervention, geography, ethos and program using static artefacts first;
- return evidence-backed fit dimensions rather than a universal recommendation score;
- expose uncertainty, freshness and coverage explicitly;
- provide compact agent projections with evidence links.

### Priority 5 — actionability

- verify donation endpoints and gift restrictions;
- identify program-level designations;
- add reporting, volunteering and contact endpoints where relevant;
- support downstream personal agents without receiving their private mandates or telemetry.

## 10. Near-term capture template

For each annual-report or Wikipedia-derived candidate, capture:

```yaml
subject_abn:
subject_scope: organisation | program | service | unit | parent_network
program_id:
observation_domain: cause | beneficiary | intervention | geography | ethos | notability | relationship
observation_type:
raw_value:
canonical_value:
strength: primary | material_adjacent | incidental | unknown
observation_role: self_described | formal_affiliation | externally_described | historical | service_or_mission
event_or_effective_start:
event_or_effective_end:
procedural_status:
qualification:
source_document_id:
source_role:
source_url:
source_revision:
source_date:
page_or_section:
evidence_span:
claim_basis:
extraction_method:
confidence:
review_status:
coverage_status:
```

Not every domain uses every field, but using one observation/evidence grammar prevents Ethos, Notability and annual-report extraction from becoming disconnected mini-products.

## 11. Product test

CharityGraph is agent-ready when a personal agent can ask:

> “My principal will match environmental causes, accepts food-system and wildlife adjacency at 50%, excludes compulsory religious participation, requires DGR status and permits only $10 autonomous gifts to unfamiliar recipients. Does this unrestricted gift qualify, what matching rate does the principal's precedent imply, and what evidence should I show if challenged?”

CharityGraph should return the organisation/program facts, scope, eligibility, relevant classifications, ethos/service orientation, notable context, uncertainty and provenance needed to answer. It should not decide the principal's values or execute the payment.

That capability unifies guarded discovery, causal matching, travel giving, challenges, investment offsetting and See/Say/Do while keeping CharityGraph focused on its durable comparative advantage.
