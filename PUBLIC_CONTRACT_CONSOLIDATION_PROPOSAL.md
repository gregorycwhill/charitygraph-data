# CauseBase Public-Contract Consolidation Proposal

> **Authority status:** Historical consolidation proposal. Its relevant 0.5 contract decisions are now implemented in PUBLIC_CONTRACT_0_5.md; it does not propose a current public-schema change.

**Historical status at the time:** approved design direction; not a current public-schema proposal.
**Date:** 2026-08-14  
**Basis:** accepted 120-card RC4 Viewer publication, `phase2b-2026-08-14-rc4-fundraising-projection-correction`

## 1. Executive summary

RC4 demonstrates that CauseBase is already more than a flat charity directory: it is a versioned, evidence-bound card publication with source-native records, selective canonicalisation, and derived material. The core direction is sound. The current `0.1` card, however, has accumulated overlapping presentation fields and multiple partially-general observation patterns while RC2–RC4 added capabilities.

This proposal recommends a deliberately modest pre-1.0 consolidation:

1. make a three-layer contract explicit: source-native records, canonical observations, and derived projections;
2. use small shared envelopes for provenance, time, coverage and derivation, while retaining explicit domain structures for financial statements, participation, programs, relationships and classifications;
3. make claim basis (`direct`, `mechanically_derived`, `inferred`, `estimated`) independent of extraction method (`api`, `document_text`, `table`, `ocr`, `vision`, `llm`, `manual`, `deterministic_parser`);
4. preserve complete source-native financial statements and retain canonical headline metrics and analytic aggregates as separate objects; and
5. publish one authoritative RC4 release tree in CauseBase Data before any vNext migration work.

The architectural direction and decisions recorded below are approved. No production schema has changed: this document is not an implemented schema specification.

### Ground-truth caveat

The accepted RC4 manifest and 120 cards were verified from Viewer commit `77d84befa90c1079346e146f82504ff2ef0d9f26` and imported byte-for-byte into `CauseBase-Data/releases/rc4-2026-08-14`. The shorter directory name avoids Windows path-length failure for the accepted percent-encoded sidecar names; the immutable manifest retains the full dataset version `phase2b-2026-08-14-rc4-fundraising-projection-correction`. CauseBase Data is now the authoritative release owner; Viewer reproduces a selected Data release through an explicit local preparation boundary.

### Approved decision record

- Claim basis is `direct`, `mechanically_derived`, `inferred` or `estimated`; extraction and derivation/inference methods are separate.
- Coverage describes whether a capability has a defensible governed observation, not whether a preferred exact scalar was printed.
- Canonical ordinary financial magnitudes are non-negative; surplus/deficit and net assets/equity retain meaningful signs; source statement rows preserve printed signs.
- Source-native payload publication is source-family governed and sidecar-first; the card references rather than duplicates full payloads.
- Capability names use a small namespaced/extensible registry. The initial registry remains a schema-specification task.
- A scope-safe current financial view may be an explicit pointer over observations, never an independent or silently selected scalar.
- Identity continuity semantics are defined now; actual assertions publish only when a real case requires them. Sparse-card summaries may be absent. Public derivative lineage exposes validity-relevant metadata but not prompts, telemetry or caches.

## 2. Evidence inspected

Shared product documents: `PRODUCT.md`, `PRINCIPLES.md`, `EXPERIENCES.md`, `CURRENT_STATE.md`, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md`, `TEST_PLAN.md`, and `CODEX_TO_CHATGPT_HANDOFF.md`.

Artefacts inspected: RC4 Viewer `manifest.json`, cards, Markdown projections, JSON/JSONL/CSV/Parquet references, source-record sidecars, taxonomy, schema, coverage and release-history artefacts; RC3 CauseBase Data release artefacts for comparison.

Implementation inspected: Builder `models.py`, publication rendering/validation, Phase 2A/2B/2D projection paths, source structures and registry rules; Viewer search and presentation modules. Private archive boundaries were inspected only through the implementation’s declared inputs and publication safeguards; no archive was changed or copied.

Representative validation cases:

- **Environmental Justice Australia (EJA)** — rich report/AIS case, RC4 card `cb_604da7f26c6c48dd934e713edc493e9f`.
- **Multicultural Senior Digital Support QLD Inc** — sparse card, `cb_1ed4d44d34e949098005cf9c6ca1885c`.
- **Defence Force Welfare Association – National Inc** — branch/membership language without an asserted relationship, `cb_408c113ff48c4b4f91c7697b00b211dd`.
- **EJA again** — legitimate different financial observations for 2022–23 AIS and 2024–25 report, demonstrating retention rather than scalar overwrite.

## 3. Current-state schema map

| Concept | RC4 form and creation | Public status/layer | Assessment |
| --- | --- | --- | --- |
| Identity | `causebase_id`, `subject_kind`, legal/display/operating/former names, external identifiers, registrations, tax statuses; Builder registry and source normalisation | Public; canonical | Stable semantic direction. `acnc_profile_url`/`acnc_ais_url` duplicate generic source URLs. |
| Source records | `source_native_records[]` with family, dataset version, URL, retrieved/observed/effective dates, fields/payload, mappings and evidence IDs; rendered as card content and deduplicated sidecars | Public-safe source-native; private raw archives excluded | Correct layer, but a full public API payload can be very large and field mappings are strings rather than typed links. |
| Evidence | `evidence[]` / `EvidenceRef`: ID, source type, title, publisher, URL, observed date, reporting period, page/section/hash | Public; evidence/provenance | Useful common reference, but source location and time are too thin for all observation types. |
| Coverage | `coverage[]`: capability, eight-state status, optional source/evidence, observed date, freshness note | Public; canonical capability observation | Sound state vocabulary. “one effective state per capability” is enforced, but transition/history semantics are implicit and capability strings are open. |
| Financial sources | `financial_records[]`, line-item projections, ordered rows, statements, comparatives and `MoneyObservation` | Public; mixed source-native/canonical | Best-developed area. There are overlapping breakdowns, headline fields and statements; their hierarchy is not explicit in JSON. |
| Financial canon | `financial_metrics[]` with multiple observations/reconciliation, canonical annotations on rows | Public; canonical | Correctly preserves conflicts, but duplicates direct headline fields in `financial_records`. |
| Fundraising | `fundraising_expenditure`, `funding_sources`, `fundraising_methods`, report-level `donations_gifts_bequests` | Public; derived/canonical mix | Direction is good. The four representations need a common derivation envelope and clearer scope/time links. RC4 correctly leaves expenditure null for all 120 where no defensible amount exists. |
| Participation | legacy `participation_modes[]`, richer `participation_observations[]`, dated `opportunities[]` | Public; canonical observations | Correct evidence/action distinction in richer object; duplicate legacy list should not remain canonical. |
| Programs | `programs[]` nested observations with stable local program IDs, status, source URL/evidence | Public; canonical observation | Correct default: not every program is a subject. It lacks explicit promotion/relationship criteria. |
| Classification | taxonomy ID/version/term/method/confidence/evidence; private taxonomy-maintenance signals excluded from public output | Public canonical classification; private review signals | Stable multi-taxonomy direction. Assignment method currently conflates a model process with the fact’s epistemic status. |
| Geography | descriptive `geography[]`, provenance-aware observations in Builder, and controlled `navigation_geography[]` | Public; canonical projection | Two valid jobs but card serialisation still exposes the unprovenanced display list. |
| Relationships/history | relationship type, target ID, evidence, note, valid/observed dates, confidence/status; source resolutions separately retain ambiguity | Public canonical observations | Stable identity principles. Merge/split/tombstone are registry concepts but lack a published continuity representation. |
| Derivatives | summary, taxonomy, fundraising, embedding, similarities assessments with input hash/reuse reason; synthesis metadata separately records model/prompt/evidence hash | Public derived metadata | Validity inputs are split across two models; `assessment_method` strings hide a reusable contract. |
| Publication | card JSON/Markdown, source-record sidecars, bulk JSON/JSONL/CSV/Parquet, taxonomy/schema, manifest and release history | Public projections | Intended one-card/many-projections rule is correct. Current Data/Viewer RC3/RC4 split violates the single authoritative-release boundary. |

### RC4 card shape

The card has 45 top-level properties, including identity, display/navigation conveniences, evidence, canonical facts, source-native records, financial structures and publication metadata. Required schema fields are only `causebase_id`, legal/display name, entity status, summary, dataset version and build time. This permissiveness is appropriate before 1.0, but it means consumers need conventions rather than schema constraints to know which fields are authoritative, derived, historical or optional.

## 4. Problems and accidental complexity

| Finding | Classification | Recommendation |
| --- | --- | --- |
| Accepted RC4 lives in Viewer while Data release tree ends at RC3 | RESTRUCTURE | Establish Data as authoritative immutable release owner before vNext. Viewer should copy/consume that release, not become its sole canonical location. |
| `card_schema_version` remains `0.1` although Builder Phase 2 paths set later internal versions | RENAME / RESTRUCTURE | Define one public contract version source in the manifest and schema; do not derive it from an implementation constant. |
| `acnc_profile_url`, `acnc_ais_url`, `website`, evidence URLs and source-record URLs overlap | MERGE | Retain `website` as organisation self-link; move regulator/document locators under source records/evidence and derive convenience links. |
| `geography`, activities, beneficiaries and participation modes coexist with richer observation objects | DEPRECATE | Preserve display projections during migration, but make evidence-bound observations canonical. |
| `income_breakdown`, `expense_breakdown`, balance-sheet breakdown, ordered line items, statement rows and headline fields overlap | RESTRUCTURE | Statements/rows are source truth; headline annotations and analytics reference row IDs. Convenience breakdowns become generated views. |
| EJA represents total expenses as positive in the headline and negative in the statement allocation denominator | APPROVED RESTRUCTURE | vNext canonical ordinary financial magnitudes are non-negative; source statement rows retain printed/accounting signs. Surplus/deficit and net assets/equity retain meaningful signs. RC4 remains unchanged. |
| `direct_observation: bool`, derivation method and extraction method are mixed in finance and classifications | MERGE / RENAME | Introduce separate `claim_basis` and `extraction_method` fields everywhere a claim is published. |
| Arbitrary coverage capability strings and one-current-state overwrite behaviour | RESTRUCTURE | Register capability IDs, retain historical coverage observations privately or in a history stream, and publish a current projection with explicit effective time. |
| `source_payload` can expose a large full API response in each card plus sidecar | PRIVATE-ONLY / KEEP | Keep public structured regulator payload where terms permit, but place it in a single sidecar; cards carry an ID and selected mapping, not a duplicate payload. |
| `source_resolutions` appear on cards despite being source-record-level review state | RESTRUCTURE | Keep resolution assertions in a source-record collection; project only resolved bindings or explicit unresolved notices to cards. |
| `taxonomy_maintenance_signals` appears in generated schema despite model comment that it is private | PRIVATE-ONLY | Remove from public schema in a future breaking version; retain only private review packet structures. |
| `enrichment_level` is a coarse label alongside precise coverage | DEPRECATE | Keep as a generated UI badge only if needed; do not treat it as contract truth. |
| Named participation action source URL versus evidence URL is already separate | KEEP | Preserve and formalise the distinction. |
| Nested program records are not automatically subjects | KEEP | Formalise promotion/relationship criteria; do not create a generic graph. |

No consolidation is warranted for opaque IDs, external identifier separation, multi-taxonomy support, raw source labels, exact-decimal money, retained conflicting financial observations, or the static artefact publication model.

## 5. Proposed conceptual model

### 5.1 Three layers

**Layer 1 — source-native.** A source record describes what one acquired public source said at a time. It preserves source family, source ID, locator, retrieval/published/effective time, original field labels/payload where republishable, and source-specific structure. Reports, snapshots, prompts, credentials and raw operational traces remain private unless there is a clear public right and product purpose.

**Layer 2 — canonical/harmonised observations.** These are selective CauseBase concepts that make sources interoperable: subject identity, external IDs, registration/DGR status, controlled navigation geography, coverage, taxonomy assignment, relationship, financial headline annotation and participation path. They never erase the source record they depend on.

**Layer 3 — derived/analytic projections.** These include neutral summaries, donations/gifts/bequests aggregates/shares, mechanically calculated fundraising amounts, classification where not source-native, embeddings, similarities and “current” selections. Each identifies governing inputs and method.

RC4 already follows this model in spirit. The vNext contract should state the layer on every published record/object rather than relying on field location or a Viewer convention.

### 5.2 Small common observation grammar

Use a shared envelope only where the semantics truly recur:

```json
{
  "observation_id": "obs:...",
  "subject_id": "cb_...",
  "kind": "financial_statement_row | participation | relationship | coverage | ...",
  "basis": "direct | mechanically_derived | inferred | estimated",
  "extraction_method": "api | document_text | table | ocr | vision | llm | manual | deterministic_parser",
  "evidence_ids": ["ev:..."],
  "source_record_ids": ["src:..."],
  "time": {"reported_at": null, "valid_from": null, "valid_to": null, "observed_at": null},
  "confidence": "high | medium | low | null",
  "warnings": [],
  "derivation": null
}
```

This is an embedded envelope, not a universal EAV table. Financial rows keep financial fields; relationships keep their target and type; coverage keeps its state; classifications keep taxonomy terms. `derivation` is required when `basis` is not `direct` and contains a method such as `formula`, `heuristic`, `peer_imputation`, `llm_inference`, `rule` or `approved_model`, input observation IDs, and optional uncertainty.

### 5.3 Claim basis is not extraction method

| Situation | `basis` | `extraction_method` |
| --- | --- | --- |
| ACNC API reports total revenue | `direct` | `api` |
| Report text explicitly states a value | `direct` | `document_text` |
| Report chart says “Fundraising 10%” and vision recovers it | `direct` | `vision` |
| 10% × reported total expenses | `mechanically_derived` | `deterministic_parser` (derivation method `formula`) |
| Published rule estimates an amount from known components | `estimated` | `deterministic_parser` (derivation method `heuristic`) |
| Model identifies a relationship expressed ambiguously in evidence | `inferred` | `llm` (inference method `llm_inference`) |

This preserves the key RC4 rule: an LLM may recover a directly reported fact; it does not thereby turn the fact into a CauseBase estimate.

### 5.4 Time

Minimum public fields are source URL/ID, `retrieved_at` where public acquisition freshness matters, source publication/report date when known, `observed_at`, reporting-period start/end/label, and `valid_from`/`valid_to` for temporal relationships or statuses. A release has `generated_at`, release/version and immutable manifest hash. Private-only metadata includes retry attempts, cache timestamps, parser diagnostics, raw snapshot paths and detailed spend telemetry.

Subjects persist through ordinary name, status, address or program changes. Attributes and relationships are time-bounded observations. Merge/split/tombstone must be represented as identity-continuity assertions with evidence, rather than minting a new subject for each changed attribute.

### 5.5 Coverage

Canonical states remain: `observed`, `not_found_in_source`, `not_available_from_source`, `not_applicable`, `retrieval_failed`, `not_yet_processed`, `stale`, and `unknown`.

Public coverage projection:

```json
{"capability":"fundraising_expenditure","state":"observed",
 "as_of":"2025-10-01","source_record_ids":["src:..."],"evidence_ids":["ev:..."],
 "note":"A directly reported share and a defensible mechanically derived approximate amount exist; no exact printed dollar amount exists."}
```

Invariants: each current card has at most one current projection per registered capability; `observed` requires a defensible governed observation and evidence or a source record; an output requiring a source cannot coexist with `not_yet_processed` for that capability; a direct fundraising share or mechanically derived amount makes fundraising-expenditure coverage `observed`, even if an exact printed dollar amount is absent; `stale` retains the prior observation and adds freshness context, rather than silently changing it. Private operations retain attempts, retries and failure classifications. A small namespaced/extensible capability registry replaces arbitrary implementation strings; its initial terms remain a schema-specification task.

## 6. Domain treatment

### Financials

Financial source truth is a `financial_report` with scope, period, evidence and one or more source-faithful statements. A statement has ordered rows, headings/subtotals/totals, original labels, current/comparative amounts, page/location and extraction metadata. Cash flow and equity statements remain supported even if not present in every release.

Canonical headline annotations (`revenue`, `total_expenses`, `surplus_deficit`, `assets`, `liabilities`, `net_assets`) refer to source-row observation IDs and carry a reconciliation set when legitimate observations conflict. A canonical headline is not another source row.

Functional allocations are direct source observations when a chart/table reports a percentage. A calculated amount is a separate mechanically-derived observation whose denominator and rounding warning are explicit. Funding-source observations retain their original row/label and may be linked to a controlled analytic category. `Donations, gifts & bequests` is an analytic aggregate: it lists components, denominator row, formula and share; it must not replace the printed source rows.

The EJA RC4 allocation denominator demonstrates the approved sign convention: its statement-derived total expenses is negative (`(5,852,789)`), while canonical `total_expenses` is the non-negative magnitude `5,852,789`. vNext retains original printed/accounting signs on source rows; surplus/deficit and net assets/equity retain meaningful signs. RC4 is not rewritten.

Fundraising expenditure is a separate analytic projection. A capability is `observed` where a defensible direct share or derived amount exists, even when no exact printed dollar amount exists. Claim basis remains `direct`, `mechanically_derived`, `inferred` or `estimated`; extraction and derivation/inference methods remain separate. An unavailable/null result remains valid where no defensible observation exists.

### Participation

`participation` is a canonical observation with mode, label, evidence IDs, optional `action_url`, status and effective/observed time. Evidence proves the claim; `action_url` is a user destination and may be absent. A dated event or vacancy remains an `opportunity`, not proof that the general participation path is current.

### Programs and subject boundary

Default to a nested program observation. Promote to a durable subject only when it has a durable independent identity/role, evidence supports it being separately useful to users, and its relationship to the parent is evidenced. Use `program_of` only for an explicit relationship assertion. Name similarity alone neither promotes nor merges. Ambiguity remains unresolved and is published as such where material.

### Identity and relationships

Retain opaque permanent `causebase_id`; ABN/ACNC/domain/name are external identifiers. Registration and DGR are roles/statuses. A relationship assertion has type, source/target IDs, evidence, status, confidence and valid/observed times. For a merge, split or tombstone, retain the old ID as resolvable with an explicit continuity assertion; do not rewrite history or turn every source record into one organisation.

### Classifications, geography and derivatives

Classification remains domain-specific: taxonomy ID/version, stable term ID/label, assignment basis, evidence and confidence. Source-native classification is direct; an LLM-assisted classification is derived and needs lineage. Descriptive geography remains human-friendly, while controlled navigation geography stays a distinct canonical navigation projection.

Derivative lineage is a reusable envelope with `derivative_kind`, generated/released time, input IDs/hashes, contract version, editorial/rule/prompt version, model where material, disposition and invalidation reason. Summary, taxonomy/classification, embedding and similarity may need distinct validity rules; do not force all into one generic recomputation engine.

## 7. Public and private boundary

Public: stable subject identity; public-safe source records; useful canonical observations; derived projections; evidence/provenance needed to inspect claims; current coverage/freshness; release/schema/taxonomy metadata; public source URLs; JSON/Markdown/bulk artefacts and schemas.

Private: credentials; raw prompts and excerpts; raw website/PDF archives where republication is not appropriate; cache/retry/log/staging state; unmoderated correction submissions; detailed token/spend telemetry; parser diagnostics; review notes; taxonomy-maintenance signals; full private source archive locations.

RC4’s largest boundary risk is duplicated full `source_payload` in cards and source-record sidecars. The approved vNext direction is a source-family publication policy: public-safe structured records may appear in sidecars where source terms and product value justify it; cards reference them rather than duplicating payloads. Raw PDFs and website snapshots remain private absent a separate right and purpose. RC4 is unchanged.

## 8. Representative before/after examples

### A. EJA — rich report case

**RC4:** EJA has both an AIS 2022–23 financial record and a report 2024–25 record. The latter carries `$5,016,000` revenue, `$5,852,789` total expenses, printed income rows including “Donations, fundraisings and lectures” `$2,051,817`, report-statement rows, a fundraising chart allocation and a null fundraising-expenditure projection. The card also carries separate `financial_metrics`, a `donations_gifts_bequests` analytic object, source-native ACNC payload, program observations and a participation observation.

**vNext proposal:** retain the two distinct `financial_report` observations. Within the 2024–25 report, preserve the printed row and statement order; create `canonical_metric: revenue` referencing the total income row; create `analytic_aggregate: donations_gifts_bequests` referencing that printed income row and revenue denominator; preserve the reported fundraising percentage as `basis: direct, extraction_method: vision`; retain the approximate dollar amount as a distinct `basis: mechanically_derived` formula. Fundraising-expenditure coverage is `observed` because that governed observation set satisfies the capability, while the observation set makes its approximation explicit. This prevents a report row, canonical metric and analytic aggregate from being mistaken for three different facts.

### B. Sparse case — Multicultural Senior Digital Support QLD Inc

**RC4:** the sparse card retains regulator identity and source-native information but has limited report/web enrichment.

**vNext proposal:** publish the regulator source record, resolved subject binding, registration and external identifiers; retain available canonical financial/regulatory fields; set each unprocessed or unavailable capability explicitly. Do not manufacture a summary, fundraising amount, participation action or program merely to satisfy a rich-card layout. A general-purpose LLM can distinguish “no report processed” from “the organisation does not have a report.”

### C. Identity/relationship — Defence Force Welfare Association – National Inc

**RC4:** website evidence refers to branch membership and branch activity. The card is a national subject, but no evidenced branch subjects or `branch_of` relationships are asserted.

**vNext proposal:** keep the national card and the source-native/website observations. Treat branch language as a descriptive participation/funding observation unless a branch has a durable subject and evidence supports a relationship. If a later branch subject is promoted, publish a `branch_of` assertion with evidence, time and confidence. Do not infer a network graph from names or prose.

### D. Multiple observations — EJA financial conflict/non-comparability

**RC4:** the AIS 2022–23 revenue is `$7,770,242`; the report 2024–25 revenue is `$5,016,000`. Neither should overwrite the other because the reporting periods differ. Within a single period, different scope or rounded sources may also legitimately diverge.

**vNext proposal:** observations retain reporting period/scope/source and the metric reconciliation object says `non_comparable`, `divergent`, or `precision_consistent` as applicable. The card may expose a clearly labelled latest/direct projection, but it must identify the selection policy. No universal “best value” scalar is introduced.

## 9. Breaking-change and migration inventory

| Change | Compatibility / impact | Risk |
| --- | --- | --- |
| Move source-native payload from card to referenced sidecar | Breaking for consumers reading `source_native_records[].source_payload` | Medium; improves size and ownership clarity. |
| Replace legacy display arrays with observation projections | Backward-compatible aliases possible for one pre-1.0 release | Medium; Viewer/search read these arrays today. |
| Restructure financial records around statements/row IDs and annotations | Breaking for consumers of convenience breakdowns/headline fields | High; must be validated against EJA and sparse AIS cards. |
| Add claim-basis/extraction-method separation | Additive initially; becomes required later | Low/medium; semantics gain is substantial. |
| Capability registry/current coverage projection | Additive for states; breaking for arbitrary custom capability strings | Medium. |
| Move source resolution and private taxonomy signals out of public card | Breaking only for consumers of implementation leakage | Low. |
| Standardise public release ownership/version source | Reversible publication cleanup, not a product-semantic change | Medium operationally, high governance value. |

Eventual Builder work: new vNext models/validators, projection adapters, coverage invariants, typed source-record references, statement/annotation conversion, derivative-lineage validation, and publication ownership checks. Eventual Viewer work: accept vNext projections, render claim basis/period/coverage, use sidecar source records, and avoid dependence on legacy arrays. Eventual Data work: immutable RC4 import, vNext schema/release path, compatibility documentation, migration fixture corpus and checksum validation.

## 10. Closed product decisions

1. **Public source-native payload breadth — approved.** Use a source-family publication policy. Public-safe structured regulator/source-native records may be sidecars where source terms and product value justify them; cards reference those records and do not duplicate full payloads. Raw PDFs and website snapshots remain private unless separately justified and permitted.
2. **Coverage capability registry — approved.** Use a small namespaced/extensible public registry, with controlled extension before 1.0. Its initial terms are deferred to the subsequent schema-specification task.
3. **Current financial projection — approved.** CauseBase may expose an explicit scope-safe pointer over observations (for example `latest_nonconflicted_reporting_period`), including selected observation IDs, period and selection policy. It is not an independent scalar and never silently chooses among unresolved same-period/scope conflicts.
4. **Identity continuity — approved.** Define stable merge/split/successor/tombstone semantics now, but publish actual continuity assertions only when real cases require them. Opaque published CauseBase IDs remain resolvable; no empty identity-history subsystem is required.
5. **Sparse-card summary — approved.** Summary may be null or absent. Structured authoritative evidence can stand alone; no fallback prose is created merely to fill a card shape.
6. **Public derivative lineage detail — approved.** Publish input/evidence hash, policy/prompt version, output/contract version, material model/version, generated/assessed time and reuse/refresh disposition. Keep raw prompts, detailed inputs/outputs, token/spend data and retry/cache state private.
7. **Canonical financial sign convention — approved.** Canonical/user-facing ordinary magnitudes are non-negative; surplus/deficit and net assets/equity retain meaningful signs; source rows preserve printed/accounting signs exactly.

## 11. Recommended approval and implementation sequence

1. **Record the approved decision gate and repair release ownership** (completed by this bounded task): import and verify immutable RC4 in CauseBase Data; make Viewer preparation select it explicitly.
2. **Write the vNext public contract/schema and compatibility matrix** from these approved decisions; retain a frozen RC4 fixture suite.
3. **Implement adapters and validators** in Builder against a small representative fixture set, especially EJA, sparse, relationship and conflicting-observation cards.
4. **Update Viewer only after Builder projection validates**, preserving an explicit RC4 compatibility mode during the pre-1.0 transition.
5. **Run a controlled rebuild only after approval**, compare RC4/vNext record-by-record, human-review differences and publish a migration/release note.

### Abstraction check

The proposed observation envelope solves several demonstrated problems: duplicated provenance/time semantics, direct-versus-extraction confusion, and derivative traceability. It does not turn the contract into generic EAV: financial statements, relationships, programs, coverage and classifications remain explicit structures. No graph database, event sourcing, generic knowledge graph, backend service or API is proposed. Where RC4 has one proven use only (identity continuity and some derivative kinds), the proposal reserves a small representation rather than introducing a framework.

## 12. Review conclusion

The decision gate is closed and the RC4 authoritative-release boundary is repaired. The next task is the bounded vNext public-schema and compatibility specification—not a migration or rebuild. The pre-1.0 consolidation should improve explicitness for humans and general-purpose LLMs—identity, source, evidence, direct/derived status, period, coverage and freshness—without discarding source-native detail or inventing a universal ontology.

**NO production schema migration performed.**  
**NO deployed public release changed.**
**NO corpus processing or model calls performed.**
