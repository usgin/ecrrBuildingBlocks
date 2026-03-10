
# ECRR Software profile (Schema)

`ecrr.bbr.metadata.profiles.ecrrProfiles.ECRRSoftware` *v0.1*

Complete ECRR metadata profile for software and application resources, composing base, common, assessment, and software-specific building blocks.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ECRR Software Profile

Complete metadata profile for registering software and application resources in the EarthCube Resource Registry.

### Composition

This profile composes four building blocks using `allOf`:

1. **ecrrBase** — mandatory identity, type, name, description, mainEntity classification, license
2. **ecrrCommon** — optional shared properties (creators, keywords, domains, audience, related resources, funding, citation)
3. **ecrrAssessment** — resource assessment (maturity, expected lifetime, usage level, stewardship, registration metadata)
4. **ecrrSoftware** — software-specific (application categories, runtime platforms, programming languages, supporting data, code repository, install URL, dependencies)

### Type Requirements

- `@type` must include `schema:CreativeWork` and `schema:SoftwareApplication`
- `mainEntity` must reference `http://cor.esipfed.org/ont/earthcube/ECRRO_0000206` (Software)

### Key Vocabularies

| Vocabulary | Property | Description |
|-----------|----------|-------------|
| SFO_ | applicationCategory | Software function categories |
| RTE_ | runtimePlatform | Runtime environments |
| MTU_ | ECRRO_0000138 | Maturity state |
| ELT_ | ECRRO_0000219 | Expected lifetime |
| UBA_ | ECRRO_0000017 | Usage level |
| ADO_ | about | Science domains |
| AUT_ | audience | Target audiences |

## Examples

### Pyleoclim Software - Complete ECRR Record
Example metadata instance for ECRRSoftware profile.
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
  "@id": "http://n2t.net/ark:/23942/g22914",
  "@type": [
    "schema:CreativeWork",
    "schema:Product",
    "schema:SoftwareApplication"
  ],
  "schema:name": "Pyleoclim",
  "schema:additionalType": [
    "EC Software"
  ],
  "schema:alternateName": "Python Package for the Analysis of Paleoclimate Data",
  "schema:description": "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues to simplify the user's life, with intuitive, high-level analysis and plotting methods that support publication-quality scientific workflows.",
  "schema:identifier": "https://doi.org/10.5281/zenodo.4002870",
  "schema:version": "0.6.2",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206",
    "schema:name": "Software"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License (GPL)",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/SWL_0000017"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Pyleoclim GitHub page",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
    },
    {
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
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:creator": [
    {
      "@type": "schema:Person",
      "schema:name": "Deborah Khider",
      "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Feng Zhu"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Julien Emile-Geay",
      "schema:identifier": "https://orcid.org/0000-0001-5920-4751"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Jun Hu"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Myron Kwan"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Pratheek Athreya"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Alexander James"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Daniel Garijo",
      "schema:identifier": "https://orcid.org/0000-0003-0454-7145"
    }
  ],
  "schema:keywords": "Paleoclimate",
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:name": "US National Science Foundation (US NSF)",
        "schema:identifier": "https://ror.org/021nxhr62"
      }
    },
    {
      "@type": "schema:MonetaryGrant",
      "schema:name": "US NSF, ICER-1541029, AGS-2002556"
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Data Users",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000002"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Technologists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000004"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Members of the Public",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000009"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Earth Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000021"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Paleoclimatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000043"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Paleoceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000051"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Documentation",
      "schema:url": "https://pyleoclim-util.readthedocs.io/en/stable/"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Example Notebooks LinkedEarth",
      "schema:url": "https://github.com/LinkedEarth/LiPDbooks/tree/master/notebooks"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Example Notebooks Github",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Linked Paleo Data framework Publication",
      "schema:url": "https://cp.copernicus.org/articles/12/1093/2016/"
    }
  ],
  "schema:applicationCategory": [
    "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
    "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
    "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
    "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
    "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011"
  ],
  "schema:runtimePlatform": [
    "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005"
  ],
  "schema:programmingLanguage": "Python 3.8",
  "schema:codeRepository": {
    "@type": "schema:CreativeWork",
    "schema:name": "Pyleoclim GitHub repository",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "schema:installURL": {
    "@type": "schema:CreativeWork",
    "schema:name": "PyPI",
    "schema:url": "https://pypi.org/project/pyleoclim/"
  },
  "schema:supportingData": {
    "@type": "schema:DataFeed",
    "schema:name": "Input Data Type specification",
    "schema:position": "input",
    "schema:encodingFormat": [
      "application/zip;type=LiPD",
      "application/json;type=pyleoclim",
      "text/csv;application=pyleoclim"
    ]
  },
  "dependencies": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
    "schema:name": "dependencies",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "Python 3.8",
      "schema:url": "https://www.python.org/"
    }
  },
  "dct:bibliographicCitation": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692"
  },
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
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
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
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": [
      {
        "@type": "schema:Person",
        "schema:name": "Deborah Khider",
        "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
      },
      {
        "@type": "schema:Person",
        "schema:name": "Feng Zhu"
      }
    ]
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
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-03-02"
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
    "https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware/context.jsonld",
    "https://schema.org/",
    {
      "ecrro": "http://cor.esipfed.org/ont/earthcube/",
      "ecrr": "https://n2t.net/ark:/23942/g2",
      "dct": "http://purl.org/dc/terms/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "http://n2t.net/ark:/23942/g22914",
  "@type": [
    "schema:CreativeWork",
    "schema:Product",
    "schema:SoftwareApplication"
  ],
  "schema:name": "Pyleoclim",
  "schema:additionalType": [
    "EC Software"
  ],
  "schema:alternateName": "Python Package for the Analysis of Paleoclimate Data",
  "schema:description": "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues to simplify the user's life, with intuitive, high-level analysis and plotting methods that support publication-quality scientific workflows.",
  "schema:identifier": "https://doi.org/10.5281/zenodo.4002870",
  "schema:version": "0.6.2",
  "schema:mainEntity": {
    "@type": "schema:CreativeWork",
    "schema:url": "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206",
    "schema:name": "Software"
  },
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License (GPL)",
      "schema:url": "http://cor.esipfed.org/ont/earthcube/SWL_0000017"
    }
  ],
  "schema:subjectOf": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Pyleoclim GitHub page",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
    },
    {
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
          "@id": "https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware"
        }
      ],
      "schema:sdDatePublished": "2026-03-03"
    }
  ],
  "schema:creator": [
    {
      "@type": "schema:Person",
      "schema:name": "Deborah Khider",
      "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Feng Zhu"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Julien Emile-Geay",
      "schema:identifier": "https://orcid.org/0000-0001-5920-4751"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Jun Hu"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Myron Kwan"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Pratheek Athreya"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Alexander James"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Daniel Garijo",
      "schema:identifier": "https://orcid.org/0000-0003-0454-7145"
    }
  ],
  "schema:keywords": "Paleoclimate",
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:funder": {
        "@type": "schema:Organization",
        "schema:name": "US National Science Foundation (US NSF)",
        "schema:identifier": "https://ror.org/021nxhr62"
      }
    },
    {
      "@type": "schema:MonetaryGrant",
      "schema:name": "US NSF, ICER-1541029, AGS-2002556"
    }
  ],
  "schema:audience": [
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Data Users",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000002"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Technologists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000004"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Developers",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000006"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Scientists",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000007"
    },
    {
      "@type": "schema:Audience",
      "schema:audienceType": "Members of the Public",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/AUT_0000009"
    }
  ],
  "schema:about": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Climatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000035"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Earth Science",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000021"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Paleoclimatology",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000043"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Paleoceanography",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ADO_0000051"
    }
  ],
  "schema:isRelatedTo": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Documentation",
      "schema:url": "https://pyleoclim-util.readthedocs.io/en/stable/"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Example Notebooks LinkedEarth",
      "schema:url": "https://github.com/LinkedEarth/LiPDbooks/tree/master/notebooks"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Example Notebooks Github",
      "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Linked Paleo Data framework Publication",
      "schema:url": "https://cp.copernicus.org/articles/12/1093/2016/"
    }
  ],
  "schema:applicationCategory": [
    "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
    "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
    "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
    "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
    "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011"
  ],
  "schema:runtimePlatform": [
    "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005"
  ],
  "schema:programmingLanguage": "Python 3.8",
  "schema:codeRepository": {
    "@type": "schema:CreativeWork",
    "schema:name": "Pyleoclim GitHub repository",
    "schema:url": "https://github.com/LinkedEarth/Pyleoclim_util"
  },
  "schema:installURL": {
    "@type": "schema:CreativeWork",
    "schema:name": "PyPI",
    "schema:url": "https://pypi.org/project/pyleoclim/"
  },
  "schema:supportingData": {
    "@type": "schema:DataFeed",
    "schema:name": "Input Data Type specification",
    "schema:position": "input",
    "schema:encodingFormat": [
      "application/zip;type=LiPD",
      "application/json;type=pyleoclim",
      "text/csv;application=pyleoclim"
    ]
  },
  "dependencies": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "http://purl.obolibrary.org/obo/RO_0002502",
    "schema:name": "dependencies",
    "schema:value": {
      "@type": "schema:CreativeWork",
      "schema:name": "Python 3.8",
      "schema:url": "https://www.python.org/"
    }
  },
  "dct:bibliographicCitation": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "dct:bibliographicCitation",
    "schema:name": "Bibliographic citation",
    "schema:value": "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692"
  },
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
      "schema:name": "1 - 5 years",
      "schema:identifier": "http://cor.esipfed.org/ont/earthcube/ELT_0000003"
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
  "ecrro:ECRRO_0000218": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "ecrro:ECRRO_0000218",
    "schema:name": "Stewardship",
    "schema:value": [
      {
        "@type": "schema:Person",
        "schema:name": "Deborah Khider",
        "schema:identifier": "https://orcid.org/0000-0001-7501-8430"
      },
      {
        "@type": "schema:Person",
        "schema:name": "Feng Zhu"
      }
    ]
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
        "schema:name": "Stephen M. Richard"
      },
      "schema:datePublished": "2021-03-02"
    }
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ecrro: <http://cor.esipfed.org/ont/earthcube/> .
@prefix schema1: <http://schema.org/> .

<http://n2t.net/ark:/23942/g22914> a schema1:CreativeWork,
        schema1:Product,
        schema1:SoftwareApplication ;
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
    ecrro:ECRRO_0000218 [ a schema1:PropertyValue ;
            schema1:name "Stewardship" ;
            schema1:propertyID "ecrro:ECRRO_0000218" ;
            schema1:value [ a schema1:Person ;
                    schema1:name "Feng Zhu" ],
                [ a schema1:Person ;
                    schema1:identifier "https://orcid.org/0000-0001-7501-8430" ;
                    schema1:name "Deborah Khider" ] ] ;
    ecrro:ECRRO_0000219 [ a schema1:PropertyValue ;
            schema1:name "expected lifetime" ;
            schema1:propertyID "ecrro:ECRRO_0000219" ;
            schema1:value [ a schema1:DefinedTerm ;
                    schema1:identifier "http://cor.esipfed.org/ont/earthcube/ELT_0000003" ;
                    schema1:name "1 - 5 years" ] ] ;
    ecrro:ECRRO_0001301 [ a schema1:PropertyValue ;
            schema1:name "registration metadata" ;
            schema1:propertyID "ecrro:ECRRO_0001301" ;
            schema1:value [ a schema1:StructuredValue ;
                    schema1:additionalType "ecrro:ECRRO_0000156" ;
                    schema1:contributor [ a schema1:Person ;
                            schema1:name "Stephen M. Richard" ] ;
                    schema1:datePublished "2021-03-02" ] ] ;
    dct:bibliographicCitation [ a schema1:PropertyValue ;
            schema1:name "Bibliographic citation" ;
            schema1:propertyID "dct:bibliographicCitation" ;
            schema1:value "Deborah Khider, Feng Zhu, Julien Emile-Geay, Jun Hu, Alexander James, Pratheek Athreya, Myron Kwan, Daniel Garijo. (2021). Pyleoclim: v0.6.1 Release. Zenodo. http://doi.org/10.5281/zenodo.1212692" ] ;
    schema1:about [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000021" ;
            schema1:name "Earth Science" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000043" ;
            schema1:name "Paleoclimatology" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000035" ;
            schema1:name "Climatology" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/ADO_0000051" ;
            schema1:name "Paleoceanography" ] ;
    schema1:additionalType "EC Software" ;
    schema1:alternateName "Python Package for the Analysis of Paleoclimate Data" ;
    schema1:applicationCategory "Data Analysis, http://cor.esipfed.org/ont/earthcube/SFO_0000010",
        "Data Exploration, http://cor.esipfed.org/ont/earthcube/SFO_0000006",
        "Data Preparation, http://cor.esipfed.org/ont/earthcube/SFO_0000007",
        "Data Processing / Modeling, http://cor.esipfed.org/ont/earthcube/SFO_0000008",
        "Visualization, http://cor.esipfed.org/ont/earthcube/SFO_0000011" ;
    schema1:audience [ a schema1:Audience ;
            schema1:audienceType "Scientists" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000007" ],
        [ a schema1:Audience ;
            schema1:audienceType "Developers" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000006" ],
        [ a schema1:Audience ;
            schema1:audienceType "Technologists" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000004" ],
        [ a schema1:Audience ;
            schema1:audienceType "Members of the Public" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000009" ],
        [ a schema1:Audience ;
            schema1:audienceType "Data Users" ;
            schema1:identifier "http://cor.esipfed.org/ont/earthcube/AUT_0000002" ] ;
    schema1:codeRepository [ a schema1:CreativeWork ;
            schema1:name "Pyleoclim GitHub repository" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util" ] ;
    schema1:creator [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0001-7501-8430" ;
            schema1:name "Deborah Khider" ],
        [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0003-0454-7145" ;
            schema1:name "Daniel Garijo" ],
        [ a schema1:Person ;
            schema1:name "Myron Kwan" ],
        [ a schema1:Person ;
            schema1:identifier "https://orcid.org/0000-0001-5920-4751" ;
            schema1:name "Julien Emile-Geay" ],
        [ a schema1:Person ;
            schema1:name "Jun Hu" ],
        [ a schema1:Person ;
            schema1:name "Alexander James" ],
        [ a schema1:Person ;
            schema1:name "Feng Zhu" ],
        [ a schema1:Person ;
            schema1:name "Pratheek Athreya" ] ;
    schema1:dependencies [ a schema1:PropertyValue ;
            schema1:name "dependencies" ;
            schema1:propertyID "http://purl.obolibrary.org/obo/RO_0002502" ;
            schema1:value [ a schema1:CreativeWork ;
                    schema1:name "Python 3.8" ;
                    schema1:url "https://www.python.org/" ] ] ;
    schema1:description "Pyleoclim is a Python package primarily geared towards the analysis and visualization of paleoclimate data. Such data usually come in the form of timeseries with missing values and age uncertainties, so the package includes several low-level methods to deal with these issues to simplify the user's life, with intuitive, high-level analysis and plotting methods that support publication-quality scientific workflows." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:identifier "https://ror.org/021nxhr62" ;
                    schema1:name "US National Science Foundation (US NSF)" ] ],
        [ a schema1:MonetaryGrant ;
            schema1:name "US NSF, ICER-1541029, AGS-2002556" ] ;
    schema1:identifier "https://doi.org/10.5281/zenodo.4002870" ;
    schema1:installURL [ a schema1:CreativeWork ;
            schema1:name "PyPI" ;
            schema1:url "https://pypi.org/project/pyleoclim/" ] ;
    schema1:isRelatedTo [ a schema1:CreativeWork ;
            schema1:name "Linked Paleo Data framework Publication" ;
            schema1:url "https://cp.copernicus.org/articles/12/1093/2016/" ],
        [ a schema1:CreativeWork ;
            schema1:name "Example Notebooks LinkedEarth" ;
            schema1:url "https://github.com/LinkedEarth/LiPDbooks/tree/master/notebooks" ],
        [ a schema1:CreativeWork ;
            schema1:name "Documentation" ;
            schema1:url "https://pyleoclim-util.readthedocs.io/en/stable/" ],
        [ a schema1:CreativeWork ;
            schema1:name "Example Notebooks Github" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util/tree/master/example_notebooks" ] ;
    schema1:keywords "Paleoclimate" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "GNU General Public License (GPL)" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/SWL_0000017" ] ;
    schema1:mainEntity [ a schema1:CreativeWork ;
            schema1:name "Software" ;
            schema1:url "http://cor.esipfed.org/ont/earthcube/ECRRO_0000206" ] ;
    schema1:name "Pyleoclim" ;
    schema1:programmingLanguage "Python 3.8" ;
    schema1:runtimePlatform "Linux, http://cor.esipfed.org/ont/earthcube/RTE_000005" ;
    schema1:subjectOf [ a schema1:CreativeWork ;
            schema1:name "Pyleoclim GitHub page" ;
            schema1:url "https://github.com/LinkedEarth/Pyleoclim_util" ],
        [ a schema1:CreativeWork ;
            dct:conformsTo <https://w3id.org/cdif/bbr/metadata/cdifProperties/cdifMandatory>,
                <https://w3id.org/cdif/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware> ;
            schema1:additionalType "dcat:CatalogRecord" ;
            schema1:sdDatePublished "2026-03-03" ] ;
    schema1:supportingData [ a schema1:DataFeed ;
            schema1:encodingFormat "application/json;type=pyleoclim",
                "application/zip;type=LiPD",
                "text/csv;application=pyleoclim" ;
            schema1:name "Input Data Type specification" ;
            schema1:position "input" ] ;
    schema1:version "0.6.2" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: ECRR Software Profile
description: Complete ECRR metadata profile for software and application resources.
  Composes ecrrBase (mandatory identity and classification), ecrrCommon (optional
  shared properties), ecrrAssessment (maturity, lifetime, usage), and ecrrSoftware
  (application categories, languages, repositories, etc.). Resources must have schema:additionalType
  containing "EC Software".
allOf:
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrBase/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrCommon/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrAssessment/schema.yaml
- $ref: https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/ecrrProperties/ecrrSoftware/schema.yaml
- properties:
    schema:additionalType:
      contains:
        enum:
        - EC Software
x-jsonld-extra-terms:
  ecrr: https://n2t.net/ark:/23942/g2
x-jsonld-prefixes:
  schema: http://schema.org/
  ecrro: http://cor.esipfed.org/ont/earthcube/
  dct: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ecrrBuildingBlocks/build/annotated/bbr/metadata/profiles/ecrrProfiles/ECRRSoftware/context.jsonld)

## Sources

* [EarthCube Resource Registry](https://www.earthcube.org/resource-registry)
* [schema.org SoftwareApplication](https://schema.org/SoftwareApplication)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ecrrBuildingBlocks](https://github.com/usgin/ecrrBuildingBlocks)
* Path: `_sources/profiles/ecrrProfiles/ECRRSoftware`

