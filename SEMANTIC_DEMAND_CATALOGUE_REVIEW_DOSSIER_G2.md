# Gate 2 semantic-demand catalogue candidate — CG-G2-SEMANTIC-DEMAND-CATALOGUE-CLEAN-398-LUNA

## Review status

**PARTIAL — stop for supervisor/Product Owner semantic review.** This candidate was authored in an isolated worktree at the exact canonical Data commit `b108746be5f9de7775996533535fe522fa651a88`. It is a review candidate, not canonical product semantics and not evidence-test input.

## Clean-base evidence

- Authoring worktree: `.cg398-data-clean`
- Base: `b108746be5f9de7775996533535fe522fa651a88`
- Initial `git status --porcelain`: empty
- Pre-existing `charitygraph-data` checkout was dirty and remained untouched; it was not the authoring base.

## Candidate shape and cardinality

The candidate contains 20 executable demand families corresponding to the 20 North Star sections. This is a hypothesis, not an imposed target. The one-per-domain hypothesis is not sufficient where subject type, lifecycle, parameterisation, temporal scope, or evidence authority materially differ. Identity/regulatory, programmes/services, fundraising/Giving Offers, finance, funding flows, relationships, outcomes/evaluation, and evidence governance require supervisor confirmation about whether the family must split. A 74-row catalogue would preserve the experiment scaffold rather than reusable product propositions and is rejected absent semantic justification.

## Legacy reconciliation

`LEGACY_74_DEMAND_INVENTORY_CANDIDATE.json` contains all 74 legacy IDs recovered from the run-395 coverage matrix. Every row must receive an item-specific Luna disposition and concrete successor before semantic canonicalisation. Generic family crosswalks are not accepted as row-level rationales. Rows whose surviving hint does not distinguish among identity, purpose, programme, funding, offer, finance, relationship, or evidence-governance semantics are explicitly **DECISION_REQUIRED** for Product Owner adjudication rather than silently mapped.

## Executable semantics

The machine-readable candidate preserves demand IDs, domains, families, definitions, required/optional execution parameters, proposition templates, examples, proposition-level evidence expectations, provenance and the shared answer-state vocabulary. `NOT_FOUND_IN_REVIEWED_UNIVERSE` means only that the proposition was not found in the bounded reviewed universe; it is never real-world absence. `NOT_APPLICABLE` and `UNRESOLVED_PROCESSING_FAILURE` remain distinct. Source authority is proposition-specific.

## Coverage

The 20 North Star domains are represented by `SDC-C01` through `SDC-C20`. This is coverage of knowledge domains, not proof that each domain has exactly one demand. Cross-domain relationships, funding, evidence governance, and temporal/provenance semantics require review before acceptance.

## Authorship and mechanics

Luna authored the demand boundaries, definitions, templates, examples, provenance interpretation, cardinality hypothesis, and migration review. Mechanical actions were limited to clean-worktree creation, copying prior migration evidence for review, counting records, and repository/status checks. No script selected a semantic disposition, inferred a successor, or generated a rationale.

## Validation performed

- Exact base SHA and clean initial status verified.
- Legacy inventory count verified: 74.
- Candidate demand count verified: 20.
- No remote publication, source acquisition, provider execution, Gate-2 evidence testing, progress award, push, PR, or gate closure occurred.
- `git diff --check` and clean post-commit status remain required after semantic repairs; no candidate commit is recommended while row-level migration fields remain incomplete.

## Decisions required

1. Confirm demand boundaries and whether any of the 20 families must split or merge.
2. Adjudicate every legacy row with an item-specific disposition, successor IDs, and rationale; generic family crosswalks are insufficient.
3. Confirm the final machine-readable schema and provenance granularity.

After those decisions and supervisor acceptance, the next authorised action is a catalogue-finalisation tranche, followed separately by Gate-2 evidence testing.
