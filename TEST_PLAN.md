# CharityGraph Test Plan

**Status:** Canonical verification strategy  
**Version:** 1.0-draft  
**Updated:** 2026-08-23

## 1. Purpose

Testing must establish more than valid JSON. It must prove identity integrity, evidentiary lineage, semantic restraint, publication safety, reproducibility, recovery and cross-channel consistency.

The current protected baseline is:

- Builder: 119 tests passed;
- focused Builder smoke: 12 passed;
- legacy compatibility: 2 passed;
- Viewer: 21 passed;
- Data schema/example validation: passed;
- immutable 0.5 checksum: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

## 2. Test levels

- unit tests for identifiers, hashing, schemas, parsing and policy rules;
- contract tests across internal records and public projections;
- fixture-based vertical slices;
- migration and regression tests against immutable 0.5;
- benchmark/evaluation tests against governed cases;
- publication and distribution acceptance;
- selected human review where product semantics cannot be safely automated.

National raw sources and private archives are not required for routine CI.

## 3. Documentation and authority tests

- active documents declare status, version/date and scope;
- authority links resolve;
- superseded material is not presented as current instruction;
- active product and agent-instruction files contain no former-brand terminology;
- public 0.5 material is labelled implemented compatibility, not future design;
- Builder architecture and product documents agree that observations are internal authority and cards are projections.

## 4. Subject identity and scope

Test:

- stable opaque `subject_id` generation and persistence;
- no identity from name/domain alone;
- source-record identity independent of subject identity;
- binding states: resolved, candidate, ambiguous and unresolved;
- conflict and review metadata;
- subject lifecycle, merge/split/successor/tombstone semantics;
- program/service/unit local scope;
- governed nested-to-durable promotion;
- separation of subject relationships from artefact lineage;
- no parent/network attribute transfer without scoped evidence.

## 5. Artefact and lineage contracts

Every persisted artefact validates its type, schema version, ID, canonical hash, creation provenance and typed input/output edges.

Test that:

- shared subject association never becomes causal lineage;
- candidates cannot appear as canonical observations without a decision;
- model output cannot become a human decision;
- supersession preserves history;
- invalidation reaches dependent coverage, derivatives and release projections;
- filenames are never treated as identity.

## 6. SQLite and operations

Test:

- clean migration from every supported catalogue version;
- constraints and uniqueness rules;
- deterministic idempotency keys;
- transaction rollback after injected failure;
- single-writer assumptions and bounded worker behaviour;
- retry/backoff and terminal failure;
- lock/lease expiry and process-death recovery;
- sliced run resume;
- held/quarantined case handling;
- deterministic reindex from durable artefacts;
- complete evidence recovery after database deletion;
- no governed fact exists only in SQLite;
- scale/throughput on representative national-index metadata.

## 7. Source acquisition and parsing

- status, media type and size validation before durable placement;
- completed-byte hashing;
- URL sanitisation and no credential/query leakage;
- source version, retrieval, licence and attribution metadata;
- exact structured-field preservation;
- document page/region, table labels, order, units and signs;
- bounded website routes, freshness and failure states;
- explicit unavailable OCR/vision routes rather than silent fallback;
- no archive mutation by index/import operations.

## 8. Source authority and shadow registries

Test claim-specific policies:

- evaluated registry membership/status, fee/code applicability and dates may be direct authoritative candidates;
- registry code applicability does not imply compliance;
- fee/levy rule does not imply member-specific amount or volume;
- source-led enumeration does not bypass subject binding;
- vendor or award material can establish a named campaign/event/relationship only within its source role;
- promotional ROI, uplift, conversion, retention and effectiveness do not become canonical performance observations;
- source rights and public-projection policy are enforced by source family.

## 9. Common observation semantics

Validate:

- claim basis independently from extraction method;
- source/evidence references;
- subject and explicit scope;
- event/effective, reporting, observed, assessed, generated and release time;
- qualification, warnings and confidence;
- derivation metadata for non-direct observations;
- contradictory observations retained with reconciliation status;
- no empty-list negative inference.

## 10. Coverage

- exactly one current assessment per applicable capability and policy context;
- allowed coverage states validate;
- `not_found_in_source` requires `assessment_scope`;
- assessment scope records relevant source families/roles, periods and policy version;
- unknown, not processed, failed, unavailable and stale remain distinct;
- coverage never upgrades merely because historical material was preserved;
- public projection is compact and private telemetry remains private.

## 11. Domain tests

### Activities, beneficiaries and programs

- observable activity differs from mission rhetoric;
- beneficiary differs from audience, supporter or incidental person;
- programs/services retain source-local identity, status, dates and scope;
- name similarity cannot promote a program to subject;
- program geography does not become organisation-wide geography automatically.

### Participation and opportunities

- initial structured and web/document slices attempt participation extraction;
- stable participation modes remain separate from opportunities;
- modes, labels, status and action URLs validate;
- action URLs differ from evidence URLs;
- transient opportunities carry effective dates, first/last observation and freshness;
- closed/stale opportunities do not render as current;
- absence after assessed sources is expressed through coverage, not “no opportunities”.

### Geography

- source-faithful descriptive geography and controlled navigation terms remain separate;
- geography role distinguishes registration, office, service delivery, beneficiary, impact, fundraising and program/appeal scope;
- granularity and confidence are preserved;
- global-parent geography does not transfer to an Australian subject.

### Funding and fundraising

- funding source, practice, campaign and expenditure never collapse;
- practice kinds distinguish channel, program, mechanism and partnership;
- campaign type, mechanics and channels are orthogonal;
- reported target/raised/spent/count metrics retain source wording, period and scope;
- campaign values do not silently reconcile to accounts;
- no ROI, cost-to-raise, acquisition efficiency or causal attribution is produced;
- expenditure ladder permits null and prohibits universal prior, peer fill, forced point and automatic midpoint;
- component additivity and double-counting blocks operate.

### Ethos and service orientation

- organisational ethos cannot be inferred from beneficiaries, names, images or model impression;
- roles distinguish self-description, formal affiliation, external description and history;
- service/mission orientation is separate;
- parent/network ethos does not transfer without evidence;
- absence does not imply secular or unaffiliated;
- first-pilot publication requires human review.

### Notable context

- category is contextual, never a score or polarity;
- procedural statuses remain distinct;
- Australian subject and global parent/network scope remain distinct;
- absence from Wikipedia has no meaning;
- revision/discovery lineage is retained;
- sensitive/adverse observations require adequate underlying evidence and human review;
- correction challenges trigger expedited re-review.

## 12. Taxonomy tests

- ACNC source-native schemes remain separate from CharityGraph-native assignments;
- classifications identify taxonomy, version, term, scope, method and evidence;
- native v0 terms are migration seeds, not automatic current assignments;
- invalid term IDs and versions fail;
- no invented model terms enter canonical output;
- unmapped concepts and ambiguity remain private maintenance signals;
- taxonomy changes produce a new version and migration analysis;
- crosswalks have independent provenance;
- cause centrality remains separate from taxonomy adjacency.

## 13. Corrections and decisions

- raw submissions remain private;
- moderated proposals receive stable IDs and target subject/assertion/release;
- decision authority, rationale, time and applicability validate;
- accepted corrections regenerate dependent observations, summaries, classifications, embeddings and release projections;
- rejection does not erase the proposal history where public retention is appropriate;
- retraction and exceptional privacy/legal removal follow separate policies.

## 14. Model-task tests

- task types have separate schemas and cache identities;
- exact inputs, prompt/policy, model snapshot and local-tool versions are material to cache identity;
- output schema and evidence-span validation;
- token/cost/latency budgets and safe retries;
- fake clients in CI;
- no raw prompts/responses or spend telemetry in public candidates;
- editorial synthesis consumes governed observations only and cannot create new facts;
- bundled calls retain separate logical outputs, validation and lineage.

## 15. Evaluation and economics

The shared benchmark stratifies size, source richness and complexity. It covers activities/beneficiaries, programs, participation, geography, fundraising, ethos, service orientation and notable context.

Validate benchmark/cohort identity, source opportunity, proposition/review and cost ledgers. Measure domain-level precision, recoverable recall, oracle gap, source-scope gap, public-evidence sparsity, review burden, accepted observations per dollar and refresh cost.

No aggregate score authorises automation across domains. Test that every eligible subject receives the cheap common baseline and extra compute is not allocated by worthiness proxies.

## 16. Public release gates

A release candidate must pass:

- schemas and referential integrity;
- identity and domain invariants;
- capability/assessment-scope completeness;
- taxonomy and crosswalk validity;
- provenance and derivative lineage;
- public allowlist and privacy scan;
- source-family rights policy;
- cross-representation consistency;
- drift/anomaly checks;
- manifest/hash verification;
- previous-valid-release preservation.

Raw reports, scraped pages, prompts, private corrections, databases, caches, credentials, logs and debug dumps must not appear.

## 17. Distribution and Viewer

Test:

- current-release discovery;
- stable subject HTML routes;
- per-subject JSON and Markdown alternatives;
- source-record links;
- sitemap and permissive robots policy;
- canonical metadata and citation information;
- bulk artefact/schema discovery;
- consumer-LLM interpretation using genuinely naive contexts;
- Viewer fidelity to the selected Data release;
- accessibility, density, speed and keyboard/mobile behaviour;
- anti-marketplace acceptance.

## 18. Migration and immutable compatibility

- the public 0.5 adapter has frozen fixtures;
- historical differences are classified as input, decision, policy, derivative or defect;
- unresolved historical data is never promoted by mere presence;
- legacy identifiers remain isolated;
- immutable public bytes and checksum remain unchanged before and after every pre-cutover PR.

