# Knowledge Validation v1

**Status:** deterministic preparation complete; human gate pending. No public semantic release is authorised.

## Scope and safety

This increment validates whether retained Evidence Engine material can become
governed knowledge. It does not publish candidates, alter the immutable
`v0.5.0-2026-08-15` release, rebuild cards, change the taxonomy, change Viewer
content, deploy Viewer, or begin scale work.

The private deterministic packet is produced by Builder
`knowledge_validation.prepare` from the Evidence Engine v1 output and Golden
Corpus v1. It holds exact excerpts and source locations; raw snapshots and the
packet remain private working material.

## Candidate inventory

| Dimension | Result |
| --- | ---: |
| Review-only website candidates | 102 |
| Pilot cases with candidates | 11 |
| Observed domains | activities 32; beneficiaries 43; geography 12; participation 12; programs 3 |
| Source/page role | retained organisation-website snapshot 102; homepage 89; activities page 13 |
| Stability | stable 102; transient 0 |
| Extraction route / basis | deterministic HTML parser v2 102; direct source text 102 |
| Exact/near-duplicate groups | 1 group; 100 unique domain/text pairs |
| No candidate observed | opportunities, self-description, fundraising, identity-sensitive |

All 102 remain unadjudicated direct text, not CharityGraph observations. 39 are
not safely attached to a canonical subject in this review output; that is an
identity review state, not an invitation to resolve by domain or name.

## Governed semantic sample

The generated 48-case sample is deterministic and stratified, not random:
activities 14, beneficiaries 16, geography 10, participation 6 and programs
2. It preserves every available subject, domain, role/stability class and
decision-changing edge class before filling the remaining slots round-robin.
It includes four boilerplate traps, five rhetoric cases, 23
activity/participation boundaries, 16 beneficiary ambiguities, ten geography
ambiguities and two program/organisation boundaries.

Each private review unit contains only: opaque case and subject ID (when
available), domain, exact URL/excerpt/selector, candidate representation,
claim basis, extraction method, freshness/stability, material alternative and
a targeted question. Valid human outcomes are `ACCEPT`, `EDIT`, `REJECT`,
`WRONG_DOMAIN`, `INSUFFICIENT`, `IDENTITY_BLOCKED` and `ADDITIVITY_BLOCKED`.
Anything other than `ACCEPT` needs rationale. Model output cannot create these
labels.

## Automation posture before human review

No overall accuracy score is meaningful here. Every observed domain is
**HUMAN REVIEW** until its own adjudicated precision and provenance evidence is
available. Opportunities, self-description, fundraising semantics and
identity-sensitive observations are **NOT READY** because this web sample has
no candidates in those domains. No domain is auto-promotable; identity and
fundraising inference are never auto-promoted by aggregate accuracy.

No semantic model run has been claimed. The packet records that absence rather
than manufacturing a model result. A future bounded model run must record the
model/version, prompt policy version, evidence hash, structured output and
private cost/latency, and can only be compared with later human decisions.
