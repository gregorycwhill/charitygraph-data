# Data repository development and review checks

**Status:** Reference — repository reproducibility instructions  
**Date:** 11 September 2026

CharityGraph Data is a documentation, contract, schema and release repository.
It has no application dependency-install or build step. A clean public clone can
be reviewed without private runtime material or credentials.

## Clean-clone checks

From the repository root:

```powershell
git diff --check
Get-Content .\releases\v0.5.0-2026-08-15\manifest.json
Get-FileHash .\releases\v0.5.0-2026-08-15\manifest.json -Algorithm SHA256
```

The expected immutable release manifest digest is recorded in
`PUBLIC_CONTRACT_0_5.md` and `CURRENT_STATE.md`. Release bytes, schemas and
manifest content must not be rewritten.

Validate JSON examples with the host's JSON tooling or an equivalent parser.
Markdown links should be checked as repository-relative links; links to sibling
repositories are intentionally external. No private-runtime command is required
for document review.

Cross-product changes must begin with `DOCUMENT_AUTHORITY.md` and the current
`CURRENT_STATE.md`, `ROADMAP.md`, `IMPLEMENTATION_PLAN.md` and `TEST_PLAN.md`.
