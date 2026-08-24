# CharityGraph experiences

**Status:** Canonical user and channel requirements

**Version:** 2.0-draft

**Date:** 24 August 2026

## 1. Experience principles

Every CharityGraph experience SHALL preserve:

- the unit of analysis;
- subject and scope;
- source-native, mapped and derived status;
- applicable time;
- coverage and missingness;
- evidence and production method;
- current, disputed or corrected state; and
- release identity.

Ordinary users should not need to understand the internal ontology. Analysts, developers and agents may progressively retrieve deeper structure.

## 2. Public organisation discovery

A user searches for a charity by name, identifier, cause, location or program.

They receive:

- resolved operating organisation and relevant legal identities;
- current public summary;
- programs and services;
- cause, population, activity and SDG assignments;
- geography roles;
- selected finance, participation, fundraising, governance and evidence information;
- clear source and assessment labels;
- coverage and freshness; and
- links to challenge a field or inspect more detail.

The page is restrained and readable. It does not expose runtime state, private source bodies or every internal assertion by default.

## 3. Program and service discovery

A user asks what a charity actually does rather than relying on its legal purpose.

They can distinguish:

- program from organisation;
- repeatable service from bounded project;
- intended, eligible, reached and represented populations;
- operating, delivery, catchment and observed-reach geography;
- activity, intervention, output and outcome;
- current availability from historical description; and
- source-reported classification from CharityGraph mapping.

## 4. Analyst cohort builder

An analyst constructs a cohort using identity, regulatory, cause, population, geography, program, service, participation, fundraising, finance, governance, capacity, relationship, outcome and time filters.

Before export, CharityGraph identifies:

- unit of analysis;
- cohort denominator and exclusions;
- release and policy version;
- coverage by claim family;
- comparable and non-comparable measures;
- missingness and staleness;
- selected-current-view policy; and
- known source or right-tail bias.

The analyst can export linked tables rather than destructively flatten every domain into one row.

## 5. Service-system and competitor map

A consultant asks:

> Where is need, and how is it being met?

CharityGraph connects external need or demand evidence to:

- programs and services;
- providers and delivery partners;
- sites and channels;
- advertised, funded and observed geography;
- capability, capacity and availability;
- referral pathways and access conditions;
- workforce and infrastructure constraints;
- grants, contracts and other resource relationships; and
- actual reach where evidenced.

The experience distinguishes need, demand, referral, waitlist and unmet-demand estimates. It does not infer that an advertised service is currently available or that a waitlist represents all demand.

## 6. Funding and ecosystem analysis

An analyst traces grant, contract, donation, sponsorship or in-kind flows through intermediaries, auspices and delivery partners.

The view distinguishes:

- award;
- commitment;
- payment or disbursement;
- receipt;
- revenue recognition;
- expenditure or use; and
- refund or return.

It prevents one economic flow reported by several parties from being counted several times. Network measures identify projection, method and missingness and are not organisation-worth rankings.

## 7. Fundraising activity analysis

A user examines how an organisation mobilises resources.

They can separate:

- strategy;
- solicitation mechanism;
- communication channel;
- setting and physical configuration;
- resource sought;
- donor relationship stage;
- commitment and payment instrument;
- delivery party and compensation model;
- campaign, appeal, creative and placement; and
- audited facts from vendor or fundraiser performance claims.

Future directly observed activity can show a shopping-centre table, residential door-knocking, donation bin, television creative or out-of-home placement without implying a continuous organisation-wide practice from one encounter.

## 8. Participation discovery

A user discovers opportunities to contribute time, skill, voice, membership, governance or lived experience.

CharityGraph distinguishes:

- an advertised opportunity;
- an enduring role structure;
- a bounded participation episode; and
- an aggregate measure.

The initial experience is discovery and structured data, not matching, scheduling or participant management.

## 9. Finance and comparison

An analyst inspects source-faithful statements and normalised concepts.

They can trace every normalised amount to reporting instance, source line, period, currency, scale, consolidation and assurance context. CharityGraph calculations expose formulas and inputs and do not inherit audit status automatically.

Comparison tools warn when periods, scopes, definitions or allocation methods are incompatible. No default administration-cost or efficiency league table is presented.

## 10. Evidence and evaluation review

A funder or analyst inspects an outcome or impact claim.

They can distinguish:

- output from outcome and impact;
- monitoring from evaluation;
- observed change from causal effect;
- qualitative, quantitative and mixed-method evidence;
- first-party claim from independent finding;
- null, mixed and negative findings; and
- social-value modelling from cash or audited return.

The experience exposes study scope, population, method, comparator, uncertainty, limitations and source location.

## 11. Ethos, conduct and notable context

A user inspects evidence relevant to organisational character or a downstream mandate.

The interface distinguishes:

- value or ethos statement;
- policy position;
- commitment;
- implementation evidence;
- practice observation;
- complaint or allegation;
- investigation;
- finding;
- sanction;
- appeal;
- response and remediation; and
- notability signal.

It uses neutral procedural language, exposes subject response and avoids a universal controversy, virtue, reputation or trust score.

## 12. Mandate screening by a downstream agent

An agent receives an explicit user rule such as legal eligibility, cause, geography, population, ethos or adverse-matter constraints.

CharityGraph supplies:

- resolved subject and program scope;
- applicable governed assertions;
- source authority and evidence status;
- freshness and coverage;
- conflicts and corrections;
- non-inference constraints; and
- stable references for explanation.

The downstream agent applies the rule and returns an explainable decision. CharityGraph does not execute the payment or convert private preferences into canonical data.

## 13. Model-assessed taxonomy assignment

A well-documented charity is processed for SDG, cause, population or activity classifications.

The model receives governed evidence and an approved mapping policy. It returns:

- best-supported primary assignments;
- secondary assignments where useful;
- subject or program scope;
- evidence references;
- confidence;
- concise rationale;
- model and policy metadata; and
- alternatives when genuinely close.

The model does not return `unknown` merely because a different reasonable mapping is possible. The public record clearly labels the assignment as CharityGraph- or model-assessed.

## 14. Charity or community correction

From a field, assertion or graph edge, a contributor can:

1. identify the challenged record automatically;
2. describe the problem;
3. propose a replacement, qualification or new source;
4. declare relevant affiliation;
5. request privacy protection where applicable;
6. receive a challenge identifier;
7. track review; and
8. see the outcome and affected future release.

Possible outcomes include accepted, accepted with edit, partially accepted, upheld, insufficient evidence, duplicate, superseded by newer evidence, withdrawn or specialist review.

The contributor need not understand the internal schema.

## 15. Research reproducibility

A researcher identifies:

- release and schema versions;
- taxonomy releases and mappings;
- source cohorts;
- current-view and automation policies;
- model/provider and prompt-policy identity;
- correction history;
- coverage limitations; and
- exact public artefact checksums.

Exact release reproduction is mandatory. Forensic reconstruction of every external source state may vary by rights, sensitivity and cohort policy.

## 16. Data-builder experience

A developer discovers the current release without running Viewer code. They can retrieve:

- catalogue metadata;
- manifest and checksums;
- schemas;
- subject and domain distributions;
- stable references;
- licences and attribution;
- coverage and corrections; and
- machine-readable provenance.

Static artefacts remain available even if a future service is unavailable.

## 17. Community-curation experience

The public can see that contributions matter:

- review status is visible;
- decisions explain whether and why a record changed or stood;
- accepted corrections appear in release notes;
- systematic error classes inform later pipeline improvements; and
- contributors may receive attribution where desired and safe.

Community evidence improves the dataset; prominence, voting and coordinated pressure do not determine canonical truth.

## 18. Failure and limitation experiences

The product communicates:

- source unavailable;
- not acquired;
- not processed;
- extraction failed;
- unresolved identity;
- insufficient evidence;
- not reviewed;
- stale;
- disputed;
- withheld; and
- not applicable.

These are useful states. They do not collapse into a blank field or a negative conclusion.
