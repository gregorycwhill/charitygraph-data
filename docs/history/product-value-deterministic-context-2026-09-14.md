# Deterministic product-value context candidates — 14 September 2026

**Status:** Historical offline execution record; candidate-only, not current governed authority
**Run time:** 14 September 2026, 03:56 UTC
**Cohort:** The fixed eight-subject product-value cohort
**Source boundary:** The eight exact retained ACNC AIS representations already bound by the accepted model-assisted source-only baseline lock
**Authority:** Records the bounded deterministic extraction authorized for context preparation. It does not authorize provider work, semantic execution, human adjudication, promotion, canonical changes, public release, Viewer work, or Phase 5 scale.

## Result

The Builder derived 118 private candidates from allow-listed fields in the eight retained ACNC AIS representations. The private output is in the Builder worktree at `work/product-value-baseline-2026-09-14/deterministic-context/`: `candidates.json`, `adjudication-packet.md`, `projection-preview.json`, and `run-metadata.json`. These files are ignored work data and are not committed to either repository.

The extraction reused the existing `ExperimentCandidate` provenance, scope, source-role, epistemic-status, and locator fields. It added no general NLP, discovery, or runtime behavior. Every candidate records `DETERMINISTIC_STRUCTURED_EXTRACTION`, exact subject and organization scope, source artifact/record and representation hash, retention decision, regulator-carried source role, source/effective-date metadata, and a field-level pointer attached to the existing evidence locator.

| Candidate class | Count | Treatment |
|---|---:|---|
| Legal name, ABN, and explicit AIS statement year | 24 | Identity candidates; exact values only |
| Literal charitable-purpose field values | 24 | Three boolean fields per subject; all values are `false`. These are source-field values only and do not mean that a charitable purpose is absent. |
| Literal activity field values | 16 | `ActivityOperating` and `ActivityOperatingOverseas`; no inference about current service availability, capacity, or eligibility |
| Structured program records | 46 | Exact program name and available source classification/identifier, retained at the organization scope reported by the AIS |
| Mixed purpose/activity description fields | 8 | Exact source field retained for review, with no North Star section assignment or automatic text atomization |

No explicit current registration-status field was extracted. The AIS record carrier is ACNC, but the carried AIS values are not treated as independent regulator findings; non-identity AIS assertions are labelled first-party reports carried by the regulator. The extracted program rows do not create program or service legal scopes because the retained evidence and approved request scope identify the organization only.

## Preview and sufficiency

Each subject has three Identity candidates (legal name, ABN, and statement year), three literal Purpose-field candidates, and between four and eleven section-mapped Activity candidates. Each also has one unassigned mixed purpose/activity description. Candidate presence is not evidence of correctness or governed support.

The offline projection preview contains **zero governed items, zero governed coverage states, and zero projected items**. It labels the unprocessed annual-report representation, purpose atomization, registration status, service availability/capacity/eligibility, Outcomes, and Commitments as run-specific `not_processed` states. These states describe this extraction pass only; they do not mean source silence, source unavailability, processing failure, or substantive absence. No `not_found_in_reviewed_sources` or `source_silent` state was inferred from a missing or null field.

The predeclared fixed-Inspect sufficiency rule remains: after proposition adjudication, require legal Identity, at least one accepted Purpose or Activity statement, explicit reporting scope, and explicit coverage/missingness states for material Inspect questions. For the five semantic subjects, later adjudicated Outcomes or Commitments context is additionally required. The three sparse controls require I/P/A context plus explicit gaps. On this run, all eight subjects remain **insufficient for a governed projection** because nothing has been adjudicated and no coverage state has been governed. This is not a final usefulness decision.

The private packet is prepared for Greg to adjudicate each proposition independently. Its disposition and correction/rationale fields remain blank. No human adjudication, semantic model request, provider call, new source acquisition, candidate promotion, governed projection, or public product change occurred. The five preflight requests remain byte-frozen and `PREPARED_NOT_SENT`; the locked source-only baseline was not modified. The broader Phase 5 Top-100 objective remains active, and product-value projection review remains downstream of the bounded experiments and human adjudication.

## Reproducibility and controls

- Accepted source-only baseline lock SHA-256: `dd269e6837e940601e1855e3a9b38b0e96ee669362889d91ae461bf621332d56`.
- The extractor refuses a changed lock, a representation hash mismatch, a representation not listed by the lock, an unexpected cohort/source count, an identity mismatch between ABN and source record, or a generation time not later than the lock.
- The five prepared request payloads and their manifest were not edited or regenerated.
- Existing projection construction accepts `ExperimentGovernedItem`, not `ExperimentCandidate`; regression validation confirms raw candidates cannot enter the experiment projection.
- Counts: provider calls 0; source acquisitions 0; human adjudications 0; promotions 0; governed items 0; governed coverage states 0; projection items 0.

This is a historical execution record, not a semantic experiment result or a change to the current product contract. Later project state may supersede its candidate counts or status without rewriting this record.
