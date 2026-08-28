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
