# v0.2 review findings

The preserved v0.1 base contains 53 questions with tier counts A/B/C = 12/23/18. Seven workflow-driven questions bring the retained question set to 60. Twelve correction challenges are retained separately under the same `SemanticDemandScenario` model. The correction set includes accepted replacements, qualifications, holds, rejected/insufficient challenges, projection-only repair, and systemic-remediation escalation.

Primary domains drive complexity; supporting evidence and coverage domains do not inflate semantic-domain counts. All 20 North Star domains are covered across primary/supporting fields. Public/donor/participant and charity-insider/adviser are explicit roles. Analytical lenses are separate and reusable; there is no corrector persona.

The validator normalises the preserved pilot into the v0.2 common structure for machine validation, preserving its wording, typed slots, signatures and answerability. It does not silently mutate the pilot source. No public correction API, UI, queue, override store, North Star contract or external provider activity is introduced.

Correction-to-regression promotion is a reviewed, anonymised, generalised step; it is never automatic ingestion of private challenge content.
