# CharityGraph Semantic Reliability and Reproducibility

**Status:** Canonical cross-cutting governance policy

**Version:** 1.0-draft

**Date:** 28 August 2026

## Purpose

CharityGraph uses model-assisted semantic measurement at scale. Quality therefore includes both evidence-grounded validity and empirical reliability.

## Core quality model

Validity, repeatability and input robustness are independent dimensions:

`validity × repeatability × input robustness`

They SHALL NOT be collapsed into one quality score. Validity asks whether a judgment is evidence-supported and represents the underlying charity appropriately. Repeatability asks whether materially identical measurements reproduce similar graph structure. Input robustness asks how results respond to reasonable changes in presentation or evidence selection. Repeatability does not establish validity: a consistently reproduced error remains an error.

## Durable semantic results

A valid ModelResult is a provenance-bearing artefact. Routine production and release replay SHALL reuse a valid persisted result when material task identity is unchanged. A fresh semantic call is justified only by an explicit reason, such as changed evidence, task/prompt/policy, model/version/parameters, invalidation or correction, or deliberately authorised evaluation replication. A normal rebuild SHALL NOT regenerate unchanged semantic material.

## Technical replication

Semantic evaluation cohorts SHOULD contain deliberately selected technical replicates. No permanent replicate percentage is set; each evaluation packet specifies its own fraction and design. A replicate keeps evidence, order, source-role context, task schema, prompt, model snapshot, parameters and policy materially identical while executing an independent generation. Replicates require explicit authorisation and must remain distinguishable from accidental duplicate execution. Exactly-once production protections remain in force. An evaluation replicate is not an accidental retry.

## Reliability measures

Evaluation SHALL separately measure semantic subject-set overlap, granularity/split/merge stability, disposition/type agreement, operational-status agreement, evidence-support agreement and proposal-count dispersion. Exact proposal keys, labels, rationale wording and JSON bytes are insufficient measures of semantic equivalence. Ambiguous matching may require governed human review.

## Source-role context

Source role is semantically material. Evidence about a charity is not necessarily activity of the charity. Regulator identity/context, regulator-reported charity information, first-party activity claims and independent evaluation occupy different roles. A regulator interface, portal, search tool or registration marker is not a charity program/service merely because it appears in an evidence bundle. Source, publisher and authority context belong in task semantics; changing materially relevant role metadata changes task material identity. This is not implemented as a list of forbidden phrases.

## Longitudinal protection

A changed model output is not by itself evidence that the charity changed. Stochastic appearance or disappearance of a candidate must not mechanically create, tombstone or close a governed graph subject. Real-world change requires evidence and governance appropriate to the claim.

## Release meaning

A stable CharityGraph release does not imply a deterministic LLM API call. It means evidence and semantic machinery are versioned, accepted results are persisted, releases are immutable, rebuilds reuse governed results, and stochastic repeatability is measured separately.

## Public claims

CharityGraph SHALL NOT claim deterministic or near-deterministic semantic extraction, a numeric reliability rate or “same answer every time” without an appropriately designed evaluation. Any empirical reliability claim must identify the task family, model snapshot, evidence protocol, cohort, replicate protocol, matching/adjudication method, sample size and limitations.

## Prospective repeatability x validity experiment — 2026-08-28

The first deliberately authorised prospective experiment used a frozen
20-charity cohort and exactly two independent technical replicates per charity.
It made 40 logical semantic calls and 40 HTTP requests. One measurement was
terminal-invalid. The primary repeatability analysis therefore covered 19
charities, excluding the single-measurement case without interpreting it as a
failed replication.

The aggregate validity cross-tab was:

| Validity class | 2/2 | 1/2 |
|---|---:|---:|
| Clearly supported | 61 | 22 |
| Plausible / grain ambiguous | 40 | 8 |
| Likely artefact | 7 | 10 |
| Evidence inadequate | 7 | 3 |
| **Total** | **115** | **43** |

There were 158 eligible semantic families: 115 recurring in both valid
measurements (2/2) and 43 appearing in one valid measurement (1/2). The
within-group proportions were clearly supported 53.0% versus 51.2%, clearly
supported or plausible 87.8% versus 69.8%, and likely artefact 6.1% versus
23.3%. Descriptive risk differences and ratios (2/2 relative to 1/2) were:

- clearly supported: **+1.9 percentage points**, **RR 1.04**;
- clearly supported or plausible: **+18.1 percentage points**, **RR 1.26**;
- likely artefact: **-17.2 percentage points**, **RR 0.26**.

Leave-one-charity-out clearly-supported risk differences ranged from **-5.85
percentage points to +12.53 percentage points**. Seven likely artefacts were
stable across both measurements, while 22 clearly supported singleton
families were observed.

Conditional on an approximately matched subject, disposition agreement was
111/115 (96.5%), operational-status agreement was 93/115 (80.9%), mean
subject-family Jaccard overlap was 0.516, and weighted structural overlap was
0.379. The structural overlap statistic is retained as a separate descriptive
measure from the reviewed-family mapping.

These results establish the following methodological conclusions:

1. Repeatability and validity are independent dimensions.
2. 2/2 recurrence did not materially predict clearly supported validity.
3. 2/2 recurrence was associated with substantially lower artefact prevalence
   and higher clearly-supported-or-plausible prevalence.
4. Stable artefacts exist.
5. Clearly supported singleton subjects exist.
6. Replicate intersection MUST NOT be used as a validity or publication rule.
7. Repeatability MAY be used as an uncertainty or review-prioritisation signal.
8. Subject enumeration and grain remain less repeatable than attributes
   conditional on approximately matching the subject.
9. Operational status is less repeatable than disposition and remains an
   independent reliability concern.

The experiment also tested the review instrument. Excerpt-only blinded review
produced widespread `EVIDENCE_INADEQUATE` judgements; providing the complete
frozen evidence reduced evidence-inadequate cases substantially. Document-level
evidence binding is therefore insufficient for efficient proposition-level
review. This motivates, but does not approve, a future proposition-level
supporting-evidence locator.

This prospective result supplements the retrospective/Fresh-18 observations
recorded in [the 2026-08-28 baseline note](SEMANTIC_RELIABILITY_BASELINE_2026-08-28.md).
That earlier note remains historical experimental context; neither experiment
sets a product performance threshold. Charity-level validity classifications
and unblinded family mappings remain private.
