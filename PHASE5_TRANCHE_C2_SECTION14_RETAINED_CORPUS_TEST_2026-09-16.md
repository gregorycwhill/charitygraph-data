# Phase 5 Tranche C2 — North Star v0.2 §14 funding / dependencies retained-corpus test

**Status:** Completed bounded retained-corpus semantic test; no execution authority.
**Date:** 16 September 2026. **Active projection:** `north-star-v0.2`.

## Question and boundary

This test asks what retained evidence can establish about funding relationships
and dependencies without turning receipt, revenue, a category share or source
silence into dependency. The controlling rule is: **a receipt alone does not
prove dependency**. No source was acquired, refetched or transmitted.

The starting commits were Builder
`7f1a6f8397dbd55e091466ba4470bedcd3487889` and Data
`42680f5288538e607fe42251eda5999f6a019f44`.

## Frozen cohort and retained evidence

| Item | Why selected | What it supports | Limit |
|---|---|---|---|
| Environmental Justice Australia FY2024–25 financial report, ABN `74052124375`, `archive/processed/phase2b/2026-08-14/report-extracts/74052124375-EJA-Financial-Report-2024-25.json` | Smallest retained complete report with stages, commitments and an explicit reliance statement. | Aggregate grant/donation/revenue/receipt facts; specific-project commitments; accounting performance obligations; source-reported economic reliance and Future Fund contingency. | No named funder, individual award, independently verified dependency or viable alternative. |
| Australian Red Cross FY2022–23 retained pages, `archive/processed/reality-spike/2026-08-10/report-extracts/50169561394-2022-23-financial-pages.json` | Named NBA/Lifeblood arrangement, conditions and scope countercase. | Lifeblood-scoped government-funding relationship, Deed, funding categories, performance obligations, return of excess funds and a transparent category share. | 25 retained pages from a 131-page source; endpoints are not governed durable subjects; no Society-wide dependency conclusion. |

The wider retained-universe check found no positive retained case for a resolved
funder/recipient pair, named philanthropic award, intermediary, viable
alternative funding pathway, source-reported concentration, or non-renewal
risk. Historical World Vision funder names remain unresolved diagnostics.

## Semantic findings

EJA's aggregate grants and cash receipts establish neither a named funding
relationship nor dependency. Its Note 23 establishes only a first-party,
source-reported reliance interpretation. The EJA $621,997 future-project amount
is a commitment/restriction fact, not automatically a broad condition.

Red Cross's `835,006 / 1,059,791 = 0.787897` is reproducible only as a
same-period, Lifeblood-scoped **government-funding category share of
report-stated total revenue**. It is not a single-funder measure, risk score,
threshold crossing or dependency finding. Its funding terms show that award,
receipt, revenue recognition, expenditure and return can be different facts.

Observed funding categories demonstrate an historical mix only. They do not
establish current diversity, diversification strategy, alternatives or
substitutability. Source silence, not processing and insufficient retained
evidence do not mean not dependent.

## §13 / §14 boundary

Section 13 retains source-faithful financial statements, line items, periods,
currency, revenue recognition, expenditure/use and return. Section 14 projects
only evidence-bound funding relationship meanings. The same source may support
both projections, but a §13 financial row cannot create a §14 dependency claim.

## Representation result

Existing `Observation`, `ObservationTime`, scope, evidence, lineage,
`RelationshipStatement` `funder`/`deliverer` roles and `CoverageInput` are
reused. `FundingSourceObservation` remains historical v0.5 category support;
it is not a relationship/dependency contract.

The bounded Builder vocabulary adds atomic v0.2 §14 observations bound by a
shared `funding_context_id`: instrument, stage, restriction, condition, amount,
concentration measure, source-reported dependency, observed diversity,
source-reported diversification/alternative, and unresolved-party mention. It
does not add recipient or intermediary roles because the retained cohort has no
concrete bound case. It does not create a dependency assessment predicate or a
universal concentration threshold.

The deterministic adapter preserves subject, scope, time, source role,
locators, source-record IDs, lineage, coverage, claim basis and semantic role;
it projects only to v0.2 §14. Concentration requires numerator, denominator,
method and result. Source-reported dependency requires source interpretation and
an exact detail. `governed_assessment` is rejected because no governed rule
exists.

## Adversarial review

A separate Terra review required the shared funding-context binding and rejected
all receipt-to-dependency, category-to-party, restriction-to-condition,
composition-to-alternative and silence-to-non-dependency shortcuts. The final
tests prove a stage remains §14-only, a deterministic measure remains distinct
from a source-reported dependency claim, unrelated observations cannot bind
`CardEvidence`, and `not_processed` remains non-negative coverage.

## Decision

**Section 14 remains `PARTIAL`.** Architecture can now carry bounded funding
meanings and honest unknown dependency. The empirical corpus still does not
support a governed dependency assessment, resolved funding relationship,
intermediary, viable alternative, or general concentration-risk claim.

This tranche made **0** provider calls, source acquisitions, semantic
executions, candidate generations, promotions, runtime mutations, Top-100
executions and Phase 6 reopenings. It does not authorize §13 finance work or
any subsequent Tranche C action.
