# CharityGraph LLM Economics and Cohort Policy

**Status:** Canonical shared product and implementation policy  
**Version:** 1.0-draft  
**Date:** 2026-08-23  
**Applies to:** Builder model-assisted processing, evaluation and corpus-build planning

## 1. Decision

CharityGraph is a Python-controlled, LLM-powered data product. Models are not a rare rescue path after local NLP fails. They are a routine means of recovering, interpreting, structuring and explaining public evidence. Python makes that use economical, reproducible and governable.

Coverage is the optimisation objective. Defensibility is a constraint expressed through evidence, method labels, typed schemas, risk policy and corrections. A legally cautious pipeline with negligible coverage does not satisfy the product commitment.

## 2. Protected cohort budgets

The first corpus build uses three pooled paid-model budgets:

| Cohort | Membership | Total cap | Average planning allowance |
| --- | --- | ---: | ---: |
| C100 | 100 highest-total-donations charities | AUD 100 | AUD 1.00 |
| C1K | next 1,000 highest-total-donations charities | AUD 100 | AUD 0.10 |
| C10K | next 10,000 highest-total-donations charities | AUD 100 | AUD 0.01 |

The cap includes every paid inference output attributable to the cohort:

- text and vision extraction, including difficult OCR/page recovery;
- relevance screening and semantic judgement;
- typed fact, relationship and classification extraction;
- participation, fundraising, ethos, service-orientation and notable-context interpretation;
- adjudication/escalation by a stronger model;
- card blurbs and other bounded writing;
- embedding vectors;
- retries, validation repairs and failed paid attempts where the provider charges them.

Human labour, Codex implementation tokens and local compute are accounted for in total-cost-of-ownership evaluation but do not consume these API/model caps.

Budgets are pooled within a cohort. Easy charities may subsidise difficult charities. Unused budget does not cross to another cohort unless the product owner explicitly approves a transfer. A planning allowance is not a per-charity entitlement or hard sub-cap.

## 3. Processing order and meaning

Total donations is used as `donor_decision_exposure_proxy`: a practical proxy for how many or how consequential donor decisions may be affected by CharityGraph when donor-count data is unavailable.

It must never be described as:

- individual or retail donor count;
- donor-decision count;
- public support quality;
- charity merit, worth, credibility or effectiveness;
- likely fit or recommendation;
- proof that a charity has an active brand/legal function.

It controls initial processing order and risk-aligned assurance. The first 100 receive more available spend and scrutiny because their public profile makes errors more consequential and more likely to be challenged. The next 1,000 receive a leaner route; the next 10,000 rely predominantly on economical automated processing and sampling.

Missing or unreliable donations data requires a versioned fallback proxy and an explicit reason; it must not be silently treated as zero.

## 4. Division of labour

### Python control plane

Python is responsible for:

- source discovery/acquisition orchestration and rights policy;
- completed-byte hashing and immutable evidence storage;
- obvious structured extraction and source-native preservation;
- off-the-shelf OCR and document segmentation;
- subject/source joins and deterministic binding rules;
- evidence selection, deduplication and compact evidence packs;
- typed schemas, validation and repair routing;
- batching, scheduling, caching, retries, rate limits and resume;
- budget reservation, actual-cost reconciliation and hard stops;
- coverage assessment, derivative invalidation and release compilation.

### Routine LLM work

Models are expected to perform:

- difficult OCR/vision recovery where normal text extraction is inadequate;
- semantic relevance screening;
- typed extraction from prose, tables and mixed layouts;
- entity/relationship interpretation where syntax alone is insufficient;
- program/service, activity, beneficiary and geography judgement;
- participation and fundraising classification;
- ethos, service/mission orientation and notable-context analysis;
- taxonomy candidate assignment and ambiguity explanation;
- bounded summaries and card blurbs from accepted observations;
- stronger-model adjudication for selected conflicts/risks.

Embeddings are a separate model-derived artefact generated from stable release-safe derivative text.

## 5. Local NLP decision

The initial build does not include custom local NER, relevance, taxonomy, reranking or summarisation models. It retains cheap mechanical components: parsing, regular expressions, vocabulary checks, joins, off-the-shelf OCR and deterministic validation.

A custom local NLP component requires an approved benchmark showing a total-cost-of-ownership advantage. The comparison includes:

- API cost saved;
- Codex design and implementation effort;
- training/label data creation;
- evaluation and regression maintenance;
- model packaging, runtime and drift monitoring;
- debugging and operational complexity;
- any recall/quality loss or routing latency.

Saving a few dollars of API spend is insufficient if it creates more implementation or maintenance cost.

## 6. Logical tasks and physical requests

OCR/vision recovery, relevance, extraction, interpretation, taxonomy, writing and embeddings remain separate logical tasks with separate schemas, lineage, validation and invalidation.

Physical execution may optimise them:

- **provider batch:** group independent requests for asynchronous economical processing where available;
- **same-subject task bundle:** one request may emit several logical outputs if benchmarked and independently validated;
- **multi-subject bundle:** disabled by default; requires a contamination and omission benchmark;
- **selective escalation:** a cheap route may refer only difficult or risky items to a stronger model.

One physical call does not create one undifferentiated governance object.

## 7. Scheduler requirements

For each run, the scheduler must:

1. resolve the immutable cohort definition and ranking snapshot;
2. enumerate required logical tasks and valid cache hits;
3. select evidence and estimate token/image/call cost;
4. group compatible work by provider, model snapshot, task schema and prompt/policy version;
5. reserve estimated AUD cost transactionally before submission;
6. submit, poll and resume without duplicate paid work;
7. validate each logical result and route repair/escalation within remaining budget;
8. reconcile provider-reported actual usage/cost and release unused reserve;
9. stop new paid work before the cohort cap can be exceeded;
10. emit a complete cost, coverage, failure and cache report.

Scheduling may use expected information yield and risk within a cohort. It may not use perceived charity worthiness.

## 8. Cache and provenance contract

The canonical cache identity is:

```text
H(task type, task schema, evidence hashes, prompt/policy version,
  model snapshot, parameters, material tool versions)
```

The operational record also stores subject, scope, cohort, physical batch/request, timestamps and status even where these are not part of semantic cache identity.

Retain privately:

- canonical request specification and selected evidence IDs/hashes;
- raw provider response;
- separately validated logical outputs;
- provider/model snapshot and parameters;
- prompt, policy, task-schema and tool versions;
- usage, latency, provider-currency price and AUD conversion;
- attempts, repairs, retries and escalations;
- cache reuse, supersession and invalidation.

No prompt, raw response or spend telemetry enters a public release.

## 9. Pricing and currency

Every run binds to a `PricingSnapshot` containing provider, effective/retrieved time, model IDs, input/cached-input/output/image/tool/embedding rates, provider currency and authoritative source URL. Every AUD conversion binds to the FX rate, source and time used.

The scheduler estimates against the bound snapshot and reconciles against provider-reported usage. A price change creates a new snapshot; it does not rewrite historical cost.

Current planning examples, not permanent requirements:

- OpenAI lists GPT-5.6 Luna at USD 0.20 per million input tokens, USD 0.02 cached input and USD 1.20 output; it supports image input and structured outputs: <https://developers.openai.com/api/docs/models/gpt-5.6-luna>.
- OpenAI lists `text-embedding-3-small` at USD 0.02 per million tokens and `text-embedding-3-large` at USD 0.13: <https://developers.openai.com/api/docs/models/text-embedding-3-small> and <https://developers.openai.com/api/docs/models/text-embedding-3-large>.

At those example text rates, a 10,000-input/1,000-output Luna request is approximately USD 0.0032 before image/tool charges. Embedding 2,000 tokens for 11,100 charities is approximately USD 0.44 with the small model or USD 2.89 with the large model. These examples show feasibility only; benchmarks and actual provider bills control decisions.

## 10. Governance and assurance

“Governed” means source-bound, typed, policy-controlled, versioned, testable and correctable. It does not mean universal human approval.

A model output:

- is never a human decision;
- may remain a private candidate;
- may become canonical through an explicit automation policy backed by applicable benchmark evidence;
- may be routed to a stronger model, human reviewer or hold state;
- must retain model/policy/evidence provenance.

Human review is concentrated on benchmark samples, identity conflicts, materially contradictory evidence, sensitive/reputational/legal claims, policy-edge cases and higher-exposure subjects. Stronger-model adjudication may replace some human review when benchmarked. Sensitive fields may use stricter policies without blocking ordinary card coverage.

## 11. Coverage-first acceptance

Defensibility constrains what can be published; it is not the objective to maximise. Prefer a source-linked model interpretation with an explicit method and uncertainty to a null chosen solely because it is safer.

Measure by cohort and domain:

- charities with usable summaries and embeddings;
- program/service, participation, activity/beneficiary, fundraising, ethos/service-orientation and notable-context coverage where evidence opportunity exists;
- proportion receiving the intended model-assisted pass;
- accepted observations per charity and per AUD;
- recoverable recall and evidence-opportunity conversion;
- unsupported-claim and material-error rate;
- correction/challenge rate and response time;
- stronger-model/human review burden;
- cache-hit savings, batch efficiency and refresh cost.

The release/pilot gate must reject both extremes:

- unsupported high-coverage output; and
- extremely precise but trivially sparse output.

Targets are established by the economics spike and approved before each production cohort. They are domain-specific; no aggregate score silently authorises every task.

## 12. Required implementation order

1. Install this policy and aligned product/architecture/plans.
2. Define minimum task, cohort, pricing, cost and cache contracts.
3. Implement the thin SQLite ledger and fake-provider scheduler.
4. Run the bounded real-model economics spike.
5. Complete the LLM-powered vertical slice.
6. Expand domains and archive reuse only after the spike informs the design.
7. Process C100, C1K and C10K sequentially, with a review between cohorts.

No architecture tranche may insert a custom local semantic model or universal human-review gate without explicit product approval.
