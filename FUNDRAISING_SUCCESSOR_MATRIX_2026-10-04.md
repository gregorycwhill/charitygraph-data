# Fundraising capability and gap matrix — 4 October 2026

**Status:** Active bounded implementation map. It consumes—not reopens—the 287 vocabulary/measurement gate and 288 local review-only integration. It authorises neither acquisition, production ingestion, public contract/release, Viewer work, nor Top-100 scale.

## Reconciled predecessor state

| Repository | Base inspected | Settled predecessor state | Verification |
| --- | --- | --- | --- |
| Data | `1513648` (`origin/main`) | Gate `c5681c0`; original successor record `08f143e`; current local authority/readout `282733f` on `phase5-direct-service-v1.2-closeout` | Gate reports 59 overlapping executions, not a unique-test count. |
| Builder | `2221d4e` (`origin/main`) | Reconciled 288 local review-only tip `279cd8c` on clean `cg-fundraising-publication-288`; code integration `97626d3`, packet `faaa618` | Focused suite at the tip: **55 passed in 2.09s** on 4 October. |

The dirty Builder checkout is not an integration target. Before work, use a fresh worktree and compare its selected base to `279cd8c`; do not replay old 287 patches whose effects already appear in the 288 tip.

## Capability and gap matrix

| Facet / metric | State | Exact seam / settled commit | Tests and retained evidence | Remaining work or blocker |
| --- | --- | --- | --- | --- |
| Evidence-bound standing practice | **Proven, local, review-only** | `src/charitygraph/models.py`, `docs/TYPED_FUNDRAISING_CONTRACT_V1.md`, `src/charitygraph/north_star_projection.py`; `304e490`, retained at `97626d3` | `tests/contracts/test_typed_fundraising_contracts.py` | Persist only governed evidence retaining locator/wording, binding, scope, time, role, coverage and review state. No prose heuristic or public card. |
| Campaign distinct from practice | **Proven, local, review-only** | Same typed seam; `304e490` | Typed-contract separation controls | Candidate campaign-type vocabulary needs cohort pressure before enum/public mapping. |
| Explicit provider relationship | **Proven, local, review-only** | `models.py`; `304e490` | `test_typed_fundraising_contracts.py` rejects inferred providers | No relationship from logo wall/directory/membership; provider-case currentness remains a gap. |
| F2F lifecycle/currentness | **Proven policy and deterministic implementation** | `src/charitygraph/f2f_currentness.py`, `docs/F2F_CURRENTNESS_POLICY.md`; `dccc7ab` | `tests/test_f2f_currentness.py`: current/recent/historical/discontinued/unknown/scoped-nonfinding | No universal freshness age or inferred setting, agency, regular giving or continuity. |
| Native terms and composable facets | **Candidate contract, review-only** | `src/charitygraph/fundraising_vocabulary.py`, `docs/FUNDRAISING_VOCABULARY_V1_CANDIDATE.md`; `3e80813` | `tests/test_fundraising_vocabulary.py` | 30–50-case adversarial vocabulary-pressure review before public mappings. |
| Industry-source promotion | **Candidate/review-only; no ingestion** | `src/charitygraph/fundraising_industry_promotion.py`, `src/charitygraph/semantic_benchmark.py`; `d2dcf2c` | `tests/test_fundraising_industry_promotion.py` | PFRA/FIA/Donor Republic/Funraisin need rights, retention, refresh, republication, identity and time-semantics decisions. |
| Finance compatibility | **Proven policy/local implementation** | `src/charitygraph/finance_measurement.py`, `docs/FINANCE_MEASUREMENT_COMPATIBILITY_V1.md`; `8a93cd9` retained, not reapplied | `tests/test_finance_measurement_compatibility.py`, `tests/test_v05_fundraising_bounds.py` | Preserve entity/period/basis/metric/component treatment; incompatibility stays unavailable. |
| Money-to-practice/campaign/provider linkage | **Proven, local, review-only** | `src/charitygraph/fundraising_money_linkage.py`; `1d7ae85` | `tests/test_fundraising_money_scope_linkage.py` | Link only at exact smallest supported grain; organisation/portfolio finance stays unattributed. |
| Expenditure bounds / derivatives | **Policy proven; real cases incomplete** | `src/charitygraph/fundraising_financial_derivatives.py`; `fe0c0d4`; study `docs/research/FUNDRAISING_MONEY_ATTRIBUTION_GRAIN_STUDY_V1.md`, `research/fundraising_money_attribution_grain_v1.json`; `d35bcd5` | `tests/test_safe_fundraising_financial_derivatives.py`, `tests/test_fundraising_money_attribution_study.py` | Needs lawful real definite/possible/excluded envelopes and checked additivity. No ROI, net proceeds, cost share or causal/effectiveness derivative. |
| Legacy annual expenditure estimator | **Unsafe/retired for new use** | `src/charitygraph/fundraising.py`; cohort change `fc80c0e` | `tests/test_fundraising.py`, `tests/test_bounded_real_charity_fundraising_cohort.py` | `estimate_fundraising`/`CB-FUND-H03` cannot extract or attribute method/campaign money; isolate callers and separately govern any compatibility migration. |
| Local review profile | **Proven, local, review-only** | `src/charitygraph/fundraising_review_projection.py`, `docs/FUNDRAISING_REVIEW_PROFILE_V1.md`, `tests/fixtures/fundraising_review_profile.json`; `97626d3` | `tests/test_fundraising_review_projection.py`, `tests/test_fundraising_cohort_regression.py`; `artifacts/fundraising-cohort-regression-288.json` in `faaa618` | Keep out of public card/release renderers; 24-case regression is coverage control, not production performance. |
| Card-facing projection API | **Candidate local code; public use blocked** | `src/charitygraph/north_star_projection.py`, `docs/FUNDRAISING_CARD_PROJECTION_V1.md`, `tests/test_fundraising_card_projection.py`; `9ebe417` | Projection/contract controls | Needs coordinated Builder/Data/Viewer versioned contract and correction decision. |
| Public schema, release, Viewer and scale | **Blocked** | No enabled production seam | No qualifying cohort/release gate | Needs lawful 30–50-case cohort, independent identity review, measured error classes, finance envelopes, vocabulary review and coordinated approval. |

## Ordered implementation plan

1. If an owner selects a Builder target, compare its clean worktree with `279cd8c`, preserve the review-only boundary, and run the focused 55-test suite recorded in the publication packet.
2. Harden only the persisted-observation boundary: require source locator/wording, binding basis, observed/valid time, scope, production method, review state and coverage; add refusal tests for omitted fields.
3. Inventory and quarantine legacy estimator callers. A compatibility migration must be a separately tested decision and cannot become method attribution.
4. Expand fixture-bound adversarial coverage (negative, cessation, ambiguous binding, scoped silence, incompatible finance and contradiction), reporting denominators and false-positive/false-negative findings.
5. Open source, bounds or public lanes only with their stated decisions. Those blockers do not stop steps 1–4.

## Mandatory failure modes

Use `unknown`, `not_found_in_scoped_source`, `not_processed`, `unavailable` or `null` as appropriate. Never infer practice from generic purpose, donations revenue, legal permission, generic copy, peer priors or PFRA membership alone; never allocate aggregate money; never turn silence or a bound into a point.
