# Product-value bounded commitment-content representation fix - 15 September 2026

**Status:** Historical implementation record; bounded fix complete.

**Decision preserved:** The completed product-value evaluation remains `ADVANCE_WITH_BOUNDED_FIX`. This implementation records completion of the required fix; it does not revise or rerun that evaluation.

**Scope:** Close the specific Commitments V5 representation weakness identified by the bounded product-value slice. This is not scale authorization, a broad commitment redesign, or a public contract change.

## Defect and invariant

The earlier `commitment_stated` shape required commitment kind and instrument metadata but had no required field for the substantive WHAT. A candidate could therefore pass mechanical validation with period, instrument, kind and scope while omitting what was being committed to.

Builder now exposes the strengthened provider contract as `phase6-corrected-contracts-v5.1`. Each `commitment_stated` proposition must contain `commitment_content` in one of two tagged forms:

- `source_text`, with nonblank substantive commitment wording; or
- `structured_equivalent`, with both `committed_action_or_state` and `object_or_result` populated.

The existing scope, evidence locators/carrier roles, epistemic class, commitment kind, instrument, and optional `stated_period` remain distinct. A missing `stated_period` is allowed; a supplied period is preserved independently and cannot be inferred from another commitment or its enclosing strategy. Metadata alone does not satisfy the required content field. The V5.1 schema is strict and locally revalidated; its tagged content alternatives use the provider-supported `anyOf` form, with the local typed validator enforcing the representation tag and required fields.

The older V5 response contract remains available as a historical read-only parser. This provides structural access to retained bytes but does not accept those records under V5.1. V3/V4 parsers and historical payloads were not rewritten. No V6/V7 contract was introduced.

## Regression and compatibility record

Offline fixtures cover the bounded examples from the completed review:

- the Greenpeace mission/objective form (“secure the Earth's ability to nurture and sustain life in its diversity”) passes without a date;
- the 1.5°C objective passes with “by the end of the century” preserved;
- the strategic goal passes with its separate 2024–26 period;
- the deforestation target passes with “by 2026” preserved;
- a metadata-only candidate fails with a diagnostic naming `commitment_content`;
- a typed action/object structured equivalent passes, while a metadata-shaped incomplete equivalent fails.

The tests validate representation shape and temporal preservation. Whether content is faithful to cited source evidence remains a semantic and human-governance question; the structural validator does not claim to prove that meaning.

The corrected validator was applied read-only to the three retained product-value response packets produced under Commitments V5 (12 propositions total). Six `commitment_stated` candidates (one Red Cross, four Greenpeace, one Sunrise) lack `commitment_content` and fail V5.1 with the expected missing-field diagnostics. The other six propositions in those packets are non-commitment proposition types and remain valid under their existing V5.1 shapes. These six commitment candidates predate the strengthened invariant. The old V5 historical parser reads all three original response structures successfully. No response bytes, hashes, candidate records or human adjudications were modified, and the completed experiment was not rerun. Other earlier Phase 6 V5 provider payloads are not present in the current Builder worktree; its redacted V2 structural-history fixture remains covered by its existing compatibility test.

## Product status and boundaries

Implementation status: `PRODUCT_VALUE_BOUNDED_FIX_COMPLETE`.

The historical evaluation decision remains `ADVANCE_WITH_BOUNDED_FIX`. The bounded slice demonstrated useful Inspect, constrained Compare and Verify over its fixed cohort and evidence universe, while preserving key evidence-role, scope, epistemic and missingness distinctions. It did not establish broad 20-section coverage, Top-100 production scale, Capacity/access/availability capability, uncontrolled/open-ended research, or automated semantic promotion. Phase 5 remains active; Top-100 scale is not authorized; Capacity remains deferred. No canonical/public promotion, Viewer work, public v0.5 change, or merge occurred.

Provider calls: **0**. New source acquisitions: **0**. New human adjudications: **0**. Canonical/public promotions: **0**.

## Validation

The implementation was validated offline with commitment-content regression cases, Commitments V5/V5.1 contracts, Outcomes V6 contract tests, semantic-contract and product-value experiment tests, the full Builder suite, relative links in edited Data docs, strict UTF-8 decoding, and `git diff --check`. One mojibake marker in the pre-existing body of `PRODUCT_VALUE_VALIDATION_SLICE_DESIGN_2026-09-14.md` predates this change and is outside the added implementation entry; it was not changed as part of this bounded fix. Validation and local commit identities are recorded in the corresponding Builder and Data commits; neither commit was pushed or merged.
