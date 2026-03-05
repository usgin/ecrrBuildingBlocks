## ECRR Specification-Specific Properties

Defines properties specific to specification resources in the EarthCube Resource Registry. For resources with `mainEntity` pointing to `ECRRO_0000204` (Specification).

### Properties

- **ecrro:ECRRO_0000501** — parent specifications that this specification profiles or extends

### Specification Subtypes (SPKT vocabulary)

Specification subtypes are conveyed via additional entries in the `mainEntity` array. The SPKT vocabulary includes:

| Subtype | SPKT URI |
|---------|----------|
| Data Format Convention | `SPKT_0000001` |
| Naming Convention | `SPKT_0000002` |
| Web Service Convention | `SPKT_0000003` |
| Data Model | `SPKT_0000004` |
| Information Model | `SPKT_0000005` |
| Protocol | `SPKT_0000006` |
| Encoding Standard | `SPKT_0000007` |
| Transfer Standard | `SPKT_0000008` |
| Metadata Standard | `SPKT_0000009` |
| API Specification | `SPKT_0000010` |
| Profile | `SPKT_0000011` |
| Quality Standard | `SPKT_0000012` |
| Security Standard | `SPKT_0000013` |

### Example mainEntity with Specification Subtype

```json
{
  "schema:mainEntity": [
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000204",
      "schema:name": "Specification"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Data Format Conventions"
    }
  ]
}
```
