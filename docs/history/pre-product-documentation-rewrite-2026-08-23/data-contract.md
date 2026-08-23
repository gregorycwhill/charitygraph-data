# CharityGraph data contract

The post-0.5 CharityGraph contract is organised around source-native records, resolved subject bindings, canonical observations, evidence, taxonomies, and derived projections. Core neutral concepts are `entity_id`, `source_record_id`, `subject_binding_id`, `observation_id`, `evidence_id`, `taxonomy_id`, `schema_version`, `claim_basis`, and `extraction_method`.

`claim_basis` states the epistemic basis of a claim; `extraction_method` states how the relevant material was obtained or interpreted. They are not interchangeable.

The 0.5 release is immutable legacy material. Its `causebase_id` field is accepted only as a deprecated compatibility alias while the successor contract is introduced.
