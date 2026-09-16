# Phase 5 Tranche C5 — North Star v0.2 cross-cutting scope, time and epistemic boundaries

**Status:** completed bounded retained-evidence representation test; no execution authority.
**Date:** 16 September 2026. **Active projection:** `north-star-v0.2`.

## Cohort and question

The tested risk is scope broadening: a true observation becomes false when its subject, population role, organisational role, status, time, source role or evidence state is widened. No sources were acquired or sent to a provider.

| Retained case | Required distinction and locator |
|---|---|
| Australian Red Cross Society FY2022–23 | `archive/processed/reality-spike/2026-08-10/report-extracts/50169561394-2022-23.json`: p2 legal Society/ABN/two operating divisions; p4 mixed members-volunteers and staff; p5 Board/Lifeblood Board/executive and dated CEO death; p7 sites and geography. |
| Fitted for Work FY2024 | `archive/processed/reality-spike/2026-08-10/report-extracts/78126256862-2023-24-full.json`: pp23–24 served clients, services, demographics and observed geography; p41 program volunteers/mixed staff-volunteer count; pp53–58 Board, committees and team snapshots. |
| APNIC Foundation FY2025 | `archive/processed/phase2b/2026-08-14/report-extracts/24646643156-a2a8898a4f64ceade90b63f11bb3939a63c992b7e4c21a00c9c6ed7a86fb5e60.json`: p1 Board/CEO; p9 named population/countries; p28 directors/officers/audit context. |
| ACNC authority and absence controls | `archive/sources/regulator/acnc-ais-2023/2026-08-10/source.json`, its CSV, `archive/processed/reality-spike/2026-08-10/acnc-name-resolution.json`, and `archive/processed/phase2a/2026-08-10/phase2a1-corrective-reruns.json` preserve issuing-authority limits and unavailable descriptive evidence. |
| Federation/history controls | `archive/processed/reality-spike/2026-08-10/federated-relationship-findings.md` and `archive/processed/phase2b/2026-08-14/report-extracts/49079016738-5848f21901bd747f35facb46fe653144e92a334b8047cb0b6592e54ed89c4d06.json` pp9,12,15 prevent brand/entity and historical/current collapse. |

No retained substantive conduct matter was suitable as a positive governed claim. Existing typed §16 conduct architecture is used only for explicit coverage/knowability.

## Terra adjudication and result

Primary/adversarial inventory: **41 propositions — ACCEPT 20, NARROW 8, REJECT 5, KNOWABILITY_ONLY 8.** The adversarial pass required: Lifeblood division is not a program/legal entity; address/site/operating/delivery/reach geography do not collapse; reached/served/participating/mentioned/consulted populations remain distinct; Board/committee/executive/staff/volunteer/member/FTE/capability remain distinct; allegation/investigation/finding/response/status remain distinct; historical facts are not current facts; observation/retrieval time is not freshness/effective time; and newer source is not automatically a correction.

| Section | Cluster result | Overall disposition | Exact residual |
|---:|---|---|---|
| 1 | legal authority, operating-unit and missingness control | PARTIAL | no positive branch/brand or rename-versus-succession case |
| 5 | population/geography role, scope and reporting-period control | PARTIAL | intended/eligible/consulted evidence thin |
| 9 | Board/committee/executive and snapshot-time control | PARTIAL | no complete register, authority or tenure case |
| 10 | staff/volunteer/mixed workforce role, measure, unit, scope and period control | PARTIAL | no FTE/contractor/labour-hire/partner-personnel case |
| 16 | process-state contract and honest coverage | KNOWABILITY_ARCHITECTURE_REQUIRED | no retained substantive matter; silence is never a clean record |
| 17 | dated event and historical/current separation | PARTIAL | no clear legal merger/split/succession case |
| 20 | source, locator, role, time, lineage and coverage | PARTIAL | no canonical freshness policy or positive correction/dispute case |

## Representation and boundary decision

`SubjectRecord`, `ScopeRecord`, `PartyRole`, `Observation`, `ObservationTime`, source/evidence records, lineage, `CardEvidence` and coverage are reused. The bounded v0.2 C5 adapter adds typed identity, population/geography, governance, workforce, historical-event and provenance-event inputs. The existing typed §16 contract is reused; C5 creates no conduct assertion. Every input projects one observation and one intended section only. There is no automatic assignment to §§3, 6, 11 or v0.1. Duplicate explicit coverage for the same subject, contract and section is rejected.

§20 uses distinct meanings for `source_correction`, `source_supersession`, `charitygraph_correction`, `source_disagreement` and `real_world_change`. A newer source does not establish any of them. Historical evidence can remain valid for its time without being fresh for a current-state question; retrieval date is not effective date; no generic freshness interval is invented.

No section is `SUPPORTED_BY_EXISTING_PROOF`. No new evidence or provider work is decision-relevant before review of these retained-evidence controls.

Provider calls: `0`. Source acquisitions: `0`. Semantic executions: `0`. Candidates: `0`. Promotions: `0`. Runtime mutations: `0`. Top-100: `0`. Phase 6 reopening: `0`.
