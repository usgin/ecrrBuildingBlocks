## ECRR Resource Assessment Properties

Defines ECRR-specific properties for assessing resource status, sustainability, and provenance. These properties use the PropertyValue pattern with ECRRO ontology property identifiers as top-level JSON keys.

### Properties

| Property | ECRRO ID | Vocabulary | Description |
|----------|----------|------------|-------------|
| Maturity state | `ecrro:ECRRO_0000138` | MTU_ | Current development/deployment status |
| Expected lifetime | `ecrro:ECRRO_0000219` | ELT_ | Anticipated longevity of the resource |
| Usage level | `ecrro:ECRRO_0000017` | UBA_ | Current adoption level |
| Stewardship | `ecrro:ECRRO_0000218` | (agent) | Maintainer(s) of the resource |
| Primary publication | `ecrro:ECRRO_0000600` | (string) | Citation of the primary publication |
| Registration metadata | `ecrro:ECRRO_0001301` | (StructuredValue) | Who registered the resource and when |

### Pattern

Each assessment property is a top-level key with an ECRRO URI. The value is a PropertyValue object whose `value` field contains a DefinedTerm (for vocabulary-controlled properties), an agent (for stewardship), or a string (for publications).

```json
{
  "ecrro:ECRRO_0000138": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000138",
    "schema:name": "has maturity state",
    "schema:value": {
      "@type": "schema:DefinedTerm",
      "schema:name": "In production",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/MTU_0000002"
    }
  }
}
```

### Controlled Vocabularies

- **MTU (Maturity)**: Used in multiple places, In production, Alpha, Beta, Planning, etc.
- **ELT (Expected Lifetime)**: Long-term, >5 years, 1-5 years, Unknown, N/A
- **UBA (Usage)**: Wide (>50), Some (10-50), Low, Unknown, N/A
