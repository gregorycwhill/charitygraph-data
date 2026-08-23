# CharityGraph Data

CharityGraph Data publishes versioned public contracts, schemas, taxonomies, releases and shared project memory for structured, governed Australian charity data.

Start with [DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md) and the canonical [BRAND_AND_REUSE.md](BRAND_AND_REUSE.md). The canonical product set is [PRODUCT.md](PRODUCT.md), [PRINCIPLES.md](PRINCIPLES.md), [PUBLIC_COMMITMENTS.md](PUBLIC_COMMITMENTS.md) and [EXPERIENCES.md](EXPERIENCES.md). Current execution state and plans are linked from that authority record.

## Public contract and releases

[PUBLIC_CONTRACT_0_5.md](PUBLIC_CONTRACT_0_5.md) describes the implemented public compatibility contract. Its exact authority is the immutable [v0.5.0-2026-08-15](releases/v0.5.0-2026-08-15) release, schemas, examples and manifest. Literal historical field names, paths and artefact names remain only where the release requires compatibility; they are not the vocabulary for future internal work.

[PUBLIC_SCHEMA_VNEXT_SPEC.md](PUBLIC_SCHEMA_VNEXT_SPEC.md) is retained as a technical reference for implemented 0.5 schema material. It is not a future-contract proposal. Machine-distribution obligations are in [AGENT_DATA_DISTRIBUTION_CONTRACT.md](AGENT_DATA_DISTRIBUTION_CONTRACT.md).

## Repository boundary

Builder creates validated release candidates; Data owns immutable public artefacts; Viewer renders an explicitly selected release. Raw upstream material, private evidence, model traces, runtime databases, caches, logs, credentials and debug output do not belong here.

## Licence and upstream material

CharityGraph-originated data and content are licensed under [CC BY 4.0](LICENSE). That licence does not grant rights in third-party regulator data, annual reports, website content, trademarks or other source evidence. Downstream users remain responsible for applicable terms and attribution.