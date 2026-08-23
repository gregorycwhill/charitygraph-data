# CauseBase public-data contract 0.5 (proposed)

**Status:** Design approved / ready for implementation; not a production schema
**Contract version:** `0.5`
**Applies to:** a future pre-1.0 CauseBase Data release
**Baseline:** immutable RC4 at `releases/rc4-2026-08-14`

## 1. Scope and versioning

This is the concrete public contract approved in direction by `PUBLIC_CONTRACT_CONSOLIDATION_PROPOSAL.md`. It is deliberately a small, explicit JSON contract, not an entity-attribute-value model or a claim graph.

`0.5` is the public **card contract** version. A release has one `contract_version`, each card and source-record sidecar repeats that value, and the release manifest is authoritative for the selected release. The value must agree everywhere. `schemas/vnext/release.schema.json` is the machine-readable expression of this draft.

Pre-1.0 `0.x` contract releases may be breaking. Breaking releases must publish migration notes and retain their immutable release artefacts; no SemVer-compatible guarantee is implied before 1.0. Patch/document revisions may correct documentation or validation without changing public semantics. No consumer should infer compatibility from generator or editorial-policy versions.

## 2. Release contract and ownership

The authoritative boundary is:

`Builder → immutable CauseBase Data release → Viewer/static or other consumers`.

A release directory contains `manifest.json`, `schema/`, `cards/`, `source-records/`, `taxonomy/`, `coverage.json`, public bulk projections, checksums declared in the manifest, and release-history/current-release metadata. Viewer takes an explicit selected Data-release directory through `CAUSEBASE_DATA_RELEASE_DIR`; it must not fetch or resolve `latest`, and its output must copy rather than link the selected artefacts.

Required release metadata is `release_id`, `dataset_version`, `contract_version`, `based_on_release`, `generated_at`, release-owned capability-registry ID/path, `card_count`, `source_record_count`, `validation.status`, artefact hashes/sizes, licence/attribution notice and compatibility metadata. `release_id` is immutable and path-safe; `dataset_version` is the human/release label. RC4's short physical directory name is an archival Windows-path workaround, not a new public version convention.

## 3. Public object model

| Object | Purpose and stable ID | Required core / references | Time and provenance | Public status / versioning |
| --- | --- | --- | --- | --- |
| Release | Immutable publication boundary; `release_id` | manifest, schema, cards, sidecars, checksums | `generated_at`; build policy | Public bulk; contract fixed for that release |
| Subject card | Durable CauseBase subject; opaque `causebase_id` | identity, `subject_kind`, release metadata; references observations, source records and evidence | representation/build time | Public card; same ID persists across releases |
| Source record | Independent upstream record; `source_record_id` | family, native/upstream ID where available, URL/publisher, acquisition, evidence | retrieved/published/effective time | Public sidecar only when source-family policy permits |
| Evidence reference | Citable source fragment; `evidence_id` | title, source role, URL when public, location | observed/reporting time | Public if its URL/metadata are safe; cards carry a compact registry |
| Canonical observation | One governed assertion; `observation_id` | common envelope plus domain payload | claim basis, recovery method, evidence/source and time | Public when its payload is public-safe |
| Financial report / statement / row | Preserve source-native financial structure | report/statement IDs, source rows; metrics reference row observations | report period, source location, extraction | Public canonical structure; raw report remains private unless separately approved |
| Derived projection | Transparent analytic result | observation IDs, inputs and method | derivation time and rounding/uncertainty | Public where useful; never replaces inputs |
| Coverage observation | Capability support state | capability, status, supporting references | assessed/observed time | Public current projection, historical observations optionally retained |
| Relationship | Asserted subject-to-subject relation | relationship ID, target, type and evidence | valid/observed time | Public only when supported; no empty history system |
| Participation / program | Discrete supported observations | local observation ID, value, evidence | status and observed/effective time | Public card structures; program is not a subject by default |
| Classification | Taxonomy assignment | taxonomy/version/term/basis/method | assessed time, evidence and confidence | Public; private maintenance signals excluded |
| Derivative lineage | Validity of a derived output | derivative ID/kind, inputs, disposition | generated/assessed time | Public lineage; raw prompts/telemetry private |

An object may cite multiple source records and an upstream record may resolve to zero, one or multiple subjects. ABN, ACNC ID, domain and names are never subject primary keys.

## 4. Common observation envelope

Domain observations use this envelope, then place their domain fields in an explicit structure. They do not become generic key/value records.

```json
{
  "observation_id": "obs:...",
  "subject_id": "cb_...",
  "kind": "financial_statement_row",
  "claim_basis": "direct",
  "extraction_method": "vision",
  "source_record_ids": ["src:..."],
  "evidence_ids": ["ev:..."],
  "time": {"reporting_period": {"start": "2024-07-01", "end": "2025-06-30", "label": "2025"}},
  "confidence": "high",
  "warnings": []
}
```

`claim_basis` is exactly `direct`, `mechanically_derived`, `inferred`, or `estimated`. It answers why CauseBase can state the proposition. `extraction_method` is independent and is one of `api`, `document_text`, `table`, `ocr`, `vision`, `manual`, `deterministic_parser`, `llm`, or a documented extension. Tool names are never claim bases. `confidence` is optional and only meaningful for uncertain recovery, inference or estimation.

Non-direct observations require `derivation`: `method_kind` (`formula`, `heuristic`, `rule`, `peer_imputation`, `llm_inference`, `approved_model`), versioned `method_id`, input observation IDs, optional formula/rule reference, rounding/uncertainty, and material model/version where applicable. EJA's stated fundraising share is `direct`/`vision`; its approximate amount is `mechanically_derived`, with `formula`, the share and total-expenses observations as inputs, and a rounding warning.

## 5. Source records, evidence, and privacy

Source records are sidecars indexed by `source-records/{encoded source_record_id}.json`; the manifest contains their hashes and cards hold `source_record_refs`, not duplicate payloads. A source record has `source_record_id`, `source_family`, `upstream_id` when known, `source_url`, `publisher`, `dataset_version`, `retrieved_at`, optional `source_published_at`, `reporting_period`, `valid_from/to`, source-safe `source_fields`, optional public-safe `source_payload`, and `evidence_ids`.

Publication uses source-family policy: structured public regulator/source-native payloads may be sidecars when lawful and useful. Full PDFs, website snapshots, raw model prompts, raw correction submissions, cache/retry state and spend telemetry are private by default. Evidence references are not copied reports; they are citable public metadata/locations.

| Data class | Card | Sidecar/bulk | Private archive/operations/review |
| --- | --- | --- | --- |
| Identity, registrations, status | public | public bulk | review signals private |
| Public-safe source payload | reference only | source-family policy | source archive retained privately |
| PDFs and website snapshots | no | only separately approved republication | private archive |
| Evidence/source URLs/action URLs | public references | public | private if unsafe |
| Financial statements/rows | public structure | source sidecar may support | raw reports private by default |
| Prompts, token/cost/retry/cache telemetry | no | no | private operations |
| Derivative lineage | public compact lineage | public bulk | raw inputs/output telemetry private |
| Corrections | governed public decisions only | public when approved | raw submissions/private review |
| Taxonomy maintenance diagnostics | no | no | private review |

## 6. Subject card

A card requires `causebase_id`, `subject_kind`, `identity`, `release`, `source_record_refs`, `coverage`, and `evidence`. `identity` retains legal/display/operating/former names, external identifiers, registrations, tax statuses, entity status, optional website and optional descriptive location. `canonical_url`, ACNC profile URL and AIS URL are generated convenience links, not canonical truth; the external identifier/registration and source records remain authoritative.

Cards embed compact public convenience identity fields and observations. They do not embed source-native payloads. `summary` is optional/nullable; a sparse authoritative card is valid with no prose. When present, a summary is a derivative with an explicit `derivative_id`/lineage.

Descriptive geography is an evidenced observation with free text. Controlled navigation geography is a separate `navigation_geography[]` projection with stable typed terms `country`, `state_territory`, `region`, or `locality`. RC4 `geography[]` is retained only as a generated display alias during compatibility; it is not v0.5 canonical truth.

## 7. Coverage, participation, programs, classifications and relationships

Coverage is one coherent `coverage.current[]` projection, each entry containing `capability`, `status`, `observation_ids`/`source_record_ids`/`evidence_ids`, `assessed_at`, optional `observed_at`, and freshness detail. Status is one of `observed`, `not_found_in_source`, `not_available_from_source`, `not_applicable`, `retrieval_failed`, `not_yet_processed`, `stale`, `unknown`.

Initial controlled capability IDs are deliberately small: `regulatory.acnc_profile`, `regulatory.ais`, `tax.dgr`, `web.website`, `report.annual_report`, `financial.report`, `financial.statements`, `programs`, `participation`, `funding.sources`, `fundraising.methods`, `fundraising.expenditure`, `taxonomy.causebase`, and `semantic.embedding`. `observed` means a defensible governed observation exists, not that a preferred scalar exists. Thus EJA `fundraising.expenditure` is observed: its direct 10% and mechanically derived approximate amount support the capability.

Participation observations carry `participation_id`, mode, label, evidence, optional external absolute `action_url`, status, and observed/effective time. Evidence URLs are never assumed to be action URLs. Programs are nested observations with a source-local `program_id`, name, optional description/URL, status, dates and evidence. A later durable subject promotion requires an explicit governed relationship (`program_of`, etc.); names never imply identity.

Classifications include taxonomy ID/version, stable term ID and label, `claim_basis`, `assignment_method`, evidence and optional confidence. CauseBase taxonomy remains independent from regulator taxonomy. Relationships contain `relationship_id`, source/target IDs, type, basis, evidence, optional confidence/review status and valid/observed time. Reserved relationship lifecycle semantics are `merged_into`, `split_into`, `successor_to`, and `tombstone`; publish them only where a real supported case exists.

## 8. Time and derivative lineage

`retrieved_at` and `source_published_at` belong to source records. `valid_from`, `valid_to`, and `reporting_period` describe world/effective time and belong wherever the assertion has them. `observed_at` records the observation/source state; it is not a substitute for reporting period. `generated_at` is used for derived objects and the release; `assessed_at` is used for coverage and derivative validity checks. A card's `release.generated_at` is representation time, not a claim that all card facts were observed then.

Derivative lineage has `derivative_id`, `kind`, `input_hash`, input observation/evidence IDs, `contract_version`, `generated_at`, optional `assessed_at`, policy/prompt version where material, model/version where material, disposition (`generated`, `reused`, `refreshed`, `invalidated`), and optional invalidation reason. Summary, classification, embedding, similarity and analytic projections use lineage appropriate to their validity rules.

## 9. Financial contract

Financial source preservation has three layers.

1. `financial_reports[]` represents a source/report, its report/evidence ID, period, scope/consolidation, currency and statements.
2. A statement retains type, exact printed title, source ordering, page/table/location and rows. A row is an envelope observation with stable ID, exact source label, row type (`heading`, `line_item`, `subtotal`, `total`), indentation, source/current amount, comparisons, source sign, recovery metadata and evidence. P&L and financial-position rows are comprehensive where source extraction supports them; cash flow/equity remain source-native structures.
3. `canonical_metrics[]` annotate source observation IDs (for example revenue or total expenses). They retain all legitimate conflicting/non-comparable observations with a reconciliation status; no hidden universal precedence scalar exists. `current_financials` is an optional pointer over those observations, never duplicated values.

Canonical amount objects preserve `source_amount` as the reported exact decimal (including sign), `source_raw_value`, unit/currency and `normalised_amount`. Normalisation records unit scaling, not FX conversion. Canonical ordinary metrics and analytic amounts are non-negative (`revenue`, `total_expenses`, assets, liabilities, fundraising expenditure). `surplus_deficit` and `net_assets_equity` preserve economically meaningful signed values. A metric derived from a negatively printed source row records the source row ID and `sign_normalisation` such as `absolute_magnitude`; it never discards the original source amount.

When a legacy RC4 value cannot be given a defensible canonical observation envelope, it is retained in `legacy_unbound` with the immutable origin release and SHA-256 of its origin card. This is public preservation, not a governed observation and does not by itself produce `observed` coverage. The container is deliberately domain grouped, including descriptive domains and unresolved historical financial records.

`current_financials.selection_policy` is one of `latest_nonconflicted_reporting_period`, `explicit_report`, or `not_selected`. It must identify period, scope and all selected metric observation IDs. It is absent if competing same-period/scope observations are unresolved.

Funding/fundraising structures are explicit. `funding_sources[]` and `fundraising_methods[]` are observations. `donations_gifts_bequests` is an analytic aggregate with component observation IDs, amount, denominator observation ID/amount, share, period/scope and derivation lineage. `fundraising_expenditure` contains a direct reported share observation plus optional mechanically-derived amount; it does not imply a full functional allocation.

Where attribution is genuinely bounded, an analytic projection may carry `lower_bound`, `upper_bound`, an optional defensible `point_estimate`, and explicit attribution components marked `definite`, `possible` or `excluded` with an additivity basis. Bounds are not efficiency, ROI or causal fundraising economics; no midpoint, fractional allocation or donor-income causal assertion is implied without its own governed rule.

## 10. Validation invariants

- `causebase_id` is unique/stable; external identifiers never become subject IDs.
- All public source/evidence/observation references resolve within the selected release or stated public URL.
- Coverage has no duplicate current capability; `observed` has support; `not_yet_processed` cannot coexist with processed supporting observations; `stale` retains the prior observation and freshness reason.
- Source statement row order, exact labels and source signs are preserved. Canonical metrics reference real row/observation IDs. A derived value references inputs and method. A current-financial pointer has one coherent period/scope and no unresolved competing selection.
- A participation `action_url` is a public absolute external HTTP(S) URL; evidence URLs are not automatically action URLs.
- Derivative lineage inputs resolve; a reused derivative retains its original generation identity.
- Manifest, card and source-record contract/dataset versions agree. Every card source-record reference exists. Private-only fields do not appear in public output.

## 11. Machine/LLM legibility and abstraction review

A consumer can answer identity, direct/derived basis, recovery method, evidence, period, current/historical status, coverage, EJA donations/fundraising, participation destination and unresolved source/identity conflict from the card plus referenced sidecars—without Viewer code. The remaining generated aliases (`canonical_url`, ACNC convenience URLs and legacy display geography) are explicitly non-authoritative.

Rejected abstractions: a universal claim graph, general identity-history store, universal financial reconciliation engine, mandatory summary, arbitrary geography facets and an enormous coverage enum. The initial registry and derivative method vocabulary are controlled but extensible by documented pre-1.0 contract change.

## 12. Open product questions

None block the corrected 0.5 design package. Exact controlled geography term registries and future source-family publication permissions are governed implementation/catalogue work, not new product choices. A later release must decide a concrete machine-readable licence/attribution manifest shape from actual upstream terms before publishing additional source families.

## 12A. Approved correction clarifications

Cards explicitly retain evidence-bound `activities`, `beneficiaries`, `descriptive_geography`, `funding_sources`, `fundraising_methods`, `participation`, `opportunities`, `programs`, and `identity.website`; these are not optional-by-schema omissions. Each uses the common observation semantics where relevant while retaining domain payloads.

The release owns an applicable capability registry (`capability-registry-0.5-initial`): `regulatory.acnc_profile`, `regulatory.ais`, `tax.dgr`, `web.website`, `report.annual_report`, `financial.report`, `financial.statements`, `understanding.activities`, `understanding.beneficiaries`, `understanding.geography`, `programs`, `participation`, `funding.sources`, `fundraising.methods`, `fundraising.expenditure`, `taxonomy.causebase`, `semantic.embedding`. Every applicable card has exactly one current entry for every registry capability. Omission has no meaning. `consolidated` is JSON `true`, `false`, or `null` (unknown).

Use `sourceReportedMoney` only for values printed by an upstream source. It preserves source/normalised amounts and source fidelity. CauseBase-derived amounts use `{amount, currency}` plus derivation/rounding metadata; they must not manufacture `source_amount` fields. For EJA, the source 10% share is rounded/limited precision, `0.10 × 5,852,789 = 585,279` is mechanically derived and approximate, and the normal human display is approximately AUD 585k.

Derivative generation and later assessment are separate. `generated_under` permanently records original output-contract, input hash, generation time, policy/prompt and material model. `current_assessment` records v0.5 assessment/reuse/refresh/invalidation; a projection never rewrites the original generation contract.

Pre-1.0 `0.x` contract releases may be breaking and must publish migration notes. Patch/document corrections may use a patch version or document revision. A v0.5 release has its own identity and records RC4 as `based_on_release`; RC4 never changes contract version. Migration is immutable RC4 → deterministic fixture adapter/validation → new immutable v0.5 release → lock-step Viewer migration. There is no active twin RC4/v0.5 production projection requirement.

Source-resolution corpus state is distinct from card evidence. Only a resolved/bound source normally appears in ordinary `source_record_refs` and observations. Candidate, ambiguous and unresolved records remain outside the card unless the uncertainty itself is published as an explicit identity-resolution notice.

## 13. Implementation after approval

Implement only after approval: Builder v0.5 models/validators and an RC4-to-v0.5 adapter; frozen EJA/sparse/identity/multi-period fixtures; publication validation; a Viewer v0.5 renderer/adaptor; then an approved controlled rebuild and migration note. Do not modify RC4 or deploy as part of this design.
