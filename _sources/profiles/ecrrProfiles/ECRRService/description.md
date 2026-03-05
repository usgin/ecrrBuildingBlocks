## ECRR Service Instance Profile

Complete metadata profile for registering service instance resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties
3. **ecrrAssessment** — resource assessment properties
4. **ecrrService** — service-specific (communication protocols, interface specification, supporting data, invocation)

### Type Requirements

- `@type` must include `schema:CreativeWork` (and typically `schema:WebAPI` or `schema:Product`)
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000202` (Service Instance)
