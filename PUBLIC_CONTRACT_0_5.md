# CharityGraph Public Data Contract 0.5

**Status:** Implemented compatibility contract  
**Release:** `v0.5.0-2026-08-15`  
**Date implemented:** 2026-08-15  
**Not:** a future Builder architecture or proposed next public schema

## 1. Authority and purpose

This document classifies the implemented public contract 0.5. The exact immutable authority is the named Data release, its schemas, capability registry, examples and manifest.

Public 0.5 remains the current compatibility boundary until a separately approved release supersedes it. It must not determine Builder vNext's internal storage model.

## 2. Release flow

```text
Builder release projection → immutable CharityGraph Data release → Viewer and other consumers
```

Builder working state, private evidence, caches and operational databases are outside the public contract.

## 3. Public objects

Contract 0.5 provides:

- subject cards with a stable legacy public subject key;
- source-record sidecars;
- evidence registries;
- source bindings;
- common observation semantics;
- coverage and a release-owned capability registry;
- financial reports, source-faithful statement rows and canonical metrics;
- activities, beneficiaries, descriptive/navigation geography, participation, opportunities and programs;
- funding sources, fundraising methods and fundraising expenditure projections;
- relationships and classifications;
- derivatives and release metadata;
- explicit preservation of unresolved historical material.

## 4. Observation semantics

The common contract distinguishes:

- claim basis: direct, mechanically derived, inferred or estimated;
- extraction method: API, document text, table, OCR, vision, manual, deterministic parser or LLM;
- source records and evidence;
- reporting/effective/observed/assessed/generated time as applicable;
- optional confidence, warnings and derivation.

Extraction method does not determine claim basis.

## 5. Coverage

The initial capability registry includes regulatory profile/AIS, DGR, website, annual report, financial report/statements, activities, beneficiaries, geography, programs, participation, funding sources, fundraising methods, fundraising expenditure, native taxonomy and embeddings.

Coverage states distinguish observed, not found in assessed sources, unavailable, not applicable, retrieval failed, not yet processed, stale and unknown.

Omission has no negative meaning.

## 6. Financial contract

Contract 0.5 preserves:

- exact source amounts, currencies, unit scale and raw presentation;
- source statement order, hierarchy and signs;
- reporting period, reporting scope and consolidation state;
- all legitimate conflicting/non-comparable observations;
- explicit mechanical derivation and attribution components;
- a current-financial pointer rather than duplicated independently authored values.

Fundraising expenditure may be null when evidence is insufficient. No universal prior or peer fill is allowed.

## 7. Compatibility preservation

The release is a deterministic migration from an earlier release boundary without fresh source acquisition or semantic enrichment.

Where an old value lacked sufficient immutable evidence binding, contract 0.5 preserved it under a legacy container with its origin release and origin-card hash. Preservation does not make the value canonical and does not upgrade capability coverage.

The migration preserved 402 activity items, 226 beneficiary items, 198 geography items, 573 native-taxonomy assignments, six funding/fundraising items and 86 financial records in this manner.

## 8. Immutable release

The release contains:

- 120 subject cards;
- 228 source-record sidecars;
- 349 manifest artefacts.

Manifest checksum:

`01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`

These bytes must not be edited or regenerated in place.

## 9. Future migration

A future public contract requires:

- an approved product decision;
- versioned schemas and examples;
- subject-key and domain migration rules;
- losslessness and compatibility analysis;
- representation-consistency tests;
- Data and Viewer coordinated acceptance;
- a new immutable release and migration notes.

Until then, Builder vNext uses an explicit 0.5 projector/adapter and fixture suite.

