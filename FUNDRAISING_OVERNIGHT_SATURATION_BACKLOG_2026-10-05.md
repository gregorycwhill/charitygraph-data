# Fundraising overnight saturation backlog — 5 October 2026

**Status:** Active bounded backlog.  This sequences local engineering and
research-preparation only; it neither authorises source acquisition,
production ingestion, public contracts/releases, Viewer work, nor population
scale.

**Authority consumed:** the 290 Builder bounded-scale readout (`98c967e`,
amended by `fab22d5`), the Builder scale readout (`5424296`), this repository's
scale/error register, and the 287/288 successor matrix.  The 290 cohort has
50 deterministic fixture cases, zero source retrievals and zero provider
calls.  It is explicitly `local_review_only_fixture`, so its 50/50 fixture
descriptors and adjudication labels do not satisfy the independent,
source-backed 30–50-case gate.

## Gate decision

**Scale gates remain closed.**  The 290 run increased adversarial regression
coverage (35/50 observed practice fixtures, 25/50 available money fixtures,
5/50 ambiguous/unresolved binding refusals, 2/50 incompatible-finance
refusals, and 0/25 share-or-bounds outcomes), but it did not add lawful source
evidence, independent identity adjudication, source-family rights decisions,
or real finance envelopes.  Therefore this tranche must close deterministic
and evidence-packet blockers rather than broaden the cohort or project a
public surface.

## Ranked executable backlog

| Rank | Work item and bounded deliverable | Evidence basis / value | Acceptance checks | Explicit non-goal and predecessor disposition |
|---|---|---|---|---|
| 1 | **Real-source cohort-packet validator.** Add a Builder-local, non-acquiring schema/validator for a manually retained candidate packet. Require source identity/role, exact wording or locator, subject-binding basis, observed/valid time, scope, production method, review status, coverage, rights disposition, and assertion-level adjudication. Emit separate denominators for practice, F2F currentness, campaign/provider, finance compatibility and money linkage. | The critical missing gate is not another fixture: it is a 30–50 independently identity-adjudicated, source-backed packet. The present runner accepts fixture handles as descriptors; a validator can make the eventual packet reviewable and fail closed without retrieving a source. | Tests reject missing locator/wording, binding, time/scope, coverage, rights state, review disposition, incompatible finance dimensions, and aggregate money linkage. Tests retain `unknown`, `not_found_in_scoped_source`, `not_processed`, `unavailable`, `ambiguous_binding`, and `incompatible_finance`. A generated empty/template packet is labelled `not_processed`, not evidence. | Do not retrieve, retain, ingest, or publish any new source. Do not repeat 290's 50-case fixture expansion (`98c967e`/`fab22d5`); it is the regression input the validator must distinguish from a source-backed packet. |
| 2 | **Retire the remaining generic legacy-estimator call path.** Replace or isolate the `pipeline.py` call to `estimate_fundraising` behind a compatibility-only adapter that can return only direct source-native disclosure or explicit `not_yet_processed`; document the legacy output boundary and add a caller inventory test. | The scale register quarantines `estimate_fundraising`/`CB-FUND-H03`. The unsafe component-label heuristic was removed in `fc80c0e`, but the sole production-path call remains in `src/charitygraph/pipeline.py`. This is a concrete deterministic defect, independent of external evidence. | Search-based or import-level test inventories every callable reference; generic marketing/PR/event/donor-acquisition labels produce no amount; direct disclosure retains period/entity/basis/grain; cards expose coverage rather than a manufactured estimate. Focused fundraising/pipeline tests pass. | Do not reintroduce `CB-FUND-H03`, method attribution, reconstruction, bounds, or finance allocation. Do not duplicate the heuristic-removal work already completed in `fc80c0e`. |
| 3 | **Assertion-level error ledger from packet validation.** Extend the local report format to tally retained, edited, rejected and refused assertions by source role and error class: identity/binding, F2F status/time, scope, campaign/practice, provider direction/time, finance entity/period/basis, and exact-grain linkage. | Both the 24-case and 50-case reports count controls but explicitly do not measure real-world precision, false negatives, or per-assertion error. A ledger is required before a human-reviewed packet can demonstrate that precision dominates recall without concealing a failure class. | Fixture/template tests prove overlapping assertions do not become a unique-case denominator; contradiction, cessation, scoped silence, ambiguity, finance-only, incompatible finance and aggregate-money controls each yield a named class; report has no aggregate “pass rate” that masks any class. | No numerical quality threshold is invented and no fixture rate is called external precision/recall. Do not redo the current 290 aggregate counters. |
| 4 | **Finance evidence-envelope preflight.** Define/validate a source-row envelope for direct disclosure and deterministic reconstruction: reporting entity, period, basis, metric/flow meaning, gross/net treatment, components, denominator and additivity outcome. Reject a bounds/share candidate unless all definite/possible/excluded components and its legal/source status are explicit. | 290 has 25 money-available fixtures but 0/25 share-or-bounds. The existing compatibility and derivative policies are sound; this closes the packet-format gap that otherwise invites an unsafe point estimate. | Direct organisation-level finance remains available but unattributed; mismatched entity/period/basis is `incompatible_finance`; incomplete envelopes are `unavailable`; no derived share, net proceeds, ROI or effectiveness field can be emitted. | Do not manufacture a “real” bounds case, change the direct > reconstruction > bounds > unavailable ordering, or reopen the existing finance contract/unit-test work. |
| 5 | **Rights and source-family decision-record template (research only).** Produce a per-family decision form for the ordered surfaces already mapped: charity reports/statements, first-party practice/campaign pages, regulator disclosure, platforms, providers, PFRA/industry, trade/awards, and search inventories. | Rights, retention, refresh, republication, identity and time semantics are the prerequisite common to any future real-source packet. The source-discovery map supplies the order and current disposition but not a reusable auditable decision record. | Each form requires terms/rights evidence, allowed retention/republication, refresh expectation, source role, binding method, time semantics, owner/reviewer disposition and an explicit `blocked_by_rights` outcome. Default is research-only/no acquisition. | Do not treat a template as rights clearance or promote PFRA/FIA/Donor Republic/Funraisin/provider/platform material; those lanes remain quarantined. |

## Sequencing and stop rules

Run ranks 1–4 in a single clean Builder worktree because they share the
cohort/finance model boundary; rank 5 may be documented in Data independently.
After each rank, rerun the existing focused fundraising suite and the 290
fixture regression as a regression control only.  Record the selected base,
commit(s), tests and changed packet version.

Stop the tranche after rank 5, or earlier only for a genuine source-rights or
product-owner decision.  A completed validator/template does not open source
retrieval.  If no independently adjudicated, rights-cleared source packet is
provided, the correct final state is `not_processed`/research-only, not an
attempt to fill the cohort from public pages.

## Deliberately excluded as duplicate or gated work

| Item | Why it is not in this backlog |
|---|---|
| Another 30–50/50-case fixture expansion, F2F policy fixtures, or aggregate report rerun | Completed in the 290 local fixture cohort (`98c967e`, `fab22d5`); re-running may verify regressions but cannot advance the external gate. |
| Typed practice/campaign/provider/F2F/finance/money-linkage contracts | Implemented and retained as local review-only predecessor work; the current gap is source-backed adjudication and packet evidence, not a new semantic axis. |
| Public card API, Data schema/release or Viewer integration | Explicitly blocked pending the source-backed cohort, rights and coordinated cross-product decision. |
| PFRA/FIA/Donor Republic/Funraisin, provider/platform or trade-source ingestion | Quarantined/research-only pending per-family rights and time/identity semantics. |
| Bounds, share, ROI, cost-to-raise-$1, net proceeds, attribution or causal metrics | 0/25 share/bounds in 290 and the governed product boundary prohibit generic derivation. |
| Top-100/population completion claims | Neither local fixture denominator is a charity, page, independent identity, prevalence or representative sample. |

## Evidence handoff required to reopen scale

The next scale decision needs a packet accepted by rank 1 and independently
reviewed for 30–50 real, rights-cleared, source-backed cases. It must retain
the source-native material/locator and binding evidence; report assertion and
case denominators separately; include cessation, contradiction, ambiguous
binding, scoped silence, campaign/practice separation, provider ambiguity,
finance-only, incompatible-finance and aggregate-money non-attribution cases;
and report edits/rejects/refusals without hiding a failure class. Until then,
all capabilities remain local review only or quarantined exactly as stated in
the scale/error register.
