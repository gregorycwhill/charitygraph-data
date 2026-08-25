# CharityGraph Taxonomy and Scheme Governance

**Status:** Canonical governance specification, version 1.0-draft

**Applies to:** External classifications, CharityGraph-native vocabularies, mappings and assignments

## 1. Policy

CharityGraph uses multiple schemes because no single hierarchy can faithfully represent legal purpose, beneficiaries, operational activity, participation, fundraising, finance, outcomes, ethos and public goals. External schemes are adopted where they provide authority or interoperability. Native vocabularies fill documented gaps.

Every scheme considered must have a visible research and disposition record. Sector insiders and researchers should be able to see whether a familiar scheme was adopted, adapted, mapped, deferred or rejected, and why.

## 2. Taxonomy plurality and optional external schemes

CharityGraph is taxonomy-plural. No single external scheme is the master taxonomy. ACNC/ATO classifications remain source/authority facts; SDGs provide an alignment lens; CharityGraph-native vocabularies describe operational activity and other gaps; external and custom schemes remain independently versioned, mapped and governed.

CLASSIE Subject and Population are optional integrations. Authoritative 4.2 Subject/Population materials are discoverable and exist, but private processing, LLM use, reuse, redistribution and publication rights remain unresolved. CLASSIE is not a prerequisite for identity, evidence, programs/services, activities, SDGs, regulatory facts or the underlying graph.

## 2. Scheme record

Each scheme or version records:

- canonical name, owner and version/date;
- purpose and intended users;
- concept model and hierarchy type;
- identifiers, labels, definitions and notes;
- licence, attribution and redistribution conditions;
- jurisdiction, language and cultural scope;
- maintenance and deprecation status;
- strengths, gaps and known biases;
- CharityGraph disposition and rationale;
- mappings to other schemes;
- assignment method and evaluation evidence;
- steward and review date.

## 3. Dispositions

Allowed dispositions are:

- `adopted`: used substantially as issued;
- `incorporated`: concepts reused within a broader profile with preserved attribution;
- `adapted`: modified under documented rules and rights;
- `mapped`: kept separate but crosswalked;
- `reference_only`: informative but not used for assignment;
- `deferred`: potentially useful, pending evidence, rights or implementation;
- `rejected`: unsuitable, with recorded reason;
- `retired`: previously used but no longer active.

## 4. Approved initial portfolio

| Domain | Scheme/profile | Initial disposition | Role |
|---|---|---|---|
| Regulatory purpose/beneficiaries/activities | ACNC/ATO classifications | Adopted as source classifications | Preserve what regulators report; do not mistake for the complete semantic model |
| Charity subject and population | CLASSIE Subject and Population | Deferred / optional pending rights review | Desirable Australian interoperability lens; not foundational and not the master taxonomy |
| Finance | National Standard Chart of Accounts | Adopted/mapped | Normalised not-for-profit financial concepts while retaining reported line items |
| Public goals | UN Sustainable Development Goals | Adopted as multi-label alignment | Widely recognised goal lens; assignments may apply to organisations or programs |
| Geography and statistical population | ABS standards | Adopted where applicable | Locations, regions and demographic/statistical compatibility |
| Operational activity | CharityGraph native | Developed with mappings | Concrete work performed, distinct from purpose and beneficiary |
| Participation | CharityGraph native | Developed with external research | Volunteering, giving, membership, advocacy and other ways people participate |
| Fundraising | CharityGraph native | Developed with external research | Method, channel, setting, instrument, audience, campaign and observation detail |
| Ethos/conduct | CharityGraph native | Developed cautiously | Values, stance and conduct assertions with evidence and consequence-aware review |
| Notability | CharityGraph processing profile | Native, non-normative | Resource allocation and retrieval prioritisation, never charity worth or quality |
| Outcomes/evaluation | CharityGraph evidence profile | Developed with external mappings | Evaluation method, outcome claim and evidence-strength description without universal scoring |

## 5. Assignment model

Assignments are first-class assertions, not columns pasted onto an organisation. An assignment records:

- subject and scope (organisation, program, site, campaign or activity);
- scheme and concept version;
- primary/secondary or other role;
- method (source-reported, deterministic, model-assessed, human-reviewed, community-proposed);
- evidence and rationale;
- confidence/strength where appropriate;
- valid time, review status and lineage.

Multi-label assignment is normal. A program may align with several SDGs or concepts from any permitted external or native scheme. A primary label supports discovery; secondary labels preserve material breadth. Scheme removal must not invalidate independent governed knowledge.

## 6. Mapping model

A concept mapping is different from an instance assignment. Mappings use explicit predicates such as:

- `exact_match`;
- `close_match`;
- `broader_match`;
- `narrower_match`;
- `related_match`;
- `no_match`.

Exact correspondence must not be inferred merely because labels look similar. Mapping evidence, method, version and review status are retained.

## 7. UN SDG policy

SDG alignment is approved for vNext from the first reality slice. It is:

- multi-label;
- preferably program-scoped when program evidence exists;
- organisation-scoped when only whole-of-organisation evidence is available;
- an alignment judgment, not proof of impact or UN endorsement;
- supported by evidence and rationale;
- allowed to be decisive under ordinary ambiguity.

Targets and indicators may be added later where evidence supports that granularity. Initial work should not pretend that an activity demonstrates an official indicator result.

## 8. Finance policy

The Chart of Accounts normalises financial concepts but does not erase the source presentation. Store:

- reported label, value, period and statement context;
- normalised account/concept;
- calculation and consolidation scope;
- mapping method and confidence;
- source and evidence;
- restatement or correction lineage.

## 9. Participation and fundraising design

These domains use faceted vocabularies rather than one brittle hierarchy. A record may separately identify:

- role or mode of participation;
- fundraising method;
- channel/medium;
- physical or digital setting;
- instrument or thing transferred;
- audience/targeting;
- solicitation and fulfilment mechanism;
- campaign and temporal scope;
- direct observation versus organisational reporting.

This permits distinctions such as residential door-knocking versus a staffed shopping-centre table, and shop-counter goods donation versus an unattended charity bin, without multiplying opaque compound labels.

## 10. Private payloads, publication rights and scheme retirement

Open-source CharityGraph code may contain generic taxonomy schemas, version metadata, import/assignment machinery, mapping predicates and publication-policy controls. Restricted third-party payloads do not need to live in the open repository. Official artefacts remain provenance roots; private runtime storage may hold content-hashed source files, normalised concepts, protected prompts and model outputs where rights and policy allow.

Taxonomy payload, internal processing material and CharityGraph-derived assignments are separately governed. Public CLASSIE representation may independently be configured as no assignment, external concept ID only, ID plus label or richer metadata, subject to permission. No current form is approved by this document.

`CLASSIE disabled` is a supported state: stop new CLASSIE tasks, withhold/remove CLASSIE assignments from publishable projections, and invalidate/regenerate only CLASSIE-dependent derived objects. Do not reacquire evidence or rebuild identity, programs, relationships, native activities, SDGs or independent schemes. Historical internal lineage may remain where lawful; publication eligibility remains rights-controlled.

## 11. Future custom and researcher schemes

Researchers, academic projects, innovators, government, foundations, sector bodies and other legitimate scheme owners may propose conforming taxonomies. Each scheme independently records owner, version, source, purpose, scope, identifiers, hierarchy/facets, rights, attribution, disposition, assignment method, mappings and review state. Custom assignments remain named scheme assignments and do not silently become CharityGraph-native facts.

## 12. Research register requirements

Taxonomy research must cover, where relevant:

- Australian regulators and statistical standards;
- Australian charity, philanthropy and fundraising research;
- industry and professional bodies;
- international nonprofit classifications;
- grantmaking and impact-taxonomy initiatives;
- academic schemes and data dictionaries;
- advertising, media and participation classifications;
- Indigenous data and cultural-governance frameworks.

For every considered scheme, cite primary material where available and record the disposition. Lack of immediate adoption is not permission to omit the research trail.

## 11. Versioning and deprecation

Concept identifiers are stable within a version. Labels may be multilingual or revised without changing identity when meaning is unchanged. Material meaning changes create a new concept/version and explicit mapping. Deprecated concepts remain resolvable and are not silently reassigned in historical releases.

## 12. Governance workflow

1. Register the candidate scheme and source material.
2. Assess purpose, rights, granularity, coverage, maintenance and fit.
3. Test against representative Australian charity and program cases.
4. Record disposition and rationale.
5. Define mappings and assignment policy.
6. Validate with a fixed evaluation set and, where warranted, domain experts.
7. Publish scheme/version metadata and limitations.
8. Monitor corrections, drift and sector feedback.

## 13. Community proposals

Community members may propose concepts, definitions, mappings and assignments. Proposals are versioned observations and do not directly edit canonical vocabularies. Accepted proposals retain contributor attribution where permitted and exact decision lineage.

## 14. Prohibitions

CharityGraph must not:

- imply endorsement by a scheme owner;
- turn notability into a worth score;
- collapse purpose, beneficiary, activity and outcome into one label;
- interpret missing classification as negative evidence;
- force exact mappings where only related concepts exist;
- hide the origin of adapted concepts;
- publish culturally sensitive classifications without appropriate governance.

This document governs vNext only and does not modify contract 0.5.
