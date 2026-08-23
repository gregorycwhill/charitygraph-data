# CharityGraph Documentation Authority

**Status:** Canonical project-governance document  
**Version:** 1.1-draft  
**Date:** 2026-08-23

## 1. Purpose

This document defines which CharityGraph documents govern product intent, architecture, public contracts and implementation. It prevents an old plan, historical handoff or immutable release description from silently overriding a current decision.

CharityGraph is one product implemented through three repositories:

- **Builder** produces governed knowledge and release candidates;
- **Data** publishes immutable public data contracts and releases;
- **Viewer** provides the public inspection interface.

Repository location does not determine product authority.

## 2. Authority order

When documents conflict, use this order:

1. `PRODUCT.md`, `PRINCIPLES.md`, `PUBLIC_COMMITMENTS.md` and `EXPERIENCES.md`;
2. `LLM_ECONOMICS_AND_COHORT_POLICY.md` for model role, cohort order/budgets, cost orchestration and coverage-first acceptance, plus other approved architecture/product decision records;
3. the applicable version-specific public Data contract and schemas;
4. `CURRENT_STATE.md`, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md`;
5. domain designs, evaluation designs and implementation proposals;
6. historical plans, handoffs, experiments, migration records and immutable release artefacts.

A more specific approved contract governs its subject within the boundaries set by higher-level product documents.

## 3. Document statuses

| Status | Meaning |
| --- | --- |
| Canonical | Current product or governance authority |
| Approved decision | Binding design decision awaiting or undergoing propagation |
| Implemented contract | Exact contract for a named released version |
| Active plan | Current sequencing or execution plan; may not change product semantics |
| Working design | Investigation or proposed detail; not authority unless approved |
| Reference | Useful operational or explanatory material |
| Superseded | Replaced; retained only for traceability |
| Historical | Evidence of a past state; contains no current instruction |
| Immutable release | Published bytes and metadata that must not be rewritten |

Every active document must state its status, version or date, scope and supersession relationship where relevant.

## 4. Current authorities

| Subject | Authority |
| --- | --- |
| Product purpose and boundary | `PRODUCT.md` |
| Product principles | `PRINCIPLES.md` |
| Public promises | `PUBLIC_COMMITMENTS.md` |
| Users, channels and end-to-end jobs | `EXPERIENCES.md` |
| Current delivery state | `CURRENT_STATE.md` |
| Capability sequence | `ROADMAP.md` |
| Approved implementation sequence | `IMPLEMENTATION_PLAN.md` |
| Verification and release gates | `TEST_PLAN.md` |
| Model economics, cohort priority and orchestration | `LLM_ECONOMICS_AND_COHORT_POLICY.md` |
| Builder internal architecture | approved Builder target architecture and subsequent ADRs |
| Current public release contract | `PUBLIC_CONTRACT_0_5.md`, its schemas and immutable release manifest |
| Current machine distribution | `AGENT_DATA_DISTRIBUTION_CONTRACT.md` |
| Current execution handoff | `CODEX_TO_CHATGPT_HANDOFF.md` |

## 5. Decision propagation

An approved working decision is binding for its subject even before every document is updated. The implementation owner must either propagate it or record an explicit conflict; it must not silently follow stale text.

After propagation:

- mark the decision record as propagated;
- link to the canonical destination;
- remove duplicated normative instructions where practical;
- retain empirical evidence and rejected alternatives as history.

## 6. Public-contract discipline

The implemented public contract 0.5 is current compatibility authority for its immutable release. It is not the target internal Builder model and is not a future-schema proposal.

Builder's internal canonical authority is governed typed observations attached to durable subjects and scopes. Cards and other public formats are release projections. A future public-contract migration requires its own decision, schemas, examples, migration notes and release gates.

## 7. Naming and historical separation

All active product, architecture, operational and agent-instruction documents use CharityGraph names and current paths.

The former brand may occur only where exact matching is necessary inside:

- immutable historical release bytes;
- isolated compatibility adapters and tests;
- quarantined migration evidence;
- unavoidable third-party historical citations.

Active narrative uses neutral phrases such as “former project name”, “legacy public key” or “public contract 0.5 compatibility”. Historical documents should live under a clearly marked history directory and must not contain executable current instructions.

## 8. Change control

- Product-boundary changes require an approved product decision and updates to the four canonical product documents.
- Builder architecture changes require an ADR and traceability to product requirements.
- Public-contract changes require versioned schemas, examples, migration analysis and Data/Viewer acceptance.
- Domain vocabulary changes require taxonomy or schema governance and affected-observation migration analysis.
- Immutable releases are never edited in place.
