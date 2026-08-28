# Semantic Reliability Baseline — 2026-08-28

**Status:** Reference — experimental validation note, not product performance guarantee

**Date:** 28 August 2026

## Scope

This note records an exploratory repeated-measures baseline from `program_service_discovery/v2` using GPT-5.6 Luna. The fresh heterogeneous cohort was drawn mechanically from ACNC 2024 AIS donation ranks 1–10,000; 18 subjects were selected. The final run produced 17 successful semantic outputs and one provider-terminal case. An execution incident unintentionally produced independent repeated outputs for 17 subjects using materially identical frozen evidence, prompt, schema, model and parameters. The repetitions were serendipitous, not prospectively designed.

## Repeatability observations

- 17 paired charities;
- substantively identical: 2;
- minor naming/granularity variation: 5;
- material subject differences: 7;
- major structural disagreement: 3;
- run-1 proposals: 99;
- run-2 proposals: 97;
- semantically matched proposal families: 69;
- run-1-only: 30;
- run-2-only: 28;
- descriptive pooled matched-subject Jaccard: `69 / (69 + 30 + 28) ≈ 54%`;
- among the 69 matched proposal families: 2 disposition disagreements and 2 operational-status disagreements.

Subject enumeration and grain were much less stable than attributes conditional on rediscovering the same subject. These figures are exploratory descriptive observations, not an established product performance rate or acceptance threshold. In particular, they must not be presented as approximately 97% reliable attribute agreement.

## Qualitative observations

- category/portfolio/registry artefacts were observed in 11/17 successful cases;
- channel-as-service was observed in 7/17;
- weak evidence with high confidence was observed in 8/17;
- unsupported impact/outcome claims were apparent in 0/17;
- acquisition-limited interpretation was explicit in 3/17.

Repeatability is not validity. Source-role mistakes can be highly repeatable, while valid subjects can appear in only one replicate. Subject discovery and fixed-subject classification should therefore be evaluated separately. Deliberate prospective replication is required before quantitative public reliability claims.

This reference intentionally omits private runtime paths, response identifiers, response bodies and charity-by-charity review output.
