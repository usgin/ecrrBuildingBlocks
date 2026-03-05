## ECRR Interface/API Profile

Complete metadata profile for registering interface and API specification resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Interface_API"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000207` (Interface_API)
