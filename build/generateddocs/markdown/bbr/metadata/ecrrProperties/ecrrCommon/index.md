
# ECRR Common optional metadata (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrCommon` *v0.1*

Schema defining commonly used optional properties shared across ECRR resource types, including agents, identifiers, keywords, science domains, audience, and related resources. Defines properties: schema:identifier, schema:url, schema:datePublished, schema:version, schema:alternateName, schema:sameAs, schema:creator, schema:contributor, schema:publisher, schema:editor, schema:funding, schema:keywords, schema:about, schema:audience, schema:subjectOf, schema:isRelatedTo, schema:isBasedOn, schema:encodingFormat, dct:bibliographicCitation, dct:conformsTo. Uses building blocks: labeledLink (schemaorgProperties), identifier (schemaorgProperties), definedTerm (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties), funder (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Common Optional Properties

Defines optional metadata properties frequently used across multiple ECRR resource types. These properties complement the mandatory `ecrrCore` fields.

### Agent Properties
- **schema:creator** — authors/originators of the resource
- **schema:contributor** — other contributing parties
- **schema:publisher** — party that made the resource available
- **schema:editor** — editors of the resource

All agent properties accept Person, Organization, or `@id` references to agents defined elsewhere.

### Identification and Versioning
- **schema:identifier** — external identifier (DOI, ARK) using PropertyValue pattern
- **schema:url** — landing page URL
- **schema:datePublished** — publication date (ISO 8601)
- **schema:version** — version string or number
- **schema:alternateName** — alternative names
- **schema:sameAs** — other identifiers for the same resource

### Classification and Discovery
- **schema:keywords** — free-text keywords
- **schema:about** — science domains from the ADO vocabulary (array of DefinedTerm)
- **schema:audience** — target user communities from the AUT vocabulary

### Related Resources
- **schema:subjectOf** — links to metadata records or web pages about this resource
- **schema:isRelatedTo** — documentation, publications, related tools
- **schema:isBasedOn** — specifications or semantic resources this resource builds on
- **dct:conformsTo** — specifications the resource conforms to

### Other
- **schema:funding** — grants and funding sources (MonetaryGrant)
- **schema:encodingFormat** — representation formats (MIME types)
- **dct:bibliographicCitation** — preferred citation (PropertyValue pattern)

## Examples

### Pyleoclim Software - Common Fields
ECRR common properties for the Pyleoclim software resource, shared across
all ECRR resource types.
#### json
```json
{
  "schema:identifier": "https://doi.org/10.5281/zenodo.4002870",
  "schema:version": "0.6.2",
  "schema:alternateName": "Python Package for the Analysis of Paleoclimate Data",
  "schema:creator": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Deborah Khider",
      "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Feng Zhu"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Julien Emile-Geay",
      "schema:identifier": "https://orcid.org/0000-0001-5920-4751"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Jun Hu"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Myron Kwan"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Pratheek Athreya"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Alexander James"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Daniel Garijo",
      "schema:identifier": "https://orcid.org/0000-0003-0454-7145"
    }
  ],
  "schema:keywords": "Paleoclimate",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "US National Science Foundation (US NSF)",
        "schema:identifier": "https://ror.org/021nxhr62"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "US NSF, ICER-1541029, AGS-2002556"
    }
  ],
  "schema:audience": [
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Data Users",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000002"
    },
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    }
  ],
  "schema:about": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Paleoclimatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000043"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Paleoceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000051"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Documentation",
      "schema:url": "https://pyleoclim-util.readthedocs.io/en/stable/"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Example Notebooks",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Pyleoclim GitHub page",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "dct:bibliographicCitation": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/context.jsonld"
  ],
  "schema:identifier": "https://doi.org/10.5281/zenodo.4002870",
  "schema:version": "0.6.2",
  "schema:alternateName": "Python Package for the Analysis of Paleoclimate Data",
  "schema:creator": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Deborah Khider",
      "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Feng Zhu"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Julien Emile-Geay",
      "schema:identifier": "https://orcid.org/0000-0001-5920-4751"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Jun Hu"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Myron Kwan"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Pratheek Athreya"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Alexander James"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Daniel Garijo",
      "schema:identifier": "https://orcid.org/0000-0003-0454-7145"
    }
  ],
  "schema:keywords": "Paleoclimate",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "US National Science Foundation (US NSF)",
        "schema:identifier": "https://ror.org/021nxhr62"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "US NSF, ICER-1541029, AGS-2002556"
    }
  ],
  "schema:audience": [
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Data Users",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000002"
    },
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": [
        "schema:Audience"
      ],
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    }
  ],
  "schema:about": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Paleoclimatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000043"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Paleoceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000051"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Documentation",
      "schema:url": "https://pyleoclim-util.readthedocs.io/en/stable/"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Example Notebooks",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:CreativeWork"
    ],
    "schema:name": "Pyleoclim GitHub page",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "dct:bibliographicCitation": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692"
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

[] dcterms:bibliographicCitation [ a schema1:PropertyValue ;
            schema1:name "Bibliographic citation" ;
            schema1:propertyID "dct:bibliographicCitation" ;
            schema1:value "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692" ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000035" ;
            schema1:name "Climatology" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000043" ;
            schema1:name "Paleoclimatology" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000051" ;
            schema1:name "Paleoceanography" ] ;
    schema1:alternateName "Python Package for the Analysis of Paleoclimate Data" ;
    schema1:audience [ a schema1:Audience ;
            schema1:audienceType "Scientists" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000007" ],
        [ a schema1:Audience ;
            schema1:audienceType "Developers" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000006" ],
        [ a schema1:Audience ;
            schema1:audienceType "Data Users" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000002" ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Jun Hu" ],
        [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0001-7501-8430" ;
            schema1:name "Deborah Khider" ],
        [ a schema1:Person ;
            schema1:name "Feng Zhu" ],
        [ a schema1:Person ;
            schema1:name "Alexander James" ],
        [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0001-5920-4751" ;
            schema1:name "Julien Emile-Geay" ],
        [ a schema1:Person ;
            schema1:name "Myron Kwan" ],
        [ a schema1:Person ;
            schema1:name "Pratheek Athreya" ],
        [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0003-0454-7145" ;
            schema1:name "Daniel Garijo" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:identifier "https://ror.org/021nxhr62" ;
                    schema1:name "US National Science Foundation (US NSF)" ] ],
        [ a schema1:MonetaryGrant ;
            schema1:name "US NSF, ICER-1541029, AGS-2002556" ] ;
    schema1:identifier "https://doi.org/10.5281/zenodo.4002870" ;
    schema1:isRelatedTo [ a schema1:CreativeWork ;
            schema1:name "Documentation" ;
            schema1:url "https://pyleoclim-util.readthedocs.io/en/stable/" ],
        [ a schema1:CreativeWork ;
            schema1:name "Example Notebooks" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks" ] ;
    schema1:keywords "Paleoclimate" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            schema1:name "Pyleoclim GitHub page" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util" ] ;
    schema1:version "0.6.2" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Common optional metadata
description: Commonly used optional properties shared across multiple ECRR resource
  types. Includes identifiers, agents (creator, contributor, publisher, editor), keywords,
  science domains (about), audience, related resources, funding, and citations.
type: object
properties:
  schema:identifier:
    description: External identifier for the resource (e.g. DOI, ARK). Use PropertyValue
      pattern to specify identifier scheme and resolver URL.
    anyOf:
    - $ref: '#/$defs/Identifier'
    - type: string
    x-jsonld-id: http://schema.org/identifier
  schema:url:
    type: string
    format: uri
    description: URL of a landing page or web resource describing the resource.
    x-jsonld-id: http://schema.org/url
  schema:datePublished:
    type: string
    description: ISO 8601 formatted date when the resource was published or released.
    x-jsonld-id: http://schema.org/datePublished
  schema:version:
    type:
    - string
    - number
    description: Version number or identifier for this resource.
    x-jsonld-id: http://schema.org/version
  schema:alternateName:
    description: Alternative names by which the resource is known.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
    x-jsonld-id: http://schema.org/alternateName
  schema:sameAs:
    description: Other identifiers or URIs for the same resource.
    type: array
    items:
      type: string
    x-jsonld-id: http://schema.org/sameAs
  schema:creator:
    description: 'Authors or originators of the resource content: an array of Person
      or Organization objects, or that array in a JSON-LD @list wrapper to preserve
      author order (CDIF''s form).'
    anyOf:
    - $ref: '#/$defs/Agents'
    - type: object
      required:
      - '@list'
      properties:
        '@list':
          $ref: '#/$defs/Agents'
    x-jsonld-id: http://schema.org/creator
  schema:contributor:
    description: Other parties who contributed to the resource.
    type: array
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
      - $ref: '#/$defs/Person'
      - $ref: '#/$defs/Organization'
    x-jsonld-id: http://schema.org/contributor
  schema:publisher:
    description: Party that made the resource publicly available.
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/Person'
    - $ref: '#/$defs/Organization'
    x-jsonld-id: http://schema.org/publisher
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
    x-jsonld-id: http://schema.org/editor
  schema:funding:
    description: Funding sources and grants that supported the resource.
    type: array
    items:
      $ref: '#/$defs/Funder'
    x-jsonld-id: http://schema.org/funding
  schema:keywords:
    description: Free-text keywords describing the resource content.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
    x-jsonld-id: http://schema.org/keywords
  schema:about:
    description: Science domains that the resource addresses. Array of DefinedTerm
      objects referencing the ECRR ADO (Academic Discipline Ontology) vocabulary.
    type: array
    items:
      $ref: '#/$defs/DefinedTerm'
    x-jsonld-id: http://schema.org/about
  schema:audience:
    description: Target user communities for the resource. Array of Audience objects
      with audienceType labels and identifiers from the AUT vocabulary.
    anyOf:
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: schema:Audience
          minItems: 1
          default:
          - schema:Audience
        schema:audienceType:
          type: string
          description: Label for the target audience (e.g. Data Producers, Scientists,
            Developers). Values from ECRR AUT vocabulary.
          x-jsonld-id: http://schema.org/audienceType
        schema:identifier:
          type: string
          description: URI from the ECRR AUT_ vocabulary.
          x-jsonld-id: http://schema.org/identifier
      required:
      - '@type'
      - schema:audienceType
    - type: array
      items:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:Audience
            minItems: 1
            default:
            - schema:Audience
          schema:audienceType:
            type: string
            description: Label for the target audience (e.g. Data Producers, Scientists,
              Developers). Values from ECRR AUT vocabulary.
            x-jsonld-id: http://schema.org/audienceType
          schema:identifier:
            type: string
            description: URI from the ECRR AUT_ vocabulary.
            x-jsonld-id: http://schema.org/identifier
        required:
        - '@type'
        - schema:audienceType
    x-jsonld-id: http://schema.org/audience
  schema:subjectOf:
    description: 'Metadata about this resource: the CDIF catalog record for this metadata
      (typed schema:Dataset, with dcat:CatalogRecord as its schema:additionalType),
      and/or labeled links (CreativeWork objects with name and url) to formal metadata
      records or web pages about the resource.'
    anyOf:
    - $ref: '#/$defs/SubjectOfItem'
    - type: array
      items:
        $ref: '#/$defs/SubjectOfItem'
    x-jsonld-id: http://schema.org/subjectOf
  schema:isRelatedTo:
    description: Related resources such as documentation, publications, or tools.
      Array of labeled links.
    type: array
    items:
      $ref: '#/$defs/LabeledLink'
    x-jsonld-id: http://schema.org/isRelatedTo
  schema:isBasedOn:
    description: Resources (e.g. semantic resources, specifications) that this resource
      is based on or derived from. Array of labeled links.
    type: array
    items:
      $ref: '#/$defs/LabeledLink'
    x-jsonld-id: http://schema.org/isBasedOn
  schema:encodingFormat:
    description: Representation formats for the resource content (e.g. MIME types,
      format names like RDF/XML, Turtle, JSON-LD).
    anyOf:
    - type: string
    - type: array
      items:
        type: string
    x-jsonld-id: http://schema.org/encodingFormat
  dct:bibliographicCitation:
    description: Preferred bibliographic citation for the resource, encoded as a PropertyValue
      with propertyID of dct:bibliographicCitation.
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValue
        minItems: 1
        default:
        - schema:PropertyValue
      schema:propertyID:
        type: string
        const: dct:bibliographicCitation
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        default: Bibliographic citation
        x-jsonld-id: http://schema.org/name
      schema:value:
        type: string
        x-jsonld-id: http://schema.org/value
    required:
    - '@type'
    - schema:propertyID
    - schema:value
    x-jsonld-id: http://purl.org/dc/terms/bibliographicCitation
  dct:conformsTo:
    description: Specifications or standards that the resource conforms to. Array
      of labeled links.
    type: array
    items:
      $ref: '#/$defs/LabeledLink'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
$defs:
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  Funder:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.yaml
  Agents:
    type: array
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
            description: reference to an agent defined elsewhere
      - $ref: '#/$defs/Person'
      - $ref: '#/$defs/Organization'
  CatalogRecord:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifCatalogRecord/schema.yaml
  SubjectOfItem:
    anyOf:
    - $ref: '#/$defs/CatalogRecord'
    - $ref: '#/$defs/LabeledLink'
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: ecrr.bbr.metadata.ecrrProperties.ecrrCommon
  register: https://usgin.github.io/ecrrBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-14'

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ecrr": "https://n2t.net/ark:/23942/g2",
    "schema": "http://schema.org/",
    "ecrro": "http://cor.esipfed.org/ont/earthcube/",
    "dct": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)
* [schema.org](https://schema.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrCommon`

