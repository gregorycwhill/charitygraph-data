import copy
import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / "release-manifest.schema.json").read_text(encoding="utf-8"))
EXAMPLE = json.loads((ROOT / "examples" / "release-manifest.valid.json").read_text(encoding="utf-8"))

_RELEASE_PATH = re.compile(r"^releases/[A-Za-z0-9][A-Za-z0-9._-]*$")
_COMMIT = re.compile(r"^[0-9a-f]{7,64}$")


def _absolute_https(value):
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and not any(ch.isspace() for ch in value)


def validate_manifest(manifest):
    if manifest.get("contract_version") == "0.5":
        raise ValueError("future manifest cannot use contract 0.5")
    identity = manifest["publication_identity"]
    if identity["publisher_name"] != "CharityGraph":
        raise ValueError("publisher")
    if identity["canonical_data_repository"] != "https://github.com/gregorycwhill/charitygraph-data":
        raise ValueError("repository")
    if not _RELEASE_PATH.fullmatch(identity["immutable_release_path"]):
        raise ValueError("release path")
    if identity["data_license_identifier"] != "CC-BY-4.0":
        raise ValueError("licence")
    for field in ("license_url", "upstream_rights_caveat_url"):
        if not _absolute_https(identity[field]):
            raise ValueError(field)
    commitments = identity["editorial_commitments"]
    if not commitments["identifier"] or not commitments["version"] or not _absolute_https(commitments["url"]):
        raise ValueError("commitments")
    builder = identity["producing_builder"]
    if not builder["version"] or (builder.get("commit") is not None and not _COMMIT.fullmatch(builder["commit"])):
        raise ValueError("builder")
    if not identity["attribution_guidance"]:
        raise ValueError("attribution")
    return True


class FutureManifestContractTests(unittest.TestCase):
    def test_valid_example_and_serialised_names(self):
        self.assertTrue(validate_manifest(EXAMPLE))
        identity_schema = SCHEMA["properties"]["publication_identity"]
        self.assertEqual(set(EXAMPLE["publication_identity"]), set(identity_schema["properties"]))
        self.assertEqual(set(EXAMPLE["publication_identity"]["editorial_commitments"]), set(identity_schema["properties"]["editorial_commitments"]["properties"]))

    def assert_rejected(self, mutate):
        candidate = copy.deepcopy(EXAMPLE)
        mutate(candidate)
        with self.assertRaises(ValueError):
            validate_manifest(candidate)

    def test_invalid_repository_path_attribution_urls_commit_and_contract_are_rejected(self):
        cases = [
            lambda m: m["publication_identity"].__setitem__("canonical_data_repository", "https://example.invalid/data"),
            lambda m: m["publication_identity"].__setitem__("immutable_release_path", "releases/../private"),
            lambda m: m["publication_identity"].__setitem__("immutable_release_path", "C:/release"),
            lambda m: m["publication_identity"].__setitem__("attribution_guidance", ""),
            lambda m: m["publication_identity"].__setitem__("license_url", "not-a-url"),
            lambda m: m["publication_identity"].__setitem__("producing_builder", {"version": "0.2.0", "commit": "NOT-HEX"}),
            lambda m: m.__setitem__("contract_version", "0.5"),
        ]
        for mutate in cases:
            with self.subTest(mutate=mutate):
                self.assert_rejected(mutate)


if __name__ == "__main__":
    unittest.main()