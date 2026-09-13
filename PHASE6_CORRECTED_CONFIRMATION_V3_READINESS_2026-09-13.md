# Phase 6 corrected confirmation V3 — local readiness

**Status:** Historical repair and offline readiness evidence; V3 provider execution is not authorized

**Date:** 13 September 2026

**Scope:** Outcomes/evaluation, commitments/implementation, and capacity/availability/access

**Builder implementation:** local, unpushed commit `3db4d8b`

**Relationship:** V3 supersedes the failed `phase6-corrected-contracts-v2` for any separately authorized future confirmation. It does not rewrite or retry the stopped V2 run.

## Disposition

The three failures in the stopped confirmation are understood and repaired at the contract/preflight layer. The historical result remains 0/3 mechanically valid complete outputs, with three provider crossings and nine unsent requests. No new provider call, source acquisition, semantic output, candidate packet, adjudication, or governed promotion occurred during this repair.

Builder contract `phase6-corrected-contracts-v3` and provider schema identity `charitygraph-openai-structured-output-subset-v1` were used to prepare and certify the same bounded 12-attempt campaign offline. All 12 requests passed campaign-wide local preflight, covering nine distinct subject-bound schemas. The exact prepared manifest SHA-256 is `98f2034f452b746ac30c814a8c4870f9f91d6377d258381a71dab0092dd1df37`; the preflight report SHA-256 is `20ae0c89c90d027e5ea9d68585f5f02e0c409df7440e7e88846901d3a1b4e5c2`. Conservative maximum exposure remains AUD `0.264317`.

The run is `prepared_not_sent`, explicitly marked `not_authorized_for_v3_provider_calls`, and the executor hard-stops before constructing a provider client unless its internal authorization gate is separately changed. V2 authorization does not extend to V3. This record confers no execution authority. Future V3 execution requires a new product-owner decision and authorization bound to V3.

## Diagnosis and repair

### Outcomes and capacity schema rejections

The exact captured V2 provider-facing schemas contained Pydantic-generated Decimal patterns with negative lookahead. Outcomes had four instances, at `ActivityReported.properties.count`, `OutcomeObservedReported.properties.measured_result`, `OutputReported.properties.measure`, and `ReachReported.properties.count`. Capacity/access had four, at `CapacityLimitOrMeasure.properties.measure`, `HistoricalActivityVolume.properties.measure`, `ResourceOrWorkforceMeasure.properties.measure`, and `ServiceScaleMeasure.properties.measure`.

The remaining inspected schema constructs included `$defs` and local `$ref`, enums, `anyOf` for typed alternatives and nullable values, date/date-time formats, required object properties with `additionalProperties: false`, and `minItems`. The captured schemas had no `patternProperties`, conditionals, `allOf`, provider-facing `oneOf`, or unsupported composition. Decimal fields used number/string unions, with null where applicable; the local Pydantic Decimal parser remains in force. V3 removes only that exact generated Decimal pattern from the provider-facing schema. The local semantic model still parses and validates Decimal values. The provider schema is separately certified against the pinned Responses Structured Outputs subset before a request can be sent; see the [provider's Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs).

### Commitments response validation

The six historical V2 validation errors were not six independent policy violations. Four were `union_tag_invalid` errors caused by trying the captured commitments propositions against unrelated Outcomes/Capacity union branches (two errors for each affected proposition). The other two were genuine `value_error` failures: the propositions asserted a `first_party_claim` epistemic class while citing `historical_frozen_regulator_material`, a source role that cannot support a first-party claim. The raw response is retained only in the private historical run.

The regression fixture is structurally representative and privacy-scrubbed. It reproduces all six errors under the historical V2 validator. V3 dispatches the proposition list to the selected slice's typed adapter, so it reports only the two relevant source-role invariant violations. V3 continues rejecting the invalid response; no semantic rule was loosened. The stopped-run record's six-error summary and provider/accounting history remain unchanged.

## Provider certification and campaign preflight

The executor now certifies the exact materialized provider schema, checks its contract and schema identity against an explicit supported-keyword subset, verifies strict object/required-field and local-reference rules, and records schema version, schema hash, certification hash, and status on each ticket. The former rejected V2 schemas are saved as schema-only fixtures and fail certification because their patterns are unsupported; generated V3 schemas pass without patterns.

Before a campaign can cross the provider boundary, preflight checks every scheduled request's serialization and body hash, subject and scope identity, frozen source and locator bindings, ticket and physical-attempt identity, prompt and semantic-contract hashes, model route, cost authority, schema version, and schema certification. It collects request-level failures across the campaign. Any failure leaves all ticket states prepared, records a local pre-send failure, consumes no attempt authority, and sends no requests. The sender uses the same in-memory request bytes that preflight certified, preventing a later file change from substituting an uncertified body.

V3 response validation also requires the returned `contract_version` to equal the certified V3 identity. Cross-field epistemic and source-role invariants remain local deterministic checks.

## Offline readiness results

There are four planned physical attempts per capability: three subjects plus the predeclared repeat for the difficult case. The repeat is The Smith Family for Outcomes, Greenpeace Australia Pacific for Commitments, and St George Community Housing for Capacity/access. Hashes are SHA-256. Schemas are subject-bound, so the repeated case reuses its identical schema and certification hashes.

| Capability | Contract / lineage | Planned attempts and subjects | Campaign preflight | Distinct schema SHA-256 → certification SHA-256 |
|---|---|---|---|---|
| Outcomes/evaluation | `phase6-corrected-contracts-v3`, supersedes V2 | 4: The Smith Family (2 attempts), World Vision Australia, Bush Heritage Australia | 4/4 certified; 0 failed | Smith: `9dfb1f657e73e024d7578ca47176911db36c92180d2c32cf73d93698c7604fe2` → `6a4af51327dbec1c1771a5ad8ba3a9c50f9969a1efce4339df60da8ff6baf694`; World Vision: `cc80840e607752784e4f214edece34179b834cc438b37d437336b572fa669cce` → `e91c62ec80a49fe5661e33b6ace43f84373e276b15c104270485ecf7b4aa773f`; Bush Heritage: `0a6cd6f3b4801707a6a12ce56173cce6d008500279876dfd8bc66f950c4fb7b0` → `093cfbd22904514632aeef5f882df8a2fa4c426d07bf6f576e21b5c07f391721` |
| Commitments/implementation | `phase6-corrected-contracts-v3`, supersedes V2 | 4: Greenpeace Australia Pacific (2 attempts), Australian Red Cross Society, The Sunrise Project Australia Limited | 4/4 certified; 0 failed | Greenpeace: `f0075030b746a8437f2fe64475f3052b95f9631a68e16b657502e4df07c11ff3` → `36920816e97afb7b8ac811d0a539105eb67a2fd2be395b981d2793aa95019fc6`; Red Cross: `067a45984fdb9b8fb8daf2ef6165f7f7fa150391b936dec32cdc00d8027f279e` → `fced318d5c844105e415f3537c3b8010d69cd34ad61473b8aaab49686d95ca34`; Sunrise: `1041adc3f9fceec51517a494824169349a71d1a7ae369c56c48253752a5ec87f` → `1377a9af2753dfbfc1b7dfcb049e7e525942b500c5985ac1639af4f7cc13748d` |
| Capacity/availability/access | `phase6-corrected-contracts-v3`, supersedes V2 | 4: St George Community Housing (2 attempts), Royal Flying Doctor Service of Australia (Queensland Section), The Leukaemia Foundation of Australia Limited | 4/4 certified; 0 failed | St George: `ac698dc788b2ac421ab3a6c1ea019ee23b9af42281bd3699c81a586db1d8e21e` → `a6234963a0a939b804f9fce001ba4509dc0cf2d47baa1a28cc9f5a4bed0a367f`; RFDS: `5b61948620357b0d8047133783b60f70739f7ce9c1f7081c883721b63a447e6d` → `814411610b36db1dfc09ff2f3083b50b3283008ad7cb76e5e908d98d65b572f5`; Leukaemia Foundation: `c3f15aad067764ba1a038772787c91e10ceffeaeaaf3a6fc81bd9e8b25658259` → `07c23834c09e77cd01d70bb5abadedcd21a8d2b59c5f8d6833d2333a149e5d58` |

Campaign totals: 12 scheduled, 12 certified, 0 failed; all request and physical-attempt identities unique; provider calls 0; new source acquisitions 0; attempt authority consumed 0. Provider execution, semantic acceptance, human adjudication, and promotion remain pending and unauthorized by this repair task.

The prepared route is OpenAI Responses with `gpt-5.6-luna`, reasoning effort `low`, Standard delivery. This route was recorded and locally validated only; no model was called.

## Validation and remaining decision

The full Builder test suite passed after the repair, with one pre-existing skip and three existing deprecation warnings. New regression coverage includes both previously rejected schema fixtures, all three current schema families, campaign-wide no-POST behavior on a certification failure, zero-attempt accounting for local failure, historical commitments error reproduction, V3 source-role rejection, V3 version echo enforcement, and exact certified-body transmission. The full-suite command was `pytest -q` in the Builder repository.

The one remaining product-owner decision is whether to authorize a new V3 provider campaign under its own bounded authority. No further schema or semantic-policy decision is needed to establish local readiness. Provider calls, source acquisitions, governed promotions, and candidate generation for this repair task are all zero.
