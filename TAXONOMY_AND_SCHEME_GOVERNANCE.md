# CharityGraph Taxonomy and Scheme Governance

**Status:** Canonical governance specification, version 1.0-draft

**Applies to:** External classifications, CharityGraph-native vocabularies, mappings and assignments

## 1. Policy

CharityGraph uses multiple schemes because no single hierarchy can faithfully represent legal purpose, beneficiaries, operational activity, participation, fundraising, finance, outcomes, ethos and public goals. External schemes are adopted where they provide authority or interoperability. Native vocabularies fill documented gaps.

Every scheme considered must have a visible research and disposition record. Sector insiders and researchers should be able to see whether a familiar scheme was adopted, adapted, mapped, deferred or rejected, and why.

## 2. Taxonomy plurality and optional external schemes

CharityGraph is taxonomy-plural. No single external scheme is the master taxonomy. ACNC/ATO classifications remain source/authority facts; SDGs provide an alignment lens; CharityGraph-native vocabularies describe operational activity and other gaps; external and custom schemes remain independently versioned, mapped and governed.

CLASSIE has two distinct roles: ACNC CLASSIE is AIS-year/profile-specific source reporting; CharityGraph CLASSIE is an independent, evidence-bound model assessment against a selected Our Community release. Private processing and configured-model use are approved. Redistribution and publication remain permission-gated; CLASSIE payloads and inferred assignments are withheld by default. CLASSIE is removable and not foundational to identity, evidence, programs/services, activities, SDGs, regulatory facts or the underlying graph.

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
| Classification / regulatory lenses | ACNC Registration; ATO DGR; ACNC CLASSIE (AIS profile); UN SDG; CharityGraph Native; CharityGraph CLASSIE (Our Community profile) | Independently governed, versioned and publication-controlled | Distinct grains and authorities; private CLASSIE processing approved, public CLASSIE output permission-gated |
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

## Classification / regulatory lenses (current decision)

CharityGraph uses six named lenses; they are not six equivalent taxonomies.

| Lens | Natural grain | Authority / owner | Meaning | Assignment method | Publication treatment |
|---|---|---|---|---|---|
| ACNC Registration | Legal charity/entity | ACNC | Registration, charitable purpose/subtype, beneficiary classifications and other regulatory facts kept as separate dimensions | Source-reported | Public where the governing source and release policy permit |
| ATO DGR | Legal entity or scoped fund/authority/institution | ATO / Commonwealth tax law | DGR entitlement/status, scoped endorsement and statutory item/category where applicable | Source-reported; versioned profile where enumerated | Public subject to source/provenance policy |
| ACNC CLASSIE | AIS program | ACNC, AIS-year/profile-specific | Program classification selected/reported in AIS | Source-reported | Public only under applicable rights/source policy |
| UN SDG | Program/service primarily; organisation only when genuinely organisation-wide | UN goal framework, CharityGraph governance | Alignment, not impact or UN endorsement | Model-assessed, evidence-bound and governed | Public projection is derived and policy-controlled |
| CharityGraph Native | Organisation, group, legal entity, program/service and supported scopes | CharityGraph governance | Operational knowledge, activities, populations, geography, relationships and selected native vocabularies | Source-reported or model-assisted as recorded | Eligible according to evidence and release policy |
| CharityGraph CLASSIE | Program/service primarily | CharityGraph, using selected Our Community release/profile | Independent CharityGraph assessment against CLASSIE concepts | Model-assessed, evidence-bound and human-reviewable | Private/publication-withheld by default until permission |

ACNC Registration is a regulatory family, not one taxonomy. ATO DGR is separate from ACNC Registration and must never be inferred from ACNC purpose. ACNC CLASSIE must use an explicit AIS/profile version and must not be treated as version-identical to the selected Our Community CLASSIE release. Explicit ConceptMapping records are required for any crosswalk; label equality is not an exact mapping.

Reporting groups are scope structure, not a seventh lens. An AIS or annual report may cover multiple legal charities and programs, but facts attach to the lowest evidence-supported subject/scope and do not propagate automatically.

Embeddings remain versioned retrieval/similarity aids. They may propose candidates or mappings, but cannot create a governed taxonomy assignment or justify new native concepts alone.

Private CLASSIE processing is approved. Public release remains permission-gated. If permission is denied, stop new CLASSIE tasks and withhold/remove CLASSIE-derived projections while retaining native knowledge, ACNC/ATO facts, SDGs, programs/services and evidence.