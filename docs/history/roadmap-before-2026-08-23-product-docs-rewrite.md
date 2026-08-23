# Historical snapshot — superseded 2026-08-23

**Status:** Historical reference only; not current executable instruction.  
**Current authority:** [DOCUMENT_AUTHORITY.md](../../DOCUMENT_AUTHORITY.md)

---

# CharityGraph Product Roadmap

> Historical note: the detailed RC4 and pre-pivot roadmap below records work completed under the former CauseBase name. CharityGraph is the current name and is unaffiliated with the unrelated Australian project using that name.

## Current sequence

1. Establish the CharityGraph data contract.
2. Produce a trustworthy CharityGraph Builder.
3. Develop CharityGraph Viewer later.

The current target model is source-native records, canonical observations, and derived projections. JSON/Markdown cards and sidecars are authoritative; CSV/Parquet are projections.

**Status:** Accepted product direction  
**Updated:** 2026-08-15

CauseBase is one product with three sub-products: CauseBase Data, CauseBase Builder and CauseBase Viewer. The shared CauseBase product contract governs all three. Documents may live in the CauseBase Data repository for convenience, but CauseBase Data is not the parent product.

## Historical roadmap through RC4

The following records the roadmap that guided the work through RC4. It is retained as evidence, not as the active delivery sequence; the active post-RC4 capability roadmap follows it.

### Foundations (historical)

- establish separate Builder, Data and Viewer repositories and durable/archive versus mutable/runtime storage;
- maintain a provisional CauseBase subject, card, evidence and provenance model;
- retain synthetic fixtures for deterministic testing and publication-safety work;
- make Builder/Viewer baseline behaviour reproducible and credential-free;
- establish shared documentation, release safety and agent-oriented public-data conventions.

No public schema is frozen in this phase.

### Reality spike (historical)

Process 30–50 deliberately heterogeneous Australian charities through structured ACNC/AIS/DGR evidence, representative annual or financial reports, and selected website evidence. Include identity, reporting, web-presence and accounting edge cases. Use observed failures to revise the provisional identity, card, financial-period, evidence, provenance and coverage models. Produce a product handoff before stabilising v0.x public contracts.

**Historical completion evidence:** 36 seeds processed; current ACNC/AIS outcomes retained privately; three reports and two website snapshots acquired; five governed real-card staging builds validated. DGR is explicitly deferred to a separately governed ABR national-bulk ingest, rather than inferred from its absence in a small spike.

### National structured backbone (historical)

Build national structured coverage from authoritative ACNC, AIS, DGR/ABR or equivalent sources. Record external identifiers and source relationships without assuming a one-ABN-one-subject model. This backbone may be published or downloadable before the distinctive enriched-card experience launches.

### Real enriched slice (historical)

Build roughly 100–1,000 real enriched cards using report and web evidence, the fundraising-estimation ladder, GPT-5-mini synthesis, CauseBase taxonomy v0, external taxonomies, real embeddings, precomputed semantic neighbours and basic correction intake. CauseBase taxonomy v0 is designed and tested in parallel with the reality spike.

### Public launch (historical)

Launch CauseBase Data and Viewer around a visibly distinctive enriched-card experience: dense neutral cards, provenance, estimation method, multiple taxonomies, real semantic exploration where reliable, and a working low-friction "Suggest correction" intake. Do not present CauseBase merely as a cleaned regulator mirror.

### Scale enrichment (historical)

Expand toward roughly 10,000 enriched cards with incremental refresh, source/evidence hashing, website and feed refresh, current opportunities, model routing/cost controls and a larger evaluation corpus.

### Governance depth (historical)

Add governed public proposal records, review/status history, discussion integration, taxonomy contribution governance, richer provenance/history and correction-dependent rebuilds. Raw correction submissions remain private until moderated.

### Agent ecosystem (historical)

Improve discoverability, stable entity/card URLs, per-entity JSON and Markdown, licence/schema/provenance metadata, selective retrieval examples and citation conventions. Add API or MCP services only when demonstrated demand justifies them; static public artefacts remain independently usable.

### Phase 2A completion note (historical)

A 120-card governed candidate is validated and staged for the Viewer with private website/report evidence processing, `gpt-5-mini` synthesis, Taxonomy v0, `text-embedding-3-small` neighbours, per-card JSON/Markdown, an agent guide and a configurable correction-intake contract. Human evaluation assessment and live endpoint configuration remain follow-on operational work.

## Active post-RC4 capability roadmap

The RC4 120-card baseline is released. The next roadmap is organised by user capability and dependency, rather than by repository ownership. Builder, Viewer and Data remain implementation owners underneath each capability.

### Phase 1 — define success

- Complete the public schema/data/agent contract and immutable v0.5 release semantics. **Complete.**
- Establish Golden Corpus v1 spanning financials, provenance, summaries, identity and Viewer rendering. **Complete.**

### Phase 2 — technology spikes

- Compare PDF/document extraction stacks against Golden Corpus v1 and record a governed decision. **Complete.**
- Compare frontend/JavaScript framework options against the utilitarian Viewer requirements. **Complete — KEEP CURRENT.**
- Investigate the bounded value, provenance and maintenance implications of Wikipedia/Wikidata. **Complete — broad ingestion deferred.**

### Phase 3 — evidence engine

- Build document pipeline v2 from the selected stack; acquire/extract website evidence; and stress-test identity, groups and relationships. **Bounded Evidence Engine v1 pilot complete.**

### Phase 4 — knowledge and distribution validation (active)

- Validate taxonomy on a larger stratified sample.
- Define the agent/data distribution contract.
- Test consumer-LLM discovery and accurate interpretation using the protocol in TEST_PLAN.md.
- Complete Knowledge Validation v1 minimum gate: 22 decisions validated/scored; no domain auto-promotable; 26 cases deferred. **Complete.** Semantic Enrichment Benchmark v1 is the active review-only next increment; no public release or schema change is authorised.
- Consolidate approved semantic-domain and fundraising-source design decisions before implementation. **Design decision recorded; implementation remains review-only and gated.**

### Phase 5 — Viewer

- Redesign information architecture and implement it with administrative-credibility aesthetics. Viewer supports inspection, comparison and provenance; it is not a recommendation or fundraising marketplace.

### Phase 6 — corpus machinery

- Build a resumable, sliceable corpus engine and an operations harness that monitors completion, quality, spend, corpus health and change.

### Phase 7 — progressive scale

- Process a stratified 500/1,000-card build, then a several-thousand slice. The first build is an information-generating milestone: quality, cost, source and identity findings gate any full-corpus decision.

### Phase 8 — ongoing operation

- Add longitudinal refresh/history and corrections/release governance. Do not over-specify this phase before the earlier gates.

The active capability backlog also includes schema/public-contract consolidation, golden-corpus evaluation, document and frontend bake-offs, website evidence, progressive build operations, longitudinal history, identity stress testing, agent distribution, correction governance, taxonomy validation and consumer-LLM legibility.
