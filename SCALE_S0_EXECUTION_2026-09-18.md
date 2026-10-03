# Scale S0 execution record — 18 September 2026

**Status:** `S0_INCONCLUSIVE` — pre-execution Factory capability stop

## Frozen execution inputs

| Input | Identity |
|---|---|
| Canonical Builder at execution start | `b3937b0ee03d50648cdec5563e8c0b9ae312e80a` |
| Canonical Data at execution start | `44011dffbec86e066ea3bb033a6a9270058df18e` |
| Authorisation decision | `SCALE_S0_AUTHORISATION_DECISION_2026-09-18.md#S0_AUTHORISED` |
| Authorised mandate | `SCALE_S0_MANDATE_AUTHORISED_V2.yaml` / `D00C4B3FEE234B96DB133C40C59D0206B00D5277F075DCF1384F9376DD74E632` |
| Candidate/shadow mandate | `9E5F41DCC74D95F1D939927C1710949F416495E850A37098AA76F99C2811A386` |
| Policy bundle | `6AACC79311CD0364CAA4DBCAE235B7ECFD4DD8F9B5B139CAC3D62564F2F51E81` |
| Task registry | `999F52B4A8ECFE82F53B76E6AF429B757409E87503B8478DF6FE5ED9EE3EE7BC` |
| Population | `45110269021C495B4970F310D093297A11413DD36F5F0B03B291AC6883F62D8D` |
| Sampling seed | `scale-s0-balanced-2026-09-18-v1` |

The frozen policy bundle, population, registry, source universe, reservation
policy, review/sampling policy, promotion policy and halt policy were not
changed after the authorisation merge.

## Required capability stop

No certified Factory path can execute the authorised S0 acquisition sequence.
The existing governed ACNC identity bootstrap accepts only a frozen cohort of
exactly 100 subjects. Using it would create subjects beyond the authorised
eight. The available generic ACNC-profile script writes raw JSON and does not
create governed source authorisations, source records with rights bindings,
representation records, a frozen corpus, durable S0 packets, or the required
reservation/candidate/review lifecycle.

The canonical authorisation-package loader also resolves only the historical
shadow-mandate filename. A real S0 driver would therefore require Builder code
to bind the authorised mandate and orchestrate the certified durable APIs. That
is a material Factory/authority defect. The S0 authority prohibits a live
architecture repair, so no source acquisition, durable S0-run registration,
task planning, provider reservation, provider transmission, candidate creation,
review, promotion or projection was attempted.

No hard-halt event was recorded because no governed run could be registered and
no defined halt trigger occurred. `S0_INCONCLUSIVE` is the honest terminal
state: retained evidence cannot support execution completion, failure of the
completion gate after execution, or a hard halt.

## Frozen authorised subjects

1. World Vision Australia — `28004778081`
2. The Smith Family — `28000030179`
3. Medecins Sans Frontieres Australia — `74068758654`
4. Sunrise Foundation — `37646526132`
5. Australian Red Cross Society — `50169561394`
6. Noongar Boodja Trust — `47613674461`
7. Bush Heritage Australia — `78053639115`
8. Greenpeace Australia Pacific — `61002643852`

## Observed execution accounting

| Measure | Observed value |
|---|---:|
| Durable execution run ID | none — registration blocked before mutation |
| Slice ID | `scale-s0-shadow-option-b-8` (authorised mandate only; not registered) |
| Sources planned/acquisition attempts/successes | 0 / 0 / 0 |
| Blocked or technically withheld sources | 0 / 0 |
| Structured, website, annual-report, specialist acquisitions | 0 / 0 / 0 / 0 |
| Frozen documents / visual PDFs / representation failures | 0 / 0 / 0 |
| Candidate task instances / applicable instances / semantic tasks / human-only tasks | 0 / 0 / 0 / 0 |
| Physical provider calls (Luna / Terra) | 0 (0 / 0) |
| Retries, repairs, ambiguous sends | 0 / 0 / 0 |
| Input tokens / output tokens | 0 / 0 |
| Total / strong-model spend | USD 0.00 / USD 0.00 |
| Maximum single-request reservation | USD 0.00 |
| Candidates generated/rejected/corrected | 0 / 0 / 0 |
| Mandatory review/sample/audit/human-review outstanding | 0 / 0 / 0 / 0 |
| Semantic/deterministic promotions | 0 / 0 |
| False scope/absence, taxonomy, endpoints, current-state errors | 0 / 0 / 0 / 0 |
| Hard halts / restart-recovery incidents | 0 / 0 |
| Internal projections | 0 of 8 |

No result content is canonical. This execution branch and any result PR remain
unmerged; public release remains zero, and S1 and Top-100 continuation remain
unauthorised.
