# CharityGraph Roadmap

**Status:** Canonical product/engineering sequence, version 2.1-draft

## Outcome

Build a one-stop shop for structured, governed Australian charity data: an integrated projection over linked evidence, observations, measurements, assertions, relationships, decisions and coverage—not a single semantic slice or opaque charity record.

## Delivery sequencing principle

Acquire broadly once. Preserve source-native evidence. Freeze a reusable charity evidence corpus. Assemble one or more task-specific semantic packets from that corpus. Apply one or more cost-efficient semantic passes. Persist independently governed domain knowledge. Compile analyst/public projections from that governed knowledge.

Acquisition is charity/source oriented; semantic interpretation is domain/profile oriented. A physical provider call may bundle compatible logical tasks for economics, but each logical output retains independent task identity, schema/profile identity, subject/scope, evidence binding, validation, lineage and governed disposition. The North Star card is a projection over governed knowledge, never a stored mega-record or raw model output.

## Phase 0 — Documentation, authority and baseline

Retain the existing baseline intent. Exit requires authority and supersession to be explicit, immutable release 0.5 unchanged, `NORTH_STAR_TARGET_CARD.md` installed, and implementation sequencing visibly mapped to the complete product scope.

## Phase 1 — Foundation spine

North Star emphasis: 1 Identity & regulatory status; 2 Purpose, mandate & cause; 20 Evidence, coverage, freshness & corrections; plus shared subject, scope, relationship, measurement and taxonomy primitives. Existing program/service v3/v3.1 work is valuable foundation-domain work, not the product itself.

## Phase 2 — Baseline source acquisition and reusable charity evidence corpus

For each charity, attempt a reusable baseline source set before domain-specific semantic work: ACNC Register, ACNC AIS, ATO DGR, official website, latest annual report, Wikipedia/Wikimedia context, and PFRA or another applicable fundraising-industry registry. Specialist sources remain claim-, risk- or domain-triggered by central sourcing governance; principal evidence families describe product needs and do not authorise a section to discover sources. Preserve source-native structured observations without routing regulator fields through an LLM merely for rediscovery.

Architecture: acquire broadly once → preserve source-native evidence → freeze reusable charity evidence corpus → assemble bounded semantic packets from that corpus. Corpus completeness is claim-family-specific. Record acquisition state (`attempted`, `acquired`, `unavailable`, `access_failed`, `parsing_failed`, `not_applicable`, `not_attempted`) by source family, claim family and subject/scope. `COMPLETE_ENOUGH` for program discovery is not whole-North-Star completeness.

## Phase 3 — Complete-card domain/graph hardening

CharityGraph is now in the Phase 3 domain/graph-hardening stage of the
complete-card reality slice. Use approximately 8–12 deliberately varied
charities and pressure-test the North Star claim families with explicit
missingness when unavailable or deferred. Generic whole-card feasibility is
substantially reality-tested; the active question is whether the architecture
can persist and project the cross-domain graph required by the Data product.

Phase 3 is not a licence to treat program/service discovery as the product.
Its graph deliverable is shared subject/scope ownership and directed,
evidence-bound activity relationships that distinguish operating, delivery,
funding, sponsorship, partnership, auspice and network/context roles. These
semantics are cross-domain infrastructure for programs, fundraising, finance,
capacity, governance, outcomes and ecosystem data: attach each observation to
the lowest evidence-supported scope, and do not infer proposition ownership
from domain provenance.

The immediate bounded pressure sequence is: a direct-service case stressing
sections 6 Participation, 11 Capability/capacity/access/availability and 13
Memberships/schemes/registrations/accreditations; an authoritative section 16
Conduct/adverse matters/compliance case; an evaluation-rich section 18
Outcomes/impact/evaluation case; and then the first bounded CharityGraph
Native induction once the observation corpus is sufficiently diverse.
Fundraising, ethos and other specialist profiles remain in scope but are not
blockers for that sequence.

The direct-service structure for sections 6/11/13 has been boundedly pressure-
tested. Section 16 has a bounded conduct/compliance design and pressure-test
history; its specialist regulator acquisition is experimental ground-truth
material, not production sourcing precedent. The generic Compact → specialist
lens architecture for section 18 has also been reality-tested sufficiently to
park the section, with bounded precision/recall questions remaining. Section 15
positions/commitments/implementation has completed its broad V1E Semantic Lab
and is now architecture-validated, semantic-boundary-tested and parked—not
production-complete. The permissive and corrected prompt sets are not
canonical production prompts; further polishing is deferred. Paid
interruption-safe/restart-safe execution remains a later Factory/scaling gate,
not a prerequisite for one-shot Labs. No section is production-complete.

### Phase 3 exit gate

Exit requires sufficient bounded evidence that:

- direct-service structure works across sections 6/11/13;
- subject/scope ownership survives shared-domain cases;
- operator, deliverer, funder, sponsor, partner, auspice and network roles
  survive extraction, persistence and projection;
- section 16 has a bounded high-consequence representation and approved review
  path;
- section 18 represents evaluation evidence without collapsing change,
  contribution and causation;
- claim-family coverage and material missingness states work; and
- interruption-safe execution exists before paid cohort scaling.

No universal accuracy, QA, acceptance-score or coverage threshold is implied.
Phase 4 packaging/economics and especially Phase 5 Top-100 full-card scaling
are subsequent stages, not the immediate next action merely because generic
whole-card extraction has been demonstrated.

Section 19 remains a six-lens architecture, not a completed milestone: source-
native ACNC/ATO foundations exist, SDG and CharityGraph CLASSIE have bounded
experimental evidence, and CharityGraph Native induction remains an upcoming
empirical/implementation step. “Section 19 first reality-tested” does not mean
all classification lenses are complete.

## Phase 4 — Cross-domain semantic packaging and economics

Experimentally compare one large packet, compatible domain bundles and narrower task packets from the same frozen corpus. Candidate bundles include programs/populations/geography/participation; fundraising/workforce relationships/finance; governance/affiliations/ethos; finance/grants/contracts/resource relationships; programs/outcomes/evaluation; and programs with capability/availability. Measure semantic yield per dollar, not merely calls avoided. Never collapse independent logical outputs because calls are bundled.

## Phase 5 — Top-100 full-card claim-family build

The milestone is the **Top-100 full-card claim-family build**: attempt the complete North Star surface for literal ACNC donation ranks 1–100, with risk-tiered depth and explicit coverage states for every applicable claim family. Success means baseline source coverage attempted, applicable families attempted, governed results retained, missingness explicit, high-risk work reviewed/deferred appropriately, and economics/failures measured—not every field populated.

### Phase 5 historical/current program-discovery run

The recently halted run used literal ACNC donation ranks 1–100; it produced 60 new Terra response artefacts, reused 3 exact prior Terra-A results, and had 63 available semantic results in closeout analysis. It had 60 structurally valid results, 54 whole-output quote-valid results, 287 parsed proposals, 72 program-task `COMPLETE_ENOUGH` packets and 28 `PARTIAL` packets. One in-flight attempt (ABN `48321126727`) had no response artefact and indeterminate billing status. It was intentionally halted during roadmap realignment, did not start ranks 101–1000, made no validity/quality/impact/ROI/recommendation judgements, and changed no Builder, Data or Viewer files.

Here `COMPLETE_ENOUGH` was sufficient only for the program-discovery task. Valid outputs remain reusable Section-3 material where semantic identity permits; this run does not satisfy the future Top-100 full-card milestone and must not be rerun merely because sequencing changed.

## Phase 6 — Risk-gated depth and specialist profiles

Deepen ethos/stance, conduct/adverse matters, commitments/implementation, outcomes/evaluation/causal claims, sensitive populations, Indigenous data governance, specialist capacity/availability and direct-observation profiles. These domains must already have been reality-tested at an appropriate bounded risk level in Phase 3.

## Phase 7 — Correction and public vNext

Align open-correction and public-release-candidate work while preserving immutable releases, contestability, correction lineage, coverage disclosure, rights/privacy/publication gates, simple Viewer projections and coordinated Data/Viewer acceptance.

## Phase 8 — Scaled breadth

Scale next 1,000, then 10,000, then the demand-triggered national tail. Model tier, source breadth, semantic depth, review intensity and refresh cadence may vary by cohort, but lower cohorts must not silently become program-discovery-only without an explicit governed policy.

## Parallel track — CharityGraph Playbooks

Playbooks is a separate first-class product alongside Builder, Data and Viewer. It consumes governed CharityGraph public knowledge and is not generated as canonical knowledge by Builder. Viewer may later provide contextual Playbook launch affordances, while external AI execution remains user-selected and outside canonical CharityGraph knowledge. This track must not delay complete-card reality testing or public-vNext foundations, and Playbooks is not a release gate for Builder/Data vNext unless a future explicit decision says so.

### Playbooks P0 — Product governance

This work is approved and underway through the canonical product and governance documents. It establishes fourth-product status, method/invocation/output separation, model neutrality, open licensing intent, versioning and corrigibility, Official/Community distinction, contribution and attribution principles, and privacy and feedback boundaries. The initial Playbooks repository and contract were established at commit `6466e04`; no production catalogue is claimed.

### Playbooks P1 — Establish product repository and contract

The initial `charitygraph-playbooks` product/repository, Playbook contract, base epistemic policy, versioning, CC BY 4.0 content licence, contribution model, machine-readable definition schema and Official/Community lifecycle are established at commit `6466e04`. Detailed invocation packaging, production release lifecycle and catalogue work remain future refinements in P1; this does not mark P2, P3 or P4 complete.

### Playbooks P2 — Seed and evaluate a small official collection

Develop approximately 5–7 high-value Playbooks against representative CharityGraph use cases such as peer/competitor landscape, program differentiation, partnership discovery, service/ecosystem mapping, board or sector briefing, service-gap/growth exploration and a funder due-diligence starter. These are candidate jobs, not immutable scope.

Evaluation should test representative organisations/programs across several commodity AI systems. Measure retrieval of intended CharityGraph material; unsupported or overconfident conclusions; preservation of scope, provenance and uncertainty; parameter usability; useful analytical output; provider/model sensitivity; and failures attributable separately to Data, the Playbook method and external model/retrieval. No fixed thresholds are defined yet.

### Playbooks P3 — Viewer integration

After public vNext provides stable, addressable organisation/program/service representations, Viewer may expose contextual **Use with AI** affordances. These may suggest relevant Playbooks, pre-populate known CharityGraph context, ask only for missing parameters, generate portable invocations and optionally package relevant public context for models without reliable retrieval. Private strategic parameters should remain client-side where practical. Viewer is neither the Playbooks authority nor a hosted inference service.

### Playbooks P4 — Community contribution

Introduce low-friction pathways to suggest analytical questions, submit methods or prompts, refine/evaluate candidates, propose corrections and contribute without GitHub/YAML/JSON knowledge. Preserve contributor attribution, affiliation/conflict disclosure, Community versus Official status, governed adoption/adaptation, evidence-over-voting and contribution lineage.

### Playbooks dependencies

P0/P1 can proceed independently of full-card Builder implementation. P2 can use available representative CharityGraph data and becomes more valuable as full-card coverage improves. P3 depends materially on stable public vNext addressability and suitable Viewer/Data projections. P4 should follow enough P2 experience to establish a credible contribution/evaluation process.

## Continuous workstreams

- North Star coverage audit
- source-family and claim-family coverage by cohort
- cross-domain evidence reuse and LLM bundling/economics
- model-tier routing and interruption-safe execution
- right-tail packet sufficiency and corpus refresh/reuse policy
- scheme research, source rights/privacy/security and Indigenous governance
- model evaluation, open curation, documentation and ADR maintenance
- Playbook analytical-method evaluation, cross-model portability and method/version reproducibility
- Playbook contribution, attribution, privacy of user parameters, feedback classification and epistemic-policy maintenance

## North Star ↔ roadmap matrix

| North Star section | First reality-tested phase | First scaled phase | Principal evidence families | Typical method |
|---|---|---|---|---|
| 1 Identity & regulatory status | 1 | 5 | ACNC, ATO, constitutional/registry records | deterministic + mixed |
| 2 Purpose, mandate & cause | 1 | 5 | ACNC, governing documents, official site | mixed |
| 3 Programs, services, projects & campaigns | 3 | 5 | official site, reports, ACNC, campaign sources | model-assisted + review |
| 4 Populations & beneficiaries | 3 | 5 | AIS, official site/reports, program evidence | model-assisted + review |
| 5 Geography | 3 | 5 | ACNC, sites, reports, program evidence | mixed |
| 6 Participation | 3 | 5 | official site, memberships, volunteer/event sources | mixed |
| 7 Fundraising & resource mobilisation | 3 | 5 | fundraising sources, official site/reports | model-assisted + review |
| 8 Finance & resource flows | 3 | 5 | AIS, filed accounts, annual reports, grants | deterministic + mixed |
| 9 Governance | 3 | 5 | AIS, annual reports, governing instruments | mixed + review |
| 10 Workforce | 3 | 5 | AIS, reports, workforce/contractor evidence | mixed |
| 11 Capability, capacity, access & availability | 3 | 5 | official service pages, reports, registers | mixed + review |
| 12 Relationships & ecosystem | 3 | 5 | reports, contracts/grants, partner evidence | model-assisted + review |
| 13 Memberships, schemes, registrations & accreditations | 3 | 5 | registries, scheme authorities, official sources | deterministic + mixed |
| 14 Ethos & institutional identity | 3 | 6 | governing instruments, affiliation, self-description | human/risk-reviewed |
| 15 Positions, commitments & implementation | 3 | 6 | policies, commitments, implementation evidence | mixed + review |
| 16 Conduct, adverse matters & compliance | 3 | 6 | regulators, proceedings, official responses | human/risk-reviewed |
| 17 Notable context & institutional history | 3 | 5 | contextual sources, reports, inquiries | mixed + review |
| 18 Outcomes, impact & evaluation | 3 | 6 | evaluations, studies, reports | human/risk-reviewed |
| 19 Classifications & semantic lenses | 1 | 5 | ACNC, ATO, SDG, governed taxonomies | deterministic + model-assisted |
| 20 Evidence, coverage, freshness & corrections | 1 | 5 | all receipts, locators, review/correction records | deterministic + human review |

## Explicit non-goals for early phases

- replacing SQLite with a network database;
- completing every taxonomy before a reality slice;
- public wiki-style direct edits;
- universal charity ranking or impact score;
- teaching deterministic Python to interpret unrestricted prose;
- migrating all archaeology into canonical state;
- changing immutable release 0.5;
- building a public API before download/Viewer and analyst workflows prove demand.

## Semantic feasibility checkpoint (2026-08-31)

Native induction sequencing and the parked V1–V3 findings are governed by [CHARITYGRAPH_NATIVE_ARCHITECTURE.md](CHARITYGRAPH_NATIVE_ARCHITECTURE.md). The next Native experiment remains deliberately unspecified; further Native experiments require separate experimental authorisation.

The generic whole-card feasibility and packet-economics question is now
substantially reality-tested across rich, sparse-regulator and modest-website
evidence shapes. This does not establish universal validity, completeness or
model-performance guarantees.

The next bounded domain-pressure sequence is: a direct-service case emphasising
sections 6, 11 and 13; an authoritative conduct/adverse/compliance case for
section 16; an evaluation-rich case for section 18; and then the first bounded
CharityGraph Native induction once the observation corpus is adequately
diverse. Fundraising, ethos and other specialist profiles remain on the roadmap
but are not blockers for those experiments.
