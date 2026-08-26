# Semantic heuristic approvals

**Status:** Canonical approval register  
**Scope:** CharityGraph Builder and Data

## Policy

No deterministic code may infer open-ended semantic meaning from unrestricted language through regexes, keyword or phrase lists, lexical scoring, capitalization/title-case, URL words or slugs, repetition/frequency, fuzzy lexical similarity or equivalent techniques unless a specific exception is approved by Greg and recorded here before implementation.

The review question is: **Does this diff teach Python English?** If yes and no registered approval exists, stop and redesign the evidence, prompt, task schema, model, routing, benchmark or governance.

Mechanical processing remains permitted for stable syntax and formats, identifiers and checksums, dates and numbers, URLs, file formats, whitespace and markup structure, exact source-native structured fields, schema validation, arithmetic and exact joins.

## Approved exceptions

**None.** No CG-SH-* exception is currently approved.

## Required record for a future exception

Each entry must include:

- approval ID and exact scope;
- technique and why it is preferable to a model task;
- benchmark/evidence supporting the boundary;
- cost, latency and total-cost comparison;
- failure boundary and stop condition;
- owner, approval date and expiry/review date.

A total-cost comparison alone does not authorise an exception.
