## ECRR Base Metadata Properties

Defines the mandatory properties shared by all EarthCube Resource Registry (ECRR) resource types. These properties establish the identity, classification, and legal framework for a registered resource.

### Properties

- **@id** — globally unique identifier for the resource, typically an ARK (e.g., `http://n2t.net/ark:/23942/g22914`)
- **@type** — array of schema.org types; must include `schema:CreativeWork`, with optional additional types (`SoftwareApplication`, `WebAPI`, `Dataset`, `Product`)
- **schema:name** — human-readable name of the resource
- **schema:description** — detailed text description of the resource
- **schema:mainEntity** — ECRR resource type classification using labeled links (CreativeWork objects with `name` and `url` pointing to ECRRO vocabulary URIs). This is the key ECRR pattern: resource type is conveyed via labeled link to ECRRO concept URIs, not via `@type` or `additionalType`.
- **schema:license** — legal conditions for use and access

### Resource Type Classification (mainEntity)

The `mainEntity` property uses the ECRRO vocabulary to classify resources:

| Resource Type | ECRRO URI |
|--------------|-----------|
| Software | `ECRRO_0000206` |
| Service Instance | `ECRRO_0000202` |
| Specification | `ECRRO_0000204` |
| Semantic Resource | `ECRRO_0000210` |
| Platform | `ECRRO_0000211` |
| Catalog/Registry | `ECRRO_0000212` |
| Repository | `ECRRO_0000209` |
| Interface/API | `ECRRO_0000207` |
| Interchange Format | `ECRRO_0000208` |
| Use Case | `ECRRO_0000205` |
| Bundled Object | `ECRRO_0000213` |
| Dataset | `ECRRO_0000214` |

### Usage

This building block is composed with `ecrrCommon`, `ecrrAssessment`, and type-specific blocks (e.g., `ecrrSoftware`) to form complete ECRR profiles.
