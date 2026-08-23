# RC3 release-gate evidence

> **Authority status:** Historical release-gate evidence. It records RC3 only and does not govern the current product or release.

Candidate: `phase2b-2026-08-13-rc3`.

## Automated gates

- Builder: 55 tests passed.
- Viewer: 13 tests passed.
- Candidate validation passed.
- Pages bundle preparation passed.
- Rendered source-native static HTTP crawler: 326/326 returned HTTP 200 locally and again against the deployed GitHub Pages URLs.
- Corpus invariants: 120 cards; 120 clean canonical CauseBase URLs; 120 ACNC profile locators; 101 submitted AIS locators; 19 explicit no-submitted-AIS coverage states.

## Regression-card inspection

| Fixture | Purpose | Observed result |
| --- | --- | --- |
| Environmental Justice Australia | golden card/report/participation | DGR, current AIS, program, participation, funding and two financial observations |
| Australian Rural Youth Foundation | sparse/no-AIS/non-DGR | ACNC profile; no submitted AIS and no DGR are explicit absence states |
| Ann Street Presbyterian Church | parish/religious body | ACNC profile, AIS, program and financial observation |
| Australian Conservation Foundation | major provider/DGR | ACNC profile, AIS, two programs, DGR, financial observation |
| Accelerated Evolution – The Break | multiple programs | ACNC profile, AIS and ten program observations |
| Australia Chung Tai Buddhist Foundation | DGR/religious body | ACNC profile, AIS, program, DGR and financial observation |
| Access Church | non-DGR | ACNC profile, AIS, program, financial observation; no DGR assertion |
| Biopixel Oceans Foundation | multiple programs | ACNC profile, AIS, nine program observations, DGR |
| Catholic Church Insurance | identity-complex legal form | ACNC profile, AIS, program and financial observation |

## Deployed EJA smoke check

A headless-browser rendering of EJA verified the visible About section, ABN link, exact canonical ACNC profile link, explicit `Deductible Gift Recipient: Yes`, programs, participation, compact classification chips, History, Similar organisations, canonical correction prefill URL, and the first main-prose citation as `[1]`. The left browsing pane presents collapsed filters followed by the independent result list; result rows omit ABNs.
