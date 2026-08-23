# RC4 final Viewer/editorial integration review handoff

> **Authority status:** Historical review handoff. The recorded local staging paths and legacy product name are provenance, not active instructions.

Status: locally validated candidate; not human-approved, committed, pushed or deployed.

Candidate: `C:\CauseBase-runtime\staging\phase2b-2026-08-14-rc4-final-viewer-editorial-integration`

Isolated Viewer bundle: `C:\CauseBase-runtime\staging\viewer-rc4-final-viewer-editorial-integration`

## Evidence outcomes

- Scope remains the existing 120 cards, projected from immutable `phase2a-2026-08-10-h1`. Accepted RC2 summaries are reused only when their cited evidence remains present; no model calls or embedding regeneration occurred.
- Participation has separate action-destination semantics. A participation item is clickable only when it has a valid absolute external `action_url`; report/evidence URLs are not reused as actions. The reference card has zero action URLs, so its Participation entries are evidence-cited text rather than unreliable links.
- Financials now lead with **Funding & fundraising**, ahead of **Financial reports**. The reference card displays source-labelled revenue rows and conservative derived shares over reported total income. Its printed mixed row remains `Donations, Fundraisings, Lectures`: AUD `2,051,817`, `40.9% of Total income`; it is not relabelled as individual donations.
- The reference card displays its directly reported `Fundraising` functional allocation as `10% (direct reported)`. Its mechanically derived amount is presented as `Approx. $585k`, not as a falsely precise reported figure. Functional allocations remain separate from statutory expense rows.
- Full source-preserved statements remain available: EJA has 33 Profit & loss rows and 32 financial-position rows, with source labels, order, totals, comparatives and optional canonical annotations.
- Statement and functional-allocation tables use table-level citations where all rows share one evidence source; row-level citations remain available for mixed provenance.
- The redundant `External links & developer data` section is removed. The bottom **Sources & data** section retains source-native records, references, JSON and Markdown.
- The bounded human-reviewed structured-value remediation records 40 before/after outcomes: 38 provenance-only cleanups (A) and two field-restructuring omissions (C). Its private audit is `structured-provenance-review.json` beside the candidate; it reports zero unexplained routine residues.

## Automated evidence

- Builder: 63 passing tests.
- Viewer: 17 passing tests.
- Candidate publication validation: passed (120 cards).
- Static Viewer bundle preparation: passed.
- Source-native static-link check: passed (228 rendered source-native links returned 200).
- Participation action-URL check: passed; zero action URLs in this candidate are therefore rendered as action links.

## Required human gate

Review the reference card in the isolated bundle. Confirm the accepted RC2 summary, non-clickable evidence-only Participation entries, Funding & fundraising before Financial reports, source-labelled revenue shares, prominent `Fundraising 10%` with `Approx. $585k`, complete primary statements, table-level citations, and Sources & data access.

The handoff does not authorise deployment.
