# CharityGraph Implementation Plan

**Status:** Active implementation sequence  
**Version:** 1.1-draft  
**Updated:** 2026-08-23

## 1. Scope and governing outcome

This plan implements Builder vNext as a Python-controlled, LLM-powered corpus builder while protecting immutable public contract 0.5. It is deliberately sequenced to learn the real economics of model-assisted extraction before building a large local-NLP or governance framework.

The protected model budgets are pooled totals:

| Cohort | Order | Paid-model cap |
| --- | --- | ---: |
| first 100 charities | highest total donations | AUD 100 |
| next 1,000 charities | next highest total donations | AUD 100 |
| next 10,000 charities | next highest total donations | AUD 100 |

The caps include text/vision extraction, judgement, writing, embeddings, retries and escalations. Total donations is used only as `donor_decision_exposure_proxy`; it is not a donor count or quality measure.

Every PR is bounded, tested and reversible. Use Luna-High for implementation when this plan and the typed contracts fully determine the work. Escalate to Terra-High only for unresolved architecture or semantic-policy decisions, not by default.

## 2. PR 1A — documentation economics amendment

**Recommended model:** Luna-High

Update the existing Builder and Data product-documentation PRs with this versioned amendment. Install `LLM_ECONOMICS_AND_COHORT_POLICY.md`, update the active architecture/product/plans/tests/handoff and mark the previous enrichment-economics design superseded where it conflicts.

Do not add code, call a model, create a database, mutate archives, change a public schema/release or deploy.

**Gate:** active-document/link/brand checks; Builder 119-test baseline; Data examples; immutable 0.5 checksum unchanged.

## 3. PR 2 — minimum knowledge, task and economics contracts

**Recommended model:** Luna-High; Terra-High only for a genuine contract ambiguity

Implement only the contracts needed for a model-assisted spike:

- minimum `SubjectRecord`, `SourceRecord`, `EvidenceFragment`, `CandidateObservation`, `DecisionRecord`, `CanonicalObservation` and `DerivativeArtifact` envelopes;
- `ModelTask`, `ModelResult`, `EmbeddingResult`, `TaskRun` and separately validated logical outputs;
- `BudgetCohort`, `donor_decision_exposure_proxy`, `PricingSnapshot`, `CostReservation`, `CostLedger` and `RunManifest`;
- canonical serialization, typed IDs and cache identity;
- provider-neutral interfaces and fakes; no real provider call.

Do not attempt the complete domain ontology or import archives.

**Gate:** schema round trips; stable hashes; material cache changes invalidate; cost dimensions include every paid output category.

## 4. PR 3 — thin SQLite operational ledger

**Recommended model:** Luna-High

Implement SQLite behind a narrow interface for:

- task and physical-batch state;
- idempotency and duplicate prevention;
- cache hit/validity metadata;
- cost reservations and actual reconciliation;
- attempts, retry state, leases and resume;
- durable artefact locations and hashes.

Knowledge remains in durable typed files. SQLite is not expanded into a domain database before evidence requires it. Provide migrations, integrity checks and deterministic reindex of evidentiary rows.

**Gate:** injected-failure rollback; process-death recovery; hard budget cap; deletion/rebuild loses no durable evidence.

## 5. PR 4 — scheduler, batching and fake provider

**Recommended model:** Luna-High

Implement Python orchestration that:

- ranks an approved cohort and selects pending logical tasks;
- groups compatible work by provider, model snapshot, schema and prompt/policy version;
- uses provider batch processing for independent asynchronous requests where advantageous;
- optionally bundles logical tasks for one subject while preserving separate validation and lineage;
- forbids multi-subject bundling until contamination is benchmarked;
- reserves estimated AUD cost before submission and reconciles actual usage after completion;
- retries safely, resumes incomplete batches and prevents duplicate paid requests;
- stops scheduling before the cohort cap is exceeded.

**Gate:** fake-provider simulations cover cache hits, partial batch failure, late completion, retry, overspend attempt, FX/pricing change and rerun idempotency.

## 6. PR 5 — bounded real-model economics spike

**Recommended model:** Luna-High for code; ChatGPT/product approval for task and spend design

Run 10–20 representative charities selected from the existing evidence archive. Use a separately approved micro-budget that is recorded against, but does not silently consume, a production cohort cap.

Exercise all intended paid-output classes:

- difficult page/region recovery;
- relevance judgement;
- typed extraction and semantic interpretation;
- participation/fundraising/ethos/context classification;
- bounded card writing from accepted observations;
- embeddings of stable derivative text.

Compare single-task requests with safe same-subject task bundling and provider batch execution. Publish nothing.

**Gate:** reproducible cost/yield report, validated cache reuse, unsupported-claim and recoverable-recall measurement, documented routing defaults.

## 7. PR 6 — LLM-powered end-to-end vertical slice

**Recommended model:** Luna-High after spike decisions are fixed

Complete one path from existing source material through evidence, model candidates, policy/fixture decisions, canonical observations, coverage, writing and embeddings to a fixture-only 0.5 projection.

The slice must prove that model output can be accepted by an explicit automation policy without being labelled human-governed. Include targeted human-review fixtures for conflict and sensitive context.

**Gate:** typed lineage, idempotent rerun, independently validated logical outputs and a classified fixture diff.

## 8. PR 7 — read-only archive index and evidence reuse

**Recommended model:** Luna-High

Index existing files in place. Record hashes, type/source family, known subject/run association, privacy class and migration status. Import historical task runs and governed cases only as typed historical evidence; do not auto-promote.

Use the vertical-slice task needs to decide what metadata is worth indexing. Do not build a universal archaeology database.

**Gate:** deterministic inventory, zero source-content mutation, reproducible reindex and no durable output in Temp.

## 9. PR 8 — core descriptive domains

**Recommended model:** Luna-High with Terra-High only for unresolved domain semantics

Implement generic typed observations and task schemas for:

- activities, beneficiaries, programs/services and role-specific geography;
- participation modes and transient opportunities from initial processing;
- ACNC source-native and CharityGraph-native classifications;
- cause centrality;
- ethos and separate service/mission orientation;
- neutral `notable_context`.

Use LLM semantic extraction routinely. Do not insert a custom NER or relevance tier.

**Gate:** domain fixtures, evidence-span validation, explicit coverage and risk-weighted review policy.

## 10. PR 9 — fundraising and shadow registries

**Recommended model:** Luna-High after source-role policies are approved

Implement separate funding-source, standing-practice, campaign and expenditure payloads. Add adapters for approved industry shadow registries and preserve their claim-specific authority. Keep applicable code/fee rules distinct from compliance, member spend or fundraising volume.

**Gate:** identity precision, source rights, amount/scope fidelity, no ROI/effectiveness inference and no forced expenditure point.

## 11. PR 10 — governance, correction and assurance routing

**Recommended model:** Luna-High for implementation; Terra-High only for new policy decisions

Implement decision dispositions, benchmarked automation policies, review sampling, conflict routing, sensitive-claim holds, stronger-model adjudication, correction proposals, challenges, retractions and dependent invalidation.

Assurance is risk-aligned: the first 100 receive proportionately more review/escalation; the next cohorts rely more heavily on benchmarked automation and sampling. Universal human review is prohibited as an implicit acceptance condition.

**Gate:** no model output labelled human; review routes are reproducible; correction propagation invalidates writing, classifications and embeddings.

## 12. PR 11 — first 100 production candidate

Process the highest-total-donations cohort within AUD 100. The candidate should attempt all applicable core domains, writing and embeddings rather than achieve a perfect subset.

**Gate:** hard cap, donor-proxy audit, anti-sparsity acceptance, source-bound claims, quality/risk sample and no public release without separate approval.

## 13. PR 12 — next 1,000 production candidate

Process the next cohort within AUD 100 using proven batching, caching, same-subject bundling and selective escalation. Reuse source-family and prompt caches where valid.

**Gate:** hard cap, coverage and yield targets, sampled review, correction readiness and no material quality collapse by domain.

## 14. PR 13 — next 10,000 production candidate

Process the next cohort within AUD 100 using the economical route, concise evidence packs, cached stable instructions, batch processing and targeted escalation. Record explicit unprocessed/not-found/failed states where the cap prevents further work.

**Gate:** hard cap, national-scale throughput, restartability, cache effectiveness, anti-sparsity targets and auditable routing.

## 15. PR 14 — cutover and public-contract proposal

Only after the three cohort reports:

- propose routine production commands and refresh scheduling;
- propose phase-orchestration deprecation;
- propose any future public schema separately;
- supply migration fixtures and Viewer implications;
- retain the previous valid public release.

## 16. Explicitly deferred

- custom local NER, relevance, taxonomy or summarisation models until total-cost-of-ownership evidence supports one;
- PostgreSQL/distributed workers until local single-writer constraints are observed;
- a graph database;
- a universal human-review gate;
- recommendation, impact, mandate-fit or fundraising-performance models;
- destructive archive reorganisation.

## 17. Cross-cutting constraints

- No active former-brand terminology outside isolated compatibility/history.
- No raw/private evidence, credentials, prompts, responses, runtime state or spend telemetry in Git or public releases.
- No immutable release mutation.
- Budget reserve precedes every paid request; actual cost is reconciled afterwards.
- Cached work is reused only when the complete cache identity still matches.
- Coverage is the objective; provenance, policy, correction and unsupported-claim limits are constraints.
- A high-precision pipeline with trivial output does not pass.
