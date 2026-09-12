# Phase 6 capability inventory and product-value shortlist

**Status:** Working planning recommendation; the product owner selected the three leading capabilities for design only; not product, semantic, or implementation authority
**Date:** 12 September 2026
**Scope:** Phase 6 Tranches 0-1 and Tranche 2 design selection; no live slice execution or implementation authorized

## Purpose and decision boundary

This inventory converts the proposed Phase 6 specialist domains into finite product
hypotheses. It is subordinate to the canonical authorities listed in
[DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md), the [North Star target card](NORTH_STAR_TARGET_CARD.md),
and the [integrated product and data model](INTEGRATED_PRODUCT_AND_DATA_MODEL.md).
It does not change those authorities, define public schema, or authorize live work.

The product owner selected outcomes/evaluation, commitments/implementation, and
capacity/access/availability for **reality-slice design only**. This is not approval
to execute Tranche 3. Conduct/adverse history remains a strong deferred fourth
candidate. The designs are in [PHASE6_REALITY_SLICE_DESIGNS_2026-09-12.md](PHASE6_REALITY_SLICE_DESIGNS_2026-09-12.md).
Each slice requires separate product-owner execution approval. No provider calls,
new source acquisition, semantic experiments, or production implementation are part
of this inventory.

## Baseline and evidence

Tranche 0 confirmed that the Builder Direct Service V1.2 branch
(`d9049e9517a92b5c87fa8f4b39aeb00bd8f44ca9`) and Data closeout branch
(`5703b2e99a7caf4d558e96259c434746b54b7b93`) are based on their respective refreshed
`origin/main` refs (`77c2995cc05c6fc058f494fe28ddadc8d917b451` and
`56516cfa8c9e86ff67ca53541480e32f744f0690`). The full Builder `pytest -q --tb=no`
suite exited successfully, with one skipped test and three deprecation warnings; no
current suite failures were present. The failures recorded in the frozen Luna review
were not assumed to be current or fixed by assertion; this full run found no failures.
The protected Data v0.5 schemas, releases and
contract were unchanged. Existing Direct Service closeout facts, exclusions, provider
crossing controls, cost reporting and Luna review provenance remain documented. This
does not claim production readiness, governed promotion, or completion of broader
Phase 5 Top-100 work.

Evidence examined includes `NORTH_STAR_TARGET_CARD.md` sections 11, 14-18 and 20,
`INTEGRATED_PRODUCT_AND_DATA_MODEL.md`, `DOMAIN_PROFILE_INDEX.md`, Builder's
`src/charitygraph/contracts/direct_service.py`,
`src/charitygraph/contracts/direct_service_wire.py`,
`src/charitygraph/contracts/conduct_compliance.py`, and
`src/charitygraph/phase5_preflight.py`. A North Star section marked reality-tested or
a structurally valid contract is not evidence that the semantic capability is useful
or correct in real-world use.

## Capability matrix: product hypotheses

| ID and capability | User questions enabled | North Star sections | Likely source families | Usefulness hypothesis | Likely economics | Recommended disposition |
|---|---|---|---|---|---|---|
| A. Outcomes and evaluation | What outcomes are claimed and measured? Is evidence activity, output, observed outcome, contribution, or causal evidence? Who/what/time does it apply to? What limits are visible? | 18 Outcomes, impact & evaluation; 20 Evidence and uncertainty; 3 Purpose/activities; 6 Population | Charity annual and impact reports; evaluation and research reports; program dashboards; government or commissioned evaluations; first-party measurement publications | A well-scoped evidence trail could let analysts distinguish claimed impact from measured change and causal support, improving on directory-level descriptions. Value is high if limitations and null/mixed results remain visible. | High potential product value; high evidence review and synthesis cost. Start with a small, overlapping existing-corpus cohort and narrow propositions; do not assume unit economics before measuring adjudication burden. | `SELECT_FOR_REALITY_SLICE` — selected for design only; execution not authorized |
| B. Commitments versus implementation | What policy, principle, pledge, target, or obligation exists? What supports intention, claimed implementation, observed practice, compliance, or outcomes? At what scope? Is evidence absent or evidence of non-implementation? | 15 Positions, commitments & implementation; 14 Governance; 16 Conduct/compliance; 20 Evidence and uncertainty | Constitutions, policies, strategies, public commitments, progress reports, annual reports, regulator records, independent audits and contractual documents | Separating what an organization says from what it has done can answer material accountability questions while preventing policy text from being mistaken for implementation. | Medium-high value; material human review and source-role classification cost. Narrow propositions may permit economical typed extraction, but adjudication is likely dominant. | `SELECT_FOR_REALITY_SLICE` — selected for design only; execution not authorized |
| C. Capacity, availability and access | What is offered, to whom and where? What eligibility/referral/access conditions apply? Is it currently available? Is capacity known, bounded, waitlisted, unavailable, occupied, or unknown? | 11 Capability, capacity, access & availability; 3 Purpose/activities; 4 Beneficiaries; 20 Evidence and uncertainty | Current service directories and intake pages; first-party service descriptions; referral and eligibility guides; dated operational updates; official waitlist or capacity notices | Current, scoped access information could make service discovery more actionable than static service descriptions, if freshness and unknown status are clear. | Medium-high usefulness; ongoing temporal verification and refresh cost may be significant. Reuse existing frozen Top-100 sources first; no fresh acquisition is implied. | `SELECT_FOR_REALITY_SLICE` — selected for design only; execution not authorized |
| D. Conduct and adverse history | Is there authoritative adverse information? Was it an allegation, investigation, finding, sanction, appeal, remediation, or historical event? Which entity/program/time does it concern, and what is its status? | 16 Conduct and compliance; 17 Notable context; 20 Evidence and uncertainty | Charity regulator and other official regulator records; courts, inquiries and commissions; official findings, appeals and organization responses/remediation | Properly qualified adverse context can materially aid diligence while avoiding a notoriety score or collapsing allegations into findings. | Potentially high diligence value but high-right-tail legal, correction, reputational and specialist-review cost; low tolerance for error. | `DEFER_GOVERNANCE` — strong fourth candidate; requires rights, correction, response and specialist controls before a slice |
| E. Ethos, values and stance | What values or affiliation does the organization explicitly describe? What positions are explicit? Which claims are self-description, and which would be inference? What operational implications are actually evidenced? | 14 Governance; 15 Positions, commitments & implementation; 20 Evidence and uncertainty | Constitutions, first-party policies and annual reports; explicit statements; affiliation/member-scheme records | Explicit, attributed self-description can add useful context, but inferred ethos has uncertain incremental value and can easily overgeneralize from affiliation or beneficiaries. | Moderate extraction cost; ongoing human attribution and scope review. Broad inference could create costly correction and trust risks. | `DEFER_UNTIL_PRODUCT_VALUE_PROVEN` |
| F. Sensitive-population and Indigenous governance | What evidence concerns a sensitive population or Indigenous community? Who has authority to describe, govern, consent to, access, or publish it? What restrictions and community-specific context apply? | 4 Beneficiaries; 6 Population; 11 Access; 20 Evidence, uncertainty and cultural governance; relevantly 16 | Consented organization/community sources; Indigenous-controlled sources and governance authorities; applicable rights, consent and community protocols | Could support important questions only where information is governed under legitimate community authority and consent. A generic open-web extraction approach is not an acceptable proxy. | High governance, relationship, consent, access-control and stewardship cost; economics cannot be responsibly estimated before governed design. | `DEFER_GOVERNANCE` |

## Capability matrix: support, gaps and controls

| ID | Existing model support | Missing model support | Semantic risk | Source-authority risk | Scope/grain risk | Human-review requirement | Model requirement |
|---|---|---|---|---|---|---|---|
| A | Shared observation, assertion, measurement, evidence, scope and evaluation concepts are present in the integrated model; North Star section 18 describes study design, population, denominator, comparator, uncertainty and limitations. Builder has generic evidence/observation primitives. | No demonstrated end-to-end outcomes/evaluation profile covering typed epistemic class, population/program scope, study design, limitations, contribution/causation and null/mixed results through governed projection. | High: activity/output/outcome/contribution/causation can be collapsed; attribution and counterfactual claims are difficult. | High: first-party impact claims, commissioned work and independent evaluation have different roles and authority. | High: study population, intervention, period, site, program and entity boundaries must be explicit. | Independent human semantic adjudication for every slice subject and proposition, with corrections or rejection dispositions and a shared rubric. | Typed extraction may use the lowest-cost adequate model; difficult evaluation synthesis is not assumed. A stronger model would require a separately justified task and comparison. |
| B | General assertion/commitment and evidence concepts; North Star section 15 explicitly distinguishes statements, commitments, claimed implementation, observed practice, verified compliance and outcome. | A validated end-to-end profile distinguishing aspiration, voluntary pledge, policy, contractual/statutory obligation, claimed action, observed practice and compliance; explicit non-evidence and temporal status handling. | High: intention, implementation, compliance and outcomes are materially different propositions. | Medium-high: official obligation, first-party claim, independent audit and regulator finding cannot be flattened. | High: organisation-wide statements may not apply to a program, site, partner, period or cohort. | Independent human review of every proposition and its epistemic class, source role, time and scope. | Typed extraction/classification only; model output remains a candidate. No autonomous conclusion that implementation or compliance occurred. |
| C | Builder Direct Service V1.2 contract/wire types cover service offer, eligibility, access pathway, current availability and capacity measure; explicit missingness and representation have bounded test coverage. | Reality-tested semantic support for freshness, actual availability versus description, capacity states, site/program granularity and source/date conflict. The V1.2 representation experiment does not establish these. | Medium-high: offer, activity, operational capacity and current availability may be conflated. | High: static first-party pages and dated/live operational notices differ in authority and freshness. | High: service, program, site, catchment, intake channel and time period must not be generalized to organization level. | Independent human review for every subject's availability/capacity claims and evidence date/scope. | Typed extraction with explicit evidence locators; use the lowest-cost adequate model, with no model authority over freshness or truth. |
| D | Builder `conduct_compliance.py` includes proposition class/procedural status, subject, owner, time and evidence structure for allegations through findings and responses. | Complete lifecycle, legal/right-of-reply and correction workflows; appeals, supersession, publication decisions, identity resolution and specialist governance are not established by the structure contract. | Very high: allegation/finding/sanction/remediation and current status are easy to misstate. | Very high: authority, jurisdiction, finality, appeal, source correction and response require specialist judgment. | Very high: named legal entity, affiliate, service, event and period must be resolved carefully. | Specialist human review before any external use, including adverse-class and subject-identity review. | Model may assist evidence extraction only; it cannot decide status, liability, materiality or publication. |
| E | General assertions and organization positions can carry attributed claims; North Star section 14 warns against inferring ethos from beneficiary identity or parent/affiliate relationships. | No safe, validated general ethos-inference profile; explicit affiliation/stance boundaries, attribution and downstream propagation require specific policy. | High for inferred ethos and operational implications; lower for narrow attributed quotations. | Medium: affiliation registries and self-description vary in authority and meaning. | High: entity, affiliate, service-user and parent scopes must stay separate. | Human review for stance and any affiliation semantics; explicit self-description may be extracted with attribution but must not be converted to inferred ethos. | Limited extraction of explicit claims only; no model-generated ethos characterization. |
| F | Generic subject, population, evidence and access-control concepts exist. North Star and product principles recognize cultural governance, rights, consent and publication limits. | Specific authority, consent, sovereignty, cultural protocols, access/publication controls and community stewardship are not established by generic primitives alone. | Very high: category imposition, context loss and inappropriate inference can cause harm. | Very high: only legitimate Indigenous/community-controlled authorities can establish relevant governance and permissions. | Very high: community, people, place, organization and collective rights do not reduce to ordinary organization fields. | Indigenous/community governance and designated data stewards must define authority, consent, use and review before any model processing; LLM judgment cannot substitute. | No model requirement is assumed. Any later model assistance is subordinate to approved governance, consent and controls. |

## Gate 1 product-owner decision and disposition

The product owner selected **A. Outcomes and evaluation**, **B. Commitments versus
implementation**, and **C. Capacity, availability and access** for reality-slice
design. They address distinct analyst needs, have meaningful potential to improve on ordinary
directory/source research, and expose complementary epistemic challenges. Capacity
has bounded V1.2 structural support but still needs reality evidence for semantic
truth, freshness and practical utility. The other two have high prospective value
and important representation gaps. Conduct/adverse history is a strong fourth, but
its unusually high governance and correction burden means it should not displace any
of the three absent evidence of materially greater product value.

This design selection is not execution approval. The separate Tranche 2 designs
specify the cohort, propositions, legal scopes, evidence/missingness rules, prohibited
inference, acceptance criteria, review, economics, stopping rules and controls. Each
slice still needs its own explicit authorization before execution. If authorized, use
only the frozen Top-100 corpus and do not acquire sources to fill a cohort.

## Authority and status

This document is a point-in-time product hypothesis inventory. Its usefulness and
economics are unmeasured expectations, not observed results. It contains no normative
product decision, public contract, semantic acceptance or permission to execute work.
The product-owner design selection is recorded in planning status; it does not
constitute an execution authorization. Broader Phase 5 Top-100 remains active; design
can proceed before its completion, while each live experiment, production
implementation, Phase 7 and scale remain separately gated.
