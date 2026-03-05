
# ECRR Service Instance properties (Schema)

`ogc.ecrrProperties.ecrrService` *v0.1*

Schema defining properties specific to service instance resources in the EarthCube Resource Registry, including communication protocols, interface specifications, supporting data, and service invocation. Defines properties: ecrro:ECRRO_0000502, ecrro:ECRRO_0000503, schema:supportingData, schema:potentialAction. Uses building blocks: labeledLink (schemaorgProperties), definedTerm (schemaorgProperties), action (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Service Instance Properties

Defines properties specific to service instance resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:WebAPI"]`.

### Properties

- **ecrro:ECRRO_0000502** — communication protocols (PropertyValue wrapping DefinedTerm array from CMPR vocabulary)
- **ecrro:ECRRO_0000503** — interface specification (PropertyValue wrapping labeled links to specification documents)
- **schema:supportingData** — input/output data formats (DataFeed objects with position and encodingFormat)
- **schema:potentialAction** — service invocation details using the Action pattern

### Communication Protocols (CMPR vocabulary)

HTTP, HTTPS, TCP/IP, FTP, SSH, SFTP, SMTP, IMAP, POP3

### Interface Specification Pattern

```json
{
  "ecrro:ECRRO_0000503": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000503",
    "schema:name": "Interface specification",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "WADL endpoint",
      "schema:url": "https://example.com/services/wadl"
    }
  }
}
```

## Examples

### GMRT GridServer Service Properties
ECRR service properties for the GMRT GridServer, including interface
specification and output data formats.
#### json
```json
{
  "ecrro:ECRRO_0000503": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000503",
    "schema:name": "Interface specification",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "HTTP"
    }
  },
  "schema:supportingData": [
    {
      "@type": "schema:DataFeed",
      "schema:name": "Output Data Formats",
      "schema:position": "output",
      "schema:encodingFormat": [
        "application/x-netcdf",
        "image/tiff;type=GeoTIFF",
        "text/plain;type=ArcASCII"
      ]
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrService/context.jsonld"
  ],
  "ecrro:ECRRO_0000503": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000503",
    "schema:name": "Interface specification",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "HTTP"
    }
  },
  "schema:supportingData": [
    {
      "@type": "schema:DataFeed",
      "schema:name": "Output Data Formats",
      "schema:position": "output",
      "schema:encodingFormat": [
        "application/x-netcdf",
        "image/tiff;type=GeoTIFF",
        "text/plain;type=ArcASCII"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

[] ecrro:ECRRO_0000503 [ a schema1:PropertyValue ;
            schema1:name "Interface specification" ;
            schema1:propertyID "ecrro:ECRRO_0000503" ;
            schema1:value [ a schema1:CreativeWork ;
                    schema1:name "HTTP" ] ] ;
    schema1:supportingData [ a schema1:DataFeed ;
            schema1:encodingFormat "application/x-netcdf",
                "image/tiff;type=GeoTIFF",
                "text/plain;type=ArcASCII" ;
            schema1:name "Output Data Formats" ;
            schema1:position "output" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Service Instance Properties
description: Properties specific to service instance resources in ECRR. For resources
  typed ["schema:CreativeWork", "schema:WebAPI"]. Covers communication protocols,
  interface specifications, input/output data formats, and service invocation.
type: object
properties:
  ecrro:ECRRO_0000502:
    description: Communication protocols used by the service. PropertyValue wrapping
      an array of DefinedTerm objects from the CMPR (Communication Protocol) vocabulary
      (e.g. HTTP, HTTPS, TCP/IP, FTP).
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000502
      schema:name:
        type: string
        default: communication protocols
      schema:value:
        anyOf:
        - $ref: '#/$defs/DefinedTerm'
        - type: array
          items:
            $ref: '#/$defs/DefinedTerm'
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  ecrro:ECRRO_0000503:
    description: Interface specification that the service implements. PropertyValue
      wrapping an array of labeled links to specification documents (e.g. WADL, WSDL,
      OpenAPI, OGC service specification).
    type: object
    properties:
      '@type':
        type: string
        const: schema:PropertyValue
        default: schema:PropertyValue
      schema:propertyID:
        type: string
        const: ecrro:ECRRO_0000503
      schema:name:
        type: string
        default: Interface specification
      schema:value:
        anyOf:
        - $ref: '#/$defs/LabeledLink'
        - type: array
          items:
            $ref: '#/$defs/LabeledLink'
        - type: object
          description: Simple reference with identifier
          properties:
            '@type':
              type: string
            schema:identifier:
              type: string
    required:
    - '@type'
    - schema:propertyID
    - schema:value
  schema:supportingData:
    description: Input and output data format specifications for the service. Array
      of DataFeed objects with position (input/output) and encodingFormat.
    anyOf:
    - $ref: '#/$defs/DataFeedSpec'
    - type: array
      items:
        $ref: '#/$defs/DataFeedSpec'
  schema:potentialAction:
    description: Service invocation details. Uses the Action building block pattern
      to describe how to call the service endpoint.
    type: array
    items:
      $ref: '#/$defs/Action'
$defs:
  LabeledLink:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/labeledLink/schema.yaml
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/schema.yaml
  Action:
    $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/action/schema.yaml
  DataFeedSpec:
    type: object
    properties:
      '@type':
        type: string
        const: schema:DataFeed
        default: schema:DataFeed
      schema:name:
        type: string
      schema:position:
        type: string
        enum:
        - input
        - output
      schema:encodingFormat:
        type: array
        items:
          type: string
    required:
    - '@type'
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrService/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrService/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/ecrrProperties/ecrrService/context.jsonld)

## Sources

* [schema.org WebAPI](https://schema.org/WebAPI)
* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrService`

