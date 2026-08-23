# CharityGraph Agent and Data Distribution Contract

**Status:** Canonical distribution requirements; current endpoints use public contract 0.5  
**Version:** 1.0-draft  
**Updated:** 2026-08-23

## 1. Purpose

Consumer LLMs, analytical tools and downstream systems are first-order CharityGraph channels. The public corpus must be discoverable, selectively retrievable, citable and interpretable without Viewer code or a proprietary integration.

## 2. Required discovery surface

A selected release must provide or identify:

- a current-release pointer;
- immutable release manifest and hashes;
- stable canonical subject routes;
- per-subject JSON and Markdown alternatives;
- crawlable semantic HTML through Viewer;
- source-record and evidence links;
- schemas and capability definitions;
- sitemap and permissive robots policy;
- licence, attribution, version and citation guidance;
- bulk JSONL/CSV/Parquet where declared by the release.

## 3. Representation authority

Builder selects governed observations, coverage and derivatives into a `ReleaseProjection`. Data publishes immutable release artefacts. Viewer renders the selected release.

JSON, Markdown, HTML and bulk formats must agree on shared released values. They are projections from the same release selection, not independently authored records.

CSV is a convenience flattening and never defines the knowledge model. Parquet is an analytical projection or declared snapshot. Markdown is a compact human/LLM representation, not a place for raw high-dimensional vectors or private evidence.

## 4. Selective retrieval

A consumer retrieving one subject should be able to understand:

- identity and scope;
- source-native versus governed versus derived status;
- evidence and source role;
- reporting/effective time and freshness;
- coverage and assessment scope;
- relevant taxonomy/version/term;
- release and schema version;
- unresolved or conflicting status.

The consumer should not need to download the corpus or execute Viewer JavaScript to obtain this information.

## 5. Analytical retrieval

Bulk releases must support defensible cohort construction and corpus analysis. Analytical projections retain stable identifiers and sufficient scope, time, provenance and coverage fields to avoid false comparison.

Nested domains may use separate tables rather than destructive flattening. All analytical rows must be traceable to released subjects and observations.

## 6. Consumer-LLM requirements

Test at least:

- unaided discovery without naming CharityGraph;
- source discovery;
- directed use of CharityGraph;
- interpretation of supplied subject JSON, Markdown or URLs;
- organisation, program, portfolio and ecosystem questions;
- evidence citation and uncertainty;
- refusal to convert descriptive similarity or context into recommendation.

Use genuinely naive sessions deliberately. Routine indexing or model familiarity is product success, not test contamination to be preserved forever.

## 7. Citation

A useful citation identifies:

- the stable CharityGraph route or artefact;
- release ID and contract version;
- subject/observation where practical;
- upstream source when the claim depends on it;
- reporting/effective period for time-sensitive claims.

## 8. Privacy and publication safety

Public distribution excludes raw reports and website archives unless separately authorised, raw model prompts/responses, private correction submissions, credentials, databases, caches, retry state, cost telemetry, logs and debug dumps.

Source-family rights and attribution policy governs whether source-native payloads, compact observations or locator-only evidence may be published.

## 9. Failure and release continuity

A failed build or deployment must not replace the previous valid public release. After publication, verify routes, manifest identity, hashes, source references, sitemap, robots and Viewer selection.

## 10. Service evolution

Static artefacts are the durable public baseline. Add API or MCP delivery only when observed demand justifies operational complexity. A service must not become the only way to obtain the public data.

