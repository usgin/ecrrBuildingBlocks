## ECRR Semantic Resource Profile

Complete metadata profile for registering semantic resources (ontologies, vocabularies, thesauri, etc.) in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrSemanticResource** — semantic-resource-specific (programming/representation language)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Semantic Resource"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000210` (Semantic Resource)
