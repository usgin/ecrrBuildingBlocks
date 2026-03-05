## ECRR Collection Profile

Complete metadata profile for registering bundled object (collection) resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrCollection** — collection-specific (component parts with type, name, URL, description, encoding format)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Bundled Object"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/SFO_0000075` (Bundled Object)
