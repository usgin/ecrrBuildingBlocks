# ECRR Building Blocks repository

Building blocks for EarthCube Resource Registry (ECRR) metadata profiles,
using the OGC Building Blocks pattern.


Modular schema components for ECRR resource type metadata. Imports shared
schema.org property building blocks from the CDIF Building Blocks repository.


## Building Blocks

### `ecrr.bbr.metadata.ecrrProperties.ecrrCatalog` — ECRR Catalog/Repository properties

**Type:** schema

Schema defining properties specific to catalog and repository resources in the EarthCube Resource Registry, including content type classification. Defines properties: schema:contentType.

### `ecrr.bbr.metadata.ecrrProperties.ecrrCollection` — ECRR Collection/Bundled Object properties

**Type:** schema

Schema defining properties specific to bundled object (collection) resources in the EarthCube Resource Registry, including component resource listings. Defines properties: schema:hasPart.

### `ecrr.bbr.metadata.ecrrProperties.ecrrSemanticResource` — ECRR Semantic Resource properties

**Type:** schema

Schema defining properties specific to semantic resource types in the EarthCube Resource Registry, including subtype classification for ontologies, thesauri, controlled vocabularies, and other semantic resources. Defines properties: schema:programmingLanguage.

### `ecrr.bbr.metadata.ecrrProperties.ecrrCore` — ECRR Core metadata

**Type:** schema

Schema defining mandatory properties for all EarthCube Resource Registry (ECRR) resource types. Includes resource identity, type classification via mainEntity, and licensing. Defines properties: @id, @type, schema:name, schema:description, schema:mainEntity, schema:license. Uses building blocks: labeledLink (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrService` — ECRR Service Instance properties

**Type:** schema

Schema defining properties specific to service instance resources in the EarthCube Resource Registry, including communication protocols, interface specifications, supporting data, and service invocation. Defines properties: ecrro:ECRRO_0000502, ecrro:ECRRO_0000503, schema:supportingData, schema:potentialAction. Uses building blocks: labeledLink (schemaorgProperties), definedTerm (schemaorgProperties), action (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrSoftware` — ECRR Software properties

**Type:** schema

Schema defining properties specific to software and application resources in the EarthCube Resource Registry, including function categories, runtime platforms, programming languages, supporting data, code repositories, and dependencies. Defines properties: schema:applicationCategory, schema:runtimePlatform, schema:programmingLanguage, schema:supportingData, schema:codeRepository, schema:installURL, schema:potentialAction, dependencies. Uses building blocks: labeledLink (schemaorgProperties), action (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrSpecification` — ECRR Specification properties

**Type:** schema

Schema defining properties specific to specification resources in the EarthCube Resource Registry, including specification subtyping and parent specification references. Defines properties: ecrro:ECRRO_0000501. Uses building blocks: labeledLink (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrAssessment` — ECRR Resource Assessment

**Type:** schema

Schema defining ECRR-specific resource assessment properties using PropertyValue pattern with ECRRO property identifiers for maturity, expected lifetime, usage level, stewardship, and registration metadata. Defines properties: ecrro:ECRRO_0000138, ecrro:ECRRO_0000219, ecrro:ECRRO_0000017, ecrro:ECRRO_0000218, ecrro:ECRRO_0000600, ecrro:ECRRO_0001301. Uses building blocks: definedTerm (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrDataset` — ECRR Dataset properties

**Type:** schema

Schema defining properties specific to dataset resources in the EarthCube Resource Registry, referencing existing distribution, spatial/temporal extent, and variable building blocks. Defines properties: schema:distribution, schema:spatialCoverage, schema:temporalCoverage, schema:variableMeasured, schema:includedInDataCatalog. Uses building blocks: dataDownload (schemaorgProperties), webAPI (schemaorgProperties), spatialExtent (schemaorgProperties), temporalExtent (schemaorgProperties), variableMeasured (schemaorgProperties).

### `ecrr.bbr.metadata.ecrrProperties.ecrrCommon` — ECRR Common optional metadata

**Type:** schema

Schema defining commonly used optional properties shared across ECRR resource types, including agents, identifiers, keywords, science domains, audience, and related resources. Defines properties: schema:identifier, schema:url, schema:datePublished, schema:version, schema:alternateName, schema:sameAs, schema:creator, schema:contributor, schema:publisher, schema:editor, schema:funding, schema:keywords, schema:about, schema:audience, schema:subjectOf, schema:isRelatedTo, schema:isBasedOn, schema:encodingFormat, dct:bibliographicCitation, dct:conformsTo. Uses building blocks: labeledLink (schemaorgProperties), identifier (schemaorgProperties), definedTerm (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties), funder (schemaorgProperties).

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRCatalog` — ECRR Catalog/Registry profile

**Type:** schema

Complete ECRR metadata profile for catalog and registry resources, composing base, common, assessment, and catalog-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRCollection` — ECRR Collection profile

**Type:** schema

Complete ECRR metadata profile for bundled object (collection) resources, composing base, common, assessment, and collection-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRInterchangeFormat` — ECRR Interchange Format profile

**Type:** schema

Complete ECRR metadata profile for interchange format resources, composing base, common, and assessment building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRInterface` — ECRR Interface/API profile

**Type:** schema

Complete ECRR metadata profile for interface and API resources, composing base, common, and assessment building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRPlatform` — ECRR Platform profile

**Type:** schema

Complete ECRR metadata profile for platform resources, composing base, common, and assessment building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRSemanticResource` — ECRR Semantic Resource profile

**Type:** schema

Complete ECRR metadata profile for semantic resource types (ontologies, vocabularies, thesauri), composing base, common, assessment, and semantic-resource-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRService` — ECRR Service Instance profile

**Type:** schema

Complete ECRR metadata profile for service instance resources, composing base, common, assessment, and service-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRSoftware` — ECRR Software profile

**Type:** schema

Complete ECRR metadata profile for software and application resources, composing base, common, assessment, and software-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRSpecification` — ECRR Specification profile

**Type:** schema

Complete ECRR metadata profile for specification resources, composing base, common, assessment, and specification-specific building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRUseCase` — ECRR Use Case profile

**Type:** schema

Complete ECRR metadata profile for use case resources, composing base, common, and assessment building blocks.

### `ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRDataset` — ECRR Dataset profile

**Type:** schema

Complete ECRR metadata profile for dataset resources, extending CDIFcomplete with base, common, and assessment building blocks.

