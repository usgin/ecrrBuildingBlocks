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
