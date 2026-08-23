# RC4 to public contract 0.5 compatibility and migration contract (proposed)

**Status:** Design approved / ready for implementation; no adapter, migration or Viewer change is implemented
**Baseline:** `releases/rc4-2026-08-14` (immutable)
**Target:** public contract `0.5`

## Compatibility recommendation

Use no active dual-projection window. Validate a deterministic RC4-to-0.5 fixture adapter, publish a new immutable 0.5 release with its own dataset identity and `based_on_release` ancestry, then migrate Viewer in lock-step. Retain RC4 indefinitely as an immutable historical release. Future Builder corpus runs need not emit a twin RC4 shape.

Release notes must name removed/renamed fields, link this matrix and identify the selected contract version. External consumers select a manifest/contract version explicitly. No consumer is expected to infer shape from `dataset_version`, and no Viewer obtains `latest` implicitly.

## Material field matrix

| RC4 field/path | v0.5 field/path | Classification | Semantic difference and strategy | Builder / Viewer / machine impact | Risk |
| --- | --- | --- | --- | --- | --- |
| `dataset_version`, `card_schema_version`, generator fields | `release.dataset_version`, `release.contract_version`; manifest authoritative | RESTRUCTURE | One contract version repeated and must agree; generator is not compatibility signal | adapter writes nested release metadata; Viewer selects contract | Medium |
| `causebase_id`, `subject_kind` | same / `identity.subject_kind` | KEEP | Opaque durable identity remains | low | Low |
| `legal_name`, `display_name`, operating/former names | `identity.*` | MOVE_TO_STRUCTURE | same content, grouped identity | straightforward map/render | Low |
| `external_identifiers`, registrations, tax statuses | `identity.*` | MOVE_TO_STRUCTURE | IDs remain external, not subject keys | map; consumers update path | Low |
| `canonical_url`, `acnc_profile_url`, `acnc_ais_url` | `identity.convenience_links` generated aliases | GENERATED_ALIAS | convenient links no longer truth/source identity | Viewer renders if present | Low |
| `source_resolutions` | `source_bindings[]` | RENAME | explicitly source-to-subject binding; preserve unresolved/conflicts | adapter preserves status/review | Medium |
| `source_native_records` / `source_payload` | `source_record_refs[]` / sidecar `source-records/*` | MOVE_TO_SIDECAR | cards stop carrying/duplicating public payloads | source-family policy publisher; Viewer follows references | High |
| card `evidence[]` | `evidence[]` compact registry | KEEP | IDs remain card-addressable; source record may add evidence refs | schema clarifies resolution | Low |
| `coverage[]` | `coverage.current[]` | RESTRUCTURE | namespaced capability and support references; current projection | map statuses, validate uniqueness | Medium |
| RC4 `enrichment_level` | omitted from canonical contract or generated release index | DEPRECATE | label is not capability truth | Viewer must not depend on it | Medium |
| `geography[]` | generated `display_geography[]` | GENERATED_ALIAS | legacy prose not controlled facets | retain during window | Low |
| `geography_observations` | `descriptive_geography[]` envelope observations | RENAME | explicit basis/method/time added | adapter fills legacy unknown only where justified | Medium |
| `navigation_geography` | `navigation_geography[]` typed terms | RESTRUCTURE | split `region_locality` into `region`/`locality`; no prose facet | controlled registry required | Medium |
| `causebase_summary`, summary evidence, `synthesis` | optional `summary` + `derivatives[]` | RESTRUCTURE | null/absent valid; lineage replaces operational synthesis metadata | Viewer handles absence | Medium |
| activities/beneficiaries plus observations | explicit domain observations | RESTRUCTURE | legacy strings become generated display projections | map supported evidence; no invented basis | Medium |
| `participation_modes` | generated compatibility alias only | DEPRECATE | plain string list not canonical truth | Viewer moves to observations | Low |
| `participation_observations` | `participation[]` | RENAME | add ID, basis/method/time; action/evidence remain separate | map/render update | Medium |
| `opportunities` | `opportunities[]` envelope observations | RESTRUCTURE | preserve optional data, no false identity inference | map as sparse | Low |
| `programs` | `programs[]` nested observations | RESTRUCTURE | add source binding/promotion criterion; no program subject requirement | map/render update | Medium |
| `financial_records` | `financial_reports[]` | RESTRUCTURE | report/statement/row hierarchy is canonical; RC4 conveniences become annotations | major adapter/validation | High |
| source ordered items / statements / statement rows | `financial_reports[].statements[].rows[]` | KEEP + RESTRUCTURE | preserve labels/order/signs; add envelope | lossless transformation required | High |
| `financial_metrics[]` | `canonical_metrics[]` | RESTRUCTURE | observation references and reconciliation; no hidden scalar | Viewer uses current pointer | High |
| `functional_expense_allocations` | report statements + `fundraising_expenditure` projection | RESTRUCTURE | no implied universal allocation | EJA fixture protects semantics | High |
| `donations_gifts_bequests` | `analytic_projections.donations_gifts_bequests` | MOVE_TO_STRUCTURE | explicit inputs/denominator/lineage | lossless EJA check | High |
| `fundraising_expenditure` | `analytic_projections.fundraising_expenditure` | MOVE_TO_STRUCTURE | direct share and derived amount distinct observations | lossless EJA check | High |
| `funding_sources`, `fundraising_methods` | named observation arrays | RESTRUCTURE | common envelope and supported absence semantics | moderate mapping | Medium |
| `classifications[]` | `classifications[]` | RESTRUCTURE | assignment basis separate from method | map; preserve taxonomy/version | Medium |
| `taxonomy_maintenance_signals` | none | PRIVATE_ONLY | internal review information cannot leak | excluded from publication | Low |
| `embedding`, similarities bulk | `derivatives[]`, bulk semantic artefacts | RESTRUCTURE | compact public lineage, vectors remain bulk refs | Viewer semantic index explicit | Medium |
| `derivative_assessments` | `derivatives[]` | RENAME | add generated/reused/refreshed/invalidated and public-safe lineage | adapter map | Medium |
| RC4 broad `method` fields / `extraction_method` | `claim_basis`, `extraction_method`, optional `derivation` | RESTRUCTURE | directness separated from recovery/method | required semantic review of adapter | High |

## Breaking changes

The breaking changes are nested identity/release paths, removal of card-embedded source payloads, new coverage capability IDs, observation envelopes, optional summary, financial report/metric restructuring, replacement of plain participation/geography arrays as truth, and removal of private taxonomy signals. The 0.5 adapter must never turn RC4 extraction method into a claim basis, silently select a financial conflict, or convert source signs in-place.

## Safe migration sequence

1. Freeze RC4 checksum fixtures, including all EJA donation/fundraising values and sparse/identity/multi-period cases.
2. Implement Builder models, validators and a deterministic RC4-to-0.5 adapter; emit both versions only for representative fixtures first.
3. Compare semantic projections record-by-record. A field must be losslessly preserved, deliberately moved, generated as an alias or explicitly unavailable—never silently dropped.
4. Add an explicit 0.5 Viewer renderer/adaptor and test it against the fixture release. Keep RC4 renderer only for the stated compatibility window.
5. After approval, perform a controlled rebuild, publish a separate immutable 0.5 release and migration notes; do not overwrite RC4.
6. At the next breaking pre-1.0 contract release, remove the transitional RC4 renderer/aliases from active consumers while retained RC4 artefacts remain accessible.

## RC4 fixtures and acceptance conditions

The fixture suite must include EJA (rich financials, direct/derived fundraising), a zero-financial sparse card, one deliberately unresolved/ambiguous source binding record, and APNIC Foundation (multiple financial periods). It must assert card/source/manifest version agreement, reference resolution, source-row order/labels/signs, all EJA figures, no private fields, and an absent summary. Existing immutable RC4 bytes are test input only and must never be mutated.
