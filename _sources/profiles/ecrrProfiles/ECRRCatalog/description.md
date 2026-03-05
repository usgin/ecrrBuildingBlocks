## ECRR Catalog/Registry Profile

Complete metadata profile for registering catalog and repository resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrCatalog** — catalog-specific (content types)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC CatalogRegistry"` or `"EC Repository"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000212` (CatalogRegistry) or `http://cor.esipfed.org/ont/earthcube/ECRRO_0000209` (Repository)
