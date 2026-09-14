# Phase 6 reality-slice designs

**Status:** Working designs selected by the product owner for design only
**Date:** 12 September 2026
**Authority:** Subordinate to the canonical product, evidence, source, economics and North Star authorities indexed in [DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md)
**Scope:** Outcomes/evaluation; commitments/implementation; capacity/availability/access
**Execution status:** None of these reality slices has executed. This document authorizes no provider call, source acquisition, semantic run, candidate promotion, public release or implementation.

## 1. Decision boundary and intended use

The product owner selected the three capabilities for **reality-slice design**. Each
design below is independently reviewable and requires a separate execution decision.
Selection does not authorize a slice, provider use, a new source, a runtime change,
or production semantics. The intended result of an authorized slice is evidence to
decide whether the capability is useful, representable with CharityGraph's epistemic
discipline, semantically reliable enough for further investment, and economically
proportionate. It is not a schema-development milestone or a production release.

The broader Phase 5 Top-100 full-card objective remains active. A product-value slice
remains downstream of these experiments and a later product-owner decision. Phase 7,
scale, and the other deferred Phase 6 capabilities remain out of scope.

The three proposed cohorts contain six subjects each. The cohorts overlap on purpose
where one subject can exercise different product questions. They are purposive,
small, difficult-case cohorts, not a representative sample of Australian charities.
The design permits source-status outcomes and no-result cases; it does not require
every subject to yield a positive proposition.

## 2. Evidence used to propose cohorts

The read-only selection basis was:

- the frozen Phase 5 Top-100 baseline corpus run `phase5-top100-baseline-corpus-v1-clean`,
  whose retained `clean-source-coverage-matrix.json` SHA-256 is
  `63a8495266a941d5e5ce23ff495383116a33137b6221e7feea1015c05b0ac536`;
- the retained known-URL official-website campaign manifest, SHA-256
  `b471d31911329835990b3ce7055694eab5a931ad4d38cfc2b977e59a735f50ca`, and its
  execution report, SHA-256
  `d84a39660f0981c120671e7109c2a977c8f8bb9657896e97a5d55105d20233b1`;
- the current Top-100 rank/ABN identity list in
  `rankings/acnc-2024-ais-donation-ranking-top10000.json`;
- Builder's read-only `phase5-top100-factory-preflight-clean-v1` coverage and planning
  outputs; and
- the prior Direct Service V1.2 closeout and its published aggregate result.

Those manifests record metadata states; they do not establish that a byte-level source
artifact is currently re-readable, fresh, legally usable for the experiment, or
semantically adequate. The saved website acquisition records are not a present-day
availability check. Before any execution, an authorized preflight must verify each
selected receipt, artifact hash, source-record binding, retained representation,
permitted use and evidence locator using existing material only. It must fail closed
on missing bytes, hash mismatch, ambiguous lineage or rights concerns. No source may
be fetched or refreshed to repair a gap under these designs.

The baseline coverage has `acquired_available` AIS bundle and ACNC register status
for the selected subjects. Each selected subject has a retained successful official-
website acquisition record, either in the later campaign or the baseline corpus.
Annual-report status is `acquired_available` for every selected subject except St
Vincent's Hospital Sydney (rank 80), for which the retained baseline records
`attempted_unavailable`. The latter is an intentional missingness case, not an
instruction to search again. The website acquisition campaign's own metadata states
that it attempted 80 subjects, acquired 65 successfully, and made no provider calls;
its acquisition is historic, not part of this task.

Do not treat rank or donation amount as quality, impact, effectiveness, importance,
or recommendation. Rank is used only to identify frozen Top-100 members. Subject
names below are labels from that same retained ranking snapshot.

## 3. Shared design and execution protocol

### 3.1 Experiment unit and frozen inputs

The experimental unit is one **subject × capability** packet. Each capability has
six proposed subjects and one task per subject. A task packet may include only the
already-retained, hash-verified, rights-usable evidence selected for the stated
question. Before any separately approved execution, freeze and hash the cohort,
material artifacts, representations, locators, source roles, allowed scopes, task
instructions, response schema, model snapshot, review rubric, economic cap and
stopping rule. Changes create a new design/run identity; do not silently repin a
historical packet.

The ordinary-research comparator uses the **same frozen source package**. First,
independent semantic reviewers adjudicate raw candidates. Then prepare a private,
reviewed candidate view that visibly preserves unknowns and evidence links. Two
analysts, neither the task author, answer matched prewritten questions using the
source package and the reviewed candidate view in counter-balanced order. Record
time, answer completeness, material errors, uncertainty and citation traceability;
do not show one answer while producing the other. Include human correction/review
time in the cost of the candidate workflow. If two independent analysts are not
available, the semantic assessment may be reported but the product-use hypothesis
remains untested. This comparison is with manual use of the retained sources, not
unrestricted current web research or every conventional directory; broader comparison
belongs in a later product-value slice.

Count a paired task as materially improved only when the reviewed view preserves or
improves substantive correctness, scope, traceability and uncertainty handling, and
either answers a material part of the question that the manual baseline missed or
answers equivalently with lower analyst time. A faster but less accurate or less
calibrated answer is not a gain. Report each analyst's task result and time; do not
hide disagreement in a mean score.

Candidate output is private and visibly unreviewed until adjudication. The analyst
comparison uses only the post-review private view; it is not canonical knowledge and
is never projected into public Data. Human correction is included in the workflow
and cost, not an automatic promotion.

### 3.2 Reuse of existing contracts; no new persistent primitives

Builder already has append-only `CandidateObservation`, `Observation`, `Assertion`,
`CanonicalObservation`, `EvidenceLocator`, `SemanticEvidence` and scope primitives.
The Direct Service contract already provides the proposition types `service_offer`,
`eligibility`, `access_pathway`, `current_availability` and `capacity_measure`, an
explicit scope allow-list and 15 coverage states. Its section-discriminated V1.2
wire contract fixed a representation defect in a 14-response sample; it did not test
the substantive truth, freshness, utility or reliability of the access/capacity
claims. Builder preflight already marks these as a source-ready constrained semantic
family, while commitments/implementation and outcomes/evaluation remain high-risk
human-reviewed/deferred depth.

For outcomes and commitments, use experiment-local typed response labels inside the
existing candidate payload boundary, then map only reviewed propositions to the
existing generic observation/assertion model if a later, separately approved step
needs to test that mapping. For capacity, reuse the Direct Service V1.2 types and
converter as they are; make no schema edit for this experiment. None of the three
designs requires a new durable ontology primitive, public schema, Builder feature,
Viewer change, Factory redesign, API, MCP or embedding system.

An `Observation` records what a source or extractor reported; it is not true merely
because it exists. A model response is a candidate and inference. An `Assertion`
requires a governed decision. A human adjudication is recorded separately from both.
Never label model-produced text as source fact or human judgment.

### 3.3 Identity, scope and source-role rules

Use the frozen ACNC-bound subject identity as the organization anchor. Every packet
must declare an allow-list containing the organization scope and only program/service
scopes already represented by stable, evidence-supported identities or explicitly
created as private experiment candidates. An LLM may propose a program/service
candidate, but cannot create or resolve a durable scope identity. A human must bind
any candidate to a known scope before comparison; otherwise retain it as unresolved.

Allowed scope grain is organization, program or service. State/region, site, reporting
group, delivery partner and beneficiary cohort may be recorded only if the existing
source evidence and applicable contract support them and the task allow-list names
them. Do not promote a program/service claim to the whole organization, generalize a
parent/affiliate/network statement, or copy attributes across scopes. If scope cannot
be resolved, label that uncertainty rather than selecting the most plausible entity.

Every evidence unit carries the publisher, source owner, source family, source role,
publication/retrieval time, effective period where stated, subject/scope relation,
first-party versus regulator-reported status, and whether independent evaluation is
claimed or evidenced. Authority is proposition-specific:

- ACNC/ATO structured material supports only matters within that source's remit; a
  regulator portal or interface is not evidence that the charity operates a service.
- A charity's website, AIS or annual report is first-party evidence. It can support
  “the charity states/claims/reports X”; it does not independently verify X.
- A report published by a charity remains first-party publication even if it
  describes commissioned or external evaluation. Evaluator identity, independence,
  methods and limitations must be stated only when the retained evidence supports
  them.
- A separate, genuinely independent evaluation may support the evaluator's finding
  within its studied population/program/time, not automatic generalization to the
  whole charity.
- Conflicting sources are retained as competing evidence with role/time distinctions;
  the model must not pick a winner by source recency alone.

### 3.4 Evidence locators and missingness

Every positive candidate proposition must carry at least one supporting locator to
the exact retained artifact and source record. A locator must resolve within the
frozen artifact without network access. Use structured-field paths for source-native
fields; for HTML/text use stable URL plus captured artifact/hash and section or exact
span; for PDFs use artifact/hash, page and exact quotation or table coordinates. A
document-level locator is allowed only when narrower pinpointing is impracticable and
the human adjudicator can verify the proposition without ambiguity. Competing or
qualifying evidence receives its own locator and role. The reviewer packet may show
short lawful excerpts but must not add source bodies to Git or a public projection.
Exclude beneficiary-level case records, personal data and unnecessary sensitive
details from model packets and analyst views. If that material cannot be separated
from a needed source, stop and seek a separate privacy/rights decision.

Never encode missingness as a blank value or as a single `unknown`. Apply the existing
coverage vocabulary and distinguish:

| State | Meaning for these experiments |
|---|---|
| `source_silent` | An available, successfully processed source in the defined scope was reviewed and does not address this proposition. |
| `source_unavailable` | A source the packet intended to use is recorded as unavailable or access-failed; no inference about its contents follows. |
| `not_acquired` / `not_attempted` | No retained source material or attempt exists for this source/proposition. Acquisition is prohibited in this task. |
| `not_processed` | Retained material exists but was not processed for this proposition. |
| `processing_failed` | Processing was attempted but failed; it is not substantive absence. |
| `not_reviewed` | A candidate or source remains unadjudicated. |
| `stale` | Evidence supports a dated/historical statement but does not meet the approved freshness rule for a present-tense claim. |
| `unknown` | Available evidence was insufficient or irreducibly ambiguous for the requested proposition. |
| `asserted_none` | The source explicitly states that the item/condition is absent; retain who asserted it and the scope/time. |
| `observed_absent` | A specified, sufficiently complete observation/search supports absence only within its stated frame. Never infer it from silence. |
| `not_found` | A predefined set of locations was searched and the proposition was not found; this says nothing beyond that search frame. |
| `not_applicable` / `withheld` | Use only for actual inapplicability or governed withholding, with basis; neither is a synonym for unknown. |

If a retained state is not supported by readable bytes, locators and provenance, it
cannot be silently upgraded to `source_silent`, `asserted_none` or `observed_absent`.

### 3.5 Mechanical gate, semantic gate and adjudication

Mechanical results are reported separately from semantic results. Before semantic
scoring, require:

1. valid response shape and allowed proposition types;
2. exact subject and scope IDs from the packet allow-list;
3. evidence locator, artifact hash and source-record resolution against frozen bytes;
4. legal time, unit and coverage-state encodings;
5. source-role fields present and consistent with the supplied evidence metadata;
6. deterministic reproducibility of normalization/validation and no accidental
   duplicate or retry; and
7. request/attempt accounting reconciled at the provider-crossing boundary if calls
   are separately authorized.

A mechanically invalid item is a mechanical failure, not a semantic rejection and
not a provider retry. A passing schema or locator is not evidence of truth.

An independent human adjudicator, other than the model-task author, reviews every
proposed proposition and each material omission question against the source evidence.
Use proposition dispositions: `accepted`, `accepted_with_correction`,
`rejected_unsupported`, `rejected_wrong_subject`, `rejected_scope_error`,
`rejected_source_role_error`, `rejected_overstatement`,
`rejected_wrong_epistemic_class`, `rejected_temporal_error`,
`rejected_missingness_error`, `rejected_material_omission`, and `unresolved`. For
reliability assessment, a second reviewer independently codes at least two of the six
subjects per slice before discussion; also double-review all contested, high-impact,
causal, obligation/compliance or current-capacity items. Report raw agreement and
disagreements descriptively; six subjects do not support a sector accuracy claim.
Resolve differences explicitly without erasing either initial judgment.

Record failure counts at proposition and subject level for: unsupported proposition;
wrong subject; wrong program/service scope; source-role/authority confusion; source
fact versus first-party claim confusion; activity/output/outcome/contribution/causation
class error; commitment versus implementation/compliance error; description versus
availability/capacity error; temporal/freshness error; unit/denominator/population
error; overstatement; material omission; wrong missingness state; unresolved
contradiction; locator/lineage failure; mechanical schema failure; processing failure;
economic exclusion; and analyst-task non-utility. Retain counts and concrete error
examples in the private review record; do not merge them into a single score.

### 3.6 Reliability, economics and provider controls

For an authorized run, the base plan is one constrained semantic task per subject
(six primary task attempts) and two deliberate same-model technical replicates on
preselected difficult subjects (eight intended requests total per capability).
Replicates keep evidence, ordering, scope, prompt/schema, model snapshot and parameters
materially identical. They measure repeatability separately from validity. No
automatic retries, fallback, second-model bake-off or replacement request is included.
A local pre-send validation failure is not a provider crossing. Any ambiguous
transmission fails closed and is not resent. Economic exclusions are terminal
non-executions, not semantic failures.

For each slice calculate conservative exposure from the frozen input/output token
upper bounds and the current approved provider price snapshot, then convert using a
dated AUD FX snapshot. Calibrate upper bounds against observed usage from comparable
retained tasks and retain explicit headroom based on that calibration; if no defensible
upper bound exists, do not authorize calls. Set both a per-request and aggregate hard
AUD cap before execution. Reconcile raw provider usage separately from the cost ledger;
include provider cost, representation/preparation work, human annotation/adjudication
minutes, analyst task time, and any orchestration overhead in total cost of intelligence.
Record the human review cost even if provider spend is negligible. Before execution,
the product owner must also set a maximum review-time budget per subject and an
all-in cost ceiling per materially improved analyst task. Compare those ceilings with
observed provider spend, preparation/review minutes and paired analyst time saved.
If no defensible ceiling or comparable price/FX snapshot is available, the economics
result is inconclusive and the slice is not authorized to run. No current prices or
spend authority are granted by this design.

Use the lowest-cost model plausibly adequate for typed extraction, with Luna as the
default hypothesis from the Phase 6 programme. Fix the actual model snapshot before
the run. A stronger model is justified only if pre-run task analysis shows genuine
multi-source synthesis or abstraction not expressible as typed extraction, or if
adjudicated lower-cost output shows a repeatable, material failure pattern that a
specific stronger reasoning capability might address. Any such test must be limited
to the affected task, preserve the same source packet and rubric, and receive a new
explicit product-owner decision and cost cap. Difficulty or prestige alone is not
grounds to select Terra.

### 3.7 Shared stopping rule

Compare technical replicates by agreement on material proposition class, subject and
scope, source role, epistemic status, evidence support, missingness and resulting
analyst answer; wording differences alone are immaterial. An answer-changing
disagreement in either deliberately repeated case blocks a “reliable enough” decision
until explained and addressed. Two repeated cases are a bounded instability check,
not a reliability-rate estimate.

Stop each slice at six subjects and the planned two replicates, when its hard cap is
reached, or earlier on a stop condition below. Do not enlarge the cohort to smooth
results. Do not run an additional call to replace an exclusion, failure or awkward
case. Stop immediately for a source-rights issue, artifact/hash mismatch, unexpected
identity/scope ambiguity, prohibited sensitive information, unresolved crossing
state, repeated critical epistemic error, or material deviation from the frozen task.
Record “inconclusive” if the evidence cannot decide the hypothesis within the frozen
packet. Any larger sample or new source universe requires a new decision.

## 4. Slice A — Outcomes and evaluation

### Hypothesis and analyst task

**Hypothesis:** For organizations with retained reports, a private evidence-linked
representation can help an analyst distinguish an organization's stated outcomes
from what it says was measured, the population/program and period measured, the
evaluator/source role, and the study's limitations more quickly and with no causal
overstatement compared with manually consulting the same retained source package.

The slice answers:

- What outcome does the organization say it seeks, and what outcome does it say was
  observed or measured?
- Is the evidence an input, activity, output, observed outcome, contribution claim,
  or causal finding reported by a source?
- Which program, population, denominator and period does the reported measure cover?
- Who conducted/published the evaluation, and what methods, comparator and limitations
  are actually stated?
- What is unknown, mixed, negative, inconclusive, absent from the reviewed source, or
  not processed?

### Cohort (six subjects)

All six have retained ACNC AIS, annual-report and official-website source-family states
recorded as available in the frozen corpus/campaign metadata. Treat every family as
historical until the common hash/rights/locator preflight passes.

| Top-100 rank; ABN | Subject | Selection challenge and reason | Candidate retained families |
|---|---|---|---|
| 1; `28004778081` | World Vision Australia | Large, multi-program subject tests boundaries between organization-level purpose and program/population-specific results. | ACNC register; ACNC AIS bundle; annual report; official website; ATO/ABR/DGR for identity/context only |
| 4; `28000030179` | The Smith Family | Tests whether educational-program measures are presented as outputs, measured outcomes or causal effects, with correct target population and period. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 20; `12004251423` | The Walter and Eliza Hall Institute of Medical Research | Deliberate difficult case for separating research activity/publication or intermediate findings from downstream beneficiary/health outcomes. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 31; `65069482829` | The Trustee for Channel 7 Telethon Trust | Tests subject attribution and whether a fund/distribution relationship is mistaken for the outcomes of funded delivery organizations. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 47; `78053639115` | Bush Heritage Australia | Adds a different outcome horizon and tests whether activity, area/output measures and ecological outcomes remain distinct. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 77; `32565549842` | St George Community Housing Limited | Tests service/program/site granularity and whether organization-level statements are overgeneralized to housing outcomes. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |

Selection roles are hypotheses from the frozen cohort identity and broad task design,
not claims that these organizations have a particular evaluation or result. The
execution packet must inventory exact source files and locator-capable representations
without searching the web. If a listed source family is unavailable or unusable,
record that state and decide whether the remaining sources still answer the task; do
not substitute a new source or silently replace the subject.

### Experiment-only proposition types and scopes

Use narrow task-local labels: `outcome_or_aim_claimed`, `activity_or_output_reported`,
`outcome_measure_reported`, `contribution_claim_reported`,
`causal_finding_reported`, `evaluation_design`, `study_population_and_period`,
`limitation_or_uncertainty`, and explicit coverage state. `*_reported` means that a
source reports it; it is not an independent CharityGraph finding. Do not infer a
causal effect. A source's causal conclusion may be classified as a reported causal
finding only when the text says so and the study design/evidence is located; the
reviewer separately evaluates whether the output overstates what the cited source
concludes. Do not create an effect-size estimate or normalize incomparable outcomes.

Legal scopes are the organization and a cited/allow-listed program or study population.
Study geography/population and study period are attributes of the evidence, not
implicit organization-wide scopes. Preserve source-stated units and denominators.

### Acceptance and slice-specific failure rules

Mechanical acceptance uses the shared gate. In addition, each numeric result must
retain its source unit, denominator where given, population and time period; an
evaluation must retain its stated design/evaluator/limitations or label them absent
from the reviewed evidence. No result may change epistemic class during mapping.

Advance as **promising for further design** only if at least four of six paired
analyst tasks produce a materially more useful or faster answer with traceable
support; all six receive final human dispositions; no unsupported causal claim,
wrong population/scope or source-role error survives in the candidate view; and review
time/cost is proportionate to the observed gain. Report raw counts, correction burden,
replicate stability and limitations. One surviving critical causal/scope error, fewer
than four useful tasks, or a repeated activity/output/outcome confusion triggers
revision or deferral, not scale.

Slice-specific failure labels include: activity called outcome; output called outcome;
observed change called contribution; contribution called causation; source-reported
causality promoted to independent conclusion; wrong denominator/population/period;
study design/evaluator independence overstated; material limitation or contrary,
negative, mixed or inconclusive result omitted; or research/commissioner misattributed.

Defer if the frozen source package does not contain enough locator-capable evaluation
material, if claims can only be made useful by unsupported causal inference, if the
review burden is disproportionate, or if the paired analyst task shows no material
gain. Do not defer merely because some organizations have no outcome evidence; correct
representation of unknown/absence is itself evaluated, but it may not establish the
capability's usefulness.

## 5. Slice B — Commitments and implementation

### Hypothesis and analyst task

**Hypothesis:** For six varied organizations, explicitly separating a policy or
commitment from first-party claimed action, independently evidenced practice and
formal compliance enables an analyst to identify what was promised, what evidence of
implementation exists and the scope/time it applies to, without converting policy
text or missing evidence into proof of implementation/non-implementation.

The slice answers:

- What policy, principle, target, pledge or obligation is actually stated, by whom,
  for what scope and period?
- Is there evidence of a planned action, self-reported implementation, observed
  practice, independent verification or formal compliance finding?
- Does implementation evidence cover the whole organization, a named program/site,
  or only a reporting period?
- Is evidence of implementation absent from the reviewed sources, or is there
  affirmative evidence of non-implementation?

### Cohort (six subjects)

All six have retained AIS, annual-report and successful official-website acquisition
metadata. These varied subjects exercise organizational form, advocacy language,
reporting entity and delivery-scope boundaries; these are case-selection hypotheses,
not substantive findings about the organizations.

| Top-100 rank; ABN | Subject | Selection challenge and reason | Candidate retained families |
|---|---|---|---|
| 13; `50169561394` | Australian Red Cross Society | Tests whether statements by a national body, network or separately scoped activity are improperly generalized across entities. | ACNC register; ACNC AIS bundle; annual report; official website; ATO/ABR/DGR for identity/context only |
| 14; `65159324697` | The Sunrise Project Australia Limited | Tests explicit advocacy/strategy commitments against claims and evidence of completed action without treating campaigns as proof of outcomes. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 31; `65069482829` | The Trustee for Channel 7 Telethon Trust | Tests trust/reporting-entity scope and attribution of implementation evidence to the trustee versus another named delivery body. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 37; `61426486715` | Cancer Council Victoria | Tests state/legal-entity and program scope against possible broader-sector statements; no national propagation without evidence. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |
| 69; `61002643852` | Greenpeace Australia Pacific Limited | Tests public position/commitment wording versus evidence of activities or organizational practice; the initial baseline website status was attempted-unavailable and a later retained campaign acquisition succeeded. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition) |
| 77; `32565549842` | St George Community Housing Limited | Tests operational policy versus claimed or observed practice at program/site scope and across time. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition; baseline website lineage was unresolved) |

### Experiment-only proposition types and scopes

Use task-local labels: `policy_or_position_stated`, `commitment_stated`,
`formal_obligation_reported`, `implementation_plan_reported`,
`implementation_claimed_by_subject`, `practice_observed_or_independently_reported`,
`compliance_finding_reported`, `evidence_against_or_contradicting`, and explicit
coverage state. A self-reported progress statement remains `implementation_claimed_by_subject`.
Do not infer a binding legal obligation from aspirational wording or decide legal
compliance. Formal obligations/findings may be extracted as attributed source reports
only; any legal interpretation remains outside this slice.

Allowed scope is organization, named program/service/site and explicit reporting
period, if named and resolvable from frozen evidence. Each commitment and each
implementation proposition is separate: they must not be joined into one status
unless source evidence explicitly links them. A policy's organization scope does not
prove uniform implementation at all locations.

### Acceptance and slice-specific failure rules

Mechanical acceptance follows the shared gate. Each proposition must independently
identify status/epistemic class, author/source role, time, scope and locator. A
commitment and an implementation item cannot share one proposition record merely to
make them appear linked.

Advance as **promising for further design** only if at least four of six paired
analyst tasks improve materially or are answered materially faster with traceable
support; all six receive human dispositions; no policy-to-implementation upgrade,
first-party-to-independent upgrade, organization-wide scope leak or claim that silence
proves non-implementation survives; and the measured review burden is proportionate.
Report raw counts and reviewer disagreements. Any surviving commitment/implementation
collapse, or fewer than four useful tasks, triggers revision or deferral.

Slice-specific failures include: aspiration called binding commitment; policy called
implementation; planned activity called completed practice; first-party claim called
independent observation; scoped activity generalized organization-wide; one entity's
actions transferred to an affiliate or partner; source silence called
non-implementation; conflicting or superseded evidence hidden; or compliance/liability
concluded from a source excerpt.

Defer if resolving material cases requires legal, regulator or relationship research
outside the retained corpus; if reviewers cannot agree on the basic commitment versus
implementation distinction; if rights/sensitivity requires additional governance; or
if structured results do not improve the paired analyst task. Missing implementation
evidence does not count as evidence that a commitment was broken.

## 6. Slice C — Capacity, availability and access

### Hypothesis and analyst task

**Hypothesis:** For six service-oriented subjects, showing evidence-linked service
offers, eligibility/access pathways, availability as-of a source date, capacity
measures and explicit unknown/stale states enables an analyst to answer where and how
a service may be accessed without conflating a description with present availability
or capacity, and is more useful than manually searching the same retained sources.

The slice answers:

- What service is described, at what organization/program/service scope, and for whom?
- What eligibility, referral, location or access conditions does the retained source
  actually state?
- What does the source say about availability, and as of what date?
- Is a capacity quantity/unit or state explicitly supported, or is capacity unknown?
- Which answer cannot be made because the source is stale, unavailable, unprocessed,
  silent or ambiguous?

### Cohort (six subjects)

All six have retained AIS and successful retained official-website acquisition
metadata. Five have annual-report metadata marked available. St Vincent's Hospital
Sydney has an explicit attempted-unavailable annual-report state and is included to
test that the task does not mistake a missing report for service absence. Its retained
website may support only statements and dates actually present in that artifact.

| Top-100 rank; ABN | Subject | Selection challenge and reason | Candidate retained families |
|---|---|---|---|
| 30; `80931522157` | Starlight Children's Foundation Australia | Tests named-service/program conditions and the line between service description and live access. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition) |
| 39; `80009663478` | Royal Flying Doctor Service of Australia (Queensland Section) | Tests geography, service/scope boundaries and whether eligibility/access claims belong to a particular program or region. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition) |
| 63; `23082732027` | St Catherine's Aged Care Services | Adds a different service setting and tests units/temporal scope of capacity statements; no person-level data is in scope. | ACNC register; ACNC AIS bundle; annual report; official website (available in baseline corpus) |
| 72; `57057493017` | The Leukaemia Foundation of Australia Limited | Tests whether information/support offers are mistaken for clinical service availability or quantified capacity. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition) |
| 77; `32565549842` | St George Community Housing Limited | Tests organization/program/site scope, eligibility/referral and any waitlist or capacity wording. | ACNC register; ACNC AIS bundle; annual report; official website (later successful retained acquisition) |
| 80; `77054038872` | St Vincent's Hospital Sydney Limited | Tests service access from retained website evidence when annual-report acquisition is explicitly unavailable. | ACNC register; ACNC AIS bundle; official website (available in baseline corpus); annual report `attempted_unavailable` |

### Proposition types, scope and temporal rules

Reuse the existing Direct Service V1.2 types without expanding the contract:
`service_offer`, `eligibility`, `access_pathway`, `current_availability` and
`capacity_measure`. Include task-local values that preserve the existing contract's
coverage states and source observation time. `capacity_measure` requires a unit; do
not invent one or return a quantity when none is sourced.

Legal scopes are organization, program, service and site only where the allow-list
and evidence support them. Availability is always `as_of` the capture/observation
time or the source-stated valid period. A static captured page does not prove
availability today. Capacity stages must remain distinct: designed, approved,
funded, staffed, operational, available, occupied and delivered are not substitutes.
Do not estimate capacity from the number of service locations, staff, beneficiaries
served, historical throughput, donations or a general service description.

### Acceptance and slice-specific failure rules

Mechanical acceptance follows the shared gate and additionally requires units for
all capacity measurements, a time basis for availability/capacity, and scope IDs from
the allow-list. Confirm that the existing V1.2 converter preserves evidence
locators, coverage state and observation time for every included proposition. Its
prior representation result is evidence only for mechanical section/type shape.

Advance as **promising for further design** only if at least four of six paired
analyst tasks are materially more useful or faster with evidence traceability; all
six receive human dispositions; no unsupported present-tense availability, invented
capacity, wrong site/program scope or source-silence-as-absence error survives; and
the selected captured sources are fresh enough for the claim as of their recorded
dates. If availability is already stale at the design's pre-approved freshness rule,
report that result; do not fetch an update. Report raw counts and update/review burden.

Slice-specific failures include: offer called available; available called staffed or
operational; designed/funded capacity called available capacity; waitlist called
unavailable service (or vice versa) without evidence; no capacity statement called
zero capacity; eligibility/referral omitted or invented; organization coverage
generalized to all sites; dated information called current now; capacity unit,
denominator or period omitted; or an unavailable/unprocessed source treated as silent.

Defer if utility requires fresh operational data that is not retained, if most
subjects cannot be answered without new acquisition, if source dates are too old for
the intended “current” question, if reviewers cannot reliably distinguish offer,
availability and capacity, or if refresh and human-review costs outweigh the measured
analyst benefit. Source recency limits should be set and approved before execution,
not inferred after inspecting results.

## 7. Separate execution approvals required

Before executing **each** slice, Greg/product owner must review and explicitly approve
that slice's final packet independently, including:

1. the six exact subject identities, scoped question cards and any permitted
   substitutions (default is no substitutions);
2. the final list of retained source artifact hashes, rights/retention basis,
   source-role metadata, representation readiness and evidence locators; any failed
   check means remove the source/proposition or stop, never acquire a replacement;
3. the final task-local output schema, coverage/missingness behavior and prohibited
   inference;
4. the independent reviewers/analysts, blind adjudication procedure and review-time
   recording;
5. whether the proposed two technical replicates and product-use comparison are
   authorized;
6. actual provider/model snapshot, prompt/task hash, no-retry crossing policy,
   per-request and aggregate AUD hard caps, price/FX snapshots and calibrated exposure;
7. the review-time and all-in cost ceilings used to decide economic proportionality;
8. the mechanical gate, semantic decision rules, stop conditions and private result
   location; and
9. confirmation that outputs remain private, candidate-only and are not promoted or
   published.

The three approvals are independent. Rejecting, deferring or stopping one capability
does not authorize or block either of the others. An approval to execute one slice
does not authorize another model, subject, source, repeat, new acquisition, schema
change or production implementation.

## 8. Deferred decisions and limits

The product owner still needs to decide, separately per slice, whether the proposed
six-subject cohort and review burden are acceptable; who will perform independent
adjudication and paired analyst tasks; whether a second reviewer is available; what
current dated FX/provider price snapshot and AUD hard cap to use; what freshness
window is appropriate for capacity; and whether a slice should proceed if a retained
source fails byte-level revalidation. No present token budget, dollar ceiling or
freshness interval is set here.

The designs do not decide broad source sufficiency, sector-wide accuracy, universal
outcomes comparability, legal compliance, current operating capacity beyond the
captured evidence, or public product value. They do not change canonical product
semantics or public v0.5. Any result may support further design, revision, deferral
or abandonment; none guarantees implementation.
