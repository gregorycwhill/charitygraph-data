# Final semantic certification 328

**Status:** local Data-only certification record; no remote publication

**Baseline:** `9ff597fd2bfa81e78b424849444d8d6d873047d4` (327), descended from
`0b15014e7363a31e82a1682f597b11d7ef2af831` (326).  The declared remote
canonical Data `main` head remains
`ee42605f31381f24e0d81fc0bd813abd89dd3d43`; this certification neither
fetches nor mutates it.

## Authority and annotation rule

Reviewed authority: `NORTH_STAR_TARGET_CARD.md` / v0.3, especially section
20; `PRODUCT.md`; `PRINCIPLES.md`; `EXPERIENCES.md`; and
`INTEGRATED_PRODUCT_AND_DATA_MODEL.md`.  Section 20 is **primary** where the
substantive demand is evidence/coverage/freshness/correction state itself;
**supporting** where one of those concepts materially constrains another
substantive demand; and **absent** where provenance or currentness is only
generic output hygiene.  Thus currentness alone does not select section 20:
an as-of scheme designation remains domain 19, while an availability answer
that turns on positive evidence, tested missingness, or its review basis uses
section 20.

## End-to-end question audit

Each of the sixty questions was reviewed for persona, independent lens, tier,
primary/supporting domains, subject/scope, temporal and evidence contract,
forbidden inference, signature, and distinction. `retain` means all these
elements remained coherent under the rule above.

| Questions | Result and semantic finding |
|---|---|
| 0001–0005 | retain — native classification/purpose/service/participation demands; as-of wording is not itself a coverage demand. |
| 0006–0014 | retain — capacity, funding, finance and fundraising distinctions stay scoped and non-inferential. |
| 0015–0020 | retain — evaluation/reproducibility contracts use section 20 only as material evidence state or as their primary subject. |
| 0021 | changed `primary [7] / supporting [5]` to `primary [20] / supporting [7,5]`: tested missingness and coverage basis are the answer, not generic service metadata. |
| 0022–0024 | retain — assessed/source classification, scope and relationship demands are distinct. |
| 0025 | changed supporting domains from `[5]` to `[5,20]`: time-bound positive availability evidence materially constrains the service-access answer; service availability remains primary. |
| 0026–0034 | retain — no currentness-only promotion; finance, fundraising, service history and conduct remain meaning-derived. |
| 0035–0050 | retain — correction/review state, evidence evaluation and service coverage remain distinct from their substantive domains. |
| 0051 | changed supporting domains from `[5,7]` to `[5,7,20]`: inclusion/exclusion and missingness reasons are a material coverage-state constraint on the service retrieval. |
| 0052–0053 | retain — evidence gaps constrain the intervention/service demand without replacing it. |
| 0073–0078 | retain — current Giving Offer, historical assessment and entity continuity retain their independently scoped semantics. |
| 0079 | changed `primary [7] / supporting [5]` to `primary [20] / supporting [7,5]`: it asks for the positive-evidence answerability state rather than service discovery alone. |

The numbering gaps reflect the curated baseline; no records were introduced to
fill them. Persona counts retain genuine `analyst` (4) and `downstream_agent`
(1) representation; no persona or lens was reassigned for balancing.

## Correction-challenge audit

All fourteen challenges retain the existing single primary correction locus,
with downstream reprojection explicitly downstream rather than a second locus.
No correction architecture was reopened. SDC-0061–0065 and 0067–0071 remain
coherent. SDC-0066 gained supporting section 20 because a governed correction
qualifies the legal-restriction interpretation. SDC-0072 gained supporting
section 20 because dispute/adjudication state materially constrains the conduct
answer. SDC-0080 was repaired from a copied finance contract to a source-edition,
effective-date and supersession contract, and uses section 20 primary with
section 19 supporting. SDC-0081 was repaired from the same copied finance
contract to a parallel source-reported/assessed classification contract; section
19 remains primary and section 20 supporting. Their correction targets, bases,
dispositions and preservation requirements now agree with their correction
classes and loci.

## Section 20 result

Primary (11): SDC-0020, 0021, 0029, 0035, 0040, 0050, 0079, 0062, 0069,
0070, 0080.

Supporting (22): SDC-0015, 0016, 0022, 0025, 0027, 0036, 0037, 0043, 0051,
0052, 0076, 0078, 0061, 0063–0068, 0071–0072, 0081.

Absent records were individually retained because their demands are domain
native and do not materially ask for or depend on evidence state beyond generic
provenance hygiene. This rejects both blanket rules considered in review.

## Coverage, distinctness and checks

There are 74 records: 60 questions and 14 correction challenges. Exact
semantic signatures are 74/74 unique; review found no surface-only duplicate
or padding candidate that warranted a merge. All 20 North Star domains remain
represented without annotation balancing. Domain references are: 1:17, 2:5,
3:21, 4:4, 5:19, 6:2, 7:20, 8:7, 9:3, 10:6, 11:3, 12:7, 13:22, 14:7, 15:7,
16:8, 17:14, 18:11, 19:10, 20:33.

Persona references: analyst 4; charity_insider_adviser 9;
consultant_service_system_planner 11; data_developer 12; downstream_agent 1;
funder_diligence 13; public_donor_participant 9; researcher_evaluator 15.
Lens references: cohorting 1; coverage 6; discovery 11; ethos_conduct 6;
evidence_evaluation 10; finance 12; funding_ecosystem 6; fundraising 5;
mandate_screening 7; reproducibility 16; service_system_mapping 14. Question
tiers are A:14, B:25, C:21; correction challenges are tier-not-applicable:14.

Deterministic validation: `python scripts/validate_semantic_demand.py` passed
(`74`, questions `60`, corrections `14`). `python -m compileall -q scripts`
passed. `git diff --check` passed. The offline environment has no
standards-compliant Draft 2020-12 engine (`jsonschema` unavailable), so schema
conformance remains the pre-existing bounded tooling gap and was not simulated
or installed from the network.

## Residual risk and decision

The remaining risk is only the absent offline Draft 2020-12 validator; it does
not weaken the deterministic validation or semantic certification. Builder was
untouched, no external/authenticated GitHub mutation occurred, and this report
is local to the successor Data worktree.

**Final decision: `SEMANTIC_DEMAND_PILOT_SCALE_READY`.** The curated pilot is
fit to inform a separately governed 700–1,200-question scale-generation
exercise; that exercise is not authorised or performed by this certification.
