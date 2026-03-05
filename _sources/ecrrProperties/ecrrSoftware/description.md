## ECRR Software-Specific Properties

Defines properties specific to software and application resources in the EarthCube Resource Registry. For resources typed `["schema:CreativeWork", "schema:SoftwareApplication"]`.

### Properties

- **schema:applicationCategory** — function categories from the SFO vocabulary (e.g. Data Analysis, Visualization, Data Processing)
- **schema:runtimePlatform** — runtime environments from the RTE vocabulary (e.g. Linux, Browser, HPC, Android)
- **schema:programmingLanguage** — implementation languages (string or ComputerLanguage objects)
- **schema:supportingData** — input/output data format specifications as DataFeed objects with position and encodingFormat
- **schema:codeRepository** — source code repository URLs or labeled links
- **schema:installURL** — software installation locations (e.g. PyPI, CRAN, npm)
- **schema:potentialAction** — web application invocation using the Action pattern
- **dependencies** — software dependencies as PropertyValue wrapping labeled links

### Data Feed Specification Pattern

The `supportingData` property describes input and output data formats:

```json
{
  "@type": "schema:DataFeed",
  "schema:name": "Input Data Type specification",
  "schema:position": "input",
  "schema:encodingFormat": ["application/json", "text/csv"]
}
```

### Dependencies Pattern

Dependencies use PropertyValue with the OBO Relations Ontology "depends on" property:

```json
{
  "@type": "schema:PropertyValue",
  "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
  "schema:name": "dependencies",
  "schema:value": {
    "@type": "schema:CreativeWork",
    "schema:name": "Python 3.8"
  }
}
```
