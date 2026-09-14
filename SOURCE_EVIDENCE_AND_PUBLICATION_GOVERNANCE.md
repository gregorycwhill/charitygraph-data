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

### 5.1 Source-rights decisions and provider processing

Accessibility is not authority to retain, transmit to a provider, or redistribute. Every content-bearing acquisition SHALL have a versioned, artefact-bound rights decision before it is offered to an external model provider. The decision binds the source artefact and the exact transmitted representation, records an evidence locator and hash, assessment date/scope, policy identity, attribution and conditions, and separately records local retention, private provider transmission and public redistribution.

The only rights bases are `explicit_open_license`, `explicit_terms_permission`, `direct_permission`, `statutory_exception`, `public_facts_only`, `unknown`, and `prohibited`. Unknown and ambiguous terms fail closed. `public` privacy classification and `private_review_only` publication eligibility are not rights classes. `public_facts_only` may authorize a transmission only where the bound representation is actually factual material and the decision says so; copied prose is not relabelled as fact.

**Approved product policy:** `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1` (version `1.0.0`), approved by the CharityGraph product owner on 13 September 2026. This records CharityGraph product policy, not external legal advice or legal certainty. It permits CharityGraph research, semantic analysis, classification, extraction, evaluation, and evidence-grounded knowledge construction using bounded snippets and bounded source-native structured factual representations from lawfully accessed, public-facing material, including public websites and documents. It applies only to private analytical processing under a versioned provider-processing policy. It does not grant unrestricted local retention or public republication.

**Approved local-retention decision:** The CharityGraph product owner subsequently approved a Fair Dealing-based bounded local-retention policy, `CG_BOUNDED_LOCAL_ANALYTICAL_RETENTION_V1` version `1.0.0`, for exact source excerpts/representations necessary for research, semantic analysis, adjudication, provenance, governed evidence construction, reproducibility of bounded experiments, and audit/review of governed propositions and coverage states. This is a CharityGraph product-policy decision, not external legal advice or legal certainty. It applies only where material was lawfully accessible/acquired without authentication, paywall, access-control circumvention or bypass; an exact source artifact and representation hash are recorded; the representation is limited to analytical need; complete/near-complete works are not retained for convenience; and purpose, scope, lifecycle and review are auditable. Explicit source prohibitions remain blockers. The decision does not authorize arbitrary website mirroring, whole-document warehousing, republication or public redistribution.

For V1, a provider decision under `statutory_exception` passes only if the artifact-specific record binds the exact sent-representation hash, source artefact and source record, public origin, source role, and acquisition receipt lineage; confirms public access without authentication, paywall, circumvention or bypass; confirms lawful acquisition; identifies one of the analytical purposes above; classifies the actual representation as `bounded_excerpt` or `structured_factual`; records that no explicit source term prohibits the relevant processing; and names the provider policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`. The provider policy is a condition, not the source-rights basis. Generic `statutory_exception` does not pass. Complete or near-complete works, unclear representations, controlled sources, unresolved lineage, missing provider policy, and explicit prohibitions fail closed. Decisions attach to exact representations and cannot be reused for changed inputs.

For the Phase 6 post-policy audit, a document excerpt is treated as bounded where its exact transmitted representation consists of no more than five selected page texts and no more than 20% of the identified source PDF. A structured factual representation is limited to one source-native entity record, not a bulk dataset or copied report. These are conservative V1 operating limits; they do not authorize altering a frozen input to meet a limit. The full text of a captured homepage is a complete page representation, not a bounded excerpt.

The original V1.0 provider-processing decision did not authorize local source retention. Local retention is now governed separately by `CG_BOUNDED_LOCAL_ANALYTICAL_RETENTION_V1` v1.0.0; provider permission never implies retention permission, and retention permission never implies provider permission. Every axis is recorded independently and bound to exact artifacts/representations. Neither decision authorizes public redistribution. Derived governed facts, observations, classifications and analysis remain subject to existing publication governance; evidence quotations remain separately constrained.

For each retained representation, record the exact source artifact ID, source record ID, representation SHA-256, retention policy ID/version, basis, permitted purpose, scope, lawful-access/no-circumvention and explicit-prohibition checks, acquisition lineage, retention status, lifecycle/review status and review due date. The approved product-value cohort's initial review date is 14 September 2027; renewal is not automatic and requires reassessment. Retain the bounded representation only while the approved analytical/governance purpose remains active; record deletion when that purpose ends and preserve lawful provenance metadata. Record provider transmission with its own exact decision ID/status and public redistribution with its own decision/status. A provider rights decision cannot be copied into the local-retention field; a local-retention decision cannot be treated as provider or publication authority. Unknown, stale, unbound or mismatched items fail closed. Deletion or review events are recorded without erasing lawful provenance metadata.

Explicit source terms that clearly prohibit the relevant processing override this policy route and block provider transmission. Terms that preserve uses permitted by the Copyright Act are not treated as a blanket prohibition of those uses. Silence is not permission: the basis, where V1 applies, is this approved product policy. A clearly suitable licence, explicit permission or direct permission remains preferable and is selected when the exact artifact and representation lineage supports it. In particular, no ACNC API response inherits a bulk-data CC licence without an exact licensed-resource binding.

Provider data handling is a separate policy dimension. The V1 provider-policy record refers to the OpenAI API/business default that inputs and outputs are not used for training unless the customer opts in; the actual selected service, policy version and no-opt-in posture must be rechecked before execution. This posture never supplies source permission. A future acquisition records the terms/licence identity and evidence URL or retained reference, evidence time, rights-policy version, source-access and bypass status, acquisition lineage, retention status, provider-processing status and redistribution status at acquisition where practical. Common explicit licences may be reusable only through a versioned policy; source family, URL reachability and source role never infer a decision at runtime.

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

For the bounded product-value experiment, the product owner approved a private experiment-only namespace for propositions and coverage states admitted only after independent human proposition-level adjudication. Raw candidates remain separate and are never rendered as governed projection content. Accepted items retain subject and legal/program/service scope, proposition type, evidence locator and exact retained representation, carrier role, epistemic status, reviewed-evidence universe, coverage state, source period, immutable candidate identity/hash, human disposition, adjudicator identity/role/time/version, and relevant request lineage. This namespace is not canonical Data, is not publicly projected, and does not authorize later canonical/public promotion; that requires a separate product-owner decision and release governance.

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
