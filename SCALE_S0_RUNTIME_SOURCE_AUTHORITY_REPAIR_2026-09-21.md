# Scale S0 durable source-runtime-authority repair — 21 September 2026

**Status:** implemented local runtime-control repair and offline certification
only. This record does not authorise S0 execution, a source acquisition, a
provider call, a reservation, candidate creation, promotion, publication, a
new execution attempt, or a public-contract change.

## Defect and boundary

The prior S0 runtime stored the immutable mandate alongside a serialised mapping
of concrete `SourceAuthorisation` objects. That mapping could be read at live
reconstruction and provider-send time. It made a policy mandate appear to carry
resource-level authority and left the exact source decision insufficiently
separate from caller memory.

This is why Attempt 5 (`attempt:s0:5` / `run:s0:attempt-5`) legitimately
stopped at its first governed-acquisition item. Its durable mandate had
`authority_json.sources = {}`. Although the canonical governed HTTP(S)
transport and its acquisition bridge already existed, there was no exact,
executable subject-bound locator/resource/version/licence/rights binding or
durable source-specific authority for a live reconstruction to use. Therefore
no live source plan, acquisition, packet, reservation, owner-attestation
binding, source-network crossing, provider call or other execution occurred.

`acnc_register` and `acnc_ais` remain mandatory baseline source families and
are policy-ready. That does not pre-authorise a concrete ACNC Register or AIS
resource: each live use still needs a current exact resource identity and
version, applicable licence, source-specific rights decision and authority
material before acquisition. Controlled resources cannot inherit any of those
facts from an unrelated endpoint, sibling resource or historical example.

The repair preserves the mandate as immutable policy authority only: population,
finite source-family universe, registry, routing and versioned policy artefacts.
It does not authorise an individual locator, resource, access state or rights
decision.

## Migration 22: concrete source authority

Builder schema migration 22 adds the append-only,
idempotent `scale_s0_source_authorities` control-plane ledger. One concrete
authority binds all of the following material before it is usable live:

- immutable mandate ID/hash and slice;
- execution attempt;
- source family and mandated subject;
- source ID, requested locator and exact resource identity;
- rights-policy ID/version, exact rights-decision identity and transmission
  decision;
- access classification and technical-access state;
- authority role and non-empty authority material, each with a canonical hash;
- authorised claim families and a timezone-aware creation time.

For `SEPARATELY_LICENSED_OR_CONTROLLED` authority, the material must also name
the exact resource and version, licence and licence version, and rights-authority
reference. The material resource identity must equal the ledger's exact resource
identity. `OPEN_WEB_PUBLIC` is a separate access classification, governed by
the adopted open-web policy, and cannot silently stand in for controlled or
licensed authority.

The ledger is not a source-body store and does not duplicate evidence. Raw bytes
remain in the content-addressed artefact store; source-native records and
acquisition receipts remain in their existing governed tables; snapshots,
representations, corpora and packets remain their existing immutable lineage.
An identical registration is idempotent. A changed material hash, competing
source ID, or repeated exact rights decision conflicts fail closed.

## Live reconstruction and crossings

Live `from_catalog` reconstruction reads only the durable policy mandate,
attempt-bound packet, source-authority ledger, snapshot, representation, corpus
and reservation state. It does not recover concrete source authority from the
mandate or accept a caller-provided replacement. The pre-send gate independently
rechecks the durable authority material/hash, mandate and rights-policy version,
subject/family/claim-family bounds, exact snapshot locator/hash and source record,
representation, corpus, bundle, reservation and owner-attestation lineage.

The existing governed transport and acquisition path is retained. Before a
transport boundary opens a socket, it resolves the supplied authority ID from
the durable ledger and checks its attempt, mandate/slice, subject, family and
locator binding. Caller fields other than that lookup identity do not grant
authority. Acquisition repeats that resolution and persists the resulting
attempt-owned snapshot through the existing bridge. It creates neither a second
source store nor a second packet system.

`OPEN_WEB_PUBLIC` remains subject to the adopted policy and accessible technical
state. `SEPARATELY_LICENSED_OR_CONTROLLED` additionally needs its exact
specialist-source authority. `TECHNICALLY_WITHHELD`, unavailable, malformed,
unbound, substituted or tampered material fails before a live crossing or send.
Such a failure never represents substantive absence.

## Offline boundary and destructive certification

Offline fixture paths must opt in explicitly. A catalogue-backed acquisition
without a live execution attempt and without offline mode fails before source
records or receipts are written. Explicit offline fixtures remain restricted to
local synthetic material and never become live authority.

The local destructive suite exercises the persistence, reconstruction and
transport boundaries using synthetic material and loopback inputs only. It does
not establish any current ACNC resource, version, licence or rights fact, and
it performs no external source-network or provider operation.

## Status retained

S0 remains `S0_AUTHORISED_NOT_YET_EXECUTED`. Attempts 3, 4 and 5 remain
historical/read-only execution evidence and were not touched by this repair.
In particular, Attempt 5 must not be resumed or reused for a live execution
after canonical implementation or material hashes change. A future live S0
execution requires a fresh execution-attempt/run identity bound to the
post-repair canonical Builder and Data commit SHAs, then its own exact durable
runtime source authorities. Public contract 0.5 and its immutable release bytes
are unchanged.
