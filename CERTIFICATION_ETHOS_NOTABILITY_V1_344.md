# Ethos and Notable History v1: bounded certification 344

**Corpus:** `cg-reality-corpus-ethos-notability-v1` v1.0.0, SHA-256
`f49735791652d3a65ab627138662653c76a615496f0f154a325bf8729d662c1b`.
The frozen population is 14 cases: 3 retained-evidence controls and 11 synthetic
contract fixtures. No corpus entry was changed by this certification.

## Results and bounds

All 14 expected outcomes matched observations from the 342 Builder adapters.
The auditable per-case matrix and empty mismatch ledger live with the executable
contract checks on Builder successor `cg-ethos-notability-certification-344-builder`.

| Subfamily | Cases | Result | Status |
|---|---:|---|---|
| beneficiary/community non-transfer | RC-01, RC-02 | 2/2 reject | CERTIFIED_BOUNDED (real controls) |
| missingness / evidence absence | RC-03 | 1/1 missing | CERTIFIED_BOUNDED (real control) |
| self-description; formal affiliation; historical/currentness; external qualification | RC-04--07 | 4/4 accept | CERTIFIED_WITH_REVIEW (synthetic only) |
| commitment vs practice/completion; parent non-transfer | RC-08--09 | 2/2 reject | CERTIFIED_BOUNDED (one synthetic scope control) |
| founder; merger/lineage; recognition | RC-10--12 | 3/3 accept | CERTIFIED_WITH_REVIEW (synthetic only) |
| public inquiry / section 16--17 separation | RC-13 | 1/1 accept | CERTIFIED_WITH_REVIEW (synthetic only) |
| milestone, discovery/support role, deterministic dedupe | RC-14 | 1/1 accept/dedupe | CERTIFIED_WITH_REVIEW (synthetic only) |

No evaluated subfamily is a production-extraction certification. The corpus gives
contract-invariant confidence only; its 3/11 real/synthetic split is too small and
too unrepresentative for empirical reliability claims.

## Measured error classes

Observed: 0/5 forbidden or unsupported positive emissions; 0/3 scope-transfer
errors; 0/1 temporal-currentness error; 0/2 source/epistemic-role errors; 0/1
section-16/17 error; 0/1 event-dedupe error; 0/1 qualification loss; 0/1
missingness-to-negative conversion; 0/14 provenance/lineage defects; 0/14
unresolved cases. Denominators are fixture opportunities, not prevalence estimates.

## Routing recommendation and Factory Integration handoff

Wire only source-native, bounded adapter projections into private S0 inputs, behind
the existing provenance, lowest-scope, date, and section guards. Mechanical
source-native fields and deterministic dedupe may use the constrained semantic lane;
routine bounded claims may use low-cost then stronger-model escalation. Require human
review for external or disputed characterisation, political/ideological or religious
characterisation, sensitive living-person context, adverse/legal ambiguity, and any
unresolved identity or parent/predecessor/successor scope. Do not automate these
uncertified areas, and do not make public projections.

Regression gates: frozen SHA and 14/3/11 count; the Builder executable certification
test; zero prohibited-field admissions; deterministic RC-14 dedupe; and RC-13's
absence of a section-16 finding. No implementation fix was justified or made.
