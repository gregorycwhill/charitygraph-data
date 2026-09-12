# Direct Service V1.2 experiment decision

**Status:** Approved empirical decision and tranche closeout

**Date:** 12 September 2026

**Scope:** Internal Builder Direct Service representation; not a public Data contract or governed-promotion decision

**Supersedes:** V1.2 candidate/pending-execution statements as current status; historical V1.1 results remain unchanged

## Decision

Select Direct Service V1.2's section-array wire representation and its dedicated
wire DTO/converter for future Direct Service work. The V1.1 representation defect
is resolved for purposes of proceeding with implementation. V1.1 remains
historical evidence and must not be rewritten as if it used the V1.2 contract.

The experiment disposition is **`V1_2_REPRESENTATION_FIX_SUPPORTED`**. This is a
bounded, non-random live sample of 14 responses. It does not claim statistical
significance, universal semantic quality, production readiness, governed data
promotion, or public release.

## Evidence

| Measure | Direct Service V1.1 historical baseline | Direct Service V1.2 live sample |
|---|---:|---:|
| Provider-executed completed responses | 42 | 14 |
| Directly valid | 19 | 14 |
| Deterministically recovered | 22 | 0 |
| Semantically unusable | 1 | 0 |
| Responses affected by representation problems | 20 | 0 |
| Illegal section/type proposition instances | 32 | 0 |
| Propositions retained | — | 49 |
| Propositions discarded | — | 0 |

V1.2's 14 provider-executed responses comprise one historical live canary and
13 final eligible executions. The original continuation population was 18:

- 13 newly executed eligible requests;
- 1 local `pre_send_validation` control failure, abandoned before provider
  crossing (zero crossings; not a semantic failure); and
- 3 economic exclusions, whose corrected conservative hard maxima were AUD
  `0.269531`, `0.300608`, and `0.462635`, each above the binding AUD `0.25`
  per-request ceiling (zero crossings; not semantic failures).

Do not reopen these four non-executions solely to increase sample size. Discovery
V2 remains complete and is not reopened by this decision.

## Economics and authority

The historical successful canary cost USD `0.113160` / AUD `0.172003`. The final
13 cost USD `0.324526` / AUD `0.493287`. Total V1.2 provider cost was USD
`0.437686` / AUD `0.665290`. The corrected conservative exposure for the final
13 was USD `0.578307` / AUD `0.879033`; all unused reservations were released.
Amendment 3 remained active. Amendment 4 was never activated. No source
acquisition or governed promotion occurred.

## Durable evidence

Primary empirical source: runtime report
`C:\CharityGraph-runtime\phase5-top100-direct-service-v1.2-cutover-v1\phase5-direct-service-v1.2-final-report-2026-09-12.json`
SHA-256: `588707746dee2de90a14ed099d13235a34d3b18bf88e9f43008c22712c047777`.

The report and raw runtime artefacts remain outside Git. This decision records
the compact aggregate result only. The Direct Service experimental tranche is
complete; the umbrella Phase 5 Top-100 full-card objective remains active and
Phase 6 remains gated on that broader objective.
