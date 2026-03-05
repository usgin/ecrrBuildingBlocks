
# ECRR Specification properties (Schema)

`ogc.ecrrProperties.ecrrSpecification` *v0.1*

Schema defining properties specific to specification resources in the EarthCube Resource Registry, including specification subtyping and parent specification references. Defines properties: ecrro:ECRRO_0000501. Uses building blocks: labeledLink (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Specification-Specific Properties

Defines properties specific to specification resources in the EarthCube Resource Registry. For resources with `mainEntity` pointing to `ECRRO_0000204` (Specification).

### Properties

- **ecrro:ECRRO_0000501** — parent specifications that this specification profiles or extends

### Specification Subtypes (SPKT vocabulary)

Specification subtypes are conveyed via additional entries in the `mainEntity` array. The SPKT vocabulary includes:

| Subtype | SPKT URI |
|---------|----------|
| Data Format Convention | `SPKT_0000001` |
| Naming Convention | `SPKT_0000002` |
| Web Service Convention | `SPKT_0000003` |
| Data Model | `SPKT_0000004` |
| Information Model | `SPKT_0000005` |
| Protocol | `SPKT_0000006` |
| Encoding Standard | `SPKT_0000007` |
| Transfer Standard | `SPKT_0000008` |
| Metadata Standard | `SPKT_0000009` |
| API Specification | `SPKT_0000010` |
| Profile | `SPKT_0000011` |
| Quality Standard | `SPKT_0000012` |
| Security Standard | `SPKT_0000013` |

### Example mainEntity with Specification Subtype

```json
{
  "schema:mainEntity": [
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000204",
      "schema:name": "Specification"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Data Format Conventions"
    }
  ]
}
```

## Examples

### INSPIRE Geology Specification Properties
ECRR specification properties for the INSPIRE Geology data specification.
#### json
```json
{
  "ecrro:ECRRO_0000501": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000501",
    "schema:name": "profile of",
    "schema:value": [
      {
        "@type": "schema:CreativeWork",
        "schema:name": "GeoSciML version 3.2",
        "schema:url": "http://geosciml.org/doc/geosciml/3.2/documentation/"
      }
    ]
  }
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrSpecification/context.jsonld"
  ],
  "ecrro:ECRRO_0000501": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000501",
    "schema:name": "profile of",
    "schema:value": [
      {
        "@type": "schema:CreativeWork",
        "schema:name": "GeoSciML version 3.2",
        "schema:url": "http://geosciml.org/doc/geosciml/3.2/documentation/"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

[] ecrro:ECRRO_0000501 [ a schema1:PropertyValue ;
            schema1:name "profile of" ;
            schema1:propertyID "ecrro:ECRRO_0000501" ;
            schema1:value [ a schema1:CreativeWork ;
                    schema1:name "GeoSciML version 3.2" ;
                    schema1:url "http://geosciml.org/doc/geosciml/3.2/documentation/" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Specification-Specific Properties
description: Properties specific to specification resources in ECRR. For resources
  with mainEntity pointing to ECRRO_0000204 (Specification). Includes profile/parent
  specification references and specification subtype classification via SPKT vocabulary
  entries in mainEntity.
type: object
properties:
  ecrro:ECRRO_0000501:
    description: Parent specifications that this specification profiles or extends.
      PropertyValue wrapping an array of labeled links pointing to the parent specification
      documents.
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000501
      schema:name:
        type: string
        default: profile of
      schema:value:
        anyOf:
        - $ref: '#/$defs/LabeledLink'
        - type: array
          items:
            $ref: '#/$defs/LabeledLink'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
$defs:
  LabeledLink:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/labeledLink/schema.yaml
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrSpecification/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrSpecification/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrSpecification/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrSpecification`

