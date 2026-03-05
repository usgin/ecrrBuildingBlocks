## ECRR Software Profile

Complete metadata profile for registering software and application resources in the EarthCube Resource Registry.

### Composition

This profile composes four building blocks using `allOf`:

1. **ecrrBase** — mandatory identity, type, name, description, mainEntity classification, license
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrSoftware** — software-specific (application categories, runtime platforms, programming languages, supporting data, code repository, install URL, dependencies)

### Type Requirements

- `@type` must include `schema:CreativeWork` and `schema:SoftwareApplication`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000206` (Software)

### Key Vocabularies

| Vocabulary | Property | Description |
|-----------|----------|-------------|
| SFO_ | applicationCategory | Software function categories |
| RTE_ | runtimePlatform | Runtime environments |
| MTU_ | ECRRO_0000138 | Maturity state |
| ELT_ | ECRRO_0000219 | Expected lifetime |
| UBA_ | ECRRO_0000017 | Usage level |
| ADO_ | about | Science domains |
| AUT_ | audience | Target audiences |
