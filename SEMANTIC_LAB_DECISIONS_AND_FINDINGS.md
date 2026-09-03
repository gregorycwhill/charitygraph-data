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

### Section 15 — ACTIVE SEMANTIC LAB, NOT YET TESTED

Four substantive existing PDF packets are frozen. The original conservative
projection of USD 0.064213 exceeded the USD 0.05 cap, so execution correctly
made zero provider calls. The approved ceiling for this unchanged experiment
is now USD 0.08. No Section 15 findings are claimed yet.

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

## Section 15 V1D — reviewed experimental findings

The V1D bounded structural-packet experiment supports packetising persisted
representations before semantic work rather than sending whole documents. It
used 23 packets over four persisted annual reports: 8 Compact responses
completed, 15 reached the 2,000-token output ceiling, 125 recoverable atoms,
9 lens calls and USD 0.089037 actual cost.

Packet `s15v1d-009` exposed a harness defect: it reported `status=incomplete`
after reaching the output ceiling but remained parseable and was incorrectly
sent to the lens. Only Compact responses with `status=completed` should enter
downstream semantic tasks.

Completion depends on semantic/output density as well as input length;
approximately 6,000 evidence tokens with a 2,000-token Compact ceiling is not
reliable. Generic free-form evidence locators are insufficiently governed;
atom-to-exact-evidence binding requires an allow-listed mechanical reference
contract. Exact effective dates must not be manufactured from coarser
year/month/reporting-period language.

V1D was substantially over-inclusive: purpose, programs, governance, finance,
registrations, services and organisational activity were repeatedly drawn into
Section 15. First-party annual reports can support target-stated positions,
commitments, targets and claimed implementation, but do not by themselves
establish independently observed practice. Obligations and verified compliance
have distinct evidence roles, and verified compliance remains outside Section
15. Strong specimens included First Nations partnership commitments,
modern-slavery positions, environmental targets, code-adherence commitments,
and implementation explicitly connected to environmental or
responsible-investment commitments.

Generic Compact sometimes retained implementation/progress while omitting a
nearby normative anchor; V1E tests whether smaller packets improve this. The
Australian Conservation Foundation remains a corpus-coverage gap because its
governed representation is only an annual-report index page.
