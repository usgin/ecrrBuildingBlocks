
# ECRR Catalog/Repository properties (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrCatalog` *v0.1*

Schema defining properties specific to catalog and repository resources in the EarthCube Resource Registry, including content type classification. Defines properties: schema:contentType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Catalog/Repository Properties

Defines properties specific to catalog and repository resources in the EarthCube Resource Registry. For resources with `mainEntity` pointing to `ECRRO_0000212` (Catalog/Registry) or `ECRRO_0000209` (Repository).

### Properties

- **schema:contentType** — types of objects cataloged or stored (array of Thing objects with name and identifier)

### Example

```json
{
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Rock magnetic data",
      "schema:identifier": "https://example.org/concept/rock-magnetic"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Paleomagnetic data"
    }
  ]
}
```

## Examples

### MagIC Data Repository Catalog Properties
ECRR catalog properties for the MagIC (Magnetics Information Consortium)
data repository.
#### json
```json
{
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Rock magnetic data"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Paleomagnetic data"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCatalog/context.jsonld"
  ],
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Rock magnetic data"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Paleomagnetic data"
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:contentType [ a schema1:Thing ;
            schema1:name "Rock magnetic data" ],
        [ a schema1:Thing ;
            schema1:name "Paleomagnetic data" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Catalog/Repository Properties
description: Properties specific to catalog and repository resources in ECRR. For
  resources with mainEntity pointing to ECRRO_0000212 (Catalog/Registry) or ECRRO_0000209
  (Repository).
type: object
properties:
  schema:contentType:
    description: Types of objects cataloged or stored in the repository. Array of
      Thing objects with name and optional identifier describing the content categories.
    type: array
    items:
      type: object
      properties:
        '@type':
          type: string
          default: schema:Thing
        schema:name:
          type: string
          description: Label for the type of cataloged content.
        schema:identifier:
          type: string
          description: URI identifying the content type concept.
      required:
      - schema:name
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCatalog/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCatalog/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCatalog/context.jsonld)

## Sources

* [schema.org DataCatalog](https://schema.org/DataCatalog)
* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrCatalog`

