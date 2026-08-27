# ACNC 2024 AIS public-data donation ranking

Status: governed cohort-prioritisation artefact  
Reporting period: 2024 Annual Information Statement (AIS)  
Authority: Australian Charities and Not-for-profits Commission (ACNC)

## Purpose and boundary

This snapshot is the canonical ranking source for the Fresh-18 generalisation
tranche. It orders the public 2024 AIS rows by the regulator-reported
`donations and bequests` amount. It is a cohort-prioritisation proxy for one
reporting period—not a CharityGraph quality, impact, effectiveness,
importance, credibility or recommendation score. It is not an absolute ranking
of every charity in the confidential regulatory population: withheld charity
information is excluded by the public source, and the public dataset can
change as late submissions are added.

For this tranche, the Fresh-18 top 10,000 universe is donation ranks 1–10,000
inclusive. This is distinct from the historical economics ladder: Economics
C10K means ranks 1,101–11,100 (the next 10,000 after C100 and C1K).

## Frozen source

- Dataset: **ACNC 2024 Annual Information Statement (AIS) Data**
- Dataset ID: `276ec1bc-4971-461c-88bc-be9f3c99a0f8`
- CSV resource ID: `710630ea-1202-4bbb-95f7-3973a972ddf8`
- Download URL: <https://data.gov.au/data/dataset/276ec1bc-4971-461c-88bc-be9f3c99a0f8/resource/710630ea-1202-4bbb-95f7-3973a972ddf8/download/datadotgov_ais24.csv>
- Resource last modified: `2026-08-23T19:05:58.138274`
- Catalogue metadata modified: `2026-08-23T20:05:15.982597`
- Retrieved: `2026-08-27T15:11:40.5447226Z`
- Raw bytes: `37,896,996`
- Raw SHA-256: `37571caeaf011ac0098840b06fececd6ab7814111658433cd1e588340787c4ba`
- Upstream licence metadata: data.gov.au reports `notspecified`; retain ACNC/data.gov.au attribution and upstream caveats.

The raw CSV is retained in the private runtime only and is not committed here.
The public derived ranking is CC BY 4.0 under this repository's data licence,
subject to the upstream ACNC/data.gov.au terms and attribution.

## Construction

1. Read the frozen CSV as structured rows.
2. Retain rows with an 11-digit ABN passing the ABN checksum.
3. Retain rows whose exact structured `registration status` is `Registered`.
4. Parse `donations and bequests` mechanically as a numeric AUD amount after
   removing whitespace, commas and currency punctuation. Missing or
   unparseable values are not eligible; no proxy, averaging, estimation or
   prose inference is used.
5. For duplicate ABNs, retain one row only when name, registration status,
   reporting period and parsed donations agree; select the most complete
   structured row. Any disagreement would stop construction rather than being
   silently deduplicated. The frozen source has one such exact duplicate
   (`52769432651`), resolved by this rule.
6. Sort by `donations_and_bequests_aud` descending, then ABN ascending, and
   assign unique ordinal `donation_rank_2024_public` values starting at 1.
7. Publish the first 10,000 records in
   `acnc-2024-ais-donation-ranking-top10000.json`.

The JSON snapshot preserves the ABN, charity name, donation amount, source
registration status and mechanically copied structured sampling fields (size,
basic religious-charity flag, conducted-activities flag and fundraising flags).
It also records the source hash and construction diagnostics in its metadata.

## Sanity checks

- Source rows: 53,875
- Valid ABNs: 53,546
- Invalid ABNs: 329
- Missing donation values among valid ABNs: 0
- Unparseable donation values among valid ABNs: 0
- Ranked registered charities after duplicate resolution: 51,817
- Published top-10,000 records: 10,000
- Donation amount at rank 1: AUD 224,749,000
- Donation amount at rank 100: AUD 18,690,764
- Donation amount at rank 1,000: AUD 1,895,501
- Donation amount at rank 10,000: AUD 79,967

