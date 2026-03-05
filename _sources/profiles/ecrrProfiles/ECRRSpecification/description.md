## ECRR Specification Profile

Complete metadata profile for registering specification resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties
3. **ecrrAssessment** — resource assessment properties
4. **ecrrSpecification** — specification-specific (parent specifications, subtype via SPKT vocabulary)

### Type Requirements

- `@type` must include `schema:CreativeWork` (and typically `schema:Product`)
- `mainEntity` must include reference to `http://cor.esipfed.org/ont/earthcube/ECRRO_0000204` (Specification)
- Additional `mainEntity` entries may specify subtype from the SPKT vocabulary (Data Format Convention, Data Model, etc.)
