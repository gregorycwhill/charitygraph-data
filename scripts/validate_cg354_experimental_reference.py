"""Mechanical integrity check for the CG354 source-only experimental reference.

This code deliberately does not interpret source prose or labels.  It checks
case/split completeness, projection separation, declared aggregate counts and
the negative-access attestation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
BASE = ROOT / "golden" / "empirical-ethos-notability-v1"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    reference_path = BASE / "cg354-experimental-reference.json"
    workshop_path = BASE / "cg354-workshop-reference.json"
    blind_path = BASE / "cg354-blind-reference.json"
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    workshop = json.loads(workshop_path.read_text(encoding="utf-8"))
    blind = json.loads(blind_path.read_text(encoding="utf-8"))
    cases = reference["cases"]
    assert len(cases) == 15
    assert len({row["case_id"] for row in cases}) == 15
    assert reference["status"] == "EXPERIMENTAL_ADJUDICATION"
    assert reference["independence"] == {**reference["independence"], "product_semantic_outputs_read": False, "candidate_bundles_read": False, "raw_provider_responses_read": False, "provider_calls": 0}
    by_split = {split: [row for row in cases if row["split"] == split] for split in ("workshop", "blind")}
    assert [row["case_id"] for row in by_split["workshop"]] == workshop["case_ids"]
    assert [row["case_id"] for row in by_split["blind"]] == blind["case_ids"]
    assert set(workshop["case_ids"]).isdisjoint(blind["case_ids"])
    ethos = {split: sum(len(row["ethos"].get("items", [])) for row in rows) for split, rows in by_split.items()}
    history = {split: sum(len(row["history"].get("items", [])) for row in rows) for split, rows in by_split.items()}
    assert ethos["workshop"] == workshop["evaluable_ethos_items"] == 0
    assert history["workshop"] == workshop["evaluable_history_events"] == 0
    assert ethos["blind"] == blind["evaluable_ethos_items"] == 1
    assert history["blind"] == blind["evaluable_history_events"] == 0
    print(json.dumps({
        "valid": True,
        "reference_sha256": digest(reference_path),
        "workshop_projection_sha256": digest(workshop_path),
        "blind_projection_sha256": digest(blind_path),
        "evaluable": {"workshop": {"ethos": ethos["workshop"], "history": history["workshop"]}, "blind": {"ethos": ethos["blind"], "history": history["blind"]}},
        "provider_calls": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
