# CharityGraph Implementation Plan

**Status:** Active implementation sequence  
**Version:** 1.0-draft  
**Updated:** 2026-08-23

## 1. Scope

This plan implements the approved product contract through Builder vNext while protecting the current public 0.5 release. It does not authorise a new public schema or corpus rebuild.

Each step is a bounded PR with its own tests, migration note and explicit exclusions. Architecture-critical PRs use Terra-High. Luna-High is appropriate for mechanical work after contracts are fixed.

## 2. PR 1 — documentation authority and architecture skeleton

**Model:** Terra-High

Deliver:

- rewritten active product documents;
- `DOCUMENT_AUTHORITY.md`;
- reclassification of public contract 0.5;
- approved Builder architecture amendments;
- aligned Builder/Data agent instructions;
- package/module boundary stubs and no-op CLI commands where useful.

Do not:

- create the runtime database;
- move or rewrite archives;
- call a model;
- change public schemas or releases;
- change Viewer behaviour.

Validate:

- active-document authority and link checks;
- zero active former-brand terminology;
- Builder 119-test baseline;
- Viewer 21-test baseline where touched by shared links only;
- Data schemas/examples;
- immutable checksum.

## 3. PR 2 — typed internal contracts

**Model:** Terra-High

Implement schema contracts for:

- `SubjectRecord` and lifecycle;
- `SourceBlob` and `SourceRecord`;
- `SubjectBinding`;
- `EvidenceFragment`;
- `CandidateObservation`;
- `DecisionRecord`;
- typed `CanonicalObservation` payloads;
- `CoverageAssessment`;
- `DerivativeArtifact`;
- `TaskRun`, `RunManifest` and `ReleaseProjection`;
- artefact lineage and separate subject relationships.

Add typed IDs, schema versions, canonical serialisation and hashing. Do not ingest real archives.

## 4. PR 3 — SQLite catalogue and recovery

**Model:** Terra-High

Implement SQLite behind a narrow interface for:

- artefact locations and hashes;
- dependency edges;
- task/run states;
- source refresh checks;
- retries and terminal failures;
- locks/leases;
- cache validity;
- schema migrations.

Specify idempotency keys and transaction boundaries. Add a deterministic reindex path from durable artefacts. Prove that deleting the database loses no governed evidence.

Runtime path is configurable and defaults under `C:\CharityGraph-runtime\state`, never OneDrive.

## 5. PR 4 — read-only archive indexer

**Model:** Terra-High

Index existing files in place. Record hash, media/schema type, source family, known subject/run association, migration status and privacy class.

Do not move, rename, edit or auto-promote evidence. Produce durable reports under the workspace archaeology directory, never Temp.

## 6. PR 5 — deterministic authoritative-source slice

**Model:** Terra-High

Run one structured source through plan, acquire/import, parse, bind, evidence, candidate, policy/fixture decision, canonicalise, coverage, derive and project.

Include when present:

- identity and source-native classifications;
- registration or DGR status;
- program records;
- participation records;
- financial/source-native rows.

Project through the 0.5 compatibility adapter into fixtures only. Classify every difference.

## 7. PR 6 — program, participation and scope

**Model:** Terra-High for design; Luna-High for mechanical fixtures after approval

- Implement organisation/program/service/unit scope.
- Populate existing participation and opportunity schemas.
- Separate stable modes from transient opportunities.
- Add role-specific geography and action/evidence URL rules.
- Add nested-to-durable subject promotion tests without enabling automatic promotion.

## 8. PR 7 — document and website evidence

**Model:** Luna-High for adapters; Terra-High for ambiguous semantic boundaries

- Reuse validated digital-text, OCR and visual extraction routes.
- Reuse bounded website acquisition and freshness rules.
- Create page/region/selector evidence fragments.
- Generate reviewable candidates for activities, beneficiaries, programs, participation and geography.
- Persist failures and assessment scope.

No whole-card prompt and no public promotion.

## 9. PR 8 — fundraising and shadow-registry sources

**Model:** Terra-High

- Implement funding source, standing practice, campaign and expenditure payloads.
- Implement source-role policies for evaluated shadow registries.
- Add source-led enumeration adapters for already approved sources.
- Preserve registry-defined authority and subject-binding requirements.
- Add campaign metrics without financial reconciliation or ROI calculations.
- Route promotional/provider claims through appropriate review.

## 10. PR 9 — governance and corrections

**Model:** Terra-High

- Implement decision dispositions, authority, rationale, applicability and supersession.
- Add private correction submission and governed proposal records.
- Add challenge, retraction and dependent invalidation.
- Produce bounded review packets.
- Add expedited sensitive-context re-review.

## 11. PR 10 — semantic domains and taxonomy artefacts

**Model:** Terra-High

- Port ACNC external classifications as source-native schemes.
- Port the native seven-dimension taxonomy as a governed seed, not old assignments.
- Add taxonomy, term, classification and crosswalk artefacts.
- Add cause centrality.
- Add ethos and separate service/mission orientation.
- Add `notable_context` categories and risk policy.
- Keep descriptors and campaign vocabularies provisional until evaluated.

## 12. PR 11 — task runner and model boundary

**Model:** Terra-High

- Implement task-specific local/remote model clients.
- Add schema validation, cache identity, budgets, telemetry, retries and fakes.
- Keep model outputs as candidates/derivatives.
- Allow bundled physical calls only under an approved benchmarked policy.

## 13. PR 12 — historical evidence import

**Model:** Luna-High after mapping rules are fixed

- Import historical model runs, governed decisions and unbound migration ledgers.
- Preserve exact origin hashes and statuses.
- Do not auto-promote old classifications or semantic fields.
- Create a review/re-extraction priority ledger.

## 14. PR 13 — controlled comparison pilot

**Model:** Terra-High

Run the shared stratified benchmark across product domains. Produce source-opportunity, proposition/review and cost ledgers. Compare deterministic, economical-model, escalation, oracle and human conditions.

No production automation policy is approved by an aggregate score. Decisions are domain-specific.

## 15. PR 14 — cutover and public-contract proposal

Only after the controlled pilot:

- propose production command surfaces;
- propose deprecation of phase orchestration;
- propose any future public contract separately;
- provide migration fixtures and Viewer implications;
- retain the previous valid release.

## 16. Cross-cutting constraints

- No active former-brand terminology outside isolated compatibility/historical material.
- No raw/private evidence, credentials, prompts, runtime state or debug material in Git.
- No archive mutation without a separately approved migration plan and hash verification.
- No public release mutation in place.
- No unsupported negative claims or forced semantic values.
- No recommendation, ranking, mandate decision or fundraising-performance inference.

