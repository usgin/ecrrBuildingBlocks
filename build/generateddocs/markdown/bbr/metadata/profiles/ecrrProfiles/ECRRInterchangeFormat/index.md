
# ECRR Interchange Format profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRInterchangeFormat` *v0.1*

Complete ECRR metadata profile for interchange format resources, composing base, common, and assessment building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Interchange Format Profile

Complete metadata profile for registering interchange format resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Interchange Format"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000208` (Interchange Format)

## Examples

### ECRR Interchange Format (synthetic example)
Example metadata instance for ECRRInterchangeFormat profile.
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
  "@id": "http://n2t.net/ark:/23942/g2example-interchange",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "NetCDF (Network Common Data Form)",
  "schema:additionalType": [
    "EC Interchange Format"
  ],
  "schema:description": "NetCDF is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is widely used in atmospheric and ocean sciences for gridded data interchange.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208",
    "schema:name": "Interchange Format"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": {
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat"
      }
    ],
    "schema:sdDatePublished": "2026-03-03"
  },
  "schema:creator": [
    {
      "@type": "schema:Organization",
      "schema:name": "Unidata/UCAR"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Atmospheric Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000030"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Oceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000039"
    }
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
      "schema:datePublished": "2024-07-20"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2example-interchange",
  "@type": [
    "schema:CreativeWork",
    "schema:Product"
  ],
  "schema:name": "NetCDF (Network Common Data Form)",
  "schema:additionalType": [
    "EC Interchange Format"
  ],
  "schema:description": "NetCDF is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is widely used in atmospheric and ocean sciences for gridded data interchange.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208",
    "schema:name": "Interchange Format"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Public"
    }
  ],
  "schema:subjectOf": {
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat"
      }
    ],
    "schema:sdDatePublished": "2026-03-03"
  },
  "schema:creator": [
    {
      "@type": "schema:Organization",
      "schema:name": "Unidata/UCAR"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Atmospheric Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000030"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Oceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000039"
    }
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
      "schema:datePublished": "2024-07-20"
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g2example-interchange> a schema1:CreativeWork,
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
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000001" ;
                    schema1:name "Long-term" ] ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Example Registrant" ] ;
                    schema1:datePublished "2024-07-20" ] ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000030" ;
            schema1:name "Atmospheric Science" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000039" ;
            schema1:name "Oceanography" ] ;
    schema1:additionalType "EC Interchange Format" ;
    schema1:creator [ a schema1:Organization ;
            schema1:name "Unidata/UCAR" ] ;
    schema1:description "NetCDF is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is widely used in atmospheric and ocean sciences for gridded data interchange." ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Public" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Interchange Format" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000208" ] ;
    schema1:name "NetCDF (Network Common Data Form)" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
                <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat>,
                <https://w3id.org/cdif/core/1.0/>,
                <https://w3id.org/cdif/discovery/1.0/> ;
            schema1:additionalType "dcat:CatalogRecord" ;
            schema1:sdDatePublished "2026-03-03" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Interchange Format Profile
description: Complete ECRR metadata profile for interchange format resources. Composes
  ecrrBase, ecrrCommon, and ecrrAssessment. Resources must have schema:additionalType
  containing "EC Interchange Format".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Interchange Format
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRInterchangeFormat/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRInterchangeFormat`

