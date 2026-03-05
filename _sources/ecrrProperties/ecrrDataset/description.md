## ECRR Dataset-Specific Properties

Defines properties specific to dataset resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:Dataset"]`.

This building block heavily reuses existing schema.org building blocks.

### Properties

- **schema:distribution** — data access via DataDownload or WebAPI (reuses existing building blocks)
- **schema:spatialCoverage** — geographic extent (reuses spatialExtent building block)
- **schema:temporalCoverage** — time coverage (reuses temporalExtent building block)
- **schema:variableMeasured** — measured variables (reuses variableMeasured building block)
- **schema:includedInDataCatalog** — reference to containing catalog (DataCatalog with @id, name, url)

### Example

```json
{
  "schema:distribution": [
    {
      "@type": ["schema:DataDownload"],
      "schema:contentUrl": "https://example.org/data/download.csv",
      "schema:encodingFormat": ["text/csv"]
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "Example Data Catalog",
    "schema:url": "https://example.org/catalog"
  }
}
```
