## ECRR Dataset Profile

Complete metadata profile for registering dataset resources in the EarthCube Resource Registry.

### Composition

This profile extends CDIFcomplete with ECRR building blocks. CDIF properties take precedence for overlapping concerns; ECRR-unique properties are included inline.

1. **CDIFcomplete** — full CDIF discovery + data description profile (creator, keywords, subjectOf, distribution, spatial/temporal coverage, variables, provenance, quality)
2. **ecrrBase** — mandatory ECRR identity: mainEntity classification, `@type` must contain `schema:CreativeWork`, requires `schema:description` and `schema:license`
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **Inline ECRR-unique properties** — properties from ecrrCommon not covered by CDIF (see below)

### ECRR-Unique Properties (not in CDIF)

- `schema:about` — science domains (ECRR ADO vocabulary)
- `schema:audience` — target user communities (ECRR AUT vocabulary)
- `schema:editor` — editors
- `schema:alternateName` — alternative names
- `dct:bibliographicCitation` — preferred citation

### Property Mappings: ECRR → CDIF

| ECRR property | CDIF equivalent | Notes |
|---|---|---|
| `schema:subjectOf` (other metadata) | `schema:relatedLink` with linkRelationship `"OtherMetadataFormat"` | CDIF reserves `schema:subjectOf` for CdifCatalogRecord |
| `schema:isRelatedTo` | `schema:relatedLink` | CDIF uses relatedLink with linkRelationship for typed relations |
| `schema:isBasedOn` | `prov:wasDerivedFrom` | CDIF uses PROV-O for derivation lineage |
| `schema:includedInDataCatalog` | `schema:subjectOf` → CdifCatalogRecord `schema:includedInDataCatalog` | Handled within the CdifCatalogRecord node |
| `schema:encodingFormat` | `schema:distribution` → DataDownload `schema:encodingFormat` | Property of distribution, not the dataset |
| `dct:conformsTo` | `schema:distribution` → DataDownload `dcterms:conformsTo` | Property of distribution or Action result |

### Type Requirements

- `@type` must include `schema:Dataset` and `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Dataset"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000214` (Dataset)

### Overlapping Properties (CDIF takes precedence)

The following properties are defined by both ecrrCommon and CDIF. In this profile, the CDIF definitions are used:

| Property | CDIF source | Notes |
|---|---|---|
| `schema:creator` | cdifOptional (`@list` wrapper) | ECRR used plain array; CDIF preserves author order |
| `schema:keywords` | cdifOptional (array of DefinedTerm/string) | ECRR allowed bare string; CDIF requires array |
| `schema:subjectOf` | cdifMandatory (CdifCatalogRecord) | ECRR usage → `schema:relatedLink` instead |
| `schema:identifier` | cdifMandatory (required) | |
| `schema:distribution` | CDIFcomplete (DataDownload/WebAPI/archive) | |
| `schema:contributor` | cdifOptional (with agentInRole support) | |
| `schema:publisher` | cdifOptional | |
| `schema:funding` | cdifOptional | |
| `schema:sameAs` | cdifOptional (Identifier or string) | |
| `schema:version` | cdifOptional | |
| `schema:datePublished` | cdifOptional | |
| `schema:url` | cdifMandatory | |
