# Semantic Demand Catalogue v0.2

This is the unified evaluation corpus for question and correction-challenge demand. The v0.1 pilot remains preserved at `../semantic-demand-catalogue-v0.1/`; its 53 questions are the retained base, with seven gap-filling questions and twelve correction challenges added here.

`surface_question` is natural user wording. `semantic_contract` is the formal, parameterised evaluation contract; wording is not treated as an executable contract.

Personas are decision roles. Analytical lenses are independent and may be combined. Correction actors describe affiliation only and never confer editorial authority.

Validation:

```powershell
python scripts/validate_semantic_demand.py
```

The validator performs real Draft 2020-12 JSON-Schema validation for every retained record and then deterministic checks for uniqueness, domain coverage, taxonomy coverage, arithmetic and forbidden behaviours.
