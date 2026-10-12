# Campaign 399 semantic reconciliation — Luna review dossier

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

## Authority and inputs

Current semantics are authored against Data commit `b108746be5f9de7775996533535fe522fa651a88`. Terra recovery commit `b082d30784494b7d8570edbd5e05da36e040d2c4` is evidence only. The authoring worktree is `C:\CharityGraph-runtime\cg399-legacy-demand-reconciliation-luna`, detached at the Terra commit, and started clean.

Recovery inputs and SHA-256:

* `README.md` — `db87ded0c7a240effa85a02b79dcd2bc651276aa020679c4d6c3b321b34f0f4b`
* `legacy-demand-recovery-ledger.v1.json` — `504492c6cc6293ac15350ca55d35917111589cf01be530f77737417b300d236`
* `validation.json` — `ae44367132e4603590dbefcb043e7b7dcdd0a925c82a45fc8bd38b91a7cc0cd1`

Independent validation found 74 unique rows: 53 `RECOVERED_EXACT`, 21 `HINT_ONLY`. Every migration row cites its exact ledger identity through `legacy_id`; exact historical wording and its recorded provenance remain in the Terra ledger. No HINT_ONLY row is promoted to historical equivalence; all 21 are explicitly `UNRECOVERABLE_LEGACY_SEMANTICS`.

## Catalogue decision

The executable catalogue contains 20 evidence-driven reusable propositions. The number is a result of decomposition, not a target: several domains require multiple demands because subject, scope, time, evidence authority or answer state differs; several demands cross domains. Every candidate contains subject, required/optional parameters, scope, temporal semantics, applicability, positive proposition, evidence-role expectations, answer states, missingness caution, example and current-canonical provenance in both the JSON and this review package.

## Run-398 hypothesis test

The run-398 one-demand-per-domain hypothesis is rejected as a catalogue rule. It is too coarse for access versus service delivery, purpose versus classification, activity versus outcome, finance versus aggregation, commitment versus conduct, and evidence lineage versus coverage/freshness. The current 20 candidates happen to cover the 20 North Star domains, but several candidates are cross-domain and domains 3, 5, 7, 13, 18 and 20 have materially distinct propositions. No legacy count is used as a current-demand target.

## North Star coverage

Domains 1–20 are covered by candidate IDs in `north_star_domains`. Cross-domain examples include C04/C05 (service and access), C10 (relationships and funding), C15/C16 (evaluation and activity), C18/C19 (evidence and coverage), and C20 (finance and evidence). Coverage is explicit in the machine-readable catalogue; no domain is silently treated as a question.

## Authorship and safety audit

Luna made the semantic boundaries, candidate definitions and all 74 dispositions. No lexical similarity, family-name shortcut, keyword score or script generated a disposition or rationale. Mechanical checks were limited to JSON parsing, candidate-ID uniqueness, vocabulary checks, successor-reference checks, 74-row coverage, domain coverage, provenance presence, whitespace and clean-status checks.

## Next action

Product Owner Greg should review the 20 current proposition boundaries and the 21 deliberate historical breaks, especially the access/service split, finance/aggregation split, and conduct/commitment split. Do not acquire sources, adjudicate Gate-2 evidence, publish, close Gate 2 or award progress until that review is complete.
