# CharityGraph — Codex Handoff

**Status:** Active bounded execution handoff

**Updated:** 24 August 2026

**Task:** Install Product Documentation Rewrite 2.0-draft; no product code

## 1. Outcome

Install the supplied documentation packet as CharityGraph's coherent active product authority, reconcile repository-local links and supersession, validate the unchanged code/release baseline, and open clean PRs for review. Do not begin the Builder reality slice in this task.

## 2. Model and effort

This task is mechanical and bounded. **Luna-High is sufficient.** Escalate to Terra only if repository-local authority conflicts cannot be resolved from `REWRITE_MANIFEST.md` and the existing documents without making a new product decision.

Do not spend tokens redesigning approved content or repeatedly polishing prose.

## 3. Preconditions

Before editing:

1. locate the Builder, Data and Viewer repositories under the CharityGraph workspace;
2. fetch and confirm clean/current `main` branches without deleting branches;
3. record `main` heads;
4. verify the immutable v0.5 manifest checksum;
5. inventory untracked files and preserve them untouched;
6. read this handoff, `REWRITE_MANIFEST.md` and `DOCUMENT_AUTHORITY.md` completely.

Expected recorded heads at packet creation:

- Builder: `8e4f2a099f7cb4a004a8ca8785f2f810a7d7d534`;
- Data: `9650781febfded436c00cbcddf9211a80a5babce`;
- Viewer: `cd6f3720f664a29e0ca7ed8be19797e573fcdfc8`.

If remote `main` has advanced normally, use the new head and report it. If the approved Builder contracts, SQLite foundation, licensing/brand work or immutable boundary are missing, stop and report the blocker.

## 4. Data repository task

Create a branch named `charitygraph-product-docs-v2` from current Data `main`.

Apply all nineteen Markdown files from the packet to the repository root according to `REWRITE_MANIFEST.md`. Preserve exact supplied bytes except for a strictly necessary repository-local relative-link correction; report any such correction.

Reconcile existing active documents:

- leave exactly one canonical document per subject;
- retain useful old reviews/contracts as history or reference;
- mark superseded documents clearly so agents cannot follow them as current instructions;
- update `README.md`, `AGENTS.md` and documentation indexes to point to the new authority set;
- keep current public-contract and brand/reuse documents consistent;
- do not change schemas, examples, release artefacts or licence terms.

Commit and push the branch. Open one Data PR targeting `main`. Do not merge it.

## 5. Builder repository task

Create a separate branch named `charitygraph-product-docs-v2-links` from current Builder `main`.

Make only repository-local documentation/link changes required by the manifest:

- link to canonical product documents in Data;
- identify `INTEGRATED_PRODUCT_AND_DATA_MODEL.md`, coverage policy, source governance, taxonomy governance, implementation plan and test plan;
- state that implemented contracts/ADRs refine conceptual authority;
- make the first private identity/program/classification slice the next implementation work;
- remove or supersede conflicting current instructions to resume old enrichment;
- preserve all implemented code contracts and historical compatibility material.

Do not copy all nineteen files into Builder. Do not edit source, tests, migrations, package metadata or CLI behaviour.

Commit and push the branch. Open one Builder PR targeting `main`. Do not merge it.

## 6. Viewer task

Inspect documentation links only. If no active link breaks, make no Viewer branch or PR. If a link must change, create a minimal documentation-only branch and PR; run the Viewer test/build checks but do not deploy.

## 7. Validation

Run:

### Data

- repository-provided schema/example validators;
- future publication-identity/schema tests where available;
- relative Markdown link checks;
- active-document naming lint;
- `git diff --check`;
- immutable release checksum.

### Builder

- full test suite from the documentation-only branch;
- focused contract/runtime suite if separately defined;
- legacy compatibility tests;
- warning-as-error imports;
- active-document naming lint;
- `git diff --check`;
- immutable release checksum boundary check.

### Viewer

Only if changed: suite, Pages build, link/canonical checks and `git diff --check`.

Do not call real providers/models or make source-acquisition network requests.

## 8. Protected material

Leave untouched:

- the immutable v0.5 release directory and manifest;
- Data schemas/examples and generated release bundles;
- Builder SQLite migrations and runtime code;
- archives, runtime databases, caches and credentials;
- archaeology evidence/reports unless the manifest explicitly requires a link;
- Viewer `debug.log` and other pre-existing untracked files;
- retained feature branches.

Do not create reports in a temporary directory. Put the completion report in the PR descriptions and, if a file is necessary, under the CharityGraph project workspace in the relevant documentation/history location.

## 9. Stop conditions

Stop without improvising if:

- the immutable checksum differs before edits;
- installing supplied bytes would overwrite a newer approved canonical document;
- two authorities cannot be reconciled without a new product decision;
- required repository instructions prohibit the mapping;
- implementation or schema changes appear necessary;
- secrets, private archives or release artefacts would enter the diff.

Report the exact conflict and the narrow decision required.

## 10. Completion report

Return:

- repository branches, commits and PR links;
- original and final `main`/branch heads;
- exact file mapping and any byte departures;
- documents superseded, retained as reference or cross-linked;
- test and lint results;
- immutable checksum before/after;
- confirmation that no code, schema, release, archive/runtime, model/network or deployment change occurred;
- untracked material preserved;
- any genuine ambiguity or blocker.

After that report, stop. The next coding prompt for PR A of `IMPLEMENTATION_PLAN.md` will be prepared separately after documentation review/merge.
