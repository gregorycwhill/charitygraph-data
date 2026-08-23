# Ethos and Notability — working product design

**Status:** Working product design; first-class constructs accepted, detailed contract not yet approved  
**Updated:** 2026-08-16  
**Scope:** Shared CharityGraph product design across Data, Builder and Viewer

This document is the working design space for two first-class CharityGraph constructs: **Ethos** and **Notability**. It deliberately precedes changes to the canonical product contract, public schema, roadmap or Viewer. Once the design is accepted, the durable decisions should be propagated into `PRODUCT.md`, `PRINCIPLES.md`, the public schema/contract material, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md` as appropriate.

The document also reopens the product-value question left narrow by `WIKIMEDIA_SOURCE_SPIKE.md`. The existing spike remains valid evidence that ABN-first Wikidata linkage is sparse. It does **not** settle whether Wikipedia is valuable as a selective contextual source, editorial filter, source-discovery graph or reciprocal public-knowledge partner.

## 1. Product thesis

A large share of the information people care about when understanding a charity is public but expensive to discover. It may be buried in a 35-page annual report, constitution, history page, inquiry report, Wikipedia article or other source that is technically available but practically high-friction.

CharityGraph should convert that public knowledge into low-friction, provenance-preserving public data:

> long source material → bounded evidence → structured observation → 5–30 words a person can understand → machine-readable data an agent can consume

This is not an invitation to turn CharityGraph into an evaluator. The product value is compression and structure, not judgement.

Two information domains are important enough to be first-class:

- **Ethos**: the worldview, tradition, affiliation or institutional orientation that materially characterises an organisation or one of its programs.
- **Notability**: externally noteworthy people, events, recognition, scrutiny or institutional history that materially helps a reader understand an organisation.

Both answer questions that regulator returns are poorly designed to answer. Both can be highly salient to donors, funders, researchers, service users and AI agents. Neither should collapse into a rating.

## 2. Accepted design direction so far

1. Ethos and Notability are first-class CharityGraph constructs, not incidental prose hidden in a summary.
2. Ethos concerns the organisation or a scoped program/unit, **not the presumed beliefs or ideology of the people it serves**.
3. Beneficiary/community characteristics remain separate. A Christian organisation serving a predominantly Muslim population is Christian because of evidence about the organisation, not because of the recipients.
4. The relationship between ethos and service/mission may itself matter and should be representable separately from both organisational ethos and recipient characteristics.
5. Ethos should distinguish self-description, formal affiliation, external characterisation and historical orientation rather than forcing them into one label.
6. Annual reports and the organisation’s own website are strong sources for **declared current ethos**. Constitutions, governance records and parent/network relationships are strong sources for **formal affiliation**.
7. Wikipedia and other robust secondary sources have a distinct role in external context, particularly where self-presentation is broad, selective, euphemistic or historically incomplete.
8. Notability is a collection of notable contextual facts, **not a scalar property or score**. CharityGraph must not produce a `notability_score`, “highly notable charity”, scandal score, prestige score or equivalent ranking.
9. For Wikipedia-derived Notability candidates, CharityGraph should initially rely substantially on Wikipedia’s existing editorial process instead of inventing an independent award-prestige, controversy-significance or source-credibility regime.
10. CharityGraph still owns subject binding, scope, provenance, qualification and neutral rendering. Wikipedia inclusion does not authorise attaching a global-parent fact to an Australian entity or flattening a disputed statement into an unqualified fact.
11. Absence from Wikipedia has no negative meaning. It cannot be used to infer that an organisation is unimportant, reputable, obscure or lacking notable history.
12. Wikimedia must never become an identity authority. Loose name/alias discovery is allowed for candidate generation; CharityGraph identity resolution remains governed by independent identity evidence.
13. CharityGraph should preserve circular provenance. A fact discovered from Wikipedia must not later be offered back to Wikipedia as independent corroboration merely because CharityGraph republished it.

## 3. User questions

### 3.1 Ethos

Ethos should help answer:

- Is this organisation religiously, politically, philosophically or culturally affiliated?
- How specifically can that orientation be described — for example, Anglican rather than merely Christian, where defensibly sourced?
- Is the orientation formal, self-described, externally described, historical, or some combination?
- Does a parent church, movement, ideology or network have a governance relationship with the organisation?
- Is the organisation historically rooted in a tradition it no longer formally belongs to?
- Does that ethos materially shape service delivery, advocacy, employment, evangelism, community participation or program design?
- Are services aimed at members of that tradition, merely delivered by an organisation with that tradition, or explicitly intended to propagate that tradition?
- Do the organisation’s own description and robust external descriptions materially differ?

### 3.2 Notability

Notability should help answer:

- What externally noteworthy facts should I know to understand this organisation?
- Who founded or shaped it?
- Is it connected to a significant person, movement, institution or event?
- Has it received genuinely notable recognition or awards?
- Has it played a meaningful role in a significant public campaign, event or policy change?
- Has it been examined by a Royal Commission, parliamentary inquiry, regulator, court or other public process?
- Has it been the subject of significant criticism, controversy or public scrutiny?
- Has it undergone a merger, split, succession, renaming or other institutional change that explains its present identity?
- Is the Australian organisation part of a larger global brand, federation or movement whose history is material to understanding the Australian operation?

CharityGraph answers by exposing bounded contextual facts and provenance, not by telling the user what conclusion to draw from them.

## 4. Separate but related constructs

### 4.1 Organisational ethos

Describes the organisation, organisational unit or program itself. Example descriptors might include Catholic social-justice tradition, Anglican, evangelical Christian, Islamic, Jewish communal, secular humanist, socialist tradition, feminist, Zionist or Indigenous-led cultural orientation.

These are examples, not an approved controlled vocabulary. The design must support specificity without pretending that all orientations fit a single hierarchy.

### 4.2 Beneficiary/community context

Describes populations or communities served, represented or targeted. It is not evidence of organisational ethos.

Examples include predominantly Muslim communities, Aboriginal and Torres Strait Islander people, LGBTQ+ young people, recently arrived refugees, or members of a particular church or cultural community.

**No ethos inference may flow automatically from beneficiary/community characteristics.**

### 4.3 Service or mission orientation

Describes whether and how organisational ethos enters the work. This is neither organisational ethos nor beneficiary identity.

Possible observations include:

- services available irrespective of faith;
- culturally specific service delivery;
- worship or religious participation forms part of the program;
- evangelism/proselytising is an explicit program purpose;
- advocacy is explicitly grounded in a stated worldview;
- religious participation is not required for service access.

The name `service_or_mission_orientation` is provisional; the distinction is more important than the label.

### 4.4 Relationships

Formal relationships should continue to use CharityGraph relationship semantics rather than being encoded only as ethos prose. `part_of`, `operates_as`, `program_of` or another approved relationship may provide stronger evidence than a descriptive label alone.

## 5. Ethos model

### 5.1 Observation-based, not a single categorical field

Do not reduce ethos to a scalar such as `ethos = Christian`.

A subject may simultaneously have a current self-description, formal affiliation, external characterisation, historical origin, scoped program orientation and explicit statements about how ethos affects service delivery.

The first version should preserve these as typed observations and generate a compact current projection only when justified.

### 5.2 Proposed observation roles

An ethos observation should distinguish at least:

- `self_described`: explicit current language used by the organisation about itself;
- `formal_affiliation`: constitutional, governance, membership, ownership or parent/network relationship;
- `externally_described`: characterisation in robust independent secondary evidence;
- `historical`: founded within, formerly affiliated with, or historically shaped by a tradition that may not describe the present organisation;
- `service_or_mission`: explicit relationship between ethos and a service/program/mission.

These roles are not mutually exclusive at subject level. A projection should not erase material disagreement between them.

### 5.3 Proposed scope

Every ethos observation should carry explicit scope. At minimum:

- `organisation`
- `program`
- `service`
- `organisational_unit`
- `related_parent_or_network`

A parent organisation’s ethos must not silently become the ethos of an Australian subsidiary, member or affiliate.

### 5.4 Candidate descriptor structure

Avoid premature ontology design. A useful candidate representation is:

- `raw_descriptor`: source-faithful concise descriptor;
- `descriptor_type`: small extensible type such as `religious_tradition`, `ideological_orientation`, `ethical_framework`, `cultural_orientation`, `institutional_affiliation`, `historical_origin`, `other`;
- `observation_role`;
- `scope`;
- source and evidence reference;
- claim basis, extraction method and derivation/inference method under the existing CharityGraph contract;
- time/effective period where relevant;
- qualification or disagreement metadata where needed.

The descriptor-type list is provisional and should be tested against real cases before becoming a public enumeration.

### 5.5 Projection behaviour

The human-facing Ethos projection should usually be 5–30 words. It may combine compatible observations but should preserve meaningful disagreement.

Examples of desired rendering behaviour:

> Christian; self-described as non-denominational, commonly characterised as evangelical.

> Secular service provider; founded by a Catholic order and retains a Catholic social-justice tradition.

> Affiliated with X movement; public materials describe the organisation more broadly as faith-based.

These are rendering examples only, not assertions about real organisations.

A projection is a view over observations, not an independently authored truth field. If the evidence does not support a safe compact synthesis, show separate sourced observations rather than forcing one sentence.

## 6. Ethos evidence policy

### 6.1 Source roles

**Organisation website and annual report** — best initial evidence for current declared ethos, values language, mission framing and statements about how ethos affects services.

**Constitution, governance records and formal network material** — best evidence for formal affiliation, control, membership, appointment rights and institutional relationships.

**Wikipedia and robust independent secondary sources** — useful for externally visible institutional context, historical description and characterisations that may be more specific than current promotional language.

**Historical archives and authoritative institutional histories** — useful where current identity differs from founding or historical orientation.

CharityGraph should preserve source role rather than silently applying a universal source-precedence rule.

### 6.2 Self-description is evidence, not editorial control

A charity is authoritative for “we describe ourselves as X”, but not necessarily for “the organisation is best characterised as X”. CharityGraph can retain both self-description and independent characterisation. Material differences are useful information and should not automatically be resolved into a winner.

### 6.3 Prohibited inference

Ethos is a sensitive domain and requires stronger inference discipline than ordinary activity extraction.

Do not infer organisational ethos solely from:

- names, surnames or presumed religion/ethnicity of directors, employees, volunteers, donors or beneficiaries;
- geographic location;
- demographic characteristics of service users;
- photographs or dress;
- one person’s political or religious activity unless it establishes a documented organisational relationship;
- language that merely “sounds” religious or ideological;
- an LLM’s impression of organisational tone;
- attendance by a staff member at an event;
- a beneficiary group associated with a religion, ethnicity, ideology or political cause.

CharityGraph should structure institutional evidence, not profile people or reverse-engineer ideology from demographic proxies.

### 6.4 External characterisation and disagreement

An external characterisation should be attributable. Where robust sources materially disagree, CharityGraph should preserve the disagreement rather than manufacture consensus.

A compact projection may say “self-described as X; independently described as Y” when that distinction is both material and well sourced.

## 7. Notability model

### 7.1 Contextual evidence, not an organisation score

The first-class construct may be called **Notability**, but its data is a set of **notable-context observations**. It must never imply that organisations without observations are less worthy, less significant or less reputable.

Potential categories to test include:

- `institutional_history`
- `founding_or_founder`
- `recognition_or_award`
- `notable_person_relationship`
- `significant_event_or_campaign`
- `public_inquiry_or_review`
- `regulatory_or_legal_matter`
- `public_criticism_or_controversy`
- `merger_split_or_succession`
- `movement_network_or_global_context`
- `other`

This list is a candidate taxonomy, not an approved public enumeration.

### 7.2 Neutrality

CharityGraph records a notable fact without translating it into a performance judgement.

- “Recipient of X Award, 2024” is context; “award-winning/high-quality charity” is evaluation.
- “Named in the findings of Y inquiry” is context; “scandal-prone charity” is evaluation.
- “Founded by X” is context; “prestigious organisation” is evaluation.

Positive and negative events use the same structural treatment. The construct should not become a reputation score with credits and debits.

### 7.3 Time and status

Notable context is often historical. Observations should retain event/effective time separately from retrieval and CharityGraph representation time.

Where a fact has a procedural status or outcome, preserve it. “Investigated”, “charged”, “found to have breached”, “cleared”, “apologised”, “award announced” and “award received” are not interchangeable claims.

### 7.4 People

Relationships to notable people may be useful, but the connection must itself be material and evidence-bound. A famous founder, patron, chair or campaigner can be relevant; incidental contact should not be promoted.

Contentious statements about living people require heightened sourcing discipline. CharityGraph should not use a charity card as an indirect way to republish poorly sourced allegations about an individual.

## 8. Wikipedia as an editorial filter for Notability

### 8.1 Terminology correction

The shorthand “did it survive the Wikipedia article?” is useful, but should not be misrepresented as Wikipedia’s formal **notability** test for each fact.

On English Wikipedia, formal notability mainly decides whether a **topic warrants a standalone article**. Individual article content is governed by verifiability, reliable sourcing, neutral point of view, due weight and related content policies.

The relevant CharityGraph signal is therefore:

> a fact has survived Wikipedia’s public editorial process under verifiability, reliable-sourcing, neutral-point-of-view and due-weight norms.

This is a pragmatic external editorial admission signal, not a claim that Wikipedia has formally certified the fact as “notable”.

### 8.2 Initial admission rule

For the first Wikipedia-derived Notability pilot, a contextual fact is eligible to become a **CharityGraph review candidate** when:

1. it appears as substantive article content in the relevant current or revision-pinned Wikipedia article/section;
2. it is materially about the CharityGraph subject, its explicitly related parent/network, or a scoped historical predecessor/successor;
3. it is not merely navigation, an infobox artefact, list-like directory entry or incidental mention;
4. it has an inline citation where the claim is contentious or otherwise requires one, or CharityGraph can follow the article’s citation graph to adequate supporting evidence;
5. CharityGraph can represent the fact neutrally without collapsing material qualification.

This deliberately outsources the first relevance/noteworthiness filter to Wikipedia rather than asking CharityGraph to invent award-prestige or controversy-significance rules before seeing the data.

### 8.3 What Wikipedia does not buy CharityGraph

Wikipedia’s editorial process does **not** mean:

- every Wikipedia statement is correct;
- every article is complete;
- every cited source is equally strong for every claim;
- absence from Wikipedia is meaningful;
- article text may be copied without licensing/attribution consideration;
- CharityGraph can skip subject/scope resolution;
- CharityGraph should publish current vandalism or an unstable claim immediately.

### 8.4 Revision provenance

For every Wikipedia-derived candidate retain, privately or publicly as appropriate:

- article title and canonical URL;
- revision ID or permanent revision URL;
- retrieval time;
- section/anchor or equivalent locator;
- concise source excerpt or evidence locator subject to rights policy;
- inline citation(s) associated with the claim where available;
- CharityGraph subject/scope decision;
- whether Wikipedia is the supporting source or only the discovery source.

### 8.5 Prefer underlying citation where practical

Preferred provenance chain:

> Wikipedia revision → discovery lead → underlying inquiry/report/news/award source → CharityGraph contextual observation

Where CharityGraph independently acquires adequate underlying evidence, that source should normally become the observation evidence and Wikipedia should remain recorded as a discovery path.

Where Wikipedia itself remains the practical secondary synthesis, CharityGraph may retain it explicitly as a community-edited secondary source, with revision provenance and appropriate attribution.

### 8.6 Circular provenance guardrail

A Wikipedia-derived observation must not later be offered back to Wikipedia as independent confirmation merely because it appears on CharityGraph.

If Wikipedia led CharityGraph to a Royal Commission report, CharityGraph can offer the **Royal Commission report** to a future Wikimedia editor. It should not offer “CharityGraph says X” as independent evidence when CharityGraph learned X from Wikipedia.

## 9. Wikipedia/Wikidata discovery and identity

### 9.1 Reinterpret the ABN-first spike

The existing 120-card spike found seven exact Wikidata ABN matches and two English-Wikipedia links. That remains useful evidence about **ABN-addressable Wikidata coverage**. It should not be interpreted as Wikipedia context coverage or user-relevant coverage.

A proper follow-up should measure at least:

1. exact identifier-linked Wikimedia coverage;
2. high-confidence corroborated candidate linkage after the CharityGraph subject is already independently known;
3. contextual yield on charities likely to be of user interest.

### 9.2 Candidate discovery may be fuzzy; identity binding may not

CharityGraph may search Wikipedia/Wikidata using legal names, operating/trading names, former names and aliases, official website/domain, known parent/network names, geographic context and independently established relationships.

These are valid candidate-generation mechanisms. They do not, by themselves, authorise CharityGraph identity resolution. Ambiguity remains ambiguity.

### 9.3 Global brand and Australian entity

Useful Wikipedia context may live in a dedicated Australian article, an Australian subsection of a global article, the global article’s history/organisation sections, or an article about a predecessor, movement or network.

CharityGraph must preserve scope explicitly. A scandal, award or political position of a global parent is not automatically an observation about the Australian legal entity. It may be useful as `related_parent_or_network` context if the relationship is independently established and the rendering makes scope clear.

## 10. Coverage semantics

### 10.1 Notability

Absence is especially easy to misread. `not_found_in_source` must mean only that no eligible notable-context observation was found in the selected/processed source set. It must **not** render as no notable history, no controversies, no recognition, not notable, good reputation or low public profile.

### 10.2 Ethos

Failure to find an explicit ethos statement does not prove that an organisation is secular, non-religious, politically neutral or unaffiliated.

A negative descriptor such as “secular” should be published only when it is itself supported, not inferred from failure to find a religious affiliation.

Both constructs should reuse existing CharityGraph coverage states such as `observed`, `not_found_in_source`, `not_available_from_source`, `not_yet_processed`, `retrieval_failed`, `stale` and `unknown` as appropriate.

## 11. Representation and progressive disclosure

### 11.1 Viewer

The default human presentation should be compact and inspectable.

```text
Ethos
Catholic social-justice tradition; services available regardless of faith.

Notable context
• Founded by …
• Named in … inquiry, 2021.
• Recipient of … award, 2024.
```

Every concise item should have a direct provenance path. Viewer language should not turn the section into a “pros and cons” box or reputation dashboard.

### 11.2 Machine representation

Preserve more than the Viewer projection:

- observation ID;
- domain and type;
- subject and scope;
- concise value/statement;
- event/effective period;
- claim basis;
- extraction method;
- derivation/inference method where applicable;
- source/evidence references;
- source role;
- qualification/disagreement;
- coverage/freshness;
- lineage sufficient to prevent citation laundering.

Reuse existing CharityGraph observation/evidence primitives rather than inventing a parallel provenance system.

### 11.3 Agent projection

The 5–30 word compression is particularly valuable for agents. A general-purpose LLM should be able to answer “is this organisation religiously affiliated?” or “what notable context should I know?” from a compact record while still being able to follow evidence links when nuance matters.

## 12. Licensing and source rights

Wikipedia article prose is CC BY-SA. CharityGraph should avoid unnecessary prose copying. Preferred pattern:

- extract the underlying fact/relationship/event;
- write CharityGraph-neutral concise rendering;
- retain Wikipedia revision attribution where Wikipedia is a source;
- follow and cite the underlying source where practical;
- preserve upstream licensing obligations.

Wikidata structured data remains useful for identifiers, aliases, relationships and discovery where available, but community-maintained Wikidata observations do not become authoritative merely because they are structured.

## 13. Reciprocal Wikimedia relationship

### 13.1 Wikimedia → CharityGraph

Potential value:

- externally filtered contextual facts;
- history and relationship discovery;
- article-to-source citation graph;
- aliases and candidate identifiers;
- external descriptions of ethos;
- discovery of scrutiny, recognition, people and events.

### 13.2 CharityGraph → Wikimedia

Potential future value:

- stable CharityGraph external identifier in Wikidata;
- citation-ready regulator and annual-report facts;
- longitudinal structured financial/regulatory observations;
- stable identity crosswalks;
- evidence packets for improving weak/stub charity articles;
- source discovery for information otherwise buried in annual reports and government records.

CharityGraph should first be useful as structured research and citation-routing infrastructure. Becoming a source cited in its own right is something to earn through transparent methods, stability, correction governance and demonstrated reliability.

A future Wikimedia-export path must exclude circularly sourced claims or point through to their independent underlying evidence.

## 14. Evaluation design

The next Wikimedia/Ethos/Notability evaluation should be designed around **information yield and correctness**, not raw ABN-match coverage.

### 14.1 Suggested cohort

Use roughly 30–50 deliberately selected organisations covering:

- prominent national charities likely to be investigated by donors;
- Australian affiliates/branches of global brands;
- explicitly religious service organisations across multiple traditions;
- organisations with subtle denominational or ideological distinctions;
- organisations whose current self-description is broader than historical/formal affiliation;
- avowedly secular or ideological organisations;
- charities operating in communities with a different dominant religion/ethos from the organisation itself;
- organisations with major inquiry/regulatory/legal context;
- organisations with notable awards/recognition;
- organisations with substantial Wikipedia pages;
- organisations with only a parent/global Wikipedia article or subsection;
- organisations with no useful Wikipedia presence;
- small/local controls to test the meaninglessness of Wikimedia absence.

Selection is an evaluation strategy, not a public CharityGraph ranking of “important charities”.

### 14.2 Ethos review questions

For each case ask:

1. What does the organisation explicitly call itself?
2. What formal affiliations or governance relationships can be established?
3. How do robust independent sources characterise it?
4. Is there a material historical orientation distinct from the current one?
5. Does ethos affect service/mission in an explicitly evidenced way?
6. Are recipient/community characteristics being kept separate?
7. Is any proposed descriptor inferred from names, demographics or other prohibited proxies?
8. Can the answer be rendered faithfully in 5–30 words?
9. Is any disagreement material enough to preserve in the projection?
10. Does the observation apply to the whole organisation or only a program/unit/parent?

### 14.3 Notability review questions

For each case ask:

1. What article/section or independent source generated the candidate?
2. Is the fact substantive enough to have survived the article’s editorial context, rather than being incidental or directory-like?
3. What source supports it?
4. Is Wikipedia the evidence source or only the discovery source?
5. Is subject scope correct?
6. Is the event/status/time represented accurately?
7. Is the rendering neutral?
8. Is a positive or negative event being turned into an evaluative label?
9. Would absence of this observation be at risk of being misread as a negative claim?
10. Is the item sufficiently distinct from other observations to avoid duplicate “pile-on” context?

### 14.4 Metrics

**Discovery/linkage**
- exact identifier matches;
- corroborated non-identifier candidate matches;
- ambiguous/rejected matches;
- dedicated article vs subsection/global-parent context.

**Context yield**
- subjects with one or more useful ethos observations;
- subjects with one or more useful notable-context observations;
- observations by category/source role;
- underlying cited-source follow-through rate;
- yield by salience/subject stratum rather than only unweighted entity count.

**Quality**
- subject/scope precision;
- factual support precision;
- self/formal/external/historical distinction accuracy;
- recipient-vs-organisation separation;
- neutral rendering acceptance;
- qualification/disagreement preservation;
- circular-provenance violations;
- human edit/reject rate.

Precision should dominate recall for both domains in v1.

## 15. Candidate hard cases

### A. Christian organisation in a predominantly non-Christian community

Expected result: organisational ethos derives from organisational evidence; community context is separately recorded; service/mission orientation explains any evangelism, faith-neutral delivery or other explicit relationship.

### B. Broad self-description, specific external characterisation

Expected result: preserve both where well sourced, e.g. “self-described as faith-based; independently characterised as [specific tradition]”. Do not let the external label silently replace self-description.

### C. Historical religious foundation, currently independent

Expected result: current formal status and historical origin remain distinct. Do not render “Catholic” as a current affiliation solely because Catholic clergy founded the organisation a century ago.

### D. Global movement with Australian affiliate

Expected result: Australian identity and formal relationship are resolved independently. Global history/context can be shown as parent/network context but cannot be silently attached to the local entity.

### E. Award-heavy charity website

Expected result: organisation-promoted awards are not automatically Notability observations. In the initial Wikipedia-derived route, only awards surviving the relevant independent editorial context enter the Wikipedia candidate set.

### F. Inquiry or controversy

Expected result: preserve exact procedural/status language and source scope. Do not render an allegation as a finding, an inquiry appearance as wrongdoing, or a global-parent controversy as an Australian-entity controversy.

### G. No Wikipedia presence

Expected result: no negative conclusion. Ethos may still be well observed from primary/formal sources; Notability coverage remains a source-coverage statement only.

## 16. Interaction with existing CharityGraph principles

This design should extend, not bypass, existing product rules:

- **Describe before evaluating:** ethos and notable context are descriptive observations.
- **Evidence precedes synthesis:** source extraction and identity/scope binding precede compact prose.
- **Extract broadly, canonicalise selectively:** retain raw/source-native descriptors and selectively project them.
- **Claim basis is separate from extraction:** a Wikipedia sentence recovered by parser/LLM does not determine whether the resulting claim is direct, inferred or derived.
- **Coverage is not a negative claim:** missing ethos/notability evidence cannot imply secularism, good reputation or obscurity.
- **Identity is independent of source records:** Wikipedia/Wikidata candidates cannot mint or resolve a CharityGraph subject by name alone.
- **Viewer is an epistemic interface:** no reputation dashboard, prestige badge or red/green controversy treatment.
- **Agents are first-class consumers:** both constructs need compact structured representations with provenance.

## 17. Schema questions deliberately left open

Do not freeze these until real-case review provides evidence:

1. Whether the public top-level key should literally be `ethos`, `ethos_observations`, or another projection + observation pair.
2. Whether Notability should expose a public key named `notability`, `notable_context`, `context`, or another term while retaining Notability as the product construct.
3. The minimum useful controlled vocabulary for ethos descriptor types.
4. Whether religious denominations/traditions should have a separate reference taxonomy or remain source-faithful descriptors in v1.
5. How to represent nested/overlapping orientations such as denomination + theological stream + ethical framework without creating a brittle universal hierarchy.
6. The final Notability category list.
7. Whether a Wikipedia-derived candidate can be publicly supported by Wikipedia alone in low-risk cases, or whether selected categories require following an underlying citation before publication.
8. Refresh policy for mutable Wikipedia context and how material article changes invalidate or re-review existing observations.
9. Whether contentious/controversy observations need an additional human-review requirement even after the general pipeline becomes more automated.
10. How much Wikipedia revision metadata belongs in public cards versus source sidecars/lineage.
11. Whether and when non-English Wikipedia editions should become discovery sources.
12. How to identify and deduplicate the same notable event reported through Wikipedia, an inquiry source and a charity annual report.
13. Whether service/mission orientation belongs inside Ethos or should become its own first-class capability after evaluation.

## 18. Design sequence while Codex execution is paused

This design can be advanced largely without Codex credits.

### Product-design work in ChatGPT + local repo

1. Challenge construct boundaries and names against real examples.
2. Research Wikimedia editorial/source rules only where they materially affect the design.
3. Select a 30–50-case evaluation cohort from the existing corpus plus additional deliberately salient cases if useful.
4. Define a compact human review packet for Ethos and Notability.
5. Develop candidate observation/projection examples against the existing v0.5 contract.
6. Resolve the open schema and publication-policy questions above.
7. Update this document as decisions settle.
8. Once approved, propagate accepted decisions into canonical CharityGraph documents in one consolidation pass.

### Later Codex implementation work

Codex should receive the approved Data commit SHA and a short implementation brief. It should then implement only the required acquisition, candidate-generation, evaluation and validation machinery; it should not be asked to rediscover the product design.

The first implementation should remain review-only. It must not mutate the immutable v0.5 release or publish Ethos/Notability observations before the human/product gate.

## 19. Candidate acceptance tests for the design

Before treating Ethos and Notability v1 as implementation-ready, the design should demonstrate that CharityGraph can answer these two questions across awkward real cases:

> **Ethos:** “What worldview, tradition or institutional orientation characterises this organisation, and does it materially affect the way its services or mission operate?”

> **Notability:** “What externally noteworthy context should I know to understand this organisation?”

A satisfactory answer should:

- usually fit each projected item into 5–30 words;
- bind the claim to the correct organisation/program/parent scope;
- preserve self-description versus external characterisation;
- never infer organisational ethos from recipient demographics or personal protected attributes;
- keep historical and current orientation distinct;
- preserve procedure/status for inquiries, litigation and controversies;
- give direct provenance sufficient for inspection;
- avoid evaluative language;
- make source absence non-negative;
- be legible to a human and a general-purpose AI agent without reading the original long source.

## 20. Policy concepts to verify during implementation

The Wikipedia-specific design should be checked against the then-current English Wikipedia policy/guideline pages, particularly:

- `Wikipedia:Notability`
- `Wikipedia:Notability (organizations and companies)`
- `Wikipedia:Verifiability`
- `Wikipedia:Reliable sources`
- `Wikipedia:Neutral point of view`

These are inputs to CharityGraph’s policy design, not delegated governance. CharityGraph remains responsible for identity, scope, provenance, licensing, public rendering and correction behaviour.
