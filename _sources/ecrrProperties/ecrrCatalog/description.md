## ECRR Catalog/Repository Properties

Defines properties specific to catalog and repository resources in the EarthCube Resource Registry. For resources with `mainEntity` pointing to `ECRRO_0000212` (Catalog/Registry) or `ECRRO_0000209` (Repository).

### Properties

- **schema:contentType** — types of objects cataloged or stored (array of Thing objects with name and identifier)

### Example

```json
{
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Rock magnetic data",
      "schema:identifier": "https://example.org/concept/rock-magnetic"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Paleomagnetic data"
    }
  ]
}
```
