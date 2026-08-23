# Public contract 0.5 schema reference

**Status:** Reference for an implemented compatibility contract  
**Scope:** detailed schema and example material for public release v0.5.0-2026-08-15  
**Canonical narrative authority:** [PUBLIC_CONTRACT_0_5.md](PUBLIC_CONTRACT_0_5.md)

This path is retained for compatibility with existing links. It is not a future-schema proposal and must not be used to define Builder's internal architecture.

The machine-readable authority remains the schemas, examples, capability registry and immutable manifest in the named public release. Public contract 0.5 retains its legacy public subject key and layout where the immutable release requires them. New internal work uses the neutral subject_id concept only behind an explicit future-contract migration.

Future release publication identity requirements are specified separately in [FUTURE_RELEASE_MANIFEST_CONTRACT.md](FUTURE_RELEASE_MANIFEST_CONTRACT.md) and its schema proposal. They do not modify public contract 0.5.

The detailed pre-implementation schema design is retained at [docs/history/pre-product-documentation-rewrite-2026-08-23/PUBLIC_SCHEMA_VNEXT_SPEC.md](docs/history/pre-product-documentation-rewrite-2026-08-23/PUBLIC_SCHEMA_VNEXT_SPEC.md). It is historical reference, not current executable instruction.

Current constraints:

- do not modify schemas, schema paths, IDs or immutable release bytes;
- do not infer a new public contract from Builder vNext terminology;
- preserve source-native records, evidence, coverage and compatibility semantics exactly as release-owned artefacts;
- require a separately approved, versioned migration for any future public-contract change.