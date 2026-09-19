# Bitemporal governed-knowledge architecture

**Status:** Implemented contract and canonical architecture note, version 1.0

**Date:** 19 September 2026

**Scope:** Internal Builder governed knowledge and its future projections. This does not alter public v0.5, authorise Scale S0 recovery, or change any source, provider, release or promotion policy.

## 1. Purpose and terms

CharityGraph must answer two different questions without silently substituting one for the other:

- **knowledge state at K:** which governed records and coverage states had entered CharityGraph's governed record by transaction-time instant K; and
- **current belief valid at V:** which current governed records have supported world-valid intervals covering V.

The combined question is explicitly `knowledge_state_at(K)` followed by valid-time filtering. It is never inferred from retrieval time, a record's age, or a newer source alone. These are bounded read models over append-only records and directed supersession lineage; they are not a claim of a universal or automatically maintained bitemporal database.

## 2. Required temporal dimensions

| Dimension | Meaning | Canonical carrier | It must not mean |
|---|---|---|---|
| World-valid time | When a fact, role, relationship or observation applies in the world, to the supported precision | observation/assertion effective interval; relationship, scope, party-role and identifier valid interval | retrieval or CharityGraph acceptance time |
| Source publication/reporting time | When the source says, publishes or reports something | source/evidence and `ObservationTime.observed_at` or reporting period | when CharityGraph learned or accepted it |
| Retrieval/acquisition time | When CharityGraph obtained a response or artefact | acquisition receipt and source record retrieval fields | source publication or world validity |
| Candidate extraction time | When a bounded process produced a candidate | candidate/task/result operational provenance where used | governed acceptance |
| Adjudication decision time | When an authorised human or governed decision was made | adjudication decision timestamp and decision record | source truth or valid time |
| Governed-current interval | When a governed record is current within CharityGraph's lineage | append-only record creation plus directed supersession/correction lineage | an assertion that the world changed at that instant |
| Release/publication time | When a projection or immutable release was produced | release manifest/publication metadata | any source or governed decision time |

All time fields retain their stated precision. A year, reporting period, date and instant are not expanded into one another. Unknown, unavailable, not attempted, acquisition failure and extraction failure remain explicit outcome/coverage states; source silence is not substantive absence.

## 3. Query contract

Builder's internal catalogue exposes:

- `knowledge_state_at(subject_id, knowledge_at=K)`: accepted/edited governed positives and explicit coverage known by K, with accepted relationships known by K. A later supersession is applied only after its own governed creation time.
- `current_belief_valid_at(subject_id, valid_at=V)`: current accepted governed positives with a supported valid interval covering V, current accepted relationships covering V, and explicit non-positive coverage separately.
- `knowledge_state_valid_at(subject_id, knowledge_at=K, valid_at=V)`: the explicit combined question, applying valid-time filtering only to governed records that were known by K.

These read models preserve the predicate, evidence/source identifiers, scope, observation/assertion time, lifecycle and lineage carried by their records. They do not decide truth, freshness, current availability, causal effect, authority, taxonomy assignment or publication eligibility.

## 4. Required behaviour

| Case | Required result |
|---|---|
| Late-arriving director relationship | A relationship valid from 1 July but governed on 21 July appears in current belief valid at 1 July, but not in knowledge state at 20 July. |
| Superseded fact | The predecessor remains historical. A knowledge-state query before the successor's governed creation returns the predecessor; later current-belief queries return the successor. |
| First-party claim | The query preserves `first_party_claim` and its source/epistemic basis. It does not promote the claim to independently verified fact. |
| Missingness | Non-positive coverage remains explicit and separate from positive observations/assertions. It cannot become a positive claim or substantive absence through query compilation. |
| Taxonomy assessment | Source-reported and CharityGraph-assessed classification remain distinct authorities. Assignment lifecycle and governed assessment lineage apply only to the latter. |

## 5. Projection, historical and compatibility rules

Projections select a question and declare their temporal basis. A card saying "current" requires an explicit valid-time and freshness policy appropriate to its section; this architecture supplies neither a universal freshness interval nor an automatic current-state assertion. Historical projections keep historical facts at their supported time. A release is a dated projection, never a rewrite of source, acquisition, candidate or decision history.

Directed supersession and correction preserve audit history. A newer record does not by itself prove a world change, invalidate a historical observation, or resolve disagreement. Release/publication decisions remain separate governance events.

Public v0.5 remains immutable. Existing S0 records and frozen packets retain their current semantics; this work adds no source store, packet system, migration, provider path or runtime execution.

## 6. Backlog-only implications for Semantica-derived research

The following are research/backlog items only. They depend on the stated gate and do not authorise a Semantica dependency, a new API/MCP/embedding path, source acquisition, external semantic execution, candidate generation, promotion or public-release change.

| Idea | Dependency/gate |
|---|---|
| Explicit discrepancy/conflict review | After stable bitemporal and correction semantics, with proposition-specific human governance. |
| Structural release/change intelligence | After source-publication, retrieval and release lineage are complete for the relevant source family. |
| Public "Why does CharityGraph say this?" lineage UX | After the public vNext contract and rights-safe publication lineage are approved. |
| PROV-O / JSON-LD / RDF export | After canonical semantics and public vNext mapping are stable; RDF is an export only, not canonical storage. |
| SHACL validation at the public boundary | After the public vNext contract defines its graph/export boundary. |
| Governance-decision lineage views | After decision and correction workflows have operational-scale evidence. |
| Rights-withdrawal and derivative blast-radius tooling | After rights/publication lineage is canonical for the affected release path. |
| Signed or attested public releases | After the public release process and key-management policy are approved. |
| High-level API/MCP Data surface | After public vNext contract stability and operational scale justify an interface commitment. |
| Semantic-neighbourhood / CharityGraph Space UX | After public vNext, rights-safe lineage and demonstrated user need; no generic vector-store abstraction is implied. |
| Entity-resolution operator workspace | After operational scale justifies a reviewed workflow and its authority/error policies are approved. |
