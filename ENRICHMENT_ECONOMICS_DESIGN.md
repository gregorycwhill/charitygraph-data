# CharityGraph Enrichment Economics — Benchmarking, Planning and Evaluation Design

> **Status: superseded as implementation authority.** Retained as detailed benchmark-design history. `COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md` controls model role, cohort order, budgets, local-NLP scope, scheduling, caching, governance and coverage-first acceptance. Any conflicting route, priority, review or stopping rule in this document does not apply.

**Status:** Working product design; not yet canonical  
**Updated:** 2026-08-22  
**Scope:** CharityGraph Data, Builder and evaluation workflow  
**Purpose:** Specify how CharityGraph should maximise useful, trustworthy enrichment coverage per dollar while distinguishing true public-information sparsity from source-scope and extraction-economics limits.

---

## 1. Product objective

CharityGraph aims to build as much **useful, evidence-backed enrichment coverage of relevant Australian charities as is economically justified**.

If inference cost were irrelevant, a plausible reference workflow would give a strong multimodal model the last several years of regulator data, annual reports, current website evidence, Wikimedia context, all relevant taxonomies and the full CharityGraph schema, then ask it to construct the card directly.

That is not the production design.

CharityGraph instead uses a staged architecture:

> **acquire broadly and cheaply → extract deterministically where possible → retrieve bounded evidence → use low-cost semantic interpretation where useful → selectively escalate difficult/high-yield cases → publish only governed observations**

The reason is economic as much as technical. Many enrichment facts can be recovered without expensive inference; many others do not exist in the public source universe at all. Spending more model tokens cannot create information that charities have never published.

The product therefore needs to answer two different questions:

1. **Coverage question:** how much useful public knowledge about a charity can CharityGraph represent?
2. **Economic question:** how much of that recoverable knowledge can CharityGraph obtain at an acceptable marginal cost?

The central optimisation problem is:

> **Maximise accepted useful observations and meaningfully enriched subjects per dollar, subject to CharityGraph's precision, provenance, neutrality and safety constraints.**

This document defines how to measure that frontier and use it to plan the production pipeline.

---

## 2. Alignment with existing CharityGraph principles

This design extends rather than replaces the current product contract.

It relies especially on the existing principles that:

- evidence precedes synthesis;
- deterministic acquisition and extraction should narrow evidence before LLM interpretation;
- extraction method and claim basis are distinct;
- source-native observations should be preserved and canonicalised selectively;
- coverage states should be explicit rather than inferred from blank fields;
- sparse cards are valid where sparse evidence is the honest public record;
- LLMs are both an implementation technology and a major downstream distribution channel;
- CharityGraph describes before evaluating;
- fundraising economics, charity quality and recommendation remain downstream concerns.

Economic optimisation must not weaken those rules. A cheaper pipeline that fabricates, over-generalises or loses provenance is not better.

---

## 3. The sparsity decomposition

A blank or missing enrichment field can arise for fundamentally different reasons. CharityGraph should distinguish them during evaluation.

### 3.1 Public-evidence absence

The relevant fact is not found in any reasonable public source inspected during benchmark review.

Examples:

- a very small association has no public statement of organisational ethos;
- a local charity has no externally noteworthy institutional history documented online;
- fundraising is handled informally and no public description of its methods exists.

This is **irreducible public-record sparsity** unless new evidence appears later.

More compute should not be spent trying indefinitely to fill these blanks.

### 3.2 Source-scope gap

The relevant fact is public, but outside the source families or pages CharityGraph currently acquires.

Examples:

- volunteering activity exists only on Facebook;
- an event is documented on Humanitix but not the charity website;
- fundraising activity is described in a community newsletter not discovered by the current pipeline;
- useful context exists in an inquiry report, media article or parent organisation page not yet in the acquisition scope.

This is an **acquisition/scope problem**, not a model-quality problem.

### 3.3 Extraction-economic gap

The relevant evidence is already inside CharityGraph's acquired source bundle, but the production pipeline fails to convert it into a governed observation.

Examples:

- local Python extraction retrieves the right annual-report page, but the low-cost LLM misses a nuanced discontinued fundraising practice;
- the deterministic website parser collects a paragraph but the domain candidate extractor routes it incorrectly;
- a low-cost model fails to resolve a scoped organisational ethos that a stronger model and human reviewer can identify from the same evidence.

This is the main area where stronger extraction, better retrieval, better prompts, or selective model escalation can improve coverage.

### 3.4 Governance/publication gap

Relevant evidence exists and may be understood, but CharityGraph should not publish the resulting assertion without additional support or review.

Examples:

- ethos would require an impermissible inference from beneficiary demographics;
- a controversy claim about a living person lacks adequate sourcing;
- an international parent fact cannot safely be scoped to the Australian charity;
- overlapping expense lines prevent a fundraising attribution bound.

This is **desirable epistemic sparsity**, not pipeline failure.

### 3.5 Processing gap

The relevant capability has simply not yet been processed, or a retrieval/build failure prevented assessment.

This should remain distinguishable from all four categories above.

---

## 4. Benchmark outcome classes

The benchmark should classify each potentially useful proposition into one of the following internal evaluation outcomes.

| Benchmark outcome | Meaning | Product implication |
| --- | --- | --- |
| `observed_economically` | Production pipeline recovered and governed the observation | Production architecture is sufficient for this case |
| `recoverable_but_missed` | Evidence is in the acquired bundle, but production missed it and stronger/human review recovered it | Extraction-economic opportunity |
| `outside_acquired_scope` | Public evidence exists, but not in the production source bundle | Source-acquisition opportunity |
| `no_public_evidence_found` | Reasonable benchmark search found no publishable public evidence | Genuine public-record sparsity |
| `present_but_non_publishable` | Evidence exists but cannot responsibly support a CharityGraph observation | Governance boundary is working |
| `not_evaluated` | Benchmark did not assess the proposition/capability adequately | Evaluation gap; never treat as absence |

These are **benchmark labels**, not necessarily new public card coverage statuses.

Public CharityGraph should continue to use its governed capability/coverage model. The benchmark is an internal tool for understanding why coverage looks the way it does.

---

## 5. The reference benchmark ladder

The benchmark should compare a sequence of increasingly expensive conditions. Each level answers a different question.

### Condition P0 — structured/public-regulator baseline

Inputs:

- structured ACNC/AIS data;
- DGR/tax data;
- other selected structured government data.

Processing:

- deterministic parsing and normalisation only.

Purpose:

- establish the zero/near-zero inference-cost baseline;
- identify domains already recoverable without documents or websites.

### Condition P1 — deterministic source extraction

Inputs:

- P0 sources;
- acquired annual reports/documents;
- acquired website pages;
- selected Wikimedia structured data where in scope.

Processing:

- local parsing;
- document text/table/OCR/vision routing already approved by CharityGraph;
- website normalisation;
- deterministic passage retrieval;
- deterministic candidate generation where appropriate.

No semantic LLM interpretation beyond any explicitly benchmarked component.

Purpose:

- measure how much coverage Python/local tooling provides;
- identify extraction failures that do not require model intelligence.

### Condition P2 — production low-cost semantic pipeline

Inputs:

- the same acquired source universe as P1;
- only bounded/retrieved slices selected by deterministic preprocessing.

Processing:

- current proposed production-grade low-cost LLM(s);
- structured output;
- domain-specific prompts/policies;
- current escalation and human-review rules.

Purpose:

- estimate actual scalable production coverage, quality and cost.

### Condition P3 — selectively escalated production pipeline

Inputs:

- same production source bundle;
- only cases routed for escalation by a governed planner.

Processing:

- stronger model or more expensive reasoning only where expected incremental information value justifies the spend.

Purpose:

- test whether selective escalation materially moves the cost/coverage frontier.

P3 should not become “send every unresolved case to the expensive model”.

### Condition O — high-spec same-source oracle

Inputs:

- **exactly the same source bundle available to production**;
- substantially more complete context than P2/P3, including full relevant reports/pages where practical;
- complete applicable CharityGraph schema, taxonomy and editorial instructions.

Processing:

- a high-capability model such as Sol-High, using a deliberately expensive/full-context extraction strategy.

Purpose:

- estimate the amount of useful information recoverable from the acquired evidence if model/inference cost were much less constrained;
- isolate extraction-economic loss from source-scope loss.

This condition is an **oracle approximation**, not ground truth. Its outputs still require adjudication.

### Condition H1 — human same-source adjudication

Inputs:

- same acquired source bundle as production and O.

Processing:

- knowledgeable human review of production/oracle disagreements and a bounded sample of apparent mutual misses.

Purpose:

- establish the reference proposition set for the acquired source universe;
- determine whether the high-spec oracle or production pipeline is actually correct;
- identify false positives and over-synthesis by the oracle.

### Condition H2 — broader public-source audit

Inputs:

- acquired source bundle plus a deliberately broader public search universe.

Possible additional sources:

- external event platforms;
- social media where lawful/practical;
- inquiry/regulatory reports;
- third-party institutional histories;
- relevant media/secondary sources;
- network/parent pages;
- other public sources discovered by human search.

Processing:

- human-led search, optionally assisted by a high-spec model.

Purpose:

- estimate the **source-scope gap**;
- determine whether an apparent blank reflects a missing source family rather than extraction failure.

H2 should run on a subset rather than the whole national corpus. It is an evaluation instrument, not automatically a commitment to acquire every discovered source operationally.

---

## 6. Why the same-source oracle matters

The benchmark must not compare the production pipeline with a high-spec model that is also allowed to browse a broader source universe unless the experiment explicitly intends to measure source acquisition.

Otherwise two effects become confounded:

- stronger reasoning/extraction;
- access to more evidence.

The primary economic comparison is therefore:

> **P2/P3 versus O/H1 on the same acquired evidence.**

That measures how much useful information CharityGraph is leaving inside sources it already paid to acquire.

The separate H2 audit measures whether the source universe itself is too narrow.

---

## 7. Evaluation unit: the proposition ledger

Simple field-by-field string matching is not adequate for semantic enrichment.

A strong model may split one paragraph into five propositions while a cheap model produces two concise observations. Counting raw outputs would reward verbosity rather than information value.

The benchmark should therefore maintain a **human-adjudicated proposition ledger** for evaluated cases.

Each accepted proposition should contain enough structure to compare pipelines:

- subject/legacy public ID;
- domain/capability;
- scoped sub-entity if relevant;
- concise proposition;
- canonical term/type if applicable;
- source role;
- evidence locator(s);
- effective/reporting time;
- claim basis;
- publishability decision;
- required qualification;
- optional relationship to duplicate/equivalent propositions.

Examples:

- “Organisation operates a current gifts-in-wills program.”
- “2025 Giving Day used matched giving.”
- “Organisation describes itself as non-denominational Christian.”
- “Independent source characterises the organisation as evangelical.”
- “Volunteer participation is publicly invited via current website.”

Production and oracle outputs are matched against this ledger as:

- correct/equivalent;
- partially correct/needs edit;
- missed;
- unsupported false positive;
- wrong subject/scope;
- wrong temporal state;
- prohibited inference.

The benchmark should not require a universal microscopic claim graph for CharityGraph production. This ledger is an evaluation device.

---

## 8. Benchmark cohort design

The first serious enrichment-economics benchmark should contain roughly **120 charities**, large enough to show structure but still feasible for selective human adjudication.

Do not rely on a purely random sample. The benchmark needs deliberate variation on the dimensions that affect extraction economics.

### 8.1 Stratify size and source richness separately

Charity size is not the same as processing cost or evidence richness.

A very small charity may have a three-page website whose entire public evidence universe is cheap to understand. A large national charity may have multiple related entities, three 100-page annual reports, dozens of programs, many fundraising channels and complex history.

The cohort should therefore cross:

**Organisation size**

- very small;
- small;
- medium;
- large/very large.

with:

**Source richness**

- regulator-only / near-empty web presence;
- thin website;
- rich website but no report;
- annual report available;
- multi-year reports;
- Wikimedia/independent context;
- multiple relevant source families.

### 8.2 Include complexity strata

Deliberately include:

- simple one-entity charities;
- groups/federations;
- Australian affiliates of international brands;
- operating names/former names;
- charities with many programs;
- charities with transient participation/fundraising activity;
- religious/ideological organisations;
- charities with public scrutiny/notability context;
- sparse local/community organisations.

### 8.3 Domain coverage

The cohort must contain enough positive and negative opportunities to assess:

- activities;
- beneficiaries;
- programs;
- participation/opportunities;
- funding sources;
- fundraising practices/campaigns;
- fundraising expenditure;
- ethos;
- notability/context;
- relationships/identity where relevant.

The benchmark should not let easy activity extraction dominate the economics of harder, high-value fields.

### 8.4 Reuse existing corpus carefully

Existing Golden Corpus and 120-card fixtures should be reused where they provide suitable cases and source retention.

Do not allow convenience of existing cases to defeat the economic stratification above. Add purpose-selected benchmark cases if necessary.

---

## 9. Source-opportunity inventory

Before semantic extraction, CharityGraph should produce a cheap **source-opportunity inventory** for every subject.

Candidate features include:

- AIS years available;
- annual reports available by year;
- annual-report page count;
- text extraction quality;
- number of visual/table-heavy pages;
- website reachable;
- number of substantive same-origin pages discovered;
- page roles available;
- total substantive text volume;
- fundraising/giving/volunteer/governance/about links discovered;
- relevant deterministic keyword/passages found;
- Wikipedia/Wikidata candidate status;
- parent/network source availability;
- prior CharityGraph observations requiring refresh;
- known identity ambiguity.

This inventory serves two purposes:

1. benchmark explanation — why was a subject cheap, expensive or sparse?
2. production planning — where is further inference likely to yield useful information?

It should be deterministic and cheap enough to run across the full corpus.

---

## 10. Production enrichment planner

CharityGraph should not allocate the same LLM budget to every charity.

The planner should be a governed routing system whose purpose is to allocate expensive interpretation where evidence opportunity is highest.

### 10.1 Universal cheap baseline

Every in-scope charity should receive the same broad low-cost baseline appropriate to available public records:

- regulator ingestion;
- identity reconciliation;
- source discovery;
- deterministic website/document extraction where sources exist;
- capability coverage assessment;
- cheap evidence-opportunity diagnostics.

This prevents the system from simply ignoring small organisations.

### 10.2 Evidence-richness routing

Additional semantic spend should depend primarily on **available evidence and unresolved information opportunity**, not charity size or perceived importance.

Examples:

- no annual report + tiny website + no relevant passages → little reason for five domain-specific LLM calls;
- 80-page annual report + rich giving pages + relevant fundraising passages → high expected yield from targeted semantic extraction;
- Wikipedia article with multiple cited historical sections → worthwhile Notability review;
- explicit ethos language in About/Governance pages → cheap Ethos extraction;
- no independent/contextual source → do not spend repeatedly trying to manufacture Notability.

### 10.3 Bundle small evidence universes

Where a charity's entire substantive evidence set is small, it may be cheaper and more accurate to send one compact evidence bundle to a low-cost model and request several structured domains together rather than run many separate calls.

This should be benchmarked rather than assumed.

### 10.4 Slice large evidence universes

For large organisations, deterministic retrieval should isolate relevant evidence before semantic calls.

Examples:

- fundraising passages → fundraising extraction;
- governance/values/history passages → Ethos;
- participation/get-involved pages → participation;
- Wikipedia article sections/citations → Notability.

Do not repeatedly send a 100-page report to a model for independent tasks unless benchmarking shows this is economically superior.

### 10.5 Selective escalation

Escalation to a more expensive model should require a measurable evidence opportunity, such as:

- low-cost model returns a structured ambiguity on an evidence-rich passage;
- deterministic candidate exists but low-cost interpretation fails validation;
- domain is high-value and benchmarked escalation has strong incremental yield;
- identity/scope complexity materially blocks otherwise recoverable facts;
- a source is too visually/semantically complex for the cheap route.

Do not escalate merely because a public field is blank.

---

## 11. Economic metrics

CharityGraph should report both **quality-adjusted information yield** and **subject coverage**, because raw observation counts can be misleading.

### 11.1 Accepted observations per dollar

For pipeline stage `s`:

> **accepted observation yield(s) = newly accepted propositions attributable to stage s / marginal variable cost of stage s**

Report by domain and stratum.

Do not pool all domains into one number as the primary metric.

### 11.2 Newly enriched subjects per dollar

> **subject coverage yield(s) = subjects gaining at least one additional accepted observation from stage s / marginal variable cost of stage s**

This prevents a single information-rich charity generating twenty observations from obscuring persistent sparsity across the rest of the corpus.

### 11.3 Recoverable recall

Within the acquired source universe:

> **recoverable recall = accepted production propositions / accepted H1 propositions available from the same sources**

Report separately for P1, P2 and P3.

This is the core measure of the extraction-economic gap.

### 11.4 Oracle gap

> **oracle gap = accepted H1 propositions recovered by O but missed by P2/P3**

This estimates how much incremental coverage a much stronger full-context model might buy.

### 11.5 Source-scope gap

On H2-audited cases:

> **source-scope gap = accepted propositions found only outside the acquired production source bundle / all accepted propositions found in the broader audit**

Report by domain.

### 11.6 Irreducible public-evidence sparsity

On H2-audited cases:

> **public-evidence sparsity = evaluated domain opportunities where no publishable evidence was found after reasonable broader search**

This is not a performance defect.

### 11.7 Precision / false-positive rate

Cost efficiency is subordinate to correctness.

For every semantic stage report:

- accepted without edit;
- accepted after edit;
- rejected unsupported;
- wrong subject/scope;
- wrong time/status;
- prohibited inference;
- non-publishable despite plausible interpretation.

A cheap model with high observation yield but weak precision is not production-efficient because it creates review burden and contaminates public data.

### 11.8 Human review burden

Where production still requires human review, report:

- review cases per 1,000 subjects;
- median review time;
- accepted observations per reviewer hour;
- review burden generated by each model route.

A model that costs fewer API dollars but doubles human review effort may be economically worse.

---

## 12. Cost accounting

The benchmark should distinguish **marginal run cost** from **engineering investment**.

### 12.1 Marginal variable cost

Track at least:

- LLM input tokens;
- cached input tokens where priced differently;
- output tokens;
- model/provider;
- OCR/vision/API charges where applicable;
- paid search/source-access cost where applicable;
- human review minutes for routes requiring production review;
- run count and retries.

Local Python/CPU work may be economically negligible at current scale but should still record runtime/latency so an apparently “free” deterministic stage does not become operationally pathological at national scale.

### 12.2 Engineering cost

Track separately when evaluating architecture choices:

- development effort;
- maintenance burden;
- source-specific brittleness;
- dependency/infrastructure cost;
- expected reuse across domains and jurisdictions.

A bespoke parser that saves $0.0002 per charity but costs weeks to maintain may be a poor investment even if its marginal run cost is tiny.

Do not mix one-off engineering cost into the per-run benchmark without making the amortisation assumption explicit.

### 12.3 Cost normalisation

Report projected costs at useful scales:

- per subject;
- per 1,000 subjects;
- per 10,000 subjects;
- full Australian registered-charity corpus where feasible.

Separate:

- first-build cost;
- refresh cost;
- changed-source-only refresh cost.

The refresh economics may be substantially better than first-build economics because unchanged evidence and valid derivatives can be reused.

---

## 13. Economic frontier and stopping rule

For each domain, plot or report the progression:

> P0 → P1 → P2 → P3 → O/H1 ceiling

against:

- cumulative cost;
- recoverable recall;
- subject coverage;
- precision;
- review burden.

The desired production point is not necessarily maximum recall.

CharityGraph should stop adding model spend when the next stage produces poor marginal value relative to alternatives.

A generic stopping rule is:

> **Do not escalate when benchmarked expected incremental accepted information per dollar is below the current alternative use of enrichment budget, unless a specific product-critical capability requires the escalation.**

Thresholds should be learned empirically. Do not hard-code a universal “$X per observation” before the benchmark establishes the distribution of value and cost.

The planner should support domain-specific stopping points.

For example, CharityGraph may rationally reach:

- near-complete deterministic financial extraction;
- high but not perfect activity/beneficiary recall;
- selective campaign/participation coverage;
- intentionally sparse Ethos due to evidence requirements;
- intrinsically sparse Notability for small/local charities.

Equal percentage coverage across domains is not the goal.

---

## 14. Domain-specific hypotheses to test

The benchmark should test rather than assume the following priors.

### 14.1 Identity and structured finance

Expected dominant constraint:

- deterministic engineering and source completeness, not model intelligence.

High-spec model escalation should add little once parsing/identity rules are mature.

### 14.2 Activities and beneficiaries

Expected dominant constraint:

- evidence retrieval and semantic normalisation.

Likely production route:

- deterministic web/report retrieval + low-cost model.

Potentially high observations-per-dollar.

### 14.3 Programs

Expected constraint:

- source availability, program/organisation boundary and program identity.

Low-cost model may perform well on clean program pages, while complex organisations require more scope handling.

### 14.4 Participation and opportunities

Expected dominant constraint:

- transient and fragmented sources rather than model capability.

The benchmark should test whether broader acquisition (events/social/ticketing) moves coverage more than stronger models.

### 14.5 Fundraising practices and campaigns

Expected constraint:

- mixed source availability plus semantic/time distinctions in annual reports and websites.

This may be a domain where targeted semantic interpretation adds substantial value over local extraction, especially for historical/discontinued practices and campaign mechanics.

### 14.6 Fundraising expenditure

Expected dominant constraint:

- public disclosure and additivity, not LLM capability.

Stronger models must not be used to manufacture a scalar where no defensible source basis exists.

### 14.7 Ethos

Expected constraints:

- genuine non-disclosure;
- historical/formal/self/external distinctions;
- high publication threshold because prohibited proxy inference is unacceptable.

A stronger model may improve interpretation of rich evidence, but blank Ethos should often remain blank.

### 14.8 Notability

Expected constraints:

- genuine sparsity for small/local charities;
- source discovery and subject scope for salient organisations;
- Wikipedia/citation graph may contribute more than expensive free-form model inference.

If high-spec same-source extraction adds little once Wikimedia discovery is good, production should not spend heavily here.

---

## 15. Source acquisition versus model spend

The benchmark should explicitly compare the marginal value of three classes of investment:

1. **better deterministic extraction** from sources already held;
2. **stronger semantic interpretation** of evidence already held;
3. **broader source acquisition**.

For each domain, ask:

> If CharityGraph had another $100 of enrichment budget, would it gain more accepted information by improving Python extraction, buying stronger-model calls, or acquiring another source family?

This turns source strategy into an economic decision rather than a completeness instinct.

Examples:

- if participation H2 audits find large numbers of valid opportunities on third-party event platforms, source expansion may dominate model escalation;
- if fundraising facts are routinely present in acquired annual reports but missed by P2, semantic extraction deserves investment;
- if Ethos remains absent even under H2, further extraction spend is wasteful;
- if Notability is captured almost entirely by Wikipedia + underlying citations, custom web-wide discovery may have weak marginal value.

---

## 16. Relevance and fairness in compute allocation

CharityGraph is allowed to optimise compute without ranking charities.

The planner should not equate:

- large charity = important;
- small charity = not worth processing;
- Wikipedia presence = worthy;
- high donation income = deserving of better data.

Every in-scope charity receives the cheap common baseline.

Additional spend is justified by **evidence opportunity and unresolved capability value**, not worthiness.

Size may be a predictive feature for source richness and expected yield, but it should not be the normative allocation rule.

This matters to CharityGraph's mission: small “right-tail” charities should remain discoverable and interpretable where evidence exists, rather than being excluded because they cannot justify enterprise-scale inference spend.

---

## 17. Benchmark run design

A benchmark run should be reproducible and versioned.

Record:

- benchmark ID/version;
- cohort definition and strata;
- selected CharityGraph/Data release SHA;
- Builder SHA;
- source acquisition snapshot/version;
- source families made available to each condition;
- parser/extraction versions;
- retrieval policy version;
- prompt/policy versions;
- model IDs/versions;
- model parameters;
- exact token/cost telemetry;
- human reviewer protocol;
- proposition-ledger version;
- adjudication date;
- exclusions/failures.

Private raw prompts/source text may remain local/private under existing CharityGraph policy. Public or committed benchmark documentation should preserve enough lineage to explain results without publishing third-party source corpora.

---

## 18. Required benchmark outputs

Each benchmark should generate a compact decision package.

### 18.1 Executive report

Markdown summary containing:

- cohort and source coverage;
- pipeline conditions compared;
- total and per-1,000 projected cost;
- precision by domain;
- recoverable recall by domain;
- subject coverage by domain;
- incremental observations and subjects per dollar;
- oracle gap;
- source-scope gap from H2 subset;
- dominant failure classes;
- recommended routing/escalation changes;
- stopping decisions;
- open product questions.

### 18.2 Machine-readable stage metrics

CSV/JSON/Parquet as appropriate:

- subject/stratum;
- domain;
- pipeline condition;
- candidate counts;
- accepted proposition counts;
- miss/false-positive categories;
- token/cost data;
- review burden;
- source-opportunity features.

### 18.3 Proposition ledger

Private/governed adjudication artefact containing the reference proposition set and evidence links.

### 18.4 Routing recommendation

A small, explicit production policy proposal, for example:

- deterministic only;
- cheap bundled model;
- cheap domain-specific model;
- selective expensive escalation;
- human review required;
- stop/unavailable.

The benchmark itself should not silently rewrite production routing.

---

## 19. Planning from benchmark results

The benchmark should directly drive product and implementation decisions.

### 19.1 Scale forecast

Use stratum-weighted benchmark results to estimate:

- expected first-build cost per 1,000 charities;
- expected refresh cost;
- expected coverage by domain;
- expected proportion routed to each model tier;
- human-review burden;
- expected number of genuinely sparse subjects.

Forecasts should include ranges, because the benchmark cohort is deliberately stratified rather than a perfect census sample.

### 19.2 Pipeline investment choices

For each proposed improvement, estimate:

- domain(s) affected;
- subjects affected;
- current miss class;
- expected accepted observations recovered;
- engineering cost;
- marginal run cost change;
- maintenance complexity;
- whether a cheaper alternative exists.

Prioritise changes with high reusable yield, especially those that improve multiple domains.

Examples of high-leverage shared improvements may include:

- better bounded page discovery;
- non-exclusive domain candidate extraction;
- reusable document passage retrieval;
- improved subject/scope handling;
- assessment-scope metadata;
- derivative reuse/change detection.

### 19.3 Source-family investment choices

A new source family should be justified by demonstrated H2 yield rather than speculative completeness.

Before adding a source family nationally, estimate:

- unique accepted propositions it contributes;
- domains improved;
- overlap with existing sources;
- acquisition/legal/licensing burden;
- freshness requirements;
- identity-resolution complexity;
- marginal cost per subject;
- likely long-term maintenance.

---

## 20. Refresh economics

The benchmark should eventually test first-build and refresh separately.

A production refresh should avoid paying again for unchanged understanding.

Where source hashes, source records and derivative lineage are unchanged:

- reuse deterministic extractions;
- reuse valid semantic derivatives where policy allows;
- avoid repeat LLM calls;
- reassess only affected domains when evidence changes.

Different source types have different expected refresh cadence:

- regulator/AIS: annual/event-driven;
- annual reports: annual;
- stable About/Governance/Giving pages: periodic/change-detected;
- opportunities/events/campaigns: transient/high-frequency where supported;
- Wikipedia: revision/change-detected;
- embeddings/summaries: regenerate only when relevant input changes.

The economic planner should therefore optimise **change-triggered enrichment**, not just initial build cost.

---

## 21. Anti-gaming and interpretation guardrails

The economics benchmark can create bad incentives if measured carelessly.

Do not optimise for:

- maximum raw candidate count;
- maximum non-null fields;
- maximum observations per charity;
- lowest API cost regardless of precision;
- apparent coverage produced by over-general source mappings;
- expensive-model recall at the cost of unreviewable false positives;
- withholding processing from small charities solely because yield is lower.

Specific protections:

1. Count human-adjudicated useful propositions, not model verbosity.
2. Report precision alongside recall and cost.
3. Report subject coverage alongside observation count.
4. Stratify by charity size/source richness/domain.
5. Keep `present_but_non_publishable` separate from model failure.
6. Keep `no_public_evidence_found` separate from `not_evaluated`.
7. Preserve public coverage semantics; benchmark classifications are internal diagnostic labels.
8. Do not let cost optimisation relax identity, sensitive-attribute or fundraising-economics guardrails.

---

## 22. Decision examples

The benchmark should make decisions of this form possible.

### Example A — cheap pipeline is good enough

Observed result:

- P2 recovers 93% of H1 activity/beneficiary propositions;
- P3 adds 2 percentage points at 8× marginal model cost;
- oracle adds only another 1 percentage point;
- precision is already high.

Decision:

- stop at P2 for those domains;
- spend the budget elsewhere.

### Example B — source scope dominates

Observed result:

- P2 and O both find little participation evidence from acquired sources;
- H2 finds many valid current opportunities on external event platforms.

Decision:

- do not buy a stronger model;
- investigate a bounded new participation source family.

### Example C — targeted semantic escalation pays

Observed result:

- fundraising practices are frequently present in acquired annual reports;
- P1 misses most semantic distinctions;
- P2 recovers 70%;
- P3 recovers 91% on only 20% of evidence-rich cases;
- cost remains acceptable.

Decision:

- retain selective P3 escalation for fundraising-rich cases.

### Example D — sparsity is real

Observed result:

- small/local charities have no Ethos evidence in acquired sources;
- oracle finds nothing more;
- H2 broader search also finds no defensible evidence.

Decision:

- accept sparse Ethos coverage;
- do not build inference heuristics from names, beneficiaries or geography.

---

## 23. Initial benchmark hypotheses and success criteria

The first benchmark should not be judged by whether one preselected architecture wins.

It succeeds if CharityGraph can answer, with evidence:

1. How much useful enrichment is present in the current acquired source bundle?
2. What share can deterministic extraction recover?
3. What incremental share does the low-cost LLM recover?
4. What incremental share does selective strong-model escalation recover?
5. How far is the affordable pipeline from the same-source human ceiling?
6. Which domains are mainly source-limited rather than extraction-limited?
7. Which domains are genuinely sparse in the public record?
8. What is the expected first-build and refresh cost per 1,000 charities?
9. Which pipeline/source investments offer the highest marginal information yield?
10. Where should CharityGraph deliberately stop spending?

A useful outcome may show that some domains should remain sparse. The goal is not to prove that every field can be filled economically.

---

## 24. Implementation sequence

### Phase 1 — benchmark specification

In CharityGraph Data:

- approve this design;
- define the benchmark proposition domains;
- define cohort stratification;
- define cost telemetry requirements;
- define adjudication protocol;
- define benchmark-only outcome labels.

No production schema change required.

### Phase 2 — Builder benchmark harness

Implement a private/local benchmark runner that can:

- construct the source-opportunity inventory;
- run P0/P1/P2/P3 under explicit configurations;
- collect model/cost telemetry;
- preserve candidates and lineage;
- export a review packet;
- compare against the proposition ledger;
- aggregate domain/stratum economics.

Do not make benchmark outputs part of public releases.

### Phase 3 — same-source oracle

Run O on the benchmark cohort or an economically selected subset.

The oracle prompt should receive:

- full acquired evidence bundle relevant to the benchmark;
- current CharityGraph schema/construct definitions;
- taxonomy definitions;
- editorial/inference prohibitions;
- explicit requirement to cite evidence and scope/time.

Record cost even though O is not proposed for routine production.

### Phase 4 — human adjudication

Adjudicate:

- P2/P3/O disagreements;
- random accepted outputs for false-positive estimation;
- a sample where all systems found nothing.

Build H1 proposition ledger.

### Phase 5 — broader-source audit

Run H2 on a smaller stratified subset, especially apparent sparse cases.

Estimate source-scope versus true public-evidence sparsity.

### Phase 6 — economic routing proposal

From benchmark results, propose:

- default routes by domain/source richness;
- escalation triggers;
- stop conditions;
- source-family experiments;
- projected cost/coverage at 1,000 and national scale.

Do not hard-code the routing policy until this review is accepted.

### Phase 7 — production trial

Apply the approved planner to a larger non-public or candidate corpus before allowing it to produce a new public semantic release.

---

## 25. Likely repository artifacts

A future implementation may introduce private/local benchmark outputs and a small number of committed specifications.

Possible committed Data artifacts:

- `ENRICHMENT_ECONOMICS_DESIGN.md` — this document;
- benchmark cohort specification without private source content;
- benchmark outcome enum/specification;
- evaluation protocol;
- approved routing policy after review;
- updates to `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md` after product approval.

Possible Builder artifacts:

- benchmark runner;
- source-opportunity inventory generator;
- model-cost telemetry wrapper;
- condition configs for P0/P1/P2/P3/O;
- adjudication packet generator;
- metric aggregation/reporting;
- tests/fixtures.

Private/local only:

- raw source bundles;
- full oracle prompts/responses where they contain copied source text;
- reviewer working packets;
- token/cost logs containing private source references if applicable;
- proposition ledger if it contains copyrighted excerpts or sensitive review notes.

---

## 26. Acceptance criteria for the first benchmark

The benchmark is complete only when:

- the cohort is stratified by both organisation size and source richness;
- P0, P1 and P2 are reproducibly runnable;
- P3 is implemented as selective escalation rather than all-case escalation;
- O uses the same acquired source universe as production;
- H1 adjudicates disagreements and a sample of mutual misses;
- H2 audits a stratified subset for broader-source evidence;
- every model condition has measured token/API cost;
- human review burden is measured where relevant;
- accepted propositions are normalised through a proposition ledger rather than raw output count;
- results are reported by enrichment domain and corpus stratum;
- recoverable recall, precision, subject coverage and marginal yield are all reported;
- source-scope gap is distinguished from extraction-economic gap;
- genuine public-evidence sparsity is explicitly estimated;
- the report forecasts cost and coverage per 1,000 charities;
- the report makes at least one concrete stop/invest/escalate/source-acquisition recommendation;
- no benchmark condition mutates the current immutable public release;
- no benchmark output is silently promoted to public CharityGraph truth.

---

## 27. Open questions for empirical resolution

The benchmark should resolve rather than speculate about:

1. Whether one bundled low-cost semantic call over a small charity's entire substantive evidence is cheaper/better than separate domain calls.
2. Which model tier gives the best production precision/cost trade-off by domain.
3. Whether high-spec escalation is useful enough to retain at all outside complex identity/scope cases.
4. How much three-year annual-report history adds beyond the latest report for each enrichment domain.
5. Whether Wikipedia context meaningfully reduces Notability discovery cost.
6. Whether participation requires new source families more than better extraction.
7. Whether Ethos is mostly evidence-limited or interpretation-limited.
8. Whether fundraising practices are more economically recoverable from annual reports or websites.
9. How much source-opportunity features can predict expected enrichment yield before LLM spend.
10. What change-detection strategy produces the best refresh economics.
11. Whether human review can be removed for any enrichment domain after sufficient benchmark precision is demonstrated.
12. What level of production sparsity users tolerate when CharityGraph clearly exposes evidence/coverage state.

---

## 28. Product principle proposed for later canonicalisation

> **CharityGraph optimises enrichment for useful, defensible public knowledge per unit cost, not for field completeness. Every subject receives a cheap common evidence baseline; additional processing is allocated according to available evidence and expected information yield. Sparse output is correct when the public record is sparse or a claim cannot be responsibly made.**

A complementary operational principle is:

> **Use expensive models to measure and selectively close the extraction-economic gap, not to conceal source absence.**

---

## 29. Summary

CharityGraph should treat enrichment architecture as an empirical economic frontier.

The production system is not trying to imitate the infinite-money mega-prompt exactly. It is trying to approach the **recoverable public-knowledge ceiling** at a small fraction of the marginal cost while retaining CharityGraph's stronger provenance and coverage semantics.

The benchmark therefore separates:

> **what is not public**  
> **what is public but outside current source scope**  
> **what is already acquired but too expensive/difficult for the cheap pipeline**  
> **what is understood but should not be published**  
> **what the economical production pipeline successfully recovers**

Once those components are measured, CharityGraph can make rational decisions about whether the next dollar belongs in Python extraction, better retrieval, a low-cost LLM, selective high-spec reasoning, human review, or a new source family — and can deliberately stop where the remaining sparsity is real rather than technical.
