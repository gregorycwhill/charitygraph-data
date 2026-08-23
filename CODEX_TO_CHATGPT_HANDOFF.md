# CharityGraph — Codex Handoff: LLM Economics Documentation Amendment

**Status:** Active execution handoff  
**Updated:** 2026-08-23  
**Recommended Codex model:** Luna-High

## 1. Task in one sentence

Update the existing Builder and Data product-documentation PRs so that cohort budgets, routine LLM use, Python cost orchestration, coverage-first acceptance, risk-weighted governance and the deferral of custom local NLP become controlling requirements throughout the active document set.

This is documentation-only. Do not implement code or run paid model calls.

## 2. Existing branches and PRs

- Builder branch `charitygraph-product-docs-vnext`, PR #3; current relevant tip includes `f38e208`.
- Data branch `charitygraph-product-docs-vnext`, PR #2; current relevant tip includes `2ad7fe2`.
- Viewer is out of scope.

Update the existing PRs. Do not create replacement PRs unless a branch is unavailable or protected, and report that blocker before proceeding.

## 3. Source packet and authority

The supplied amendment packet contains complete replacement copies or patches for active files under `builder/` and `data/`. Its controlling new source is:

- `data/LLM_ECONOMICS_AND_COHORT_POLICY.md`.

Apply it with the current observation-first documentation already on the feature branches. Do not regress the complete approved Builder target architecture in `ARCHITECTURE.md`.

Where the older `ENRICHMENT_ECONOMICS_DESIGN.md` conflicts, retain it as historical benchmark detail with the supplied supersession notice. Do not spend tokens line-editing all 1,200+ lines.

## 4. Decisions that must survive integration

### Cohort budgets

- first 100 highest-total-donations charities: AUD 100 pooled total;
- next 1,000: AUD 100 pooled total;
- next 10,000: AUD 100 pooled total.

The budgets include text/vision extraction, judgement, classification, writing, embeddings, retries and escalations. Easy subjects may subsidise difficult ones inside a cohort. Cross-cohort transfers require explicit approval.

Total donations is `donor_decision_exposure_proxy`: a processing-priority and assurance proxy only. It is not donor count, retail-donor count, merit, quality, credibility, effectiveness or recommendation.

### Architecture

- Python controls acquisition, hashing, deterministic preparation, joins, evidence selection, batching, scheduling, caching, retries, validation, cost and release compilation.
- LLMs routinely handle difficult OCR/vision, relevance, extraction, semantic judgement, classification, bounded writing and stronger-model adjudication.
- Embeddings are a model-derived output inside the budgets and are cached by stable text hash/model/policy.
- Logical tasks remain separately typed/validated even when a physical request bundles them.
- SQLite begins as a thin task/batch/cache/cost ledger, not a full knowledge database.
- Custom local NER/relevance/taxonomy/summarisation is deferred unless a total-cost-of-ownership benchmark includes Codex build effort, labels/evals, maintenance, drift and operations.

### Governance and product acceptance

- Coverage is the optimisation objective; defensibility is a constraint expressed through evidence, policy, method labels and corrections.
- A model output is never human-governed, but may become canonical under an explicit benchmarked automation policy.
- Human review is concentrated on samples, conflicts, sensitive claims and higher-exposure cases; stronger-model adjudication may replace some review.
- A high-precision pipeline that publishes almost nothing fails.
- Participation remains initial-production scope; shadow registries remain first-class claim-specific sources.
- Public contract 0.5 and its immutable checksum remain untouched.

## 5. File mapping

In Data, update/add:

- `AGENTS.md`
- `DOCUMENT_AUTHORITY.md`
- `PRODUCT.md`
- `PRINCIPLES.md`
- `PUBLIC_COMMITMENTS.md`
- `EXPERIENCES.md`
- `CURRENT_STATE.md`
- `ROADMAP.md`
- `IMPLEMENTATION_PLAN.md`
- `TEST_PLAN.md`
- `CODEX_TO_CHATGPT_HANDOFF.md`
- `LLM_ECONOMICS_AND_COHORT_POLICY.md` (new)
- `ENRICHMENT_ECONOMICS_DESIGN.md` (supersession notice only)

In Builder, update:

- `ARCHITECTURE.md`
- `AGENTS.md`
- `EDITORIAL_POLICY.md`
- `BUILD_AND_PUBLICATION.md`
- `README.md`

Do not modify source code, schemas, fixtures, releases, archives, runtime data, Viewer files or deployment workflows.

## 6. Integration method

1. Confirm each repository worktree and branch state; preserve unrelated/untracked material.
2. Record the immutable 0.5 manifest checksum before changes.
3. Apply the packet semantically against the open feature branches; do not blindly overwrite any newer non-conflicting improvement.
4. Resolve links to the actual sibling-repository layout used by the existing PRs.
5. Lint active documents for conflicting claims, especially “LLM optional/late,” “custom local NLP first,” “human review always,” “additional processing never by donation size,” and “defensibility over coverage.”
6. Run validation.
7. Commit separately in Builder and Data, push to the existing branches and add concise PR comments with validation and source mapping.

## 7. Required validation

- active Markdown local links;
- document authority/status/version consistency;
- active brand lint, respecting immutable compatibility/history exceptions;
- Builder full test suite (protected baseline: 119 passed);
- focused Builder branding/config/data-contract/legacy tests;
- Data public 0.5 schema/example validator;
- no public/private allowlist regression;
- immutable manifest SHA-256 before/after exactly:
  `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

If the baseline has changed on the feature branch, report both the expected and observed count; do not rewrite tests merely to match this handoff.

## 8. Exclusions

Do not:

- implement the task contracts, scheduler, SQLite ledger or provider adapter;
- call any LLM/embedding API or consume a cohort budget;
- acquire or reorganise evidence;
- create runtime/database/cache files;
- change public schemas or immutable release bytes;
- rebuild Data, deploy Viewer or change Pages;
- copy prompts, responses, credentials, spend telemetry or private evidence into Git;
- place durable reports in Temp;
- touch unrelated untracked archaeology or debug material.

## 9. Completion report

Return:

- branch, commit and PR link for Builder and Data;
- exact files added/changed;
- confirmation that all controlling decisions in section 4 are present and no conflicting active language remains;
- tests/checks and results;
- immutable checksum before/after;
- confirmation of no code/schema/release/archive/runtime/Viewer/deployment/model-call change;
- any genuine ambiguity that prevented faithful integration.
