
# ECRR Catalog/Registry profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRCatalog` *v0.1*

Complete ECRR metadata profile for catalog and registry resources, composing base, common, assessment, and catalog-specific building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Catalog/Registry Profile

Complete metadata profile for registering catalog and repository resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrCatalog** — catalog-specific (content types)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC CatalogRegistry"` or `"EC Repository"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000212` (CatalogRegistry) or `http://cor.esipfed.org/ont/earthcube/ECRRO_0000209` (Repository)

## Examples

### ECRR Catalog (synthetic example)
Example metadata instance for ECRRCatalog profile.
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
  "@id": "http://n2t.net/ark:/23942/g2example-catalog",
  "@type": [
    "schema:CreativeWork",
    "schema:DataCatalog"
  ],
  "schema:name": "EarthCube GeoCodes Metadata Catalog",
  "schema:additionalType": [
    "EC CatalogRegistry"
  ],
  "schema:description": "A metadata catalog indexing geoscience datasets, tools, and services registered through the EarthCube GeoCodes system.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000212",
    "schema:name": "CatalogRegistry"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog"
      }
    ],
    "schema:sdDatePublished": "2026-03-03"
  },
  "schema:creator": [
    {
      "@type": "schema:Organization",
      "schema:name": "EarthCube"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Earth Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000021"
    }
  ],
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Datasets"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Software"
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
      "schema:datePublished": "2024-06-15"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2example-catalog",
  "@type": [
    "schema:CreativeWork",
    "schema:DataCatalog"
  ],
  "schema:name": "EarthCube GeoCodes Metadata Catalog",
  "schema:additionalType": [
    "EC CatalogRegistry"
  ],
  "schema:description": "A metadata catalog indexing geoscience datasets, tools, and services registered through the EarthCube GeoCodes system.",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000212",
    "schema:name": "CatalogRegistry"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog"
      }
    ],
    "schema:sdDatePublished": "2026-03-03"
  },
  "schema:creator": [
    {
      "@type": "schema:Organization",
      "schema:name": "EarthCube"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Earth Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000021"
    }
  ],
  "schema:contentType": [
    {
      "@type": "schema:Thing",
      "schema:name": "Datasets"
    },
    {
      "@type": "schema:Thing",
      "schema:name": "Software"
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
      "schema:datePublished": "2024-06-15"
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g2example-catalog> a schema1:CreativeWork,
        schema1:DataCatalog ;
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
                    schema1:datePublished "2024-06-15" ] ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000021" ;
            schema1:name "Earth Science" ] ;
    schema1:additionalType "EC CatalogRegistry" ;
    schema1:contentType [ a schema1:Thing ;
            schema1:name "Datasets" ],
        [ a schema1:Thing ;
            schema1:name "Software" ] ;
    schema1:creator [ a schema1:Organization ;
            schema1:name "EarthCube" ] ;
    schema1:description "A metadata catalog indexing geoscience datasets, tools, and services registered through the EarthCube GeoCodes system." ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "CatalogRegistry" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000212" ] ;
    schema1:name "EarthCube GeoCodes Metadata Catalog" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory>,
                <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog> ;
            schema1:additionalType "dcat:CatalogRecord" ;
            schema1:sdDatePublished "2026-03-03" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Catalog/Registry Profile
description: Complete ECRR metadata profile for catalog and registry resources. Composes
  ecrrBase, ecrrCommon, ecrrAssessment, and ecrrCatalog. Resources must have schema:additionalType
  containing "EC CatalogRegistry" or "EC Repository".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCatalog/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC CatalogRegistry
        - EC Repository
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCatalog/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRCatalog`

