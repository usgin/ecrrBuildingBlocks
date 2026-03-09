
# ECRR Service Instance profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRService` *v0.1*

Complete ECRR metadata profile for service instance resources, composing base, common, assessment, and service-specific building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Service Instance Profile

Complete metadata profile for registering service instance resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties
3. **ecrrAssessment** — resource assessment properties
4. **ecrrService** — service-specific (communication protocols, interface specification, supporting data, invocation)

### Type Requirements

- `@type` must include `schema:CreativeWork` (and typically `schema:WebAPI` or `schema:Product`)
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000202` (Service Instance)

## Examples

### GMRT GridServer Web Service - Complete ECRR Record
Example metadata instance for ECRRService profile.
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
  "@id": "http://n2t.net/ark:/23942/g2900003",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "Global Multi-resolution Topography (GMRT) GridServer Web Service",
  "schema:additionalType": [
    "EC Service Instance"
  ],
  "schema:description": "The GridServer service provides access to gridded data from the Global Multi-resolution Topography (GMRT) Synthesis. Requested data may be up to 2GB, or approximately 20 by 20 degrees at 100 meters per node (maximum available resolution). A variety of output formats are supported.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000202",
    "schema:name": "Service Instance"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GMRT GridServer info page",
      "schema:url": "https://www.gmrt.org/services/GridServer/info#!/services/getGMRTGrid"
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
          "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory"
        },
        {
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRService"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Marine Geology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000065"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GMRT synthesis publication",
      "schema:url": "http://dx.doi.org/10.1029/2008GC002332"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Machine-readable endpoint (WADL)",
      "schema:url": "https://www.gmrt.org/services/GridServer/wadl"
    }
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
      "schema:name": "Unknown",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000004"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRService/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2900003",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "Global Multi-resolution Topography (GMRT) GridServer Web Service",
  "schema:additionalType": [
    "EC Service Instance"
  ],
  "schema:description": "The GridServer service provides access to gridded data from the Global Multi-resolution Topography (GMRT) Synthesis. Requested data may be up to 2GB, or approximately 20 by 20 degrees at 100 meters per node (maximum available resolution). A variety of output formats are supported.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000202",
    "schema:name": "Service Instance"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GMRT GridServer info page",
      "schema:url": "https://www.gmrt.org/services/GridServer/info#!/services/getGMRTGrid"
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
          "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory"
        },
        {
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRService"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Marine Geology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000065"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GMRT synthesis publication",
      "schema:url": "http://dx.doi.org/10.1029/2008GC002332"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Machine-readable endpoint (WADL)",
      "schema:url": "https://www.gmrt.org/services/GridServer/wadl"
    }
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
      "schema:name": "Unknown",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000004"
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

<http://n2t.net/ark:/23942/g2900003> a schema1:CreativeWork,
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
    ecrro:ECRRO_0000219 [ a schema1:PropertyValue ;
            schema1:name "expected lifetime" ;
            schema1:propertyID "ecrro:ECRRO_0000219" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000004" ;
                    schema1:name "Unknown" ] ] ;
    ecrro:ECRRO_0000503 [ a schema1:PropertyValue ;
            schema1:name "Interface specification" ;
            schema1:propertyID "ecrro:ECRRO_0000503" ;
            schema1:value [ a schema1:CreativeWork ;
                    schema1:name "HTTP" ] ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Stephen M. Richard" ] ;
                    schema1:datePublished "2021-02-10" ] ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000065" ;
            schema1:name "Marine Geology" ] ;
    schema1:additionalType "EC Service Instance" ;
    schema1:audience [ a schema1:Audience ;
            schema1:audienceType "Developers" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000006" ],
        [ a schema1:Audience ;
            schema1:audienceType "Scientists" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000007" ] ;
    schema1:description "The GridServer service provides access to gridded data from the Global Multi-resolution Topography (GMRT) Synthesis. Requested data may be up to 2GB, or approximately 20 by 20 degrees at 100 meters per node (maximum available resolution). A variety of output formats are supported." ;
    schema1:isRelatedTo [ a schema1:CreativeWork ;
            schema1:name "GMRT synthesis publication" ;
            schema1:url "http://dx.doi.org/10.1029/2008GC002332" ],
        [ a schema1:CreativeWork ;
            schema1:name "Machine-readable endpoint (WADL)" ;
            schema1:url "https://www.gmrt.org/services/GridServer/wadl" ] ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Public" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Service Instance" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000202" ] ;
    schema1:name "Global Multi-resolution Topography (GMRT) GridServer Web Service" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory>,
                <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRService> ;
            schema1:additionalType "dcat:CatalogRecord" ;
            schema1:sdDatePublished "2026-03-03" ],
        [ a schema1:CreativeWork ;
            schema1:name "GMRT GridServer info page" ;
            schema1:url "https://www.gmrt.org/services/GridServer/info#!/services/getGMRTGrid" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Service Instance Profile
description: Complete ECRR metadata profile for service instance resources. Composes
  ecrrBase, ecrrCommon, ecrrAssessment, and ecrrService. Resources must have schema:additionalType
  containing "EC Service Instance".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrService/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Service Instance
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRService/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRService/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRService/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)
* [schema.org WebAPI](https://schema.org/WebAPI)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRService`

