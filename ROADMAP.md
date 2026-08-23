# CharityGraph Product Roadmap

**Status:** Canonical capability roadmap  
**Version:** 1.0-draft  
**Updated:** 2026-08-23

## 1. Roadmap principle

CharityGraph is one product delivered through Builder, Data and Viewer. Work is sequenced by user capability and dependency, not repository ownership or former phase labels.

The public goal is a national, structured and governed charity-data layer. Progressive coverage is acceptable; hidden ambiguity, destructive migration and unsupported claims are not.

## 2. Protected foundation — complete and ongoing

- Maintain the immutable public 0.5 release and its checksum.
- Maintain the live static Viewer and machine-discovery routes.
- Keep Builder's full regression baseline green.
- Preserve source-native ACNC/AIS/DGR evidence, financial fidelity and compatibility tests.
- Keep raw/private archives and runtime state outside Git and public releases.

## 3. Phase 1 — product and architecture authority

**Outcome:** one internally consistent active documentation set and an implementation-ready Builder architecture.

- Adopt the canonical product, principles, public commitments and experiences.
- Establish documentation authority and historical separation.
- Reclassify public contract 0.5 as implemented compatibility, not future design.
- Amend Builder target architecture with `SubjectRecord`, scope/relationships, corrections, evaluation economics, distribution and operational recovery.
- Align Builder/Data agent instructions.
- Establish terminology: `subject_id` internally; cards as release projections.

**Gate:** no active authority conflict, no active former-brand terminology, green baseline and unchanged 0.5 checksum.

## 4. Phase 2 — Builder foundation

**Outcome:** a no-data-mutation Builder vNext skeleton.

- Create module boundaries for subjects, sources, evidence, candidates, decisions, observations, coverage, derivatives, evaluation and releases.
- Define typed IDs, schema versioning, canonical hashing and lineage contracts.
- Implement SQLite migrations behind a narrow catalogue interface.
- Define task/run state, idempotency, retries, leases, resume and crash recovery.
- Prove durable knowledge can rebuild the evidentiary catalogue.
- Add no-op CLI surfaces and fixture-only tests.

**Gate:** database deletion/reindex tests, migration tests and no public-output change.

## 5. Phase 3 — read-only evidence index

**Outcome:** the existing evidence treasure trove becomes queryable without being reorganised.

- Index source blobs, source records, extracts, governed decisions, model runs and historical releases in place.
- Verify hashes and record migration status.
- Produce explicit wrapper-required, importable and quarantined classifications.
- Preserve privacy and source rights.

**Gate:** deterministic inventory, zero source-content mutation and reproducible reindex.

## 6. Phase 4 — deterministic structured vertical slice

**Outcome:** one authoritative source flows through the complete vNext model and reproduces or explains the public 0.5 boundary.

- Source record and durable subject binding.
- Evidence and deterministic candidates.
- Policy or fixture decision and canonical observations.
- Coverage assessments.
- Program and participation observations where present in source data.
- Financial/source-native preservation where applicable.
- Release projection through the explicit 0.5 adapter.

**Gate:** typed lineage, idempotent rerun, controlled diff and unchanged immutable release.

## 7. Phase 5 — program, participation and web/document evidence

**Outcome:** current core descriptive domains can be populated with source-level lineage.

- Reuse the validated document stack and bounded website acquisition.
- Extract activities, beneficiaries, programs/services, descriptive and role-specific geography.
- Populate participation modes and transient opportunities from the start.
- Preserve action destinations separately from evidence links.
- Introduce governed program/service/unit scope.
- Add explicit retrieval failure, freshness and assessment scope.

**Gate:** domain precision on governed fixtures, no name-only identity, no negative inference from absence.

## 8. Phase 6 — fundraising knowledge and shadow registries

**Outcome:** CharityGraph describes how charities are funded and raise money without producing performance judgements.

- Separate funding sources, standing practices, campaigns and expenditure.
- Implement claim-specific authority policies for evaluated industry shadow registries.
- Use source-led enumeration where registries provide high-density records.
- Add campaign identity, mechanics, channels, time and source-reported metrics.
- Test provider relationships under source-role policy.
- Preserve no-prior/no-peer-fill fundraising expenditure rules.

**Gate:** identity precision, rights policy, additivity protection, explicit metric basis and no ROI/effectiveness inference.

## 9. Phase 7 — semantic domains and governance

**Outcome:** governed semantic observations can be reviewed, corrected and projected.

- Implement candidate and decision workflows.
- Add cause centrality and strengthen intervention/approach semantics.
- Add ethos and separate service/mission orientation.
- Add neutral `notable_context` with sensitive-content review policy.
- Add taxonomy/version/term and crosswalk artefacts.
- Add corrections, challenge, retraction and dependency invalidation.

**Gate:** domain-specific review evidence; no model output labelled human-governed; sensitive observations require adequate evidence and human approval.

## 10. Phase 8 — task-specific NLP and LLM execution

**Outcome:** difficult extraction and synthesis are economical, reproducible and governable.

- Separate OCR recovery, relevance, NER/extraction, interpretation, taxonomy and editorial tasks.
- Add canonical cache identity, budgets, telemetry and fake-client tests.
- Permit benchmarked multi-output calls only with independent validation and lineage.
- Import historical model runs as evidence without promotion.

**Gate:** reproducibility, budget enforcement, safe failure and domain-specific automation policies.

## 11. Phase 9 — shared evaluation and economics

**Outcome:** architecture and source decisions are based on measured public-knowledge yield.

- Run the shared stratified semantic benchmark.
- Maintain source-opportunity, proposition/review and cost ledgers.
- Compare structured, deterministic, economical-model, selective-escalation, oracle and human conditions.
- Measure precision, recoverable recall, oracle gap, source-scope gap, sparsity, review burden and accepted observations per dollar.
- Test processing equity across subject size and evidence richness.

**Gate:** approved routing policies and evidence that extra compute follows information opportunity rather than worthiness proxies.

## 12. Phase 10 — public-contract proposal

**Outcome:** a separately governed future public contract, only after internal architecture and pilot evidence are stable.

- Decide future subject-key migration, if any.
- Define public schemas for new domains and compact assessment scope.
- Define migration from public 0.5 with examples and losslessness analysis.
- Validate JSON/Markdown/bulk representation consistency.
- Update Viewer only after Data contract approval.

**Gate:** explicit product approval, full migration suite, public-safety validation and preserved prior release.

## 13. Phase 11 — progressive national scale

**Outcome:** move from controlled cohorts toward routine national operation.

- Maintain the common structured baseline for all eligible subjects.
- Scale source-led and evidence-opportunity enrichment in bounded cohorts.
- Schedule refresh by source and domain freshness.
- Monitor identity, coverage, quality, cost, change and failure clusters.
- Expand Viewer and distribution only where real user demand requires it.

## 14. Deferred research

- harm→remedy reference graph;
- comprehensive service-demand and unmet-need modelling;
- impact/effectiveness measures;
- international charity coverage;
- API/MCP services;
- distributed workers or PostgreSQL;
- automated sensitive-context publication;
- transactional giving or participation products.

