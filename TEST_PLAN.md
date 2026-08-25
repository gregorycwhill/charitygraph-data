# CharityGraph Builder vNext Test and Evaluation Plan

**Status:** Canonical validation strategy, version 2.0-draft

## 1. Objective

Tests must demonstrate not only that code executes, but that CharityGraph produces useful coverage with defensible mechanical lineage at controlled cost. The plan therefore combines software invariants, semantic evaluation, reality cohorts and publication boundaries.

## 2. Test layers

| Layer | Purpose | Network/model policy |
|---|---|---|
| Unit | Pure validation, identifiers, mappings, calculations | None |
| Contract | Lifecycle, provider, ledger, schema and lineage invariants | Fake/recorded only |
| Persistence | SQLite migrations, constraints, replay, concurrency assumptions | Local file-backed DB |
| Connector fixture | Known source responses and failure modes | Recorded/local fixtures |
| Golden semantic | Expected extraction/classification on fixed cases | Recorded outputs or pinned evaluation run |
| Holdout semantic | Detect overfitting and abstention | Pinned real model under approved budget |
| Vertical slice | Whole private cohort from evidence to preview | Controlled acquisition/model calls |
| Release boundary | Manifest, schema, brand, licence, privacy and immutability | Deterministic |

## 3. Non-negotiable invariants

Tests must cover:

- append-only observations and cache events;
- exact directed lineage for promotion, review and supersession;
- one current running attempt and rejection of stale completion;
- cohort/run/task and reservation scope integrity;
- signed reservation/actual/credit reconciliation;
- valid overruns and explicit unreserved actuals;
- idempotency without fabricated metadata;
- material artefact metadata checks;
- safe relative paths and content hashes;
- no in-memory production SQLite catalogue;
- source/evidence references cannot point to absent artefacts;
- public projection cannot expose restricted content;
- contract 0.5 remains byte-identical.

## 4. Semantic evaluation

For each model-assisted task, freeze:

- task schema and prompt/template version;
- scheme/concept versions;
- development examples;
- untouched holdout examples;
- evidence available to the model;
- expected acceptable labels/ranges;
- risk-weighted failure definitions;
- maximum unjustified-abstention rate;
- token/cost budget.

Evaluation recognises that multiple classifications can be reasonable. Gold data may specify required, acceptable-secondary and prohibited assignments rather than a single essay-answer key.

## 5. Required useful-judgment tests

Include clear cases where adequate evidence should lead to a classification. A result of `unknown` fails when a reasonable primary or secondary assignment was available within the task's risk policy.

For a richly evidenced major charity, the system should generally produce supported program, permitted external/native taxonomy and SDG assignments after its approved retrieval/model budget. CLASSIE assignments are optional and rights-gated; when unavailable, the non-CLASSIE build must remain valid. It must not abstain merely because a specialist could debate the exact boundary of a broad sustainability or social-purpose concept.

Also include genuinely insufficient-evidence cases where decisive classification would be fabrication.

## 6. Coverage-state tests

Test distinct representation and reporting of:

- resolved/supported;
- contradicted;
- unknown/insufficient evidence;
- not applicable;
- not attempted;
- withheld;
- acquisition failure;
- extraction/model failure.

Missing values must not collapse these states.

## 7. Reality cohort and holdout

The first cohort covers the profiles in `IMPLEMENTATION_PLAN.md`. Partition it before implementation:

- development cases may guide code and prompts;
- holdout cases are opened only for the formal evaluation run;
- after holdout failure, classify the error before changing anything;
- do not add a keyword or exception solely for that organisation;
- material prompt/model changes require a new evaluation version.

Retain evidence and evaluation artefacts by content hash so a rerun does not create a second archaeology pile.

## 8. Initial acceptance scorecard

Before paid evaluation, the reviewer-approved development benchmark must have
enough evidence-backed cases to compute every applicable frozen threshold. An
insufficient denominator blocks that task family; labels are not manufactured
to make a score computable. The operational-activity reference must cover the
frozen 6/7 development requirement and the SDG reference must cover the frozen
5/7 adequately-evidenced requirement. Insufficient evidence is a valid
benchmark state, and CLASSIE semantic scoring remains rights-gated.

Exact numeric thresholds should be frozen in the PR design packet after inspecting the cohort, but the scorecard must include:

- subject/scope correctness;
- program precision and material-program recall;
- evidence-locator validity;
- permitted external/native taxonomy and SDG required, acceptable and prohibited assignments;
- CLASSIE-off publication and derived-object invalidation without loss of independent knowledge;
- unjustified abstention;
- unsupported assertion rate;
- provenance-floor completion;
- cache/replay correctness;
- total and per-task cost;
- human-review demand;
- development/holdout gap.

No aggregate score may mask a critical lineage violation or high-consequence false assertion.

## 9. Correction and community tests

Before public correction launch, test:

- proposal identity and duplicate handling;
- evidence attachment and privacy controls;
- all governed dispositions;
- accepted-with-edit exact lineage;
- prior-release history remains accessible;
- rejected/upheld challenges do not mutate canonical data;
- contributor attribution/withdrawal rules;
- correction latency reporting.

## 10. Scale and economics tests

Before cohort expansion:

- dry-run task counts and reserved spend;
- simulate provider errors, timeouts and retries;
- verify hard/soft budget stops;
- validate cache hit/miss reasons;
- sample all cohorts including the right tail;
- report coverage and error disparity by cohort;
- ensure model payload and artefact storage growth is sublinear under reuse where expected.

## 11. Regression policy

Every corrected systematic error adds the smallest representative regression case. Do not preserve accidental implementation details. Deprecation warnings, nondeterminism and flaky network tests are treated as maintenance work rather than normal noise.

## 12. Stop rules

Stop an implementation tranche and return to design when:

- the same conceptual mismatch survives two bounded correction attempts;
- satisfying a new example requires unbounded phrase-specific logic;
- subject/scope semantics are unclear;
- source rights or authority are unresolved;
- costs cannot reconcile;
- holdout performance materially diverges from development performance;
- the proposed change would alter contract 0.5;
- a high-risk claim lacks an approved review path.

## 13. Release-candidate tests

Future vNext publication additionally requires:

- schema/example and negative contract tests;
- manifest checksum and traversal safety;
- reproducible clean build;
- coverage/limitations generation;
- licence and attribution validation;
- active-brand lint while preserving necessary historical identifiers;
- privacy and restricted-body scan;
- Data/Viewer compatibility;
- HTTP, canonical URL, robots and sitemap checks;
- rollback and previous-release resolvability.
