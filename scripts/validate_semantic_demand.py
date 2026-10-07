"""Deterministic supplementary validation for the committed v0.2 corpus.

JSON Schema conformance is deliberately a separate gate: this script never
claims to substitute for a Draft 2020-12 implementation.
"""
import json
from pathlib import Path
ROOT=Path(__file__).parents[1]/"docs"/"semantic-demand-catalogue-v0.2"
records=json.loads((ROOT/"scenarios.json").read_text(encoding="utf-8"))
questions=[r for r in records if r["scenario_type"]=="question"]
corrections=[r for r in records if r["scenario_type"]=="correction_challenge"]
errors=[]
required={"id","scenario_type","persona","analytical_lenses","job_to_be_done","surface_question","semantic_contract","primary_domains","supporting_domains","answerability","adversarial","semantic_signature","distinctiveness_rationale"}
for r in records:
 if required-r.keys(): errors.append(f"{r.get('id')}: missing required fields")
 if not r["analytical_lenses"] or not r["primary_domains"]: errors.append(f"{r['id']}: empty lens or primary domain")
 if r["scenario_type"]=="correction_challenge" and "correction" not in r: errors.append(f"{r['id']}: missing correction")
if len(questions)<60 or len(corrections)<12: errors.append("minimum corpus size")
if len({r['id'] for r in records})!=len(records): errors.append("duplicate ids")
if set(range(1,21))-{d for r in questions for d in r['primary_domains']+r['supporting_domains']}: errors.append("domain coverage")
if not {"public_donor_participant","charity_insider_adviser"} <= {r["persona"] for r in records}: errors.append("public and charity-insider demand")
if len({r["semantic_signature"] for r in records}) != len(records): errors.append("duplicate semantic signatures")
if errors:
 for e in errors: print(getattr(e,"message",e))
 raise SystemExit(1)
print(f"deterministic semantic validation passed: {len(records)} (questions={len(questions)}, correction_challenge={len(corrections)})")
