# Scale S0 live locator-discovery activation — 2026-09-22

**Principal token:** `CG-S0-PO-LIVE-LOCATOR-2026-09-22`

> **Current-control-plane addendum (2026-09-26):** This is subordinate mechanism authority only. Its ABN-valued population text is immutable compatibility evidence, not current live subject identity. Current authority is `CG-S0-PO-ATTEMPT19-2026-09-26`; governed locator subject refs and explicit ABN lookup identifiers are in `policies/scale-s0/locator-subject-bindings-v1.yaml`. Attempt 19 is allocated but A3-pending and non-executable. `reality_slice1` is deprecated non-canonical development-only code, unreachable from the current live S0 CLI/path.
**Status:** approved additive product-owner decision; ready for publication
**Effective scope:** one future fresh Scale S0 execution attempt only
**Decision date:** 2026-09-22 (Australia/Sydney)

## Decision

The product owner authorises live use of the already-merged, bounded web-locator
discovery mechanism in Scale S0, subject to every existing S0 control. This
decision closes only the live-search authority gap identified by
`SCALE_S0_PRODUCT_OWNER_AUTHORISATIONS_2026-09-22.md`. It is additive and does
not rewrite or supersede the meaning of the 18 September mandate or the
22 September A1–A5 decision.

Live locator discovery is authorised for **Scale S0 only**. It does not authorise
S1+, Top-100 continuation, additional subjects, public release, open-ended
research or broader browsing. The authorised population remains exactly the
eight subject IDs and population hash in
`SCALE_S0_MANDATE_AUTHORISED_V2.yaml`:

`28004778081`, `28000030179`, `74068758654`, `37646526132`,
`50169561394`, `47613674461`, `78053639115`, `61002643852`;
population hash `45110269021C495B4970F310D093297A11413DD36F5F0B03B291AC6883F62D8D`.

The existing provider boundaries remain unchanged: total provider spend is at
most USD 8.00, strong-model spend is at most USD 4.00, provider calls are at
most 150, and each durable reservation is at most USD 0.25. Public release
remains prohibited.

## Authorised discovery contract

The mechanism is exactly the implementation merged by Builder PR #89 and Data
PR #43, and no variant is authorised:

- no more than 5 search queries per subject;
- no more than 10 considered search results per query;
- no more than 5 authenticated locator fetches per subject; and
- early stop after sufficient authenticated useful sources are acquired.

Search results, snippets, citations, rankings and provider source metadata are
discovery metadata only. They cannot become CardEvidence, frozen-corpus
evidence, source facts, observations, candidates or semantic support. Only
separately authenticated and governed acquisition of the underlying source may
supply evidence.

Identity authentication remains exactly as governed by the 22 September
decision: one exact ABN/ACN/ACNC identifier or authoritative regulator/source
locator link is sufficient; otherwise two independent structured soft anchors
are required. Name-only matches are insufficient. Platform hosting does not
itself disqualify an official source. Authentication identifies the
organisation speaking and does not elevate first-party evidentiary reliability.

Benign HTTP-to-HTTPS and www-to-apex canonicalisation remains permitted and
must be recorded. Cross-host redirects require independent authentication. No
authentication, paywall, TLS-validation or anti-bot bypass is authorised.

Concrete source identity remains `source_family + subject_abn +
canonical_locator`. AIS local-use/provider-transmission distinctions remain
unchanged. Missing `discovery_signals` production mapping remains explicit
nonblocking missingness. Technical withholding remains `not_acquired`, never
substantive absence.

## Existing controls remain mandatory

Locator-search provider calls use the existing S0 provider accounting,
reservation, exactly-once and halt machinery. They consume the existing S0
provider-call and budget ceilings; this decision creates no additional budget
or call allowance.

Every provider crossing, including locator search, remains subject to A3:
`Share inputs and outputs with OpenAI = Disabled`; human attestation by Greg;
matching account/project and S0 authority; and validity for less than 60
minutes. Expiry or any relevant setting, account or project change requires a
fresh attestation. No A3 attestation is supplied or implied by this
documentation tranche.

Existing A1/A2/A4/A5 rules remain unchanged. This decision does not waive
source-rights, provider-processing, budget, reservation, review, promotion,
halt, execution-identity or public-release controls.

## Attempt identity and non-execution boundary

Attempt 8 is immutable historical execution evidence and remains read-only; it
must not be resumed or mutated. The next live execution must use a fresh
attempt identity. That fresh attempt must bind to the exact canonical Builder
and Data `main` SHAs that exist after this authority change is published and
merged. No post-merge SHA is implied or pre-authorised by this record.

This decision authorises live use of the bounded locator-discovery mechanism
inside an otherwise-valid fresh S0 attempt. It does not itself execute S0,
acquire a charity source, make a provider/model/API call, create an A3
attestation or provider reservation, generate candidates, promote anything,
mutate Attempt 8 or immutable public v0.5, or publish a release.

## Authority relationship and provenance

The 18 September `SCALE_S0_AUTHORISATION_DECISION_2026-09-18.md` and
`SCALE_S0_MANDATE_AUTHORISED_V2.yaml` remain the controlling S0 mandate and
frozen cohort/policy bytes. The 22 September
`SCALE_S0_PRODUCT_OWNER_AUTHORISATIONS_2026-09-22.md` remains the controlling
A1–A5 operating-policy decision. This record is a narrow additive activation
layer: it changes only the status of the already-merged bounded locator
discovery from implementation/fixture-only to live-use-authorised within S0,
while preserving all other boundaries.

The authority change starts from canonical Data `main` SHA
`5cc5e9d1d10686755e76f4471fd067f84b6469f0` and the then-canonical Builder
`main` SHA `86d6a717099b499314ed019c41ad53d18d39e559`; the future execution
identity must use the exact post-merge canonical SHAs, not these starting-state
references unless they remain the canonical post-merge values.
