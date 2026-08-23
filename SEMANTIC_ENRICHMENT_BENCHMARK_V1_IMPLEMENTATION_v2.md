# Semantic Enrichment Benchmark v1 — Implementation Contract

**Status:** Approved implementation contract for the next review-only Builder phase  
**Design basis:** CharityGraph Data commit `14f7e53be7db558495f5afe7ab8c707cb37d7134`  
**Builder baseline:** `1e532ad1fbb5f5d1c89dfea1290b183673006c4d`  
**Completed prerequisites:** fundraising safety reconciliation `f21efbb2ccf6867a5ec6cdc4eb5d76c0cbf81cd9`; Knowledge Validation 22-case governed gate `1e532ad1fbb5f5d1c89dfea1290b183673006c4d`  
**Publication status:** Private/review-only. No new public release, public schema, corpus rebuild, or Viewer change is authorised.

---

## 1. Purpose

Implement a bounded, economically instrumented **Semantic Enrichment Benchmark v1** that tests how much useful enrichment CharityGraph can recover, at what cost, and why remaining gaps exist.

The benchmark must distinguish at least:

1. genuinely absent public evidence;
2. public evidence outside the acquired/authorised source scope;
3. evidence acquired but missed by deterministic/local extraction;
4. evidence acquired but missed by the economical LLM route and recoverable by a stronger same-source oracle;
5. evidence found but blocked from publication by identity, scope, ambiguity, sensitivity, provenance, or policy;
6. evidence not yet processed.

The benchmark is not a public-data build. It is an evaluation harness that produces private candidates, review material, cost/coverage diagnostics, and later human/economic decisions.

The central economic question is:

> **What is the marginal accepted enrichment coverage gained per dollar, and which next intervention — better local extraction, a cheap model, selective model escalation, or a new source family — buys the most useful coverage?**

---

## 2. Governing product decisions

Do not reopen these decisions during implementation.

### 2.1 Product boundary

CharityGraph supplies evidence-backed charity/program facts and classifications. It does not:

- adjudicate a donor's personal mandate;
- output match percentages;
- rank recipients;
- recommend donations;
- estimate fundraising ROI;
- estimate donor lifetime value;
- score reputation, prestige, or worthiness.

### 2.2 Observation architecture

Use the existing CharityGraph typed-observation model and v0.5 common semantics.

The next private candidate layer may extend the common envelope with scoped context, qualification, source role, review fields, and assessment scope. Do **not** build:

- a universal claim graph;
- an EAV datastore;
- a generic key/value public observation system.

### 2.3 Scope

Semantic observations may be scoped to:

- `organisation`
- `program`
- `service`
- `organisational_unit`

Programs/services/units may use governed subject-local identifiers. They do not become durable CharityGraph subjects merely because observations exist about them.

No parent/network attribute transfer is permitted.

### 2.4 Cause centrality

Where needed, use:

- `primary`
- `material`
- `incidental`
- `unknown`

Centrality is distinct from taxonomy-term adjacency.

### 2.5 Ethos and service orientation

Treat:

- organisational Ethos; and
- `service_or_mission_orientation`

as separate semantic domains.

Beneficiary/community identity must not be used to infer Ethos.

All Ethos and service-orientation pilot candidates require human review.

### 2.6 Notable context

Use public/product terminology `notable_context`, never a score.

For the pilot, all notable-context candidates remain review-only.

### 2.7 Fundraising model

Keep these domains distinct:

- funding source;
- standing fundraising practice;
- fundraising campaign;
- fundraising expenditure;
- private pilot fundraising-provider relationship.

No peer-imputation or universal-prior path is permitted for fundraising expenditure.

### 2.8 Coverage / absence

`not_found_in_source` means only that no qualifying observation was found in the processed scope.

It never means the fact does not exist.

The benchmark should support compact `assessment_scope` semantics privately now, designed for later compact public coverage metadata.

---

## 3. Completed prerequisites

### 3.1 Fundraising safety reconciliation — complete

Builder commit `f21efbb2ccf6867a5ec6cdc4eb5d76c0cbf81cd9`:

- removed the production universal fallback-prior route;
- made unavailable/null fundraising expenditure valid with explicit coverage;
- prohibited peer-imputation fill for fundraising expenditure;
- preserved v0.5 definite/possible/excluded attribution bounds;
- added regressions against fallback, peer fill, forced midpoint and forced point estimates.

This prerequisite is closed. Do not reopen it in the benchmark implementation.

### 3.2 Knowledge Validation v1 minimum human gate — complete

Builder commit `1e532ad1fbb5f5d1c89dfea1290b183673006c4d` records 22 approved human-governed decisions from the deliberately difficult 48-case packet:

- `ACCEPT`: 8
- `EDIT`: 4
- `REJECT`: 4
- `WRONG_DOMAIN`: 5
- `IDENTITY_BLOCKED`: 1

By domain:

- activities: 4 reviewed — HUMAN REVIEW;
- beneficiaries: 6 reviewed — HUMAN REVIEW;
- geography: 5 reviewed — HUMAN REVIEW;
- programs: 2 reviewed — HUMAN REVIEW;
- participation: 5 reviewed — HUMAN REVIEW;
- opportunities, self-description, fundraising and identity-sensitive: NOT READY.

No domain is auto-promotable.

The remaining 26 stratified cases are **deferred rather than required before this phase**. The purpose of the minimum gate was to determine whether the existing deterministic semantic candidate machinery was safe for automatic promotion and to expose boundary failures. It has done so. Reviewing another 26 cases against the same soon-to-change extractor would have low marginal design value. Review them later only if needed for a specific precision estimate, regression, or disputed routing decision.

### 3.3 What the gate established

Treat these as implementation evidence, not universal precision estimates:

- explicit named-program detection is promising (2/2 difficult program cases accepted), but the sample is too small to authorise automation;
- participation language such as explicit volunteering or donating is often useful, but participation existence must remain separate from verified action URLs;
- activities require filtering of rhetoric, acknowledgements and other non-activity prose;
- beneficiary extraction must distinguish beneficiaries from audiences, participants, supporters and generic aspirational “communities”;
- geography must distinguish service/activity/program geography from contact/admin address, venue context and irrelevant location language;
- identity can block an otherwise semantically valid observation.

Therefore **P1 deterministic semantic extraction is a candidate-generation stage only in Benchmark v1**. It must not directly promote these semantic observations to public cards.

### 3.4 Review-model correction for Benchmark v1

Knowledge Validation v1 used a single outcome enum that mixed semantic judgement with publication/use blockers. The approved Red Cross case demonstrated the loss of information: the evidence was semantically usable with editing, while identity remained unresolved.

Do not rewrite the historical Knowledge Validation decisions. For Semantic Enrichment Benchmark v1, separate:

```json
{
  "semantic_outcome": "ACCEPT | EDIT | REJECT | WRONG_DOMAIN | INSUFFICIENT",
  "blockers": [
    "IDENTITY_BLOCKED",
    "ADDITIVITY_BLOCKED",
    "TIME_SCOPE_UNCLEAR",
    "SCOPE_AMBIGUOUS",
    "SENSITIVE_REVIEW_REQUIRED"
  ]
}
```

Rules:

- `semantic_outcome` answers whether the evidence supports the proposed domain/proposition and whether editing is needed;
- `blockers[]` answers whether an otherwise useful candidate cannot yet be used/published;
- blockers are orthogonal and may coexist with `ACCEPT` or `EDIT`;
- a rejected/wrong-domain candidate normally needs no blocker;
- the governed human decision retains rationale, optional editor note and `decision_authority = human_governed`;
- model output may propose review requirements but cannot create human-governed outcomes.

### 3.5 Automation-policy wording

Fix the current Builder wording defect during benchmark scaffold work:

- if `reviewed == 0`, the reason may say no human-adjudicated evidence exists;
- if `reviewed > 0` but the domain remains `HUMAN REVIEW`, the reason must acknowledge the available human evidence and state why it is insufficient to authorise automation.

The policy result is currently correct; only its explanation is wrong.

---

# 5. Benchmark cohort

Use approximately **40 deliberately selected charity subjects**.

This is an adversarial product/economics cohort, not a representative national sample.

Selection should cover cross-products of:

- charity size: large / medium / small / very small;
- source richness: rich / moderate / thin / failed;
- annual report: rich digital / scanned / thin / unavailable;
- website: rich / sparse / transient-heavy / unavailable;
- organisational complexity: simple / multi-program / network/affiliate / identity ambiguity;
- fundraising intensity: rich / moderate / sparse;
- fundraising-industry-source intersection: present / absent;
- Ethos: explicit / formal affiliation / externally described / absent;
- Wikimedia: strong / weak / absent;
- participation: current / historical / sparse;
- program visibility: explicit / ambiguous / none;
- notable context: present / absent / adverse-sensitive test case.

Reuse existing Golden Corpus and Knowledge Validation subjects where useful.

The cohort manifest must record selection strata and rationale privately.

Do not make cohort membership a public salience or importance label.

---

# 6. Semantic domains in benchmark v1

The benchmark should support private candidates for:

1. activities — control domain;
2. beneficiaries — control domain;
3. programs/services;
4. cause/intervention classification plus optional centrality;
5. role-specific geography where explicitly evidenced;
6. participation;
7. fundraising practices;
8. fundraising campaigns;
9. fundraising-provider relationships;
10. Ethos;
11. service/mission orientation;
12. notable context.

Do not require equal candidate volume per domain.

A genuinely sparse domain is a valid benchmark result.

---

# 7. Private candidate model

Implement a private/review candidate envelope compatible with the existing observation semantics.

Conceptual minimum:

```json
{
  "candidate_id": "seb1-...",
  "subject_id": "cb_...",
  "domain": "fundraising_campaign",

  "scope": {
    "scope_type": "organisation",
    "scope_id": null,
    "scope_label": null
  },

  "candidate_payload": {},

  "claim_basis_proposed": "direct",
  "extraction_method": "document_text",

  "source_family": "annual_report",
  "source_role": "organisation_self_report",
  "source_record_ids": ["src:..."],
  "evidence_ids": ["ev:..."],

  "source_url": "...",
  "source_location": "...",
  "source_text": "...",
  "source_content_hash": "...",

  "time": {},
  "qualification": null,
  "confidence_proposed": null,
  "warnings": [],

  "review_status": "review_required",
  "alternative_interpretation": null,

  "pipeline_stage": "P1"
}
```

Exact class/module names are implementation freedom.

Requirements:

- candidate IDs deterministic from governed inputs;
- exact evidence excerpt/location retained;
- source hash retained;
- candidate is never a public observation merely because it validates;
- model output cannot set `decision_authority = human_governed`;
- candidate domain extraction is non-exclusive: one evidence passage may support several candidate domains.

---

# 8. Source role model

Do not flatten all public evidence into generic "independent source".

Support source/evidence role metadata sufficient to distinguish at least:

- regulator / authoritative structured source;
- organisation self-report;
- formal governance/constitution;
- independent secondary source;
- Wikipedia/Wikimedia discovery/support;
- fundraising industry self-regulatory association;
- fundraising industry award record;
- fundraising industry benchmark;
- fundraising provider self-report;
- fundraising platform self-report;
- listed provider disclosure;
- Gifts-in-Wills platform/directory;
- fundraising trade publication;
- industry taxonomy/reference source.

Source role is not a universal quality score.

A source may be strong for one proposition and weak for another.

---

# 9. Evidence acquisition ladder

Instrument the benchmark by processing stage.

## P0 — structured baseline

Existing structured/regulator information and already governed observations.

No new LLM use.

## P1 — deterministic/local extraction

Includes:

- existing document extraction;
- deterministic website parsing;
- bounded page-role discovery/acquisition;
- source-led industry enumeration;
- deterministic table/list extraction;
- keyword/high-recall passage retrieval;
- local OCR/vision routes already approved;
- deterministic identity candidate generation.

P1 should maximise cheap evidence opportunity before model interpretation.

## P2 — low-cost semantic interpretation

Pass only selected bounded evidence slices to the economical model route.

P2 should:

- validate structured output;
- identify only supported propositions;
- preserve source wording;
- return `unknown`/no candidate rather than fill gaps;
- not resolve identity by itself;
- not create human-gold labels;
- log model/version/prompt/input hash/token/cost telemetry privately.

## P3 — selective higher-spec escalation

P3 is not a default corpus step.

It is authorised only when a deterministic routing rule identifies a likely high-value ambiguity or missed-evidence class.

The first benchmark may test P3 experimentally. Do not hard-code a production escalation rule before economic review.

## O — same-source high-spec oracle

The oracle receives the **same acquired evidence universe** as P1/P2/P3.

Its role is to estimate the recoverable-information ceiling under expensive interpretation.

The oracle must not browse broader sources in this stage.

Use O selectively, with highest priority for:

- program/scope resolution;
- fundraising practices/campaigns;
- Ethos/service orientation;
- selected notable-context cases.

Use only calibration samples for easy activities/beneficiaries.

Do not spend oracle calls on straightforward structured regulator facts.

## H1 — human adjudication

Human review establishes the governed reference for benchmark cases.

Models do not create human gold.

## H2 — broader-source audit

Manual benchmark-only research outside the acquired production source universe.

Purpose:

> Determine whether missing facts are absent from the public record or merely outside current CharityGraph source scope.

H2 may inspect additional public sources manually.

H2 does **not** authorise production crawling of a new source family.

Exception: fundraising-industry sources explicitly approved in the 2026-08-22 source-family design may be tested as a governed experimental acquisition arm.

---

# 10. Fundraising-industry source arm

Implement fundraising-industry sources as a distinct experimental arm.

Preferred architecture:

```text
source-led index/table/directory
    -> deterministic source-record extraction
    -> external charity/campaign/provider candidate
    -> conservative CharityGraph identity resolution
    -> optional targeted detail acquisition
    -> deterministic + low-cost semantic extraction
    -> private typed candidates
    -> human/economic review
```

Start with **2–3 high-density sources**, not all candidate sources.

Recommended first choices:

1. PFRA current charity/agency material — standing face-to-face practice + provider relationships;
2. Donor Republic/Funraisin P2P benchmark — named campaigns + source-defined activity + reported amount;
3. FIA awards — campaign/type/provider relationship.

If one source proves technically unsuitable, substitute another high-density source from the approved design rather than broadening scope arbitrarily.

Do not begin with many narrative agency case-study sites.

The benchmark should first test whether deterministic/semi-structured source-led enumeration yields the expected economic advantage.

---

# 11. Fundraising-industry claim rules

Permitted review candidates include:

- standing fundraising practice;
- campaign name/type/year;
- channel/mechanic;
- explicit provider relationship;
- explicit start/end/discontinuation;
- explicit campaign target;
- explicit dollars raised;
- explicit dollars spent;
- explicit participant/donor/fundraiser counts;
- source-native award/category/taxonomy term.

Preserve source metric wording exactly enough to distinguish:

- raised;
- pledged;
- ticket sales;
- gross proceeds;
- media spend;
- campaign spend;
- platform-processed amount.

Do not turn industry/vendor claims into canonical:

- ROI;
- ROAS;
- CPA;
- conversion;
- retention;
- uplift;
- LTV;
- provider quality;
- campaign profitability.

These may remain source-native evidence for research/audit only.

Do not calculate ROI from spend/raised merely because both values exist.

---

# 12. Website pipeline changes

Use bounded page-role discovery, but make semantic candidate extraction non-exclusive.

Candidate fundraising roles should include, where present:

- giving;
- fundraise;
- bequests/major giving;
- campaign/event;
- corporate support.

The integrated benchmark should actually process selected discovered pages, not merely record their URLs.

Requirements:

- same-origin bounded acquisition by default;
- at most one selected page per governed role unless an explicit fixture requires otherwise;
- explicit retrieval failure;
- stable/transient class retained;
- content hash retained;
- no action URL inferred from an evidence URL;
- third-party campaign platforms are not recursively crawled unless the experimental source policy explicitly includes that provider.

---

# 13. Document pipeline changes

Do not replace the approved document extraction stack.

Add a semantic-retrieval layer over extracted document text.

For each semantic domain:

1. deterministic/high-recall retrieval narrows passages;
2. bounded P2 semantic extraction interprets selected passages;
3. candidate preserves exact page/section/hash context;
4. human review decides.

Fundraising retrieval should include the vocabulary in `FUNDRAISING_KNOWLEDGE_DESIGN.md`.

Ethos/notable-context retrieval should use their approved design concepts but must not infer sensitive attributes from weak proxies.

---

# 14. Wikimedia arm

Implement only the approved narrow policy.

Candidate discovery/binding:

- no name-only identity resolution;
- preserve article/QID/revision;
- preserve section/location and citation path where available;
- record `wikimedia_role = discovery | support`.

Lower-risk stable context may retain revision-pinned Wikipedia secondary support in review candidates.

Sensitive/adverse claims require underlying adequate evidence before eventual public publication.

The benchmark itself remains review-only.

---

# 15. Assessment scope

Every domain evaluation should be able to report what was actually processed.

Private conceptual structure:

```json
{
  "source_families": ["organisation_website", "annual_report"],
  "source_roles": ["giving", "bequests_major_giving"],
  "reporting_periods": ["2025"],
  "policy_version": "semantic-enrichment-benchmark-v1"
}
```

This should feed benchmark coverage diagnostics.

Do not expose full operational telemetry publicly.

---

# 16. Gap classification

For each expected/reviewed proposition or domain-subject opportunity, support a benchmark disposition drawn from a controlled set equivalent to:

- `observed_economically`
- `recoverable_but_missed`
- `outside_acquired_scope`
- `not_publicly_evidenced`
- `present_but_nonpublishable`
- `not_yet_processed`
- `identity_blocked`
- `retrieval_failed`

The implementation may separate these into more than one field if cleaner.

The important invariant is that the benchmark can distinguish:

> absent evidence vs source-scope gap vs extraction/model gap vs governance block.

---

# 17. Human review

Reuse the Knowledge Validation discipline but use the corrected two-axis review model established in section 3.4.

## Semantic outcome

Human-governed semantic outcomes are:

- `ACCEPT`
- `EDIT`
- `REJECT`
- `WRONG_DOMAIN`
- `INSUFFICIENT`

## Orthogonal blockers

Supported blockers are initially:

- `IDENTITY_BLOCKED`
- `ADDITIVITY_BLOCKED`
- `TIME_SCOPE_UNCLEAR`
- `SCOPE_AMBIGUOUS`
- `SENSITIVE_REVIEW_REQUIRED`

A case may therefore be, for example:

```json
{
  "semantic_outcome": "EDIT",
  "blockers": ["IDENTITY_BLOCKED"]
}
```

This distinction is required for economic evaluation: a correct semantic extraction that cannot be used because identity is unresolved is not an extraction failure.

Every `EDIT`, `REJECT`, `WRONG_DOMAIN` or `INSUFFICIENT` decision requires a rationale. Every blocker should have either an explicit rationale or a machine-resolvable reason code/context.

For sensitive Ethos/notable-context material, make source/scope/procedural-status review especially visible.

Models do not create human gold.

---

# 18. Cost accounting

Track cost privately at least by:

- subject;
- domain;
- source family;
- source record/page/document;
- pipeline stage P0/P1/P2/P3/O/H2;
- model/version;
- input tokens;
- output tokens;
- cached tokens if available;
- API cost;
- OCR/vision elapsed compute if measurable;
- acquisition request count;
- elapsed wall time.

Do not publish this telemetry in cards.

The economic analysis must not use only total project spend.

---

# 19. Primary economic metrics

Report by domain and source stratum.

At minimum:

### Coverage

- accepted observations;
- subjects gaining at least one accepted observation;
- subjects with no publishable evidence;
- source-scope gap rate;
- extraction-economic gap rate;
- governance-block rate.

### Economics

- accepted observations per dollar;
- newly enriched subjects per dollar;
- marginal accepted observations per additional stage;
- marginal newly enriched subjects per additional stage;
- marginal recall against the same-source oracle;
- cost per accepted observation;
- cost per newly enriched subject.

### Quality

- precision;
- edit rate;
- reject rate;
- wrong-domain rate;
- identity/scope defect rate;
- provenance defect rate;
- time/status defect rate;
- review minutes per accepted observation where measured.

### Source-family value

For each source family:

- records/candidates per acquisition;
- accepted observations;
- identity binding precision;
- marginal subjects enriched;
- freshness gain;
- LLM requirement rate;
- human review burden;
- monetary cost;
- rights/maintenance notes.

Never hide domain failure inside a global aggregate.

---

# 20. Routing analysis

The benchmark should produce **recommendations**, not automatically change production routing.

For each domain, report candidate routing options such as:

- P1 sufficient;
- P1 + P2 worthwhile;
- selective P3 worthwhile;
- source-family expansion beats model escalation;
- evidence is genuinely sparse; stop;
- human-only/high-risk.

Do not set universal numeric thresholds in code as product policy.

After benchmark results, ChatGPT/user will approve domain-specific routing rules.

---

# 21. Source opportunity inventory

Produce a per-subject private inventory before expensive interpretation.

Conceptually include:

- structured-source availability;
- website availability and selected page roles;
- annual-report availability/year/page count/text quality;
- Wikimedia candidate presence;
- fundraising-industry source hits;
- evidence volume;
- relevant-domain retrieval hits;
- identity ambiguity signals;
- prior observations requiring refresh.

This inventory is the basis for spend allocation.

Do not allocate expensive inference simply because a charity is large or prominent.

Spend should follow **evidence opportunity and expected marginal information**, not perceived worthiness.

---

# 22. Refresh/freshness considerations

The first benchmark is primarily extraction economics, but preserve enough metadata to later distinguish refresh classes.

Examples:

- PFRA current directory — current/periodic;
- annual awards list — annual/edition;
- campaign page — transient/historical;
- provider case study — historical unless currentness explicitly supported;
- annual report — reporting-period;
- Ethos constitution/formal affiliation — slow-changing;
- participation/event pages — faster-changing.

Do not infer current continuity from an old case study.

---

# 23. Required regression cases

Include tests/fixtures covering at least:

### Cross-domain

- one passage legitimately supporting multiple domains;
- program vs organisation scope;
- parent/network no-attribute-transfer;
- beneficiary not implying Ethos;
- historical observation not current;
- `not_found_in_source` not substantive negative;
- name-only identity match blocked.

### Fundraising

- Donate button only;
- bequest income without bequest-program evidence;
- Gifts-in-Wills page;
- discontinued face-to-face program;
- Giving Day with match/target/result;
- non-fundraising gala;
- sponsor logos;
- peer-to-peer challenge;
- marketing expense ambiguity;
- direct functional allocation;
- campaign “raised $X” distinct from annual accounting revenue;
- provider relationship explicit vs implied;
- vendor ROI/CPA ignored as canonical metric.

### Notable context / Wikimedia

- stable founding/history candidate;
- adverse claim requiring underlying source;
- living-person/contentious candidate held for review;
- Wikipedia absence has no meaning;
- parent controversy not transferred to affiliate.

---

# 24. Outputs

All outputs are private runtime/staging artefacts.

Produce at least:

1. `cohort.json`
   - governed cohort and strata;

2. `source-opportunity-inventory.json`
   - per-subject acquisition/evidence opportunities;

3. `candidate-inventory.jsonl`
   - all review-only semantic candidates;

4. `assessment-scope.jsonl`
   - processed source scope by subject/domain;

5. `cost-ledger.jsonl`
   - stage/domain/source/model cost telemetry;

6. `benchmark-summary.json`
   - deterministic aggregate metrics;

7. `HUMAN_REVIEW_PACKAGE.md`
   - compact stratified review packet;

8. `review-decisions.json`
   - human decisions only;

9. `economics-report.md`
   - coverage/cost frontier and routing recommendations;

10. `source-family-report.md`
    - marginal value of fundraising-industry source families;

11. `oracle-gap-report.md`
    - P1/P2/P3 vs same-source O differences;

12. `broader-source-audit.md`
    - H2 diagnostic results if/when manually performed.

Exact filenames may vary if existing conventions strongly favour another naming scheme, but the information must be present.

No output above is a public release artefact.

---

# 25. Model-call discipline

The benchmark must be runnable in bounded slices.

Requirements:

- no model call during deterministic PREPARE;
- P2/P3/O callable separately;
- cache by source/evidence hash + prompt/model/version;
- model reruns only when governing inputs/version change;
- explicit maximum subjects/cases per run;
- dry-run / cost-estimate mode where practical;
- no complete national dataset in model context;
- no full-report LLM call where deterministic passage retrieval suffices;
- no model used as sole identity resolver.

Use the lowest-cost model that meets the benchmark route under evaluation.

The same-source oracle is intentionally expensive but sample-limited.

---

# 26. Publication and repository safety

Must remain true:

- no raw PDF/HTML/model request dumps committed;
- no private runtime outputs committed;
- no public Data release written;
- no immutable v0.5 artefact modified;
- no Viewer changes;
- no public card schema changes in this implementation;
- no fundraising-industry source republication;
- no unauthorised broad crawl;
- publication allowlist remains unchanged unless a separate product decision says otherwise.

Builder code/tests/docs may change.

CharityGraph Data should change only if explicitly required to record an implementation decision/result after review.

---

# 27. Implementation sequence

## Step 0 — completed prerequisites

Fundraising safety reconciliation and the minimum 22-case Knowledge Validation human gate are complete at the Builder SHAs recorded above.

Do not spend a new implementation turn redoing them.

## Step 1 — benchmark deterministic scaffold

Implement:

- cohort manifest;
- source-opportunity inventory;
- private candidate model;
- assessment-scope model;
- cost ledger;
- non-exclusive domain candidate architecture;
- deterministic review packet.

No model calls required for completion of this step.

## Step 2 — fundraising-industry adapters

Implement 2–3 initial high-density source adapters and conservative identity-candidate binding.

Keep all results private/review-only.

## Step 3 — document/web semantic retrieval

Add bounded retrieval/candidate generation across the approved domains.

## Step 4 — P2 low-cost model evaluation

Run only bounded cohort/slices after deterministic PREPARE is inspected.

## Step 5 — selective P3/O benchmark

Choose cases from observed ambiguity/misses, not a blanket pass.

## Step 6 — human/economic adjudication

Produce domain/source economic results.

No production routing change yet.

## Step 7 — ChatGPT/user product gate

Return results to ChatGPT/user.

The next product decision will specify:

- public schema extension, if any;
- domain-specific automation policy;
- source-family production approvals;
- P2/P3 routing;
- refresh policy;
- 120-subject economics expansion.

---

# 28. Implementation freedom

Codex/Luna may decide:

- Python module layout;
- Pydantic/dataclass implementation;
- CLI command naming;
- cache and runtime file layout;
- adapter class interfaces;
- deterministic parser implementation;
- review packet formatting;
- internal enum names;
- cost-ledger implementation;
- test helper structure.

Do not independently change:

- product boundaries;
- semantic domain definitions;
- scope semantics;
- no-parent-transfer rule;
- fundraising causal/economic boundary;
- source-role epistemics;
- H2 production permissions;
- public/private boundary;
- benchmark cohort purpose;
- human-gold requirement.

If implementation exposes a genuine unresolved product decision, stop that narrow path and report it rather than silently inventing policy.

---

# 29. Acceptance criteria

## Safety

- obsolete fundraising fallback prior removed/quarantined;
- no fundraising peer-imputation path;
- no public card/release mutation;
- no raw/private evidence committed;
- no Viewer change.

## Determinism

- PREPARE phase is API-free;
- cohort selection/config is reproducible;
- candidate IDs stable;
- inventory/aggregate outputs deterministic from same inputs;
- content hashes drive cache invalidation.

## Evidence

- every candidate resolves to subject or explicit identity block;
- every candidate preserves source family/role/location/hash;
- one passage can emit multiple domain candidates;
- scope/time preserved;
- sensitive inference guardrails tested.

## Economics

- stage/source/domain costs measurable;
- accepted observations and newly enriched subjects measurable;
- oracle gap separable from broader-source gap;
- industry-source marginal value measurable.

## Governance

- model output cannot become human gold;
- semantic outcome and orthogonal blockers are recorded separately in Benchmark v1 review decisions;
- reviewed-domain automation explanations must not falsely say human evidence is absent;
- all Ethos/service-orientation candidates require human review;
- adverse/sensitive notable-context candidates require review;
- no negative claim derived from source absence.

## Fundraising industry

- at least two high-density source families successfully enumerated or explicitly fail with documented reason;
- explicit provider/campaign/charity candidates preserve source semantics;
- vendor ROI/CPA/uplift not promoted;
- reported money preserves metric wording/scope;
- identity binding remains conservative.

---

# 30. Completion report expected from Codex

Return:

1. Builder commit SHA(s);
2. Data commit SHA only if explicitly authorised;
3. exact design authority SHA used: `14f7e53be7db558495f5afe7ab8c707cb37d7134`;
4. files/modules changed;
5. tests run and results;
6. commands for deterministic PREPARE and bounded model stages;
7. cohort/source inventory summary;
8. fundraising-industry adapters implemented;
9. candidate counts by domain/source;
10. cost-telemetry readiness;
11. known limits/failures;
12. any genuine product questions discovered;
13. confirmation that immutable v0.5 and Viewer were unchanged.

Do not stop with local-only changes. Commit and push all validated in-scope work. No deployment is required because this phase does not alter a deployable public artefact.

---

## Design rationale

> **Semantic Enrichment Benchmark v1 measures the frontier between public-evidence sparsity and economically recoverable knowledge, so CharityGraph can spend compute and source-acquisition effort where they buy the most useful, trustworthy coverage rather than trying to fill every blank indiscriminately.**
