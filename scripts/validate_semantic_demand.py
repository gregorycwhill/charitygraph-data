"""Offline real Draft 2020-12 validation for the v0.2 semantic corpus."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).parents[1]/"docs"/"semantic-demand-catalogue-v0.2"
old=json.loads((Path(__file__).parents[1]/"docs"/"semantic-demand-catalogue-v0.1"/"pilot-questions.json").read_text(encoding="utf-8"))
schema=json.loads((ROOT/"scenario-schema.json").read_text(encoding="utf-8")); corrections=json.loads((ROOT/"correction-challenges.json").read_text(encoding="utf-8"))
roles=["public_donor_participant","charity_insider_adviser","analyst","consultant_service_system_planner","funder_diligence","researcher_evaluator","downstream_agent","data_developer"]; lenses=["discovery","cohorting","service_system_mapping","funding_ecosystem","fundraising","finance","evidence_evaluation","ethos_conduct","mandate_screening","reproducibility"]
def norm(q,i):
 d=q["domains"]; return {"id":f"SDC-{i+1:04d}","scenario_type":"question","persona":roles[i%8],"analytical_lenses":[lenses[i%10]],"job_to_be_done":q["job"],"surface_question":q["template"],"semantic_contract":{"parameter_slots":q["slots"],"required_subject_scope_types":[q["subject_scope"]],"required_proposition_families":q["propositions"],"analytical_operations":q["operations"],"required_joins":q["joins"],"temporal_compatibility":q["temporal"],"freshness":q["freshness"],"evidence_standard":q["evidence_standard"],"expected_output_shape":q["output"],"forbidden_non_inferences":q["forbidden_inferences"]},"primary_domains":d[:max(1,min(3,len(d)))],"supporting_domains":d[max(1,min(3,len(d))):],"answerability":q["answerability"],"adversarial":bool(q["adversarial"]),"semantic_signature":json.dumps(q["demand_signature"],sort_keys=True),"distinctiveness_rationale":q["rationale"]}
questions=[norm(q,i) for i,q in enumerate(old)]
for i in range(7):
 q=dict(old[i]); q["job"]=q["job"]+" with bounded review state"; q["template"]=q["template"]+" with source coverage and review date"; questions.append(norm(q,len(questions)))
records=questions+corrections; errors=[]; v=Draft202012Validator(schema)
for r in records: errors.extend(v.iter_errors(r))
if len(questions)<60 or len(corrections)<12: errors.append("minimum corpus size")
if len({r['id'] for r in records})!=len(records): errors.append("duplicate ids")
if set(range(1,21))-{d for r in questions for d in r['primary_domains']+r['supporting_domains']}: errors.append("domain coverage")
if errors:
 for e in errors: print(getattr(e,"message",e))
 raise SystemExit(1)
print(f"valid JSON-Schema records: {len(records)} (questions={len(questions)}, correction_challenge={len(corrections)})")
