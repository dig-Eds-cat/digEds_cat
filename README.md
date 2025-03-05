![Catalogue_logo](DigEds_Cat_small_transp.png)

# Catalogue of Digital Editions
This research seeks to examine best practice in the field of digital editions by collating relevant evidence in a detailed catalogue of extant digital projects. The editions included in the **Catalogue** come from numerous sources and their selection follows basic criteria: the electronic texts can be ongoing or complete projects, born-digital editions or electronic reproductions of print volumes.

More information:

* [What is the Catalogue of Digital Editions?](https://github.com/dig-Eds-cat/digEds_cat/wiki)
* [How to contribute to the Catalogue?](.github/CONTRIBUTING.md)

## Affiliation(s)

This project's home is the UCL Centre for Digital Humanities. The **Catalogue** [Web Application](https://dig-ed-cat.acdh.oeaw.ac.at) is a collaboration with the Austrian Centre for Digital Humanities.

## Citation

> Franzini, G. (2012-) *A Catalogue of Digital Editions*. [![DOI](https://zenodo.org/badge/42574907.svg)](https://zenodo.org/badge/latestdoi/42574907)

## Indexing

Indexed in [OpenAIRE](https://www.openaire.eu/search/dataset?datasetId=r37b0ad08687::c2ad7b8b5225d5abc748a1c6bbb07aeb) and in the [Datenbank-Infosystem (DBIS)](http://dbis.uni-regensburg.de//fachliste.php?lett=l).

## Licence

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

*The Catalogue of Digital Editions* by [Greta Franzini](https://gretafranzini.com) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).


## development/scripts/workflows

### data-schema

The data-schema is curated in [schema.json](schema.json). This is obvisouly some custom format incuding information to
* create a typesense index (used in the webapplication)
* create a [human readable documentation](.github/CONTRIBUTING.md) of the data-schema
* create an [issue template](.github/ISSUE_TEMPLATE/new-edition.yml) providing a forms to suggest a new entry. Go to [create new issue](https://github.com/dig-Eds-cat/digEds_cat/issues/new/choose) to check it out.

run `./scripts/schema_updates.sh` to update all schema-related files

###  process new-entry issue

[This script](scripts/new_entry_issue.py) fetches the payload of a new-entry issue and merges it into the the main data-set.
* create and checkout an issue branch
* adapt ISSUE_NR in the script
* run the script
* check the result, replace the generic ID `9999` with a new one
* commit and merge the result into main branch via PR

### healh_check

The [Quality of Data repo](https://github.com/dig-Eds-cat/qod) provides an worklow checking if the URLs in the Catalogue are currently available. By running
```shell
python scripts/health_check.py
```
the results of this health checked are added to the Catalogue data.