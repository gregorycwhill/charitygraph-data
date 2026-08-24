# CharityGraph Agent and Data Distribution Contract

**Status:** Product-level future contract, version 1.0-draft

**Scope:** How agents and downstream software consume CharityGraph data; no runtime agent platform is implemented by this document

## 1. Principle

CharityGraph should be naturally usable by analysts, scripts and software agents without giving an agent more authority than the person or organisation that delegated the task.

## 2. Distribution forms

The product may expose:

- immutable downloadable release bundles;
- static Viewer pages and machine-readable card/subject projections;
- versioned schemas and vocabularies;
- checksums, manifests, coverage and limitations reports;
- future query/API endpoints where justified;
- correction/challenge submission interfaces;
- private local Builder outputs for authorised users.

The downloadable release remains the reproducible source of public truth. Dynamic services must identify the release or knowledge snapshot they use.

## 3. Agent-readable requirements

A future public record should enable an agent to determine:

- stable subject reference and external identifiers;
- scope and time of each material assertion;
- whether a value is source-reported, calculated, model-assessed or human-reviewed;
- evidence/citation and provenance projection;
- taxonomy scheme, concept and version;
- confidence/strength and lifecycle status where applicable;
- coverage and missing-state semantics;
- release identity, licence and attribution;
- correction or challenge route.

## 4. Mandate boundary

An agent acting for a user should carry a machine-readable mandate stating, as applicable:

- principal and delegated role;
- purpose and permitted tasks;
- geographic, subject and time scope;
- spending or action limits;
- data-use/privacy constraints;
- expiry and revocation;
- required evidence and review standard.

CharityGraph data does not itself authorise an agent to donate, contact a charity, make a funding decision, publish an allegation or act for an organisation.

## 5. Citation and uncertainty

Agents must not present a CharityGraph model-assessed classification as a regulator's statement. They should preserve material qualifiers, scope, time and source method. `unknown`, `not_attempted`, `not_applicable`, `withheld` and `failed` are not interchangeable.

For high-consequence decisions, an agent should inspect cited evidence and applicable current official sources rather than relying solely on a cached summary.

## 6. Query and cohort reproducibility

An exported cohort or analytical result should record:

- release/snapshot identity;
- query or filter expression;
- taxonomy and metric versions;
- inclusion/exclusion and missing-value policy;
- generated time and tool version;
- any post-processing or user edits.

This lets another analyst or agent reproduce the result without requiring identical prose explanations.

## 7. Corrections from agents

Agents may help prepare correction proposals, but proposals must identify the human/organisational principal where required, cite evidence and declare automated assistance. Automated volume does not grant priority or authority. Anti-abuse, privacy and review controls apply.

## 8. Bulk and responsible use

Open licensing permits broad reuse subject to the applicable licence. Users and agents must separately respect brand/endorsement rules, third-party rights, privacy, rate limits and laws. CharityGraph should provide efficient bulk access so responsible users do not need to scrape the Viewer.

## 9. Version change

Schemas and vocabularies are versioned. Consumers must not assume labels are permanent identifiers. Deprecated concepts and prior releases remain resolvable where retention policy allows. Breaking public changes require a new contract/release version and migration notes.

## 10. Near-term implementation boundary

The first Builder slice need only emit a private machine-readable projection with the fields above where available. Public APIs, autonomous actions, mandate exchange and agent authentication are deferred. The data model must accommodate them without making them prerequisites for useful charity data.
