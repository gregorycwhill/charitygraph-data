# CharityGraph Data architecture boundary

**Status:** Reference  
**Current product authority:** [DOCUMENT_AUTHORITY.md](../DOCUMENT_AUTHORITY.md)

Data owns public contracts, schemas, release manifests, immutable release artefacts and shared project documentation. Builder owns internal knowledge construction and validated release candidates. Viewer owns presentation of an explicitly selected public release.

Public cards, JSON, Markdown and bulk formats are release projections from the same selected observations and derivatives. They are not Builder's canonical internal object.

Public contract 0.5 is implemented compatibility authority for the named immutable release. See [PUBLIC_CONTRACT_0_5.md](../PUBLIC_CONTRACT_0_5.md). A future public contract requires its own product decision, schemas, examples, migration analysis and coordinated Data/Viewer acceptance.