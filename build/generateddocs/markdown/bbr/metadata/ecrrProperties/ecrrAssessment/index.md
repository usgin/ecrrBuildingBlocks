
# ECRR Resource Assessment (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrAssessment` *v0.1*

Schema defining ECRR-specific resource assessment properties using PropertyValue pattern with ECRRO property identifiers for maturity, expected lifetime, usage level, stewardship, and registration metadata. Defines properties: ecrro:ECRRO_0000138, ecrro:ECRRO_0000219, ecrro:ECRRO_0000017, ecrro:ECRRO_0000218, ecrro:ECRRO_0000600, ecrro:ECRRO_0001301. Uses building blocks: definedTerm (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Resource Assessment Properties

Defines ECRR-specific properties for assessing resource status, sustainability, and provenance. These properties use the PropertyValue pattern with ECRRO ontology property identifiers as top-level JSON keys.

### Properties

| Property | ECRRO ID | Vocabulary | Description |
|----------|----------|------------|-------------|
| Maturity state | `ecrro:ECRRO_0000138` | MTU_ | Current development/deployment status |
| Expected lifetime | `ecrro:ECRRO_0000219` | ELT_ | Anticipated longevity of the resource |
| Usage level | `ecrro:ECRRO_0000017` | UBA_ | Current adoption level |
| Stewardship | `ecrro:ECRRO_0000218` | (agent) | Maintainer(s) of the resource |
| Primary publication | `ecrro:ECRRO_0000600` | (string) | Citation of the primary publication |
| Registration metadata | `ecrro:ECRRO_0001301` | (StructuredValue) | Who registered the resource and when |

### Pattern

Each assessment property is a top-level key with an ECRRO URI. The value is a PropertyValue object whose `value` field contains a DefinedTerm (for vocabulary-controlled properties), an agent (for stewardship), or a string (for publications).

```json
{
  "ecrro:ECRRO_0000138": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000138",
    "schema:name": "has maturity state",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "In production",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MTU_0000002"
    }
  }
}
```

### Controlled Vocabularies

- **MTU (Maturity)**: Used in multiple places, In production, Alpha, Beta, Planning, etc.
- **ELT (Expected Lifetime)**: Long-term, >5 years, 1-5 years, Unknown, N/A
- **UBA (Usage)**: Wide (>50), Some (10-50), Low, Unknown, N/A

## Examples

### Pyleoclim Assessment Properties
ECRR assessment properties for the Pyleoclim software resource, including
maturity state, expected lifetime, usage level, stewardship contacts, and
registration metadata using ECRRO property identifiers.
#### json
```json
{
  "ecrro:ECRRO_0000138": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000138",
    "schema:name": "has maturity state",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "In production",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MTU_0000002"
    }
  },
  "ecrro:ECRRO_0000219": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000219",
    "schema:name": "expected lifetime",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
    }
  },
  "ecrro:ECRRO_0000017": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000017",
    "schema:name": "Usage",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "Some usage (10-50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000002"
    }
  },
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": [
      {
        "@type": "schema:Person",
        "schema:name": "Deborah Khider",
        "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
      },
      {
        "@type": "schema:Person",
        "schema:name": "Feng Zhu"
      }
    ]
  },
  "ecrro:ECRRO_0001301": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0001301",
    "schema:name": "registration metadata",
    "schema:value": {
      "@type": "schema:StructuredValue",
      "schema:additionalType": "ecrro:ECRRO_0000156",
      "schema:contributor": {
        "@type": "schema:Person",
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-03-02"
    }
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/context.jsonld"
  ],
  "ecrro:ECRRO_0000138": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000138",
    "schema:name": "has maturity state",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "In production",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MTU_0000002"
    }
  },
  "ecrro:ECRRO_0000219": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000219",
    "schema:name": "expected lifetime",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
    }
  },
  "ecrro:ECRRO_0000017": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000017",
    "schema:name": "Usage",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "Some usage (10-50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000002"
    }
  },
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": [
      {
        "@type": "schema:Person",
        "schema:name": "Deborah Khider",
        "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
      },
      {
        "@type": "schema:Person",
        "schema:name": "Feng Zhu"
      }
    ]
  },
  "ecrro:ECRRO_0001301": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0001301",
    "schema:name": "registration metadata",
    "schema:value": {
      "@type": "schema:StructuredValue",
      "schema:additionalType": "ecrro:ECRRO_0000156",
      "schema:contributor": {
        "@type": "schema:Person",
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-03-02"
    }
  }
}
```

#### ttl
```ttl
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

[] ecrro:ECRRO_0000017 [ a schema1:PropertyValue ;
            schema1:name "Usage" ;
            schema1:propertyID "ecrro:ECRRO_0000017" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/UBA_0000002" ;
                    schema1:name "Some usage (10-50 adopters)" ] ] ;
    ecrro:ECRRO_0000138 [ a schema1:PropertyValue ;
            schema1:name "has maturity state" ;
            schema1:propertyID "ecrro:ECRRO_0000138" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/MTU_0000002" ;
                    schema1:name "In production" ] ] ;
    ecrro:ECRRO_0000218 [ a schema1:PropertyValue ;
            schema1:name "Stewardship" ;
            schema1:propertyID "ecrro:ECRRO_0000218" ;
            schema1:value [ a schema1:Person ;
                    schema1:name "Feng Zhu" ],
                [ a schema1:Person ;
                    schema1:identifier "https://orcid.org/0000-0001-7501-8430" ;
                    schema1:name "Deborah Khider" ] ] ;
    ecrro:ECRRO_0000219 [ a schema1:PropertyValue ;
            schema1:name "expected lifetime" ;
            schema1:propertyID "ecrro:ECRRO_0000219" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000003" ;
                    schema1:name "1 - 5 years" ] ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Stephen M. Richard" ] ;
                    schema1:datePublished "2021-03-02" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Resource Assessment Properties
description: ECRR-specific properties for assessing resource maturity, expected lifetime,
  usage level, stewardship, primary publication, and registration metadata. These
  use the PropertyValue pattern with ECRRO property identifiers as top-level keys.
  The value field contains a DefinedTerm from a controlled vocabulary, an agent reference,
  or a string.
type: object
properties:
  ecrro:ECRRO_0000138:
    description: Maturity state of the resource. Value is a DefinedTerm from the MTU
      (Maturity) vocabulary (e.g. In production, Alpha, Planning).
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000138
      schema:name:
        type: string
        default: has maturity state
      schema:value:
        $ref: '#/$defs/DefinedTerm'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0000219:
    description: Expected lifetime of the resource. Value is a DefinedTerm from the
      ELT (Expected Lifetime) vocabulary (e.g. Long-term, >5 years, 1-5 years).
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000219
      schema:name:
        type: string
        default: expected lifetime
      schema:value:
        $ref: '#/$defs/DefinedTerm'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0000017:
    description: Current usage level of the resource. Value is a DefinedTerm from
      the UBA (Usage) vocabulary (e.g. Wide usage, Some usage, Low usage).
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000017
      schema:name:
        type: string
        default: Usage
      schema:value:
        $ref: '#/$defs/DefinedTerm'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0000218:
    description: Stewardship or maintainer of the resource. Value is an agent (Person
      or Organization) or array of agents responsible for maintenance.
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000218
      schema:name:
        type: string
        default: Stewardship
      schema:value:
        anyOf:
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
        - type: array
          items:
            anyOf:
            - $ref: '#/$defs/Person'
            - $ref: '#/$defs/Organization'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0000600:
    description: Primary publication about the resource. Value is a citation string.
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000600
      schema:name:
        type: string
        default: primary publication
      schema:value:
        type: string
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0001301:
    description: Registration metadata recording who registered the resource and when.
      Value is a StructuredValue with contributor (Person) and datePublished.
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0001301
      schema:name:
        type: string
        default: registration metadata
      schema:value:
        type: object
        properties:
          '@type':
            type: string
            const: schema:StructuredValue
            default: schema:StructuredValue
          schema:additionalType:
            type: string
            const: ecrro:ECRRO_0000156
          schema:contributor:
            anyOf:
            - $ref: '#/$defs/Person'
            - $ref: '#/$defs/Organization'
          schema:datePublished:
            type: string
        required:
        - '@type'
        - schema:contributor
        - schema:datePublished
    required:
    - '@type'
    - schema:propertyID
    - schema:value
$defs:
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  Person:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/context.jsonld)

## Sources

* [EarthCube Resource Registry Ontology](http://cor.esipfed.org/ont/earthcube/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrAssessment`

