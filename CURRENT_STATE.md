# CharityGraph Current State

**Status:** Canonical current-state record  
**Updated:** 2026-08-23

## 1. Current product direction

CharityGraph is the one-stop shop for structured, governed Australian charity data.

The analyst/consultant is the anchor design user. Funders, downstream personal agents, product builders, charities/advisers and public Viewer users remain first-class users. The product supports organisation, program/service, portfolio and ecosystem questions.

Builder vNext will use an evidence-first, observation-centred internal architecture:

```text
source-native records → evidence → candidates → decisions → canonical observations
                                                              ↓
                                      release projections ← derivatives and coverage
```

Cards remain stable public release objects, but are not Builder's internal knowledge store.

## 2. Repository and public cutover

The current repositories are:

- `gregorycwhill/charitygraph` — Builder;
- `gregorycwhill/charitygraph-data` — Data;
- `gregorycwhill/charitygraph-viewer` — Viewer.

The CharityGraph cutover is complete on each main branch.

| Repository | Current relevant merge |
| --- | --- |
| Data | `00079d069f1ab92d31ebb9acab398d59c9a362d0` |
| Builder cutover | `672ac6f4f7f42ee8e28593b4e86bc078355d39f3` |
| Builder full-test repair | `42370a4e1978e2f0dadb9085cfe69536d6fb07d6` |
| Viewer cutover | `4157f8d09314cf56b07da7d07c85f4055081dc0b` |
| Viewer CI repair | `e6c0d73bdb5680f187437cd52b77fd1fece77832` |
| Viewer branding cleanup | `ffaeaa3f8aed625285fc3c915070bd69a7fe47f4` |

The public Viewer is live at `https://gregorycwhill.github.io/charitygraph-viewer/`. The verified Pages deployment returned HTTP 200 with CharityGraph title, canonical URL, release pointer, schemas, source links, robots and a 121-URL sitemap.

## 3. Current public release

The current public Data release is immutable public contract 0.5:

- release: `v0.5.0-2026-08-15`;
- 120 subject cards;
- 228 public source-record sidecars;
- 349 manifest artefacts;
- immutable manifest checksum: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

That release is an implemented compatibility baseline, not the Builder vNext internal model. It must not be edited, regenerated in place or used to force card-centric implementation.

The 0.5 migration preserved unresolved historical content without upgrading it into governed observations. Important preserved totals include 402 activity items, 226 beneficiary items, 198 geography items, 573 native-taxonomy assignments, six funding/fundraising items and 86 financial records.

## 4. Validation baseline

- Builder full suite: 119 passed.
- Builder focused branding/configuration/vertical-slice suite: 12 passed.
- Legacy compatibility tests: 2 passed.
- Viewer suite: 21 passed.
- Data schema/example validation: passed.
- Static Pages build and deployment: passed.
- Brand lint: passed.
- Immutable 0.5 checksum unchanged.

This green baseline is the regression boundary for Builder vNext documentation and skeleton work.

## 5. Architecture decisions

Approved direction:

- evidence-first, typed artefact graph;
- durable `SubjectRecord` and neutral internal `subject_id`;
- explicit program/service/unit scope;
- candidate, decision, canonical and derivative separation;
- typed causal lineage distinct from subject relationships;
- task-specific deterministic, local-NLP and LLM boundaries;
- existing evidence indexed and recycled rather than destructively reorganised;
- immutable files and manifests as durable authority;
- SQLite as local operational catalogue and rebuildable index;
- DuckDB optional for analytical scans;
- PostgreSQL deferred until multi-writer or distributed operation is real;
- complete Builder-to-Data release acceptance;
- benchmark/economics and correction workflows as first-class architecture concerns.

The approved architecture requires amendment for subject lifecycle, scope/relationships, corrections, evaluation economics, distribution and operational recovery before material implementation.

## 6. Product-domain decisions

The active product model includes:

- ACNC source-native purposes and beneficiaries alongside a separate CharityGraph-native taxonomy;
- activities, beneficiaries, programs/services, role-specific geography and cause centrality;
- participation and opportunities populated from initial production processing;
- funding source, standing fundraising practice, fundraising campaign and fundraising expenditure as separate domains;
- evaluated industry shadow registries as first-class, claim-specific authorities;
- ethos and service/mission orientation as separate core domains;
- `notable_context` as neutral sourced context, never a score;
- multiple taxonomies, provenance-bound assignments and governed crosswalks;
- explicit coverage and assessment scope.

Old model-generated semantic assignments are migration and benchmark evidence, not automatic canonical facts.

## 7. Evidence archaeology

Read-only archaeology has established:

- 3,977 inventoried files totalling approximately 1.44 GB;
- 2,575 structured artefacts;
- 299 synthesis-cache records;
- 29 governed/human artefacts;
- five representative lineage dossiers;
- 1,491 historical unbound items across 114 subjects;
- no missing tracked repository files;
- no destructive moves, archive rewrites or runtime creation.

The archive is active CharityGraph evidence. It should be indexed in place, hashed and migrated lazily. Durable archaeology reports belong under the CharityGraph workspace, never Temp.

## 8. Current next gate

The next repository change is a Terra-High documentation-and-skeleton PR. It should:

1. install the approved documentation authority and rewritten active product documents;
2. update Builder architecture with the six required amendments;
3. align Builder and Data agent instructions;
4. establish internal record/schema boundaries and no-op CLI surfaces;
5. make no archive mutation, LLM call, SQLite data migration, public schema change, release change or Viewer change;
6. prove all existing tests and the immutable checksum remain green.

After that PR, implementation proceeds through SQLite/catalogue contracts, a read-only archive indexer and one deterministic end-to-end vertical slice.

## 9. Explicitly deferred

- a new public Data contract or public identifier migration;
- automated publication of ethos, sensitive context or unevaluated provider claims;
- a harm→remedy causal graph;
- demand, impact or funding-allocation modelling;
- API/MCP delivery;
- PostgreSQL or distributed workers;
- destructive archive reorganisation;
- Viewer redesign.

## 10. Local hygiene

- Active paths and documentation use CharityGraph naming.
- Literal legacy naming is isolated to immutable material, compatibility code/tests and quarantined migration evidence.
- Runtime state belongs outside synchronised storage under `C:\CharityGraph-runtime` when implementation creates it.
- Existing untracked debug/runtime material remains untouched unless a separately authorised cleanup identifies an exact target.

