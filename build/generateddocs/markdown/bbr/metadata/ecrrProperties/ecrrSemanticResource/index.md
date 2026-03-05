
# ECRR Semantic Resource properties (Schema)

`ecrr.bbr.metadata.ecrrProperties.ecrrSemanticResource` *v0.1*

Schema defining properties specific to semantic resource types in the EarthCube Resource Registry, including subtype classification for ontologies, thesauri, controlled vocabularies, and other semantic resources. Defines properties: schema:programmingLanguage.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Semantic Resource Properties

Defines properties specific to semantic resources in the EarthCube Resource Registry. For resources with `mainEntity` pointing to `ECRRO_0000210` (Semantic Resource).

### Properties

- **schema:programmingLanguage** — representation language (OWL, SKOS, RDF, etc.) as string or ComputerLanguage object

Other relevant properties from `ecrrCommon`:
- **schema:encodingFormat** — serialization formats (RDF/XML, Turtle, N-Triples, JSON-LD)
- **schema:isBasedOn** — other semantic resources this one builds on

### Semantic Resource Subtypes (srt_ vocabulary)

Subtypes are conveyed via additional entries in the `mainEntity` array:

| Subtype | srt_ URI |
|---------|----------|
| Glossary | `srt_0000001` |
| Thesaurus | `srt_0000002` |
| Ontology | `srt_0000003` |
| Controlled Vocabulary | `srt_0000004` |
| Taxonomy | `srt_0000005` |
| Conceptual Model | `srt_0000006` |
| RDF Vocabulary | `srt_0000007` |
| SKOS Vocabulary | `srt_0000008` |

### Example mainEntity with Semantic Resource Subtype

```json
{
  "schema:mainEntity": [
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000210",
      "schema:name": "Semantic Resource"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/srt_0000003",
      "schema:name": "Ontology"
    }
  ]
}
```

## Examples

### LiPD Ontology Semantic Resource Properties
ECRR semantic resource properties for the LiPD (Linked Paleo Data) ontology.
#### json
```json
{
  "schema:programmingLanguage": {
    "@type": "schema:ComputerLanguage",
    "schema:name": "OWL",
    "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MOLA_0000001"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSemanticResource/context.jsonld"
  ],
  "schema:programmingLanguage": {
    "@type": "schema:ComputerLanguage",
    "schema:name": "OWL",
    "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MOLA_0000001"
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:programmingLanguage [ a schema1:ComputerLanguage ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/MOLA_0000001" ;
            schema1:name "OWL" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ECRR Semantic Resource Properties
description: Properties specific to semantic resource types in ECRR. For resources
  with mainEntity pointing to ECRRO_0000210 (Semantic Resource). The semantic resource
  subtype is conveyed via additional entries in the mainEntity array using srt_ vocabulary
  URIs. Additional properties like programmingLanguage and encodingFormat from ecrrCommon
  are particularly relevant for semantic resources.
type: object
properties:
  schema:programmingLanguage:
    description: The representation language of the semantic resource (e.g. OWL, SKOS,
      RDF). Can be a string or a ComputerLanguage object with name and identifier
      referencing the MOLA vocabulary.
    anyOf:
    - type: string
    - type: object
      properties:
        '@type':
          type: string
          const: schema:ComputerLanguage
          default: schema:ComputerLanguage
        schema:name:
          type: string
          description: Name of the representation language (e.g. OWL, SKOS, RDF/XML)
        schema:identifier:
          type: string
          description: URI from the MOLA vocabulary
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

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSemanticResource/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSemanticResource/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSemanticResource/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/ecrrProperties/ecrrSemanticResource`

