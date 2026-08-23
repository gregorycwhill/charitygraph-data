# Historical snapshot — superseded 2026-08-23

**Status:** Historical reference only; not current executable instruction.  
**Current authority:** [DOCUMENT_AUTHORITY.md](../../DOCUMENT_AUTHORITY.md)

---

# CharityGraph Test Plan

> Historical note: pre-pivot CauseBase test records below are retained for provenance. New active checks use CharityGraph names while immutable releases retain their original artefacts.

**Status:** Accepted product direction  
**Updated:** 2026-08-15

## Cross-product release gates

- publication allowlist and absence of raw/private/working artefacts;
- manifest integrity, versioning and artefact hashes;
- evidence-reference and identity consistency;
- taxonomy/version/term validity;
- source-drift anomalies and failure isolation;
- preservation of the previous valid release after a failed build;
- correction-dependent regeneration when governed corrections are introduced;
- agent usability: an unfamiliar coding/AI agent can discover the current release and correctly retrieve and interpret one subject without downloading the national corpus.
- append-only annual observations, temporal relationship validity and current-projection selection;
- source-native sidecar provenance and source-field/canonical-field separation;
- deterministic change profiles, dependency decisions and recorded derivative reuse;
- source inventory, historical-release ledger and exact deployment-bundle safety.
- immutable-release ownership: a Data-owned release reproduces an isolated Viewer bundle from an explicitly selected path, with manifest/card/sidecar hash equality and no implicit “latest” lookup.

## Data tests

Validate JSON, JSONL, CSV and Parquet against their shared canonical values. Treat Markdown as a rendering: test required displayed values, provenance display, renderer behaviour and absence of raw vectors rather than attempting Markdown round trips. Validate per-subject retrieval, stable URLs, coverage/capability metadata, taxonomy artefacts and release discovery.

For an ownership repair/import, validate the source manifest hashes, entity count, card IDs, source-native records, taxonomy and selected financial fixture values before and after import. An archival import must not rewrite RC4 semantics.

For the proposed v0.5 contract, parse every draft schema and validate EJA, sparse, identity-binding and multiple-financial-period examples. Fixture tests must additionally assert reference resolution, version agreement, coverage-state invariants, source-row label/order/sign preservation, financial-pointer coherence, direct-versus-derived separation, public/private exclusion and participation action/evidence separation. These are design-fixture tests until approved Builder validators exist.

## Builder tests

Test opaque identity creation and external identifier/relationship handling; source parsing; archive/runtime/staging separation; evidence and provenance resolution; fundraising ladder branches; taxonomy validation; fresh isolated staging; allowlist enforcement; manifest generation; incremental invalidation; source drift; and error isolation.

## Reality-spike fixtures

Maintain small sanitised or permitted fixtures from awkward real-world cases: multiple names/identifiers, funds and branches, renamed/deregistered subjects, dead websites, scanned PDFs, separate reports, thin records, unusual accounting and no fundraising disclosure. Current retained regressions include Merri Creek's nine-month reporting transition, Fitted for Work related-record ambiguity and Red Cross non-comparable report/AIS revenue observations. These cases are regression tests for the evolving model, not a frozen schema proof.

## LLM evaluation

Maintain a human-reviewed evaluation set for neutrality, factual grounding, PR-language suppression, activity/beneficiary/geography extraction, taxonomy assignment, uncertainty, attribution, conflicting evidence and financial/fundraising interpretation. Run it for material model or prompt changes; valid JSON alone is not a quality signal.

For the RC4→0.5 migration, gate promotion on a complete-card schema run, public source-reference resolution, manifest hash verification and a losslessness audit that counts each source domain as either canonical or `legacy_unbound`. Test exact recovery only for a unique literal public source-field match, require the origin-card hash on retained legacy material, and ensure legacy preservation never upgrades capability coverage to `observed`.

Phase 2A adds a private 30-case representative evaluation corpus, weighted toward sparse/failed websites and report-bearing subjects. It records source evidence IDs, model/prompt/evidence hashes, review focus and a reviewer-assessment slot; it is the regression basis for later prompt/model changes.

Phase 2A.1 adds corpus-level assertions for one effective public coverage state per capability, no public operational synthesis telemetry, no blanket CauseBase taxonomy evidence IDs, sparse-evidence wording and broken public evidence URLs. Viewer tests cover unavailable/real fundraising estimates, observation currency, conflicting financial values and friendly taxonomy separation.

## Taxonomy-review tests

Taxonomy review must preserve the frozen baseline and never mutate canonical taxonomy files or card classifications. Test deterministic corpus diagnostics and stable input hashes; exclude ACNC classification fields, current CauseBase assignments, taxonomy labels and organisation names from taxonomy-blind Pass A; validate proposal operation types, compact review limits, support-count/representative-ID bounds and proposed-term definition profiles; retain future unmapped-concept and taxonomy-ambiguity signals privately; and ensure ACNC comparison occurs only after independent discovery.

For the durable workflow, separately test that PREPARE is API-free and bounded, MODEL-REVIEW cannot create a decision record, decision outcomes validate against the governed schema, and VALIDATE reports candidate impacts without changing cards, taxonomy files or public releases.

## Viewer tests

Test static data loading with optional-artifact failure, retrieval/search/filter semantics, deep links, exact card fidelity, estimate/provenance visibility, correction context, safe URL/text rendering, keyboard and mobile behaviour, and absence of recommendation framing.

Phase 2B additionally tests stacked facets, clickable taxonomy navigation, source-record links, funding/fundraising display, history/reuse display and accessible help controls.

## Post-RC4 evaluation and distribution tests

The golden corpus must contain governed representative and awkward cases for source-native financial preservation, reports/charts/scans, identity/group ambiguity, thin or failed websites, coverage states, derived projections and editorial/provenance review. It is the shared benchmark for document-stack, website-pipeline and Viewer changes; quality/cost evidence from it gates technology selection and scale.

Golden Corpus v1 tests validate the checked-in manifest's schema/version, unique case IDs, truth-level separation and SHA-256-bound private fixture locators. Builder evaluation tests require a stable normalised document result contract, cache-key invalidation when extraction options change, explicit unavailable OCR/vision routes rather than silent fallback, and deterministic benchmark report generation. The ecosystem bake-off must use distinct screened components, output-only financial gold comparison and computed hard-gate status: EJA P&L 33/33 and financial position 32/32 require exact labels, order, values, comparatives, signs and hierarchy; OCR requires a genuine low-text page; visual requires EJA 4/4 label/value association. Benchmark acceptance separately records elapsed time, platform availability and skipped private fixtures; review-required cases remain diagnostics and cannot be silently promoted to gold.

Evidence Engine tests require bounded same-origin discovery, explicit snapshot/fetch failure records, stable/transient page classes, content hash and selector provenance, and review-only source-observation candidates. Potential action links must not become action URLs automatically. Identity tests forbid name-only/domain-only resolution and subject minting. Fundraising review tests preserve direct-source, unavailable and additivity-blocked states without calculating an estimate. Integrated-pilot tests require all applicable document cases to complete explicitly while web scope remains bounded.

Consumer-LLM testing uses scarce genuinely naive contexts deliberately. Prepare canonical prompts and scoring criteria before use, and record model/product, date, account/context condition, exact prompt, web/search availability, selected sources, organisations returned, factual errors, citations and whether CauseBase changed the result. Test four conditions separately: unaided discovery (no CauseBase mention), source discovery, directed CauseBase use and interpretation of supplied CauseBase records/URLs. Eventual routine model familiarity/indexing is product success, not permanent contamination.

The executable initial prompt set is `golden/distribution-evaluation-v1.json` (16 cases). Static distribution tests build from the pinned release and verify direct card routes, canonical metadata, JSON/Markdown alternates, source-record links, sitemap, robots and current-release discovery. Wikimedia tests are identifier-first and must retain unmatched/ambiguous cases rather than falling back to names.

Knowledge Validation v1 adds deterministic review-sample selection, review-decision schema validation, exact excerpt/source-hash resolution, a prohibition on model output becoming human gold, domain-specific (not aggregate) automation policy, taxonomy-blind PREPARE input, historical-pressure comparison recording, fundraising additivity blocks, consumer answer-key criteria and explicit `AUTOMATED PROXY` labelling. Static-agent regressions must preserve enough linked v0.5 evidence to distinguish EJA's direct fundraising share from mechanical implications, APNIC period state, sparse coverage, DFWA/identity ambiguity and `legacy_unbound` material.

The approved next design adds documentation-level tests for: no fundraising
prior or peer-imputation fallback; separate Ethos and service-orientation
semantics; neutral `notable_context` naming; fundraising source-role and
provider/campaign attribution; industry-source absence not becoming a negative
claim; and review-only status for all industry-derived candidates. The generic
schema derivation vocabulary may retain `peer_imputation` only as an unused,
future-domain option; it must not be reachable by fundraising expenditure.

Machine-distribution acceptance includes corpus-level discoverability, crawlable semantic HTML, stable canonical URLs, per-card JSON/Markdown, manifests, taxonomy/geography semantics, direct-versus-derived and period/scope fields, provenance, coverage/absence and freshness/version. A key acceptance question is whether a general-purpose consumer AI can discover relevant CauseBase records and accurately answer a realistic funder question.

Viewer human design acceptance includes the anti-marketplace test: does the interface appear to persuade a user to favour, trust or donate to an organisation? If yes, it fails. Test accessibility, density, speed and inspectability alongside this qualitative criterion.
