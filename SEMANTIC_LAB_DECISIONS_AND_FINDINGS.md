# Semantic Lab Decisions and Findings

Living reviewed-learning record for Phase 3 semantic experiments. Raw model
outputs and private evidence remain in the runtime, not this repository.

## A. Standing architecture principles

- **DON'T TEACH PYTHON ENGLISH.** Python enforces schemas, references,
  identifiers, lineage, evidence binding, budgets and deterministic validation;
  open-ended semantic judgement belongs at the model/review boundary.
- **BUILDER DOESN'T DO DISCOVERY.** Central sourcing decides what evidence
  CharityGraph has; sections decide what that evidence means. Builder may
  acquire from approved central sources, but sections and semantic tasks do not
  search for new sources when evidence is sparse.

Canonical flow: centrally governed source universe → acquisition → immutable
raw artefacts → persisted reusable representations → high-recall knowledge →
specialist lenses → governed projections.

## B. Current experimental operating method

**LAB FIRST; FACTORY LATER** is the current Phase-3 development method:
small frozen experiments using existing governed evidence and one-shot bounded
calls, with private raw outputs and Chat cross-sample review before changes.

`Lab → Chat cross-sample review → durable decision/learning capture → next Lab`

Production scheduler, restart, ledger and persistence hardening are deferred
until semantic workloads are understood.

## C. Reviewed cross-cutting findings

Generic Compact followed by specialist lenses is viable. Evidence scope,
attribution, temporal detail and causal strength must remain explicit. Model
validity is not automatic promotion. Absence from supplied evidence is not a
knowledge candidate, and experimental labels are not canonical taxonomy.

## D. Section status / findings

### Section 18 — ARCHITECTURE-VALIDATED / PARKED — NOT SEMANTICALLY COMPLETE

Dense evidence showed Compact can preserve study design, cohort comparisons,
quantitative findings, qualitative participant evidence and causal
qualifications without Section-18-specific raw extraction. Specialist relevance
gating is necessary because most generic knowledge is not Section 18. Keep
input/resource, activity, output, observed outcome measure, outcome/change and
impact/contribution/causal claim distinct; quantitative facts are not
automatically indicators, aspiration is not achieved impact, and report
existence is not a finding. Study design, comparator/baseline, limitations,
participant evidence and recommendations are valuable. Preserve attribution,
causal strength and candidate → Compact atom → exact evidence binding.
Response-schema enum enforcement is an appropriate mechanical control.
Model-invented labels such as `outcome_measure` are taxonomy-design evidence,
not canonical taxonomy. The final precision test reduced false positives but
lost some design/comparator/limitation/recommendation recall; further prompt
polishing is deferred rather than oscillating precision and recall.

### Section 15 — ARCHITECTURE-VALIDATED / SEMANTIC-BOUNDARY-TESTED / PARKED — NOT PRODUCTION-COMPLETE

The broad V1E Semantic Lab campaign is complete and parked. Across the
historical and corrected runs, generic Compact knowledge followed by
independent specialist lenses proved viable, while the original permissive
lenses showed semantic promiscuity and the corrected lenses over-pruned some
legitimate recall. Neither prompt set is canonical production policy and no
second paid correction pass is planned. The working boundary remains:

| bounded experiment | key result |
|---|---|
| historical broad lenses | 43 packets; 344 tasks/calls; 333 complete; 11 incomplete; 919 candidates; USD 0.229121 |
| corrected reconstruction | 43 packets; 344 tasks/calls; 334 complete; 10 incomplete; 438 candidates; USD 0.160001 |
| atom fan-out | historical 458 used / 377 multi-lens (0.8231); corrected 303 used / 118 multi-lens (0.3894) |

These figures are experimental, bounded and non-performance-guaranteeing.
The corrected run is a reconstruction over retained V1E material, not an
exact replay of historical request payloads.

`statement → commitment → claimed implementation → observed practice → verified compliance → outcome`

Ordinary program delivery, governance, finance, fundraising, network
membership or organisational activity does not by itself establish a position
or commitment. Implementation requires an evidenced antecedent position,
commitment, obligation or source-explicit implementation framing; self-reported
implementation does not establish independently verified compliance.

Future lens contracts must define, per domain: the positive semantic object;
nearby concepts that do not qualify; transformations that would be epistemic
uplift; expected legitimate cross-domain reuse; and the meaning of a
zero-candidate result. Fan-out is diagnostic, not a validity or publication
rule.

### Durable operating decisions

**Semantic Lab versus Factory.** The Lab optimises information gain: cheap,
bounded experiments may tolerate imperfect replay or reconstruction, absorb
local failures while independent tasks continue, and document uncertainty.
Budgets protect against runaway or duplicate spend, not penny-level
optimisation. Stop for likely-useless results or genuine safety, billing,
corpus or provenance failures. Factory/scaling work retains stricter
requirements for exact task identity, restart/replay safety, duplicate
prevention, durable accounting and cost optimisation; those are not premature
Lab blockers. PR #48 remains parked.

**Source universe and corroboration.** The canonical sequence is:

`SOURCE UNIVERSE FIRST → ACQUIRE ONCE → FREEZE CORPUS → SEMANTICS`

Product/source governance defines the finite approved source universe and
applicability rules. Builder acquires approved sources; semantic tasks
interpret only the frozen corpus. A semantic result may expose a coverage gap
but cannot trigger external research or add a source. New source families
(including ASIC, GrantConnect, courts, specialist regulators or tender
systems) require a separate sourcing decision and acquisition pass. Bounded
specialist applicability may be predeclared by governance. **BUILDER DOESN'T
DO DISCOVERY / BUILDER DOESN'T DO RESEARCH.** Human or Chat product research
may separately propose an additional source family.

A proposition may enter CharityGraph when supported by an approved source and
represented according to that source's evidentiary role. Independent
corroboration is not universal unless a governed claim family requires it.
Annual reports may support charity-reported grants, activities or claimed
implementation; Wikipedia may support qualified context/notability; ACNC/ATO
filings may support source-reported regulatory/financial facts. First-party
language does not establish independently observed practice or verified
compliance, and semantic results do not automatically trigger corroboration
search. Overlap may add corroboration, conflict or authority.

## E. Parked production-runtime backlog

PR #48 / V12 exposed restart-safe deterministic packet/task identity,
completed-task detection, duplicate-transmission prevention, typed-ID ledger
integration, deterministic entry identity, crash-safe reservation
reconciliation/release, durable aggregate-cost enforcement, persisted-only
representations and range-aware evidence reconstruction. PR #48 remains
parked/open/unmerged; these are later scaling prerequisites, not blockers for
current Semantic Lab learning.

## F. Open questions

When should reviewed lens findings graduate into canonical contracts, and what
evidence/review thresholds should govern promotion, taxonomy mapping and
source-family changes?

## G. Promotion / supersession rule

This record is superseded only by an explicit reviewed decision or by a
canonical architecture/policy update. Experimental findings remain bounded
until that occurs.
