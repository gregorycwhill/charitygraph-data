# Reality Corpus: Ethos and Notable History v1

**Status:** frozen evaluation material, not governed public charity knowledge.  
**Version:** 1.0.0 (8 October 2026)  
**Population:** 14 cases: 3 real retained-evidence controls and 11 synthetic contract cases.

The machine corpus is `golden/reality-corpus-ethos-notability-v1.json` (SHA-256 `f49735791652d3a65ab627138662653c76a615496f0f154a325bf8729d662c1b`). `scripts/validate_reality_corpus_ethos_notability_v1.py` mechanically checks its frozen identity, count, split, IDs, retained evidence bindings and coverage. Edits require a version increment and gold-matrix review. Real cases cite retained paths and stable evidence/source-record IDs, plus available observed dates, in the fixture. They intentionally make only claims supported by those retained records: two non-transfer controls and one bounded missingness control. No unretained real organisation claim is reconstructed.

| Gold case | Kind | Expected | Contract focus |
|---|---|---|---|
| RC-01 | real | rejected | beneficiary identity non-transfer |
| RC-02 | real | rejected | community identity non-transfer |
| RC-03 | real | missing | evidence/Wikimedia absence remains unknown |
| RC-04 | synthetic | accepted | explicit non-religious self-description |
| RC-05 | synthetic | accepted | formal affiliation |
| RC-06 | synthetic | accepted | historical orientation is not current affiliation |
| RC-07 | synthetic | accepted | independent characterisation with qualification |
| RC-08 | synthetic | rejected | commitment/practice/completion boundary |
| RC-09 | synthetic | rejected | parent scope non-transfer |
| RC-10 | synthetic | accepted | founder context |
| RC-11 | synthetic | accepted | merger/predecessor binding |
| RC-12 | synthetic | accepted | award without quality inference |
| RC-13 | synthetic | accepted | inquiry occurrence stays out of section 16 |
| RC-14 | synthetic | accepted | multi-source deterministic event equivalence |

| Coverage family | Case IDs | Status |
|---|---|---|
| Beneficiary/community and parent scope non-transfer | RC-01, RC-02, RC-09 | covered |
| Current self-description, formal affiliation, historical orientation, external disagreement | RC-04–RC-07 | covered |
| Commitment/practice/completion boundary | RC-08 | covered |
| Founding/founder and lineage | RC-10, RC-11 | covered |
| Award without quality inference | RC-12 | covered |
| Inquiry occurrence separate from section 16 | RC-13 | covered |
| Multi-source dedupe and discovery/support role | RC-14 | covered |
| Wikimedia/no-evidence negative controls | RC-03, RC-14 | covered |

Synthetic entries use invented subjects only and exist because retained evidence did not provide a safely citable example for that contract boundary. The corpus has no score, reputation conclusion, or publication authority. Certification should route accepted typed projections to the **contract-representability lane**, rejected/missing cases to the **non-inference lane**, RC-11 to the **lineage/scope lane**, RC-13 to the **section-boundary lane**, and RC-14 to the **event-equivalence lane**. Metrics: 14/14 fixture validity, 100% gold/fixture case-ID agreement, 100% expected adapter outcomes, 1 deterministic dedupe group, and zero prohibited-field admissions.
