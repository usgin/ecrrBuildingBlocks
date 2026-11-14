
# ECRR Software properties (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrSoftware` *v0.1*

Schema defining properties specific to software and application resources in the EarthCube Resource Registry, including function categories, runtime platforms, programming languages, supporting data, code repositories, and dependencies. Defines properties: schema:applicationCategory, schema:runtimePlatform, schema:programmingLanguage, schema:supportingData, schema:codeRepository, schema:installURL, schema:potentialAction, dependencies. Uses building blocks: labeledLink (schemaorgProperties), action (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Software-Specific Properties

Defines properties specific to software and application resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:SoftwareApplication"]`.

### Properties

- **schema:applicationCategory** — function categories from the SFO vocabulary (e.g. Data Analysis, Visualization, Data Processing)
- **schema:runtimePlatform** — runtime environments from the RTE vocabulary (e.g. Linux, Browser, HPC, Android)
- **schema:programmingLanguage** — implementation languages (string or ComputerLanguage objects)
- **schema:supportingData** — input/output data format specifications as DataFeed objects with position and encodingFormat
- **schema:codeRepository** — source code repository URLs or labeled links
- **schema:installURL** — software installation locations (e.g. PyPI, CRAN, npm)
- **schema:potentialAction** — web application invocation using the Action pattern
- **dependencies** — software dependencies as PropertyValue wrapping labeled links

### Data Feed Specification Pattern

The `supportingData` property describes input and output data formats:

```json
{
  "@type": "schema:DataFeed",
  "schema:name": "Input Data Type specification",
  "schema:position": "input",
  "schema:encodingFormat": ["application/json", "text/csv"]
}
```

### Dependencies Pattern

Dependencies use PropertyValue with the OBO Relations Ontology "depends on" property:

```json
{
  "@type": "schema:PropertyValue",
  "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
  "schema:name": "dependencies",
  "schema:value": {
    "@type": "schema:CreativeWork",
    "schema:name": "Python 3.8"
  }
}
```

## Examples

### Pyleoclim Software Properties
ECRR software-specific properties for Pyleoclim, including application
categories, runtime platform, programming language, code repository,
install URL, supporting data formats, and dependencies.
#### json
```json
{
  "schema:applicationCategory": [
    "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
    "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
    "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
    "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
    "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011"
  ],
  "schema:runtimePlatform": [
    "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005"
  ],
  "schema:programmingLanguage": "Python 3.8",
  "schema:codeRepository": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Pyleoclim GitHub repository",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "schema:installURL": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "PyPI",
    "schema:url": "https://pypi.org/project/pyleoclim/"
  },
  "schema:supportingData": {
    "@type": [
      "schema:DataFeed"
    ],
    "schema:name": "Input Data Type specification",
    "schema:position": "input",
    "schema:encodingFormat": [
      "application/zip;type=LiPD",
      "application/json;type=pyleoclim",
      "text/csv;application=pyleoclim"
    ]
  },
  "dependencies": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
    "schema:name": "dependencies",
    "schema:value": {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Python 3.8",
      "schema:url": "https://www.python.org/"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSoftware/context.jsonld"
  ],
  "schema:applicationCategory": [
    "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
    "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
    "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
    "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
    "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011"
  ],
  "schema:runtimePlatform": [
    "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005"
  ],
  "schema:programmingLanguage": "Python 3.8",
  "schema:codeRepository": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Pyleoclim GitHub repository",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "schema:installURL": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "PyPI",
    "schema:url": "https://pypi.org/project/pyleoclim/"
  },
  "schema:supportingData": {
    "@type": [
      "schema:DataFeed"
    ],
    "schema:name": "Input Data Type specification",
    "schema:position": "input",
    "schema:encodingFormat": [
      "application/zip;type=LiPD",
      "application/json;type=pyleoclim",
      "text/csv;application=pyleoclim"
    ]
  },
  "dependencies": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
    "schema:name": "dependencies",
    "schema:value": {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Python 3.8",
      "schema:url": "https://www.python.org/"
    }
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:applicationCategory "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
        "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
        "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
        "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
        "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011" ;
    schema1:codeRepository [ a schema1:CreativeWork ;
            schema1:name "Pyleoclim GitHub repository" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util" ] ;
    schema1:installURL [ a schema1:CreativeWork ;
            schema1:name "PyPI" ;
            schema1:url "https://pypi.org/project/pyleoclim/" ] ;
    schema1:programmingLanguage "Python 3.8" ;
    schema1:runtimePlatform "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005" ;
    schema1:supportingData [ a schema1:DataFeed ;
            schema1:encodingFormat "application/json;type=pyleoclim",
                "application/zip;type=LiPD",
                "text/csv;application=pyleoclim" ;
            schema1:name "Input Data Type specification" ;
            schema1:position "input" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Software-Specific Properties
description: Properties specific to software and application resources in ECRR. For
  resources typed ["schema:CreativeWork", "schema:SoftwareApplication"]. Covers function
  categories, runtime environments, programming languages, input/output data formats,
  code repositories, installation, invocation, and dependencies.
type: object
properties:
  schema:applicationCategory:
    description: Function categories describing what the software does. Array of strings
      combining function label and URI from the ECRR SFO (Software Function Ontology)
      vocabulary.
    type: array
    items:
      type: string
    x-jsonld-id: http://schema.org/applicationCategory
  schema:runtimePlatform:
    description: Runtime environments on which the software operates. Array of strings
      referencing the ECRR RTE (Runtime Environment) vocabulary (e.g. Linux, Browser,
      HPC).
    anyOf:
    - type: string
    - type: array
      items:
        type: string
    x-jsonld-id: http://schema.org/runtimePlatform
  schema:programmingLanguage:
    description: Programming languages used to implement the software. Can be a simple
      string or an array of ComputerLanguage objects with name and identifier.
    anyOf:
    - type: string
    - type: array
      items:
        anyOf:
        - type: string
        - type: object
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: schema:ComputerLanguage
              minItems: 1
              default:
              - schema:ComputerLanguage
            schema:name:
              type: string
              x-jsonld-id: http://schema.org/name
            schema:identifier:
              type: string
              x-jsonld-id: http://schema.org/identifier
          required:
          - schema:name
    x-jsonld-id: http://schema.org/programmingLanguage
  schema:supportingData:
    description: Input and output data format specifications. Array of DataFeed objects
      with position (input/output) and encodingFormat indicating supported data formats.
    anyOf:
    - $ref: '#/$defs/DataFeedSpec'
    - type: array
      items:
        $ref: '#/$defs/DataFeedSpec'
    x-jsonld-id: http://schema.org/supportingData
  schema:codeRepository:
    description: Source code repositories for the software. Array of labeled links
      (CreativeWork objects with name and url) or simple URL strings.
    anyOf:
    - type: string
      format: uri
    - $ref: '#/$defs/LabeledLink'
    - type: array
      items:
        anyOf:
        - type: string
          format: uri
        - $ref: '#/$defs/LabeledLink'
    x-jsonld-id: http://schema.org/codeRepository
  schema:installURL:
    description: Locations where the software can be installed from (e.g. PyPI, CRAN,
      npm). Array of labeled links or URL strings.
    anyOf:
    - type: string
      format: uri
    - $ref: '#/$defs/LabeledLink'
    - type: array
      items:
        anyOf:
        - type: string
          format: uri
        - $ref: '#/$defs/LabeledLink'
    x-jsonld-id: http://schema.org/installURL
  schema:potentialAction:
    description: Web application invocation details for software accessible via a
      web interface. Uses the Action building block pattern.
    type: array
    items:
      $ref: '#/$defs/Action'
    x-jsonld-id: http://schema.org/potentialAction
  dependencies:
    description: Software dependencies encoded as a PropertyValue wrapping an array
      of labeled links. Uses propertyID http://purl.obolibrary.org/obo/RO_0002502
      (depends on).
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValue
        minItems: 1
        default:
        - schema:PropertyValue
      schema:propertyID:
        type: string
        const: http://purl.obolibrary.org/obo/RO_0002502
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        default: dependencies
        x-jsonld-id: http://schema.org/name
      schema:value:
        anyOf:
        - $ref: '#/$defs/LabeledLink'
        - type: array
          items:
            $ref: '#/$defs/LabeledLink'
        x-jsonld-id: http://schema.org/value
    required:
    - '@type'
    - schema:propertyID
$defs:
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  Action:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/action/schema.yaml
  DataFeedSpec:
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:DataFeed
        minItems: 1
        default:
        - schema:DataFeed
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:position:
        type: string
        description: Indicates whether this is an input or output data specification.
        enum:
        - input
        - output
        x-jsonld-id: http://schema.org/position
      schema:encodingFormat:
        anyOf:
        - type: string
        - type: array
          items:
            type: string
        x-jsonld-id: http://schema.org/encodingFormat
    required:
    - '@type'
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: ecrr.bbr.metadata.ecrrProperties.ecrrSoftware
  register: https://usgin.github.io/ecrrBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-14'

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSoftware/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSoftware/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdif": "https://w3id.org/cdif/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSoftware/context.jsonld)

## Sources

* [schema.org SoftwareApplication](https://schema.org/SoftwareApplication)
* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrSoftware`

