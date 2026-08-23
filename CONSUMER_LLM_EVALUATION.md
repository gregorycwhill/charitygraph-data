# Consumer-LLM evaluation foundation

This package separates four non-interchangeable conditions: unaided discovery,
source discovery, directed CharityGraph use, and supplied-record interpretation.
Each run records product/model/date, account or incognito state, exact prompt,
web/search availability, returned organisations/sources, CharityGraph discovery,
factual/citation correctness, direct-versus-derived interpretation,
period/scope handling and coverage-state handling. An API/web-search proxy is
labelled a proxy, never a consumer-product result.

The initial 16 prompts cover exact-name and ABN lookup, activity/geography,
DGR status, financial periods, EJA direct-share versus mechanical amount,
sparse coverage, DFWA identity ambiguity, legacy-unbound material, and source
retrieval. They deliberately exclude “best charity” correctness targets.

**Current evidence:** no naive consumer-product run has been claimed. Manual
new-session/incognito runs remain required after the static discovery layer is
deployed and indexed.

## Answer-key and capture contract (v1)

The machine-readable prompt foundation is
`golden/distribution-evaluation-v1.json`. Expected answers are scored by
criteria, not exact wording. Every response must be judged for the applicable
combination of correct subject, source, fact, period/scope, claim basis
(direct/mechanical/inferred/estimated), coverage/absence interpretation,
identity ambiguity, provenance/citation and refusal to manufacture an
unavailable fact.

| Prompt | Minimum expected-answer criteria |
| --- | --- |
| exact_lookup | Correct Environmental Justice Australia subject; neutral factual information; source or CharityGraph provenance. |
| abn_lookup | ABN `74052124375`; public source provenance; no name-only identity leap. |
| directed_lookup | Follows CharityGraph canonical subject route and identifies the record/release. |
| financial_interpretation | Separates direct 10% allocation from the mechanically implied approximately AUD 585,279; does not call both direct source amounts. |
| sparse_coverage | Explains `unknown` and `not_available_from_source` as coverage states, not negative facts. |
| identity_ambiguity | Retains DFWA related/former-name ambiguity; does not resolve it by name or domain. |
| legacy_unbound | Identifies `legacy_unbound` as retained historical material, not observed current evidence. |
| period_scope | States the supplied observation's period and scope; does not combine periods. |
| source_retrieval | Follows record/evidence/source links and identifies the supporting source. |
| geography | Finds stated geography only; does not recommend or rank organisations. |
| activity | Returns evidence-backed activity information without ranking or recommendation. |
| dgr | States DGR status with evidence and preserves uncertainty/coverage where present. |
| multiple_periods | Identifies multiple financial periods and the explicit current-selection state. |
| markdown_json | Retrieves both representations for the supplied opaque ID and recognises JSON as richer authority. |
| citation | Cites CharityGraph record/release plus direct evidence; distinguishes direct observation from derivation. |
| charity_information | Gives neutral public information and avoids a “best charity” claim. |

## Four traversal conditions and generic capture form

Use each relevant prompt in one of: **unaided discovery**, **source
discovery**, **directed CharityGraph use**, or **supplied-record interpretation**.
For every run capture product/model/date; new/incognito/account state; exact
prompt; web/search capability; organisations and sources returned; whether
CharityGraph was discovered; the criteria passed/failed; citations; and whether
the failure is discovery/indexing or interpretation. An API or web-search run
is labelled **AUTOMATED PROXY** with model/version/date/web capability, never a
consumer-product result. Do not inject project context into a run labelled
naive.

## Representation-gap protocol

For each directed/supplied test record whether HTML, JSON and Markdown were
sufficient as-is, too thin, unnecessarily verbose, missing epistemic context,
missing provenance or hard for LLM consumption. HTML is being measured as a
discovery projection; JSON remains the rich authority. Do not enrich Viewer
HTML before this comparison demonstrates a need.
