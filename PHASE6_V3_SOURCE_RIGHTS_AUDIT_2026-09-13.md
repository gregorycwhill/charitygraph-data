# Phase 6 V3 frozen-source rights audit

**Status:** Historical compliance audit; not execution authority
**Date:** 13 September 2026
**Scope:** the 27 frozen source artefacts used by the unsent V3 campaign
**Provider calls / acquisitions / promotions:** 0 / 0 / 0

## Result

No artefact is approved for private provider transmission. The count is **0 explicitly authorized, 27 unknown/blocked, 0 prohibited, 0 statutory-exception decisions, and 0 evidence-unrecoverable**. The audit recovered every frozen identity and its linked receipts, but no receipt retained a terms, licence, permission, or rights-policy record. The result is intentionally fail-closed.

The nine ACNC API artefacts are regulator material and have a plausible future open-data route: the [ACNC Registered Charities dataset](https://data.gov.au/data/dataset/b050b242-4487-4306-abf5-07ca073e5594) is CC BY 3.0 AU and ACNC's [data-use policy](https://www.acnc.gov.au/about/corporate-information/corporate-policies/corporate-policy-use-acnc-data) encourages reuse. But the frozen API representations do not retain an exact dataset-resource/version binding. They therefore remain `unknown`, rather than inheriting a bulk-data licence. The charity PDFs were supplied by third parties through ACNC storage and the site representations are copied publisher material; neither is made provider-transmittable by public access. No retained publisher terms gave affirmative third-party processing permission.

OpenAI processing is separately governed by `openai-api-input-v1`: the [Services Agreement](https://cdn.openai.com/osa/openai-services-agreement.pdf) places responsibility for Input rights, licences and permissions on the customer. API/business no-training treatment is relevant to confidentiality only.

## Matrix

Each row is an artefact-specific decision candidate. `R` is the exact transmitted representation SHA-256; `A` is the frozen source artefact ID. Origin is the retained source locator family (the full locator remains private with the frozen corpus). All rows: local retention **not newly approved**; provider **no**; public redistribution **no**; attribution **not determined**; confidence **blocked pending retained affirmative evidence**.

| Slice | Subject | Family | A | R | Origin | Basis / blocker |
|---|---|---|---|---|---|---|
| outcomes | The Smith Family | ACNC | `srcblob:042ea524…f58b` | `3217e513…1852` | ACNC API entity | unknown; exact CC resource not bound |
| outcomes | The Smith Family | annual report | `srcblob:1615b7da…e983` | `761328a2…ebf75` | ACNC public-file PDF | unknown; third-party report |
| outcomes | The Smith Family | website | `srcblob:baa05bb1…5d9` | `a7e78ce1…0d65` | thesmithfamily.com.au | unknown; no affirmative provider permission |
| outcomes | World Vision Australia | ACNC | `srcblob:ca734a66…c14` | `fb45eaba…a4ad` | ACNC API entity | unknown; exact CC resource not bound |
| outcomes | World Vision Australia | annual report | `srcblob:d14c0737…7db` | `22131c75…885c` | ACNC public-file PDF | unknown; third-party report |
| outcomes | World Vision Australia | website | `srcblob:e98d5ba6…1903` | `9e948b8f…1e94` | worldvision.com.au | unknown; no affirmative provider permission |
| outcomes | Bush Heritage Australia | ACNC | `srcblob:8bab3696…574` | `9b9e2b52…6456` | ACNC API entity | unknown; exact CC resource not bound |
| outcomes | Bush Heritage Australia | annual report | `srcblob:114fbe39…012` | `4d8c4476…0055` | ACNC public-file PDF | unknown; third-party report |
| outcomes | Bush Heritage Australia | website | `srcblob:15f60c66…5a5` | `37a2a6b5…8223` | bushheritage.org.au | unknown; no affirmative provider permission |
| commitments | Australian Red Cross | ACNC | `srcblob:fe2d1d88…5c2` | `c0a2fe71…1a95` | ACNC API entity | unknown; exact CC resource not bound |
| commitments | Australian Red Cross | annual report | `srcblob:f8f0b72d…7ca` | `a7a8fed7…d342` | ACNC public-file PDF | unknown; third-party report |
| commitments | Australian Red Cross | website | `srcblob:abf828c9…5bc` | `e9816c14…7153` | redcross.org.au | unknown; no affirmative provider permission |
| commitments | Greenpeace Australia Pacific | ACNC | `srcblob:79b5fe39…7e5` | `912542f3…1ff7` | ACNC API entity | unknown; exact CC resource not bound |
| commitments | Greenpeace Australia Pacific | annual report | `srcblob:af7655f4…fa0` | `2b2b42e9…8168` | ACNC public-file PDF | unknown; third-party report |
| commitments | Greenpeace Australia Pacific | website | `srcblob:02d206f4…547` | `33890bbf…1840` | greenpeace.org.au | unknown; no affirmative provider permission |
| commitments | The Sunrise Project | ACNC | `srcblob:0d79334b…881` | `ead3fcf6…fa46` | ACNC API entity | unknown; exact CC resource not bound |
| commitments | The Sunrise Project | annual report | `srcblob:707f1445…b11` | `2c562da1…0a6` | ACNC public-file PDF | unknown; third-party report |
| commitments | The Sunrise Project | website | `srcblob:82e89aa6…1a75` | `f35df0c4…121a` | sunriseproject.org.au | unknown; no affirmative provider permission |
| capacity | St George Community Housing | ACNC | `srcblob:e425e381…356` | `e657768b…31f` | ACNC API entity | unknown; exact CC resource not bound |
| capacity | St George Community Housing | annual report | `srcblob:439a7249…023` | `2250b60d…7aa` | ACNC public-file PDF | unknown; third-party report |
| capacity | St George Community Housing | website | `srcblob:8e25a63f…795` | `3d672462…b64` | sgch.com.au | unknown; no affirmative provider permission |
| capacity | Leukaemia Foundation | ACNC | `srcblob:6f543329…2cf` | `f36e257a…371` | ACNC API entity | unknown; exact CC resource not bound |
| capacity | Leukaemia Foundation | annual report | `srcblob:5e517030…def` | `dbf5c83b…5ca` | ACNC public-file PDF | unknown; third-party report |
| capacity | Leukaemia Foundation | website | `srcblob:f91f1e88…ba6` | `d5b82d4c…472` | leukaemia.org.au | unknown; no affirmative provider permission |
| capacity | RFDS Queensland | ACNC | `srcblob:134504be…d08` | `854e5df4…3d7` | ACNC API entity | unknown; exact CC resource not bound |
| capacity | RFDS Queensland | annual report | `srcblob:c58e7f24…dcc` | `3e877c04…8bc0` | ACNC public-file PDF | unknown; third-party report |
| capacity | RFDS Queensland | website | `srcblob:70008278…a47` | `b8565ace…185` | flyingdoctor.org.au/qld | unknown; no affirmative provider permission |

## V3 offline preflight and minimum remedy

All 12 attempts are blocked because each uses three frozen sources and at least one (in practice all) has no affirmative artifact-level decision. Existing request bodies, manifests and schema/request certification were not changed. The minimum unresolved set is the 27 rows above: for every row, retain evidence and record a decision under a versioned policy; for ACNC, additionally bind the exact frozen content to a named licensed resource/version. Annual reports and websites require explicit permission, a valid open licence, or exclusion/substitution in a separately authorized future change. No statutory exception is self-authorized.
