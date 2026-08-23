# Design consolidation response — workspace additions

> **Authority status:** Historical question record. Its approved answers are DESIGN_CONSOLIDATION_DECISIONS.md and the canonical documents named by DOCUMENT_AUTHORITY.md.

**Status:** discussion packet, not canonical product policy or implementation authority.  
**Prepared:** 2026-08-22

## Files reviewed

The workspace-level additions are:

| File | Date | Contribution | Authority indicated by file |
| --- | --- | --- | --- |
| `ETHOS_AND_NOTABILITY_DESIGN.md` | 2026-08-16 | evidence model for organisational ethos and externally notable context | working design; detailed contract unapproved |
| `AGENTIC_PHILANTHROPY_DATA_STRATEGY.md` | 2026-08-17 | downstream personal-agent use cases and mandate-grade data needs | strategy proposal |
| `FUNDRAISING_KNOWLEDGE_DESIGN.md` | 2026-08-21 | practices/campaigns/expenditure population design | working design; review-only pilot proposed |
| `ENRICHMENT_ECONOMICS_DESIGN.md` | 2026-08-22 | benchmark ladder, routing and cost/coverage evaluation | working design; not canonical |

The IDE tab `New Text Document.txt` was not present as a saved workspace file
at review time. Older root PDFs, usage exports, archives and the three
repositories were not treated as new design inputs.

## Overall assessment

The four additions fit the existing CharityGraph direction unusually well: they
keep CharityGraph an evidence-and-semantic layer for downstream decisions, not a
donation recommender, payment product or charity-rating service. They reuse
the current subject/source/observation/coverage model rather than proposing a
replacement datastore.

They should nevertheless remain **working design** until one consolidated
decision set resolves their common schema, source-policy, review and sequencing
questions. In particular, agentic use makes identity, scope, provenance,
coverage and contentious-context rules more consequential; it does not relax
them.

## Reconciliation findings

### Strong alignment

- The proposed personal-agent boundary agrees with `PRODUCT.md` and
  `EXPERIENCES.md`: CharityGraph supplies inspectable facts and evidence; a
  downstream agent owns personal values, matching rules, money, telemetry and
  payment execution.
- Ethos/Notability, fundraising practices and enrichment economics all endorse
  evidence-first extraction, explicit coverage, no universal scores, no public
  semantic promotion before review, and preservation of immutable v0.5.
- The agentic strategy's mandate-fit ingredients (program scope, intervention,
  geography, ethos, identity and evidence freshness) can extend the v0.5
  observation envelope without replacing it.
- The economics design is consistent with the current precision-first Knowledge
  Validation gate: it separates source absence, scope gaps, extraction gaps,
  governance blocks and not-yet-processed work instead of treating blanks as
  facts.

### Important tensions and gaps

1. **Fundraising safety conflict — resolve before any new work.** Canonical
   `PRODUCT.md` says unavailable/null is correct when no defensible method
   exists and prohibits a universal fallback prior. Builder `AGENTS.md` still
   calls a blank fundraising estimate unacceptable; `PROVENANCE_AND_ESTIMATION.md`
   and `fundraising.py` still describe/use a fallback prior. This is not a new
   product choice: the canonical Data policy should be made operationally
   authoritative before a fundraising pilot.
2. **“First-class accepted” is ambiguous.** Ethos/Notability says the
   constructs are accepted but its detailed contract is explicitly unapproved;
   the agentic strategy calls them foundational. Treat the constructs as
   accepted design intent, not accepted public schema, vocabulary, acquisition
   policy or publication rule.
3. **Notability is a risky name for a neutral product.** The design's actual
   object is a set of sourced contextual observations, including positive,
   negative and historical material. A public field called `notability` may
   imply a prestige/reputation judgement despite the safeguards. This needs an
   explicit naming decision.
4. **Mandate support can accidentally become recommendation.** “Primary /
   material-adjacent / incidental” and harm→remedy mappings are useful evidence
   dimensions, but an unexplained scalar match percentage, a default eligibility
   conclusion or an implied best recipient would cross the existing boundary.
5. **The designs compete for the same scarce review capacity.** Knowledge
   Validation is still waiting for its human gate. Ethos/Notability proposes a
   30–50-case cohort, fundraising proposes 30–50, and economics proposes a
   120-charity benchmark plus H1/H2 review. Running all independently would
   create redundant source acquisition and an unbounded adjudication load.
6. **Wikipedia policy is strategically promising but under-specified.** The
   existing ABN-first spike properly deferred broad ingestion. The new designs
   argue for selective discovery/context use, but require a common admission,
   attribution, revision-pinning, citation-following, correction and refresh
   policy before implementation.
7. **Sensitive and adverse context needs a stronger governance path.** Ethos,
   religion/ideology, inquiry/legal/controversy material, and named people
   require source-quality thresholds, subject-scope rules, a right-of-reply or
   correction path, escalation ownership and retention/refresh rules beyond
   ordinary activity extraction.

## Questions for ChatGPT/user design consolidation

### 1. Product boundary and downstream agents

1. Should CharityGraph expose only *mandate-fit ingredients*, or may it expose a
   bounded, non-normative `within_scope / outside_scope / borderline` result
   for a supplied mandate? Recommendation: ingredients only in v1; leave
   adjudication to the downstream agent unless a later policy defines a fully
   inspectable user-supplied rule evaluator.
2. Are `primary`, `material-adjacent` and `incidental` evidence labels,
   taxonomy assignments, or a separate scoped relationship between a subject /
   program and a cause? Define the unit and evidence threshold before building
   a “cause centrality” feature.
3. Is a harm→remedy→intervention graph an internal retrieval aid, a public
   reference taxonomy, or both? Who governs causal assertions, versioning and
   contested mappings?
4. Does the initial scope include program/appeal-level mandate evidence, or
   organisation-level evidence only? Program scope is much more valuable for
   matching, but increases identity, freshness and public-contract complexity.

### 2. Ethos and service/mission orientation

5. Should `service_or_mission_orientation` be part of Ethos or its own
   capability? Recommendation: preserve it as a separate observation domain
   from day one; it answers a different question from institutional identity.
6. What is the minimum publication threshold for a sensitive ethos descriptor:
   direct primary/formal evidence only, or may robust secondary evidence be
   published with explicit attribution? Decide separately for current,
   historical and disputed characterisations.
7. What review level applies to religious, political, cultural and ideological
   descriptors? Is human review mandatory initially for all, only for conflict
   or scope ambiguity, or only for sensitive categories?
8. Which source/scope relationship permits a parent/network ethos fact to be
   shown on an Australian affiliate card, and how must it be rendered to avoid
   attribute transfer?

### 3. Notable context and Wikimedia

9. Is the public construct named `notable_context`, `context`, or
   `notability`? Recommendation: retain “Notability” as an internal design
   concept but prefer `notable_context` for a public field.
10. Which categories can use a Wikipedia revision as provisional review
    evidence, and which must trace to an underlying primary/authoritative
    source before publication? Inquiry, legal, regulatory, controversy and
    living-person claims should have the strictest rule.
11. What is the minimum editorial-admission rule for recognition, founders,
    history, criticism and controversy? Wikipedia article inclusion alone is
    not a claim-specific formal standard.
12. How should corrections work for disputed context: private intake only,
    public proposal record after moderation, an organisation response field,
    or a combination? Define timing, appeal and correction/retraction
    treatment before collecting contentious facts.

### 4. Fundraising knowledge

13. Confirm the canonical fundraising ladder: is approved peer imputation
    still intended as a possible governed method, while universal/broad priors
    are forbidden? If yes, define the approval, peer cohort and publication
    requirements precisely; if no, remove it from `PRODUCT.md` as well.
14. Approve or amend the core distinction: **funding source ≠ standing
    practice ≠ campaign ≠ expenditure**. This is the key schema decision
    behind the fundraising proposal.
15. Is a campaign a nested observation first, a durable subject sometimes, or
    both under explicit promotion criteria? Determine identity/lifecycle rules
    for recurring appeals and programs.
16. Is the optional fundraising-delivery model in scope for the first pilot?
    Recommendation: defer it unless a small cohort shows direct, reliable
    evidence; it otherwise expands third-party identity and liability scope.
17. Is assessment scope (sources/pages/documents examined) public on cards,
    public only as compact coverage metadata, or private operational evidence?
    It is essential to avoid “not found” being misread as “does not exist.”

### 5. Enrichment economics and portfolio design

18. What is the first shared evaluation cohort: one 30–50-case cross-domain
    pilot, a 120-charity economics benchmark, or a staged 30–50 then 120
    design? Recommendation: one shared 30–50 cross-domain corpus first,
    expanding to 120 only after the semantic/human gate validates its review
    protocol and source inventory.
19. Which domains are worth a same-source high-spec oracle in the first
    benchmark? It is likely most informative for scope-sensitive programs,
    fundraising, ethos and notable context—not easy regulator facts.
20. What threshold converts a benchmark result into a production routing rule?
    Specify precision, provenance defect rate, review burden, marginal cost and
    minimum source coverage separately by domain; do not aggregate them.
21. Is H2 broader public-source audit authorised for sources such as social
    media, event platforms and media, or only a manual benchmark experiment?
    Define lawful access, source rights, attribution and retention boundaries.

## Proposed consolidation sequence

1. **Immediate safety reconciliation:** align Builder instructions and code
   paths with the already canonical no-universal-prior policy; add a regression
   test. This should not wait for a broader product decision.
2. **Close the current Knowledge Validation human gate.** Its outcomes should
   become baseline evidence for all new semantic domains and automation policy.
3. **Approve one shared observation-extension pattern:** scoped observation,
   source role, claim basis, extraction method, time, qualification,
   disagreement and coverage. Reuse it for Ethos, notable context, fundraising
   practices/campaigns and geography roles.
4. **Decide high-risk policy before acquisition:** ethos sensitivity, adverse
   context, Wikimedia citation policy, correction/redress and public/private
   assessment scope.
5. **Create one staged evaluation program:** shared source-opportunity
   inventory → 30–50 cross-domain review-only pilot → human decision → 120-case
   economics benchmark only where the pilot warrants it.
6. **Only then change public contract or Viewer.** Maintain immutable v0.5 and
   keep all candidate work private until a governed release decision.

## Opportunities worth retaining

- A disciplined agent-facing evidence layer can reduce brand familiarity as a
  proxy for trust without CharityGraph making donation decisions.
- Annual reports are the common high-value source across programs, geography,
  fundraising, ethos and organisational relationships; a shared extraction and
  review cohort creates leverage.
- The proposed source-opportunity inventory offers a practical way to spend
  compute fairly: every charity receives a cheap baseline, while extra work is
  driven by evidence opportunity rather than perceived worthiness or size.
- “Notability” reframed as sourced contextual history could make hard-to-find
  public facts legible while remaining neutral—if the adverse-content governance
  is designed first.
- A precise practices/campaigns/expenditure distinction would make fundraising
  data genuinely reusable without drifting into ROI or consultant scoring.

## What should not happen yet

- Do not treat these working documents as approval to change schemas, releases,
  taxonomy, Viewer, public content or corpus scale.
- Do not run broad Wikimedia/social-media acquisition or publish Ethos,
  notable-context or fundraising candidates.
- Do not implement a mandate score, reputation score, fundraising performance
  metric or payment/donation workflow inside CharityGraph.
- Do not run three separate cohorts for the same semantic/economic questions.
