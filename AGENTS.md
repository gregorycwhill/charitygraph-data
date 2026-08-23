# CharityGraph Data — Agent Instructions

**Status:** Canonical repository instructions  
**Scope:** shared product authority, public contracts and immutable releases

Read [DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md) before changing any cross-product document, contract or release. It defines precedence and the canonical document for each subject.

CharityGraph Data is the GitHub-visible home for shared product memory and public data contracts. It is a sibling of Builder and Viewer, not the parent product.

For cross-product work, read and maintain the canonical set:

- [PRODUCT.md](PRODUCT.md)
- [PRINCIPLES.md](PRINCIPLES.md)
- [PUBLIC_COMMITMENTS.md](PUBLIC_COMMITMENTS.md)
- [EXPERIENCES.md](EXPERIENCES.md)
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [ROADMAP.md](ROADMAP.md)
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)
- [TEST_PLAN.md](TEST_PLAN.md)
- [CODEX_TO_CHATGPT_HANDOFF.md](CODEX_TO_CHATGPT_HANDOFF.md)
- [PUBLIC_CONTRACT_0_5.md](PUBLIC_CONTRACT_0_5.md)
- [AGENT_DATA_DISTRIBUTION_CONTRACT.md](AGENT_DATA_DISTRIBUTION_CONTRACT.md)

Public contract 0.5 is implemented compatibility authority for its immutable release. Do not edit release bytes, schemas, manifests, or literal legacy compatibility fields. Future internal Builder work uses subject_id; this does not authorise a public-identifier migration.

Keep Builder- and Viewer-specific implementation material with the component that owns it. Do not add private raw sources, archives, runtime output, credentials, model traces, caches, logs, debug files or unreviewed source material to this repository.