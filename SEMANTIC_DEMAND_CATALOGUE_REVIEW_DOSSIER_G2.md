# Gate 2 semantic review dossier — CG-G2-SEMANTIC-DEMAND-CATALOGUE-397-LUNA

## Recommendation

Submit the candidate for supervisor semantic review with **20 demands**, not 74. The canonical North Star defines 20 knowledge domains, while the legacy CG395 scaffold contains 74 coverage rows with opaque or generic family labels. Keeping 74 would require padding, arbitrary splitting or synonym proliferation, which is expressly disallowed.

## Legacy reconciliation

`LEGACY_74_DEMAND_INVENTORY_CANDIDATE.json` inventories all 74 legacy IDs (`SDC-0001`–`SDC-0053` and `SDC-0061`–`SDC-0081`) and preserves each legacy family and CG395 instance IDs. Every item has disposition `REPLACED_BY`: no legacy identity is silently dropped. Successor mapping is by semantic family to the candidate demand that owns that proposition:

| Legacy family / hint | Successor |
|---|---|
| identifier, identity binding, organisation proposition, effective date, hard identity reconciliation | SDC-C01 |
| cause, assertion (purpose/values context) | SDC-C02 or SDC-C15; supervisor to confirm where the generic assertion cannot be disambiguated |
| access, eligibility, availability, current availability, delivery | SDC-C07 |
| population, geography, delivery geography | SDC-C05 |
| activity, appeal, channel, designation, commitment, award, appeal proceeds, giving-offer fundability | SDC-C04, SDC-C08 or SDC-C14 according to proposition object and lifecycle |
| capacity, capability, aggregate, cohort/denominator | SDC-C07 or SDC-C11 according to whether it is service capacity or organisational capability |
| role, participation, charity-insider comparison | SDC-C06, SDC-C09 or SDC-C10 according to role and subject scope |
| accounting basis, financial change, historical expenditure, financial measure, restricted income | SDC-C13 |
| funding dependency | SDC-C14 |
| evaluation, longitudinal evidence comparison, design | SDC-C18 |
| conduct, allegation, root cause | SDC-C16; causal/root-cause language remains unresolved unless explicitly evidenced |
| history, event, change | SDC-C17 |
| classification, assessed classification, rendered label | SDC-C19 |
| abstention, basis, coverage, correction, extracted fact, supported observation, positive answerability, explicit aggregation compatibility, projection | SDC-C20; these are evidence/epistemic governance propositions, not domain facts |

This family crosswalk is applied to every row in the inventory; where a legacy label is generic, the successor is chosen by the proposition’s actual subject/scope/time/object during migration review, not by lexical similarity. Legacy IDs are not retained as candidate canonical IDs.

## North Star coverage

All 20 active sections are covered one-to-one by `SDC-C01` through `SDC-C20`. Cross-cutting semantics are explicit in every demand: subject, scope, time, applicability, proposition template, proposition-specific source-role expectation, and missingness/state handling. No domain gap is currently recorded; supervisor review is still required for generic legacy labels and the final cardinality decision.

## Authority and provenance

The candidate is grounded in current Data repository documents: `NORTH_STAR_TARGET_CARD_V0_3.md` §§1–20; `PRODUCT.md` §§7–12 and §16; `INTEGRATED_PRODUCT_AND_DATA_MODEL.md` §§6–7, §§8–13 and §16; `SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md`; and `DOMAIN_PROFILE_INDEX.md`. Each demand row cites its direct North Star/product basis. No open-web research, source acquisition, or new source class was used.

## Missingness and source policy

The shared states are `SUPPORTS`, `PARTIAL`, `CONFLICTS`, `NOT_FOUND_IN_REVIEWED_UNIVERSE`, `NOT_APPLICABLE`, and `UNRESOLVED_PROCESSING_FAILURE`. The candidate explicitly preserves the distinction between reviewed-universe non-findings, explicit unavailability, source silence, unknown and processing failure. Source authority remains proposition-specific; no generic “official source” rule silently authorises every proposition.

## Authorship audit

Semantic definitions, domain ownership, proposition templates, provenance interpretation and migration crosswalk were authored by Luna from canonical prose. Mechanical work was limited to extracting the 74-row CG395 inventory, serialising the candidate table, counting IDs and checking deterministic formatting. No script inferred meaning, authored definitions, or decided a split/merge/retirement.

## Local artefacts and stop point

Candidate artefacts: `SEMANTIC_DEMAND_CATALOGUE_CANDIDATE_G2.md`, `SEMANTIC_DEMAND_CATALOGUE_CANDIDATE_G2.json`, `LEGACY_74_DEMAND_INVENTORY_CANDIDATE.json`, and this dossier. No remote publication, push, merge, canonical-main mutation, Gate-2 progress award, source sufficiency benchmark, or evidence-testing tranche was started.

**Decision required:** approve the semantically justified change from a 74-row experiment scaffold to a 20-demand executable catalogue, and confirm the resolution policy for generic legacy families that can map to more than one candidate demand. After that decision and supervisor semantic acceptance, the next action is a separately authorised catalogue finalisation/review tranche; Gate 2 evidence testing must remain paused until then.
