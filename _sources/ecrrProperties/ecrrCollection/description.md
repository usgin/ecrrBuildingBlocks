## ECRR Collection/Bundled Object Properties

Defines properties specific to bundled object (collection) resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:Product"]` with `mainEntity` pointing to `ECRRO_0000213` (Bundled Object).

A bundled object groups multiple related resources together, such as a software package with its documentation, test data, and dependencies.

### Properties

- **schema:hasPart** — component resources in the collection (array of objects with @type, name, url, description, encodingFormat)

### Example

```json
{
  "schema:hasPart": [
    {
      "@type": "schema:SoftwareApplication",
      "schema:name": "Analysis Tool",
      "schema:url": "https://example.org/tool",
      "schema:description": "Main analysis software"
    },
    {
      "@type": "schema:Dataset",
      "schema:name": "Sample Data",
      "schema:url": "https://example.org/data",
      "schema:encodingFormat": ["text/csv"]
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "User Guide",
      "schema:url": "https://example.org/docs"
    }
  ]
}
```
