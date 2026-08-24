# CharityGraph Product Documentation Rewrite Manifest

**Status:** Controlled application manifest

**Version:** 2.0-draft

**Date:** 24 August 2026

## 1. Purpose

This packet is the coherent active product-documentation set for CharityGraph Builder vNext planning. It incorporates the product expansion, archaeology evidence, implemented contracts, taxonomy research, coverage-first risk appetite, cohort LLM economics and open-curation model agreed through 24 August 2026.

Apply the packet as one reviewed documentation tranche. Do not cherry-pick attractive sections while leaving conflicting active authority in place.

The packet contains no executable code, public schema or release-data change.

## 2. Packet files and roles

| File | Role |
|---|---|
| `DOCUMENT_AUTHORITY.md` | Authority hierarchy, conflicts and supersession |
| `PRODUCT.md` | Product promise, users, scope and value model |
| `PRINCIPLES.md` | Binding design and governance principles |
| `PUBLIC_COMMITMENTS.md` | Plain-language commitments to public users |
| `EXPERIENCES.md` | Required user, analyst, agent and correction experiences |
| `INTEGRATED_PRODUCT_AND_DATA_MODEL.md` | Canonical conceptual architecture and data model |
| `COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md` | Coverage/defensibility balance, budgets, judgment and corrections |
| `SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md` | Source-to-release chain and direct-observation readiness |
| `TAXONOMY_AND_SCHEME_GOVERNANCE.md` | External/native scheme portfolio, research register and mappings |
| `DOMAIN_PROFILE_INDEX.md` | Domain boundaries and profile backlog |
| `PUBLIC_VNEXT_DECISION_LOG.md` | Approved decisions and bounded open implementation decisions |
| `CURRENT_STATE.md` | Implemented repository/release/archaeology baseline |
| `ROADMAP.md` | Product and engineering phase sequence |
| `IMPLEMENTATION_PLAN.md` | First reality-slice architecture and PR sequence |
| `TEST_PLAN.md` | Invariant, semantic, holdout, cost and release validation |
| `AGENT_DATA_DISTRIBUTION_CONTRACT.md` | Future downstream-agent/data-use boundary |
| `PUBLIC_CONTRACT_0_5.md` | Status description for current immutable public contract |
| `CODEX_TO_CHATGPT_HANDOFF.md` | Bounded installation instructions and completion report |
| `REWRITE_MANIFEST.md` | This application and supersession record |

## 3. Installation mapping

### Data repository

Install the nineteen Markdown files at the repository root, replacing same-named active files where present. The Data repository remains the canonical home of cross-project product authority.

For newly named files, add them at root. For an old active file covering the same subject, either:

- move it unchanged into the existing documented history/reference area with a supersession header; or
- add a concise supersession header in place if repository history already provides adequate preservation.

Do not delete useful research evidence.

### Builder repository

Do not duplicate the canonical product documents as competing authorities. Update only repository-local `README`, `AGENTS.md` and active architecture/documentation indexes necessary to:

- link to the canonical Data documents at stable repository URLs;
- state that implemented code contracts/ADRs refine the conceptual documents;
- identify the approved first slice and immutable 0.5 boundary;
- remove any conflicting current instruction to resume the old enrichment pipeline.

If Builder has a canonical architecture file that conflicts with the integrated model, mark it implemented-detail/refinement or superseded; preserve useful implementation facts.

### Viewer repository

No change is required unless an active documentation link becomes broken. Do not rebuild or deploy merely to install this packet.

### Local project root

Keep the ZIP and source packet under a clearly named documentation/package directory, not a temporary directory. They may remain outside Git after the repository installation is complete.

## 4. Supersession and incorporation

The following earlier documents are incorporated or superseded as active authority:

| Earlier material | New status |
|---|---|
| Product Documentation Rewrite v1.0-draft | Superseded in full by this packet |
| Builder Target Architecture v0.1 | Incorporated into the integrated model and implementation plan; retain as design history |
| Product Architecture Alignment Review v0.1 | Findings resolved/incorporated; retain as review evidence |
| Top Level Product Goals Review v0.1 | Incorporated into `PRODUCT.md`; retain as decision history |
| Common Semantic Contract v0.1 | Incorporated into the integrated model; useful reference until code contracts supersede each part |
| Entity/purpose/program/population/geography contract v0.1 | Incorporated; becomes input to the identity/program and classification profiles |
| Participation contract v0.1 | Incorporated; becomes input to the participation profile |
| Fundraising/resource mobilisation contract v0.1 | Incorporated; becomes input to the fundraising profile |
| Finance/resource flow contract v0.1 | Incorporated; becomes input to the finance profile |
| Governance/workforce/capability/service-capacity contract v0.1 | Incorporated; becomes profile design evidence |
| Relationships/networks/ecosystem contract v0.1 | Incorporated; becomes relationship-profile design evidence |
| Ethos/conduct/commitments/notability contract v0.1 | Incorporated with revised risk and notability policy |
| Impact/outcomes/evidence/evaluation contract v0.1 | Incorporated; becomes outcomes/evaluation-profile evidence |
| Source/acquisition/provenance/adjudication/publication contract v0.1 | Superseded by the integrated model and source-governance document |
| Wide taxonomy landscape v0.1 | Retained as research evidence under the taxonomy-governance process; not itself an adopted vocabulary |

Repository code, schemas, ADRs and tests remain implementation evidence. Where implemented behaviour conflicts with a conceptual statement, do not silently change either: record the discrepancy and obtain a bounded decision.

## 5. Decisions newly made explicit

- coverage and reach are first-order product requirements;
- every published assertion retains a mechanical provenance floor;
- forensic depth varies by cohort, claim consequence and evidence opportunity;
- cohort envelopes are AU$100 for the top 100, next 1,000 and next 10,000;
- ordinary low-risk model judgment should be useful and decisive rather than reflexively unknown;
- community correction is governed open curation and a success mechanism;
- external schemes and rejected/adapted alternatives require a public research/disposition trail;
- UN SDGs, CLASSIE, National Standard Chart of Accounts, ACNC/ATO classifications and applicable ABS standards enter the initial portfolio;
- participation and shadow registries are initial-state requirements;
- fundraising and participation vocabularies support granular future direct observation;
- the first coding slice is a fixed, approximately ten-charity private identity/program/classification pipeline;
- deterministic Python does not approximate unrestricted English through growing phrase rules.

## 6. Immutable and naming boundaries

- Do not modify any file in the immutable `v0.5.0-2026-08-15` release.
- Required manifest SHA-256 before and after: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.
- `PUBLIC_CONTRACT_0_5.md` in this packet must be installed byte-for-byte unless a mismatch with the currently approved file is reported and resolved.
- Do not create a new product-owned universal organisation identifier.
- New active branding and prose use CharityGraph.
- Exact historical or compatibility identifiers may remain only where necessary and clearly labelled.

## 7. Required Codex validation

Codex must report:

- source packet and destination mapping, including departures;
- files added, replaced, cross-linked or marked superseded;
- relative-link and duplicate-authority checks;
- active-document naming lint;
- Markdown whitespace/fence checks;
- relevant Builder and Data tests at the current baseline;
- Viewer tests only if Viewer was changed;
- immutable release checksum before and after;
- confirmation that no runtime database, archive evidence, credentials, model calls, network acquisition, Data bundle, schema or Viewer deployment changed.

## 8. Not authorised by this packet

- implementation of the first slice;
- SQLite migration changes;
- archive movement or automatic legacy rebinding;
- real source retrieval or provider/model calls;
- taxonomy harvesting or public schema creation;
- public Data rebuild;
- Viewer redesign or deployment;
- deletion of historical evidence, branches or compatibility code;
- merge of the installation PRs without separate approval.
