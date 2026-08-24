# Phase 1 Reality Slice 1 — Frozen Design and Acceptance Packet

**Status:** Approved execution design refining `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md`  
**Version:** 1.0-draft  
**Date:** 24 August 2026  
**Scope:** Private Phase 1 implementation gate only

This packet freezes the first approximately ten-charity reality slice before implementation PR A. It is subordinate to the canonical product, integrated model, governance, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md`. It does not change public contract 0.5, schemas, releases, Data publication or Viewer.

## 1. Starting boundary

The packet was prepared from the merged `main` foundations:

| Repository | Starting `main` |
|---|---|
| Data | `0357918dc6a92d9dab95b5a8adf72911f310fd93` |
| Builder | `3b92b7e0be6af1f59e371bcef68e336e91101f0c` |

Viewer is out of scope. No production source was downloaded, no archive was rebuilt, and no model call was made while preparing this packet.

## 2. Frozen cohort

The cohort is ten named Australian charities. Names and ABNs are candidate selection facts, not CharityGraph identifiers. PR A must perform the exact ACNC/ABR join and retain the source record and evidence; it must not mint a universal organisation identifier from a name or domain.

| Charity (legal/current name) | ABN | ACNC registration identity for PR A | Cohort role(s) | Diagnostic value and review sensitivity |
|---|---:|---|---|---|
| The Smith Family | `28 000 030 179` | Registered ACNC charity record, exact ABN join required | Simple legal entity; national education charity; fundraising and programs | A familiar single legal subject with a clearly named flagship program and substantial public reporting; avoid treating the program as a second organisation. |
| Australian Red Cross Society | `50 169 561 394` | Registered ACNC charity record, exact ABN join required | Federated/group-like operational structure; many services and brands | Tests legal subject versus branches, Lifeblood and other operational scopes; avoid collapsing business names or services into legal subjects. |
| Landscape Recovery Foundation Ltd. | `67 649 417 658` | Registered ACNC charity record, exact ABN join required | Small/project-based and volunteer/community participation case | Exercises sparse evidence, named conservation projects and small-organisation coverage; do not infer volunteer governance without evidence. |
| Indigenous Literacy Foundation Ltd. | `45 146 631 843` | Registered ACNC charity record, exact ABN join required | Indigenous-focused organisation; cultural-governance sensitivity; national program work | Exercises Indigenous data-governance boundaries, community/language scope and program decomposition; cultural or authority-sensitive claims require human review. |
| Australian Communities Foundation Limited | `20 077 830 347` | Registered ACNC charity record, exact ABN join required | Grantmaker; multi-fund/trust scope | Distinguishes grantmaking, administration and funds from grantee organisations; preserve trustee/fund relationships and legal scope. |
| Australian Conservation Foundation Incorporated | `22 007 498 482` | Registered ACNC charity record, exact ABN join required | Advocacy; national campaigns; fundraising | Exercises organisation-versus-campaign scope and advocacy activity without turning policy positions into impact claims. |
| Mission Australia | `15 000 002 522` | Registered ACNC charity record, exact ABN join required | Multi-program national organisation; service provider with many sites | Tests service, housing, employment, family and health program boundaries, site geography and regulated-provider evidence. |
| Life Without Barriers | `15 101 252 171` | Registered ACNC charity record, exact ABN join required | Service provider with multiple sites; group/subsidiary signals; high-consequence review | Exercises service/site scope and regulatory/compliance evidence. Adverse or safeguarding-adjacent claims are human-reviewed and never inferred from silence. |
| World Vision Australia | `28 004 778 081` | Registered ACNC charity record, exact ABN join required | Fundraising-intensive; national and international programs; group relationship | Tests fundraising, program and overseas-partner scope while keeping the Australian legal subject distinct from the international confederation. |
| The Fred Hollows Foundation | `46 070 556 642` | Registered ACNC charity record, exact ABN join required | Fundraising-intensive; international health programs; evaluation/research evidence | Exercises program decomposition, evidence/evaluation selection and cross-border partner scope; do not convert evaluation evidence into an impact score. |

### Development and holdout partition

The partition is frozen before implementation:

* **Development (7):** The Smith Family; Australian Red Cross Society; Australian Communities Foundation Limited; Australian Conservation Foundation Incorporated; Mission Australia; World Vision Australia; The Fred Hollows Foundation.
* **Untouched holdout (3):** Landscape Recovery Foundation Ltd.; Indigenous Literacy Foundation Ltd.; Life Without Barriers.

For holdouts, this packet records only identity, role and expected source families. No hand-labelled semantic answer, prompt tuning, parser tuning or repeated inspection is permitted. Detailed semantic assessment opens only for the formal holdout evaluation. If a holdout is inaccessible or lacks lawful evidence, record that coverage state and do not replace it during coding.

## 3. Source-family reconnaissance and bounded source plan

Reconnaissance was limited to public landing pages and register/search results sufficient to check that each candidate has usable lawful evidence. PR A must register sources before routine acquisition and must not bulk-download or archive material in this tranche.

Expected families for every subject are:

1. ACNC Charity Register, Annual Information Statement and available program records (`https://www.acnc.gov.au/charity/charities`);
2. ABR/ABN Lookup exact identity and current status (`https://abr.business.gov.au/`);
3. ATO DGR/tax-concession records where applicable (`https://www.ato.gov.au/`);
4. the charity's official website and program/service pages; and
5. the charity's annual or audited financial report where lawfully available.

Additional expected families are scoped by case:

| Case | Additional public source families to register if available |
|---|---|
| Smith Family | Education evaluation/research and government program material |
| Red Cross | Lifeblood and regulated first-aid/training material; annual report |
| Landscape Recovery Foundation | Project reports, environmental research and relevant land-management material |
| Indigenous Literacy Foundation | Literacy research and community/language material subject to cultural governance and reuse review |
| Australian Communities Foundation | Grant/fund descriptions and independent philanthropy research |
| Australian Conservation Foundation | Submissions, regulator/government material and credible environmental research |
| Mission Australia | NDIS, My Aged Care, housing/service regulator and evaluation material |
| Life Without Barriers | NDIS, child-protection, aged-care and other regulator/compliance material |
| World Vision Australia | DFAT/ACFID accreditation and program evaluation material |
| Fred Hollows Foundation | DFAT/ACFID material and independent eye-health evaluation/research |

Source authority remains proposition-specific. Charity websites may describe current programs; ACNC/ABR may establish registration and identifiers; a regulator may establish a formal decision; research may support an evaluation method or outcome claim. No source is authoritative for every proposition. Source rights, cultural governance, access terms, effective dates, retrieval metadata and publication eligibility are recorded before acquisition.

## 4. Frozen field/task method matrix

Each material output has one initial method. The method controls the first implementation; changing it requires a recorded decision and evaluation result.

| Material output/task | Initial method | Frozen boundary |
|---|---|---|
| Organisation identity and legal/current name | Deterministic | Validate ABN, exact ACNC/ABR joins and source identifiers; names/domains are candidates only. |
| External identifiers (ABN, ACN, DGR identifiers) | Deterministic | Preserve source-native values and evidence; reject invalid or conflicting joins. |
| Organisational/group scope | Human-reviewed | Build candidate legal/operational relationships mechanically, then review group, subsidiary, branch, trustee and confederation boundaries. |
| Program/service identification | Model-assisted | Extract evidence-bound candidates from structured/segmented source material; no phrase-specific Python rules. |
| Program normalisation/decomposition | Model-assisted | Judge whether candidates are material programs/services and retain evidence/rationale. |
| Geography (organisation, program, site) | Deterministic | Parse structured addresses/regions and exact source fields; narrative geography remains unresolved or model-assisted in a later task. |
| ACNC classifications | Deterministic | Preserve source-reported categories, subtype and activity fields; do not rewrite them as CharityGraph labels. |
| ATO/DGR facts | Deterministic | Preserve exact fund, item, effective dates and source status. |
| CLASSIE subjects | Model-assisted | Multi-label assignment with evidence, rationale and confidence; version/licence must be recorded. |
| CLASSIE populations | Model-assisted | Assign only where the evidence supports population scope; avoid demographic inference from names or geography. |
| CharityGraph operational activities | Model-assisted | Use the native faceted vocabulary; distinguish purpose, activity, channel and campaign. |
| UN SDG alignment | Model-assisted | Multi-label, evidence-backed alignment; no claim of UN endorsement or indicator result. |
| Evidence/relevance selection | Model-assisted | Select bounded evidence spans/records for a task; preserve rejected/competing evidence where material. |
| Rationale | Model-assisted | Generate an evidence-linked explanation; never substitute unsupported prose for a locator. |
| Confidence/strength | Model-assisted | Record task-level confidence separately from evidence quality and authority. |
| High-consequence, cultural or materially adverse claims | Human-reviewed | Require specialist/cultural review or remain governed unresolved; no inference from silence. |
| Coverage/absence state | Deterministic | Preserve `resolved`, `unknown`, `not_attempted`, `not_applicable`, `insufficient_evidence`, `withheld` and `failed` distinctly. |
| Lineage and identifiers | Deterministic | Content hashes, exact directed edges and replay/idempotency are mechanical invariants. |
| Model/provider/cost metadata | Deterministic | Record task, prompt/template, provider/model, parameters, reservation, actual, cache and output lineage. |
| Full outcome scoring, sector-wide observation and universal ranking | Deferred | Not part of this slice. |

Ordinary semantic ambiguity is handled through model judgment, evidence, rationale and confidence. It is not converted to `unknown` by keyword rules.

## 5. Frozen Phase 1 acceptance scorecard

The review panel records case-level results and the aggregate below. A critical mechanical, provenance, cultural-governance or public-contract failure fails the slice regardless of any aggregate score.

### Mechanical and provenance

* **Identity:** 10/10 ABNs pass checksum validation and exact ACNC/ABR joins; no name-only binding promotes a subject and no duplicate subject is minted.
* **Source joins:** every accepted source fact has a valid source record and evidence locator; conflicting identifiers remain review candidates.
* **Artefacts:** identical content creates one content-addressed artefact; duplicate artefacts for identical bytes = 0.
* **Lineage:** 100% of accepted observations, assertions, assignments and decisions have complete directed lineage back to source/evidence. No orphan or reversed controlled edge is accepted.
* **Replay:** two clean replays of the same run produce the same IDs and projections, no duplicate artefacts, and no additional model charge except an explicitly recorded operational receipt.
* **Coverage states:** 100% of in-scope fields use the correct distinction among `unknown`, `not_attempted`, `not_applicable`, insufficient evidence, withheld and failure.
* **Model lineage:** every model call has task, input evidence, prompt/template, provider/model, output validation and cost lineage; ordinary tests use fake or recorded providers.
* **Boundary:** public contract 0.5 manifest checksum remains `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`; public Data and Viewer publication count = 0.

### Programs and scope

On the seven development cases, a pre-run reviewer-approved material-program set is used:

* material-program recall >= 90% and precision >= 80%;
* false program creation <= 1 total across the set;
* duplicate/over-fragmented program candidates <= 10% of candidates; and
* organisation-versus-program/site scope accuracy >= 90%, with zero critical scope errors.

On the three holdouts, recall >= 80%, precision >= 75% and zero critical scope errors are required. The formal reviewer may mark a case unresolved when evidence is insufficient; that is not a false program.

### Classification and useful judgment

* ACNC and ATO classifications are source-preserved in 100% of cases; no model or native label overwrites a source-native value.
* For CLASSIE subjects and populations, every case with sufficient evidence has at least one pre-registered required/strongly expected or acceptable secondary assignment: >= 6/7 development cases and >= 2/3 holdouts. Prohibited assignments = 0. Multi-label assignments are retained where the reviewer identifies more than one defensible concept.
* For CharityGraph operational activities, the same 6/7 development and 2/3 holdout useful-judgment thresholds apply. Purpose, beneficiary, activity, channel and campaign are not collapsed.
* For SDG alignment, >= 5/7 development and >= 2/3 holdout cases with adequate evidence have at least one supported alignment; unsupported SDG indicator or impact claims = 0.
* Inadequate `unknown` is an error: in cases the reviewer marks sufficiently evidenced for an ordinary classification, an unjustified `unknown` = 0 tolerated cases. Genuine absence/insufficiency remains explicitly unresolved.
* All cultural-authority, materially adverse, safeguarding-adjacent and material contradiction cases receive human review (100%).

### Coverage and development/holdout

* At least 90% of in-scope fields are attempted on development cases and 80% on holdouts; every remainder has an explicit coverage state.
* Extraction/model failure is <= 10% of attempted fields in each partition.
* Accepted claims and assignments have a 100% provenance floor; unresolved records retain evidence of the attempt and reason for non-resolution.
* The development-to-holdout gap is <= 15 percentage points for each primary program/classification measure. A gap above 15 points, two category failures, or any critical invariant failure stops the slice for redesign.

## 6. Experimental economics ceiling

The ten-charity slice has a separate hard experimental ceiling of **AU$25 aggregate** for explicitly approved real-model evaluation only. This is a small fraction of the approved AU$100 production cohort envelopes and is not a ten-charity entitlement or a new production budget. The planning average is AU$2.50 per subject, not a guarantee or forced allocation.

Before any paid call, Builder must produce a dry-run projected-cost report, reserve through the existing SQLite economics contracts, and enforce the hard ceiling. Actuals, credits, releases and overruns reconcile in SQLite. Fake or recorded providers are mandatory for ordinary software tests. No paid calls are made in this documentation tranche.

## 7. Stop and return conditions

Implementation must stop and return for redesign if:

* a second correction pass reveals the same conceptual error class;
* Python begins accumulating phrase-specific language heuristics;
* subject or program scope cannot be represented with approved primitives;
* provenance cannot be reconstructed mechanically;
* holdout failure materially exceeds the frozen thresholds or gap;
* model economics would exceed AU$25 without an approved amendment;
* implementation would require changing public contract 0.5;
* an external taxonomy licence or version issue blocks lawful use; or
* a culturally sensitive or consequence-heavy claim requires a governance decision not already made.

Unresolved cases remain governed unresolved records. They are never forced into a value to satisfy the scorecard.

## 8. Implementation handoff

PR A must begin from the then-current Data and Builder `main`, cite this packet and the canonical authorities, and declare its allowed files, fixtures, exclusions and tests. It may implement source/evidence registration and content-addressed artefact primitives only. PR B–F remain sequenced as in `IMPLEMENTATION_PLAN.md`; no PR in this packet may publish Data or Viewer.

