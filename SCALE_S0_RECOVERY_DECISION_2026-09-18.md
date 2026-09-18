# Scale S0 recovery authorisation — 2026-09-18

The first authorised execution attempt remains historically recorded as `S0_INCONCLUSIVE`. It crossed no live execution boundary: run registration, acquisition, reservation, provider, candidate, review and promotion counts remained zero. Data PR #34 remains the separate historical, open and unmerged record.

The certified implementation now provides the missing acquisition-to-packet bridge:

`S0_ACQUISITION_PACKET_BRIDGE_CERTIFIED`

Certified Builder implementation: `f3ea027c6159344d82b075304e5d33bf0b30c7c7`

Canonical Data state at approval: `270268c7f43db934d1ab33da6350f852ac28bd64`

## Existing immutable authority

- Mandate hash: `D00C4B3FEE234B96DB133C40C59D0206B00D5277F075DCF1384F9376DD74E632`
- Policy bundle hash: `6AACC79311CD0364CAA4DBCAE235B7ECFD4DD8F9B5B139CAC3D62564F2F51E81`
- Rights policy hash: `0054FFBD3EA00A36D84278957034BD4CFF0993CE239ED3D01C1F5CE58C530FF1`
- Task registry hash: `999F52B4A8ECFE82F53B76E6AF429B757409E87503B8478DF6FE5ED9EE3EE7BC`
- Population policy hash: `45110269021C495B4970F310D093297A11413DD36F5F0B03B291AC6883F62D8D`

## Product-owner decision

`S0_RECOVERY_AUTHORISED_CLEAN_RESTART`

Recovery creates a fresh execution attempt and does not resume or mutate attempt 1. All existing S0 limits and the public-release prohibition remain unchanged. This record adds implementation/recovery authority only; it does not modify the mandate or policy package.
