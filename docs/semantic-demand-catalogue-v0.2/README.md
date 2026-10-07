# Semantic Demand Catalogue v0.2

This is the unified evaluation corpus for question and correction-challenge demand. `scenarios.json` is the committed validation target: it contains 60 semantically curated question records and fourteen correction challenges. The seven 325 coverage-review variants were removed as non-distinct; seven independently justified demand gaps were added. See `CURATION_REVIEW.md` and `curation-audit.json`. The v0.1 pilot remains preserved at `../semantic-demand-catalogue-v0.1/` as historical source material.

`surface_question` is natural user wording. `semantic_contract` is the formal, parameterised evaluation contract; wording is not treated as an executable contract.

Personas are decision roles. Analytical lenses are independent and may be combined. Correction actors describe affiliation only and never confer editorial authority.

Validation:

```powershell
python scripts/validate_semantic_demand.py
```

The Python validator performs deterministic semantic checks for the committed records. Draft 2020-12 validation is a required separate gate; this repository currently has no offline standards-compliant engine available, so this run must not represent deterministic checks as JSON Schema conformance.
