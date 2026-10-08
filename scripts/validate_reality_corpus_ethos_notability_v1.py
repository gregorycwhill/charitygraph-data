"""Provider-free integrity check for the frozen Ethos/Notable History corpus."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
PATH = ROOT / "golden" / "reality-corpus-ethos-notability-v1.json"
MATRIX = ROOT / "REALITY_CORPUS_ETHOS_NOTABILITY_V1.md"
EXPECTED_SHA256 = "f49735791652d3a65ab627138662653c76a615496f0f154a325bf8729d662c1b"

def main() -> None:
    raw = PATH.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256, "frozen corpus bytes changed"
    corpus = json.loads(raw)
    cases = corpus["cases"]
    assert corpus["version"] == "1.0.0" and len(cases) == 14
    assert [c["id"] for c in cases] == [f"RC-{i:02d}" for i in range(1, 15)]
    matrix = MATRIX.read_text(encoding="utf-8")
    assert all(case["id"] in matrix for case in cases), "human gold matrix and machine corpus disagree"
    assert sum(c["kind"] == "real" for c in cases) == 3
    assert sum(c["kind"] == "synthetic" for c in cases) == 11
    for case in cases:
        if case["kind"] == "real":
            assert set(case["evidence"]) == {"path", "ids"} and case["evidence"]["ids"]
            assert case.get("source_observed_at")
            assert (ROOT / case["evidence"]["path"]).is_file()
        else:
            assert "evidence" not in case
    coverage = " ".join(c.get("coverage", "") for c in cases)
    for required in ("formal affiliation", "historical/current", "commitment", "parent scope", "founding", "recognition", "section 16", "equivalence"):
        assert required in coverage
    print("reality corpus ethos/notability v1: 14 cases (3 real, 11 synthetic): PASS")

if __name__ == "__main__":
    main()
