# Semantic Demand Catalogue v0.1 — pilot

**Status:** experimental product-design artefact; subordinate to canonical CharityGraph authorities.  It creates no public contract, schema, runtime behaviour, ontology term, evidence, or benchmark answer.

## Purpose and boundary

This is a demand specification, not a prompt gallery.  A question records the semantic conditions an answer would have to meet, including scope, time, evidence, joins, answerability and prohibited inference.  It does not assert that the required evidence exists for any real charity. `supported`, `bounded_partial`, `tested_missingness`, and `unresolved` are valid outcomes; a refusal can be successful.

## Authority map reviewed before generation

| Authority | Demand-side consequence |
|---|---|
| `NORTH_STAR_TARGET_CARD.md` / `north-star-v0.3` | Twenty knowledge domains are demand surfaces, not independent FAQ headings; retain scope, time, provenance, coverage and correction. |
| `EXPERIENCES.md` | Personas come from analyst cohort building, service-system analysis, funding/ecosystem, fundraising, finance comparison, evaluation, mandate screening, reproducibility and data-builder work. |
| `PRODUCT.md`, `PRINCIPLES.md` | Discovery is evidence-led and restrained; comparisons cannot silently equate periods/scopes; downstream analysis stays downstream. |
| `INTEGRATED_PRODUCT_AND_DATA_MODEL.md` | Cross-domain questions follow seams (for example program–service–availability and campaign–financial line), never property propagation. |
| `DOMAIN_PROFILE_INDEX.md` | Domain-specific questions preserve the relevant subject, scope and evidence risks. |
| `SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md` | Source authority is proposition-specific; absence needs coverage; observed, reported, asserted and adjudicated states stay separate. |
| Builder `BUILDER_MACHINERY.md` at `ddd3881…` | Existing evidence/coverage/projection machinery is the grounding map; no new acquisition or semantic machinery is assumed. |

The pilot has a temporary broad pool of **78** candidates, pruned using demand signatures (not wording) to **36** retained questions.  This package contains only retained reusable templates; it has no real-charity instances or golden prose answers.

## Files

- `personas.md` — derived jobs and failure modes.
- `relevance-matrix.md` — all persona × North Star domain cells; `M`/`N` are permitted zero-question cells.
- `question-schema.json` — machine-readable schema and controlled vocabulary.
- `pilot-questions.json` — 36 curated semantic demands.
- `findings.md` — generation, dedupe, critique and scale decision.

## Reuse and execution

Templates may later be instantiated only with typed parameters and separately governed evidence.  A future executable benchmark must add real instances, source/evidence bindings and adjudicated expected answerability; it must not treat this catalogue as evidence or fabricate an answer.
