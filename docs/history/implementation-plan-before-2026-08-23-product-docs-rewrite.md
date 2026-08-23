# Historical snapshot — superseded 2026-08-23

**Status:** Historical reference only; not current executable instruction.  
**Current authority:** [DOCUMENT_AUTHORITY.md](../../DOCUMENT_AUTHORITY.md)

---

# CharityGraph Implementation Plan

> Historical note: pre-pivot CauseBase plan items below are retained for provenance. The active identity is CharityGraph; do not treat historical product names as current public branding.

**Status:** Active implementation plan; historical phases retained for traceability
**Updated:** 2026-08-15

## Phase 2B contract

CauseBase uses a three-layer source contract: source-native public observations, selectively harmonised canonical card fields, and governed derived artefacts. Source observation time, world/effective time and CauseBase representation/release time are separate. Annual financial and regulator observations append; the current projection is a view, not an overwrite.

Incremental refresh is staged: acquire/extract, deterministic change profile, dependency decision, optional bounded semantic assessment, then reuse or refresh. Reuse itself is recorded with the assessed inputs and reason. Numeric-only changes do not automatically regenerate prose or embeddings.

Funding sources, fundraising methods, current-campaign freshness and fundraising expenditure are distinct fields. They remain descriptive, evidence-bound and non-normative.

The approved v0.5 design distinguishes claim basis from extraction method, treats coverage as capability availability, permits a null sparse-card summary, uses source-family sidecars rather than duplicating payloads in cards, and permits an explicit current-financial pointer over retained observations. It is implemented in the immutable v0.5 release; RC4 remains historical.

## Historical implementation record — completed reality spike through RC4

### Historical — Phase 2A completion record

1. The 120-subject heterogeneous, reproducible cohort uses authoritative ACNC promotion only and records selection strata/provenance privately.
2. Enrichment uses bounded current website/report evidence, cache-aware `gpt-5-mini` synthesis, CauseBase-native Taxonomy v0 and production embeddings.
3. The public candidate is allowlisted and contains cards, indices, taxonomy, aggregate coverage, semantic neighbours and an agent retrieval guide; source archives and model inputs stay private.
4. Viewer consumes the generated release, keeps similarity descriptive, and hands corrections to a configurable external intake URL using the documented prefill contract.

### Historical — Phase 2A.1 human-test hardening

Treat published release `phase2a-2026-08-10` as historical. Any corrected public-card content uses a new release version and separately recorded Viewer deployment commit. Maintain `main` -> manual validated bundle -> static-only `gh-pages`; no ordinary push deploys. Human feedback is a private external form with generic and field-specific prefill, while the 30-case review pack remains local/private.

1. Establish three repository boundaries and configure these path classes:
   - durable OneDrive archive for completed source and processed evidence;
   - local mutable runtime for state, temp, cache, logs and staging;
   - public Data publication destination.
2. Replace the provisional one-ABN identity assumption with a stable opaque `causebase_id`, `subject_kind`, `external_identifiers[]` and explicit `relationships[]`.
3. Preserve synthetic fixtures, but label all current schemas and rendered outputs as provisional.
4. Make publication staging isolated and allowlisted; preserve the previous valid candidate on failure.
5. Add ACNC/AIS/DGR structured-source interfaces sufficient for a 30–50 subject reality spike.
6. Select a deliberately awkward cohort; record selection rationale rather than treating it as a representative national sample.
7. Acquire representative structured, report and website evidence; record failures as domain findings.
8. Produce and maintain a Codex-to-ChatGPT handoff before stabilising public v0.x card, identity or evidence schemas.

#### Historical — reality-spike completion record

- The full 36-seed cohort has been processed through current ACNC and AIS extracts (8 resolved, 26 candidate, 2 ambiguous), with no name-only promotion.
- Three reports and two web snapshots are retained/extracted privately; five governed real cards pass registry-gated staging validation.
- The DGR source is available through the ABR national bulk extract but is intentionally deferred to a separately governed national ingest because it is not a cohort-scale feed.

### Historical — Phase 1 completion record

- National ACNC, AIS and ABR/DGR sources are privately archived with retrieval metadata, hashes and licence information.
- National normalisation writes private source-record records and diagnostics without forcing subject resolution.
- The safe Phase 1 staging candidate publishes only public registry and aggregate structural metadata; raw source content remains excluded.

### Historical — web evidence pipeline design

Website ingestion is a core enrichment stage, separate from report processing. It starts with homepage, About/What we do, programs, volunteer/get involved, events, governance, news/blog, feeds and selected opportunity pages. It produces stable-understanding evidence separately from transient current-activity and opportunity observations, each with independent freshness/refresh policies.

### Historical — enriched-card outputs

For a real enriched subject, treat classification, embedding and similarity outputs as related derived products. Use production embeddings only for real enriched cards; synthetic hash embeddings must never be presented as public semantic similarity.

### Historical — taxonomy maintenance lifecycle

Run deterministic PREPARE periodically against a frozen corpus and taxonomy. It produces a compact private packet before any optional model work. An optional model critique is advisory evidence only. Human decisions are recorded with definitions, boundaries, exclusions, cases and migration implications; implementation then creates a candidate version. VALIDATE compares that candidate with the baseline and current corpus without rebuilding or publishing. Only a separately governed reclassification/release may follow.

### Historical — correction delivery sequence

The Phase 2/3 enriched-card release requires basic private intake with prefilled card/field/release context and a traceable acknowledgement. Public proposal records, moderation decisions and full history arrive later. No raw intake payload is automatically public.

### Historical — contract discipline

The project is contract-led, not contract-frozen. Public schema versions may deliberately break before public 1.0, with clear versioning and migration/release notes. The historical reality spike informed the contract; the current stabilisation gate is public-contract consolidation and golden-corpus review.

## Current implementation direction — immediate post-RC4 sequence

The public-contract gate is complete. The next work is governed evaluation before evidence-engine scale:

1. **Public contract v0.5** — complete: specifications, Builder validation/migration, Data release and Viewer cutover are validated and deployed. Do not mutate `releases/v0.5.0-2026-08-15`.
2. **Golden Corpus v1 and document-stack bake-off** — establish governed awkward cases and acceptance measures for document extraction, financial reconciliation, provenance, identity, editorial rendering and Viewer usability. Benchmark bounded extraction candidates against retained private evidence, recording availability, quality, cost and failure modes.
3. **Document pipeline v2 and first Evidence Engine pilot** — complete: a computed decisive routed architecture retains deterministic `pdfplumber`, page-routed local Tesseract and local vector colour/geometry extraction. The bounded retained-snapshot website/identity/fundraising pilot is complete and produces review material only. Preserve every source result as private evidence rather than a public artefact.

Then conduct bounded, decision-producing frontend and Wikipedia/Wikidata spikes. Each records alternatives, fixtures, quality/cost/accessibility evidence, a recommendation and an explicit decision gate; none silently becomes production architecture.

**Completed distribution increment:** frontend decision is KEEP CURRENT; Wikimedia is deferred as a broad source; the agent/data contract and 16-case consumer-LLM foundation are checked in. The minimal static discovery layer is a Viewer projection of the pinned v0.5 release, not a new Data release or backend. Full consumer-product testing and larger taxonomy validation remain the next knowledge-validation work.

**Knowledge Validation v1 (minimum gate complete):** 22 approved decisions were validated/scored across the deliberately difficult sample; no domain is auto-promotable and the remaining 26 cases are deferred. The active next phase is the private/review-only Semantic Enrichment Benchmark v1 implementation contract in `SEMANTIC_ENRICHMENT_BENCHMARK_V1_IMPLEMENTATION_v2.md`; no public schema, release or Viewer change is authorised.

**Approved design consolidation:** the next review-only implementation may use
scoped observations for program/service/unit evidence; separate Ethos and
`service_or_mission_orientation`; preferred public `notable_context`; and
fundraising practice/campaign/expenditure distinctions. A bounded
fundraising-industry source category is authorised for experimental review
only. Before that work, reconcile Builder's obsolete fallback-prior guidance
and code with the canonical no-prior/no-peer-imputation fundraising policy.
Do not change the v0.5 release or public schemas in that reconciliation.

After those decisions, build document pipeline v2, website evidence acquisition/extraction and identity/group stress tests. Larger taxonomy validation, agent/data distribution and consumer-LLM evaluation precede the Viewer redesign. Corpus machinery follows the redesigned, validated contract; the 500/1,000-card run is a gated learning slice, not an automatic scale commitment.

## Operations harness direction

The build engine executes resumable, sliceable processing. A separate operations harness determines whether it is proceeding correctly, completely and economically. It will monitor completion (selected through published/held), quality (benchmarks, reconciliations, contradictions, outliers, links and failure clusters), spend (API/OCR/vision/synthesis usage and cost), corpus health (taxonomy/source/AIS/DGR/geography/identity distributions) and change (new evidence, invalidations, stale records and refresh backlog).
