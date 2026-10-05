# F2 Fundability reality slice 299

**Status:** local, review-only experimental evidence packet, assessed 2026-10-05
(Australia/Sydney).  It is neither a public contract nor a recommendation, payment
instruction, legal/tax conclusion, allocation promise, or a record of a completed
donation.  No form was submitted and no personal data was supplied.

## Lineage and bounded cohort

This continues the approved F0/F1 contract and packet 296.  The fixed cohort is four
Australian accepting charities/appeal operators.  `src:299:*` and `lineage:299:*`
identify review targets and retained-evidence slots; they do not claim that hidden
payment controls were acquired.  Source text was reviewed on the assessment date;
source bytes are excluded from Git under the Builder rules.

| ID | organisation / identifier | official locator and role | compact observed evidence | currentness |
|---|---|---|---|---|
| OX-01 | Oxfam Australia, ABN 18 055 208 636 | first-party appeal, https://www.oxfam.org.au/ways-to-donate/our-appeals/gaza-palestinian-crisis/ | “Funds raised from this appeal will support Oxfam's Middle East crisis response, including Gaza, the West Bank and Lebanon”; public Give once/Give regularly action. | current page, reviewed 2026-10-05 |
| OX-02 | Oxfam Australia, ABN 18 055 208 636 | first-party policy, https://www.oxfam.org.au/our-impact/where-the-money-goes/ | emergency appeals: at least 90% to emergency-response programs; remaining 10% covers specified promotion, phone-room, processing, receipting, audit and accountability costs. | current page, reviewed 2026-10-05 |
| OX-03 | Oxfam Australia, ABN 18 055 208 636 | first-party impact/annual-report landing page, https://www.oxfam.org.au/our-impact/ | 2024–25: $39.5m+ invested in programs; page also presents 67c per dollar spent on life-changing work. | annual context, not appeal finance |
| ARC-01 | Australian Red Cross Society | first-party appeal, https://www.redcross.org.au/middleeastcrisisappeal/ | public appeal says donations help emergency relief and longer-term humanitarian support; excess/changed-circumstance funds go to international-crises work; up to 10% supports core operating costs. | current page, reviewed 2026-10-05 |
| WV-01 | World Vision Australia | first-party FAQ, https://www.worldvision.com.au/child-sponsorship-faqs | sponsorship donations are pooled with other sponsors/donors for community projects; “where it’s most needed” is available through phone/chat. | current at packet-296 review; effective date not stated |
| CC-01/02/04 | Cancer Council NSW, ABN 51 116 463 846 | first-party giving/appeal/historic-report locators retained in packet 296 | general giving, a 2025 appeal presentation, major-gift pillars over $5,000, and a 2016/17 historical route. | as classified in packet 296 |

## Governed resolution and atomic review

The following is an experimental governed §3 resolution, not a claim that the appeal
is a separately incorporated organisation or every underlying program.  Source scope
and destination are the same named appeal-response scope only because OX-01 states
both its accepting organisation and the response/geographic envelope.

| governed scope ID | §3 kind and label | resolution decision | support / boundary |
|---|---|---|---|
| `scope:299:oxfam-middle-east-crisis-response` | appeal — Oxfam Middle East crisis response (Gaza, West Bank and Lebanon) | **resolved** to OX-01 donor label “Gaza / Palestinian crisis appeal” | it is an appeal scope accepted by Oxfam Australia and includes, rather than equals, particular country activities; it is not promoted to an individual program, partner, legal restriction, or one-to-one allocation |
| `scope:299:arc-middle-east-crisis-appeal` | appeal — Australian Red Cross Middle East Crisis Appeal | candidate | evidence supports donor-facing appeal semantics, but no separate §3 identity adjudication in this bounded packet; finance join blocked |
| `Child Sponsorship`, CC general donation, CC research labels | labels / parent or program presentation | unresolved | retain packet-296 disposition; no §13 join |

| offer atom | disposition | material terms and coverage |
|---|---|---|
| OX-01 public current Giving Offer to resolved Oxfam appeal scope | **positive, public, source-stated designation** | designation is source-stated purpose, not a legal restriction.  Current public once/regular action is represented as a first-party form without submission. |
| OX-01 redirection/excess terms | **conditional, supported** | if funds exceed need or cannot be used (including government restrictions), Oxfam directs them to its International Crisis Fund. |
| OX-02 shared-cost terms | **supported, contextual** | at least 90% of emergency-appeal funds to program/humanitarian work; stated 10% categories are appeal-support/administration costs.  This is not a promise about one donor’s marginal dollar. |
| OX-03 finance join attempt | **incompatible / unknown** | organisation-year program investment and organisation-wide spend ratio lack appeal-specific numerator/denominator and allocation grain.  No share is imputed or joined to the OX-01 appeal. |
| ARC-01 public Middle East Crisis Appeal | **supported, conditional** | current appeal, explicit redirection/excess and “up to 10%” core-operating-cost statement.  Scope remains candidate, so finance is blocked. |
| WV-01 sponsorship / parent route | **supported, unresolved** | pooled sponsorship; named-child presentation is not unique allocation.  Phone/chat route is a simple right-tail route, not an online payment instruction. |
| CC-02 pillars over $5,000 | **supported, major-donor only** | negotiated choice only; excluded from the default retail projection. |
| CC research retail selector | **not found** | absence in reviewed retail channels is not explicit unavailability. |
| CC-04 historic route | **stale** | excluded from current results. |

No source in this bounded cohort explicitly stated that a **money** designation is
unavailable.  The explicit ARC statement declining in-kind goods is recorded only as
a resource-type boundary, not falsely converted into an explicit-negative money
designation.  `explicitly_unavailable` therefore remains unobserved rather than
manufactured.

## Review-only mini Fundable Universe

This is a parameterised projection over the above evidence and coverage states, not a
stored master list, recommendation, or ranking.  Default retail excludes
`major_donor`; historical/stale is visible only in review mode.

| accepting charity | destination / resolution | retail designation / audience | terms, route and freshness | finance / coverage |
|---|---|---|---|---|
| Oxfam Australia | Oxfam Middle East crisis response / **resolved appeal scope** | source-stated designation; public | first-party once/regular form; excess/blocked-use → International Crisis Fund; current | attempted but incompatible organisation-level annual context; share unknown; supported |
| Australian Red Cross | Middle East Crisis Appeal / candidate | source-stated purpose; public | first-party form; excess/changed circumstances → international crises; up to 10% core costs; current | blocked: unresolved scope; supported / conditional |
| World Vision Australia | Child Sponsorship / unresolved | pooled sponsorship preference; public | recurring; pooled community arrangement; current | no join; supported |
| World Vision Australia | Where it’s most needed / unresolved | unrestricted parent giving; public | phone/chat setup; current | no join; supported simple route |
| Cancer Council NSW | Cancer Research / unresolved | designation unknown; public | no ordinary selector observed in reviewed channels | no join; **not_found** |
| Cancer Council NSW | named pillars / unresolved | negotiated; **major donor** | contact route and >$5,000 condition; current | no join; supported, excluded from retail |
| Cancer Council NSW | 2016/17 Breakthrough / unresolved | historic only; public | historical report | no join; **stale** |

## Adversarial review and decision

The review rejected each of: program = fundable destination; donor wording = legal
restriction; appeal = every underlying program; a visible donate action = unique
allocation; historical expenditure/share = marginal allocation; absence = explicit
negative; and a major-gift route = retail availability.  Resolved scope is required
before finance; all unresolved rows are blocked.  Oxfam’s emergency offer is current
but its currentness is page-review evidence, not an asserted page publication date.

Evidence proven: a current, public direct-designation offer to a governed appeal
scope; humanitarian forcing case; official endpoint; redirection/excess and
shared-cost treatment; right-tail route; major-donor retail exclusion; a scoped
finance-join attempt with unknown outcome; and negative/not-found, unknown,
conditional, and stale coverage.  Evidence not proven: an appeal-specific historical
expenditure share, a money-designation explicit-negative, a separately governed ARC
scope, and a current appeal-specific offline payment instruction.

Product recommendation: publish current offers nested under accepting charities with
destination-first traversal; reserve “directly fundable” for a current observed public
endpoint plus source-stated designation and governed destination; retain fund/appeal
as scopes rather than promoting them to organisations; label official third-party
routes distinctly; refresh active disaster pages rapidly; keep major gifts outside
retail defaults; and accept future charity manifests only as evidence pending review.

**Decision: `ADVANCE_WITH_BOUNDED_FIX`.**  The core end-to-end representation proof
is achieved.  Before productisation, add a separate deliberately acquired,
source-explicit money-designation-unavailable example (if such evidence is needed for
UI testing) and rerun currentness review; neither gap authorises inference.
