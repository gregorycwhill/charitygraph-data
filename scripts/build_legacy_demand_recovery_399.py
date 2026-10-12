"""Mechanical extractor for CG399 legacy-demand recovery.

This script does not author or infer demand meaning.  It copies explicit fields
from two historical Data catalogue snapshots and the frozen CG395 benchmark
matrix, records their provenance, and validates the resulting 74-row ledger.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "history" / "legacy-demand-recovery-399"
HISTORICAL_COMMIT = "587ee2c23734f82e111de292971c01eddb08bf5a"
INITIAL_COMMIT = "2b5a7d77be5d74dac84a0d6a8c85acf2220abc23"
HISTORICAL_PATH = "docs/semantic-demand-catalogue-v0.2/scenarios.json"
INITIAL_PATH = "docs/semantic-demand-catalogue-v0.1/pilot-questions.json"
MATRIX = Path(r"C:\Users\grego\OneDrive\Documents\GitHub\CharityGraph\artifacts\g2-proposition-adjudication-benchmark-395\demand-coverage-matrix.json")
BENCHMARK = Path(r"C:\Users\grego\OneDrive\Documents\GitHub\CharityGraph\artifacts\g2-proposition-adjudication-benchmark-395\benchmark-manifest.json")


def git_show(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def provenance(**items: str) -> dict:
    return items


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    current_raw = git_show(HISTORICAL_COMMIT, HISTORICAL_PATH)
    initial_raw = git_show(INITIAL_COMMIT, INITIAL_PATH)
    matrix_raw = MATRIX.read_bytes()
    benchmark_raw = BENCHMARK.read_bytes()
    current = {item["id"]: item for item in json.loads(current_raw)}
    initial = {item["id"]: item for item in json.loads(initial_raw)}
    matrix = json.loads(matrix_raw)
    benchmark = json.loads(benchmark_raw)
    benchmark_questions = {}
    for cell in benchmark["cells"]:
        benchmark_questions.setdefault(cell["demand_id"], cell["proposition_question"])

    rows = []
    for source_row in matrix["rows"]:
        demand_id = source_row["demand_id"]
        number = int(demand_id.split("-")[1])
        common = {
            "legacy_id": demand_id,
            "legacy_family_label": source_row["demand_family"],
            "legacy_benchmark_cells": source_row["cell_ids"],
            "historical_variants": [],
            "explicit_semantic_hints": [],
            "confidence": "LOW",
            "limitations": [],
        }
        matrix_prov = provenance(
            source_family="existing CharityGraph run evidence (CG395)",
            repository="local CharityGraph execution archive",
            ref="CG395 frozen artifact",
            path=str(MATRIX),
            locator=f"/rows/[demand_id={demand_id}]",
            sha256=sha256(matrix_raw),
            snippet=source_row["demand_family"],
        )
        if number <= 53:
            old_id = f"SDC-{number:02d}"
            exact = current[demand_id]
            variants = []
            if old_id in initial:
                old = initial[old_id]
                variants.append(
                    {"chronology": "2026-10-06 initial pilot", "record": old,
                     "provenance": provenance(source_family="Data Git history", repository="charitygraph-data", ref=INITIAL_COMMIT, path=INITIAL_PATH, locator=f"/[id={old_id}]", sha256=sha256(initial_raw), snippet=old["template"])}
                )
            variants.append(
                {"chronology": "2026-10-07 curated historical catalogue", "record": exact,
                 "provenance": provenance(source_family="Data Git history", repository="charitygraph-data", ref=HISTORICAL_COMMIT, path=HISTORICAL_PATH, locator=f"/[id={demand_id}]", sha256=sha256(current_raw), snippet=exact["surface_question"])}
            )
            common.update({
                "evidence_status": "RECOVERED_EXACT",
                "confidence": "HIGH",
                "historical_variants": variants,
                "explicit_semantic_hints": [
                    {"kind": "full historical scenario record", "value": exact, "provenance": provenance(source_family="Data Git history", repository="charitygraph-data", ref=HISTORICAL_COMMIT, path=HISTORICAL_PATH, locator=f"/[id={demand_id}]", sha256=sha256(current_raw), snippet=exact["surface_question"])},
                ],
                "limitations": (["The initial pilot used the explicitly recorded zero-padded-short ID %s; this ledger mechanically normalizes only its numeric spelling to the CG395 ID %s." % (old_id, demand_id)] if old_id in initial else ["No v0.1 pilot record exists for this ID; exact recovery is from the later v0.2 historical catalogue."]) + ["Historical scenario records are legacy evidence, not current product authority."],
            })
        else:
            common.update({
                "evidence_status": "HINT_ONLY",
                "explicit_semantic_hints": [
                    {"kind": "CG395 family label", "value": source_row["demand_family"], "provenance": matrix_prov},
                    {"kind": "CG395 generic proposition-question template", "value": benchmark_questions[demand_id], "provenance": provenance(source_family="existing CharityGraph run evidence (CG395)", repository="local CharityGraph execution archive", ref="CG395 frozen artifact", path=str(BENCHMARK), locator=f"/cells/[demand_id={demand_id}][slot=1]/proposition_question", sha256=sha256(benchmark_raw), snippet=benchmark_questions[demand_id])},
                ],
                "limitations": ["No item-specific executable definition, parameter contract, subject scope, or evidence standard was found in the searched historical catalogue snapshots for this surviving CG395 ID.", "Family label and generic benchmark template are retained as hints only; they must not be expanded into a reconstructed definition.", "CG395 is run/archive evidence, not current product authority."],
            })
        rows.append(common)

    ledger = {
        "schema": "charitygraph.legacy-demand-recovery-ledger/v1",
        "schema_version": "1.0.0",
        "evidence_status_vocabulary": ["RECOVERED_EXACT", "RECOVERED_PARTIAL", "HINT_ONLY", "UNRECOVERABLE"],
        "recovery_rule": "Only copied explicit historical text/structured fields are present. No semantic reconstruction from IDs, families, adjacency, lexical similarity, or the current candidate catalogue is permitted.",
        "rows": rows,
    }
    output = OUT / "legacy-demand-recovery-ledger.v1.json"
    output.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ids = [row["legacy_id"] for row in rows]
    assert len(rows) == 74 and len(set(ids)) == 74
    assert set(row["evidence_status"] for row in rows) <= set(ledger["evidence_status_vocabulary"])
    assert all(row["historical_variants"] or row["explicit_semantic_hints"] for row in rows)
    assert all(row["confidence"] and row["limitations"] for row in rows)
    counts = Counter(row["evidence_status"] for row in rows)
    validation = {"schema": "charitygraph.legacy-demand-recovery-validation/v1", "ledger": str(output.relative_to(ROOT)).replace("\\", "/"), "ledger_sha256": sha256(output.read_bytes()), "row_count": len(rows), "unique_id_count": len(set(ids)), "status_counts": dict(sorted(counts.items())), "checks": {"all_74_unique": True, "known_statuses_only": True, "evidence_present_for_claimed_rows": True, "provenance_present_for_every_hint_or_variant": True, "semantic_authorship": "none; script copies explicit source fields and performs enumeration/hashing/validation only"}}
    (OUT / "validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
