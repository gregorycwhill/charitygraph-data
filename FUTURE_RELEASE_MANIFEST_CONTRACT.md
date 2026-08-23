# Future Release Manifest and Publication Identity Contract

**Status:** Canonical future-release requirement / schema proposal
**Version:** 0.1-draft
**Date:** 2026-08-24
**Scope:** future public release candidates only; not public contract 0.5

## Purpose

A future CharityGraph release must carry machine-readable publication identity and reuse metadata. This contract does not alter, validate or regenerate the immutable `releases/v0.5.0-2026-08-15` release. Public contract 0.5 remains valid without these fields.

## Required manifest metadata

Future release manifests must include `publication_identity` with:

- `publisher_name`: `CharityGraph`;
- `canonical_data_repository`: `https://github.com/gregorycwhill/charitygraph-data`;
- `immutable_release_path`: the repository-relative immutable path, such as `releases/v0.6.0-YYYY-MM-DD`;
- `data_license_identifier`: `CC-BY-4.0`;
- `license_url`: the applicable licence URL;
- `attribution_guidance`: concise reusable attribution guidance;
- `upstream_rights_caveat_url`: the canonical upstream-rights caveat;
- `editorial_commitments`: identifier, version and canonical URL for `PUBLIC_COMMITMENTS.md`;
- `producing_builder`: required object containing a required Builder version and an optional producing commit.

The canonical repository and immutable release path are the publication identity. A manifest must not require the Data commit that contains that manifest, avoiding circular self-reference. The `producing_builder` object and its version are always required. Only the producing commit may be absent or null when no coherent commit exists.

## Representation availability

The same publication identity must be discoverable from the release manifest and exposed or linked by future JSON, Markdown and bulk distribution metadata. Consumers must be able to identify the licence, attribution guidance, release path and upstream-rights caveat without executing Viewer code.

## Compatibility and validation

The future schema proposal is [schemas/future/release-manifest.schema.json](schemas/future/release-manifest.schema.json). A future candidate is invalid when `publication_identity` is absent or incomplete. Existing 0.5 validators continue to validate the immutable contract without requiring this metadata.
