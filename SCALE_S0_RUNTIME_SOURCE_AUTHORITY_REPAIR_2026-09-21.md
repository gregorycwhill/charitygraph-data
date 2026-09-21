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

The local destructive suite covers mandate/source separation, migration 22,
idempotency, required binding absence, source family/subject/locator/resource,
rights-policy version/decision, access/technical state and authority-material
substitution, competing source decisions, durable restart reconstruction,
cross-attempt ownership, snapshot/representation/corpus/packet/reservation
lineage, owner-attestation gating, governed transport caller-spoof rejection,
and explicit offline fixtures. It performs no external network or provider
operation.

## Status retained

S0 remains `S0_AUTHORISED_NOT_YET_EXECUTED`. Historical halted material is not
resumed or rewritten. No Attempt 3, Attempt 4 or Attempt 5 is created or
authorised by this repair. Public contract 0.5 and its immutable release bytes
are unchanged.
