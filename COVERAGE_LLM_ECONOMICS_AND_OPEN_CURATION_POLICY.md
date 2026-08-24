# CharityGraph Coverage, LLM Economics and Open Curation Policy

**Status:** Canonical policy, version 1.0-draft

**Applies to:** Builder vNext, future Data releases and governed review

**Authority:** Refines `PRODUCT.md`, `PRINCIPLES.md` and `PUBLIC_COMMITMENTS.md`

## 1. Policy decision

CharityGraph optimises for a useful balance of **coverage, reach and defensibility**, not forensic perfection on a tiny fraction of the sector. Every published claim must meet a mechanical provenance floor. The amount of evidence retrieval, model reasoning and human review above that floor is deliberately risk- and cohort-dependent.

This is a coverage-first policy, not a provenance-light policy.

## 2. Why this policy exists

A one-stop shop for Australian charity data has little public value if it describes only a handful of organisations perfectly. Broad coverage creates the conditions for analysts, charities and communities to find, challenge and improve the data. Transparent correction is part of the product's success.

Conversely, broad but unauditable output would be untrustworthy. CharityGraph therefore separates:

- **mechanical lineage**, which is mandatory;
- **semantic judgment**, which may reasonably be contestable;
- **review depth**, which varies with consequence, evidence and budget.

## 3. Universal provenance floor

For every published assertion or classification, the system must retain enough governed information to identify:

- the subject and applicable scope;
- the source artefact and its retrieval metadata;
- the relevant evidence span or structured record;
- the transformation or model task that produced the result;
- prompt/template version, model/provider identity and material parameters when a model was used;
- the output, validation result and any adjudication;
- the release and public representation in which it appeared;
- supersession, correction and withdrawal events.

Raw source data, governed derivatives and mechanical lineage are retained according to source rights, privacy and storage policy. Public release may expose a lawful projection rather than every retained artefact.

## 4. Judgment policy

LLMs are used because many public-data tasks require language judgment. They are not merely expensive regular expressions.

When adequate evidence exists, a model task should make the best-supported low-risk judgment—for example, assigning a charity or program to a cause, population, activity or UN Sustainable Development Goal. Ordinary semantic disagreement is represented through:

- primary and secondary assignments;
- confidence or strength;
- evidence and rationale;
- competing observations where materially useful;
- later correction or supersession.

`unknown` is appropriate when evidence is genuinely absent, inaccessible, unprocessable or insufficient for the requested proposition. It is not the default response to ordinary ambiguity.

High-consequence claims—such as misconduct, safeguarding, legal status, financial distress or assertions about Indigenous authority—may require stronger evidence or specialist review regardless of cohort.

## 5. Approved cohort budgets

The initial scheduled-batch planning rule is:

| Cohort | Approximate reach | Aggregate LLM budget | Indicative average | Intended treatment |
|---|---:|---:|---:|---|
| A | Top 100 | AU$100 | AU$1.00 per subject | Broad retrieval, richer synthesis, higher scrutiny |
| B | Next 1,000 | AU$100 | AU$0.10 per subject | Targeted retrieval and multi-domain extraction |
| C | Next 10,000 | AU$100 | AU$0.01 per subject | Efficient classification and selected extraction |
| D | Remaining eligible population | No routine per-subject allocation initially | Near zero | Mechanical sources, cache reuse, selective escalation |

These are portfolio controls, not an entitlement or hard per-record cap. The scheduler may spend more on difficult or high-risk work and less on easy work while remaining within the cohort envelope.

The ranking and membership method for each cohort must be versioned and reproducible. Notability may help allocate processing effort but must not become a universal quality or worth score.

## 6. Budget enforcement

Before a paid task begins, Builder must:

1. identify cohort, run and task;
2. estimate or reserve spend;
3. apply provider and task policies;
4. reuse a valid cache entry where permitted;
5. record attempts, actual cost and credits;
6. reconcile reservations, including overruns and unreserved actuals;
7. stop or escalate according to the configured hard and soft limits.

Costs are signed ledger entries. Reservations, actuals and credits remain distinct. Budget reporting must not hide overruns through fabricated releases, zeroing or aggregation.

## 7. Coverage measurement

Coverage is measured at several levels:

- **reach:** eligible subjects represented at all;
- **source coverage:** expected source classes acquired;
- **domain coverage:** identity, programs, participation, fundraising, finance and other domains attempted;
- **claim coverage:** requested propositions resolved as supported, contradicted, unknown or not applicable;
- **evidence coverage:** assertions with valid evidence and lineage;
- **enhanced coverage:** subjects receiving deeper retrieval or review;
- **temporal coverage:** freshness and historical span;
- **right-tail coverage:** small and low-notability organisations represented fairly.

Coverage reports must distinguish `not_attempted`, `not_applicable`, `unknown`, `withheld`, `failed` and `resolved`. Silence is not interpreted as absence.

## 8. Quality and risk measures

The program should track at least:

- false-promotion and material factual error rates;
- unjustified abstention rates;
- evidence and lineage completeness;
- taxonomy assignment agreement on governed evaluation sets;
- cost per subject, domain and resolved claim;
- human-review demand and outcomes;
- correction frequency, latency and disposition;
- cohort and right-tail disparities;
- stale-source and failed-acquisition rates.

No single metric is the objective function. A lower error rate achieved by declaring most classifications unknown is not success.

## 9. Open curation and challenge

CharityGraph is an open-data project with governed community correction. A person must be able to:

1. identify the public claim and supporting evidence;
2. submit a correction, counter-evidence or scope clarification;
3. receive a stable proposal/reference identifier;
4. see its status and eventual disposition;
5. see an accepted change in a subsequent governed release;
6. see the previous assertion retained in history rather than silently rewritten.

Supported dispositions are:

- `accepted`;
- `accepted_with_edit`;
- `partially_accepted`;
- `upheld`;
- `insufficient_evidence`;
- `duplicate`;
- `superseded_by_newer_evidence`;
- `withdrawn`;
- `specialist_review`.

Community input does not mutate production data directly. It creates governed observations or proposals that pass validation, review and promotion controls.

## 10. Corrections are a success signal

An evidence-based change to a tag, amount or relationship is not automatically a pipeline failure. It shows that the dataset is being used and curated. It becomes a processing failure only when analysis shows a preventable error class—for example, a broken parser, wrong scope, ignored authoritative source or systematically misleading prompt.

One-off corrections should update the record. Repeated patterns should update the method, evaluation set or source policy.

## 11. Human review allocation

Review is prioritised by consequence and learning value, including:

- high-risk claim types;
- material contradictions between authoritative sources;
- uncertainty that affects a prominent public conclusion;
- potentially systematic model or extraction failures;
- Indigenous data-governance questions;
- well-supported community challenges;
- evaluation-set sampling across cohorts, including the right tail.

Human review is not required for every ordinary low-risk taxonomy judgment.

## 12. Anti-wheel-spinning controls

For each implementation slice:

- freeze the design packet, acceptance tests and evaluation cohort before coding;
- classify fields as deterministic, model-assisted, human-reviewed or deferred;
- use a fixed development set and untouched holdout;
- repair error classes, not an expanding list of individual phrasings;
- normally allow one implementation pass and one bounded correction pass;
- after a second conceptual failure, stop and redesign rather than layering heuristics;
- keep unresolved cases as governed records instead of blocking the slice;
- duplicate neither raw evidence nor model artefacts merely because a run is repeated.

## 13. Publication rules

Future releases must publish:

- cohort and coverage definitions;
- material model/provider and prompt-policy information;
- known limitations and failure rates;
- correction and challenge pathways;
- release identity and checksums;
- lawful provenance projections;
- clear distinctions between source facts, calculated values, model-assessed classifications and human decisions.

This policy does not alter immutable public contract 0.5. It governs vNext implementation and future releases only.
