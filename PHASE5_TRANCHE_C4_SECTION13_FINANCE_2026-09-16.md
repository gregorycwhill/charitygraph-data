# Phase 5 Tranche C4 — North Star v0.2 §13 finances retained-evidence semantic and representation test

**Status:** Completed bounded retained-evidence semantic and representation test; no execution authority.
**Date:** 16 September 2026. **Active projection:** `north-star-v0.2`.

## Question, fixed starting point and boundary

Can source-faithful finance knowledge be projected to §13 while retaining reporting scope, period, currency and scale, statements and source rows, accounting and cash-flow distinctions, assurance, restrictions/reserves, comparatives and reconciliation? The controlling rule is: **accounting and cash-flow concepts remain distinct even where they concern the same money.**

The starting commits were Builder `1cd1c3960124efd203161038bcbd6d6402a4a660` and Data `9a854c3df1c1fe04d0c71e03dffd165290dd6217`. This test did not acquire, refetch or transmit a source; it did not create candidates, governed knowledge, public-v0.5 changes or runtime data.

## Frozen minimum cohort

All four cases are required. Removing any one loses a distinct semantic pressure, so no larger cohort was needed.

| Case and retained artefact | Irreducible pressure |
|---|---|
| Environmental Justice Australia FY2024–25, `archive/processed/phase2b/2026-08-14/report-extracts/74052124375-EJA-Financial-Report-2024-25.json` | Individual-entity accounts, AUD functional/presentation currency, source rows, cash-flow rows, accounting policy, future-project commitment that is not a liability, and a bounded refund label. |
| Australian Red Cross Society FY2022–23, including Lifeblood, `archive/processed/reality-spike/2026-08-10/report-extracts/50169561394-2022-23-financial-pages.json` | Society/group versus operating-division scope, grants, receipts, recognition, expenditure, return liability, pledges, specific-purpose funds and subtotal/total non-comparability. |
| APNIC Foundation FY2025, `archive/processed/phase2b/2026-08-14/report-extracts/24646643156-a2a8898a4f64ceade90b63f11bb3939a63c992b7e4c21a00c9c6ed7a86fb5e60.json` | Functional/presentation-currency change, transformed comparative, translation reserve, accrual basis and actual independent auditor opinion. |
| Fitted for Work FY2024 comparative and AIS FY2023, `archive/processed/reality-spike/2026-08-10/report-extracts/78126256862-2023-24-full.json` and `archive/processed/reality-spike/2026-08-10/financial-reconciliation-findings.md` | One-dollar presentation/precision difference without substantive divergence. |

## Primary Terra adjudication

`ACCEPT` means a bounded source-faithful §13 proposition; `NARROW` means the source supports only the stated qualified meaning; `REJECT` means the proposed shortcut is unsupported; `KNOWABILITY_ONLY` means the retained universe supports an honest coverage state only.

| ID | Retained proposition and exact locator | Disposition | §13 role and boundary |
|---|---|---|---|
| E1 | EJA is an individual entity; FY ended 30 June 2025; AUD functional and presentation currency — EJA p. 5 (financial-report p. 1). | ACCEPT | Reporting entity/scope, period and monetary basis; first-party financial-report fact. |
| E2 | EJA P&L prints grants `$2,078,583`, total income `$5,016,000`, employee benefits expense `($4,670,344)` with 2024 comparatives — EJA p. 12 (financial-report p. 8). | ACCEPT | Source-native statement rows, current/comparative amounts, AUD unit `$`; not a named funder, fundraising method or cash-flow claim. |
| E3 | EJA cash-flow statement prints receipts `$4,956,356` and supplier/employee payments `($5,667,110)` — EJA p. 15 (financial-report p. 11). | ACCEPT | Receipt/payment source rows, separately typed from E2 recognition/expense rows. |
| E4 | EJA policy: enforceable/sufficiently-specific arrangements may create a contract liability and revenue only as obligations are satisfied — EJA pp. 16–17 (financial-report pp. 12–13). | NARROW | First-party accounting-policy assertion, not proof that any individual grant was recognised, paid, received or performed. |
| E5 | EJA `621,997` future-project funds are committed but not liabilities because no enforceable/sufficiently-specific obligation — EJA p. 28 (financial-report p. 24), Note 21. | ACCEPT | Commitment at individual-entity/FY25 scope; explicitly not liability or recognised-revenue shortcut. |
| E6 | EJA PLSLA `Refund (20,520)` appears in provisions — EJA p. 25 (financial-report p. 21), Note 12. | NARROW | Source row has a refund label; it does not establish a cash payment or completed refund stage. |
| R1 | Red Cross reports total government funding `$835,006,000`, displayed total revenue `$1,059,791,000`, and distinct gain on assets/investments `$44,841,000` — ARC p. 57. | ACCEPT | Group-level source rows in `$'000`; generic government category is not a named funder or dependency. |
| R2 | ARC report subtotal `$1,014,950,000` excluding the separate gain matches AIS, while the displayed total includes it — `financial-reconciliation-findings.md`. | ACCEPT | `non_comparable`, not divergent; source-row/subtotal/total definitions remain separate. |
| R3 | Lifeblood is a separate operating division; the Society statements include it; cessation under its Deed is not expected to affect the remainder — ARC p. 55. | NARROW | Division-scoped fact and group-report context only. It cannot become whole-Society finance or a durable funded-relationship assertion. |
| R4 | Lifeblood output funding: excess FY23 `$7.603m` is returnable and recorded as a liability; capital funding can be carried forward — ARC p. 64. | ACCEPT | Division-scoped return/liability and recognition facts; return is not payment, and the funding arrangement is not a dependency conclusion. |
| R5 | ARC says grant expenditure may not correlate with timing of grant receipts — ARC p. 63. | ACCEPT | First-party accounting-policy fact proving receipt, expenditure and recognition cannot be collapsed. |
| R6 | Donations for specific purposes transfer to a separate equity fund after profit-or-loss recording; pledges are not revenue until cash receipt — ARC p. 64. | ACCEPT | Restriction/fund and receipt/recognition distinctions; neither establishes dependency or fundraising method. |
| A1 | APNIC changes functional and presentation currency AUD→USD; functional change is prospective, the 2024 comparative is translated to USD, and translation differences accumulate in a reserve — APNIC p. 34 (annual-report p. 32). | ACCEPT | Comparative transformation, not accounting-error correction. Transformed 2024 values are not untouched same-basis historical amounts. |
| A2 | APNIC statements are accrual-basis general-purpose accounts — APNIC p. 34. | ACCEPT | First-party accounting-basis fact, scoped to company/FY25. |
| A3 | PKF independent auditor report audits APNIC FY25 financial report and gives the stated opinion — APNIC p. 41 (annual-report p. 39). | ACCEPT | Source fact about explicit assurance context and opinion; annual-report presence alone would not suffice. |
| F1 | Fitted FY24 report gives FY23 total income `$4,081,571`; AIS gives `$4,081,570` — reconciliation finding and Fitted p. 27 (annual-report p. 51). | ACCEPT | `precision_consistent` candidate, not a substantive divergence or silently-selected scalar. |
| X1 | “Government grants identify the NBA/funder.” | REJECT | Generic category does not name a funder; ARC named NBA context remains separately scoped and does not attach to every row. |
| X2 | “Restricted/specific-purpose funds, a category share, or a commitment establish dependency.” | REJECT | §14 conclusion, prohibited absent its own evidence and contract. |
| X3 | “No retained correction/restatement means no corrections exist.” | KNOWABILITY_ONLY | Retained corpus has no strong accounting-error/revision case; use honest `not_processed`, `not_reviewed`, `unknown`, etc., never zero/absence. |

Counts: **ACCEPT 11; NARROW 3; REJECT 2; KNOWABILITY_ONLY 1.**

## Resource-flow, scope and comparative conclusions

| Concept | Retained evidence | Existing/added representation result |
|---|---|---|
| Award | No sufficiently bounded §13 award case retained. | `KNOWABILITY_ONLY`; a §13 stage can be explicit if evidenced, but §14 `FundingStage` is not reused. |
| Commitment | EJA Note 21. | Explicit §13 `commitment`; must not become liability/revenue. |
| Payment | EJA cash-flow rows. | Explicit §13 `payment`; not expense. |
| Receipt | EJA cash-flow rows; ARC pledge policy. | Explicit §13 `receipt`; not revenue recognition. |
| Revenue recognition | EJA/ARC accounting policy. | Explicit §13 `revenue_recognition`; policy remains source-attributed. |
| Expenditure/use | EJA P&L and ARC policy. | Explicit §13 `expenditure_or_use`; not payment. |
| Refund/return | ARC excess-funds liability; EJA refund label. | Explicit §13 `refund_or_return`; a liability/label does not prove cash completion. |

`Financials`, `FinancialStatementObservation`, `FinancialStatementRow`, `FinancialPeriod`, `MoneyObservation`, `FinancialMetricSet`, `SourceNativeRecord`, generic `Observation`/scope/time/evidence/lineage, and card coverage are reused. The C4 adapter adds only one atomic v0.2 §13 projection input. It requires scope and reporting/attribution metadata; an operating-division proposition requires `division_reported` or `explicit_allocation`, while division attribution is rejected for organisation scope. This mechanically prevents Lifeblood evidence from becoming whole-Society evidence.

APNIC’s retrospective translated comparative is a **comparative transformation**, distinct from ordinary comparative, correction and revision. `MoneyObservation` already prohibits implicit FX and preserves source amount, currency, scale, raw value and precision. Red Cross and Fitted require reconciliation status to remain respectively `non_comparable` and `precision_consistent`.

## Representation inventory and adversarial result

| Concept | Classification | Result |
|---|---|---|
| Monetary observation; period; statement, row, metric and comparative; scope/consolidation; reconciliation | `ALREADY_EXPLICITLY_REPRESENTABLE` | Existing finance models preserve them; C4 projects their bounded §13 meaning. |
| Accounting basis; restrictions/funds/reserves; source-native policy text | `REPRESENTABLE_WITH_EXISTING_GENERIC_PRIMITIVE_WITHOUT_LOSS` | C4 requires source detail, role, locator, record, lineage and time. |
| Assurance context; §13 resource-flow stage; comparative transformation | `NOT_EXPLICITLY_REPRESENTABLE` before C4 | C4 adds narrow typed v0.2 predicates, not a finance mega-record. |
| Corrections/revisions/restatements | `AMBIGUOUS` | No retained accounting-error case. Existing supersession/coverage can express unknown or later correction lineage, but no first-class §13 correction/revision contract is added on speculation. |
| Missingness | `ALREADY_EXPLICITLY_REPRESENTABLE` | C4 maps non-positive states, including `processing_failed` and `not_attempted`; it rejects asserted absence. |

Independent adversarial review required: stage is confined to §13 and typed separately; commitment/receipt/expenditure/return cannot share a shortcut; a generic grant category has no named-funder field; restriction has no dependency predicate; division attribution requires division scope; derived calculations require method, operands and deterministic basis; and assurance requires explicit source-reported assurance kind and detail. Card evidence is bound to §13 and has no automatic §8 or §14 assignment. Historical v0.1 has no numeric/semantic assignment path.

## Decision and residuals

Cluster dispositions: reporting scope/period/currency **SUPPORTED_BY_EXISTING_PROOF**; statements/rows/metrics/comparatives **SUPPORTED_BY_EXISTING_PROOF**; reconciliation/derived calculations **SUPPORTED_BY_EXISTING_PROOF**; resource-flow stages **SUPPORTED_BY_EXISTING_PROOF**; restrictions/funds/reserves **SUPPORTED_BY_EXISTING_PROOF**; assurance **SUPPORTED_BY_EXISTING_PROOF**; revisions/corrections/transformations **PARTIAL**; missingness **SUPPORTED_BY_EXISTING_PROOF**.

**§13 remains `PARTIAL`.** The representation residual is limited to a future evidence-bound correction/revision/restatement contract if a positive retained case justifies one; no representation change is warranted now. The empirical residual is the absence of a retained accounting-error/revision case, a bounded individual award, universal audit coverage/opinion variety, and broader tested reporting-scope/flow coverage. No new source or provider work is shown necessary before any cheaper retained-evidence action.

Recommended product-owner action: accept this bounded §13 representation and `PARTIAL` disposition, then decide separately whether a correction/revision pressure case merits a future retained-evidence test. Do not begin that action here.

Provider calls: `0`. Source acquisitions: `0`. Semantic provider executions: `0`. Candidate generation: `0`. Promotions: `0`. Canonical runtime mutations: `0`. Top-100: `0`. Phase 6 reopening: `0`.
