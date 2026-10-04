# Fundraising vocabulary and measurement research gate — 4 October 2026

**Status:** Approved bounded research-gate decision; governs the next review-only implementation tranche, not public release or scale.
**Scope:** North Star sections 8 (Fundraising), 12 (Relationships), 13 (Finances) and 20 (Evidence/Coverage/Freshness).
**Supersession:** Consolidates the fundraising-specific findings of campaign tasks t01–t12. It does not supersede the product, evidence, taxonomy, source-rights, or immutable-release authorities indexed in `DOCUMENT_AUTHORITY.md`.

## Decision

**Proceed with a bounded, review-only fundraising slice; do not authorise Top-100, public promotion, new source acquisition, or a public-schema change.** The governing safety semantics are ready to freeze. The candidate vocabulary, source adapters, and public projection remain review-only until a representative, rights-cleared source-backed pilot passes the preconditions below.

### What CharityGraph can safely answer now — for a supported review case

| User question | Safe answer and required support | Honest failure mode |
| --- | --- | --- |
| Does this charity use F2F? | `current`, `recent`, `historical`, or `discontinued` only for a bound, scoped F2F practice observation with source wording, evidence ID, observation date, source role and lifecycle/time support. | `unknown`, `not_found_in_scoped_source`, or `not_processed`; never a timeless Boolean or an absence claim. PFRA membership alone establishes membership only. |
| What evidence and date support that? | The review projection can expose source/evidence identifiers, source-native wording, observed date, optional validity interval, source role, subject binding and scope. | Ambiguous or unresolved identity blocks promotion; old reports/case studies stay historical unless continuity is explicitly evidenced. |
| What does it spend on fundraising? | A directly disclosed amount/share, deterministic reconstruction from a defensible denominator, or defensible lower/upper attribution bounds, all with accounting entity, period, basis, source rows and component treatment. | `unavailable`/`not_available_from_source` or `null`; no marketing heuristic, prior, peer fill, midpoint or zero-by-silence. |
| Can reported money be attached to this method/campaign? | Only where source wording and evidence explicitly identify the same smallest supported practice, campaign, appeal, or provider-relationship scope. Preserve the source metric/basis. | Organisation or portfolio money remains unattributed. Do not split aggregates merely because a method/campaign/provider is observed; no ROI, net proceeds, cost share, effectiveness or causal join. |

## Capability disposition

| Capability | Gate disposition | Decision |
| --- | --- | --- |
| Native facets and source-scheme crosswalk | **Ready to freeze** as an internal, versioned composable-facet contract. | Preserve source term → candidate term → provenance/crosswalk; do not freeze a universal flat taxonomy or source-specific terms as universal truth. |
| F2F currentness | **Ready to freeze** as evidence/time/scope policy and deterministic governance. | Distinguish `current`, `recent`, `historical`, `discontinued`, `unknown`, and scoped non-finding; no universal freshness age. |
| Provider relationship | **Ready to freeze** for explicit, directed, evidence-bound relationships. | F2F, directories, logo walls, or generic testimonials do not infer an agency relationship; currentness needs its own time evidence. |
| Campaign identity | **Ready to freeze** as a separate, bounded object. | Campaign identity/edition/time/mechanics remain distinct from standing practice; recurrence must be evidenced. Candidate type vocabulary remains review-only. |
| Money metric vocabulary | **Ready for review only.** | Retain source-native amount, metric label, currency, period, accounting basis and scope. Campaign `raised`, target, ticket/proceeds and spend are not interchangeable accounting metrics. |
| Attribution grain | **Ready to freeze** as an explicit-link rule. | The smallest supported grain is organisation, portfolio, practice, campaign, appeal, or provider relationship; unknown stays organisation-level/unattributed. |
| Expenditure bounds | **Ready to freeze** as a constrained measurement policy; **review-only** as a production representation. | Direct disclosure → deterministic reconstruction → bounds (definite/possible/excluded) → unavailable/null. No forced point estimate. |
| Cost share and net proceeds | **Not appropriate** as generic CharityGraph metrics. | Only retain an expressly reported source-native share or proceeds amount with its basis; do not calculate net proceeds or allocate a portfolio share across methods/campaigns. |
| Source adapters | **Needs more evidence.** | PFRA/FIA/Donor Republic/Funraisin remain bounded experimental/research adapters. No production ingestion or public promotion is approved. |
| Visible projection | **Ready for review only.** | The four-subject local profile is reproducible and displays lifecycle, evidence, scope, money linkage and coverage safely; it is neither a public card nor a release surface. |

## Evidence considered

The decision is based on local, reproducible t01–t12 artifacts, not new acquisition: the Builder archaeology map (`FUNDRAISING_STATE_MAP_2026-10-04.md`), typed-contract and F2F policy fixtures, money-scope linkage, a 16-case research-only grain study, the vocabulary candidate, the four-case review profile, and the 24-case regression fixture. The focused suites passed on 4 October 2026: **59 test executions** (29 cohort/currentness/vocabulary/money/derivative tests, 5 typed-contract tests, and 25 industry-promotion tests). Suites overlap, so this is not a unique-test count.

The regression fixture reports 12/24 practice observations, 3/5 confirmed PFRA bindings, 4/24 unresolved or ambiguous bindings, 14/24 available money observations, zero available share/bounds cases, and nine finance-without-method-attribution controls. Those numbers validate fail-closed contract handling; they do not estimate population coverage or precision on production sources.

## Scale preconditions and open research

Scale remains premature until all of the following are complete:

1. A 30–50-case, adversarial, source-backed review cohort with retained lawful evidence/locators, independent identity adjudication, and the fundraising hard cases (including F2F cessation, provider ambiguity, campaign/practice separation, finance-only and scoped non-findings).
2. Measured domain precision, edit/reject rate, time/status and identity/scope accuracy, campaign/practice and funding-source/practice boundary errors, false-positive classes, and explicit coverage-scope review. Precision must dominate recall; no aggregate score may conceal a failure class.
3. A source-family rights, refresh, retention and republication decision for each proposed adapter, plus exact identity-binding and time semantics. Research retrieval is not canonical acquisition.
4. Finance fixtures with real defensible definite/possible/excluded component envelopes and independently checked additivity; the current cohort has no available share/bounds case.
5. A review of vocabulary pressure and crosswalk non-equivalence using the cohort before public enums, campaign types, or adapter mappings are frozen.
6. A coordinated public-contract, Data, Builder and Viewer decision with versioned schemas/examples, projection tests, correction treatment and release gates. This gate does not authorise any of them.

Remaining research questions are: which source families can lawfully produce publishable campaign-row money; how PFRA membership semantics vary over time and membership class; what precise currentness evidence a provider case study can support; whether any real financial disclosures support defensible method/campaign bounds; and which campaign categories survive cross-source mapping without flattening mechanics, channels and delivery details.

## Reused and untouched machinery

The slice reuses subject identity binding, source/evidence records, coverage/missingness, time and reporting-period fields, `MoneyObservation`, financial-record linkage, generic relationships, and projection gates. It deliberately leaves workforce/compensation claims, organisation-wide F2F continuity, street/door/private-site setting, provider effectiveness, fundraising ROI, donor economics, causal attribution, public v0.5, Viewer, and national/Top-100 processing untouched.

## Canonical policy promoted by this record

This record freezes only these policies: multi-axis evidence-bound practice observations; campaign/practice/provider/funding-source/finance separation; F2F lifecycle and scoped-nonfinding semantics; explicit smallest-grain money linkage; and the direct/reconstruction/bounds/unavailable expenditure ordering. It does not promote any candidate source adapter, vocabulary assignment, research metric, local fixture, or public schema.
