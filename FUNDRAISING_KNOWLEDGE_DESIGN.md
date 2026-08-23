I’ve drafted it as an implementation-oriented product/design document, grounded in the current v0.5 contract and Builder. In particular, it incorporates the current flat fundraising-method model, the fact that `web_v2` has no fundraising candidate domain and is currently first-match-only, the integrated pilot’s page-processing limitation, and the obsolete fallback-prior path that still survives in old Builder code/docs.

The file-generation runtime is currently erroring even on trivial writes, so I can’t give you a reliable sandbox attachment this turn. Save the following verbatim as **`FUNDRAISING_KNOWLEDGE_DESIGN.md`** in the Codex directory:

````markdown
# CharityGraph Fundraising Knowledge — Design and Population Plan

**Status:** Working product design; implementation-ready for a bounded review-only pilot  
**Updated:** 2026-08-21  
**Scope:** CharityGraph Data contract design + CharityGraph Builder evidence/pipeline design

## 0. How Codex should use this document

This is a **product/design instruction**, not an invitation to rediscover the product semantics.

Before implementing it, read the canonical shared CharityGraph documents in `CharityGraph-Data`:

- `PRODUCT.md`
- `PRINCIPLES.md`
- `CURRENT_STATE.md`
- `ROADMAP.md`
- `IMPLEMENTATION_PLAN.md`
- `TEST_PLAN.md`
- `CODEX_TO_CHATGPT_HANDOFF.md`
- `PUBLIC_SCHEMA_VNEXT_SPEC.md`
- `PUBLIC_CONTRACT_CONSOLIDATION_PROPOSAL.md`

Then inspect the current CharityGraph Builder implementation, especially:

- `src/causebase_builder/models.py`
- `src/causebase_builder/v05/models.py`
- `src/causebase_builder/v05/fundraising.py`
- `src/causebase_builder/fundraising.py`
- `src/causebase_builder/sources/web_v2.py`
- `src/causebase_builder/evidence_engine.py`
- `PROVENANCE_AND_ESTIMATION.md`
- `AGENTS.md`

Where old Builder documentation conflicts with the current Data contract, **the current Data contract wins**.

In particular, old Builder material still contains obsolete instructions that fundraising expenditure must never be blank and that a fallback prior may be used. That is superseded. Current CharityGraph policy permits `null`/unavailable when no defensible measurement or bound exists and explicitly prohibits a universal fallback prior.

Do not mutate the immutable public release `releases/v0.5.0-2026-08-15`.

The first implementation of this design is **review-only**. It should produce private candidate/evaluation material, fixtures, diagnostics and tests. It must not silently publish new fundraising observations or rebuild the public corpus.

---

# 1. Product objective

CharityGraph should make public fundraising information legible as a structured, longitudinal description of a charity's fundraising operating model.

A user should be able to ask:

- How does this charity raise money?
- What standing fundraising practices does it use?
- What identifiable fundraising campaigns or activities has it run?
- What public evidence supports those observations?
- When were those practices or campaigns active?
- What public evidence exists about fundraising expenditure?
- Which public sources did CharityGraph actually assess when it found nothing?

The acceptance test is:

> **Can a competent analyst understand or compare charities' fundraising approaches from CharityGraph without re-scraping all the underlying source documents?**

This is useful to donors, researchers, journalists, charity advisers, charities, sector analysts and general-purpose AI agents.

Commercial users such as fundraising consultants may derive substantial value from the data. That is acceptable and desirable where it results from reuse of general-purpose public infrastructure.

CharityGraph should not build their consulting recommendations, prospect scores or proprietary analytics for them.

---

# 2. Product boundary

CharityGraph may publish:

- directly disclosed fundraising practices;
- directly disclosed fundraising campaigns or activities;
- directly reported campaign targets, amounts raised and donor counts;
- source-faithful fundraising-related financial rows;
- direct functional-expense allocations;
- mechanically derived financial amounts;
- defensible fundraising-expenditure attribution bounds;
- explicit source-coverage states;
- longitudinal practice/campaign observations;
- evidence and provenance.

CharityGraph must not publish or infer:

- fundraising ROI;
- cost to raise $1;
- donor acquisition cost;
- donor lifetime value;
- campaign profitability;
- channel effectiveness;
- causal attribution from fundraising expenditure to particular donation income;
- claims that one fundraising method generated a particular revenue amount;
- arbitrary overhead allocations to revenue sources;
- charity fundraising rankings;
- "good fundraiser" / "poor fundraiser" labels;
- consultant prospect scores;
- claims that a practice does not exist merely because CharityGraph did not observe it.

Downstream products may combine CharityGraph observations into evaluative or commercial analyses under their own methodology, assumptions, disclosures and branding.

---

# 3. Current-state diagnosis

## 3.1 Existing architecture worth preserving

The approved v0.5 contract already separates:

- `funding_sources[]`;
- `fundraising_methods[]`;
- `fundraising.expenditure`;
- source-native financial statements;
- canonical financial metrics;
- analytic projections;
- explicit coverage;
- claim basis;
- extraction method;
- direct versus mechanically derived versus inferred/estimated claims.

The approved fundraising-expenditure bounds model is also conceptually sound:

- components may be `definite`, `possible` or `excluded`;
- lower bound sums definite components;
- upper bound sums definite + possible components;
- additivity must be established;
- point estimate is optional;
- point estimate needs an independently defensible basis;
- no midpoint is automatically invented;
- bounds are attribution bounds, not confidence intervals;
- no ROI is implied.

Keep this architecture.

## 3.2 Current fundraising-method model is semantically mixed

The older Builder `FundraisingMethodObservation` vocabulary places materially different concepts in one flat list.

Examples include:

**Channels**
- face-to-face
- telephone
- direct mail
- digital advertising

**Standing programs**
- regular giving
- major donor program
- bequest program

**Mechanisms**
- peer-to-peer
- raffles or lotteries

**Relationships**
- corporate partnerships

**Events / activity forms**
- fundraising events
- community fundraising

This is workable as a rough exploratory vocabulary but poor as a durable analytical model.

The public v0.5 schema is even looser: fundraising methods have a source/display label and optional category. That flexibility is useful pre-1.0 but should not become the corpus ontology by accident.

## 3.3 Population is currently the larger weakness

The current website candidate extractor has no fundraising domain.

It searches:

- activities;
- beneficiaries;
- programs;
- participation;
- geography.

Therefore a fundraising passage cannot currently become a fundraising-knowledge candidate through the generic website semantic pipeline.

The block classifier is also effectively mutually exclusive. Once a block matches a domain, processing stops.

That is wrong for CharityGraph evidence semantics.

For example:

> Join our annual challenge and raise funds from friends to support children with cancer.

may legitimately support:

- participation;
- fundraising campaign;
- peer-to-peer fundraising;
- beneficiary.

Those are different propositions supported by one source passage.

The page-discovery layer also lacks dedicated fundraising roles such as:

- Ways to Give;
- Fundraise for Us;
- Gifts in Wills;
- Major Giving;
- Giving Day;
- Appeals.

The integrated Evidence Engine currently records discovered URLs but, in the bounded retained-snapshot pilot, processes only the first retained snapshot for the selected subject. The stated page-role contract is therefore ahead of integrated execution.

Finally, the document pipeline is strong at financial syntax but does not yet have a systematic semantic fundraising-practice/campaign pass.

## 3.4 Current-data behaviour to preserve

The v0.5 migration retains old fundraising-method material under `legacy_unbound` where governed provenance could not be reconstructed.

Do not "repair" that by manufacturing evidence.

Legacy preservation is not observed coverage.

## 3.5 Legacy safety issue

`src/causebase_builder/fundraising.py` still contains an obsolete demo estimation path that applies a broad fallback prior, defaulting to 15% of total expenditure.

Old Builder `PROVENANCE_AND_ESTIMATION.md` and `AGENTS.md` also preserve superseded language saying:

- fundraising estimates are required;
- blank is unacceptable;
- a fallback prior is permitted.

This contradicts the current CharityGraph contract.

Before scale:

1. remove or quarantine the obsolete production-accessible fallback implementation;
2. reconcile stale Builder documentation with current Data policy;
3. add a regression test proving no current production/publication path can invoke a universal fundraising prior.

Historical fixtures may retain old behaviour only if clearly isolated and incapable of entering a current build.

---

# 4. Core model decision: standing practice is not a campaign

This is the most important schema distinction.

A persistent or recurring way of seeking donations is not the same thing as an identifiable fundraising campaign or event.

## 4.1 Fundraising practice

A **fundraising practice** describes a standing, recurrent or materially persistent way the organisation seeks funds.

Examples:

- regular giving;
- face-to-face donor acquisition;
- outbound telephone fundraising;
- direct mail;
- gifts-in-wills program;
- major gifts;
- corporate partnerships;
- workplace giving;
- community fundraising capability;
- peer-to-peer capability;
- paid digital acquisition;
- raffles/lotteries.

For pre-1.0 compatibility, retain the existing conceptual location `fundraising_methods[]`, but define it as **standing/recurrent fundraising practices**.

A later rename to `fundraising_practices` may be cleaner, but should be decided after the pilot rather than forced now.

Candidate observation:

```json
{
  "observation_id": "obs:...",
  "claim_basis": "direct",
  "extraction_method": "document_text",
  "source_record_ids": ["src:..."],
  "evidence_ids": ["ev:..."],

  "practice_kind": "channel",
  "term_id": "fundraising.face_to_face",
  "term_label": "Face-to-face fundraising",
  "source_label": "our face-to-face donor acquisition program",

  "status": "current",

  "time": {
    "effective_from": null,
    "effective_to": null
  }
}
````

Candidate `practice_kind` values:

* `channel`
* `program`
* `mechanism`
* `partnership`
* `other`

This facet exists to avoid putting channels, programs and mechanisms on the same conceptual level. It is not intended as a grand universal fundraising ontology.

Preserve source wording separately from the CharityGraph mapping.

For example:

> source: "telephone appeals"

may map to:

> `fundraising.telephone`

but CharityGraph retains the source phrase and provenance.

If mapping is uncertain, keep an unmapped/review state rather than forcing a term.

### Multi-dimensional observations

One passage may support more than one practice.

Example:

> Monthly donors are recruited through outbound telephone campaigns.

May support:

* `regular_giving` — program;
* `telephone` — channel.

Those should not be collapsed into an awkward single compound category.

---

# 5. Fundraising campaigns

A **fundraising campaign** is an identifiable fundraising initiative, appeal or event, usually time-bounded or edition-bounded.

Examples:

* 2025 Giving Day;
* annual gala;
* emergency flood appeal;
* month-long challenge;
* fun run;
* peer-to-peer challenge;
* crowdfunding campaign;
* Christmas appeal;
* matched-giving drive;
* raffle;
* capital campaign.

Campaigns deserve a separate object because they may have:

* name;
* edition/year;
* dates;
* status;
* campaign type;
* channels;
* mechanics;
* target;
* reported amount raised;
* reported donor count;
* reported new-donor count;
* matching arrangements;
* action URL;
* recurrence.

Candidate shape:

```json
{
  "campaign_id": "frcamp:...",
  "observation_id": "obs:...",

  "claim_basis": "direct",
  "extraction_method": "document_text",
  "source_record_ids": ["src:..."],
  "evidence_ids": ["ev:..."],

  "name": "Giving Day 2025",
  "campaign_type": "giving_day",
  "status": "historical",

  "time": {
    "start": "2025-05-14",
    "end": "2025-05-14",
    "label": "2025 Giving Day"
  },

  "mechanics": [
    "matched_giving",
    "peer_to_peer"
  ],

  "channels": [
    "digital"
  ],

  "reported_target": {
    "amount": "500000",
    "currency": "AUD"
  },

  "reported_amount_raised": {
    "amount": "620000",
    "currency": "AUD",
    "basis_label": "reported by organisation as raised"
  },

  "reported_donor_count": 842,
  "reported_new_donor_count": null,

  "action_url": null
}
```

Only evidence-supported fields should be populated.

## 5.1 Candidate campaign types

Seed the pilot with likely types, but do not freeze them yet:

* `giving_day`
* `appeal`
* `emergency_appeal`
* `capital_campaign`
* `gala_or_dinner`
* `challenge`
* `peer_to_peer_event`
* `fun_run_or_walk`
* `crowdfunding`
* `raffle_or_lottery`
* `matched_giving_campaign`
* `community_event`
* `other`

## 5.2 Campaign type, mechanic and channel are orthogonal

A Giving Day may use:

* matched giving;
* ambassadors;
* peer-to-peer;
* email;
* organic social;
* paid digital;
* telephone;
* workplace teams.

Do not create a new campaign type for every combination.

Possible mechanics for evaluation:

* `matched_giving`
* `peer_to_peer`
* `ambassadors`
* `team_fundraising`
* `sponsorship`
* `challenge_completion`
* `auction`
* `raffle_or_lottery`
* `pledge`
* `other`

Possible channels:

* `face_to_face`
* `telephone`
* `direct_mail`
* `email`
* `paid_digital`
* `organic_digital`
* `event`
* `workplace`
* `other`

These are pilot vocabularies, not frozen public enums.

## 5.3 Campaign does not automatically imply standing practice

One gala in 2024 proves a campaign/activity.

It does not prove the organisation currently operates a standing gala/event fundraising program.

Recurring activity may support both propositions only where recurrence is itself evidenced.

---

# 6. Optional fundraising delivery model

Evaluate whether public evidence supports a useful **delivery model** observation.

Possible examples:

* in-house fundraising team;
* external face-to-face agency;
* outsourced telemarketing/call centre;
* event delivered by a fundraising partner;
* campaign technology provider.

Candidate:

```json
{
  "delivery_role": "external_fundraiser",
  "delivery_mode": "face_to_face",
  "provider_name": "Example Agency",
  "provider_subject_id": null,
  "status": "current"
}
```

This is optional for v1.

Do not turn vendor identity into a prerequisite.

Do not infer delivery relationships from logos or generic partner pages.

---

# 7. Vocabulary strategy

Apply the existing CharityGraph principle:

> **Extract broadly; canonicalise selectively.**

Preserve three layers:

1. source-native phrase;
2. small CharityGraph canonical fundraising term where defensible;
3. unmapped or ambiguous review state.

Do not force everything into `other` for the sake of 100% categorical coverage.

Treat fundraising vocabulary as distinct from the main CharityGraph cause/activity taxonomy. It can still have stable term IDs and versioning.

The 30–50-case pilot should determine the minimum useful vocabulary.

High-recall retrieval should seek at least:

* regular/monthly giving;
* face-to-face / direct dialogue;
* telephone / telemarketing / call centre;
* direct mail;
* email appeals;
* paid social/search/digital acquisition;
* general appeals;
* emergency appeals;
* major gifts;
* philanthropy;
* bequests;
* gifts in wills;
* legacy giving;
* corporate partnerships;
* workplace giving;
* community fundraising;
* peer-to-peer;
* crowdfunding;
* events;
* galas;
* fun runs/walks;
* challenges;
* Giving Days;
* capital campaigns;
* raffles/lotteries;
* matched giving;
* donor acquisition;
* retention/stewardship where explicitly described as fundraising practice.

This is a retrieval longlist, not a publication taxonomy.

---

# 8. Critical anti-inference rules

These should become explicit fixtures and validation rules.

## 8.1 Funding source does not prove method

Bequest income does not prove a current gifts-in-wills program.

Regular donation revenue does not prove a regular-giving acquisition program.

Corporate donations do not prove a corporate-partnership fundraising strategy.

Funding source and fundraising practice remain separate domains.

## 8.2 Donate button does not prove digital fundraising strategy

A Donate action URL can support:

> participation: donation available

It does not by itself support:

* digital advertising;
* donor acquisition;
* regular giving;
* active appeal;
* fundraising campaign.

## 8.3 Event does not automatically mean fundraising event

A gala, dinner, run or community event may be programmatic.

Only classify it as fundraising when fundraising purpose is supported by evidence.

## 8.4 Sponsor logo does not prove fundraising partnership

A logo may represent:

* commercial sponsorship;
* donated services;
* program partnership;
* supplier;
* venue;
* corporate philanthropy.

No automatic fundraising classification.

## 8.5 "Raised $X" is not automatically accounting revenue

An organisation saying:

> The campaign raised $2 million.

may mean:

* cash;
* pledges;
* gross proceeds;
* gross before event costs;
* a campaign period different from the financial year;
* money collected for another entity.

Preserve the source-reported campaign metric and basis.

Do not silently reconcile it to AIS donation income or a financial statement.

## 8.6 Campaign donor count is not CRM analytics

CharityGraph may report:

> Organisation states that 1,000 donors participated.

It must not infer:

* annual unique donors;
* retention;
* acquisition rate;
* LTV;
* donor quality;
* duplication with other campaigns.

## 8.7 Historical evidence is not current evidence

Example:

> We discontinued face-to-face donor acquisition in March 2025.

Expected:

* face-to-face practice observed historically;
* end date/period retained;
* current status not inferred.

## 8.8 Provider relationship does not imply effectiveness

CharityGraph may record an explicitly disclosed external fundraising provider.

No judgement about effectiveness, value or cost follows.

---

# 9. Coverage needs assessment scope

`not_found_in_source` is useful only if the consumer knows what CharityGraph actually inspected.

Compare:

> Homepage assessed; no bequest evidence found.

with:

> Homepage, Ways to Give, Gifts in Wills links and latest annual report assessed; no bequest program evidence found.

Those are very different information states.

Add a general optional `assessment_scope` concept to coverage.

Candidate:

```json
{
  "capability": "fundraising.methods",
  "status": "not_found_in_source",
  "assessed_at": "2026-08-21T...",

  "assessment_scope": {
    "source_families": [
      "organisation_website",
      "annual_report"
    ],

    "page_roles": [
      "homepage",
      "giving",
      "fundraise",
      "bequests_major_giving"
    ],

    "reporting_periods": [
      "2025"
    ],

    "assessment_policy_version":
      "fundraising-knowledge-v1"
  }
}
```

This should be designed as a general CharityGraph primitive, because it will also be useful for Ethos and Notability.

The rendering rule is strict:

> `not_found_in_source` = no qualifying observation found in the processed source scope.

Never render it as:

* does not have a bequest program;
* does not use telephone;
* has no campaigns;
* has no fundraising activity.

A downstream commercial user can choose to treat "not publicly observed in assessed sources" as a prospecting signal.

CharityGraph does not convert that into a claim of absence.

Evaluate separate capabilities:

* `fundraising.methods`
* `fundraising.campaigns`
* `fundraising.expenditure`

---

# 10. Pipeline architecture: candidate domains must be non-exclusive

Do not simply add `"fundraising"` to the existing block-category dictionary and retain first-match behaviour.

Move toward independent domain candidate producers.

Conceptually:

```text
normalised evidence block
    |
    +-- activity candidates
    +-- beneficiary candidates
    +-- program candidates
    +-- participation candidates
    +-- geography candidates
    +-- fundraising candidates
```

Future Ethos and Notability can use the same architecture.

Every private candidate should retain:

* candidate ID;
* domain;
* subtype;
* exact source text;
* source URL;
* page/report role;
* selector/page/location;
* source/content hash;
* retrieval time;
* source role;
* proposed claim basis;
* extraction method;
* candidate canonical value/term;
* material alternative where relevant;
* time/status signal;
* warnings;
* review status.

A candidate is not a public claim.

Deduplication may group repeated propositions later but must not prevent the same evidence supporting distinct domains.

---

# 11. Website acquisition

Keep acquisition bounded.

Add fundraising page roles such as:

* `giving`
* `fundraise`
* `bequests_major_giving`
* `fundraising_campaign`
* optionally `corporate_support`

Useful discovery phrases:

**Giving**

* donate
* ways to give
* support us
* monthly giving
* regular giving

**Fundraise**

* fundraise
* fundraising
* raise funds
* community fundraising
* peer-to-peer
* challenge
* start a fundraiser

**Bequests / major giving**

* gifts in wills
* bequest
* leave a gift
* legacy giving
* major gifts
* major giving
* philanthropy

**Campaign**

* appeal
* giving day
* emergency appeal
* campaign
* challenge
* fundraiser
* raffle
* gala

For the pilot:

1. load/fetch homepage;
2. perform bounded same-origin discovery;
3. select at most one page per governed role;
4. load/fetch each selected page or retain explicit failure;
5. normalise each selected page;
6. run independent candidate extractors;
7. retain hash/location provenance;
8. produce review packet.

Do not recursively crawl.

Treat:

* giving/fundraise/bequests pages as generally stable;
* campaign/event/news pages as generally transient.

Third-party campaign platforms are explicitly out of scope for broad crawling in v1.

Retain external destinations as action/discovery links. A later product decision may authorise selected external campaign-page acquisition.

---

# 12. Annual reports and documents

Annual reports may be the richest source for fundraising practice because they often disclose:

* donor-acquisition channels;
* regular giving;
* bequests;
* major gifts;
* community fundraising;
* campaign performance facts;
* strategy changes;
* discontinued methods;
* fundraising expenditure;
* external providers;
* year-on-year changes.

Do not send whole reports to an LLM by default.

Use:

> deterministic extraction → high-recall fundraising retrieval → bounded semantic extraction → human review

Retrieve candidate passages around terms such as:

* fundraising;
* fundraise;
* donor;
* supporter;
* appeal;
* regular/monthly giving;
* face-to-face;
* telephone;
* telemarketing;
* call centre;
* direct mail;
* digital acquisition;
* major gifts;
* philanthropy;
* bequest;
* gifts in wills;
* community fundraising;
* peer-to-peer;
* crowdfunding;
* gala;
* challenge;
* Giving Day;
* match funding;
* workplace giving;
* corporate partnership;
* raffle;
* donor acquisition;
* retention;
* capital campaign.

Retain enough surrounding context to determine:

* organisation versus industry commentary;
* subject scope;
* practice versus campaign;
* current versus historical;
* campaign metric versus accounting metric.

The bounded semantic stage should answer questions such as:

* Does this passage explicitly establish a fundraising practice?
* What source-faithful phrase describes it?
* Standing practice or campaign?
* What time/status is supported?
* Campaign name/type?
* Mechanics/channels?
* Target/amount/donor metrics?
* Discontinuation/change?
* External provider?
* Canonical mapping sufficiently clear?
* What remains unknown?

All semantic output remains review-only until the product gate is passed.

---

# 13. Keep four fundraising domains distinct

CharityGraph should model separately:

1. **Funding sources** — where money comes from.
2. **Fundraising practices** — standing ways money is sought.
3. **Fundraising campaigns** — identifiable initiatives/events.
4. **Fundraising expenditure** — public evidence about fundraising-related costs.

Source-native financial rows remain a fifth preservation layer.

A card might validly say:

* donations/gifts/bequests = 42% of income;
* regular giving observed;
* face-to-face historically observed;
* 2025 Giving Day observed;
* fundraising allocation = 10%.

CharityGraph must not conclude:

> The 10% fundraising spend generated the 42% donation income.

---

# 14. Preserve current fundraising-expenditure policy

Allowed:

* direct fundraising expenditure;
* direct functional allocation/share;
* mechanically derived amount from direct share × defensible denominator;
* definite/possible/excluded component treatment;
* lower and upper attribution bounds;
* point estimate only with independent allocation basis.

Forbidden:

* universal fallback prior;
* default 15%;
* peer imputation simply to avoid a blank;
* midpoint of bounds;
* arbitrary fractional marketing allocation;
* parent + child double counting;
* automatic treatment of marketing as fundraising;
* fundraising expense / donation income efficiency ratios.

If no defensible measurement or bound exists:

* retain `null`;
* use appropriate coverage;
* retain assessment scope.

That is a successful result, not a pipeline failure.

---

# 15. Pilot cohort

Use approximately 30–50 deliberately adversarial cases.

This is a product-design corpus, not a statistically representative national sample.

Include:

* large national fundraising brands;
* hospital/health foundations;
* international aid;
* animal/environment;
* education/university foundations;
* cultural organisations;
* religious charities;
* advocacy organisations;
* small/local charities;
* rich annual reports;
* sparse websites;
* regular-giving programs;
* bequests;
* face-to-face;
* telemarketing;
* Giving Days;
* challenge events;
* galas/events;
* peer-to-peer/community fundraising;
* corporate partnerships;
* direct fundraising-expenditure disclosure;
* ambiguous marketing/fundraising costs;
* organisations where no method is publicly observed.

Prefer existing CharityGraph subjects where practical.

---

# 16. Human review questions

## Practices

For each case:

1. What fundraising practices are explicitly evidenced?
2. What exact wording supports them?
3. Current, historical, discontinued or unknown?
4. Channel, program, mechanism or partnership?
5. Safe canonical mapping?
6. Is this really a funding source instead?
7. Is the supposed evidence merely a Donate link?
8. Is a campaign being incorrectly converted to a standing practice?

## Campaigns

1. Is there an identifiable campaign?
2. Name/type?
3. Period/edition?
4. Mechanics/channels?
5. Explicitly reported targets/results?
6. Campaign metrics kept separate from accounts?
7. Recurrence explicitly evidenced?
8. Correct organisation/program/parent scope?

## Expenditure

1. Direct disclosure?
2. Direct functional share?
3. Mechanical amount?
4. Definite/possible/excluded components?
5. Additivity safe?
6. Defensible bounds?
7. If not, is unavailable/null correct?

## Coverage

1. Which source families/page roles were assessed?
2. Is non-observation phrased safely?
3. Does the assessment scope explain the limitation?

---

# 17. Evaluation metrics

Do not use one aggregate accuracy score.

Report:

## Acquisition

* homepages acquired;
* fundraising-role pages discovered;
* fundraising-role pages acquired;
* failures by role;
* annual reports available;
* fundraising passages retrieved.

## Candidate yield

* practice candidates per subject;
* campaign candidates per subject;
* expenditure candidates per subject;
* source family/role;
* canonical mapping rate;
* ambiguous mapping rate.

## Human quality

* practice precision;
* campaign precision;
* campaign/practice boundary errors;
* funding-source/practice errors;
* time/status accuracy;
* identity/scope accuracy;
* false positives from Donate links;
* false positives from events;
* false positives from sponsor logos;
* human edit/reject rate;
* additivity correctness;
* null/unavailable correctness.

## Coverage quality

* `not_found_in_source` cases with adequate assessment scope;
* reviewer judgement that absence language is non-misleading.

Precision should dominate recall in v1.

---

# 18. Required hard-case fixtures

## A. Donate button only

Expected:

* donation participation may be observed;
* no digital-advertising practice;
* no donor-acquisition inference;
* no campaign.

## B. Bequest income but no program evidence

Expected:

* bequest financial/funding-source observation;
* no current gifts-in-wills program.

## C. Gifts-in-wills page

Expected:

* bequest program observed;
* current status if supported;
* no bequest-income inference.

## D. Face-to-face discontinued

Expected:

* historical/discontinued practice;
* date/period if supported;
* not current.

## E. Giving Day with match

Expected:

* campaign;
* giving-day type;
* matched-giving mechanic;
* direct reported target/result;
* no ROI.

## F. Gala with unclear purpose

Expected:

* no fundraising campaign unless fundraising purpose explicit.

## G. Corporate logos

Expected:

* no automatic fundraising partnership.

## H. Peer-to-peer challenge

Expected:

* campaign;
* peer-to-peer mechanic;
* participation path;
* standing practice only if recurrence/capability separately supported.

## I. Marketing expense line

Expected:

* not automatically fundraising;
* possible component only with contextual evidence;
* no invented percentage allocation.

## J. Direct fundraising functional allocation

Expected:

* direct share;
* mechanically derived approximate amount where denominator supports it;
* no duplicate source row;
* no ROI.

## K. Campaign "raised $X"

Expected:

* direct campaign result;
* source wording/basis retained;
* no automatic reconciliation to donation revenue.

## L. Broad assessed scope with no evidence

Expected:

* `not_found_in_source`;
* assessment scope retained;
* no substantive negative.

---

# 19. Public-contract implications after the pilot

Do not mutate 0.5 as part of the pilot.

The next contract should be prepared to consider:

* richer `fundraising_methods[]`;
* new `fundraising_campaigns[]`;
* optional `fundraising_delivery[]`;
* `fundraising.campaigns` capability;
* general coverage `assessment_scope`;
* versioned fundraising vocabulary;
* explicit practice time/status;
* campaign-result observations distinct from canonical financial metrics.

Reuse existing CharityGraph observation/evidence primitives.

Do not create a parallel provenance architecture.

---

# 20. Viewer and agent implications

No major Viewer redesign in the first pilot.

A future fundraising section could look conceptually like:

### How it raises funds

* Regular giving
* Gifts in wills
* Face-to-face fundraising — historical; ended 2025

### Recent fundraising activity

* 2025 Giving Day — matched giving; organisation reports $620k raised

### Fundraising expenditure

* Directly reported allocation: 10%
* Approximate amount: $585k, mechanically derived

### Funding mix

* Donations, gifts & bequests: ...

Every item exposes evidence.

Never show:

* green/red fundraising performance;
* "strong fundraising program";
* "missing opportunity";
* ROI;
* prospect scores.

Machine-readable output should let an unfamiliar agent distinguish:

* source of funds versus fundraising practice;
* practice versus campaign;
* campaign result versus accounts;
* direct versus mechanically derived;
* current versus historical;
* non-observation versus non-existence.

---

# 21. Implementation sequence

## Phase A — safety reconciliation

1. Verify current canonical Data policy.
2. Quarantine/remove obsolete fallback-prior production access.
3. Reconcile stale Builder `AGENTS.md` and `PROVENANCE_AND_ESTIMATION.md`.
4. Add regression tests prohibiting fallback-prior use in current builds.

No public release change.

## Phase B — private candidate model

Add review-only structures for:

* fundraising practice;
* fundraising campaign;
* optional delivery model;
* assessment scope.

Do not change public cards.

## Phase C — website pipeline

1. Add fundraising page roles.
2. Make domain candidate extractors independent/non-exclusive.
3. Actually process selected discovered pages.
4. Emit fundraising practice/campaign candidates.
5. Preserve acquisition and assessment scope.

## Phase D — document pipeline

1. Deterministic fundraising passage retrieval.
2. Bounded semantic extraction.
3. Preserve page/section/hash provenance.
4. Keep all outputs review-only.

## Phase E — 30–50-case pilot

1. Run cohort.
2. Generate compact review packet.
3. Score domain-specific quality.
4. Inspect vocabulary pressure.
5. Inspect practice/campaign boundary.
6. Inspect coverage-scope usefulness.
7. Report recurring false-positive classes.

## Phase F — product decision

Only after review:

* freeze/modify fundraising vocabulary;
* decide final public schema;
* decide whether delivery model survives;
* decide campaign coverage capability;
* decide public assessment-scope shape;
* decide automation threshold.

Update canonical Data product documents before corpus-scale implementation.

---

# 22. Likely Builder touchpoints

Codex should inspect rather than blindly assume, but likely files include:

* `src/causebase_builder/sources/web_v2.py`
* `src/causebase_builder/evidence_engine.py`
* `src/causebase_builder/models.py`
* `src/causebase_builder/v05/models.py`
* `src/causebase_builder/v05/fundraising.py`
* `src/causebase_builder/fundraising.py`
* document-v2 extraction/evaluation modules
* tests/fixtures
* `AGENTS.md`
* `PROVENANCE_AND_ESTIMATION.md`

Do not hand-edit generated release files.

Likely Data changes after the pilot, not before, may include:

* `PRODUCT.md`
* `PRINCIPLES.md`
* `PUBLIC_SCHEMA_VNEXT_SPEC.md`
* public schemas
* capability registry
* `TEST_PLAN.md`
* `ROADMAP.md`
* `IMPLEMENTATION_PLAN.md`

---

# 23. Non-goals

The first implementation must not:

* build a national fundraising benchmark dashboard;
* build a Catalyst-specific product;
* build prospect scoring;
* ingest donor CRM data;
* estimate LTV;
* estimate acquisition costs;
* infer strategy from revenue composition;
* crawl arbitrary third-party campaign platforms;
* create a universal fundraising-vendor database;
* redesign Viewer;
* rebuild the national corpus;
* mutate v0.5;
* implement Ethos/Notability in the same change;
* introduce large new infrastructure;
* run a frontier model over the whole corpus.

---

# 24. Implementation freedom

Codex may choose:

* private candidate-model classes;
* module boundaries;
* cache layout;
* CLI command names;
* deterministic retrieval implementation;
* review packet format;
* fixture structure;
* test helpers;
* bounded page-fetch implementation.

Codex should not independently change:

* measurement/evaluation boundary;
* practice-versus-campaign semantics;
* absence semantics;
* no-fallback-prior policy;
* direct-v-derived semantics;
* identity rules;
* publication status;
* immutable-release ownership;
* review-only nature of the first pilot.

If implementation exposes a genuine product conflict, report it rather than silently resolving it.

---

# 25. Minimum acceptance criteria

## Safety

* no immutable Data release mutation;
* no raw/private source committed;
* no universal fallback prior reachable from current production/publication paths;
* no public card writes;
* no ROI/efficiency calculation.

## Acquisition

* fundraising-specific page roles are discoverable;
* selected bounded pages are actually processed;
* failures are explicit.

## Semantics

* domains are non-exclusive;
* funding source remains separate from practice;
* practice remains separate from campaign;
* current/historical status survives;
* campaign result remains separate from canonical financial metrics.

## Provenance

Every candidate retains:

* source URL/document locator;
* hash;
* page/report role;
* extraction method;
* candidate claim basis;
* subject/scope or explicit identity block.

## Coverage

`not_found_in_source` retains assessment scope and cannot become a substantive claim of non-existence.

## Evaluation

Produce:

* 30–50-case review packet;
* hard-case fixtures;
* domain-specific precision/edit/reject statistics;
* vocabulary-pressure report;
* campaign/practice boundary error report;
* recurring false-positive analysis.

No aggregate score may hide poor fundraising precision.

---

# 26. Completion report expected from Codex

When implementation is explicitly authorised, return:

1. concise summary of changes;
2. Builder commit SHA;
3. Data SHA only if Data changes were explicitly authorised;
4. tests run and results;
5. pilot command/run details;
6. candidate counts;
7. review-packet location;
8. unexpected source/pipeline findings;
9. unresolved product questions;
10. confirmation that v0.5 and Viewer were unchanged;
11. confirmation that obsolete fallback-prior production access was removed or quarantined.

Do not stop with local-only validated changes when implementation is authorised. Commit and push all in-scope work. No deployment is required if no deployable public artefact changed.

---

# 27. Design rationale

> **CharityGraph should describe fundraising as a longitudinal, evidence-bound operating model — funding sources, standing practices, identifiable campaigns and fundraising expenditure — while leaving effectiveness, causal economics and commercial recommendations to downstream users.**

```

One thing I found while doing this that is worth elevating: **the stale Builder instructions are more than documentation debt.** `AGENTS.md` currently instructs coding agents that a blank fundraising estimate is unacceptable and refers them to the old fallback ladder, while the current product contract says the opposite.  `PROVENANCE_AND_ESTIMATION.md` still explicitly defines peer imputation and a fallback prior as levels 5–6.  I’ve therefore made reconciliation of those files **Phase A**, before Codex does any new fundraising work. That is a high-leverage guard against a future agent helpfully resurrecting the 15% prior. 
```
