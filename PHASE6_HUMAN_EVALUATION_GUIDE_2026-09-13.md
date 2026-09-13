# Phase 6 Human Evaluation Guide

**Status:** Working evaluation protocol for review; no evaluation administered
**Date:** 13 September 2026
**Authority:** Subordinate to the Phase 6 semantic correction plan and the existing Phase 6 reality-slice design
**Scope:** Blind source-only versus adjudicated-candidate comparison for the three selected capabilities

## 1. Purpose

Measure whether a corrected, evidence-linked CharityGraph view helps an analyst answer the same questions more completely or faster than using the exact retained source representations alone, without reducing factual correctness, scope discipline, evidence traceability, or uncertainty handling.

The source-only task export and candidate packet are separate artifacts. Condition A reviewers receive no Luna output or candidate-derived evidence selection. Condition B reviewers receive only the corrected candidate packet after proposition-level human adjudication; the raw candidates and unresolved failures remain separately available to adjudicators, not ordinary task analysts.

The current local Condition A export contains 18 tasks: six original subjects for each capability. It is generated in a private temporary directory from the exact 24 frozen request bodies and includes zero candidate outputs, propositions, and answers. Regenerate it from the retained request preparation if that directory has been cleaned. Do not place source representations in Git or combine them with candidate material.

## 2. Task populations and question sets

For the paired usefulness test, use the original six-subject set per capability so the predeclared threshold remains six paired tasks. The smaller three-subject confirmation cohorts in `PHASE6_SEMANTIC_CORRECTION_AND_ADVANCEMENT_PLAN_2026-09-13.md` assess contract reliability; they do not replace the six-task usefulness denominator.

Use the identical questions in both conditions:

**Outcomes / evaluation:** What outcome is sought and what was measured? Is the evidence input, activity, output, observed outcome, contribution, or a reported causal finding? Which population, denominator, program and period apply? Who conducted/published any evaluation, with what methods, comparator and limitations? What is unknown, mixed, negative, inconclusive, absent from reviewed sources, or unprocessed?

**Commitments / implementation:** What policy, principle, target, pledge or obligation is stated, by whom, and for what scope and period? Is there a plan, first-party implementation report, independent observation, external verification or formal finding? What entity/program/site and period does the evidence cover? Is implementation evidence absent, or is there affirmative evidence of non-implementation?

**Capacity / availability / access:** What service is described, at what scope and for whom? What eligibility, referral, location or entry conditions are stated? What availability is reported and as of what date? Is capacity explicitly bounded or unknown? What cannot be answered because evidence is stale, unavailable, unprocessed, silent or ambiguous?

## 3. Administration

Assign anonymous task and analyst IDs. Have two analysts work independently where available. Counterbalance condition order across subjects; do not show one condition's answer while completing the other. The same frozen evidence package must support both conditions. If two independent analysts are unavailable, report the limitation and do not claim that the comparative usefulness hypothesis was tested.

Record for every condition: start/end time and active minutes; answer completeness; source citations and locator success; scope and period; uncertainty/missingness; analyst confidence before adjudication; and material errors or omissions. For Condition B also record candidate correction time and which structured candidates were accepted, rejected, narrowed, or left unresolved. Candidate correction and semantic adjudication time count toward the candidate-assisted workflow cost.

Independent reviewers adjudicate proposition correctness after both analyst answers are captured. Do not treat either analyst answer as ground truth. Keep disagreements and per-subject results; do not hide them in an average. Candidate outputs remain private and are never promoted by this evaluation.

## 4. Paired usefulness scoring

A task is a **materially useful candidate-assisted result** only if all of these hold:

1. substantive correctness, source role, scope, traceability, date/as-of, and uncertainty are preserved or improved;
2. there is no critical unsupported claim or epistemic upgrade;
3. the candidate-assisted view either answers a material part of the question missed by the source-only answer, or answers equivalently with less analyst time; and
4. the time comparison includes candidate correction and review effort, not just reading time.

A faster but less correct, less scoped, less traceable, or less calibrated answer does not count. An unresolved critical semantic error makes that task not useful even if the analyst catches it, because the product view did not safely carry the answer.

The usefulness threshold is **at least four of six paired tasks per capability**. This is a small-sample gate for further product-value consideration, not a population estimate or proof of generality. Report the numerator/denominator and all six task records. All six tasks must also have final human dispositions, and all capability-specific semantic gates must pass. Four useful tasks cannot offset a critical surviving semantic or scope error.

## 5. Review form

Use one row per subject and condition, plus a paired disposition row:

| Field | Entry |
|---|---|
| Capability, subject ABN, anonymous task ID | |
| Anonymous analyst ID, condition, condition order | |
| Start, end, active minutes | |
| Answer completeness and material omissions | |
| Proposition-level correctness after adjudication | |
| Evidence locator resolved; source role preserved | |
| Scope, population, denominator and time/as-of correct | |
| Missingness and uncertainty handled correctly | |
| Critical error category, if any | |
| Analyst confidence before adjudication | |
| Condition B correction and reviewer minutes | |
| Paired result: materially useful / equivalent-faster / no gain / harmful | |
| Reviewer rationale and unresolved disagreement | |

Reviewer identity and notes remain empty until a real review is administered. No result is assumed by the current export or tests.

## 6. Decision reporting

For each capability report: six subject-level paired results; useful-task count; source-only and candidate-assisted correctness/omission comparison; median and range of analyst and correction time; unresolved disagreements; critical failures; source/rights exclusions; and total workflow cost. Apply the four-of-six threshold and semantic gates independently to Commitments, Outcomes, and Capacity. A passing capability may be proposed for an 8-12 organization product-value slice; it is not automatically included and does not authorize publication, promotion, or broad rollout.
