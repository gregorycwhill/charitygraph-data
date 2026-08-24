# CharityGraph Domain Profile Index

**Status:** Canonical index, version 1.0-draft

**Purpose:** Define the governed domain profiles to be specified and implemented incrementally

## 1. Profile pattern

Each domain profile will define:

- user questions and scope;
- entities, assertions, relationships and events;
- source families and proposition-specific authority;
- external schemes and native vocabularies;
- deterministic, model-assisted and human-review methods;
- absence, uncertainty and contradiction semantics;
- evidence and lineage requirements;
- publication projection and risk controls;
- coverage and evaluation measures;
- representative examples and holdout cases.

All profiles use the integrated primitives in `INTEGRATED_PRODUCT_AND_DATA_MODEL.md`.

## 2. Identity and organisational structure

**Questions:** What is the entity? Which identifiers, names, legal forms, registrations, groups, brands and operating units apply at a given time?

**Key scope:** Legal entity, registered charity, ABN holder, reporting group, brand, branch, program and site must remain distinguishable. `provider_subject_id` is an external boundary field. No new universal CharityGraph identifier is invented.

**Priority:** Foundation slice.

## 3. Programs, services and operating geography

**Questions:** What does the organisation actually do, through which programs or services, for whom and where?

**Key scope:** Program identity, activity, delivery mode, eligibility, service area, site and temporal status. Website navigation is evidence, not necessarily the program model.

**Priority:** Foundation slice.

## 4. Purpose, causes, beneficiaries and public goals

**Questions:** What purposes, subject areas, populations and public goals are evidenced?

**Schemes:** ACNC/ATO source categories, CLASSIE, UN SDGs and CharityGraph operational-activity vocabulary. Purpose, beneficiary, activity and outcome remain separate.

**Priority:** Foundation slice.

## 5. Participation

**Questions:** How can people or organisations participate—giving money or goods, volunteering, membership, advocacy, events, peer support, governance or other contribution?

**Design:** Facets for participant role, mode, channel, setting, commitment, eligibility, transfer/instrument and temporal availability. Organisational invitations and direct observations are distinguished.

**Priority:** Initial population target; full breadth follows foundation slice.

## 6. Fundraising

**Questions:** How, where and to whom does the organisation solicit or receive support?

**Design:** Method, channel, setting, instrument, audience, campaign, creative, call-to-action, fulfilment and observation method. Must accommodate direct observation of door-knocking, staffed tables, bins, shops, OOH, TV and digital media.

**Priority:** Initial population target with extensible observation model.

## 7. Finance

**Questions:** What resources, income, expenditure, assets, liabilities and financial trends are reported or calculated, and at what consolidation scope?

**Schemes:** Source line items plus National Standard Chart of Accounts mapping. Calculated metrics remain formula-labelled, period-aware and source-traceable.

**Priority:** Early core domain after identity/scope.

## 8. Governance and organisational capacity

**Questions:** Who governs and leads, how is the organisation structured, what policies and capabilities are evidenced, and how do these change?

**Risk:** Personal information, role timing and group/entity scope require care. Governance facts are not a quality rating.

**Priority:** Early core domain.

## 9. Relationships and ecosystems

**Questions:** Which organisations fund, operate, own, auspice, partner with, accredit, regulate, support or are affiliated with one another?

**Design:** Directed, typed, scoped and time-bounded relationship statements with role-specific evidence. Avoid generic “related to” edges where a precise predicate is available.

**Priority:** Early analyst use case.

## 10. Industry participation and shadow registries

**Questions:** Which memberships, accreditations, codes, registrations and industry obligations apply?

**Authority:** An industry body can be authoritative within its own registry remit. Fees, code participation and membership status are first-class data where lawful.

**Priority:** First-class source family from initial build.

## 11. Ethos, stance and conduct

**Questions:** What values, religious or philosophical positions, public stances and conduct are evidenced and materially relevant?

**Risk:** Separate self-description, external allegation, formal finding and CharityGraph synthesis. Consequence-aware review and precise evidence are mandatory.

**Priority:** Staged after foundation, with strict risk policy.

## 12. Notability and information demand

**Questions:** Which subjects warrant greater acquisition, refresh or review effort?

**Design:** Reproducible features may include scale, public prominence, network position, information volume and user demand. This is processing prioritisation—not merit, impact or trustworthiness.

**Priority:** Required early for cohort allocation.

## 13. Outcomes, evaluation and evidence

**Questions:** What outcomes are claimed, measured or evaluated; by whom; using what design; for which population and time?

**Design:** Preserve claim, measure, study/evaluation method, comparator, result, attribution level and limitations. Do not collapse heterogeneous evidence into a universal effectiveness score.

**Priority:** Staged domain, informed by academic and sector research.

## 14. Adverse events, compliance and correction

**Questions:** What formal decisions, sanctions, material controversies, corrections or resolved challenges are evidenced?

**Risk:** High-consequence claims require authoritative sourcing, status/time precision, response/right-of-reply context and specialist escalation where necessary.

**Priority:** Controlled profile, not part of the first low-risk slice.

## 15. Source, publication and coverage

**Questions:** Where did each item come from, how was it processed, what is published, and what remains unattempted or unresolved?

**Design:** Source registry, acquisitions, artefacts, evidence, model tasks, adjudications, releases, coverage observations and correction proposals.

**Priority:** Universal infrastructure; present in every slice.

## 16. First reality slice

The first implementation slice combines profiles 2–4 and 15 for approximately ten varied charities. It should produce governed private previews for:

- identity and scope;
- programs/services and geography;
- source-reported regulatory classifications;
- CLASSIE subject/population assignments;
- operational-activity assignments;
- UN SDG alignment;
- coverage, evidence and model lineage.

It deliberately excludes public release, Viewer changes, universal ontology completion and high-risk adverse/conduct conclusions.
