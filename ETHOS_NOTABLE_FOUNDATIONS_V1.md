# Ethos and Notable History Foundations v1

**Status:** Implemented bounded internal-domain contract; no public-schema or release authority.
**Date:** 8 October 2026
**Applies to:** `north-star-v0.3` sections 15 and 17 only.

## Projection lineage

`north-star-v0.2` remains an immutable historical projection identity. Its
existing section-15 specialist observations remain v0.2 records and are not
renamed. The active v0.3 implementation uses `north-star-v0.3` explicitly for
new section-15 and section-17 observations. The section numbers are stable
for these two sections, but identity is still versioned: an adapter or card
assignment must state its contract ID rather than treating v0.2 as v0.3.

## Section 15: Ethos v1

The contract records one source-faithful descriptor at one durable subject and
lowest supported scope, with evidence locators, source record(s), lineage,
effective/observation time, source role, qualification and material
disagreement. It has exactly four epistemic roles:

- `self_described`;
- `formal_affiliation`;
- `external_characterisation`; and
- `historical_orientation`.

It does not prescribe a religious, political or ideological taxonomy. A
commitment, claimed implementation, observed practice and verified completion
remain distinct lifecycle observations; none is upgraded by this contract.

## Section 17: Notable Event/History v1

The event contract supports bounded founding/founder, institutional milestone,
merger/split/succession, program/campaign, public inquiry/review,
recognition/award, movement/network and notable-person relationship events.
Every event retains the source-faithful statement; subject/scope; event date
separate from source/retrieval date; discovery/supporting/corroborating role;
evidence locator(s); qualifications/uncertainty; lineage; and related-subject
or predecessor/successor binding where material. A deterministic candidate ID
over event identity collapses repeated descriptions of one event.

An inquiry/review in section 17 records an occurrence/procedural status only.
Allegations, findings, sanctions and remediation remain section 16 records and
may be linked by a future governed relation, never copied as section-17 prose.

## Non-inference boundary

Neither contract permits beneficiary identity to establish ethos; parent,
network or predecessor attributes to transfer; founding to establish current
affiliation; a commitment to establish practice; ethos to establish service
participation rules; an award to establish quality; an inquiry to establish an
adverse finding; or missing evidence to establish secular/neutral status,
reputation, notability or absence. Wikimedia is only a possible discovery
source and its absence is not history missingness.

The executable Builder authority is
`src/charitygraph/ethos_history.py`, with regressions in
`tests/contracts/test_ethos_history_v1.py`. It establishes a foundation only:
no production acquisition, broad corpus certification, public projection,
automatic promotion or universal ontology is authorised.
