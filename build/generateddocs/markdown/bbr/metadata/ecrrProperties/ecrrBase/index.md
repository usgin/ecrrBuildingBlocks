
# ECRR Base metadata (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrBase` *v0.1*

Schema defining mandatory properties for all EarthCube Resource Registry (ECRR) resource types. Includes resource identity, type classification via mainEntity, and licensing. Defines properties: @id, @type, schema:name, schema:description, schema:mainEntity, schema:license. Uses building blocks: labeledLink (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Pyleoclim Software - Base Fields
ECRR base properties for the Pyleoclim software resource, including resource
type, name, description, main entity classification, and license.
#### json
```json
{
  "@context": [
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g22914",
  "@type": ["schema:CreativeWork", "schema:Product", "schema:SoftwareApplication"],
  "schema:name": "Pyleoclim",
  "schema:description": "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206",
    "schema:name": "Software"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License (GPL)",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/SWL_0000017"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ecrro": "http://cor.esipfed.org/ont/earthcube/"
    },
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g22914",
  "@type": [
    "schema:CreativeWork",
    "schema:Product",
    "schema:SoftwareApplication"
  ],
  "schema:name": "Pyleoclim",
  "schema:description": "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206",
    "schema:name": "Software"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License (GPL)",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/SWL_0000017"
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g22914> a schema1:CreativeWork,
        schema1:Product,
        schema1:SoftwareApplication ;
    schema1:description "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues." ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "GNU General Public License (GPL)" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/SWL_0000017" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Software" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206" ] ;
    schema1:name "Pyleoclim" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Base metadata
description: Mandatory properties for all EarthCube Resource Registry (ECRR) resource
  types. Every ECRR resource must have identity (@id), type classification (@type),
  name, description, resource type classification (mainEntity), and licensing.
type: object
properties:
  '@id':
    type: string
    description: Globally unique identifier for the resource, typically an ARK identifier
      (e.g. http://n2t.net/ark:/23942/g22914).
  '@type':
    description: Array of schema.org types. Must include schema:CreativeWork. Additional
      types (schema:SoftwareApplication, schema:WebAPI, schema:Dataset, schema:Product)
      indicate the nature of the resource.
    type: array
    items:
      type: string
      enum:
      - schema:CreativeWork
      - schema:SoftwareApplication
      - schema:SoftwareSourceCode
      - schema:Product
      - schema:WebAPI
      - schema:Dataset
      - schema:DataCatalog
      - schema:DefinedTermSet
    contains:
      const: schema:CreativeWork
    minItems: 1
  schema:name:
    type: string
    description: The name of the resource.
  schema:description:
    type: string
    description: A text description of the resource, providing enough detail for discovery
      and basic understanding of the resource purpose and content.
  schema:mainEntity:
    description: ECRR resource type classification. Array of labeled links (CreativeWork
      objects) with name and url pointing to ECRRO resource type URIs. The first entry
      identifies the base resource type (e.g. Software, Service Instance, Specification).
      Additional entries may specify subtypes from SPKT_ or srt_ vocabularies.
    anyOf:
    - $ref: '#/$defs/LabeledLink'
    - type: array
      items:
        $ref: '#/$defs/LabeledLink'
      minItems: 1
  schema:license:
    description: Legal conditions governing use and access. Array of labeled links
      identifying the license(s), ideally with URIs from https://spdx.org/licenses/
      or http://cor.esipfed.org/ont/earthcube/swl.
    type: array
    minItems: 1
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: a reference to a license definition
      - $ref: '#/$defs/LabeledLink'
required:
- '@id'
- '@type'
- schema:name
- schema:description
- schema:mainEntity
- schema:license
$defs:
  LabeledLink:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)
* [schema.org CreativeWork](https://schema.org/CreativeWork)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrBase`

