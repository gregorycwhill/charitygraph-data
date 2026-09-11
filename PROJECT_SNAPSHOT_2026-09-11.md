# CharityGraph project snapshot — 11 September 2026

**Status:** Reference — immutable review/navigation snapshot; not product authority  
**Review date:** 11 September 2026

## Repositories and intended review refs

| Product | Repository | Intended review ref | Note |
|---|---|---|---|
| Builder | `gregorycwhill/charitygraph` | branch `review-snapshot-2026-09-11` at `b69ab9f3ec7c3479d1c2a6829a67fa4198f5746a` | Phase-5 implementation snapshot |
| Data | `gregorycwhill/charitygraph-data` | branch `review-readiness-2026-09-11` | canonical documentation and contracts; exact commit pinned externally by the review instruction |
| Viewer | `gregorycwhill/charitygraph-viewer` | branch `review-readiness-2026-09-11` at `b66168074c2111363020463749ac283f9024bbd7` | documentation-only authority-link correction; existing Viewer state |
| Playbooks | `gregorycwhill/charitygraph-playbooks` | branch `review-readiness-2026-09-11` at `f0cd9fe76b9fd402ec53b82210e148feeb984af6` | review checks added; no production catalogue |

These are frozen published review branches. They are not release candidates or
merge proposals. The exact Data commit is pinned externally by the review
instruction because this file is part of the Data branch and cannot contain a
self-referential final commit claim.

## Navigation

- Authority entry point: [DOCUMENT_AUTHORITY.md](DOCUMENT_AUTHORITY.md)
- Current state: [CURRENT_STATE.md](CURRENT_STATE.md)
- Development method: [DEVELOPMENT_METHOD.md](DEVELOPMENT_METHOD.md)
- Architecture: [INTEGRATED_PRODUCT_AND_DATA_MODEL.md](INTEGRATED_PRODUCT_AND_DATA_MODEL.md), [docs/architecture.md](docs/architecture.md)
- Implementation and validation: [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md), [TEST_PLAN.md](TEST_PLAN.md)
- Viewer contract and UX context: [PUBLIC_CONTRACT_0_5.md](PUBLIC_CONTRACT_0_5.md), [EXPERIENCES.md](EXPERIENCES.md)
- Playbooks contract: [charitygraph-playbooks](https://github.com/gregorycwhill/charitygraph-playbooks), especially its `PLAYBOOK_CONTRACT.md` and `PLAYBOOK_BASE_POLICY.md`
- Phase-5 empirical snapshot: [PHASE5_EXECUTION_STATUS_2026-09-11.md](PHASE5_EXECUTION_STATUS_2026-09-11.md)

The current public release remains immutable `v0.5.0-2026-08-15`.

Private runtime databases, raw source archives, provider responses, credentials
and private experiment artefacts are excluded from public Git.
