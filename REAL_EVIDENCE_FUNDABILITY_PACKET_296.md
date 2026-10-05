# Bounded real-evidence Fundability packet 296

**Review status:** local, review-only evidence packet.  It is not a public contract,
recommendation, payment instruction, legal conclusion, or a claim about allocation of
the next unrestricted dollar.  Acquired/reviewed 2026-10-05 (Australia/Sydney) from
the named public official pages.  No forms were submitted.

## Cohort and source lineage

| ID | accepting organisation / identifier | source role and retained locator | reviewed evidence (short locator/quote) | observed currentness |
|---|---|---|---|---|
| WV-01 | World Vision Australia (ABN unresolved in this bounded packet) | first-party; `https://www.worldvision.com.au/child-sponsorship-faqs` | FAQ says sponsorship is $48/month and that regular sponsorship donations are pooled with other sponsors/donors; it also offers a donation "where it’s most needed" through phone/chat. | page current at review; effective date not stated |
| CC-01 | The Cancer Council NSW, ABN 51 116 463 846 | first-party; `https://www.cancercouncil.com.au/ways-to-donate/` | public page exposes regular giving and a Major gifts contact route. | page current at review; effective date not stated |
| CC-02 | The Cancer Council NSW, ABN 51 116 463 846 | first-party fundraising page; `https://give.cancercouncil.com.au/eofy` | public page says gifts over $5,000 may choose one of three pillars; it directs direct-deposit donors to contact staff. | current page at review; campaign label is time-bounded/unknown |
| CC-03 | The Cancer Council NSW, ABN 51 116 463 846 | first-party annual-highlight report; `https://www.cancercouncil.com.au/wp-content/uploads/2024/11/Cancer-Council-NSW-Annual-Highlights-Report-2023-24-Final.pdf` | report describes 2023/24 regular-giver revenue and long-term research/support commitments. | historical financial context (2023/24), not offer evidence |
| CC-04 | The Cancer Council NSW, ABN 51 116 463 846 | first-party 2016/17 annual report; `https://www.cancercouncil.com.au/wp-content/uploads/2023/06/Annual-Report-2016-2017-Cancer-Council-NSW.pdf` | historic regular-giving wording and donation URL. | historical/stale; must not be rendered as a current offer |

`source_record_id` convention in the Builder fixture is `src:296:<ID>`;
`lineage_id` is `lineage:296:<ID>`; each evidence locator is the canonical URL plus
an in-page heading.  These identifiers identify a retained-review target, not a claim
that the renderer acquired hidden form controls.  Dynamic payment forms were not
interacted with and their hidden selector semantics are deliberately not inferred.

## Human adjudication: atomic outcomes

| organisation | donor-facing destination / resolution | retail designation state and offer pattern | terms/caveats | route/audience | coverage |
|---|---|---|---|---|---|
| World Vision Australia | `Child Sponsorship` — **unresolved** destination identity | a current observed sponsorship commitment; not a direct individual-child allocation | source expressly says contributions are pooled and used for community projects; a named child is relational presentation, not evidence of unique allocation | public, first-party; recurring $48/month | supported offer; no finance join |
| World Vision Australia | `Where it’s most needed` — **unresolved** parent destination | current observed unrestricted/parent gift option | broad range of work; set-up stated as phone/chat rather than a represented public form | public contact route | supported offer; no inferred restriction |
| Cancer Council NSW | `Cancer Council NSW general donation` — **unresolved** parent destination | current public pooled give-once/regular giving; programs mentioned in copy are not selector evidence | supports research, prevention, advocacy and information/support; no source evidence that a retail donor selects one | public, first-party donation surface | supported offer; known program labels have **not_found_in_reviewed_public_giving_channels**, not explicit unavailability |
| Cancer Council NSW | `Cancer Research Awards 2025` — **unresolved** appeal destination | current observed appeal-linked retail donation surface | source headline names awards but generic FAQ continues to describe pooled organisation programs; legal restriction and ultimate allocation are unknown | public, first-party payment surface (not submitted) | supported offer with designation **unknown**, not a proven direct research allocation |
| Cancer Council NSW | `Cancer Prevention and Advocacy`, `Cancer Information and Support`, `Cancer Research` — **unresolved** three destination labels | no ordinary retail selector proven; explicit choice is stated only for gifts over $5,000 | source says a major donor can choose one of three pillars; scope/terms beyond that are unobserved | major-donor / contact route, negotiated | supported negotiated opportunity; not a default retail offer |
| Cancer Council NSW | 2016/17 Breakthrough regular giving | historic source only | historic source has no currentness proof | historical/stale page/report | stale: excluded from current Fundable Universe |

## Finance context and non-joins

CC-03 reports **regular-giver revenue**, not a program expenditure numerator and total
expenditure denominator at compatible entity/period/grain.  It is therefore retained
as fundraising/finance context only: program expenditure share is **unknown**.  No
historical share is calculated or rendered as marginal allocation of a new unrestricted
gift.  All donor-facing destination labels in this bounded packet remain unresolved
against governed §3 scope identity; consequently none may join to §13 finance.

## Review-only mini Fundable Universe projection

Traversal can be read both ways: a donor destination row identifies an accepting
organisation; each organisation’s rows enumerate observed offers and coverage states.

| accepting charity | destination/source label | kind / identity | public designation | audience / route | freshness | financial context | evidence / coverage |
|---|---|---|---|---|---|---|---|
| World Vision Australia | Child Sponsorship | sponsorship; unresolved | source-stated pooled commitment, not individual allocation | public / first-party | current observed | unknown | WV-01 / supported |
| World Vision Australia | Where it’s most needed | parent unrestricted; unresolved | unrestricted parent giving | public / contact route | current observed | unknown | WV-01 / supported |
| Cancer Council NSW | General donation | parent unrestricted; unresolved | generic pooled giving; program selection not proven | public / first-party | current observed | unknown | CC-01 / supported |
| Cancer Council NSW | Cancer Research Awards 2025 | appeal; unresolved | appeal presentation; direct designation unknown | public / first-party | current observed, campaign effective date unknown | unknown | CC-02 / supported |
| Cancer Council NSW | Cancer Research (retail) | program label; unresolved | no selector found in reviewed retail channels | public / — | current review | unknown | CC-01/02 / not_found_in_reviewed_public_giving_channels |
| Cancer Council NSW | three named pillars | labels; unresolved | negotiated choice only | major donor / contact route | current observed | unknown | CC-02 / supported |
| Cancer Council NSW | 2016/17 Breakthrough | historical giving program | not current evidence | public / historical URL | stale | historical only | CC-04 / stale |

## Adversarial findings and product-owner recommendations

No semantic conflation was accepted: program names were not promoted to fundable
destinations; a form/appeal was not promoted to a legal restriction; a named sponsored
child was not treated as unique allocation; historical material was excluded; absence
was not converted to explicit unavailability; and no finance join/allocation inference
was made.  No bounded code defect was found in this packet.

Recommend: keep funds/appeals as §3 scopes only when separately governed; show offers
nested beneath a charity by default but permit destination-first traversal; reserve
"directly fundable" for an observed current public action endpoint plus a source-stated
designation (not merely persuasive copy); allow official third-party forms only with
explicit linkage; show stale/closed offers as excluded historical evidence; use short
refresh windows for active-disaster pages; define a future charity-submitted manifest as
evidence subject to verification; and keep negotiated major-gift opportunities out of
default retail views while allowing a clearly labelled optional view.

## Decision

**ADVANCE_TO_F2 (proposal only).** This bounded proof supplies two real organisations
and materially different public, pooled, appeal, negotiated, and historical patterns.
F2 should use a small cohort, official acquisition only, direct/official-third-party
routing, manual evidence review, fixed cost cap, stop on representation or identity
failure, and success criteria requiring positive plus negative/unknown coverage without
finance imputation.  It must not execute payment, contact charities, or activate S0.
