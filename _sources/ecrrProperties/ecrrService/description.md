## ECRR Service Instance Properties

Defines properties specific to service instance resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:WebAPI"]`.

### Properties

- **ecrro:ECRRO_0000502** — communication protocols (PropertyValue wrapping DefinedTerm array from CMPR vocabulary)
- **ecrro:ECRRO_0000503** — interface specification (PropertyValue wrapping labeled links to specification documents)
- **schema:supportingData** — input/output data formats (DataFeed objects with position and encodingFormat)
- **schema:potentialAction** — service invocation details using the Action pattern

### Communication Protocols (CMPR vocabulary)

HTTP, HTTPS, TCP/IP, FTP, SSH, SFTP, SMTP, IMAP, POP3

### Interface Specification Pattern

```json
{
  "ecrro:ECRRO_0000503": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000503",
    "schema:name": "Interface specification",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "WADL endpoint",
      "schema:url": "https://example.com/services/wadl"
    }
  }
}
```
