# Scale S0 product-owner authorisations — 2026-09-22

**Decision ID:** `CG-S0-PO-2026-09-22`
**Status:** approved bounded operating policy
**Effective date:** 2026-09-22 (Australia/Melbourne)
**Scope:** Scale S0 only; the authorised eight-subject cohort, budget and public-release boundary are unchanged.

This decision supersedes only conflicting S0 operating details in earlier
authorisation/calibration material. It does not reopen the completed Phase 5
North Star, authorise S1+, or alter public contract 0.5. Public release remains
prohibited.

## Authorisations

1. `official_first_party_web` concrete immutable source identity is the tuple
   `source_family + subject_abn + canonical_locator`. A canonical locator is the
   canonical URL or host materially identifying the acquired source. A different
   ABN or materially different locator receives a distinct definition; an
   existing materially different definition is never mutated.
2. An ACNC AIS resource may be locally acquired, retained and deterministically
   processed only with unambiguous ACNC/data.gov.au provenance, exact
   dataset/resource and version binding, and a content hash. Explicit compatible,
   blank, and `NOTSPECIFIED` licence metadata pass this local-use boundary.
   `local_acquisition=true`, `local_retention=true`,
   `local_deterministic_processing=true`, `provider_transmission=false`,
   `public_release=false`, `exact_resource_binding=required`, and
   `attribution/provenance=required`. Missing resource-level licence metadata is
   not a local-processing veto; it remains a provider-transmission restriction.
3. A human attestation that `Share inputs and outputs with OpenAI = Disabled`
   authorises otherwise-valid S0 sends for exactly 24 hours from `observed_at`
   only when
   `attested_by=Greg`, account/project and S0 execution authority match, and the
   setting is unchanged. Expiry, observed/suspected setting change, or account/
   project change requires a fresh attestation. It is never inferred or
   fabricated; packet, rights, budget, reservation and exactly-once controls
   still apply. This does not rewrite historical campaign evidence.
4. `discovery_signals_mapper_required_for_slice_progress=false`. A missing
   production mapper is explicit nonblocking implementation/coverage missingness,
   not semantic absence. `invent_mapping=false`, `infer_taxonomy_mapping=false`,
   `semantic_absence=false`, and `public_promotion=false`.
5. If an initial first-party locator is unavailable, an alternate may be used
   only with recorded authoritative relationship evidence from the ACNC Register,
   the organisation's reached domain/navigation, an officially linked document/
   subdomain, or another S0-permitted authoritative registry/source. Maximum
   locator probes per subject is five. Redirects and alternate official hosts are
   permitted. Authentication, paywall, TLS-validation and anti-bot bypasses are
   prohibited. Technical withholding means `not_acquired`, never substantive
   absence.

## Accepted S0 web-locator discovery repair

Registry locators are seeds, not an authoritative limit on discovery.  Builder
MAY search for plausible current public locators using only already-authorised
public entity identity (best available legal/trading name, ABN and other
governed identity anchors), through a provider-neutral locator-search boundary.
Discovery is bounded to no more than five queries, ten considered results per
query and five authenticated locator fetches per subject, with early stopping
after sufficient authenticated useful sources are acquired.

Search results, snippets, citations and provider source metadata are discovery
metadata only.  They MUST NOT become CardEvidence, source facts, frozen-corpus
evidence, candidate observations or semantic claim support.  Only a separately
governed acquisition of the underlying locator may supply evidence.  Durable
lineage records subject, query, provider/search-call identity, returned URL and
available title/snippet/source metadata/rank, anchors, authentication decision
and reason, final locator, redirect chain and later acquisition linkage.

Official owned domains and plausible official social, community, charity and
sector-platform pages are candidates; platform hosting is not a disqualifier.
Authentication is high-recall but bounded: one exact ABN/ACN/ACNC identifier or
an authoritative regulator/source locator link is sufficient; otherwise two
independent structured soft anchors (name, address/location, officer, contact,
program, authenticated cross-link or comparably specific governed material) are
required.  A collision-prone name-only match is insufficient.  Authentication
identifies the organisation speaking; it does not elevate reliability beyond
ordinary first-party/self-reported treatment.

HTTP-to-HTTPS and www-to-apex canonicalisation are accepted and recorded.  A
different final host requires independent authentication under the same rule.
Authentication, paywall, TLS-validation and anti-bot bypasses remain prohibited.
Concrete first-party source definitions remain immutable and use
`source_family + subject_abn + canonical_locator`; materially different existing
records are never mutated.  `discovery_signals` remains explicit nonblocking
implementation missingness; this decision does not introduce a mapper.

The existing AIS A2 local-use restriction and A3 identity, scope, authority,
send-start, one-crossing, reservation, accounting, and restart controls are
unchanged. The 2026-09-26 Product Owner decision supersedes the prior S0 A3
60-minute duration: a valid Greg-observed disabled-setting attestation expires
exactly 24 hours after `observed_at`, with all existing fail-closed invalidators
remaining in force. Locator-search provider calls use the existing provider accounting,
reservation, attestation and exactly-once controls rather than a side channel.
This repair authorises implementation and fixture testing only: it does not
authorise live search, website acquisition, provider inference, attestation,
public release or alteration of immutable Attempt 8 execution evidence.

## Attempt identity

This subsection records the state at initial A1–A5 approval:
`attempt:s0:7` / `run:s0:attempt-7` was immutable historical execution evidence
bound to Builder `d4dd962aac2630c48310a89551a03dfa7caf8f7a` and Data
`70e273fa3bdf25188ea4e4ef4959a8def7500bf4`. It must not be mutated or resumed.
The later immutable Attempt 8 execution and its exact evidence binding are
recorded in the additive
`SCALE_S0_ATTEMPT8_IDENTITY_RECONCILIATION_2026-09-22.md`; that record is the
current/latest execution-history authority for Attempt 8 and supersedes only
the temporal implication here that Attempt 7 remains latest. Any next live
execution after locator activation is canonical must use a fresh Attempt 9
identity. It may reuse source bytes/evidence only where the canonical
content-addressed lifecycle permits reuse without falsifying acquisition
lineage.

No live charity-evidence acquisition, provider/model call, provider reservation,
owner attestation, or public release is authorised by this implementation tranche.

The durable A3 window/invalidation ledger is an additive Builder migration 23;
immutable migration 22 and all historical Attempt 7 records remain unchanged.
