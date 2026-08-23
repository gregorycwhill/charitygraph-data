# CharityGraph — Current Handoff

**Status:** Active execution handoff  
**Updated:** 2026-08-23  
**Supersedes:** all earlier current/next-action handoff sections

## 1. Read this first

CharityGraph's public cutover is complete and live. Builder's full regression baseline is green. Read-only archaeology and product/architecture review are complete. SQLite is approved for the local operational catalogue.

The next task is documentation-and-skeleton work only. Do not resume the pre-rearchitecture enrichment sequence.

## 2. Repositories and baseline

- Builder: `https://github.com/gregorycwhill/charitygraph`
- Data: `https://github.com/gregorycwhill/charitygraph-data`
- Viewer: `https://github.com/gregorycwhill/charitygraph-viewer`
- live Viewer: `https://gregorycwhill.github.io/charitygraph-viewer/`

Relevant main commits:

- Builder: `42370a4e1978e2f0dadb9085cfe69536d6fb07d6`
- Data: `00079d069f1ab92d31ebb9acab398d59c9a362d0`
- Viewer: `ffaeaa3f8aed625285fc3c915070bd69a7fe47f4`

Validation baseline:

- Builder full suite: 119 passed;
- focused Builder suite: 12 passed;
- legacy compatibility: 2 passed;
- Viewer: 21 passed;
- Data schema/examples: passed;
- Pages deployment: passed;
- brand lint: passed.

Immutable public 0.5 manifest checksum:

`01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`

## 3. Current product authority

Install and follow:

- `DOCUMENT_AUTHORITY.md`;
- rewritten `PRODUCT.md`;
- rewritten `PRINCIPLES.md`;
- rewritten `PUBLIC_COMMITMENTS.md`;
- rewritten `EXPERIENCES.md`;
- rewritten current state, roadmap, implementation and test plans;
- approved Builder target architecture and product–architecture alignment review.

Key product decisions:

- one-stop shop for structured, governed Australian charity data;
- analyst/consultant as anchor design user;
- organisation, program/service, portfolio and ecosystem scales;
- internal `subject_id` and durable `SubjectRecord`;
- cards as public release projections;
- participation populated from initial production processing;
- evaluated shadow registries as first-class claim-specific sources;
- fundraising split into source, practice, campaign and expenditure;
- ethos separate from service/mission orientation;
- neutral `notable_context`;
- downstream agents apply mandates; CharityGraph supplies adjudicable ingredients.

## 4. Public release protection

Public contract 0.5 is implemented compatibility authority for the immutable current release. It is not the Builder vNext internal model and is not a future-schema proposal.

Do not:

- edit immutable release files;
- rename literal compatibility fields in the release;
- treat unresolved historical material as canonical;
- change Viewer release selection;
- propose a future public schema inside the architecture skeleton PR.

## 5. Evidence archaeology

The durable archive and archaeology findings are migration inputs. Index them in place later; do not reorganise them now.

Known evidence includes:

- 3,977 files / approximately 1.44 GB;
- 2,575 structured artefacts;
- 299 model-run cache records;
- 29 governed/human artefacts;
- 1,491 historical unbound items across 114 subjects.

Old model outputs are candidates, derivatives or benchmark evidence. They are not human decisions and must not be auto-promoted.

## 6. Immediate Codex task

Use Terra-High.

1. Create a branch from current Builder main for the documentation-and-skeleton tranche.
2. Apply the approved active documentation set in the appropriate repositories.
3. Create `DOCUMENT_AUTHORITY.md` and update cross-links.
4. Reclassify the existing public “vNext” documentation as implemented contract 0.5 without changing schemas or immutable bytes.
5. Supersede old card-centric Builder architecture with the amended target architecture.
6. Update Builder and Data agent instructions to match observation-first authority and current naming.
7. Add only non-material package/module skeletons or no-op CLI surfaces required by the approved architecture.
8. Move no archive files and create no runtime database.
9. Call no LLM and make no network acquisition.
10. Run all relevant tests, documentation checks, brand lint and immutable checksum verification.

## 7. Required architecture amendments

Before the target architecture becomes implementation authority, add:

- `SubjectRecord` and lifecycle;
- scope and subject relationships distinct from lineage;
- correction/challenge/retraction and dependent invalidation;
- benchmark/economics artefacts;
- complete Builder-to-Data distribution acceptance;
- SQLite idempotency, retries, leases, resume, migrations and recovery.

Also require initial participation population and claim-specific authority policies for shadow registries.

## 8. Exclusions

This tranche must not:

- implement real SQLite tables beyond an explicitly approved empty skeleton;
- index the archive;
- import historical evidence;
- run the semantic benchmark;
- change a public schema;
- rebuild Data or Viewer content;
- deploy;
- delete historical documents or compatibility code;
- touch unrelated untracked debug/runtime material.

## 9. Completion report

Return:

- branch and commit;
- files added, replaced, superseded or moved;
- authority/link/brand-lint results;
- Builder/Data/Viewer tests run and outcomes;
- immutable checksum before/after;
- confirmation of no archive, runtime, public-release or Viewer mutation;
- any genuine product ambiguity, without silently resolving it.

