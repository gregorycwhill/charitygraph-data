# CharityGraph Fundraising Industry Source Design

**Status:** Approved experimental source-family design for review-only integration  
**Date:** 2026-08-22  
**Applies to:** Semantic Enrichment Benchmark v1 and subsequent fundraising-source evaluation  
**Related documents:** `FUNDRAISING_KNOWLEDGE_DESIGN.md`, `ENRICHMENT_ECONOMICS_DESIGN.md`, `DESIGN_CONSOLIDATION_DECISIONS.md`

## 1. Executive decision

CharityGraph should treat the Australian fundraising industry as a distinct **experimental public enrichment source category**.

This is not merely a fallback web-search channel.

Professional fundraising bodies, awards, benchmark projects, consultants/agencies, fundraising platforms, listed providers and Gifts-in-Wills platforms publish unusually information-dense material that can directly identify:

- charities using particular fundraising practices;
- named fundraising campaigns;
- campaign type/mechanics/channels;
- fundraising-provider relationships;
- current or historical practice status;
- campaign targets;
- specific dollars spent or raised;
- participant/donor/fundraiser counts where explicitly reported;
- recurring campaign/program names;
- professional fundraising vocabulary and taxonomies.

For professionally fundraised charities, these sources may be fresher and more semantically precise than charity annual reports.

The preferred architecture is therefore:

> **source-led enumeration → conservative CharityGraph identity binding → targeted detail acquisition → bounded extraction → human review**

rather than charity-by-charity open-web search.

The first use remains review-only. No new source family is automatically authorised for public sidecar republication or national production crawling merely because it is public on the web.

## 2. Why this source category matters

Fundraising is a high-interest but poorly standardised part of the public charity record.

Regulator/AIS data provide donation/bequest income and broad financial information but usually do not answer questions such as:

- Does the organisation use face-to-face acquisition?
- Does it operate a current Gifts-in-Wills program?
- Does it run peer-to-peer challenge events?
- What Giving Day or gala campaigns did it run?
- Which external agency or platform delivered a campaign?
- How much did a specific campaign report raising?
- Was a fundraising practice recently discontinued or launched?

The fundraising industry generates public records because it needs to regulate practice, recognise work, market services, benchmark campaigns, disclose commercial relationships and demonstrate platforms/programs.

That creates a public “shadow registry” of fundraising activity that CharityGraph can structure without inventing performance judgements.

## 3. Product boundary

This source family expands **descriptive fundraising knowledge**, not fundraising evaluation.

CharityGraph may use adequately sourced industry material to represent:

- the existence of a fundraising practice;
- the existence/name/type/time of a campaign;
- the existence of a provider/platform relationship;
- explicit channels or mechanics;
- explicit campaign targets;
- explicit dollars spent;
- explicit dollars raised;
- explicit participant/donor/fundraiser counts;
- source-defined industry categories;
- explicit start/end/discontinuation/renewal information.

CharityGraph must not turn vendor/industry claims into canonical measures of:

- ROI;
- ROAS;
- cost per acquisition;
- donor acquisition efficiency;
- conversion;
- retention;
- uplift;
- lifetime value;
- campaign profitability;
- provider quality;
- causal effectiveness.

Such metrics may be retained as source-native evidence where useful for research/audit, but are not canonical CharityGraph performance observations in v1.

## 4. Direct dollars are allowed, but metric basis must remain explicit

Specific source-reported money can be highly useful and should not be discarded merely because it comes from a fundraising provider or industry source.

CharityGraph may represent direct observations such as:

> “Provider reports that campaign X raised AUD 6,149,957 over eight years.”

or:

> “Source reports campaign spend of AUD 85,000 for the stated period.”

provided the source, period, scope and metric wording are explicit.

These amounts are **source-reported campaign/provider observations**, not automatically canonical accounting values.

Rules:

- preserve source wording such as `raised`, `pledged`, `ticket sales`, `media spend`, `campaign spend`;
- preserve period/edition and reporting scope;
- do not silently map gross raised to AIS donations/bequests;
- do not silently map reported campaign spend to canonical annual fundraising expenditure;
- do not calculate ROI from raised/spent values merely because both are present;
- source-reported amounts may later be reconciled only under a separately governed policy.

## 5. Source-role model

The key epistemic design is **source role, not a universal source-quality score**.

A source can be excellent evidence for one proposition and poor evidence for another.

For example, a fundraising agency case study can be strong evidence that the agency delivered a named campaign for a charity, while its claim of “450% uplift” is a commercial performance claim unsuitable as a canonical CharityGraph metric.

Use source/evidence roles conceptually equivalent to:

| Source role | What it can strongly establish | Main cautions |
| --- | --- | --- |
| `industry_self_regulatory_association` | method participation, member status, compliance framework, explicit charity↔agency relationships | membership semantics must be understood; current page ≠ historic continuity unless dated |
| `industry_award_record` | named campaign, award/category, nomination, charity↔service-provider relationship | award recognition ≠ quality rating in CharityGraph; prefer official award record where available |
| `industry_benchmark` | campaign identity, source-defined category, explicit reported amount/count, sector vocabulary | metrics may have source-specific definitions/coverage; aggregate performance claims not canonical |
| `fundraising_provider_self_report` | client relationship, delivered campaign, channels/mechanics, direct reported campaign facts | commercial effectiveness/uplift claims remain source-native |
| `fundraising_platform_self_report` | platform-client/campaign relationship, campaign mechanics, direct reported campaign facts | platform may observe only funds/data processed on its system |
| `listed_provider_disclosure` | disclosed partner/client/program relationship, source-defined transaction/program scale | still provider-side; accounting/statutory context must be preserved |
| `gifts_in_wills_platform` | candidate or explicit charity partnership, bequest-program pathway | directory listing may need charity-side corroboration before current-program publication |
| `fundraising_trade_publication` | secondary reporting, award/event coverage, discovery/corroboration | ordinary secondary-source standards; distinguish publication from underlying award/provider claim |
| `industry_taxonomy_reference` | vocabulary, channel/program distinctions, benchmark definitions | not evidence that a specific charity uses a method unless charity attribution is explicit |

These roles should integrate with CharityGraph evidence/source metadata rather than become confidence scores.

## 6. Initial high-value source families

The first benchmark should evaluate source families in priority order based on information density, extraction cost and identity precision.

### 6.1 PFRA — face-to-face self-regulatory ecosystem

The Public Fundraising Regulatory Association (PFRA) is a particularly strong candidate because it is a charity-led self-regulatory body specifically for face-to-face fundraising.

Public material includes:

- charity member directory;
- fundraising-agency member directory;
- membership semantics and fee structure linked to donors recruited;
- monthly bulletins and fundraiser spotlights;
- standards/compliance material.

PFRA states that charity members benefit from face-to-face fundraising and its membership fee includes a levy per donor recruited in the previous calendar year. This gives current membership unusually strong semantics for the existence of a recent face-to-face fundraising program.

Bulletins can explicitly identify charity↔agency relationships, for example a fundraiser representing a named charity through a named agency.

Candidate facts:

- `fundraising_practice = face_to_face`;
- regular-giving relationship where explicitly supported;
- current/historical PFRA membership;
- `fundraising_provider_relationship` where charity and agency are explicitly connected;
- dated practice observations from bulletins.

Do **not** import PFRA statements about efficiency as CharityGraph fundraising-performance metrics.

Reference examples:

- https://pfra.org.au/about-us/
- https://pfra.org.au/membership/
- https://pfra.org.au/membership/fundraising-agency-members/
- https://pfra.org.au/march-bulletin/

### 6.2 FIA awards / recognised fundraising awards

Fundraising award programs provide semi-structured annual records of:

- charity;
- named campaign;
- professional category;
- consultant/service-provider nomination relationships;
- award/finalist year.

Candidate facts:

- campaign name/type/year;
- recognised campaign category as a source-native taxonomy term;
- provider relationship where the charity explicitly nominated the consultant/service partner;
- recognition observation under `notable_context` where appropriate.

CharityGraph must not translate “award finalist/winner” into a fundraising-quality score.

Prefer the official award body record. Trade-publication reproductions may act as secondary evidence/discovery when official material is unavailable.

Reference example:

- https://fandp.com.au/finalists-fia-awards-2026-407586/

### 6.3 Donor Republic / Funraisin P2P Top 30

The annual Australia/New Zealand peer-to-peer benchmark is especially attractive because it enumerates named campaigns and charities and attaches source-defined activity categories and fundraising amounts.

Candidate facts:

- campaign identity;
- beneficiary charity/organisation candidate;
- campaign year;
- P2P/event activity type;
- reported amount raised;
- year-on-year campaign observation;
- source-defined P2P taxonomy terms.

The benchmark itself notes limitations in public revenue collection/coverage. Preserve its metric definition and source basis; do not treat the value as audited accounting revenue.

Reference examples:

- https://donorrepublic.com.au/australia-new-zealands-top-30-peer-to-peer-events-benchmarks-p2p-performance/
- https://www.funraisin.co/peer-to-peer-fundraising-trends-2026

### 6.4 Fundraising agencies/consultancies

Public agency client lists and case studies can provide explicit:

- client relationships;
- campaign names;
- channels;
- campaign mechanics;
- dates;
- direct dollars/counts;
- launch/discontinuation/renewal context.

Examples include Cornucopia and Elevate.

Evidence use should distinguish:

- **relationship/method fact** — often strong first-party evidence about the agency's own work;
- **commercial performance claim** — source-native only unless independently corroborated and separately governed.

Reference examples:

- https://cornucopia.com.au/our-partners/
- https://cornucopia.com.au/2024/08/14/celebrating-25-years-of-impact-with-exciting-new-partnerships/
- https://elevatefundraising.com.au/ourwork/
- https://elevatefundraising.com.au/ourwork/one-foot-forward/
- https://elevatefundraising.com.au/ourwork/bloody-long-walk/
- https://elevatefundraising.com.au/ourwork/donate-a-plate/

### 6.5 Fundraising platforms

Platforms such as Raisely and Funraisin publish case studies and benchmark material because they process/host campaign infrastructure.

Potential direct observations:

- charity/platform relationship;
- named campaign;
- campaign type;
- mechanics such as matched giving or P2P;
- direct source-reported amount/count;
- platform-observed timing.

Platform figures may represent only activity visible on that platform and must retain that scope.

Reference example:

- https://www.raisely.com/blog/eofy-fundraising-australia

### 6.6 Listed providers / statutory commercial disclosure

Listed providers can provide high-quality evidence of client/program relationships in annual reports and market disclosures.

Jumbo Interactive's FY25 annual report, for example, names new charity lottery programs/partners. Such disclosures are valuable for:

- provider relationship;
- program type such as charitable lottery;
- period/currentness;
- provider-reported portfolio/program scale where explicitly defined.

This is strong relationship evidence because it appears in statutory corporate reporting, though it remains provider-side evidence rather than charity accounting evidence.

Reference example:

- https://www.jumbointeractive.com/wp-content/uploads/2025/08/Annual-Report-2025.pdf

### 6.7 Gifts-in-Wills platforms/directories

Platforms such as Safewill and Willed publicly enumerate large numbers of charity relationships and custom partnership paths.

Candidate facts:

- likely or explicit Gifts-in-Wills partnership;
- current charity listing;
- provider relationship;
- campaign/activation page where present.

A provider directory can cheaply generate candidates. For publication of a current charity bequest program, charity-side corroboration is preferred where easily available.

Reference examples:

- https://safewill.com/
- https://www.willed.com.au/charities/directory
- https://www.willed.com.au/charities/partners

### 6.8 Benchmarking Project and professional taxonomy sources

The Benchmarking Project benchmarks transactional fundraising data from 50+ Australian and Aotearoa New Zealand charities and explicitly works to standardise fundraising terminology.

Much of its detailed data is aggregate/member-restricted rather than attributable to specific public charities. Its main CharityGraph value may therefore be:

- external vocabulary/taxonomy evidence;
- definitions of fundraising programs/streams;
- sector-scale context;
- evidence about which distinctions professionals actually use.

Where public material does attribute a fact to a specific charity, ordinary evidence rules apply.

Reference examples:

- https://www.benchmarkingproject.org/
- https://fandp.com.au/reports/the-benchmarking-project-highlights-from-the-essentials-report-2025/

## 7. Source-led acquisition architecture

For fundraising-industry sources, prefer periodic enumeration of high-density sources over per-charity general search.

Conceptual pipeline:

```text
industry source index/table/directory
        ↓
deterministic source-record extraction
        ↓
external charity/campaign/provider candidate
        ↓
conservative CharityGraph identity resolution
        ↓
targeted detail-page acquisition if warranted
        ↓
deterministic + low-cost semantic extraction
        ↓
review-only typed candidates
        ↓
human/economic gate
```

Benefits:

- many charity candidates per request/download;
- high signal-to-noise ratio;
- lower LLM usage;
- better freshness;
- source-native taxonomy terms;
- explicit provider/campaign relationships;
- easier refresh/diff processing.

The existence of an industry-source match never overrides CharityGraph identity rules.

## 8. Source-family identifiers

Do not collapse every source into a single generic `independent_reference` record.

Use specific source-family identifiers under a fundraising-industry namespace or equivalent naming convention, for example:

```text
fundraising_industry.pfra
fundraising_industry.fia_awards
fundraising_industry.donor_republic_p2p
fundraising_industry.funraisin
fundraising_industry.raisely
fundraising_industry.cornucopia
fundraising_industry.elevate
fundraising_industry.jumbo
fundraising_industry.willed
fundraising_industry.safewill
fundraising_industry.benchmarking_project
```

Exact IDs are implementation detail, but source-family granularity must be sufficient to support:

- independent refresh policy;
- rights/publication policy;
- parser/version tracking;
- source-specific metric semantics;
- source-level coverage/economics.

Publisher/domain-specific adapters should not require a public schema change merely to exist.

## 9. Candidate observation types

The industry-source layer should feed the already approved fundraising domains.

### 9.1 Standing fundraising practice

Examples:

- face-to-face;
- telephone/telefundraising;
- regular giving;
- gifts in wills;
- peer-to-peer capability;
- community fundraising;
- lottery/raffle;
- digital acquisition;
- corporate partnership.

A source can support current, historical or unknown status depending on time evidence.

### 9.2 Fundraising campaign

Candidate fields may include:

- local campaign ID;
- name;
- campaign type;
- edition/year;
- time;
- status;
- mechanics;
- channels;
- reported target;
- reported amount raised;
- reported amount spent;
- reported participant/donor/fundraiser counts;
- action URL where appropriate;
- evidence.

### 9.3 Fundraising provider relationship

Private pilot candidate shape conceptually:

```json
{
  "relationship_type": "fundraising_service_provider",
  "provider_name": "Example Agency",
  "provider_external_id": null,
  "provider_subject_id": null,
  "fundraising_scope": {
    "practice_term": "face_to_face",
    "campaign_id": null
  },
  "status": "current",
  "time": {
    "valid_from": null,
    "valid_to": null,
    "observed_at": "2026-07-01"
  },
  "source_record_ids": ["src:..."],
  "evidence_ids": ["ev:..."]
}
```

Do not mint a charity subject for a commercial provider.

A later cross-domain organisation registry may decide how non-charity organisations are represented. This pilot does not require that decision.

## 10. Provider relationship evidence rules

A provider relationship may become a review candidate when explicit evidence establishes the charity and provider in a fundraising context.

Strong examples:

- association bulletin: fundraiser represents Charity A through Agency B;
- charity-nominated service-partner award: Agency B nominated by Charity A;
- agency case study: Agency B says it delivered named fundraising program/campaign for Charity A;
- charity site: Charity A identifies Agency/Platform B;
- listed provider report: Provider B names Charity A as a current program/client;
- platform case study: Platform B names Charity A and campaign X.

Weak/insufficient by itself:

- logo wall with no context;
- generic testimonial without identifiable fundraising relationship;
- social-media follow/mention;
- provider saying it works “with charities like…” when relationship status is unclear;
- supplier directory entry without charity linkage.

For public promotion, relationship status/time must be explicit enough not to turn an old case study into a current supplier relationship.

## 11. Freshness and time semantics

Fundraising-industry evidence can be unusually fresh and therefore requires disciplined time handling.

Retain separately where available:

- source publication date;
- retrieval date;
- campaign/event period;
- relationship valid-from/valid-to;
- observed-at;
- edition/year;
- current/historical/unknown status.

Rules:

- a current member directory may support current membership/practice only where membership semantics warrant it;
- a dated “new client” announcement supports the relationship at that time, not indefinite current status;
- an old case study is historical unless later evidence confirms continuity;
- a recurring annual campaign should retain edition-specific observations;
- refresh policies should vary by source family.

## 12. Identity resolution

Fundraising-industry sources create **candidate external identities**, not automatic subject bindings.

Use available corroboration such as:

- exact legal/operating name;
- official charity domain;
- ABN/ACNC where present;
- state/branch qualifier;
- known parent/network relationship;
- campaign page linking to official charity site;
- charity-side corroboration.

Name-only matching never binds an observation to a CharityGraph subject.

Hard cases include:

- RFDS state sections versus national body;
- RSPCA state entities versus RSPCA Australia;
- Cancer Council state entities;
- global brands with Australian affiliates;
- similarly named foundations;
- renamed campaigns/organisations.

Preserve ambiguity rather than attach provider/campaign evidence to the wrong legal/operating subject.

## 13. Taxonomy strategy

Fundraising-industry sources provide valuable empirical taxonomy evidence.

Use professional vocabularies from FIA, Donor Republic/Funraisin, Benchmarking Project, platforms and agencies to test distinctions such as:

- regular giving;
- single giving/appeals;
- face-to-face;
- telephone;
- direct mail;
- digital acquisition;
- major gifts;
- gifts in wills;
- community fundraising;
- peer-to-peer;
- events;
- Giving Days;
- corporate partnerships;
- workplace giving;
- lottery/raffle;
- capital campaign.

Do not adopt any one industry's taxonomy as universal CharityGraph truth.

Preserve:

> source-native term → candidate CharityGraph term → provenance/crosswalk

Canonical vocabulary remains deliberately small and versioned, and should be frozen only after the shared pilot shows real mapping pressure.

## 14. Campaign metrics policy

### 14.1 Canonical/direct candidates allowed

Where explicit and scoped:

- target amount;
- dollars raised;
- dollars spent;
- ticket sales/proceeds where accurately labelled;
- participant count;
- donor count;
- fundraiser count;
- campaign duration;
- campaign edition/year.

### 14.2 Source-native/noncanonical by default

- ROI;
- ROAS;
- CPA/CAC;
- conversion rate;
- retention rate;
- activation rate;
- uplift/increase claims;
- average donor value;
- lifetime value;
- provider “efficiency” or “performance” scores.

The source-native record may preserve these values if lawful/useful, but they do not become CharityGraph analytic conclusions.

### 14.3 No causal join

Do not compute:

```text
campaign dollars raised / campaign spend = CharityGraph ROI
```

and do not connect campaign reported money to AIS income/expense without a separate governed reconciliation method.

## 15. Rights, attribution and republication

Public accessibility does not automatically grant bulk republication rights.

For every source family, record/assess:

- access method;
- robots/terms constraints where relevant;
- copyright/licence;
- whether structured values may be republished;
- whether source prose should remain locator-only;
- attribution requirements;
- snapshot-retention policy;
- refresh cadence;
- source takedown/change handling.

Default pilot posture:

- private retained snapshot where lawful/consistent with CharityGraph source policy;
- public evidence URL/title/date/location;
- compact factual CharityGraph observation rather than copied marketing prose;
- no bulk publication of third-party case-study text.

Production/public sidecar policy is decided source-family by source-family after the pilot.

## 16. Benchmark integration

Add a fundraising-specific source-economics comparison inside Semantic Enrichment Benchmark v1.

For the selected fundraising-rich cohort compare:

- **F0** — structured charity/regulator data;
- **F1** — charity annual report + charity website;
- **F2** — deterministic fundraising-industry indexes/directories/tables;
- **F3** — targeted provider/platform/award detail pages;
- **F4** — low-cost LLM on selected narrative slices;
- **O** — same-source high-spec oracle on selected hard cases;
- **H1** — human adjudication;
- **H2** — broader-source audit where needed.

Key question:

> **Does adding fundraising-industry evidence produce more accepted fundraising knowledge per dollar than escalating model capability over charity-only evidence?**

Expected outcome is empirical, not assumed.

## 17. Source-family economics metrics

Measure per source family:

- records/pages downloaded;
- charities/campaigns enumerated;
- identity candidates produced;
- resolved/ambiguous/rejected identity bindings;
- accepted fundraising-practice observations;
- accepted campaign observations;
- accepted provider relationships;
- accepted monetary/count observations;
- subjects gaining first fundraising-practice coverage;
- subjects gaining first campaign coverage;
- marginal freshness relative to charity annual report/website;
- percentage extracted deterministically;
- percentage requiring low-cost LLM;
- human review minutes;
- acquisition/model dollar cost;
- refresh/maintenance burden;
- rights/licensing complexity;
- error modes by source family.

Report both:

- accepted observations per dollar; and
- newly enriched subjects per dollar.

The second metric prevents a few information-rich large charities from dominating the apparent economics.

## 18. Initial adapter sequence

Do not integrate every source immediately.

Recommended first implementation:

### Adapter A — structured campaign benchmark

Use a P2P benchmark/table source such as Donor Republic/Funraisin to test:

- table extraction;
- campaign identity;
- charity resolution;
- source-defined campaign/activity taxonomy;
- reported amounts;
- edition/year;
- duplicate/recurring campaign handling.

### Adapter B — structured method/provider source

Use PFRA to test:

- current method participation;
- charity membership semantics;
- agency directory;
- bulletin relationship extraction;
- current/historical status;
- charity/branch identity ambiguity.

### Adapter C — award/provider relationship source

Use FIA award records (or an authoritative award listing) to test:

- named campaign/category;
- consultant/service-provider nominations;
- recognition/notable-context crossover.

Only after those prove the shared source abstraction should narrative agency/platform adapters be added.

## 19. Review-only candidate dispositions

Reuse the shared semantic review outcomes where possible:

- `ACCEPT`
- `EDIT`
- `REJECT`
- `WRONG_DOMAIN`
- `INSUFFICIENT`
- `IDENTITY_BLOCKED`
- `TIME_SCOPE_UNCLEAR`
- `CANONICAL_MAPPING_UNCLEAR`

Useful fundraising-specific reasons may include:

- `COMMERCIAL_PERFORMANCE_CLAIM`
- `ACCOUNTING_SCOPE_UNCLEAR`
- `PROVIDER_RELATIONSHIP_UNCLEAR`
- `CAMPAIGN_PRACTICE_AMBIGUOUS`

Prefer a small disposition enum plus detailed rationale over an enormous status vocabulary.

## 20. Hard-case fixtures

The source-family pilot must include fixtures for:

1. **Current PFRA member** — method observation supported, but no assumed agency relationship.
2. **Bulletin names charity + agency** — provider relationship candidate with date.
3. **Old agency case study** — historical relationship/campaign, not automatically current.
4. **Provider logo only** — reject/insufficient relationship evidence.
5. **Agency says campaign raised $X and ROI 7:1** — accept direct dollars with source basis; keep ROI noncanonical.
6. **P2P benchmark campaign amount** — accept source-reported campaign amount; do not map to accounting donation income.
7. **Award finalist campaign** — accept campaign/recognition candidate; no quality score.
8. **Charity-nominated service partner** — strong relationship candidate; time scope retained.
9. **Willed/Safewill directory listing** — provider/bequest candidate; charity-side corroboration preferred before current-program publication.
10. **Listed provider annual report names client program** — strong provider/program relationship candidate.
11. **RFDS/RSPCA branch ambiguity** — identity block until correct legal/operating subject is established.
12. **Commercial uplift claim only** — retain source-native if needed; no canonical performance observation.

## 21. Public coverage semantics

A charity with no match in fundraising-industry sources is **not** inferred to lack professional fundraising.

Coverage should eventually distinguish what was processed, for example:

```json
{
  "capability": "fundraising.methods",
  "status": "not_found_in_source",
  "assessment_scope": {
    "source_families": [
      "organisation_website",
      "annual_report",
      "fundraising_industry.pfra"
    ],
    "policy_version": "semantic-enrichment-v1"
  }
}
```

No industry-source absence becomes a substantive negative claim.

## 22. Relationship to general H2 source audit

The general enrichment-economics H2 audit remains manual/broad-source research.

Fundraising-industry evidence is different because it has now passed enough product review to justify a dedicated **experimental source category**.

This means the next Builder phase may implement bounded adapters for approved fundraising-industry sources without waiting for a national social-media/web-source policy.

It does **not** authorise:

- broad social-media crawling;
- arbitrary agency-site crawling at national scale;
- republishing provider content;
- automatic public promotion.

## 23. Public schema implications after pilot

The pilot should inform, but not immediately force, public contract changes for:

- richer `fundraising_methods` / future `fundraising_practices` semantics;
- `fundraising_campaigns[]`;
- campaign-reported money/count objects;
- public provider relationship representation;
- new source/evidence roles;
- fundraising campaign coverage capability;
- compact assessment scope.

Keep all candidate/source extraction review-only until the shared pilot validates identity, time, source-role and monetary semantics.

## 24. Success criteria

The experimental source family is successful if it demonstrates that CharityGraph can obtain materially better fundraising coverage at acceptable cost while preserving epistemic discipline.

Specifically, the pilot should show:

- high identity-binding precision;
- high precision for practice/campaign/provider facts;
- meaningful additional subjects enriched beyond charity-only sources;
- meaningful freshness gain;
- substantial deterministic extraction from indexes/tables;
- low-cost bounded LLM use for narrative pages;
- no canonical adoption of commercial performance claims;
- exact source basis for reported dollars/counts;
- manageable refresh and rights burden.

## 25. Governing principle

> **Fundraising-industry sources are valuable because they are dense public records of who raised money, how, with whom and through which campaigns. CharityGraph should structure those observable facts while refusing to inherit the industry's commercial judgements about what worked.**
