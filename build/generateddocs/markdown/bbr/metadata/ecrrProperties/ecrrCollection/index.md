
# ECRR Collection/Bundled Object properties (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrCollection` *v0.1*

Schema defining properties specific to bundled object (collection) resources in the EarthCube Resource Registry, including component resource listings. Defines properties: schema:hasPart.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Collection/Bundled Object Properties

Defines properties specific to bundled object (collection) resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:Product"]` with `mainEntity` pointing to `ECRRO_0000213` (Bundled Object).

A bundled object groups multiple related resources together, such as a software package with its documentation, test data, and dependencies.

### Properties

- **schema:hasPart** — component resources in the collection (array of objects with @type, name, url, description, encodingFormat)

### Example

```json
{
  "schema:hasPart": [
    {
      "@type": "schema:SoftwareApplication",
      "schema:name": "Analysis Tool",
      "schema:url": "https://example.org/tool",
      "schema:description": "Main analysis software"
    },
    {
      "@type": "schema:Dataset",
      "schema:name": "Sample Data",
      "schema:url": "https://example.org/data",
      "schema:encodingFormat": ["text/csv"]
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "User Guide",
      "schema:url": "https://example.org/docs"
    }
  ]
}
```

## Examples

### ECRR Bundled Object (synthetic)
Synthetic example of an ECRR bundled object (collection) with constituent
parts including software, dataset, and documentation components.
#### json
```json
{
  "schema:hasPart": [
    {
      "@type": "schema:SoftwareApplication",
      "schema:name": "Analysis Tool v2.0",
      "schema:url": "https://example.org/analysis-tool",
      "schema:description": "Main analysis software component"
    },
    {
      "@type": "schema:Dataset",
      "schema:name": "Sample Observation Data",
      "schema:url": "https://example.org/sample-data",
      "schema:encodingFormat": ["text/csv", "application/json"]
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "User Documentation",
      "schema:url": "https://example.org/docs",
      "schema:encodingFormat": ["text/html"]
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCollection/context.jsonld"
  ],
  "schema:hasPart": [
    {
      "@type": "schema:SoftwareApplication",
      "schema:name": "Analysis Tool v2.0",
      "schema:url": "https://example.org/analysis-tool",
      "schema:description": "Main analysis software component"
    },
    {
      "@type": "schema:Dataset",
      "schema:name": "Sample Observation Data",
      "schema:url": "https://example.org/sample-data",
      "schema:encodingFormat": [
        "text/csv",
        "application/json"
      ]
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "User Documentation",
      "schema:url": "https://example.org/docs",
      "schema:encodingFormat": [
        "text/html"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:hasPart [ a schema1:CreativeWork ;
            schema1:encodingFormat "text/html" ;
            schema1:name "User Documentation" ;
            schema1:url "https://example.org/docs" ],
        [ a schema1:Dataset ;
            schema1:encodingFormat "application/json",
                "text/csv" ;
            schema1:name "Sample Observation Data" ;
            schema1:url "https://example.org/sample-data" ],
        [ a schema1:SoftwareApplication ;
            schema1:description "Main analysis software component" ;
            schema1:name "Analysis Tool v2.0" ;
            schema1:url "https://example.org/analysis-tool" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Collection/Bundled Object Properties
description: Properties specific to bundled object (collection) resources in ECRR.
  For resources typed ["schema:CreativeWork", "schema:Product"]. A bundled object
  groups multiple related resources together.
type: object
properties:
  schema:hasPart:
    description: Component resources that are part of this collection/bundle. Array
      of objects identifying each component with its type, name, URL, and optional
      encoding format.
    type: array
    items:
      type: object
      properties:
        '@type':
          description: Schema.org type of the component resource (e.g. schema:SoftwareApplication,
            schema:Dataset, schema:CreativeWork).
          anyOf:
          - type: string
          - type: array
            items:
              type: string
        schema:name:
          type: string
          description: Name of the component resource.
        schema:url:
          type: string
          format: uri
          description: URL where the component can be accessed.
        schema:description:
          type: string
          description: Brief description of the component.
        schema:encodingFormat:
          description: Format(s) of the component resource.
          type: array
          items:
            type: string
      required:
      - schema:name
    minItems: 1
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCollection/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCollection/context.jsonld)

## Sources

* [schema.org Product](https://schema.org/Product)
* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrCollection`

