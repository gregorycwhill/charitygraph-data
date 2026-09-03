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

Dense evidence showed Compact can preserve evaluation design, comparisons,
findings, participant evidence and qualifications. Section relevance must be
established before classification; outputs, outcomes and causal claims remain
distinct. Further prompt polishing is deferred.

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
