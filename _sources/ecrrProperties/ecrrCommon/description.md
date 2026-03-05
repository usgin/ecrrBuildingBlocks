## ECRR Common Optional Properties

Defines optional metadata properties frequently used across multiple ECRR resource types. These properties complement the mandatory `ecrrBase` fields.

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
