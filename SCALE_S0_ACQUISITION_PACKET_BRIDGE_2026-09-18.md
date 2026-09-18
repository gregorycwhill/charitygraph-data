# Scale S0 acquisition-packet bridge certification

**Status:** offline implementation checkpoint; no execution authority

The original Scale S0 pre-execution stop remains authoritative.  PR #34 records
that stop and remains open and unmerged.  This work does not resume S0.

## Inventory and adapter decision

Builder already has reusable immutable S0 mandates, task registry, source
authorisation, packet, preflight, halt and durable-catalogue controls.  It also
has content-addressed source artefacts, source records, acquisition receipts and
document-v2 representations.  `bootstrap_cohort` is deliberately a historical
Top-100 path: it rejects any cohort other than exactly ranks 1--100 and ties
identity creation to the frozen ACNC CSV.  The generic ACNC profile script saves
convenience JSON and is not a governed S0 acquisition path.

The bounded Builder adapter introduces an offline-only sequence from immutable
mandate population to centrally planned sources, source authorisation, fixture
acquisition, immutable snapshot identity, representation, frozen corpus,
honest task applicability and frozen packet material.  It has no HTTP client,
provider client, reservation creation or semantic execution entry point.

Migration 18 is required and is deliberately narrow. It persists immutable
source plans, snapshots, representation bindings, corpora and physical bundles
in the canonical Builder catalogue. Raw bytes remain in the existing
content-addressed artefact store; source-native records and acquisition
receipts remain in their existing tables. Packets carry the frozen corpus ID in
their immutable material, retaining the packet-to-corpus link without a second
packet schema or store.

## Offline checkpoint evidence

The deterministic fixture checks prove exact eight-subject membership,
order-independent population identity, and rejection of seven, ninth and
substituted subjects. It covers ACNC Register/AIS structured fixtures, public
HTML, reliable-text and visually material PDF representations, parsing failure,
controlled specialist authority, technically withheld login, unavailable
responses, immutable source records/acquisition receipts, corpus freeze,
applicability, logical packet preparation, compatible physical bundles and the
existing preflight construction. Restrictive terms metadata is non-veto open
web provenance; a technical barrier fails before acquisition. The packet is
only prepared; there are zero provider sends and zero reservations.

Focused bridge, migration and S0 durability tests pass. The complete Builder
suite passes locally, with three pre-existing configuration deprecation
warnings. No S0 test performs a network call or provider operation.

## Certification result

`S0_ACQUISITION_PACKET_BRIDGE_INCONCLUSIVE`

The control-plane implementation and Builder suite pass, but this is not an
honest full bridge certification: the fixture representation values are
explicit test inputs and have not yet been produced by document-v2 from real
local PDF fixture files. The required PDF extraction/render path and its
page-selected artefact lineage therefore remain unproven. This is a material
representation-certification gap, not a source-policy or provider defect.

The offline bridge is not a live recovery decision. It does not attach actual
S0 source material or create an S0 reservation/provider attempt. No policy or
mandate was changed, no live source was acquired, and the authorised S0 remains
paused pending a separate recovery decision.
