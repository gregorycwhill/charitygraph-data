# Fundability and Giving Offers design

**Status:** F2-semantic-certified; entering canonical productisation. **Date:** 5 October 2026. **Scope:** prospective Builder/Data architecture only; not public or corpus-complete.

## Decision and archaeology

Existing governed Subjects/Scopes, source/evidence/observation lineage, §8 fundraising/campaign semantics, §13 scoped financial attribution, §14 historical funding/restriction facts, and §20 coverage/freshness are reusable. No current contract represents a donor-facing, time-bounded invitation to accept money for a destination. That seam is genuinely absent. This adds no source acquisition, provider call, release, public schema, v0.5 byte, North Star v0.2, S0 authority, or payment execution.

## Meaning and ownership

A **Giving Offer** is source-evidenced, time-bounded information that an accepting organisation will accept a monetary contribution from a stated or implied audience, possibly for a destination, on stated terms. It is not a Program field, campaign, transaction, successful payment, financial allocation, funding relationship, historical flow, or legal restriction without evidence.

§8 owns offer existence, accepting party, audience, instrument/commitment pattern, designation, terms, action route and currentness. §3 owns destination identity, scope and lifecycle. §13 owns historical expenditure and calculations. §14 owns actual grants/donations and their restrictions. §20 owns coverage/freshness. No projection may propagate a fact across those seams automatically.

An offer has an accepting subject and an independently represented donor-facing destination label. Destination resolution is `resolved`, `candidate`, `ambiguous`, or `unresolved`; only resolved destinations may join governed scope or financial context. VNext scope vocabulary includes `fund` and `appeal` without forcing them to become durable subjects.

## Offer vocabulary

V1 is money-only and preserves unknowns. It supports audiences `public`, `major_donor`, `institutional`, `corporate`, `member`, `unknown`; designation types `unrestricted`, `source_stated_designation`, `source_stated_preference`, `source_reported_restricted`, `contractual_restriction`, `negotiated`, `unknown`; offer state `current`, `historical`, `stale`, `unknown`; and routes `first_party_form`, `official_third_party_form`, `contact_route`, `phone`, `email`, `offline_instruction`, `other`.

Redirection, excess-funds, charity discretion, shared costs/overhead, conditions/minimum/contact requirements and grouped forms (`giving_offer_group_id`) are separate evidence-bound terms. A program selector does not establish legal restriction; `source_reported_restricted` is source-faithful, not legal advice. A third-party route requires official linking evidence and distinguishes an identified-but-unrepresented form from represented controls. Suggested amount is not a minimum; UI prominence/defaults never evidence semantics.

## Missingness, time and coverage

`designation_explicitly_unavailable_observed` is allowed only for direct retained source evidence. A review finding no selector is `not_found_in_reviewed_public_giving_channels`, not inability to fund. Capability coverage is independent for `fundability.giving_offer`, `.designation`, `.terms`, `.action_endpoint`, `.redirection`, and `.shared_costs`; a Donate button is insufficient. Effective, observed, retrieved and decision time remain independently retained; F0/F1 establish no universal TTL.

## Projection and finance boundary

`FundabilityV1` emits atomic evidence-bound §8 candidates: offer, audience, designation availability/unavailability/terms, redirection/excess/shared-cost terms, conditions, commitment pattern and endpoint. Positives carry locator, source record, source role, lineage and time. A bounded reprojection produces only §8 observations.

The future normalized Giving Offer projection and `FundabilityView(destination, audience, instrument, as_of)` are derived reads over these facts. The view may display a known unrestricted parent offer and historical scoped financial context, but never recommends either. A financial `scope_expenditure_share_of_organisation` requires compatible period, currency, reporting scope, attributed numerator/denominator, method/formula and evidence. Historical 15% reports historical expenditure share only: it neither allocates the next unrestricted dollar nor proves a designated gift. Historical §14 restrictions never create present donation availability.

## Fundable Universe and sourcing

The **Fundable Universe** is a parameterized query over governed offers plus explicit coverage: charity/program universe, audience, money instrument and as-of time. It is not a stored master list, recommendation engine, marketplace or checkout. A charity-supplied future manifest would enter ordinary first-party evidence, governance and correction workflow; it has no editorial-control shortcut.

Central source acquisition may represent Donate/Give, Ways to Give, program giving, appeal/campaign, form/FAQ/terms, major-giving, official third-party pages, annual/financial reports and formal gift/fund policies. Section code cannot crawl or parse English; dynamic-form representation is a separately scoped need.

## F2 certification, productisation and next evidence boundary

F0 established typed representation and safety contracts; F1 supplied retained real-evidence review; F2 certified the end-to-end semantic distinctions using bounded official-source review evidence. Certification means the model has been pressure-tested for the stated cases, not that it is public, a stable public schema, corpus-complete, or operationally proven at scale. The retained review packets remain evidence fixtures, not production corpus records or special-case product logic.

The settled internal rules are: fund/appeal may be governed scopes without mandatory durable-subject promotion; an official third-party endpoint is acceptable only with official-link provenance; stale or closed offers remain historical and are excluded from current views; and negotiated/major-donor routes are excluded from default retail views. A Fundable Universe is a parameterised query/projection, never stored master truth or a recommendation that direct program giving is normatively superior to unrestricted giving.

The next bounded operational phase is a **Fundability coverage/acquisition reality slice**, not authorised by this document. Its acceptance bar is evidence for source-discovery recall across a heterogeneous cohort; ordinary and sophisticated donation surfaces; officially linked third-party and simple/offline routes; temporary appeals; dynamic-form gaps; destination-resolution rate; freshness/refresh needs; and explicit production coverage states. It must not execute payment, collect donor data, contact charities, or infer finance. A positive Giving Offer → governed destination → compatible historical-finance join remains deferred evidence unless an existing retained source supplies one; F2's incompatible/unresolved examples correctly abstain.

The next versioned North Star may surface Fundability in §8, with cross-links to §§3/13/14/20, only after representative evidence proof. North Star v0.2 and public v0.5 remain immutable.
