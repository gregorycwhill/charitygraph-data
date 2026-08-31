# CharityGraph Source, Evidence and Publication Governance

**Status:** Canonical governance specification, version 1.1-draft

**Date:** 28 August 2026

**Applies to:** Source registration, acquisition, evidence, adjudication and future publication

## 1. Purpose

This document governs how CharityGraph turns public material into traceable knowledge without confusing a source, an extraction, a judgment and a published assertion.

## 2. Core chain

The canonical chain is:

`source registry entry → acquisition event → source artefact → evidence span or structured record → observation → assertion/classification → adjudication → publication projection → release`

Every link has a stable identifier and append-only history. A public record may simplify this chain, but Builder must be able to reconstruct it.

## 3. Source registry

Each source family is registered before routine acquisition. Registration records:

- source owner, publisher and jurisdiction;
- source class and authority role;
- access URL or acquisition mechanism without secrets;
- licence, reuse, attribution and redistribution conditions;
- privacy and sensitivity classification;
- expected update cadence and temporal semantics;
- identifier and scope expectations;
- parser/extractor and validation policy;
- robots, terms, rate and access constraints;
- publication eligibility and required projection;
- responsible steward and review date.

Sources include official registries, regulators, charity publications, industry shadow registries, academic datasets, media and direct observations. “Shadow registry” is a first-class source role where an industry body authoritatively records participation, fees, codes or accreditation within its remit.

## 4. Authority is proposition-specific

A source is not globally authoritative. Authority depends on the proposition, time and scope. For example:

- ACNC may be authoritative for current registration status;
- an industry association may be authoritative for its own membership or code participation;
- a charity may be authoritative for a current program description but not for an independent impact conclusion;
- a regulator or court may be authoritative for a formal decision;
- direct observation may be authoritative that an advertisement or collection point was observed at a time and place, not that it represents the organisation's entire strategy.

The source registry records these roles explicitly.

## 5. Acquisition

Acquisition events record:

- requested and resolved location;
- retrieval time and applicable effective date;
- response metadata and content type;
- content hash, byte size and storage reference;
- terms/licence snapshot or reference;
- success, absence, block, failure or partial status;
- retry and replacement relationships;
- tool/version and material parameters.

Credentials, authorisation headers and sensitive URL query strings are never written into public reports or provenance records.

## 6. Artefacts and evidence

Source artefacts are immutable content-addressed objects. Normalisation or OCR produces a new derived artefact linked to its input; it does not overwrite the source.

Evidence may be:

- a structured record and field;
- a text span with locator;
- a table region;
- an image region or OCR span;
- a document-level inference where narrower evidence is impracticable;
- a governed direct observation with time, place, medium and observer protocol.

Evidence locators must be sufficiently stable to support review. Public projections may omit copyrighted bodies while retaining citation, hash and lawful excerpt/locator metadata.

## 7. Observation and assertion

An **observation** records what a source, extractor, model, person or sensor reported. It is append-only and does not become true merely because it exists.

An **assertion** is CharityGraph's governed, scoped proposition about a subject. It records:

- predicate and value;
- subject and subject scope;
- valid/effective time and observation time;
- evidence and contributing observations;
- method and responsible agent;
- confidence/strength where applicable;
- lifecycle status;
- contradiction and supersession relationships;
- publication eligibility.

Accepted edits preserve continuity through exact directed lineage. Previous assertions are not rewritten.

## 8. Absence semantics

The following are distinct:

- explicitly stated absence;
- searched-for but not found;
- source not acquired;
- field not attempted;
- field not applicable;
- evidence insufficient;
- value withheld;
- extraction or model failure.

Only the first is ordinarily publishable as a positive absence claim without further reasoning.

## 9. Mechanical and model processing

Deterministic work includes retrieval, parsing stable formats, identifier validation, exact joins, arithmetic, schema validation and content hashing.

Model-assisted work includes difficult OCR, semantic extraction, entity recognition, relevancy screening, program decomposition, classification, synthesis and drafting. Each model result records the task contract, input references, prompt/template version, provider/model, parameters, output, validation and cost.

Builder must not evolve a growing pile of Python phrase rules to imitate general language comprehension. Deterministic post-processing should validate structure and invariants, not silently reinterpret model semantics.

## 10. Contradiction and adjudication

Contradictory observations are retained. Resolution considers proposition-specific authority, time, scope, evidence quality and method. Adjudication records:

- question and candidate assertions;
- decision and rationale;
- reviewer or model task;
- accepted evidence and material rejected evidence;
- exact lineage to the resulting assertion;
- review and expiry conditions.

Routine low-risk classification may be promoted under an approved model policy. High-risk claims use stricter gates.

## 11. Direct observation readiness

The model must accommodate future sousveillance and field-observation projects without building collection tooling now. A direct observation can record:

- observed organisation or uncertain identity;
- activity, channel and mechanism;
- time interval and geographic/place scope;
- physical or media placement;
- campaign, creative and call-to-action where observable;
- evidence object, capture method and lawful-use constraints;
- observer protocol, confidence and verification;
- relationship to later corroborating or contradicting evidence.

Examples include residential door-knocking, staffed shopping-centre tables, charity bins, shop-counter goods donation, out-of-home advertising, television commercials and digital advertising.

## 12. Publication projection

Private working knowledge is richer than public Data. Publication policy determines which assertions and provenance elements are projected, considering:

- licence and copyright;
- privacy and sensitivity;
- claim consequence;
- confidence and review state;
- public usefulness;
- schema stability;
- minimisation and contextual fairness.

Publication never grants source authority retroactively and never deletes contrary internal evidence.

## 13. Release governance

A future release requires:

- an immutable versioned manifest;
- schema and vocabulary versions;
- artefact hashes and safe relative paths;
- generation and validation metadata;
- coverage and known-limitations reports;
- licence, attribution, branding and reuse information;
- correction pathway;
- reproducible release pointer and Viewer compatibility declaration.

Contract 0.5 remains frozen byte-for-byte. vNext changes use new schemas and release identities.

## 14. Retention and deletion

Retention is governed by reproducibility, source rights, privacy, cost and legal obligation. Content-addressed storage avoids unnecessary duplication. A retention or deletion event itself is recorded. Deleting a restricted body need not destroy the remaining lawful provenance metadata or decision history.

## 15. Minimum source acceptance checklist

Before a source enters a production run, confirm:

- identity and proposition-specific authority;
- lawful acquisition and intended use;
- stable identifiers or a scoped matching plan;
- temporal meaning;
- expected failure and absence modes;
- validation/evaluation sample;
- evidence locator strategy;
- publication projection;
- update and retirement policy;
- cost and rate implications.

## 9A. LLM-first semantics and reconstructible provenance

Evidence-bundle or document-level inference is legitimate when the input scope is recorded. First-party wording is strategically authored evidence: it may support a source-native proposition but is not taxonomy authority. Keyword presence or frequency does not establish semantic fit.

Open-ended semantic relevance, entity/program/service interpretation, durability boundaries, activity/population interpretation, taxonomy/SDG alignment and semantic ambiguity are model tasks by default. Deterministic processing validates structure and invariants; it does not reproduce language understanding through lexical heuristics. Provenance records source artefact, evidence bundle, task/prompt policy, provider/model, output, validation and governed disposition so the result is reconstructible; it does not claim token-level causal explanation or expose internal model reasoning.

## Complete-card semantic chain (propagated decision)

The governed chain is: source artefact -> reusable representation -> semantic
task projection -> observation or relationship -> downstream task view. A
substantive acquired source must not silently collapse into severe truncation or
a binary placeholder. Native extraction, OCR and layout recovery are
representation; gaps are recorded as explicit coverage states. A task
projection may mechanically exclude fields that would contaminate an
independent lens while preserving the original artefact and lineage.

Where an official site serves a network, brand, federation or auspice
arrangement, domain provenance is not subject ownership. Assertions attach to
the lowest evidence-supported scope. Bounded same-origin sitemap/navigation
acquisition is permitted; open-ended relevance remains a model task, not a
keyword or semantic Python rule. Downstream taxonomy tasks normally consume
governed semantic knowledge and follow evidence lineage rather than rereading
raw source bodies.

## 16. Semantic source role and result replay

A source artefact has both content and role. Evidence about a subject is not necessarily evidence of activity by that subject. Semantic task construction preserves, where applicable, the publisher/source owner, source class, proposition-specific authority role, first-party or regulator-reported status, regulator context, independent-evidence status and the subject/scope to which the evidence relates.

Regulator navigation, interface, search and portal material is not charity activity. First-party activity descriptions can support charity activity claims. Regulator-reported program fields are distinct from regulator interface functionality. Tasks must receive sufficient provenance context to make these distinctions; this is not implemented as a forbidden-phrase list.

A valid ModelResult is retained as a provenance-bearing artefact and routine rebuilds reuse it. An intentional technical replicate is explicitly authorised as evaluation; replicate identity remains distinct from accidental duplicate identity.
