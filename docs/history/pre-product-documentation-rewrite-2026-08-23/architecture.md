# CharityGraph architecture

CharityGraph separates authoritative data from derived delivery formats:

1. source-native records retain a source's original structure and provenance;
2. canonical observations bind evidence to subjects, time, taxonomy, and claim basis; and
3. derived projections provide cards, JSON, Markdown, CSV, Parquet, search indices, and other consumer formats.

JSON and Markdown cards and their sidecars are authoritative publication artefacts. CSV and Parquet are projections, never the sole source of meaning. Public contracts, schemas, taxonomies, releases, and governed shared project documents live in this repository; production code belongs in the sibling `charitygraph` repository.
