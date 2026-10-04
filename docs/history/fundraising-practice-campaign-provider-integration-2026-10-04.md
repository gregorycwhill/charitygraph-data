# Fundraising practice, campaign and provider integration — 4 October 2026

**Status:** Completed review-only Builder integration record.

**Authority:** Implements lanes A and B of `FUNDRAISING_SUCCESSOR_MATRIX_2026-10-04.md` and the bounded policy in `FUNDRAISING_VOCABULARY_MEASUREMENT_RESEARCH_GATE_2026-10-04.md`. It creates no acquisition, production ingestion, public schema, Viewer, release, or scale authority.

## Implemented contract

Builder now carries separate versioned collections for standing fundraising practices,
bounded campaigns/appeals and directed fundraising-provider relationships. Funding source
and aggregate fundraising expenditure remain separate fields. The local review projection
contains only the typed collections; it does not adapt the legacy flat method field.

Each assertion retains source-native wording, scope, valid and observation time,
lifecycle, source role, production method, confidence/uncertainty, coverage state and
evidence IDs. Provider relationships additionally retain their common directed
relationship, resolved provider subject, relationship status/time and role direction.

## Guards and verification

The integration rejects duplicate typed IDs, same-axis practice facets, unknown facets,
observed assertions without evidence, dangling embedded provider-relationship evidence,
and repeated or contradictory provider role assignments for the same target/provider-role/scope.

Focused contract tests compile a card through JSON validation, project it, and verify that
practice, campaign and provider subjects remain distinct while historical/ended lifecycle,
scope/valid/observation time, source role, method, uncertainty, coverage/missingness and
evidence metadata survive. Refusal fixtures cover missing/unprocessed practice data and
contradictory provider roles.

## Deliberate non-claims

This work does not infer F2F setting, external agency, compensation, regular giving,
organisation-wide continuity or current use. It allocates no money to a practice, campaign
or provider, and makes no ROI, effectiveness, causal or donor-economics claim. Candidate
vocabulary remains review-only and source-adapter research remains outside production
ingestion.
