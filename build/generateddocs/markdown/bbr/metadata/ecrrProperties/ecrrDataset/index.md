
# ECRR Dataset properties (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrDataset` *v0.1*

Schema defining properties specific to dataset resources in the EarthCube Resource Registry, referencing existing distribution, spatial/temporal extent, and variable building blocks. Defines properties: schema:distribution, schema:spatialCoverage, schema:temporalCoverage, schema:variableMeasured, schema:includedInDataCatalog. Uses building blocks: dataDownload (schemaorgProperties), webAPI (schemaorgProperties), spatialExtent (schemaorgProperties), temporalExtent (schemaorgProperties), variableMeasured (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Dataset-Specific Properties

Defines properties specific to dataset resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:Dataset"]`.

This building block heavily reuses existing schema.org building blocks.

### Properties

- **schema:distribution** — data access via DataDownload or WebAPI (reuses existing building blocks)
- **schema:spatialCoverage** — geographic extent (reuses spatialExtent building block)
- **schema:temporalCoverage** — time coverage (reuses temporalExtent building block)
- **schema:variableMeasured** — measured variables (reuses variableMeasured building block)
- **schema:includedInDataCatalog** — reference to containing catalog (DataCatalog with @id, name, url)

### Example

```json
{
  "schema:distribution": [
    {
      "@type": ["schema:DataDownload"],
      "schema:contentUrl": "https://example.org/data/download.csv",
      "schema:encodingFormat": ["text/csv"]
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "Example Data Catalog",
    "schema:url": "https://example.org/catalog"
  }
}
```

## Examples

### ECRR Dataset Properties (synthetic)
Synthetic example of ECRR dataset-specific properties.
#### json
```json
{
  "schema:distribution": [
    {
      "@type": ["schema:DataDownload"],
      "schema:contentUrl": "https://example.org/data/observations.csv",
      "schema:encodingFormat": ["text/csv"],
      "schema:name": "Observation data CSV download",
      "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:name": ["Global"],
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "-90 -180 90 180"
      }
    }
  ],
  "schema:temporalCoverage": ["2010-01-01/2023-12-31"],
  "schema:variableMeasured": [
    {
      "@type": ["schema:PropertyValue"],
      "schema:name": "Temperature",
      "schema:description": "Surface air temperature measurements"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "EarthCube Data Catalog",
    "schema:url": "https://www.earthcube.org/datasets"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrDataset/context.jsonld"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "https://example.org/data/observations.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:name": "Observation data CSV download",
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:name": [
        "Global"
      ],
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "-90 -180 90 180"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2010-01-01/2023-12-31"
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:name": "Temperature",
      "schema:description": "Surface air temperature measurements"
    }
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "EarthCube Data Catalog",
    "schema:url": "https://www.earthcube.org/datasets"
  }
}
```

#### ttl
```ttl
@prefix ns1: <dcterms:> .
@prefix schema1: <http://schema.org/> .

[] schema1:distribution [ a schema1:DataDownload ;
            ns1:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://example.org/data/observations.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Observation data CSV download" ] ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "EarthCube Data Catalog" ;
            schema1:url "https://www.earthcube.org/datasets" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "-90 -180 90 180" ] ;
            schema1:name "Global" ] ;
    schema1:temporalCoverage "2010-01-01/2023-12-31" ;
    schema1:variableMeasured [ a schema1:PropertyValue ;
            schema1:description "Surface air temperature measurements" ;
            schema1:name "Temperature" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Dataset-Specific Properties
description: Properties specific to dataset resources in ECRR. For resources typed
  ["schema:CreativeWork", "schema:Dataset"]. References existing building blocks for
  distribution, spatial/temporal coverage, and measured variables.
type: object
properties:
  schema:distribution:
    description: 'How to access the dataset: file downloads (DataDownload) or API
      access (WebAPI).'
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DataDownload'
      - $ref: '#/$defs/WebAPI'
  schema:spatialCoverage:
    description: Geographic area covered by the dataset.
    type: array
    items:
      $ref: '#/$defs/SpatialExtent'
  schema:temporalCoverage:
    description: Time period covered by the dataset. Can be ISO 8601 date ranges or
      structured temporal extent objects.
    type: array
    items:
      $ref: '#/$defs/TemporalExtent'
  schema:variableMeasured:
    description: What the dataset measures (e.g. temperature, pressure).
    type: array
    items:
      $ref: '#/$defs/VariableMeasured'
  schema:includedInDataCatalog:
    description: The data catalog that contains this dataset. Object with @id, name,
      and url identifying the containing catalog.
    anyOf:
    - $ref: '#/$defs/DataCatalogRef'
    - type: array
      items:
        $ref: '#/$defs/DataCatalogRef'
$defs:
  DataDownload:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  WebAPI:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/webAPI/schema.yaml
  SpatialExtent:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  VariableMeasured:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
  DataCatalogRef:
    type: object
    properties:
      '@id':
        type: string
      '@type':
        type: string
        const: schema:DataCatalog
        default: schema:DataCatalog
      schema:name:
        type: string
      schema:url:
        type: string
        format: uri
    required:
    - '@type'
    - schema:name
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrDataset/context.jsonld)

## Sources

* [schema.org Dataset](https://schema.org/Dataset)
* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrDataset`

