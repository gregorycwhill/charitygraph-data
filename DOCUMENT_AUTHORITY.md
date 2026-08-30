# CharityGraph documentation authority

**Status:** Canonical project-governance document

**Version:** 2.1-draft

**Date:** 28 August 2026

## 1. Purpose

This document defines which CharityGraph documents govern product intent, conceptual architecture, domain semantics, public contracts and implementation. It prevents a historical plan, design exploration, code comment, handoff or immutable release description from silently overriding a current decision.

CharityGraph is a product family built around governed Australian charity knowledge:

- **Builder** acquires evidence, constructs governed knowledge and builds release candidates;
- **Data** publishes reusable governed public data, immutable contracts, releases, schemas, catalogue metadata and shared product authority;
- **Viewer** provides human inspection, navigation and contextual entry points; and
- **Playbooks** publishes governed, open analytical methods for applying general-purpose AI to CharityGraph data.

The dedicated Playbooks repository has not yet been created. Shared CharityGraph product, editorial and governance authority remains centred in the canonical documents maintained in `charitygraph-data`. A future `charitygraph-playbooks` repository may own Playbooks-specific contracts and releases, subject to the shared product principles and commitments.

Repository location does not determine authority.

## 2. Authority hierarchy

When documents conflict, apply this order:

1. `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_COMMITMENTS.md` and `EXPERIENCES.md`;
2. `INTEGRATED_PRODUCT_AND_DATA_MODEL.md`;
3. `COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md` and other approved cross-cutting governance policies;
4. `SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md` and `TAXONOMY_AND_SCHEME_GOVERNANCE.md`;
5. the domain authorities indexed in `DOMAIN_PROFILE_INDEX.md`;
6. approved architecture decision records and implemented Builder contracts;
7. the applicable version-specific public Data contract, schema and immutable release manifest;
8. `CURRENT_STATE.md`, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md`;
9. working designs, evaluation plans and implementation proposals; and
10. historical plans, handoffs, experiments, migration evidence and immutable historical artefacts outside their compatibility scope.

A more specific approved contract governs its subject within the boundaries established by higher-level documents.

## 3. Document statuses

| Status | Meaning |
|---|---|
| Canonical | Current product or governance authority |
| Approved decision | Binding decision awaiting controlled propagation |
| Implemented contract | Exact contract for a named implementation or release |
| Active plan | Current sequencing; may not change product semantics |
| Working design | Proposed detail or investigation; not authority until approved |
| Reference | Operational, methodological or explanatory material |
| Superseded | Replaced but retained for traceability |
| Historical | Evidence of a former state; no current instruction |
| Immutable release | Published bytes and metadata that must not be rewritten |

Every active document SHALL state its status, version/date, scope and material supersession relationship.

## 4. Current authorities

| Subject | Authority |
|---|---|
| Product promise, boundary and users | `PRODUCT.md` |
| Playbooks product purpose and boundaries | `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_COMMITMENTS.md`, `EXPERIENCES.md` |
| Product principles | `PRINCIPLES.md` |
| Public promises | `PUBLIC_COMMITMENTS.md` |
| End-to-end experiences | `EXPERIENCES.md` |
| Integrated conceptual model and domain seams | `INTEGRATED_PRODUCT_AND_DATA_MODEL.md` |
| Coverage, model economics and open curation | `COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md` |
| Source, evidence, provenance, adjudication and release governance | `SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md` |
| Taxonomies, external schemes and native vocabularies | `TAXONOMY_AND_SCHEME_GOVERNANCE.md` |
| Domain ownership and research-design status | `DOMAIN_PROFILE_INDEX.md` |
| Current public release | `PUBLIC_CONTRACT_0_5.md`, its schemas and immutable manifest |
| vNext product and future-contract decisions | `PUBLIC_VNEXT_DECISION_LOG.md` |
| Current delivery state | `CURRENT_STATE.md` |
| Capability sequence | `ROADMAP.md` |
| Approved execution sequence | `IMPLEMENTATION_PLAN.md` |
| Verification and release gates | `TEST_PLAN.md` |
| Machine and agent distribution | `AGENT_DATA_DISTRIBUTION_CONTRACT.md` |
| Playbook-specific format, method governance, contribution, evaluation and release rules | Future canonical Playbooks contract, once established |
| Semantic reliability, technical replication and reproducible semantic replay | `SEMANTIC_RELIABILITY_AND_REPRODUCIBILITY.md` |
| Current coding handoff | `CODEX_TO_CHATGPT_HANDOFF.md` |

## 5. Refinement and conflict rules

A domain profile MAY:

- specialise a shared primitive;
- introduce domain vocabulary and validation;
- impose stronger evidence or publication requirements; and
- define domain-specific calculations and views.

It SHALL NOT:

- change the meaning of a shared primitive silently;
- create a competing canonical record for the same underlying fact;
- weaken higher-level privacy, rights, lineage or correction requirements;
- propagate attributes across subject or relationship boundaries without an approved rule; or
- change public promises or release contracts indirectly.

When a genuine conflict appears:

1. preserve both statements and identify their authority;
2. determine whether the conflict is semantic, temporal, scope-specific or implementation-only;
3. record the resolution in an approved decision;
4. propagate it to affected canonical documents; and
5. retain superseded material as history or design evidence.

## 6. Decision propagation

An approved decision is binding within its subject before every document is updated. The implementation owner SHALL either propagate it or record an explicit conflict. Stale text SHALL not be followed silently.

After propagation:

- mark the source decision as propagated;
- link to the canonical destination;
- remove duplicated normative instructions where practical;
- retain empirical evidence, alternatives and research sources; and
- update relevant tests and agent instructions.

## 7. Public-contract discipline

Public contract 0.5 is current compatibility authority for its immutable release. It is not the target internal Builder model and not a future-schema proposal.

Builder vNext is governed by subjects, scopes, evidence, observations, assertions, relationships, measurements, decisions and release projections. Cards are public convenience views.

A future public migration requires:

- approved product decision;
- evidence from representative reality slices;
- versioned schemas and examples;
- identifier and domain migration rules;
- losslessness and compatibility analysis;
- Data and Viewer coordinated acceptance;
- release catalogue and correction treatment; and
- a new immutable release.

## 8. Naming and historical separation

All active product, architecture, operational and agent-instruction documents use CharityGraph names and current paths.

Historical naming may occur only where exact matching is unavoidable inside:

- immutable release bytes;
- isolated compatibility adapters and tests;
- quarantined migration evidence; or
- exact third-party historical citations.

Active narrative uses neutral phrases such as “former project name”, “legacy public key” or “public contract 0.5 compatibility”. Historical documents SHALL live under a clearly marked history or evidence location and SHALL not contain executable current instructions.

## 9. Change control

- Product-boundary changes require a product decision and updates to the four canonical product documents.
- New Playbook product semantics must remain traceable to the four canonical product documents. A future Playbook-specific contract may refine those semantics but may not override shared CharityGraph neutrality, evidence, openness, privacy, contestability or brand rules.
- Integrated-model changes require seam analysis and affected domain review.
- Builder architecture changes require traceability to canonical requirements and an ADR where material.
- Taxonomy changes require scheme disposition, version analysis and affected-assignment review.
- Source-policy changes require claim-family, rights and publication analysis.
- Public-contract changes require versioned schemas, examples, migration and release gates.
- Immutable releases are never edited in place.
- Handoffs and manifests report work; they do not create product authority.

## 10. Complexity boundary

Conceptual sophistication belongs in the governed data layer. Developers, software agents and LLMs may consume detailed schemas and provenance. Ordinary users receive simple, purpose-built projections and progressive disclosure.

User-interface simplicity SHALL NOT be achieved by weakening internal semantics, and internal semantic richness SHALL NOT require an unnecessarily complex public experience.
Phase 1 reality-slice execution design is indexed by [REALITY_SLICE_1_ACCEPTANCE_PACKET.md](REALITY_SLICE_1_ACCEPTANCE_PACKET.md). It is a subordinate refinement of IMPLEMENTATION_PLAN.md and TEST_PLAN.md.

## Semantic gate authority

SEMANTIC_HEURISTIC_APPROVALS.md is the canonical register for exceptions to the Semantic Heuristic Gate. No implementation may rely on a deterministic semantic lexical exception without a registered approval ID and explicit Greg approval. The gate is ex-ante and controlling for Builder and Data planning.

## 11. Semantic reliability authority

`SEMANTIC_RELIABILITY_AND_REPRODUCIBILITY.md` is the canonical cross-cutting authority for semantic validity, repeatability, technical replication and reproducible replay. `SEMANTIC_RELIABILITY_BASELINE_2026-08-28.md` is reference experimental evidence subordinate to that policy; it establishes no product threshold.

## North Star planning anchor

`NORTH_STAR_TARGET_CARD.md` derives from `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_COMMITMENTS.md`, `EXPERIENCES.md`, `INTEGRATED_PRODUCT_AND_DATA_MODEL.md` and `DOMAIN_PROFILE_INDEX.md`. It does not override those authorities and is not a public schema proposal. `ROADMAP.md` and `IMPLEMENTATION_PLAN.md` SHALL map delivery against it so a reality slice or domain implementation cannot silently redefine product scope.
