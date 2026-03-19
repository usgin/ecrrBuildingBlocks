
# ECRR Dataset profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRDataset` *v0.1*

Complete ECRR metadata profile for dataset resources, extending CDIFcomplete with base, common, and assessment building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Dataset Profile

Complete metadata profile for registering dataset resources in the EarthCube Resource Registry.

### Composition

This profile extends CDIFcomplete with ECRR building blocks. CDIF properties take precedence for overlapping concerns; ECRR-unique properties are included inline.

1. **CDIFcomplete** — full CDIF discovery + data description profile (creator, keywords, subjectOf, distribution, spatial/temporal coverage, variables, provenance, quality)
2. **ecrrCore** — mandatory ECRR identity: mainEntity classification, `@type` must contain `schema:CreativeWork`, requires `schema:description` and `schema:license`
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **Inline ECRR-unique properties** — properties from ecrrCommon not covered by CDIF (see below)

### ECRR-Unique Properties (not in CDIF)

- `schema:about` — science domains (ECRR ADO vocabulary)
- `schema:audience` — target user communities (ECRR AUT vocabulary)
- `schema:editor` — editors
- `schema:alternateName` — alternative names
- `dct:bibliographicCitation` — preferred citation

### Property Mappings: ECRR → CDIF

| ECRR property | CDIF equivalent | Notes |
|---|---|---|
| `schema:subjectOf` (other metadata) | `schema:relatedLink` with linkRelationship `"OtherMetadataFormat"` | CDIF reserves `schema:subjectOf` for CdifCatalogRecord |
| `schema:isRelatedTo` | `schema:relatedLink` | CDIF uses relatedLink with linkRelationship for typed relations |
| `schema:isBasedOn` | `prov:wasDerivedFrom` | CDIF uses PROV-O for derivation lineage |
| `schema:includedInDataCatalog` | `schema:subjectOf` → CdifCatalogRecord `schema:includedInDataCatalog` | Handled within the CdifCatalogRecord node |
| `schema:encodingFormat` | `schema:distribution` → DataDownload `schema:encodingFormat` | Property of distribution, not the dataset |
| `dct:conformsTo` | `schema:distribution` → DataDownload `dcterms:conformsTo` | Property of distribution or Action result |

### Type Requirements

- `@type` must include `schema:Dataset` and `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Dataset"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000214` (Dataset)

### Overlapping Properties (CDIF takes precedence)

The following properties are defined by both ecrrCommon and CDIF. In this profile, the CDIF definitions are used:

| Property | CDIF source | Notes |
|---|---|---|
| `schema:creator` | cdifOptional (`@list` wrapper) | ECRR used plain array; CDIF preserves author order |
| `schema:keywords` | cdifOptional (array of DefinedTerm/string) | ECRR allowed bare string; CDIF requires array |
| `schema:subjectOf` | cdifCore (CdifCatalogRecord) | ECRR usage → `schema:relatedLink` instead |
| `schema:identifier` | cdifCore (required) | |
| `schema:distribution` | CDIFcomplete (DataDownload/WebAPI/archive) | |
| `schema:contributor` | cdifOptional (with agentInRole support) | |
| `schema:publisher` | cdifOptional | |
| `schema:funding` | cdifOptional | |
| `schema:sameAs` | cdifOptional (Identifier or string) | |
| `schema:version` | cdifOptional | |
| `schema:datePublished` | cdifOptional | |
| `schema:url` | cdifCore | |

## Examples

### ECRR Dataset (synthetic example)
Example metadata instance for ECRRDataset profile.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "http://n2t.net/ark:/23942/g2example-dataset",
  "@type": [
    "schema:CreativeWork",
    "schema:Dataset"
  ],
  "schema:name": "Global Surface Temperature Anomalies",
  "schema:additionalType": [
    "EC Dataset"
  ],
  "schema:description": "Monthly global surface temperature anomaly data relative to the 1951-1980 base period, derived from meteorological station and ocean observations.",
  "schema:identifier": "http://n2t.net/ark:/23942/g2example-dataset",
  "schema:url": "https://example.org/data/global-surface-temperature-anomalies",
  "schema:dateModified": "2026-03-03",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000214",
    "schema:name": "Dataset"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:ecrr-dataset-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRDataset"
      }
    ],
    "schema:sdDatePublished": "2026-03-03",
    "schema:about": {
      "@id": "http://n2t.net/ark:/23942/g2example-dataset"
    }
  },
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "Example Climate Institute"
      }
    ]
  },
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "https://example.org/data/temperature-anomalies.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:name": "Temperature anomaly CSV download"
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
    "1880-01-01/2023-12-31"
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "EarthCube Data Catalog",
    "schema:url": "https://www.earthcube.org/datasets"
  },
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
      "schema:name": "Long-term",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000001"
    }
  },
  "ecrro:ECRRO_0000017": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000017",
    "schema:name": "Usage",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "Wide usage (>50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000001"
    }
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
        "schema:name": "Example Registrant"
      },
      "schema:datePublished": "2024-01-15"
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
      "dcterms": "http://purl.org/dc/terms/",
      "ecrro": "http://cor.esipfed.org/ont/earthcube/"
    },
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRDataset/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2example-dataset",
  "@type": [
    "schema:CreativeWork",
    "schema:Dataset"
  ],
  "schema:name": "Global Surface Temperature Anomalies",
  "schema:additionalType": [
    "EC Dataset"
  ],
  "schema:description": "Monthly global surface temperature anomaly data relative to the 1951-1980 base period, derived from meteorological station and ocean observations.",
  "schema:identifier": "http://n2t.net/ark:/23942/g2example-dataset",
  "schema:url": "https://example.org/data/global-surface-temperature-anomalies",
  "schema:dateModified": "2026-03-03",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000214",
    "schema:name": "Dataset"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:ecrr-dataset-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRDataset"
      }
    ],
    "schema:sdDatePublished": "2026-03-03",
    "schema:about": {
      "@id": "http://n2t.net/ark:/23942/g2example-dataset"
    }
  },
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "Example Climate Institute"
      }
    ]
  },
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "https://example.org/data/temperature-anomalies.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:name": "Temperature anomaly CSV download"
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
    "1880-01-01/2023-12-31"
  ],
  "schema:includedInDataCatalog": {
    "@type": "schema:DataCatalog",
    "schema:name": "EarthCube Data Catalog",
    "schema:url": "https://www.earthcube.org/datasets"
  },
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
      "schema:name": "Long-term",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000001"
    }
  },
  "ecrro:ECRRO_0000017": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000017",
    "schema:name": "Usage",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "Wide usage (>50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000001"
    }
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
        "schema:name": "Example Registrant"
      },
      "schema:datePublished": "2024-01-15"
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g2example-dataset> a schema1:CreativeWork,
        schema1:Dataset ;
    ecrro:ECRRO_0000017 [ a schema1:PropertyValue ;
            schema1:name "Usage" ;
            schema1:propertyID "ecrro:ECRRO_0000017" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/UBA_0000001" ;
                    schema1:name "Wide usage (>50 adopters)" ] ] ;
    ecrro:ECRRO_0000138 [ a schema1:PropertyValue ;
            schema1:name "has maturity state" ;
            schema1:propertyID "ecrro:ECRRO_0000138" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/MTU_0000002" ;
                    schema1:name "In production" ] ] ;
    ecrro:ECRRO_0000219 [ a schema1:PropertyValue ;
            schema1:name "expected lifetime" ;
            schema1:propertyID "ecrro:ECRRO_0000219" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000001" ;
                    schema1:name "Long-term" ] ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Example Registrant" ] ;
                    schema1:datePublished "2024-01-15" ] ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000035" ;
            schema1:name "Climatology" ] ;
    schema1:additionalType "EC Dataset" ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "Example Climate Institute" ] ) ;
    schema1:dateModified "2026-03-03" ;
    schema1:description "Monthly global surface temperature anomaly data relative to the 1951-1980 base period, derived from meteorological station and ocean observations." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/temperature-anomalies.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Temperature anomaly CSV download" ] ;
    schema1:identifier "http://n2t.net/ark:/23942/g2example-dataset" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "EarthCube Data Catalog" ;
            schema1:url "https://www.earthcube.org/datasets" ] ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Dataset" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000214" ] ;
    schema1:name "Global Surface Temperature Anomalies" ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "-90 -180 90 180" ] ;
            schema1:name "Global" ] ;
    schema1:subjectOf <urn:uuid:ecrr-dataset-catalog-record> ;
    schema1:temporalCoverage "1880-01-01/2023-12-31" ;
    schema1:url "https://example.org/data/global-surface-temperature-anomalies" .

<urn:uuid:ecrr-dataset-catalog-record> a schema1:Dataset ;
    dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
        <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRDataset>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <http://n2t.net/ark:/23942/g2example-dataset> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2026-03-03" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Dataset Profile
description: Complete ECRR metadata profile for dataset resources. Extends CDIFcomplete
  with ecrrCore (mainEntity, @type contains CreativeWork, requires description and
  license) and ecrrAssessment (maturity, lifetime, usage, stewardship). CDIF properties
  take precedence for overlapping concerns (creator, keywords, subjectOf, distribution,
  etc.). ECRR-unique properties from ecrrCommon are included inline. ECRR subjectOf
  usage (links to other metadata formats) maps to schema:relatedLink with linkRelationship
  "OtherMetadataFormat" per CDIF convention. Resources must have schema:additionalType
  containing "EC Dataset".
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCore/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Dataset
    schema:alternateName:
      description: Alternative names by which the resource is known.
      anyOf:
      - type: string
      - type: array
        items:
          type: string
    schema:editor:
      description: Editors of the resource.
      type: array
      items:
        anyOf:
        - type: object
          properties:
            '@id':
              type: string
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
    schema:about:
      description: Science domains that the resource addresses. Array of DefinedTerm
        objects referencing the ECRR ADO (Academic Discipline Ontology) vocabulary.
      type: array
      items:
        $ref: '#/$defs/DefinedTerm'
    schema:audience:
      description: Target user communities for the resource. Array of Audience objects
        with audienceType labels and identifiers from the AUT vocabulary.
      type: array
      items:
        type: object
        properties:
          '@type':
            type: string
            const: schema:Audience
            default: schema:Audience
          schema:audienceType:
            type: string
            description: Label for the target audience (e.g. Data Producers, Scientists,
              Developers). Values from ECRR AUT vocabulary.
          schema:identifier:
            type: string
            description: URI from the ECRR AUT_ vocabulary.
        required:
        - '@type'
        - schema:audienceType
    dct:bibliographicCitation:
      description: Preferred bibliographic citation for the resource, encoded as a
        PropertyValue with propertyID of dct:bibliographicCitation.
      type: object
      properties:
        '@type':
          type: string
          const: schema:PropertyValue
          default: schema:PropertyValue
        schema:propertyID:
          type: string
          const: dct:bibliographicCitation
        schema:name:
          type: string
          default: Bibliographic citation
        schema:value:
          type: string
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
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "ada": "https://ada.astromat.org/metadata/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRDataset/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)
* [schema.org Dataset](https://schema.org/Dataset)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRDataset`

