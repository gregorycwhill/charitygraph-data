# CharityGraph Data

CharityGraph Data publishes versioned public contracts, schemas, taxonomies, releases and shared project memory for structured, governed Australian charity data. It is one member of the CharityGraph product family: Builder constructs governed knowledge, Data publishes reusable governed data and shared authority, Viewer supports human inspection, and [Playbooks](https://github.com/gregorycwhill/charitygraph-playbooks) publishes governed open analytical methods for using CharityGraph with general-purpose AI. Playbooks is a separate product, not a Data feature.

Start with [DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md) and the canonical [BRAND_AND_REUSE.md](BRAND_AND_REUSE.md). The canonical product set is [PRODUCT.md](PRODUCT.md), [PRINCIPLES.md](PRINCIPLES.md), [PUBLIC_COMMITMENTS.md](PUBLIC_COMMITMENTS.md) and [EXPERIENCES.md](EXPERIENCES.md). The integrated model, coverage/open-curation policy, source governance, taxonomy governance and domain index complete the active v2.0-draft authority set. Current execution state and plans are linked from that authority record.

## Public contract and releases

[PUBLIC_CONTRACT_0_5.md](PUBLIC_CONTRACT_0_5.md) describes the implemented public compatibility contract. Its exact authority is the immutable [v0.5.0-2026-08-15](releases/v0.5.0-2026-08-15) release, schemas, examples and manifest. Literal historical field names, paths and artefact names remain only where the release requires compatibility; they are not the vocabulary for future internal work.

[PUBLIC_SCHEMA_VNEXT_SPEC.md](PUBLIC_SCHEMA_VNEXT_SPEC.md) is retained as a technical reference for implemented 0.5 schema material. It is not a future-contract proposal. Machine-distribution obligations are in [AGENT_DATA_DISTRIBUTION_CONTRACT.md](AGENT_DATA_DISTRIBUTION_CONTRACT.md).

## Product authority and delivery

- [INTEGRATED_PRODUCT_AND_DATA_MODEL.md](INTEGRATED_PRODUCT_AND_DATA_MODEL.md)
- [COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md](COVERAGE_LLM_ECONOMICS_AND_OPEN_CURATION_POLICY.md)
- [SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md](SOURCE_EVIDENCE_AND_PUBLICATION_GOVERNANCE.md)
- [TAXONOMY_AND_SCHEME_GOVERNANCE.md](TAXONOMY_AND_SCHEME_GOVERNANCE.md)
- [DOMAIN_PROFILE_INDEX.md](DOMAIN_PROFILE_INDEX.md)
- [SEMANTIC_RELIABILITY_AND_REPRODUCIBILITY.md](SEMANTIC_RELIABILITY_AND_REPRODUCIBILITY.md)
- [SEMANTIC_RELIABILITY_BASELINE_2026-08-28.md](SEMANTIC_RELIABILITY_BASELINE_2026-08-28.md)
- [SEMANTIC_EXTRACTION_AND_MAPPING_DECISIONS_2026-08-31.md](SEMANTIC_EXTRACTION_AND_MAPPING_DECISIONS_2026-08-31.md)
- [PUBLIC_VNEXT_DECISION_LOG.md](PUBLIC_VNEXT_DECISION_LOG.md)
- [ROADMAP.md](ROADMAP.md) · [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) · [TEST_PLAN.md](TEST_PLAN.md)

## Repository boundary

Builder creates validated release candidates; Data owns immutable public artefacts; Viewer renders an explicitly selected release. Raw upstream material, private evidence, model traces, runtime databases, caches, logs, credentials and debug output do not belong here.

## Licence and upstream material

CharityGraph-originated data and content are licensed under [CC BY 4.0](LICENSE). That licence does not grant rights in third-party regulator data, annual reports, website content, trademarks or other source evidence. Downstream users remain responsible for applicable terms and attribution.
Phase 1 execution packet: [REALITY_SLICE_1_ACCEPTANCE_PACKET.md](REALITY_SLICE_1_ACCEPTANCE_PACKET.md).
