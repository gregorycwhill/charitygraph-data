# CharityGraph Current State

**Status date:** 28 August 2026

**Status:** Baseline after Fresh-18 semantic-reliability analysis

## 1. Repositories

| Component | Repository | Current `main` | State |
|---|---|---|---|
| Builder | `gregorycwhill/charitygraph` | `c8806c869d62b38cd00eaf9dcea1e6a8a4eaa4c1` | Production foundations and native discovery v2 available |
| Data | `gregorycwhill/charitygraph-data` | `e7882a05b9024cfb4ac0d749475a401c6ba69db5` | Canonical contracts, releases and governance |
| Viewer | `gregorycwhill/charitygraph-viewer` | `cd6f3720f664a29e0ca7ed8be19797e573fcdfc8` | Existing deployed Viewer; unchanged by this state update |

## 2. Immutable public release

Public contract 0.5 remains immutable:

- release: `v0.5.0-2026-08-15`;
- manifest SHA-256: `01D047484909B8E15941D5023749ECDB6811FA472CB04BD1B9E0272935050DFB`.

No v0.5 release files, schemas or ranking snapshots were changed.

## 3. Current production capabilities

The implemented foundation includes evidence/source registry, knowledge persistence, taxonomy/pre-run foundations, exactly-once semantic-call authorization, durable ModelTask/ModelResult evidence binding, multi-proposal native program/service discovery v2, operational-status separation, governed ProgramCandidate -> SubjectRecord promotion, production native-discovery execution, v2 parser dispatch, and canonical ACNC 2024 AIS donation ranking in Data.

## 4. Fresh-18 observation

A mechanically selected, heterogeneous 18-charity cohort was processed using frozen evidence and `program_service_discovery/v2` with GPT-5.6 Luna. The final run produced 17 successful semantic outputs, 97 proposals and 80 projected candidates; no subject promotion or classification was performed.

An accidental 17-pair repeated-measures baseline now informs evaluation design. It exposed source-role/grain and semantic-repeatability issues. The private harness changed authorization-store databases between executions, so 17 already-transmitted semantic calls were repeated. This produced useful experimental evidence but remains an execution defect, not desired production behaviour. The exact first-run provider spend was not retained; corrected-run cost must not be treated as total factual spend.

## 5. Reliability and replay position

Semantic validity, semantic repeatability, graph/structural repeatability and input robustness are separate dimensions. Valid persisted ModelResults are reused for unchanged material; technical replication is deliberate evaluation, not retry. Stochastic rediscovery does not create or remove governed subjects without evidence and governance.

## 6. Open work and constraints

The project is not ready for an unbounded fresh paid cohort. Reliability methodology, durable cross-store authorization continuity, accounting telemetry and source-role/grain evaluation remain active topics. Builder PR #15 remains frozen/open/unmerged archaeology. Private evidence, raw responses, runtime databases and repeatability artefacts remain private. No automatic public subject promotion is implied by Fresh-18 output.
