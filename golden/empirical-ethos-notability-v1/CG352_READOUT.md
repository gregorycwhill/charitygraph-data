# CG352 empirical acquisition readout

Builder began at `a40e6fb0be2d83d364cc16c8b39816bfbda1eb95`; Data began at
`93a2621e9e1feb492a2f2e00767e1e4a396962b6`.  The cohort freeze is Data
commit `d2c8a14096eb3e9d60b53201192a42443f351e3b`: exactly ten challenge and
five deterministic blind controls.  Its SHA-256 is
`8f2de067b29c1834b5d9307ed580fd2cfb42045fa633104dfab1a6512b2222e4`.

Central ACNC acquisition made 30 durable attempts (15 before, 15 after a
central schema repair): 12 captures and 3 current coverage gaps (EEN-02,
EEN-03, EEN-04), all unresolved exact-name bindings.  No cases were replaced.
The initial defect was the public search envelope's `data.Name` field rather
than the legacy `data.CharityName`; repair is in Builder's central acquisition
script.  The attempt manifest retains requested/resolved locators, status,
retrieval times, raw/representation hashes, identities, bindings, and failures.

Frozen corpus: `empirical-ethos-notability-v1` v1.0.0,
SHA-256 `9419efa3496b7e4feac369f819f82057e6ff0136a6e2636f5efa22eb096fa178`.
It contains 30 provider-free packet views (two independently selected/hashes
per case); captured views share each source blob/representation lineage.  The
reference was created afterwards and before any candidate output: it is an
**independent reference adjudication**, not human gold, with SHA-256
`1030dfff7e472fc515116c78e3dd55a637439fac59fb5510eda6043588f054ac`.
All 30 items are deliberately `NOT_EVALUABLE` because regulatory identity
material alone cannot justify a §15 observation or §17 event.

Provider calls: 0. Candidate outputs: 0. Semantic acquisition: 0.
Regression command passed: the 344/345/351 retained-capture and integration
selection ran 67 tests successfully. The next blind paid extraction measurement
is **not ready**: it needs central acquisition of source families capable of
supporting semantic adjudication, while preserving the frozen cohort and corpus
version (a successor corpus, not a mutation, if such new acquisition is authorised).
