
# ECRR Specification profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRSpecification` *v0.1*

Complete ECRR metadata profile for specification resources, composing base, common, assessment, and specification-specific building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Specification Profile

Complete metadata profile for registering specification resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties
3. **ecrrAssessment** — resource assessment properties
4. **ecrrSpecification** — specification-specific (parent specifications, subtype via SPKT vocabulary)

### Type Requirements

- `@type` must include `schema:CreativeWork` (and typically `schema:Product`)
- `mainEntity` must include reference to `http://cor.esipfed.org/ont/earthcube/ECRRO_0000204` (Specification)
- Additional `mainEntity` entries may specify subtype from the SPKT vocabulary (Data Format Convention, Data Model, etc.)

## Examples

### INSPIRE Data Specification on Geology - Complete ECRR Record
Example metadata instance for ECRRSpecification profile.
#### json
```json
{
  "@context": [
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2800001",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "INSPIRE Data Specification on Geology",
  "schema:additionalType": [
    "EC Specification"
  ],
  "schema:identifier": "http://inspire.ec.europa.eu/tg/ge/3.0",
  "schema:description": "Geology is a reference data theme that provides information for several themes of INSPIRE Annex III: Mineral resources, Natural Risk Zones, Soil, Energy resources, and it has a specific relationship with one of the most important natural resources, water, through groundwater bodies contained in aquifers. Scope is Geologic and Geophysical data interchange format.",
  "schema:mainEntity": [
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000204",
      "schema:name": "Specification"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Data Format Conventions",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208"
    }
  ],
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "INSPIRE specification document",
      "schema:url": "https://inspire.ec.europa.eu/file/1519/download?token=IGCGbum3"
    },
    {
      "@type": [
        "schema:CreativeWork"
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
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:name": "European Commission"
      }
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Data Facilities and Repositories",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000003"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000056"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Based on: GeoSciML version 3.2",
      "schema:url": "http://geosciml.org/doc/geosciml/3.2/documentation/"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Legal basis: Directive 2007/2/EC of the European Parliament",
      "schema:url": "http://data.europa.eu/eli/dir/2007/2/oj"
    }
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
  },
  "dct:bibliographicCitation": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0"
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
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
    }
  },
  "ecrro:ECRRO_0000600": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000600",
    "schema:name": "primary publication",
    "schema:value": "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0"
  },
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": {
      "@type": "schema:Organization",
      "schema:name": "European Commission Joint Research Centre"
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
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-02-10"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2800001",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "INSPIRE Data Specification on Geology",
  "schema:additionalType": [
    "EC Specification"
  ],
  "schema:identifier": "http://inspire.ec.europa.eu/tg/ge/3.0",
  "schema:description": "Geology is a reference data theme that provides information for several themes of INSPIRE Annex III: Mineral resources, Natural Risk Zones, Soil, Energy resources, and it has a specific relationship with one of the most important natural resources, water, through groundwater bodies contained in aquifers. Scope is Geologic and Geophysical data interchange format.",
  "schema:mainEntity": [
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000204",
      "schema:name": "Specification"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Data Format Conventions",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208"
    }
  ],
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "INSPIRE specification document",
      "schema:url": "https://inspire.ec.europa.eu/file/1519/download?token=IGCGbum3"
    },
    {
      "@type": [
        "schema:CreativeWork"
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
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:name": "European Commission"
      }
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Data Facilities and Repositories",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000003"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000056"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Based on: GeoSciML version 3.2",
      "schema:url": "http://geosciml.org/doc/geosciml/3.2/documentation/"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Legal basis: Directive 2007/2/EC of the European Parliament",
      "schema:url": "http://data.europa.eu/eli/dir/2007/2/oj"
    }
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
  },
  "dct:bibliographicCitation": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0"
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
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
    }
  },
  "ecrro:ECRRO_0000600": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000600",
    "schema:name": "primary publication",
    "schema:value": "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0"
  },
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": {
      "@type": "schema:Organization",
      "schema:name": "European Commission Joint Research Centre"
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
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-02-10"
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g2800001> a schema1:CreativeWork,
        schema1:Product ;
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
    ecrro:ECRRO_0000218 [ a schema1:PropertyValue ;
            schema1:name "Stewardship" ;
            schema1:propertyID "ecrro:ECRRO_0000218" ;
            schema1:value [ a schema1:Organization ;
                    schema1:name "European Commission Joint Research Centre" ] ] ;
    ecrro:ECRRO_0000219 [ a schema1:PropertyValue ;
            schema1:name "expected lifetime" ;
            schema1:propertyID "ecrro:ECRRO_0000219" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000003" ;
                    schema1:name "1 - 5 years" ] ] ;
    ecrro:ECRRO_0000501 [ a schema1:PropertyValue ;
            schema1:name "profile of" ;
            schema1:propertyID "ecrro:ECRRO_0000501" ;
            schema1:value [ a schema1:CreativeWork ;
                    schema1:name "GeoSciML version 3.2" ;
                    schema1:url "http://geosciml.org/doc/geosciml/3.2/documentation/" ] ] ;
    ecrro:ECRRO_0000600 [ a schema1:PropertyValue ;
            schema1:name "primary publication" ;
            schema1:propertyID "ecrro:ECRRO_0000600" ;
            schema1:value "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0" ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Stephen M. Richard" ] ;
                    schema1:datePublished "2021-02-10" ] ] ;
    dct:bibliographicCitation [ a schema1:PropertyValue ;
            schema1:name "Bibliographic citation" ;
            schema1:propertyID "dct:bibliographicCitation" ;
            schema1:value "INSPIRE Thematic Working Group Geology, 2013-12-10, D2.8.II.4 INSPIRE Data Specification on Geology - Technical Guidelines: European Commission Joint Research Centre D2.8.II.4_v3.0" ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000056" ;
            schema1:name "Geology" ] ;
    schema1:additionalType "EC Specification" ;
    schema1:audience [ a schema1:Audience ;
            schema1:audienceType "Data Facilities and Repositories" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000003" ] ;
    schema1:description "Geology is a reference data theme that provides information for several themes of INSPIRE Annex III: Mineral resources, Natural Risk Zones, Soil, Energy resources, and it has a specific relationship with one of the most important natural resources, water, through groundwater bodies contained in aquifers. Scope is Geologic and Geophysical data interchange format." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:name "European Commission" ] ] ;
    schema1:identifier "http://inspire.ec.europa.eu/tg/ge/3.0" ;
    schema1:isRelatedTo [ a schema1:CreativeWork ;
            schema1:name "Legal basis: Directive 2007/2/EC of the European Parliament" ;
            schema1:url "http://data.europa.eu/eli/dir/2007/2/oj" ],
        [ a schema1:CreativeWork ;
            schema1:name "Based on: GeoSciML version 3.2" ;
            schema1:url "http://geosciml.org/doc/geosciml/3.2/documentation/" ] ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Public" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Data Format Conventions" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208" ],
        [ a schema1:CreativeWork ;
            schema1:name "Specification" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000204" ] ;
    schema1:name "INSPIRE Data Specification on Geology" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            schema1:name "INSPIRE specification document" ;
            schema1:url "https://inspire.ec.europa.eu/file/1519/download?token=IGCGbum3" ],
        [ a schema1:CreativeWork ;
            dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
                <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification>,
                <https://w3id.org/cdif/core/1.0/>,
                <https://w3id.org/cdif/discovery/1.0/> ;
            schema1:additionalType "dcat:CatalogRecord" ;
            schema1:sdDatePublished "2026-03-03" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Specification Profile
description: Complete ECRR metadata profile for specification resources. Composes
  ecrrBase, ecrrCommon, ecrrAssessment, and ecrrSpecification. Resources must have
  schema:additionalType containing "EC Specification".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSpecification/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Specification
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSpecification/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRSpecification`

