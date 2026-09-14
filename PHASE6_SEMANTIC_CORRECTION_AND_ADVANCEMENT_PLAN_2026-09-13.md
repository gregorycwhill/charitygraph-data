# Phase 6 semantic correction and advancement plan

**Status:** Working proposal for product-owner review; not product or execution authority
**Date:** 13 September 2026
**Scope:** Source-only evaluation export, three experiment-local semantic contracts, adversarial tests, and bounded confirmation design
**Execution:** No confirmation request is authorized by this document. No provider call or source acquisition has occurred under this tranche.

## 1. Purpose and current disposition

This package turns the supplied product-owner plan into a reviewable implementation proposal. It does not reopen broad Phase 6 exploration, change public v0.5, register production tasks, or authorize a confirmation run.

The working dispositions supplied for the three capabilities are:

| Capability | Working disposition | Gate before product-value work |
|---|---|---|
| Commitments / implementation | `ADVANCE_WITH_REPRESENTATION_FIX` | Review the corrected contract package, then pass a three-subject confirmation slice. |
| Outcomes / evaluation | `REPEAT_AFTER_SEMANTIC_FIX` | Pass the outcome ladder, targeted semantic confirmation, and the paired usefulness test. |
| Capacity / availability / access | `REPEAT_AFTER_SEMANTIC_FIX` | Pass the separated access/eligibility/scale/capacity/availability contract and its confirmation tests. |

These are planning dispositions, not accepted proposition decisions. The historical 24-output packet and its triage still record no proposition-level human adjudication. The examples named below become adversarial test cases supplied by the product-owner plan; this package does not rewrite the historical review ledger or claim new reviewer decisions.

## 2. Boundaries and authority

The canonical Phase 6 execution and triage artefacts remain unchanged. The new Builder models are isolated under `charitygraph.phase6_semantic_contracts`; they are not registered as production tasks, wired into persistence, or projected into public Data. The existing Direct Service V1.2 contract, converter, Viewer, Factory, and public v0.5 remain unchanged.

The Data documents in this package are working proposals subordinate to the authorities in `DOCUMENT_AUTHORITY.md`. The contract labels and tests require product-owner review as a coherent package before a provider run. Python checks controlled fields, enum membership, IDs, source roles, temporal fields, and evidence presence; it does not inspect prose to decide whether a claim is an outcome, eligibility rule, access pathway, implementation, or capacity.

## 3. Tranche A: blinded source-only evidence export

An evaluation-only Condition A export was generated from the exact request bodies retained for the completed 24-attempt run. It contains one task for each of the 18 unique subject/capability pairs in the original six-subject cohorts; repeat requests were checked for identical source representations, scopes, and missingness before deduplication. The export contains the exact transmitted source representation strings, source identity and role, source/artifact/locator IDs, source and retrieval dates, effective period where recorded, the request's permitted organization scope ID, and explicit unavailable-source records.

The export excludes provider response envelopes, model outputs, proposition candidates, answer fields, generated explanations, and candidate-derived evidence selection. It has no program/service scope IDs because none were supplied in these requests; named sub-organization scopes must remain unresolved unless the source-only packet itself establishes a permitted identity. The export utility reads only frozen preparation requests, verifies each canonical request-body hash, and fails if repeat inputs differ. It has no provider or acquisition path.

Private export path on the current machine: `%TEMP%\cg-phase6-source-only-eval-20260913`. Manifest SHA-256: `62fa35105741f92fc5f297183745b798062b36eb41653a231a159d5acc3cfd81`. The source contents are deliberately excluded from Git under Builder/Data source-material rules. Keep this local export separate from candidate packets and share it only with assigned source-only reviewers under applicable rights and privacy controls. The committed manifest metadata and generator are reproducible; a future review session must regenerate the local export if the temp directory has been cleaned.

## 4. Cross-cutting semantic contract

Every positive candidate is an evidence-bound, scoped, typed report. Its proposition type and epistemic class are structured fields; free-form qualification text is not allowed to reverse their meaning. Each evidence reference carries a frozen locator, source role, source date and/or retrieval time, and effective period where known. Source role is validated against epistemic class:

- first-party websites, annual reports, financial reports, and policies can support attributed first-party claims or measures, not independent observation;
- regulator, court, independent-evaluation, or external-authoritative material can support only a proposition within its stated remit and source role;
- a first-party report remains first-party even if it is formal, audited for financial purposes, or summarizes commissioned research;
- model inference and human adjudication are not source epistemic classes. Candidate inference remains unaccepted; a human decision is recorded separately.

Every proposition must bind to an allowed scope ID. Organization, program, service, site, and study-population scope are never inferred from labels. Missingness remains distinct (`source_silent`, `source_unavailable`, `not_processed`, `processing_failed`, `stale`, `unknown`, and related governed states); absence is not inferred from missing evidence.

The validator enforces only mechanically expressible relationships. It does not classify unrestricted prose. A structurally valid candidate can still be semantically wrong and must pass proposition-level human adjudication. Any confirmed contradiction between source evidence and structured type is a critical semantic failure, even when schema validation passes.

## 5. Tranche C: Outcomes / evaluation V2

The review contract separates:

1. `activity_reported`;
2. `output_reported`;
3. `reach_or_participation_reported`;
4. `outcome_observed_reported`;
5. `contribution_claim_reported`;
6. `causal_attribution_claim_reported`; and
7. `causal_evidence_supported`.

An observed outcome requires a measured beneficiary state or target-system condition, population, indicator, result, unit, period, evidence, scope, and explicit first-party-measure or independent-finding epistemic class. Reach, participation, delivered services, hectares managed, grants, money raised, expenditure, and surplus have separate activity/output/reach/resource shapes and cannot satisfy the outcome-measure schema by field shape alone. A source's own causal language remains a reported causal attribution claim. The stronger causal-evidence type requires an independent source, explicit study design and comparator, population, period, result, and limitations. Its presence is not an automated endorsement of study quality.

Regression cases: World Vision reach/participation; Smith Family reading-age improvement; WEHI expenditure; Channel 7 surplus; Bush Heritage protected hectares; SGCH satisfaction; and SGCH housing scale/surplus. A positive measured outcome must retain its population, denominator when available, unit, period, scope, and evidence. Activity/output/outcome/contribution/causation are never collapsed by conversion.

## 6. Tranche D: Commitments / implementation V2

The review contract separates:

1. `commitment_stated`;
2. `policy_or_standard_adopted`;
3. `implementation_activity_self_reported`;
4. `implementation_activity_independently_observed`;
5. `implementation_evidence_regulatory_or_external`; and
6. `implementation_outcome_reported`.

Self-reported implementation requires first-party source role and `first_party_claim` epistemic class. Independently observed activity requires an independent or external source role and `independent_finding_reported`. A commitment or policy does not establish implementation; reported implementation does not establish completeness, effectiveness, compliance, or achievement. There is no generic `practice_observed` type and no compliance decision type in this experiment contract.

Regression subjects: Sunrise Project, Australian Red Cross, Greenpeace, Channel 7 Telethon, SGCH, and Cancer Council Victoria. The three-subject confirmation set is Sunrise Project (first-party commitment and action), Australian Red Cross (external/regulatory evidence boundary), and Greenpeace (ambiguous commitment/action scope). These are selection hypotheses against frozen inputs, not claims about what those subjects' sources contain.

## 7. Tranche E: Capacity / availability / access V2

The review contract separates:

1. `service_exists`;
2. `intended_beneficiary_group`;
3. `formal_eligibility_rule`;
4. `access_information`;
5. `access_pathway`;
6. `historical_activity_volume`;
7. `resource_or_workforce_measure`;
8. `service_scale_measure`;
9. `capacity_limit_or_capacity_measure`;
10. `availability_reported_as_of_date`;
11. `current_availability`; and
12. `availability_unknown`.

A beneficiary description is not a formal rule. Formal eligibility requires an explicit rule issuer and rule basis. Address, contact, hours, an information page, or an online-operation flag are access information; an access pathway requires at least one controlled entry action such as apply, request referral, call intake, book, complete an assessment, attend drop-in, or submit an online request. Historical throughput, expenditure, staff, volunteers, homes, beds, and locations are represented as activity, resource, or scale measures, not as a capacity limit. A capacity measure requires a declared capacity basis, bounded unit, value and as-of date.

`availability_reported_as_of_date` preserves a source-bounded historical/current-at-capture statement. `current_availability` requires an as-of date, a named freshness-policy ID, and dated source evidence. Validation fails closed until an approved freshness window is supplied to the temporal validator; this package does not invent an age threshold. Without adequate dated evidence, use `availability_unknown` and retain the actual missingness state.

Regression cases: RFDS 24/7 claim; St Catherine client composition; Leukaemia Foundation access information/pathway; SGCH application pathway versus housing stock; St Vincent beneficiary categories and locations; and Starlight service descriptions. Confirmation subjects: SGCH (entry pathway versus housing scale), RFDS Queensland (dated 24/7 claim), and Leukaemia Foundation (information versus clinical access/availability). Unknown is an acceptable result.

## 8. Tranche F: adversarial tests

The Builder review-only tests assert typed separation or rejection for:

- reach/participation represented as an outcome;
- organization expenditure/surplus represented as a beneficiary outcome;
- expenditure represented as a capacity limit;
- housing stock represented as capacity;
- beneficiary population represented as a formal eligibility rule;
- a physical address represented as an access pathway;
- undated availability represented as current availability;
- a first-party statement represented as independent observation; and
- a first-party causal claim represented as independently supported causality.

Positive cases cover a distinct reported measured outcome, first-party implementation activity, explicit access actions, valid unknown availability, independent evidence shape, and exact allowed-scope binding. These tests validate the structured boundary, not natural-language truth. They do not claim a semantic classifier can recognize a false label from arbitrary prose.

## 9. Tranche G: bounded confirmation design

Use only existing frozen evidence; no cohort expansion, new sources, API/MCP, embeddings, Factory work, Viewer changes, or public release. Each capability gets a separate run identity and a maximum of three unique subjects. Subject selection is listed in Sections 5-7. A single predeclared repeat of one difficult subject may be included within that same three-subject cohort only if repeatability is necessary to test the corrected boundary; it does not add a subject.

Use the same pinned low-cost model family and settings as the prior run to isolate the contract correction; do not run a model bake-off. Pin exact model snapshot, schema, prompt, source packet hashes, scope allow-list, output budget, cost ceiling and stop rule before any future authorization. Existing per-request and programme caps from the approved experiment design remain controlling. No confirmation run begins until this package and the storage/rights handling of source-only materials receive product-owner approval.

Per capability, stop on the first critical type/epistemic/scope/source-role error that survives deterministic validation; two answer-changing replicate disagreements; any source/hash/rights mismatch; or the approved cost cap. Do not retry provider failures unless an amended authorization explicitly permits it. A clean mechanical result is necessary but not sufficient.

## 10. Advancement gates

A corrected capability may be considered for the 8-12 subject product-value slice only if:

- all targeted cases receive final human dispositions;
- strict schema, evidence-locator, allowed-scope, source-role, temporal, and type invariants pass;
- no critical semantic-category or epistemic upgrade error survives review;
- no answer-changing repeat instability attributable to the corrected representation remains unexplained; and
- the paired Human Evaluation Guide shows material usefulness without loss of correctness, traceability, scope, or uncertainty handling.

Commitments may advance independently. Outcomes and Capacity remain deferred unless their distinct confirmation gates pass. A capability may be deferred for persistent semantic instability or low incremental usefulness; absence of positive claims is not a failure if unknown/missingness is represented faithfully.

## 11. Open decisions before confirmation execution

The following decisions remain for the product owner after reviewing this coherent package:

1. approve, revise, or reject the experiment-local proposition names and required fields;
2. approve a freshness window/policy for any `current_availability` result, or prohibit that type in the first confirmation run;
3. approve the private storage location and reviewer access/rights conditions for the source-only export;
4. approve or revise the three-subject cohorts, exact model snapshot, cost caps, and stop rules; and
5. separately authorize each capability's provider run after the package is approved.

Until those decisions are recorded, these contracts remain a working proposal, the historical 24 candidate outputs remain unadjudicated, and no confirmation request is sent.
