# CharityGraph Agent and Data Distribution Contract

**Status:** Product-level future contract, version 1.1-draft

**Date:** 29 August 2026

**Scope:** How agents and downstream software discover and consume CharityGraph data; no runtime agent platform is implemented by this document

## 1. Principle

CharityGraph should be naturally usable by analysts, scripts and software agents without giving an agent more authority than the person or organisation that delegated the task.

Public CharityGraph knowledge should be readable, addressable and discoverable. Machine discoverability is a distribution property of governed public releases, not a separate source of truth and not a reason to weaken provenance, scope, uncertainty or release identity.

## 2. Distribution forms

The product may expose:

- immutable downloadable release bundles;
- static, crawlable Viewer pages for organisations, programs, services and evidence;
- machine-readable JSON and Markdown card/subject projections;
- versioned schemas and vocabularies;
- checksums, manifests, coverage and limitations reports;
- declared mirrors or archival deposits of identified releases;
- future query/API, MCP or browser-agent endpoints where justified;
- correction/challenge submission interfaces; and
- private local Builder outputs for authorised users.

The downloadable release remains the reproducible source of public truth. Dynamic services, mirrors and agent-facing projections must identify the CharityGraph release or knowledge snapshot they use.

Static public artefacts remain the durable baseline. A distribution channel must not become an independent editorial or semantic authority.

## 3. Machine discoverability

A public subject representation should be:

- **readable:** understandable by a person or general-purpose language model when retrieved in isolation;
- **addressable:** available through a stable subject or evidence reference and, where web-published, a durable canonical URL; and
- **discoverable:** reachable through ordinary web indexing, release catalogues, sitemaps or other declared machine-discovery mechanisms.

Public web projections should use ordinary web standards before platform-specific integrations. Where appropriate this may include canonical links, sitemaps, metadata and Schema.org or successor structured-data vocabularies. Such metadata is a projection from CharityGraph governed knowledge and must not become the internal ontology or silently change subject meaning.

Critical public facts, scope, provenance and release identity should not depend solely on client-side interaction or an agent executing code in the Viewer.

Crawler and reuse policy must distinguish at least:

- ordinary search/indexing;
- user-requested retrieval or citation;
- automated agent access;
- foundation-model training or other secondary corpus use; and
- bulk reuse under the applicable public licence.

These are separate policy choices. CharityGraph may permit several or all of them, but must not treat "AI access" as one undifferentiated permission. Inclusion in a foundation-model training corpus is neither a product requirement nor a distribution success metric.

CharityGraph should remain vendor-neutral. OpenAI-, Google-, Anthropic-, Perplexity- or other provider-specific metadata or integration may be supplied as optional projections, but the durable public contract must not depend on one provider's crawler, store, prompt format or agent runtime.

## 4. Agent-readable requirements

A future public record should enable an agent to determine:

- stable subject reference and external identifiers;
- scope and time of each material assertion;
- whether a value is source-reported, calculated, model-assessed or human-reviewed;
- evidence/citation and provenance projection;
- taxonomy scheme, concept and version;
- confidence/strength and lifecycle status where applicable;
- coverage and missing-state semantics;
- release identity, licence and attribution; and
- correction or challenge route.

A concise card or subject page may optimise retrieval and comprehension, but it does not replace the governed assertion/evidence model behind it.

## 5. Retrieval, citation and uncertainty

Agents must not present a CharityGraph model-assessed classification as a regulator's statement. They should preserve material qualifiers, scope, time and source method. `unknown`, `not_attempted`, `not_applicable`, `withheld` and `failed` are not interchangeable.

A machine-facing projection should make it practical for a consuming system to cite CharityGraph and, where appropriate, follow the lineage to the underlying source or evidence projection.

For high-consequence decisions, an agent should inspect cited evidence and applicable current official sources rather than relying solely on a cached summary, search snippet, embedding hit or secondary mirror.

Search-engine ranking, generative-search citation and model-provider confidence signals are external behaviours. CharityGraph should optimise for accurate, accessible, well-linked and well-described public information rather than attempt to manipulate undocumented ranking or trust mechanisms.

## 6. Secondary distribution and archival mirrors

Secondary channels such as research repositories, dataset hubs or archival services may distribute identified CharityGraph releases to improve reuse, citation, preservation and machine-learning access.

Examples may include services such as Hugging Face or Zenodo where their terms and capabilities fit the release. A DOI or other persistent citation may identify a release or archived deposit.

A mirror must:

- state the CharityGraph release and licence;
- preserve attribution and limitations metadata;
- distinguish mirrored CharityGraph material from downstream additions;
- avoid silently becoming a newer or different editorial version; and
- point consumers to the canonical CharityGraph release record where practical.

Distribution through a dataset hub or archival repository does not imply or guarantee use in foundation-model pre-training, fine-tuning or retrieval systems.

## 7. Dynamic agent and tool interfaces

Future APIs, MCP servers, browser-agent interfaces such as WebMCP or successor standards, and platform-specific applications may provide convenient query and retrieval over public CharityGraph knowledge.

These interfaces are downstream projections of identified releases or snapshots. They must not create a second canonical knowledge state.

Read/query use should precede action-oriented integrations. A future tool interface may expose capabilities such as subject lookup, program/service search, evidence retrieval or cohort construction without authorising donation execution, outreach, procurement or other consequential action.

Dynamic interfaces should be introduced when user demand justifies their operating, security, compatibility and maintenance costs. They are not prerequisites for a useful CharityGraph release.

## 8. Mandate boundary

An agent acting for a user should carry a machine-readable mandate stating, as applicable:

- principal and delegated role;
- purpose and permitted tasks;
- geographic, subject and time scope;
- spending or action limits;
- data-use/privacy constraints;
- expiry and revocation; and
- required evidence and review standard.

CharityGraph data does not itself authorise an agent to donate, contact a charity, make a funding decision, publish an allegation or act for an organisation.

## 9. Query and cohort reproducibility

An exported cohort or analytical result should record:

- release/snapshot identity;
- query or filter expression;
- taxonomy and metric versions;
- inclusion/exclusion and missing-value policy;
- generated time and tool version; and
- any post-processing or user edits.

This lets another analyst or agent reproduce the result without requiring identical prose explanations.

## 10. Corrections from agents

Agents may help prepare correction proposals, but proposals must identify the human/organisational principal where required, cite evidence and declare automated assistance. Automated volume does not grant priority or authority. Anti-abuse, privacy and review controls apply.

## 11. Bulk and responsible use

Open licensing permits broad reuse subject to the applicable licence. Users and agents must separately respect brand/endorsement rules, third-party rights, privacy, rate limits and laws. CharityGraph should provide efficient bulk access so responsible users do not need to scrape the Viewer.

Bulk releases and machine-readable subject projections should be preferred over forcing downstream developers to reconstruct CharityGraph by crawling rendered pages.

## 12. Version change

Schemas and vocabularies are versioned. Consumers must not assume labels are permanent identifiers. Deprecated concepts and prior releases remain resolvable where retention policy allows. Breaking public changes require a new contract/release version and migration notes.

Machine-discovery metadata, crawler policy and dynamic tool interfaces may evolve faster than the underlying data contract. Changes to those channels must not silently change the meaning or authority of released CharityGraph knowledge.

## 13. Near-term implementation boundary

The first Builder slice need only emit a private machine-readable projection with the fields above where available. No Builder implementation work is required solely to optimise search-engine or agent discovery.

Public crawlability, canonical URLs, structured web metadata, sitemaps, crawler policy, secondary dataset mirrors, DOI deposits, APIs, MCP, WebMCP, platform applications, autonomous actions, mandate exchange and agent authentication are distribution-layer work and remain deferred until the relevant public release and user demand justify them.

The data model must accommodate those channels without making them prerequisites for useful charity data.
