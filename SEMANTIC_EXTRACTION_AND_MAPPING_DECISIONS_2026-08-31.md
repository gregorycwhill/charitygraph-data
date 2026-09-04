# Semantic extraction and mapping decisions — 2026-08-31

**Status:** Approved decision — propagation tranche
**Scope:** Complete-card semantic extraction, independent taxonomy mapping and
model-economics direction
**Authority:** Subordinate to the canonical product, principles, integrated
model, source governance and taxonomy governance documents.

This record consolidates the complete-card and downstream semantic experiments
through Builder PR #35. It records architecture direction and empirical
rationale; it does not change immutable public release 0.5, create model-
performance guarantees, publish private CLASSIE material or approve a hosted
inference product.

## Experimental sequence

The evidence base comprises: the Fred whole-card Terra/Luna comparison; the ACF
clean Terra/Luna comparison; World Vision Luna whole-card v0.2, Luna SDG v0.3
and Terra SDG review v0.4; Tweed sparse whole-card, CharityGraph CLASSIE and
private Terra review v0.5-v0.5.3; and Local Buying Foundation website-led
whole-card and CharityGraph CLASSIE v0.6, including the corrected
scope/blindness v0.6.1 run. These were bounded private experiments, not public
release certification.

## Empirical findings

- Complete-card extraction produced useful evidence-linked knowledge across
  rich, sparse-regulator and modest-website evidence shapes, but output remains
  a governed experiment result rather than canonical truth.
- Representation defects can masquerade as semantic sparsity; structured
  projections and explicit representation gaps are therefore necessary.
- Shared official domains expose entity/activity-role ambiguity. Funding,
  operation, delivery, sponsorship, partnership, auspice and network context
  cannot safely be collapsed.
- Independent taxonomy calls must not receive source-reported taxonomy fields
  or prior assignments. Post-hoc comparison is informative but not ground truth.
- Reviewed taxonomy experiments primarily narrowed or rejected over-broad
  candidates and found no strongly supported omission in those bounded cases.
- Exact batch sizes, QA percentages, elapsed-time estimates and stronger-model
  superiority were not established as universal facts.

## Empirical anchors

The following bounded experiment measurements support the decisions above.
They are non-sensitive aggregates, are not performance guarantees, and should
not be read as release acceptance thresholds.

| Experiment | Aggregate observation |
|---|---|
| ACF Terra/Luna whole-card | Luna 55 observations versus Terra 26; approximate cost USD 0.035 versus USD 0.252 |
| World Vision whole-card | Luna 71 observations across all 20 sections; approximate cost USD 0.040 |
| World Vision SDG Terra review | 21 Luna candidates reviewed: 9 accept, 8 narrow, 4 reject, 0 strongly supported omissions |
| Tweed representation comparison | Defective representation: 12 observations across 3 sections; corrected representation: 64 observations across 17 sections |
| Tweed CG CLASSIE Terra review | 5 candidates: 3 accept, 1 narrow, 1 reject, 0 strongly supported omissions |
| Local Buying v0.6 | 99 observations across 19 sections: 71 website-only, 26 regulator-only, 2 mixed |
| Local Buying v0.6.1 | Clean, scope-corrected CG CLASSIE: 26 assignments versus 50 in contaminated v0.6 |

Controlled taxonomy labels, definitions and assignment identities are omitted;
these figures describe experiment shape and economics only.

## Approved architecture decisions

1. **Whole-card knowledge:** use evidence -> reusable representation -> high-
   recall governed semantic knowledge -> independently governed downstream
   tasks. Seek every supported proposition in the governed Target Card; do not
   delegate product materiality to the model. Recall is upstream; compression
   and synthesis are downstream. A response is not a stored mega-card.
2. **Model tiering:** use the lowest-cost demonstrated adequate tier for
   routine production. Stronger tiers are assurance, arbitration, sampling and
   difficult-boundary resources. Current implementation direction is a
   low-cost primary producer with sampled/risk-triggered stronger assurance;
   named routing is not a permanent product promise.
3. **Representation integrity:** acquisition, representation and semantic
   interpretation are separate. OCR/layout recovery is representation. No
   substantive source may silently become a placeholder or severe truncation;
   gaps are explicit states.
4. **Sparse evidence:** sparse evidence yields sparse knowledge. It never
   lowers evidentiary standards or authorises outside-knowledge completion.
5. **Official websites:** bounded first-party website acquisition is part of
   the normal baseline when an official site exists and may lawfully be
   acquired. Structural discovery is mechanical; page relevance is
   model-assisted. Website claims are strategically authored evidence, not
   independent verification.
6. **Provenance and ownership:** domain provenance does not establish
   proposition ownership. Attach assertions to the lowest evidence-supported
   subject or scope; shared networks and auspiced arrangements remain explicit.
7. **Activity role:** operating, delivering, funding, sponsoring, partnering,
   auspicing and network/context roles remain distinct. Expose structured role
   semantics rather than interpreting free-text labels in downstream Python.
8. **Knowledge-layer mappings:** downstream semantic lenses normally consume
   governed CharityGraph observations, not raw source documents. Evidence
   remains reachable through lineage.
9. **Taxonomy blindness:** independent inferred schemes use task-specific
   blind views excluding source-reported classifications, prior assignments and
   unrelated schemes where they would contaminate inference. Preserve source-
   native classifications separately and compare only after inference.
10. **Mechanical invariants:** Builder supplies task identity, scheme/version
    and other known invariants mechanically; models need not regenerate them.
11. **Mapping object:** target/scope -> scheme concept -> supporting governed
    observations -> qualifications is the durable mapping. Explanatory prose is
    downstream synthesis, not assignment identity.
12. **ACNC versus CharityGraph CLASSIE:** ACNC CLASSIE is source-reported;
    CharityGraph CLASSIE is independent. ACNC is withheld from CG inference and
    may be compared post-hoc only. Existing private-processing and publication
    permission rules remain unchanged.
13. **UN SDG:** SDG is a downstream alignment lens over CharityGraph knowledge,
    preferably at program/service grain. It is not impact measurement or UN
    endorsement.
14. **CharityGraph Native:** induce Native concepts bottom-up from a broad,
    taxonomy-blind corpus of evidence-linked observations. External taxonomy
    assignments, prior Native assignments and raw sources are excluded.
    Low-cost models may discover/attach provisional concepts; stronger tending
    may merge, split, reparent, rename, redefine, retain or deprecate them.
    Cadence remains empirical.
15. **Embeddings:** embeddings are versioned retrieval/similarity aids. They
    propose candidates but do not establish evidence, assignments or Native
    truth.
16. **Economics and scale:** optimise semantic yield per cost. Use economical
    provider modes, concurrency, cache/reuse, resumable waves and staged QA
    where appropriate. Scale gradually with threshold-triggered spot testing;
    do not canonise exact batch sizes or timing estimates.
17. **Reviewer value:** current evidence supports primary high-recall mapping
    with sampled/risk-triggered stronger-model assurance, not universal double
    inference. This is an implementation hypothesis, not a quality guarantee.

## Implementation direction

Native induction and promotion are governed by [CHARITYGRAPH_NATIVE_ARCHITECTURE.md](CHARITYGRAPH_NATIVE_ARCHITECTURE.md); the V1–V3 experiments do not establish a universal Native hierarchy or a V4 design.

Implement the shared chain as frozen corpus -> representation -> whole-card
knowledge -> persisted observations/relationships -> task-specific blind views
-> independent semantic lenses -> projections. Add structured activity and
relationship roles, preserve source/native separation, and make production
waves resumable and interruption-safe. Keep provider names and exact routing
out of permanent product promises.

## Open empirical questions

Measure activity-role schema shape, proposition-level evidence binding, direct-
service and conduct/evaluation pressure cases, Native induction diversity,
review allocation, batch/flex economics, corpus refresh effects and right-tail
bias. No current experiment fixes universal quality thresholds or replaces a
future explicit product decision.
