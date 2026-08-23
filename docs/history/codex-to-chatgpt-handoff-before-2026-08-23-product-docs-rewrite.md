# Historical snapshot — superseded 2026-08-23

**Status:** Historical reference only; not current executable instruction.  
**Current authority:** [DOCUMENT_AUTHORITY.md](../../DOCUMENT_AUTHORITY.md)

---

# CharityGraph — Codex to ChatGPT Handoff

> Migration status: current work uses CharityGraph. References to CauseBase in retained handoff history identify the former working name or immutable legacy material only.

## Current handoff — read this first (2026-08-15)

- The live Viewer release is `v0.5.0-2026-08-15` (Viewer commit `c1fc831`), with 120 cards. GitHub Actions run `31856788408` passed its Viewer tests, selected the immutable Data release and deployed to `gh-pages`; the public site returned HTTP 200.
- RC4 completed source-native financial-statement preservation, selective visual allocation extraction and the narrow Funding & fundraising projection. EJA's Donations, gifts & bequests projection is AUD 2,101,817 / 41.9% of total income, using only `Donations, Fundraisings, Lectures` and `Donations - Future Fund`; Fundraising is direct 10% of expenditure with an approximate AUD 585k implication.
- The public-contract decision gate is closed in `PUBLIC_CONTRACT_CONSOLIDATION_PROPOSAL.md`: claim basis/extraction separation, capability coverage semantics, financial signs, source-payload policy, extensible capabilities, current-financial pointers, identity continuity, sparse summaries and derivative lineage are approved direction.
- Public contract `0.5` is implemented: `PUBLIC_SCHEMA_VNEXT_SPEC.md` defines the object/release/observation/financial/coverage/privacy contract; `RC4_TO_VNEXT_COMPATIBILITY.md` records the completed RC4 migration; `schemas/vnext/` and `examples/vnext/` provide the release-owned capability registry and frozen cases. Builder’s `causebase_builder.v05` supplies the deterministic adapter, release assembly and validators; Viewer derives its browser index from the selected Data release.
- Gate A is passed: immutable `releases/v0.5.0-2026-08-15` has 120 v0.5 cards, 228 public source sidecars, 349 manifest artefacts and passing schema, source-reference, losslessness and manifest-hash checks. It recovers only 20 uniquely matching geography values; it preserves all other unresolved material in public `legacy_unbound` with an RC4-card SHA-256. This includes 402 activities, 226 beneficiaries, 198 geography values, 573 classifications, one funding-source record, five fundraising-method records and 86 historical AIS records whose evidence IDs have no immutable RC4 sidecar. Legacy material does not make a capability observed. See `MIGRATION_V05_AUDIT.md`.
- The Viewer v0.5 gate is also green and deployed: its generated browser index is derived directly from the selected Data release, all Viewer tests pass and all 228 source-record links resolve in the static bundle. The workflow explicitly checks out CauseBase Data and selects `v0.5.0-2026-08-15`.
- Golden Corpus v1 is a 21-case governed manifest (seven hard-gold, fourteen review-required) without PDFs or private extraction outputs. The superseding six-component local ecosystem bake-off selected Document Pipeline v2.3: `pdfplumber` passes EJA P&L 33/33 and financial position 32/32 with source labels, values, comparatives, signs, order and hierarchy; local Tesseract recovers genuine low-text pages; and local vector colour/geometry passes EJA’s 4/4 page-29 chart association with legend/value bounding boxes. PyMuPDF is not adopted because of AGPL/commercial licensing; Docling remains excluded in this OneDrive path because of Windows path length. The computed Document Gate is **DECISIVE**. See DOCUMENT_EXTRACTION_ECOSYSTEM_REVIEW.md and DOCUMENT_EXTRACTION_STACK_DECISION.md.
- The first bounded Evidence Engine v1 pilot is complete. It used retained private snapshots only for twelve selected website subjects, completed Document Pipeline v2.3 across all seven retained PDFs, and exercised all 21 Golden cases for identity and fundraising review. It produced 102 review-only web candidates with source selectors and freshness metadata; did not mint any subject; retained identity ambiguity for review; kept fundraising overlap additivity-blocked; and wrote no cards. See EVIDENCE_ENGINE_PILOT.md.
- The technology spikes are closed: retain the dependency-free static Viewer (no framework migration); defer broad Wikimedia ingestion after a 120-subject ABN-first Wikidata test found only 7 exact matches and 2 English-Wikipedia links. Wikimedia may later be an attributed discovery/corroboration source, never identity authority.
- Machine distribution was **RED** before remediation: robots blocked indexing and hash-only, JavaScript-rendered cards had no crawlable direct route. The validated static-discovery build emits canonical `/charity/<causebase_id>/` pages, JSON/Markdown alternates, source links, sitemap, permissive robots and a current-release pointer from the same pinned immutable v0.5 Data release. Consumer-LLM protocol exists; no project-aware session is represented as a naive consumer test. See AGENT_DATA_DISTRIBUTION_CONTRACT.md and CONSUMER_LLM_EVALUATION.md.
- Viewer commit `f198335` deployed the discovery layer in successful workflow run `31862499938`. Live direct HTML, current-release, sitemap, robots, JSON and Markdown endpoints return HTTP 200 (the original unversioned Markdown URL may be briefly CDN-cached after deployment; the deployed branch and versioned URL verify the artefact). Data release `v0.5.0-2026-08-15` remains unchanged.
- Knowledge Validation v1 minimum gate is complete: 22 approved human decisions were validated/scored; no domain is auto-promotable and the remaining 26 stratified cases are deferred. The active next phase is the private/review-only Semantic Enrichment Benchmark v1 (Steps 1–2 deterministic scaffold and fundraising-industry source arm); no public semantic release, schema change, corpus rebuild or Viewer change is authorised. See `SEMANTIC_ENRICHMENT_BENCHMARK_V1_IMPLEMENTATION_v2.md`.

# Historical and superseded handoffs — evidence only

All sections below record prior candidates, releases and decisions. They are not current instructions: do not execute their deployment, approval, human-gate or “next increment” language. The current handoff above is authoritative.

**Historical handoff snapshot:** Updated: 2026-08-10 — Phase 1 complete

## Historical — Phase 2B RC2 human-review remediation (candidate; not deployed)

- Candidate: `phase2b-2026-08-12-rc2`, with the existing 120-card corpus only. Failed `phase2b-2026-08-12-rc1` is retained under Viewer `public/releases/`; h1 remains retained there too.
- Editorial migration: all 120 summaries regenerated with `gpt-5-mini`, prompt `phase2b-rc2-1`, editorial policy `0.3-rc2`, and citation-ID output. Private cache telemetry: 327,726 input tokens, 222,747 output tokens, estimated USD 0.527423. Summary validity now treats evidence hash, prompt, editorial policy and output contract as governing inputs.
- Viewer: fixed verified Google Forms entry IDs and `usp=pp_url`; card-wide stable `[n]` reference links; independently scrollable result and inspector panes; URL-persisted search/facets/selection; ABN, ACNC search-profile, website, JSON, Markdown and source-native links; always-visible Funding & fundraising states; controlled geography; CauseBase dimensions separated from ACNC classifications.
- EJA golden card (`cb_604da7f26c6c48dd934e713edc493e9f`): natural reader-first summary with references; ABN and ACNC public links; Australia/Victoria navigation projection; source-native ACNC and AIS records; explicit funding-source `not_available_from_source` and fundraising-method `not_yet_processed` states. It does not merge EJA with Environmental Defenders Office.
- Validation complete: Builder 55 tests; Viewer 11 tests; RC2 publication validation; static deployment-bundle preparation.
- **Historical former release gate (superseded):** deploy the candidate through the then-existing validated manual workflow, then in a clean/incognito browser open EJA and use **Suggest correction**. Confirm the Form visibly contains the organisation, `cb_604da7f26c6c48dd934e713edc493e9f`, `phase2b-2026-08-12-rc2`, the exact card URL, `causebase_summary`, and the displayed summary. Also confirm the selected card remains visible while scrolling the left result list. Do not treat this as a current deployment instruction.

## Historical — Phase 2A completion handoff

## Historical — Phase 2A.1 human-test hardening (candidate, not yet deployed)

## Historical — Taxonomy Review v0.1 (private decision package; no taxonomy change applied)

- Baseline reviewed: `0.1-phase2a`, frozen at 7 dimensions and 23 terms. The review never mutates canonical taxonomy files, existing card classifications or Viewer data.
- First review used the 120-card `phase2a-2026-08-10-h1` candidate. Taxonomy-blind Pass A excluded ACNC classifications/labels/mappings/cohort strata, current CauseBase assignments and organisation names. Pass B received the baseline only after independent discovery; ACNC comparison is post-hoc only.
- Private package: 8 unapproved proposals (4 HIGH, 3 MEDIUM, 1 WATCH), a complete 23-term audit, deterministic frequency/co-occurrence/coverage diagnostics, definition and boundary profiles, migration analysis, and private API telemetry. The strongest diagnostics include `geography.local_or_regional` at high frequency and major co-occurrences for local geography/organisation, events/public-events and volunteer approach/participation.
- At that time, human taxonomy governance was required for every HIGH proposal: approve, reject, defer/watch, request more evidence or modify. Any accepted material change would have required a new taxonomy version and explicitly governed affected-card reclassification; proposals were not applied automatically.

- Historical deployed release remains `phase2a-2026-08-10`; hardening candidate is `phase2a-2026-08-10-h1`.
- Fixed 86 duplicate coverage-capability presentations, blanket CauseBase-classification provenance, public OpenAI operational telemetry, sparse ACNC-classification-exclusion wording, currency-hardcoded financial display, misleading enriched badge and merged taxonomy headings.
- Nine sparse/negative-wording cards were rerun with `gpt-5-mini` prompt `phase2a-0.5`: 12,500 input tokens, 9,556 output tokens, approximately USD 0.022 estimated synthesis cost. Nine changed embedding inputs were regenerated (1,386 input tokens); 111 vectors were reused.
- New candidate diagnostics are clean for the targeted defects; 31 cards have no neighbour above the conservative threshold, which is retained as an honest semantic-coverage state rather than padded with weak links.
- Private 30-case local review pack is ready. Google Forms intake is configured with supplied responder endpoint and six contextual prefill fields; the form owner confirmed private/reviewer handling. Human-test deployment is live at `https://gregorycwhill.github.io/CauseBase-Viewer/`: dataset `phase2a-2026-08-10-h1`, Viewer commit `a97b99951915a3c92a03da48352f94ad727db511`.

- A validated 120-card governed enriched corpus candidate is staged in CauseBase Viewer. Each automatically promoted ACNC-authoritative subject has opaque CauseBase identity, valid ABN/source provenance and `subject_kind: unknown`; no group, legal-entity or brand inference was made.
- Evidence: 82 observed websites; explicit failure/not-available coverage otherwise; five annual-report PDFs privately page-extracted (180 pages) with one acquisition failure retained. Reports, HTML snapshots, prompts and credentials are not public.
- Synthesis: `gpt-5-mini-2025-08-07`, `phase2a-0.4`, content-addressed evidence cache and full provenance. Final summaries are 82–192 words (median 159); 78 are 150–220 words and eight remain short because selected evidence is sparse.
- Taxonomy v0 implements cause/problem, beneficiary, activity, approach, participation, geography and organisational-character dimensions. ACNC labels remain attributed external classifications and are excluded from native taxonomy inference and semantic text.
- Embeddings: `text-embedding-3-small`, 120 cards and 162 thresholded descriptive neighbours; never recommendation framing. No universal fundraising fallback was introduced; unavailable estimates remain explicit.
- The approved design consolidation is recorded in `DESIGN_CONSOLIDATION_DECISIONS.md`. It separates Ethos from `service_or_mission_orientation`, uses `notable_context` for neutral contextual observations, forbids fundraising expenditure priors and peer-imputation fills, and approves fundraising-industry sources only as a bounded review-only experimental category. The four supporting designs and industry-source design are now copied verbatim into CauseBase Data. This does not change v0.5, public schemas, Viewer or corpus scope.
- Evaluation: private `phase2a-eval-0.1` has 30 representative cases, including report and website-failure cases, ready for human reviewer assessment.
- Viewer: generated cards, taxonomy, coverage, agent guide and semantic artefacts validate cleanly. Correction links support a configurable external intake with documented prefill fields; no live endpoint/form is configured.
- Validation: Builder 42 passing tests; Viewer 3 passing tests; 120-card public candidate has zero allowlist/manifest/representation validation errors.
- **Historical former next vertical increment (superseded):** complete human evaluation-rubric assessments, broaden report-page discovery, and configure the external correction endpoint before treating the release as operationally mature.

## Historical — Phase 1 completion record

- Built a reproducible national structured backbone from current ACNC Register, ACNC AIS and ABR/DGR sources.
- Archived source files privately with retrieval metadata, hashes, URLs, publisher and licence records.
- Normalised source records privately with stable source-record IDs independent of CauseBase subjects.
- Produced a validated safe staging candidate containing only public registry entries, aggregate coverage metadata, schema and manifest.

## Historical — national corpus statistics

- ACNC Register: 65,472 records / 65,472 ABNs.
- AIS: 53,465 financial observations / 53,465 ABNs.
- DGR: 31,593 observations from the dated 2026-08-05 ABR bulk extract, plus two independently retained ABN Lookup checks.
- Registry: 5 durable promoted subjects.

## Historical — identity/resolution findings

- 5 ACNC records bind to existing reviewed registry promotions; 65,467 remain `candidate` with no subject promotion.
- National normalisation performs only authoritative ABN joins between source records. It does not use name similarity to resolve a subject.
- The Salvation Army and Royal Flying Doctor Service remain recorded multiplicity examples; no automatic group aggregation was introduced.

## Historical — AIS/financial findings

- 44,699 reporting periods are approximately annual; 573 are nonstandard; 8,193 lack usable report dates.
- Consolidation values: 1,249 true, 11,719 false, 40,497 unknown.
- 50,403 AIS records join an ACNC register ABN; 3,062 do not. This remains source coverage, not a negative claim.
- Money uses exact decimal source and normalised values. No precedence/reconciliation scalar is derived nationally.

## Historical — DGR findings

- Current ABR source is retained as two private bulk archives with SHA-256 hashes and CC BY 3.0 Australia metadata.
- DGR is a dated external tax-status observation, never CauseBase identity.
- Absence is meaningful only relative to this dated complete bulk extract; no general negative claim is inferred.

## Historical — coverage/provenance findings

- Private diagnostics include source counts, identifiers, coverage, period/consolidation distributions, duplicate patterns, parser failures, drift baseline and major identity multiplicity examples.
- Raw source archives and private normalised source records are excluded from staging and Git publication boundaries.

## Historical — tests/validation

- Builder: 36 tests passing.
- Viewer: 3 tests passing.
- `phase1-structured-backbone` staging candidate structural validation passed.

## Historical — decisions made locally

- Used a compact safe public projection rather than publishing regulator rows or raw archives.
- Used a full dated ABR bulk pass to make national DGR coverage semantics defensible.
- Kept first-baseline source drift as `not_assessed`; meaningful drift requires a subsequent refresh.

## Historical — questions requiring product decision

None. The remaining work is operational refresh/release design and enrichment scope under the accepted product direction.

## Historical — known limitations

- ACNC/AIS source dates are current baseline acquisitions, not a scheduled refresh service.
- No public national card corpus is implied by the backbone; only five reviewed subjects are promoted.
- DGR parser currently records endorsed presence; richer fund/item/date field mapping can be added without changing identity semantics.

## Historical — taxonomy workflow handoff

This historical workflow began with Builder `taxonomy-review-prepare`, not a model call. Its private packet was the human discussion input; optional advisory model output remained separate. The historical v0.1 or Sol packages were not to be altered, and candidate taxonomy implementation required an explicit human decision record followed by `taxonomy-review-validate` before any reclassification/rebuild decision.

## Historical — former recommended Phase 2 increment (superseded)

Build a governed real enriched slice (roughly 100–1,000 subjects) using targeted report and website evidence, taxonomy work, real embeddings and correction intake, while retaining this backbone as the source/coverage layer.
