
# ECRR Collection profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRCollection` *v0.1*

Complete ECRR metadata profile for bundled object (collection) resources, composing base, common, assessment, and collection-specific building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Collection Profile

Complete metadata profile for registering bundled object (collection) resources in the EarthCube Resource Registry.

### Composition

1. **ecrrBase** — mandatory identity and classification
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrCollection** — collection-specific (component parts with type, name, URL, description, encoding format)

### Type Requirements

- `@type` must include `schema:CreativeWork`
- `schema:additionalType` must contain `"EC Bundled Object"`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/SFO_0000075` (Bundled Object)

## Examples

### ECRR Collection (synthetic example)
Example metadata instance for ECRRCollection profile.
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
  "@id": "http://n2t.net/ark:/23942/g2example-collection",
  "@type": [
    "schema:CreativeWork",
    "schema:Product",
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Reference Standards Bundle",
  "schema:additionalType": [
    "EC Bundled Object"
  ],
  "schema:description": "A curated collection of geochemical reference standard datasets, software tools, and documentation for analytical laboratory calibration.",
  "schema:identifier": "http://n2t.net/ark:/23942/g2example-collection",
  "schema:url": "http://n2t.net/ark:/23942/g2example-collection",
  "schema:dateModified": "2026-03-03",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/SFO_0000075",
    "schema:name": "Bundled Object"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:ecrr-collection-catalog-record",
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCollection"
      }
    ],
    "schema:sdDatePublished": "2026-03-03",
    "schema:about": {
      "@id": "http://n2t.net/ark:/23942/g2example-collection"
    }
  },
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "USGS Geochemistry Lab"
      }
    ]
  },
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geochemistry",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000055"
    }
  ],
  "schema:hasPart": [
    {
      "@type": [
        "schema:Dataset"
      ],
      "schema:name": "BHVO-2 Reference Values",
      "schema:url": "https://example.org/standards/bhvo2",
      "schema:encodingFormat": [
        "text/csv"
      ]
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Standard Comparison Tool",
      "schema:url": "https://example.org/tools/standard-compare"
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
      "schema:name": "Some usage (10-50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000002"
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
      "schema:datePublished": "2024-03-20"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCollection/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g2example-collection",
  "@type": [
    "schema:CreativeWork",
    "schema:Product",
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Reference Standards Bundle",
  "schema:additionalType": [
    "EC Bundled Object"
  ],
  "schema:description": "A curated collection of geochemical reference standard datasets, software tools, and documentation for analytical laboratory calibration.",
  "schema:identifier": "http://n2t.net/ark:/23942/g2example-collection",
  "schema:url": "http://n2t.net/ark:/23942/g2example-collection",
  "schema:dateModified": "2026-03-03",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/SFO_0000075",
    "schema:name": "Bundled Object"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:ecrr-collection-catalog-record",
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCollection"
      }
    ],
    "schema:sdDatePublished": "2026-03-03",
    "schema:about": {
      "@id": "http://n2t.net/ark:/23942/g2example-collection"
    }
  },
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "USGS Geochemistry Lab"
      }
    ]
  },
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geochemistry",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000055"
    }
  ],
  "schema:hasPart": [
    {
      "@type": [
        "schema:Dataset"
      ],
      "schema:name": "BHVO-2 Reference Values",
      "schema:url": "https://example.org/standards/bhvo2",
      "schema:encodingFormat": [
        "text/csv"
      ]
    },
    {
      "@type": [
        "schema:SoftwareApplication"
      ],
      "schema:name": "Standard Comparison Tool",
      "schema:url": "https://example.org/tools/standard-compare"
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
      "schema:name": "Some usage (10-50 adopters)",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/UBA_0000002"
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
      "schema:datePublished": "2024-03-20"
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

<http://n2t.net/ark:/23942/g2example-collection> a schema1:CreativeWork,
        schema1:Dataset,
        schema1:Product ;
    ecrro:ECRRO_0000017 [ a schema1:PropertyValue ;
            schema1:name "Usage" ;
            schema1:propertyID "ecrro:ECRRO_0000017" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/UBA_0000002" ;
                    schema1:name "Some usage (10-50 adopters)" ] ] ;
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
                    schema1:datePublished "2024-03-20" ] ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000055" ;
            schema1:name "Geochemistry" ] ;
    schema1:additionalType "EC Bundled Object" ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "USGS Geochemistry Lab" ] ) ;
    schema1:dateModified "2026-03-03" ;
    schema1:description "A curated collection of geochemical reference standard datasets, software tools, and documentation for analytical laboratory calibration." ;
    schema1:hasPart [ a schema1:Dataset ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "BHVO-2 Reference Values" ;
            schema1:url "https://example.org/standards/bhvo2" ],
        [ a schema1:SoftwareApplication ;
            schema1:name "Standard Comparison Tool" ;
            schema1:url "https://example.org/tools/standard-compare" ] ;
    schema1:identifier "http://n2t.net/ark:/23942/g2example-collection" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Bundled Object" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/SFO_0000075" ] ;
    schema1:name "Geochemical Reference Standards Bundle" ;
    schema1:subjectOf <urn:uuid:ecrr-collection-catalog-record> ;
    schema1:url "http://n2t.net/ark:/23942/g2example-collection" .

<urn:uuid:ecrr-collection-catalog-record> a schema1:Dataset ;
    dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifCore>,
        <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRCollection>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <http://n2t.net/ark:/23942/g2example-collection> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2026-03-03" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Collection Profile
description: Complete ECRR metadata profile for bundled object (collection) resources.
  Composes ecrrBase, ecrrCommon, ecrrAssessment, and ecrrCollection. Resources must
  have schema:additionalType containing "EC Bundled Object".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCollection/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Bundled Object
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCollection/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRCollection/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRCollection`

