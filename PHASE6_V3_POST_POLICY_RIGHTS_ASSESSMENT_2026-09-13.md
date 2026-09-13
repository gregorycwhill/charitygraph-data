# Phase 6 V3 post-policy source-rights assessment - 13 September 2026

**Status:** Completed offline rights reassessment; V3 remains unexecuted and is not cleared for execution.

## Authority and scope

On 13 September 2026 the CharityGraph product owner approved `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1` version `1.0.0` for bounded private analytical processing of lawfully accessible public-facing material. This is CharityGraph product policy, not external legal advice or a claim of legal certainty. This assessment evaluates only the exact frozen representations V3 would transmit. It neither changes those representations nor authorizes provider execution.

The preceding [pre-policy source-rights audit](PHASE6_V3_SOURCE_RIGHTS_AUDIT_2026-09-13.md) remains the historical record: before policy approval, all 27 were unknown/blocked. The separate [pre-send blocker record](PHASE6_CORRECTED_CONFIRMATION_V3_EXECUTION_BLOCKER_2026-09-13.md) records that V3 had not crossed the provider boundary. No V3 request body, manifest, or certification was modified by this reassessment.

## Decision summary

- Exact frozen artifacts assessed: **27** across nine subjects; linked existing acquisition receipts: **30**. Every artifact has a recorded available HTTP 200 receipt and source lineage. This is a read-only review of retained records, not a new acquisition.
- Explicit open-license authorizations: **0**. No exact licensed-resource/version lineage was established for these API or report representations; no ACNC bulk-data licence was inferred.
- Fair Dealing V1 authorizations: **18** (nine one-record ACNC JSON representations and nine report excerpts).
- Blocked under Fair Dealing V1: **8** (seven complete/near-complete homepage representations and one unclear 43-character representation).
- Prohibited: **1** (The Smith Family homepage: explicit website terms prohibition).
- Public redistribution allowed: **0**; local retention allowed by this policy: **0**. Derived publication and evidence quotations remain governed separately.

The nine annual-report representations contain the following exact selected page numbers from the identified source PDFs: Smith Family 1, 2, 4, 5 of 52 (7.7%); World Vision 1-5 of 51 (9.8%); St George Community Housing 1-5 of 39 (12.8%); Australian Red Cross 1-4 of 122 (3.3%); Leukaemia Foundation 1, 2, 3, 5 of 29 (13.8%); Greenpeace 1-5 of 33 (15.2%); Sunrise Project 1-5 of 26 (19.2%); Bush Heritage 1-5 of 64 (7.8%); RFDS Queensland 1, 3, 4 of 34 (8.8%). Each exact representation therefore satisfies the assessment's conservative limit of at most five selected pages and at most 20% of the identified PDF.

## Exact artifact decisions

All origins below are the source locators frozen in the Condition A export. `Representation SHA-256` hashes the exact UTF-8 string V3 uses. `Artifact ID` identifies the retained source blob. Receipt IDs are the existing acquisition lineage attached to that artifact. The assessment record digest is provided so the rights decision can be checked without including copied source text.

### Australian Red Cross Society (ABN 50169561394)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:fe2d1d884e78198d18bd448904da3cd397f4f26f53075986cf067ae1ddbb95c2`; source record: `srcrec:b6fcbd45f255e0fac946aaf59378da41e2601b1d932ee4659f8247723dbd9b17`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/804f9f79-dab9-f011-bbd2-7ced8d32320c>
- Exact representation SHA-256: `c0a2fe710acca0d8d4e34116a2790755be34b2eff71b277a46214ce0e05b1a95` (20142 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `2ee99824c1c4fecd29709baef51562e7b919d2ab464d8cf1773cfdc3373af44f` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:736c63d4bd196176808d3f18a22f0bc41b26299c0d78969dac7339575ad6b10e`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:f8f0b72dd0deed2f0e8037aec593ae416c0390760346649a016f6fa64f0de7ca`; source record: `srcrec:7de5fdd0c663304aa73a11e51a3875a7c37f3c6329df9b7205ec174d0db006a1`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/3474837c-38af-e811-a95e-000d3ad24c60-74f2df7d-14bf-4dfd-b178-99ca03fb7da8-Financial%20Report-b258d370-dab9-f011-bbd2-000d3a6a0cf2-2024-2025_Australian_Red_Cross_Annual_Report.pdf>
- Exact representation SHA-256: `a7a8fed716d4df9783579911ef892eb24c4e6e771f54a6cee1bbdc43a363d342` (5398 characters).
- Selected source PDF pages: 1, 2, 3, 4 of 122 (3.3%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `84c18f2213948ddadc33103a1a1b7cd3ce222afcdbcfe19a1b3f52def1a07ff6` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:4fc197477bc366cd1593080e662043f95af9eaf906354b309514b76115002762`, `acq:a7a7ab326a5d02a9952fde0ae3878bdbdfddf070c47a5ffe28fdc03f2fcf59f0`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:abf828c9732e6049690f3dbba157d0d39e7a600df24d7b4e58ac3e8509b045bc`; source record: `srcrec:4743c8f9750b1a8be7afbab3e148dbe38ef3278d58b1712f915c00d7a9d7016d`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.redcross.org.au/>
- Exact representation SHA-256: `e9816c1428df6ca2293081d0ea29f38b2b053f6e1d30ba108b61f691620d7153` (4622 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `d1591ca42c3b3517b32c78b2a2c7ace1daead8b5e301fe67550eff2387d94e08` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:cbf7ceb2b08c3e50db02fcc77f1ca6bc485ba89232753ac67d64bb9fcfaddffb`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### Bush Heritage Australia (ABN 78053639115)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:8bab369625eaeee7eb5eca6e614e35b198de81d7c7ad24b35d4904520563c574`; source record: `srcrec:7cb70d6c23be8e1003453ff5db1c627f9af0c0ff6ca31a396c4d9a7804af2d63`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/fa7de00b-c999-f011-b41c-7c1e528a8d67>
- Exact representation SHA-256: `9b9e2b5281112cd40ad936251be5c61e17764bc7badcb3a26843180b9a886456` (13597 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `bd4a841b0616b50f360e940d4863921616186b07b0a4c1a6a2a354ab17c59373` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:8662bdd6a2999e5fe7d82823e71be00d8a65010807a5d7fdc032306602111588`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:114fbe39092dee196c4240fd83da98de62c5c6f723b0cc5d368a66ad20519012`; source record: `srcrec:648604698833daa698d52aef656b454f0703f34eae903edfd426db01495c7613`; role: `annual_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/54ae8ce0-2daf-e811-a961-000d3ad24182-5a78c0c2-fe65-44ce-a2d7-bee578d1e65b-Annual%20Report-20e13893-e49c-f011-bbd2-6045bdc40aa5-Bush-Heritage-Impact-Report_2024-25_v2.pdf>
- Exact representation SHA-256: `4d8c447672de6e507940d8fde68563be6e2b8b2c3ae2820f7bd32dff7ee0055b` (6917 characters).
- Selected source PDF pages: 1, 2, 3, 4, 5 of 64 (7.8%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `b986722801d31813456a375f75bec4caec1c021ee07a0a57a7bb13d1aa2d696c` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:c3e203b08de7aea0ae946d42f17b85ba96244e414b2226898cfe0b377706eb19`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:15f60c66a5a6b18386fab7d5ba87c7676c5c94d9deb7dca1ad466242f982d5a5`; source record: `srcrec:e60d7d6270bc8c069ed4c8c7d86730d3ddc59380f43ed83521f30be1f948084a`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.bushheritage.org.au>
- Exact representation SHA-256: `37a2a6b5b6a1074e2e56e3adf772f34844c740f50c203d67690500ca3f618223` (9259 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `0001bbe2840ae68bfd62100f1968bcd1855850b64126337b3b59e575b235eedd` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:c356d931d81066df95e349b74fd7ec8dd6e415de45673d50b69421c9ee1ae8e2`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### Greenpeace Australia Pacific Limited (ABN 61002643852)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:79b5fe3929ca3ec89419992930d9252b78997f6b6314d19d86e096cf0e1c17e5`; source record: `srcrec:1da5b2e18c676e613b950c85fc0fdee19a55a2993c55ff9d4d0bb9bd2c01822a`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/4d50d9cd-6865-f111-a826-6045bde5b710>
- Exact representation SHA-256: `912542f3018d66c6a02c65ac63ab1f6f92c2e8390b5158b4f90ca735aed41ff7` (13171 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `f871cc7a87014137597e3a681b6b18bc7664d239e31458a394319a2e0ba203da` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:d3a4b50c49b901a1524e74455537d9533acec9d927e78e041577f6fe12166f8f`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:af7655f46eb41466109397c6a2d7fd8e045219695b8baf183968be61d84d2fa0`; source record: `srcrec:464b9bba0bb1e497ee89f215b5573f028ecaf9d16dada766292694b8fe3ea735`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/8e28f2a8-38af-e811-a963-000d3ad244fd-f029bdd2-24d0-4400-8bf9-afd029b7ab23-Financial%20Report-5009abc5-6865-f111-a826-7ced8d33fe37-GPAP_Annual_Report_2025_-_SIGNED.pdf>
- Exact representation SHA-256: `2b2b42e9b967d388e2754460e7d2c41fbae8b1b5a3db6227bfb9658f142a8168` (12303 characters).
- Selected source PDF pages: 1, 2, 3, 4, 5 of 33 (15.2%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `6d8b61106c54dc95e36686faa49069b48cf96af7d8fb36745ce95fd2cb3b29dc` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:4040b9f0f3ecb79827002135745a9d695945b50ff738b75db6c3e876ac6c51e2`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:02d206f43c555483be08191be154f94c518aae4f985750a3be514c54be224547`; source record: `srcrec:0b4004d3872a52f076f74d42a524f32f7ee5f8433821d9b6a5e54f6c1fd64204`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.greenpeace.org.au/>
- Exact representation SHA-256: `33890bbf462c78bab23b0567c24dadbd59fe7742b004232c738dc3a1cd831840` (15652 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `ec053e42898f395d026d1666697ced7025e36f5f746ded080040a1b686500c8a` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:ed859ed9402a4a81a8168aa566b05003e551bda14ef3f05c58538afeb316d622`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### Royal Flying Doctor Service of Australia (Queensland Section) (ABN 80009663478)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:134504be6b3b2324132291cbeb80029ffbd520bc43a72b1332d03500cca78d08`; source record: `srcrec:4a3b655e6e10d07ac05f0b522c18a8f6324708a805e9ff442a8db5fe331fb52e`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/2f4caacc-48c0-f011-bbd2-7c1e5262dd07>
- Exact representation SHA-256: `854e5df432c1a002a99e3a697cc18089b067af19aa7c51c1ee1aec6b6b3f83d7` (9692 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `b5b41d90afec9250f7aaa85defd019335107df5c367862680f83a52908c6d969` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:2ee61241aa3db6f54e9d2a75cf3e061ba88d5de23495d62dc850a3bc7f1f6481`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:c58e7f244961750bb7c3d8e10fce2703e86efbb9166b66ff90c0a798bfc7adcc`; source record: `srcrec:77f05fe40e7284d064b5d0cc5f79f4e7f044f2cb60148b2c4382bd291fd9e993`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/cd1eb9e5-38af-e811-a963-000d3ad244fd-67f15fa9-4249-41f0-845c-614cb2240584-Financial%20Report-3c5c77c9-48c0-f011-bbd2-6045bde61dfb-Annual_Report__FY25_Official_Web_Version.pdf>
- Exact representation SHA-256: `3e877c044bc16b52c857fb79508d497a6d6d22788a61eb355e90550e81098bc0` (4659 characters).
- Selected source PDF pages: 1, 3, 4 of 34 (8.8%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `6d8a95c3245ab0d84156de33684ff52eeb87158b7b2bfac7ca59038d0e9d1153` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:1909165abf1386599dddc6f9b518524af54b30675e759b5ecfc15b9fd85dad40`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:7000827803ce85cdf6a623e0bfca85ba04a3c2518b16ea71f323b82f1c697a47`; source record: `srcrec:68a16eae0decd536fc934ac2ac19005117e89cb93ad838613cc390778be62120`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.flyingdoctor.org.au/qld/>
- Exact representation SHA-256: `b8565ace7aab699cdd1d4fc1b1c76a4df8bcf932ebdd848f20ba7673b6b91185` (5172 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `4aac0a9693edec7c1429092939baed72fc6b9deccb31c68ba43e45856dd151b4` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:08411a2b073aef586248bb0da2e7369fc808d69f0b1818b928ea3063d9edea38`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### St George Community Housing Limited (ABN 32565549842)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:e425e381eb9f430f281a25b35b97783faec3e5810c9821eb7d6b6d01302b5356`; source record: `srcrec:3954602adfd1244a9c947e022946343a46961b85bfa0a101861724bcc8f10674`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/1f7817bb-2cec-f011-8544-6045bde4e64f>
- Exact representation SHA-256: `e657768b1296e64669dce2f37cb3e7043628c2dae69226689886f37cf00d531f` (9403 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `4f87b810021bfe54847f11115b338f0fbf230ae13f88ede264efdd283eb666f4` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:4243c1b5ab4f9258a6cf3348ba0e5e646e0ee26779033bf3ec4fc84bde85403c`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:439a724994278222d8394973202ac4d1049e6cd617bcbf3d12edf5e3c0114023`; source record: `srcrec:3859ad2350896a32595fbe97752d4d8957af35fc5a755ad49d7a6ada71ae2f33`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/a8a8d9e5-2daf-e811-a962-000d3ad24a0d-6285f0f5-17d8-4553-bad8-600c64b0a9fd-Financial%20Report-143bdead-2cec-f011-8406-7c1e522ab269-FY25_St_George_Community_Housing_Limited_Financial_Statements_FINAL_SIGNED_-_KPMG.pdf>
- Exact representation SHA-256: `2250b60d007deda01d6d42757f071d13edddae5e692d0215b2f8097c688b27aa` (12426 characters).
- Selected source PDF pages: 1, 2, 3, 4, 5 of 39 (12.8%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `2aadfe97289eb80c8f663338377a9ef942856abb4017ccee9d18a1649bc3bbb7` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:b356f171a13ce20c6c85853a0fa6a294b883c80de7c147b0e1a65d3bf77eebf2`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:8e25a63f7670a5cb85808df3186e7a1bbf30801436eaf8daeca2944ec74dd795`; source record: `srcrec:516f98a4687df0bc49f009a4cc206cb10e2d1fc4d7ecd8980d505487614660a1`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.sgch.com.au>
- Exact representation SHA-256: `3d67246208c74fb50e520592d5d11e5eac25cebaee50ea32d9d96ffa6889eb64` (4321 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `845b80441007aafa6d76fdff659e9e0a3495c24f84f97c6e19a6056ceee12141` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:98b8ebbbd2786b347da13f632fba23ad0bb329ee616952bbfdf4941a47c0d350`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### The Leukaemia Foundation of Australia Limited (ABN 57057493017)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:6f5433292d31ede2d8b0bbe5a024d3143a12cca600f340e653a01b85526282cf`; source record: `srcrec:f45e6d4d180d3ee4d3919c2232da7ea730eb4f4295ae141c61588660b35d20ab`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/f419ff2d-4ace-f011-bbd3-6045bde61dfb>
- Exact representation SHA-256: `f36e257a66b3cdf41597718b5c065751b932d333095b6f49af08b41e0118a371` (14072 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `6c3df83d36d1e54a979cc9e6428539cc19626fbfa59b93fe653d692fb798978a` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:cc6f5c4a47ecfd189f9dc52145b953b36cb1294f8f36d5032ac32b4a4bf1a002`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:5e51703003ed000775c41b90e4fed3177cae1118c7a1dd8ad1e0fe010683fdef`; source record: `srcrec:863b51f86c910ac382b1da05a60c70d61168fed2a2d3ccd198420e2e6df9c47a`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/52cae909-39af-e811-a963-000d3ad24077-39064b33-3443-4565-bc9e-436f4cde0b35-Financial%20Report-bef0161c-4ace-f011-bbd3-6045bde67d52-FY25_LFA_Audited_Accounts_-_executed.pdf>
- Exact representation SHA-256: `dbf5c83b4d450581d428f9686415f960a4e3dc13ae8c2a4450abbf26e4aa25ca` (9482 characters).
- Selected source PDF pages: 1, 2, 3, 5 of 29 (13.8%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `ab2fe2059fc082800b00dac8f068524513cce6b527813eae519556a8ab934c05` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:7e3959b29ed12129ac58b9a442d5e19a87b770622052301942b655a02aea9efa`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:f91f1e8874ed0ca662f72eafe257dad09b673fa278f62fa4876eb5d8cf419ba6`; source record: `srcrec:25246834b21052feb5ea7ff7b90d153df4ab523ebe30e4e82e86a5cdd8119c09`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.leukaemia.org.au/>
- Exact representation SHA-256: `d5b82d4cf49941800984bc8743ddc473ed5a68c1c38d3ba74765aa672fa5472b` (9480 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `9a5594fddbcc5959cd3d0b5fa7a0498620a600db5729b64d341faba0353e2da1` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:d74b624526135c1625777016753d92067b59aaf44f5fbdc38b0c226e69e85b71`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### The Smith Family (ABN 28000030179)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:042ea52404924f92bfdd5c0d813a8b05ae4c5d4061b116f6b5bc97fe2154f58b`; source record: `srcrec:82d38012faefe4e307481181e69f648890e925b9a4a95650f81db8bee7088a37`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/36824617-67d9-f011-8543-7ced8d32d0e3>
- Exact representation SHA-256: `3217e5138552b6d9b7818f941f106523db4fb8b4433a35040a3363389daf1852` (14652 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `e21e31a6edf6ffbc7f67758e9a5bdc17ef9055415210d717c94757211b17c491` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:3981112b9a296b3f15233f9e2e6cbf6f576ec1eace8dae29fee82c2b2ed4e180`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:1615b7da778e57a09456405577edfb7a9bca6192ae8ecaa4099d382a79f0e983`; source record: `srcrec:5e852b575d3bb4dcff99e9fcccede508dc5626a7762af1253d723f19a39a959c`; role: `annual_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/c5fb7e82-38af-e811-a960-000d3ad24282-54098a92-8ed4-4281-ad76-799c4c2cf444-Annual%20Report-c4712e74-68d9-f011-8544-7ced8d344b97-The_Smith_Family_Annual_Impact_Report_24-25_ACNC.pdf>
- Exact representation SHA-256: `761328a2f76b65980361e89c29e5277c7be723e5faead940753fa98c4feebf75` (10892 characters).
- Selected source PDF pages: 1, 2, 4, 5 of 52 (7.7%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `672c44536bb7212a8a35efa3f9a91e12f28859f2e09a6170257211414678f5ad` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:76c6c4c3db0ed145bfacaf343090c15d12cff80f9c3a184dfb94bf085da7a778`, `acq:608a32d42392bc239626f15b44cd19e0ccf1cfee5b4e24a3018c7e67fa7ee8fc`.

**official_website** - `prohibited`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:baa05bb1284f0eadb1f16018c375d7d800245ca6892fa4b64c8826415b9285d9`; source record: `srcrec:b3656626028c76a8e3a78464eb5bcd8c386c9a481bf08629643bb2e5e4f59033`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.thesmithfamily.com.au/>
- Exact representation SHA-256: `a7e78ce17414cc9db1d9c424df79110c3967fa9e13f0cbc4fef97c47ba450d65` (9078 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `c26e8dc1215edd5e4a50d7dc4a1141fdf7beef2b6305bdce16e1ac35387b50ae` at `https://www.thesmithfamily.com.au/-/media/files/policies/website-terms-and-conditions.pdf`.
- Existing acquisition receipt lineage: `acq:8d61a6c3da379d0a769da5e92ad8ef467cad1f692eda86577a1d2d62a4d1a2a2`.
- Blocker: explicit source-term prohibition.
- Explicit prohibition evidence: [The Smith Family Website Terms and Conditions](https://www.thesmithfamily.com.au/-/media/files/policies/website-terms-and-conditions.pdf) prohibits data mining, robots, and similar data-gathering or extraction.

### The Sunrise Project Australia Limited (ABN 65159324697)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:0d79334b7bb3b9005e609f416e2706936f5ef39e963e50a92613fcc037ecf881`; source record: `srcrec:e1432a47d4d721d5652d0185371c61bd5444a6ddead1f62018987b2074ffe3fa`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/9b7195fd-0671-f111-ab0d-002248954ea6>
- Exact representation SHA-256: `ead3fcf61b706f000a699bab7ca0d9212a8f7ac31e3b27f9c21089c76feafa46` (9930 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `0645adf347bbf18c8262476bb6a1e373586ebf9c62778c4f422fbac02cf4683a` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:4d4199672b3fac6fc28c776708cc11e1ccff61b15c7931e0734046910b51d810`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:707f14459082702c384c6c79c205ce06ac32a4cf569a46fa63ca323ba3db8b11`; source record: `srcrec:5dd5e33b9ce104902588d0292db6eaf2326236c29c1d33d8e742dc4a4e09601d`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/fd27e06b-38af-e811-a962-000d3ad24a0d-e1600206-c6ea-46a7-a7bb-d9ae5b0f32a8-Financial%20Report-4729b3f2-0671-f111-ab0d-0022489549a2-The_Sunrise_Project_-_2025_Financial_Report_(signed)_(2).pdf>
- Exact representation SHA-256: `2c562da147ef17189cd0963e9d471da066f602637571284c3e572f53624e60a6` (13203 characters).
- Selected source PDF pages: 1, 2, 3, 4, 5 of 26 (19.2%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `aa7e8547afdb459a0c3f9ff4ae2e525846bcbaeaeca8735f1f55e705dae3917a` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:6c3c01b3b5b04ff59d5daf1def51a43d0f11206668ef007dad7e271f9f68fc66`.

**official_website** - `statutory_exception`; representation `complete_or_near_complete_work`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:82e89aa641ad312b8e7e9796c0c79540f9cfc87ba35623c6f0883b4ed1131a75`; source record: `srcrec:590934a40473b3f213401265578cbc2d49113107a034dc962e5bd98c44e94ea3`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://sunriseproject.org.au/>
- Exact representation SHA-256: `f35df0c49cdc53226cb2e1642ca16dd02d59ac186675a1845cd5c44058cb121a` (6224 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `f6a76be5d666859eb17f776656c607b4a145eb11ffd30fb164464b52446cb406` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:36d5305e22313b5e99921f71f50f855fe13e134d928318ce543825ecdc67a44b`.
- Blocker: complete/near-complete homepage outside Fair Dealing V1.
- Blocker rationale: this is the complete or near-complete captured homepage; V1 excludes such representations. No other clear prohibition applying to this analytical use was identified in the reviewed official material, but silence is not permission.

### World Vision Australia (ABN 28004778081)

**acnc_ais_bundle** - `statutory_exception`; representation `structured_factual`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:ca734a664418ef7a903dcaad772b6685b03953c123ac362bcaead131b8df9c14`; source record: `srcrec:050749c1866ee0ca9a34c492567398686011afa70d97949bfd386510e6f18611`; role: `historical_frozen_regulator_material`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.acnc.gov.au/api/dynamics/entity/8aaf1465-3e27-f111-8341-0022489549a2>
- Exact representation SHA-256: `fb45eabaf00f2455f7706e7ebaf74e5d1e1eb6b80cd0f1e9f3cf6ae08c04a4ad` (17331 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `6150d9adfc06a7c07ef02f970c6ae7ec23acb42cbc3979bd65a9285d968ca66f` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:d0cbb3380c4a123d89c94bfe6c3b5aa5bebd5b1a3c5f3cd284331a99bd3f38ce`.
- Classification basis: one source-native ACNC entity record at its entity endpoint, not a bulk dataset; exact CC dataset/version binding was not established.

**annual_report** - `statutory_exception`; representation `bounded_excerpt`; provider transmission **allowed**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:d14c07377b49a3e9c6d2dc2a1a20cccc7c0868d0fd6eee52953fca0a334207db`; source record: `srcrec:735604fbb77b48126df73e729ac57f52fc3134b101ae967a371baf274da8ee88`; role: `financial_report`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://acncpubfilesprodstorage.blob.core.windows.net/public/32477d82-38af-e811-a95e-000d3ad24c60-db4f7abc-04c5-4789-9ff2-9a7e8a83a406-Financial%20Report-9133735b-3e27-f111-8341-70a8a5543577-WVA_FY25_Financial_Statements_(signed).pdf>
- Exact representation SHA-256: `22131c75cf0f010bdf8da6e3eaafb3d275bc07f7b21097096facf8082e80885c` (11395 characters).
- Selected source PDF pages: 1, 2, 3, 4, 5 of 51 (9.8%).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `77d823713318d484cad1d6ea13e3fbd13f551794551f950dd910a430513a2244` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:8aa0ef5a04524bf2d5272f172d557d8a78329a56496257656aa191dcadd61980`, `acq:4b849d4f73bab3a92b73983d6f8d22de848b1ceaa85226f03c05bd2006d4e616`.

**official_website** - `statutory_exception`; representation `unclear`; provider transmission **blocked**; public redistribution **not allowed**; local retention **not authorized by V1**.

- Artifact: `srcblob:e98d5ba651d4619426c113f848a658f509cc6c95251b5221cd2ab49efe9b1903`; source record: `srcrec:7d3f0e0cd8dc292c8b65fb36ccfd955f62aaa6cdbe2e7a6b3fef1fd0943f3407`; role: `official_homepage`.
- Public access: affirmative (the retained acquisition receipt records an available HTTP 200 response; no authentication, paywall, circumvention, or bypass was recorded).
- Origin: <https://www.worldvision.com.au>
- Exact representation SHA-256: `9e948b8f8e9fc1796b8bb8168f0c250b6317a9c3379f8574d38728e2a531e94f` (43 characters).
- Policy IDs: `AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1`; provider-processing policy `OPENAI_API_BUSINESS_NO_TRAINING_DEFAULT_AS_OF_2026_09_13_V1`.
- Assessment evidence: `b3dbec1a11619f8a9a0e734f0f7b8edd7a6d10231973f43d0e3cf50e9029629b` at `policy://AU_FAIR_DEALING_ANALYTICAL_PROCESSING_V1/v1#artifact-assessment`.
- Existing acquisition receipt lineage: `acq:ef7f41a7b3f276e4e4645c2d5fb94bf9302e4463fcd2f614466ab03851fecfb8`.
- Blocker: representation class unclear.
- Blocker rationale: this retained 43-character representation is too short/context-poor to classify affirmatively as a bounded excerpt; uncertainty fails closed.

## Offline V3 request-level preflight

The unchanged execution manifest contains 12 schema-certified attempts. Each attempt uses three representations for its subject. In every attempt, the ACNC entity record and annual-report excerpt are authorized under Fair Dealing V1, but the homepage is not; therefore no request is rights-ready.

| Capability | Subject (ABN) | Request item | Aggregate rights status | Exact blocker |
|---|---|---|---|---|
| outcomes | The Smith Family (28000030179) | `requestitem:2501833e2328ae3a483bd1fbfb1dc880c3ecbf795ecd8b4b55e3dc612b7f576b` | **blocked** | srcblob:baa05bb1284f0eadb1f16018c375d7d800245ca6892fa4b64c8826415b9285d9 - explicit source-term prohibition |
| outcomes | The Smith Family (28000030179) | `requestitem:9d14cb5d528e169039b5b4d5919d8cd639a21340cc25ce42aeba638f176d0b3e` | **blocked** | srcblob:baa05bb1284f0eadb1f16018c375d7d800245ca6892fa4b64c8826415b9285d9 - explicit source-term prohibition |
| outcomes | World Vision Australia (28004778081) | `requestitem:9c430f181164a9b42b88234c45959747fbf2d697c88091523927ff98d1159354` | **blocked** | srcblob:e98d5ba651d4619426c113f848a658f509cc6c95251b5221cd2ab49efe9b1903 - representation class unclear |
| outcomes | Bush Heritage Australia (78053639115) | `requestitem:1d42fb307cf25898123966e81284d574d9a70fb57fd66bcdc4d567860f3ee97c` | **blocked** | srcblob:15f60c66a5a6b18386fab7d5ba87c7676c5c94d9deb7dca1ad466242f982d5a5 - complete/near-complete homepage outside Fair Dealing V1 |
| commitments | The Sunrise Project Australia Limited (65159324697) | `requestitem:1c88c7477aa667fb86fe012af5757107ecd3fe5f08d41eefcd71f3a2083f6ca0` | **blocked** | srcblob:82e89aa641ad312b8e7e9796c0c79540f9cfc87ba35623c6f0883b4ed1131a75 - complete/near-complete homepage outside Fair Dealing V1 |
| commitments | Australian Red Cross Society (50169561394) | `requestitem:665268cb712a785207621a61aa423d2fc5b2b3dfc291951907ed31772ef59255` | **blocked** | srcblob:abf828c9732e6049690f3dbba157d0d39e7a600df24d7b4e58ac3e8509b045bc - complete/near-complete homepage outside Fair Dealing V1 |
| commitments | Greenpeace Australia Pacific Limited (61002643852) | `requestitem:dcb75d4fb993d07ce0af4ed79676ef95f39b6097ddd65ccdc804487575b628ad` | **blocked** | srcblob:02d206f43c555483be08191be154f94c518aae4f985750a3be514c54be224547 - complete/near-complete homepage outside Fair Dealing V1 |
| commitments | Greenpeace Australia Pacific Limited (61002643852) | `requestitem:75d9e779c29daf61612e0ed6a0e6e279c76b0fb4cc49e9b2222f10094361cd3e` | **blocked** | srcblob:02d206f43c555483be08191be154f94c518aae4f985750a3be514c54be224547 - complete/near-complete homepage outside Fair Dealing V1 |
| capacity | St George Community Housing Limited (32565549842) | `requestitem:4932012ed5dff11d317eef43ba42141dbd0a66a7d332991f2549e2bb450252af` | **blocked** | srcblob:8e25a63f7670a5cb85808df3186e7a1bbf30801436eaf8daeca2944ec74dd795 - complete/near-complete homepage outside Fair Dealing V1 |
| capacity | St George Community Housing Limited (32565549842) | `requestitem:2476ab0585d5c64f181b3d3d9cd0778888e8ef75996c211a8058891154595b87` | **blocked** | srcblob:8e25a63f7670a5cb85808df3186e7a1bbf30801436eaf8daeca2944ec74dd795 - complete/near-complete homepage outside Fair Dealing V1 |
| capacity | Royal Flying Doctor Service of Australia (Queensland Section) (80009663478) | `requestitem:2131ff6cee83f469a2146deb6dc21b65be33f7e3ee0a2a4c0b1eecc856d8a4fe` | **blocked** | srcblob:7000827803ce85cdf6a623e0bfca85ba04a3c2518b16ea71f323b82f1c697a47 - complete/near-complete homepage outside Fair Dealing V1 |
| capacity | The Leukaemia Foundation of Australia Limited (57057493017) | `requestitem:1463297e2d921cee03dd36e87caafe324e6b5cfbb87e17fa7a7594555e2c5186` | **blocked** | srcblob:f91f1e8874ed0ca662f72eafe257dad09b673fa278f62fa4876eb5d8cf419ba6 - complete/near-complete homepage outside Fair Dealing V1 |

**Preflight result:** 0/12 authorized; 12/12 blocked; provider calls 0. The gate checked each exact representation hash and bound artifact ID, source record, origin, role, and acquisition lineage. V3 remains `prepared_not_sent`; no request was posted. The offline check does not modify the execution authorization flag or grant permission to execute.

## Predicate record and limits

For every authorized Fair Dealing row, the assessment affirms public access without circumvention, no access-control bypass, lawful acquisition, the approved evidence-grounded knowledge-construction purpose, the bounded representation class, no identified explicit prohibition, and exact source/receipt lineage. The provider-processing policy ID records the OpenAI API/business default that inputs and outputs are not used for model training unless the customer opts in; it does not supply source permission. The selected service, applicable policy version, and actual no-opt-in posture still require rechecking before any separately authorized execution. [OpenAI Business Data](https://openai.com/business-data/).

The policy decision separates lawful public access, bounded extraction, private provider analysis, local retention, public redistribution, derived facts/assertions, and publication of evidence excerpts. It provides no general retention or republication permission. This assessment authorizes none of the V3 campaign as a whole: every request includes a blocked homepage input. No source representation was shortened, substituted, or otherwise changed to pass the gate.

The machine-readable artifact decisions and exact offline preflight JSON were retained outside Git in the private assessment work area; they contain provenance and hashes but no copied source text or credentials. The Git assessment above records the decision fields needed for future review without publishing source bodies.
