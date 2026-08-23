# CharityGraph Principles and Guardrails

**Status:** Canonical shared product contract  
**Version:** 1.1-draft  
**Date:** 2026-08-23

## Public purpose

1. Be the one-stop public integration layer for structured, governed Australian charity data.
2. Describe before evaluating. CharityGraph supplies evidence and structure, not worthiness, recommendation or allocation decisions.
3. Design for organisation, program/service, portfolio and ecosystem questions.
4. Use the analyst/consultant as the anchor design user while serving funders, agents, builders, charities and public users.
5. Treat machine distribution as a product channel, not an afterthought.

## Identity and scope

6. A CharityGraph subject exists independently of any source record, identifier, name, card or taxonomy.
7. Names and domains never create identity by themselves.
8. Keep source-to-subject binding explicit, governed and reversible.
9. Distinguish organisations, groups, legal entities, units, funds, programs and services.
10. Allow scoped program/service observations without prematurely creating durable subjects.
11. Keep real-world subject relationships separate from processing lineage.

## Knowledge and evidence

12. Evidence precedes synthesis.
13. Preserve source-native records before canonicalising selectively.
14. Separate candidates, governed decisions, canonical observations and derivatives.
15. Claim basis and extraction method are independent.
16. Preserve material provenance, qualification, conflict, uncertainty and time.
17. Source authority is claim-specific. No publisher is universally authoritative for everything it says.
18. Evaluated shadow registries are first-class authorities for their registry-defined facts.
19. Public accessibility does not override source rights or authorise bulk republication.
20. Absence is not a negative claim. `not_found_in_source` requires a declared assessment scope.
21. An unsupported claim is prohibited, but null-by-default is not success. Prefer a source-linked, method-labelled model interpretation with uncertainty when evidence supports it.

## Domain integrity

22. Keep ACNC source classifications separate from CharityGraph-native classifications.
23. Support multiple versioned taxonomies and provenance-bound crosswalks.
24. Keep cause centrality separate from taxonomy adjacency and user-specific mandate rules.
25. Keep beneficiary identity separate from organisational ethos.
26. Keep ethos separate from service or mission orientation.
27. Treat `notable_context` as sourced context, never as a score or reputation balance.
28. Keep funding source, standing fundraising practice, fundraising campaign and fundraising expenditure separate.
29. Never infer fundraising ROI, causal revenue attribution, effectiveness or quality from descriptive observations.
30. Fundraising expenditure has no universal prior, peer fill, forced point or automatic midpoint.
31. Treat participation as a current core capability; distinguish stable modes from transient opportunities.
32. Keep evidence URLs separate from action or application destinations.
33. Preserve source statement signs and exact money; make normalisation and currency conversion explicit derivations.

## Models and automation

34. Use Python as the control plane and LLMs as the routine semantic engine. Deterministic work should prepare, constrain and validate model work, not postpone it until a brittle local pipeline fails.
35. Model outputs are candidates or derivatives, never human decisions. A model candidate may become canonical only through a separately versioned, benchmarked automation policy and is never relabelled as human-governed.
36. Separate logical task contracts for OCR/vision recovery, relevance, extraction, interpretation, taxonomy, writing and embeddings; several logical tasks may share one physical request only when benchmarked and independently validated.
37. Treat batching, scheduling, caching, retry control, cost reservation/reconciliation and resumability as core Python responsibilities.
38. Version material prompts, policies, task schemas, model snapshots, tools, pricing tables and cache identities.
39. Do not build custom local NER, relevance, taxonomy or summarisation models in the initial architecture. Admit one only after a total-cost-of-ownership benchmark includes coding, labels/evaluation, maintenance and operations as well as API spend.
40. Authorise automation by domain-specific policy and evidence, not by convenience. Use human review for samples, conflicts, sensitive claims and higher-exposure cases rather than as a universal gate.

## Corrections and releases

41. Accepted corrections change governed inputs and regenerate dependent outputs.
42. Raw correction submissions are private by default; public contestability concerns moderated proposals and decisions.
43. Sensitive context receives heightened evidence, risk-weighted review and expedited correction handling.
44. Publish only complete, validated, allowlisted release candidates.
45. Keep immutable releases immutable and retain a previous valid release when publication fails.
46. Generate representations from the same release selection of observations and derivatives.

## Economics, interface and institutional posture

47. Give every eligible subject a cheap common evidence baseline and an economical model-assisted pass where the cohort policy requires it.
48. Rank initial processing by total donations as an explicitly labelled donor-decision-exposure proxy. It determines priority and assurance spend, never merit, quality, credibility or recommendation.
49. Enforce pooled paid-model budgets of AUD 100 for the first 100 charities, AUD 100 for the next 1,000 and AUD 100 for the next 10,000; include extraction, judgement, writing, embeddings, retries and escalations.
50. Allocate spend within each cohort by evidence opportunity, risk and expected information yield. Easy subjects may subsidise difficult ones; cross-cohort transfer requires approval.
51. Optimise useful coverage subject to provenance, correction and quality constraints. A near-perfect system that publishes almost nothing fails.
52. Keep Viewer credible, utilitarian, dense, accessible and fast.
53. Apply the anti-marketplace test: if the interface persuades users to favour, trust or donate to a subject, it has moved in the wrong direction.
54. Keep CharityGraph inspectable, challengeable and replaceable.
