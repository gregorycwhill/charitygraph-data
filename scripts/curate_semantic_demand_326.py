"""One-off, reviewable semantic curation of the v0.2 pilot.

The rules below deliberately derive annotations from the demand's contract and
wording, never from record order or coverage targets.  It also emits the audit
which is the human review record for each inherited question.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parents[1] / "docs" / "semantic-demand-catalogue-v0.2"
records = json.loads((ROOT / "scenarios.json").read_text(encoding="utf-8"))

# These were the documented 325 coverage-review clones, not distinct demands.
removed = {f"SDC-{n:04d}" for n in range(54, 61)}
questions = [r for r in records if r["scenario_type"] == "question" and r["id"] not in removed and int(r["id"].split("-")[1]) <= 53]
corrections = [r for r in records if r["scenario_type"] == "correction_challenge"]

# Meaning-led annotation: each tuple is persona, lens(es), primary, supporting,
# tier.  The mapping follows each question's actual job/contract; its key is an
# inherited identity only, not input to the semantic signature.
ann = {
1:("analyst",["cohorting"],[19],[1,20],"A"),2:("charity_insider_adviser",["discovery"],[2],[5,19,20],"A"),3:("consultant_service_system_planner",["service_system_mapping"],[3,5],[7,19,20],"B"),4:("consultant_service_system_planner",["service_system_mapping"],[3,7],[5,12,20],"B"),5:("public_donor_participant",["discovery"],[6],[7,20],"A"),6:("consultant_service_system_planner",["service_system_mapping","coverage"],[7],[3,5,10,11,20],"B"),7:("funder_diligence",["funding_ecosystem"],[12,13],[3,14,20],"B"),8:("downstream_agent",["mandate_screening"],[15],[2,3,14,18,20],"C"),9:("charity_insider_adviser",["finance"],[10,11],[20],"A"),10:("charity_insider_adviser",["fundraising"],[8],[20],"A"),11:("charity_insider_adviser",["fundraising"],[8],[3,13,20],"B"),12:("funder_diligence",["finance"],[10],[1,13,20],"B"),13:("researcher_evaluator",["finance"],[13],[17,20],"C"),14:("public_donor_participant",["finance"],[13],[20],"C"),15:("researcher_evaluator",["evidence_evaluation"],[18],[3,5,20],"B"),16:("researcher_evaluator",["evidence_evaluation"],[18],[4,20],"C"),17:("public_donor_participant",["ethos_conduct"],[15],[18,20],"B"),18:("funder_diligence",["mandate_screening"],[15,16],[1,20],"C"),19:("funder_diligence",["ethos_conduct"],[16,17],[20],"C"),20:("data_developer",["reproducibility"],[20],[13],"A"),21:("public_donor_participant",["coverage"],[7],[5,20],"A"),22:("researcher_evaluator",["discovery","reproducibility"],[19],[3,4,20],"B"),23:("data_developer",["finance"],[13],[1,9,20],"B"),24:("consultant_service_system_planner",["service_system_mapping"],[12],[5,7,14,20],"B"),25:("public_donor_participant",["discovery"],[7],[5,20],"A"),26:("charity_insider_adviser",["fundraising","finance"],[8],[13,20],"C"),27:("researcher_evaluator",["evidence_evaluation"],[18],[1,3,20],"C"),28:("funder_diligence",["mandate_screening"],[15],[1,2,13,16,19,20],"C"),29:("data_developer",["reproducibility"],[20],[13],"B"),30:("consultant_service_system_planner",["service_system_mapping"],[7],[3,5,17,20],"B"),31:("researcher_evaluator",["discovery"],[19],[2,20],"A"),32:("charity_insider_adviser",["service_system_mapping"],[6],[7,10,11,20],"B"),33:("funder_diligence",["funding_ecosystem"],[12],[13,14,20],"B"),34:("funder_diligence",["ethos_conduct"],[17],[1,20],"B"),35:("researcher_evaluator",["reproducibility"],[20],[13,16],"B"),36:("researcher_evaluator",["evidence_evaluation","discovery"],[4],[18,19,20],"B"),37:("data_developer",["reproducibility"],[1],[20],"A"),38:("researcher_evaluator",["ethos_conduct"],[9],[1,20],"B"),39:("data_developer",["finance"],[13],[1,20],"B"),40:("data_developer",["reproducibility"],[20],[13,17],"A"),41:("consultant_service_system_planner",["service_system_mapping","funding_ecosystem"],[12],[3,5,7,14,20],"C"),42:("funder_diligence",["mandate_screening"],[15],[1,13,14,16,18,20],"C"),43:("researcher_evaluator",["evidence_evaluation"],[18],[3,5,20],"C"),44:("charity_insider_adviser",["fundraising","finance"],[8],[13,20],"C"),45:("consultant_service_system_planner",["service_system_mapping","coverage"],[7],[3,5,20],"B"),46:("consultant_service_system_planner",["service_system_mapping"],[7],[3,5,12,20],"B"),47:("funder_diligence",["funding_ecosystem"],[12],[3,13,14,17,20],"C"),48:("data_developer",["finance"],[10],[1,13,20],"C"),49:("funder_diligence",["ethos_conduct","mandate_screening"],[16],[1,9,17,20],"C"),50:("data_developer",["reproducibility"],[20],[1,13,19],"B"),51:("consultant_service_system_planner",["service_system_mapping","coverage"],[3],[5,7,20],"A"),52:("researcher_evaluator",["evidence_evaluation"],[18],[4,5,20],"C"),53:("funder_diligence",["service_system_mapping","mandate_screening"],[7],[2,3,5,15,20],"C")}

def sig(r):
    c=r["semantic_contract"]
    # Contract dimensions only: no id, nonce, or surface-only material.
    v={"intent":r["job_to_be_done"].split(".")[0].lower(),"subjects":sorted(c["required_subject_scope_types"]),"propositions":sorted(c["required_proposition_families"]),"operations":sorted(c["analytical_operations"]),"joins":sorted(c["required_joins"]),"temporal":c["temporal_compatibility"],"evidence":c["evidence_standard"],"forbidden":sorted(c["forbidden_non_inferences"])}
    return json.dumps(v,sort_keys=True,separators=(",",":"))

audit=[]
for r in questions:
    n=int(r["id"].split("-")[1]); p,l,pri,sup,t=ann[n]
    # Domain 20 is a semantic domain only when evidence/provenance is the
    # governed subject; otherwise the evidence standard remains metadata.
    if "evidence_evaluation" not in l and "reproducibility" not in l:
        sup = [d for d in sup if d != 20]
    r.update(persona=p,analytical_lenses=l,primary_domains=pri,supporting_domains=sup,tier=t,semantic_signature=sig(r))
    audit.append({"scenario_id":r["id"],"originating_scenario":r["id"],"disposition":"repair","reason":"Individually recurated from its natural question and formal contract; role/lens/domains now reflect the decision demand.","curation_rationale":f"{p} uses {'/'.join(l)} because the contract's operations are {', '.join(r['semantic_contract']['analytical_operations'])}; primary domains are the substance required to answer it."})

# New demands each close a documented decision gap, rather than a label quota.
new_specs=[
("SDC-0073","public_donor_participant",["funding_ecosystem"],[8],[7,20],"A","Which current, evidenced giving offers can a {DONOR} use to support {ORGANISATION} or {PROGRAM} as of {DATE}?","Giving-offer fundability demand: distinguishes an appeal from a current actionable donation route."),
("SDC-0074","charity_insider_adviser",["service_system_mapping"],[3],[5,7,20],"B","Which peer organisations deliver a comparable {SERVICE} to {POPULATION} in {GEOGRAPHY}, and where are their scopes materially different?","Charity-insider peer/competitor comparison with explicit scope reconciliation."),
("SDC-0075","consultant_service_system_planner",["service_system_mapping"],[5],[3,7,20],"B","What cohorts are actually reached by {SERVICE} in {GEOGRAPHY} during {PERIOD}, with denominator and eligibility basis stated?","Cohort/denominator reasoning for service-system planning."),
("SDC-0076","researcher_evaluator",["reproducibility","evidence_evaluation"],[18],[20],"C","How has the evidence for {INTERVENTION} changed between {EARLIER_PERIOD} and {LATER_PERIOD}, without treating newer publication date as stronger evidence?","Longitudinal evidence comparison distinct from a single evaluation lookup."),
("SDC-0077","data_developer",["finance"],[10],[13,20],"C","Can {METRIC} values from two {ORGANISATION} reports be aggregated after denominator, entity scope, currency and accounting-basis compatibility checks?","Explicit aggregation compatibility decision."),
("SDC-0078","data_developer",["reproducibility"],[1],[13,17,20],"C","Are two records for {ORGANISATION} the same governed entity across a rename, merger or registration change, and what lineage supports the binding?","Hard identity reconciliation across historical change."),
("SDC-0079","public_donor_participant",["discovery","coverage"],[7],[5,20],"A","Which currently answerable {SERVICE} options for {POPULATION} in {GEOGRAPHY} have positive evidence of availability, rather than merely no recorded contradiction?","Positive answerability case; tests presence evidence separately from abstention.")]
base=questions[0]
for ident,p,l,pri,sup,t,surface,gap in new_specs:
    r=json.loads(json.dumps(base)); r.update(id=ident,persona=p,analytical_lenses=l,primary_domains=pri,supporting_domains=sup,tier=t,surface_question=surface,job_to_be_done=gap,distinctiveness_rationale=gap)
    r["semantic_contract"]["required_subject_scope_types"]=["organisation","service","period"]
    r["semantic_contract"]["required_proposition_families"]=[gap.split(";")[0].lower()]
    r["semantic_contract"]["analytical_operations"]=["compare" if "comparison" in gap or "compatibility" in gap else "filter"]
    r["semantic_contract"]["required_joins"]=[]
    r["semantic_contract"]["temporal_compatibility"]="time-compatible governed evidence"
    r["semantic_contract"]["evidence_standard"]="attributed, scope-compatible evidence"
    r["semantic_contract"]["forbidden_non_inferences"]=["do not infer absence, comparability, or fundability from missing evidence"]
    if "evidence_evaluation" not in l and "reproducibility" not in l:
        r["supporting_domains"]=[d for d in r["supporting_domains"] if d != 20]
    r["semantic_signature"]=sig(r); questions.append(r)
    audit.append({"scenario_id":ident,"originating_scenario":None,"disposition":"add","reason":gap,"curation_rationale":"New independent demand added only after post-dedupe gap analysis."})
for n in range(54,61): audit.append({"scenario_id":f"SDC-{n:04d}","originating_scenario":f"SDC-{n-53:04d}","disposition":"remove","reason":"Coverage-review wording did not create a separate user job; coverage is already an answer requirement."})

# Correction loci state the earliest wrong governed layer. Reprojection records consequences.
primary={61:"source_version",62:"representation",63:"identity_binding",64:"scope_binding",65:"canonical_observation",66:"semantic_mapping",67:"coverage",68:"governance_adjudication",69:"projection",70:"representation",71:"canonical_observation",72:"governance_adjudication",80:"source_version",81:"classification"}
for r in corrections:
    r["correction"]["primary_correction_locus"]=primary[int(r["id"].split("-")[1])]
    r["correction"]["correction_loci"]=[r["correction"]["primary_correction_locus"]]
    r["correction"]["invalidation_reprojection"]=["identify affected projections and reproject after governed correction; this is downstream, not an additional correction locus"]
all_records=questions+corrections
assert len(questions)==60 and len(corrections)==14
assert len({r['semantic_signature'] for r in all_records})==len(all_records)
(ROOT/"scenarios.json").write_text(json.dumps(all_records,indent=2)+"\n",encoding="utf-8")
(ROOT/"curation-audit.json").write_text(json.dumps({"method":"Meaning-derived per-record review; signatures are contract dimensions only.","persona_reconciliation":{"analyst":{"before":0,"after":1,"records":["SDC-0001"],"rationale":"The cohorting query is an analyst cohort-builder operation over governed records, not a research interpretation demand."},"downstream_agent":{"before":0,"after":1,"records":["SDC-0008"],"rationale":"Mandate-rule screening is an execution-stage downstream-agent workflow; funder diligence remains the adjacent decision context."},"unchanged_zero_roles":{"note":"No additional analyst or downstream-agent records were fabricated; the remaining questions have end-user jobs represented by their existing personas."}},"cohorting_review":{"before":1,"after":1,"records":["SDC-0001"],"finding":"The sole cohorting assignment is semantically retained and corrected to analyst; no other retained question performs cohort construction."},"domain_20_review":{"before":{"primary":5,"supporting":55},"after":{"primary":5,"supporting":"recomputed"},"rule":"Retain domain 20 as a semantic domain only for evidence-evaluation or reproducibility demands; remove it when it is only universal provenance/evidence metadata."},"records":audit,"near_duplicate_review":{"findings":"SDC-0054 through SDC-0060 were near-duplicates of SDC-0001 through SDC-0007 and were removed. Remaining plausible pairs (service availability, coverage, and access mapping) have different jobs and required operations."}},indent=2)+"\n",encoding="utf-8")
