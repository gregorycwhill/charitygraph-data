# CharityGraph Current State

**Status date:** 30 August 2026

**Status:** Baseline after Playbooks repository establishment

## 1. Repositories

| Component | Repository | Current `main` | State |
|---|---|---|---|
| Builder | `gregorycwhill/charitygraph` | `5e5656df635f6531b676e595ae41d4f5a8a523a5` | Production foundations and native discovery v2 available |
| Data | `gregorycwhill/charitygraph-data` | `9135db270c7b6d42b293d4c598109068b5b9bd14` (Data main before this documentation tranche) | Canonical contracts, releases and governance |
| Viewer | `gregorycwhill/charitygraph-viewer` | `cd6f3720f664a29e0ca7ed8be19797e573fcdfc8` | Existing deployed Viewer; unchanged by this state update |
| Playbooks | `gregorycwhill/charitygraph-playbooks` | `6466e04` | Initial product contract, base policy, contribution guidance, schema and example; no production catalogue |

## 2. Immutable public release

Public contract 0.5 remains immutable:

- release: `v0.5.0-2026-08-15`;
- manifest SHA-256: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

No v0.5 release files, schemas or ranking snapshots were changed.

## 3. Current production capabilities

The implemented foundation includes evidence/source registry, knowledge persistence, taxonomy/pre-run foundations, exactly-once semantic-call authorization, merged PR #24 durable authorization and semantic technical-replication safety, durable ModelTask/ModelResult evidence binding, multi-proposal native program/service discovery v2, operational-status separation, governed ProgramCandidate -> SubjectRecord promotion, production native-discovery execution, v2 parser dispatch, and canonical ACNC 2024 AIS donation ranking in Data.

## 4. Fresh-18 observation

A mechanically selected, heterogeneous 18-charity cohort was processed using frozen evidence and `program_service_discovery/v2` with GPT-5.6 Luna. The final run produced 17 successful semantic outputs, 97 proposals and 80 projected candidates; no subject promotion or classification was performed.

An accidental 17-pair repeated-measures baseline now informs evaluation design. It exposed source-role/grain and semantic-repeatability issues. The private harness changed authorization-store databases between executions, so 17 already-transmitted semantic calls were repeated. This produced useful experimental evidence but remains an execution defect, not desired production behaviour. The exact first-run provider spend was not retained; corrected-run cost must not be treated as total factual spend.

## 5. Reliability and replay position

Semantic validity, semantic repeatability, graph/structural repeatability and input robustness are separate dimensions. Valid persisted ModelResults are reused for unchanged material; technical replication is deliberate evaluation, not retry. Stochastic rediscovery does not create or remove governed subjects without evidence and governance.

## 6. Open work and constraints

The project is not ready for an unbounded fresh paid cohort. Reliability methodology, durable cross-store authorization continuity, accounting telemetry and source-role/grain evaluation remain active topics. Builder PR #15 remains frozen/open/unmerged archaeology. Private evidence, raw responses, runtime databases and repeatability artefacts remain private. No automatic public subject promotion is implied by Fresh-18 output.

## 7. North Star realignment and halted Top-100 run

Program/service v3/v3.1 is one foundation-domain implementation, not the whole product. Controlled model-tier experiments found Terra improved execution reliability over Luna, while Sol did not establish routine value.

A program/service-only Top-100 Terra run using literal ACNC donation ranks 1–100 was begun and intentionally halted during roadmap realignment. It produced 60 new Terra response artefacts and 3 exact prior Terra-A reuses: 60/63 structurally valid results, 54/63 whole-output quote-valid results and 287 parsed proposals. Under the program-task condition, 72 packets were `COMPLETE_ENOUGH` and 28 were `PARTIAL`; this was task-specific and is not whole-card completeness. One in-flight attempt had indeterminate billing state. Valid results remain reusable Section-3 material where semantic identity permits. No exact cost total is asserted for the interrupted run.

The next architectural objective is complete-card reality testing from reusable charity evidence corpora. Broad cohort scaling no longer means scaling a single semantic profile by default.

## 8. Product-family state

CharityGraph now has an approved four-product model:

- **Builder** constructs governed knowledge and release candidates;
- **Data** publishes reusable governed public data and shared product authority;
- **Viewer** provides human inspection, navigation and contextual entry points; and
- **Playbooks** publishes governed, open analytical methods for applying general-purpose AI to CharityGraph data.

Builder, Data, Viewer and Playbooks repositories now exist. Playbooks is approved as a fourth product with initial contract, base policy, contribution guidance, schema and example at `6466e04`; no production Playbook catalogue, hosted inference/runtime, Viewer integration or API/MCP integration has been implemented.

## 9. Current Playbooks documentation state

The active documentation branch records, subject to eventual merge:

- canonical product recognition of Playbooks;
- governance and authority boundaries;
- approved decision `CG-D030`;
- CC BY 4.0 licensing intent; and
- agent, privacy and feedback boundaries.

These documentation changes do not alter the Builder/Data full-card critical path or claim a production Playbooks catalogue, hosted inference or Viewer integration.
