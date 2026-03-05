## ECRR Platform Profile

Complete metadata profile for registering platform resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Platform"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000211` (Platform)
