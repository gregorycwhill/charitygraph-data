# Scale S0 execution attempt 2 — halted before crossing

**Terminal state: `S0_HALTED`**

## Authority and recovery

This fresh attempt was created after the approved clean-restart decision. The original attempt remains `S0_INCONCLUSIVE` and crossed no live execution boundary. Data PR #34 remains open, unmerged, and historical.

- Builder canonical implementation: `f3ea027c6159344d82b075304e5d33bf0b30c7c7`
- Data canonical after recovery authority: `870fe92502583a85133005bc5ebab62154920e22`
- Migration level: 18
- Bridge state: `S0_ACQUISITION_PACKET_BRIDGE_CERTIFIED`
- Mandate: `D00C4B3FEE234B96DB133C40C59D0206B00D5277F075DCF1384F9376DD74E632`
- Policy bundle: `6AACC79311CD0364CAA4DBCAE235B7ECFD4DD8F9B5B139CAC3D62564F2F51E81`
- Rights policy: `0054FFBD3EA00A36D84278957034BD4CFF0993CE239ED3D01C1F5CE58C530FF1`
- Task registry: `999F52B4A8ECFE82F53B76E6AF429B757409E87503B8478DF6FE5ED9EE3EE7BC`
- Population policy: `45110269021C495B4970F310D093297A11413DD36F5F0B03B291AC6883F62D8D`

Fresh execution identity: `s0-execution-attempt-2` / `run:s0-attempt-2-20260918`.

## Exact mandated population

World Vision Australia (`28004778081`); The Smith Family (`28000030179`); Medecins Sans Frontieres Australia (`74068758654`); Sunrise Foundation (`37646526132`); Australian Red Cross Society (`50169561394`); Noongar Boodja Trust (`47613674461`); Bush Heritage Australia (`78053639115`); Greenpeace Australia Pacific (`61002643852`). No ninth subject was added.

## Binding failure

The certified Builder runtime can persist mandate, policy, source-plan, snapshot, representation, corpus, bundle and packet material, and can register a run with an opaque `configuration_hash`. It has no durable runtime field/table for the required Builder implementation SHA, canonical Data SHA, migration/certification identity, or an independently inspectable binding tying those values to the fresh run. Encoding them only inside an opaque configuration hash would not satisfy the explicit identity-binding requirement.

The brief requires stopping rather than repairing production architecture when this capability is absent. Therefore no source plan was executed, no network boundary was crossed, and no run registration, source acquisition, reservation, provider call, candidate, review, promotion or runtime mutation was performed.

## Disposition

Recovery remains authorised in principle, but this attempt is halted pending a separately authorised architecture change that can durably bind implementation identity. No policy or mandate was changed. S0 is not resumed automatically.
