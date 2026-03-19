# ECRR Building Blocks

Modular metadata schemas for [EarthCube Resource Registry (ECRR)](https://www.earthcube.org/resource-registry) resource types, structured as [OGC Building Blocks](https://opengeospatial.github.io/bblocks/).

## Building Blocks

### ecrrProperties (10 schema components)

| Building Block | Description |
|---|---|
| ecrrCore | Mandatory identity, type, name, description, mainEntity, license |
| ecrrCommon | Shared optional: identifiers, agents, keywords, domains, funding |
| ecrrAssessment | Maturity, lifetime, usage, stewardship, registration |
| ecrrCatalog | Catalog/repository content types |
| ecrrCollection | Bundled object component parts |
| ecrrDataset | Distribution, spatial/temporal coverage, variables |
| ecrrSemanticResource | Representation language for semantic resources |
| ecrrService | Protocols, interface specs, data formats, invocation |
| ecrrSoftware | Functions, runtime, languages, repos, dependencies |
| ecrrSpecification | Parent specification references |

### ecrrProfiles (11 resource type profiles)

ECRRCatalog, ECRRCollection, ECRRDataset, ECRRInterchangeFormat, ECRRInterface, ECRRPlatform, ECRRSemanticResource, ECRRService, ECRRSoftware, ECRRSpecification, ECRRUseCase

Each profile composes ecrrCore + ecrrCommon + ecrrAssessment with resource-type-specific properties via `allOf`. ECRRDataset additionally extends [CDIFcomplete](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/bblock/bbr.metadata.profiles.CDIFcomplete).

## Cross-repo imports

This repository imports shared schema.org property building blocks from [Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism:

```yaml
# bblocks-config.yaml
imports:
  - default
  - https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
```

External `$ref` paths in ecrrProperties schemas point to published URLs at `https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/`.

## Viewer

Browse all building blocks at: https://usgin.github.io/ecrrBuildingBlocks/

## License

Apache 2.0 - see [LICENSE](LICENSE).
