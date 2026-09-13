# Governed product-value validation slice — working design (14 September 2026)

**Status:** Working design; not execution authority

**Owner:** Shared CharityGraph product/data

**Scope:** Prepare one integrated, bounded product-value validation across Inspect, Compare and Verify. It is downstream of Phase 6 and does not execute it.

**Supersession:** This design supersedes the prior planning line that product-value work must wait for V6 adjudication; the final V6 adjudication and Phase 6 closeout are recorded in [the closeout history](docs/history/phase6-closeout-2026-09-14.md).

## Product proposition

For a selected charity, a competent analyst should be able to inspect a broad, useful set of North Star questions from a governed projection without rereading every primary source, while tracing each material answer to its governed proposition, evidence locator, source, epistemic status and coverage state. A bounded comparison should answer only questions for which the subjects' fields, scopes and periods are genuinely comparable. It must not rank charities or treat search relevance as merit.

This is an integrated product experiment, not another isolated semantic capability benchmark. It is a preparation packet only. No source is acquired, no provider is called, no candidate is promoted and no live analyst task is run by this design.

## Cohort feasibility from frozen material

The proposed cohort is **eight** subjects represented in the retained Top-100/Phase 6 frozen material and the 13 September post-policy rights assessment. The rights assessment covers nine subjects and 27 exact artifacts. Its 18 affirmative decisions apply to nine single-record ACNC structured representations and nine bounded annual/financial-report excerpts; they do not authorize websites, arbitrary source substitutions, public redistribution or local retention under that policy. The product-value slice must bind any later request to those exact representation identities/hashes and revalidate the applicable policy, provider settings and execution authority. It is not an approval to reuse the privately retained copies.

North Star coverage below is an approximate source-input map, not a count of governed answers. ACNC structured records plus short report excerpts can support varying evidence for identity/regulatory status (1), purpose (2), activity (3), governance (14), commitments/implementation (15), outcomes/evaluation (18) and evidence/freshness/coverage (20). Depth varies by the exact excerpt. Financial/resource information (7), beneficiary detail (4), service access/capacity (11), relationships (12), workforce (13), conduct (16), context (17) and other specialist fields are not presumed covered. Only adjudicated, governed propositions count in the eventual Inspect/Compare/Verify tasks.

| Candidate | Existing frozen source families | Exact provider-transmission rights readiness | Approximate North Star source-input coverage | Phase 6 capability relevance | Gaps and inclusion/exclusion reason |
|---|---|---|---|---|---|
| World Vision Australia | ACNC structured entity record; annual-report excerpt | Both exact representations were authorized for provider transmission under Fair Dealing V1; not public redistribution or policy-approved local retention. | 1/2/3/14/18/20; 18 coverage remains provisional from the narrow excerpt. | Outcomes V6; human PASS on reach versus observed outcome. | Include for scale and a clear reach-without-observed-outcome case. No independent evaluation source is in the approved pair; do not infer an outcome from reach or generic monitoring/evaluation text. |
| Bush Heritage Australia | ACNC structured entity record; annual/impact-report excerpt | Both exact representations authorized on the same narrow basis. | 1/2/3/14/15/18/20; exact coverage depends on excerpt. | Outcomes V6; human PASS on attributed causal claim versus observed result. | Include for environment and a difficult causal-attribution boundary. The exact management/health claim is attributed, not measured or causal evidence. No claim of independent ecological measurement. |
| Australian Red Cross Society | ACNC structured entity record; annual-report excerpt | Both exact representations authorized on the same narrow basis. Its full/near-complete website representation is blocked and excluded. | 1/2/3/7/14/15/18/20, uneven and excerpt-dependent. | Commitments/implementation V5 human review; the accepted evidence separates self-report from independent verification. | Include for large humanitarian operations and a challenging broad report. Only the bounded excerpt and structured record are candidates; no broad website or full-card coverage is assumed. |
| Greenpeace Australia Pacific | ACNC structured entity record; annual/financial-report excerpt | Both exact representations authorized on the same narrow basis. Its full/near-complete website representation is blocked and excluded. | 1/2/3/7/14/15/18/20, with the report's periods kept explicit. | Commitments V5; repeat is `STABLE_AT_ANALYST_ANSWER_LEVEL`. | Include for an advocacy organisation, temporal commitment wording, and repeat stability. Do not equate an aim or activity under way with completed implementation. |
| The Sunrise Project Australia | ACNC structured entity record; annual/financial-report excerpt | Both exact representations authorized on the same narrow basis. Its full/near-complete website representation is blocked and excluded. | 1/2/3/7/14/15/18/20, excerpt-dependent. | Commitments V5 human review. | Include for climate philanthropy/advocacy and stated-versus-implemented distinctions. Previously rejected activity-to-commitment overstatement remains an adversarial case. |
| St George Community Housing Limited | ACNC structured entity record; financial-report excerpt | Both exact representations authorized on the same narrow basis; exact frozen pair was rights-assessed, though not transmitted in Phase 6. | 1/2/3/7/14/20; section 11/service detail is not established by this source pair. | No selected Phase 6 capability result; Capacity remains deferred. | Include for community housing and a smaller-scale contrast. It exercises sparse evidence; do not treat accounting data as current service capacity or availability. |
| Royal Flying Doctor Service of Australia (Queensland Section) | ACNC structured entity record; financial-report excerpt | Both exact representations authorized on the same narrow basis; exact frozen pair was rights-assessed, though not transmitted in Phase 6. | 1/2/3/7/14/20; section 11/current availability remains unknown from this pair. | No selected Phase 6 capability result; Capacity remains deferred. | Include for geographically distributed health/emergency service context and a scope challenge. Keep Queensland Section distinct from national RFDS; no service-capacity inference. |
| The Leukaemia Foundation of Australia Limited | ACNC structured entity record; annual/financial-report excerpt | Both exact representations authorized on the same narrow basis; exact frozen pair was rights-assessed, though not transmitted in Phase 6. | 1/2/3/7/14/18/20; actual evaluation detail remains unconfirmed. | No selected Phase 6 capability result; Outcomes relevance is only an available report family, not an adjudicated outcome result. | Include for health and patient-support context at a different scale. Do not convert beneficiaries, services or reach to measured health outcomes. |

**Excluded candidate:** The Smith Family is in the nine-subject rights assessment, and its exact ACNC/report representations were assessed separately from its explicitly prohibited website representation. It is excluded from this proposed cohort because its Outcomes V4 transport history includes two ambiguous attempts and V6 adjudication was not completed for it. No retry or source substitution is proposed. It can return only after an independent product-owner decision resolves whether and how that history affects a separately identified future task.

The cohort is not selected for Phase 6 performance: it deliberately combines two reviewed Outcomes subjects, three reviewed Commitments subjects, three subjects with sparse unconfirmed specialist coverage, different domains and scales, and a rights-sensitive exclusion. The exact source family/representation list is closed; no website capture or new source is silently substituted.

## Shared reviewed-evidence coverage

The offline Builder representation in `phase6_semantic_contracts.py` is a bounded carry-forward for these two selected capabilities. Each coverage item is bound to a named `ReviewedEvidenceUniverse` with a subject, legal scope and unique finite set of source-record IDs and processing states. It uses separate states for `evidence_present`, `not_found_in_reviewed_sources`, `source_silent`, `not_processed`, `source_unavailable`, `not_acquired`, `processing_failed`, unresolved `unknown` and justified `not_applicable`. Not-found requires at least one exact reviewed source ID in the same universe; positive evidence requires a locator bound to a reviewed source. Unprocessed, unavailable, not acquired, failed and unresolved inputs cannot be relabelled not found. No state makes a claim about evidence elsewhere.

Outcomes coverage is explicit for observed outcome measure, evaluation/assessment, evaluator identity, method, comparator/counterfactual, and limitations. Commitments coverage is explicit for implementation evidence, independent implementation verification, implementation outcome, and affirmative evidence of non-implementation. These coverage items remain orthogonal to proposition type, evidence carrier/source role, epistemic class and human/governed disposition. First-party measured outcome reporting remains first-party; first-party implementation does not become independent verification. Phase 6 proposition classes remain intact, including V6's observation-basis requirement.

## Product task design

### Inspect

For each of the eight charities, provide the same bounded analyst prompt: identify legal subject and scope; summarize stated purpose and evidenced activities; state which commitment/implementation and outcome/evaluation answers are actually supported; show whether observed measures, evaluator, method, comparator and limitations are present or missing in the defined evidence universe; and state the source periods and material gaps. The task is successful only when the projection carries answers, uncertainty and locators together. It is not a general endorsement or charity-quality assessment.

### Compare

Prepare pairwise, non-ranking questions only for fields with compatible subject grain, proposition meaning, period and source basis. Candidate comparison fields are legal/operating scope, stated purpose/activity, reporting-period commitment versus implementation, whether an observed outcome measure exists in reviewed sources, and the presence/absence state of evaluation method/comparator/limitations. If the sources do not align, report `not_comparable` with the reason. No score, league table, search-relevance proxy, or charitable-merit conclusion is produced.

### Verify

For each material answer, the reviewer must traverse: answer → governed proposition/knowledge → explicit organisation/program/service scope → evidence locator → source record and source role → epistemic status and human/governed disposition → reviewed-evidence universe and coverage state. Any answer without a complete path is unverified and must be reported as such. Positive propositions and explicit unknown/missing states receive the same traceability requirement.

## Human evaluation and later decision rule

Use candidate-blind paired tasks: one analyst answers using the governed projection; a second source-only task uses only the exact frozen evidence universe. Counterbalance task order where practical and record analyst experience. Capture proposition-level answer correctness, material completeness, traceability success, uncertainty/missingness visibility, misleading semantic upgrades, comparison comparability and analyst time/cognitive effort. Review every material answer and every reported not-found state; retain the source-only answer key and adjudication separately from candidate output.

No statistical threshold is asserted and the Phase 6 four-of-six gate is not transplanted. After the bounded eight-subject review, the product owner should decide whether the integrated projection gives materially correct and traceable answers with visible missingness and lower analyst effort, while producing no unresolved critical semantic upgrade. Advance only if the owner accepts those observed trade-offs and rights/governance constraints; otherwise correct a bounded defect and seek fresh approval, or defer. A critical untraceable or overstated answer pauses the decision; cohort averaging cannot offset it.

## Execution blockers requiring product-owner decisions

1. Approve or reject the cohort, questions and later human-evaluation protocol; authorize any future execution separately.
2. Resolve rights and handling for source representations: the V1 post-policy assessment authorizes exact bounded provider transmission but explicitly does not authorize local retention or public redistribution. Existing private files are not themselves evidence of a retention right. A compliant source-only human review and governed evidence store need an approved handling basis.
3. Decide the approved path from Phase 6 candidates to governed knowledge for this experiment. No Phase 6 candidate is governed merely by human slice adjudication, and no promotion is included here.
4. Before any future provider request, revalidate exact representation hashes and artifact-rights decisions, current provider-processing policy/attestation, source scope, budget, request identity and separate execution approval. All eight subjects are rights-ready only for their exact assessed pairs and subject to those checks.
5. Define who performs the independent source-only and proposition-level review and how disagreements are recorded before seeing any new candidate output.

Until these decisions are made, the slice remains design-only. Phase 5 Top-100 scaling remains not authorized; Capacity is not selected; no Factory redesign, Viewer work, API/MCP or embeddings are in scope.
