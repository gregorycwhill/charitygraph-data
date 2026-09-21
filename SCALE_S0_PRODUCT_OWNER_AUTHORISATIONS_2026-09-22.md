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
   authorises otherwise-valid S0 sends for less than 60 minutes only when
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

## Attempt identity

`attempt:s0:7` / `run:s0:attempt-7` is immutable historical execution evidence
bound to Builder `d4dd962aac2630c48310a89551a03dfa7caf8f7a` and Data
`70e273fa3bdf25188ea4e4ef4959a8def7500bf4`. It must not be mutated or resumed.
The first post-merge execution must use a fresh attempt identity bound to the
new Builder and Data SHAs. It may reuse source bytes/evidence only where the
canonical content-addressed lifecycle permits reuse without falsifying
acquisition lineage.

No live charity-evidence acquisition, provider/model call, provider reservation,
owner attestation, or public release is authorised by this implementation tranche.
