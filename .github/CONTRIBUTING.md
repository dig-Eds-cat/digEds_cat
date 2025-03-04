# How to contribute a digital edition to the _Catalogue_

## Inclusion criteria
The project is constantly evolving as users request more features and development on the [web app](https://github.com/acdh-oeaw/dig_ed_cat) moves forward. At the moment we don't accept ebooks, any form of commercial digital books or transcriptions made available via Wikisource, but projects whose authorship can be traced back to one or multiple individuals with, if possible, an institutional affiliation (university and/or GLAM institution). We primarily look for digital editions and digital scholarly editions (by which we mean editions with a strong critical component) but people are also beginning to submit digital archives, textual collections where some texts are treated in more detail, etc. It's worth noting that people define their projects in various ways (e.g. a project may define itself as a database when it fact it might be more of a digital archive) using different terms synonymously. This makes it difficult to pick what should be included in our list or not. The line of inclusion in our catalogue is a little blurry but it reflects the fuzziness that comes with these projects.

## Updating existing entries
If you want to **suggest changes to existing editions**, please add these as issues in this repository with the name of the edition in question. You can suggest edits either via a GitHub pull-request or by telling us in the issue text field what you'd like us to change.

## Contribution options: GitHub or Google Forms
There are **three different ways to contribute a digital edition**: 

1. If you're familiar with GitHub, you know what to do: fork this repository, edit the .csv file and create a pull request. 
2. If you're not familiar with GitHub, you can create a GitHub [issue](https://github.com/gfranzini/digEds_cat/issues) with as much information about the edition as possible (see "Data fields" section below). The more information you provide, the sooner the edition will appear in the _Catalogue_.
3. If you'd rather not use GitHub at all, you can fill-in [this Google Form](https://goo.gl/forms/4Ya3jwRCBi0VSexx2). Your entry will be moderated and added to the _Catalogue_ by an administrator.

It's important you're consistent and follow these guidelines for the [web application](https://dig-ed-cat.acdh.oeaw.ac.at/) to display your contribution correctly.

## Contributing via GitHub
The fields the _Catalogue_ uses to classify information are listed below. Some take free text, others use predefined values. 
The words "**not provided**" are used to indicate that the website or project does not provide the relevant information.
However you choose to contribute a digital edition to the _Catalogue_, please ensure you address as many of the following fields as possible.

#### id

An internal identifier. Provided by the data-curation team

#### Historical Period

This field broadly categorises the source material of a digital edition by the following periods:

* Antiquity [700 BC - 500 AD]
* Middle Ages [500 - 1500]
* Early Modern [1500 - 1789]
* Long Nineteenth Century [1789 - 1914]
* Modern [1914 - 1965]
* Contemporary [1965 - Today]

#### Time/Century

The specific year(s) or century of the digital edition's source material.
Year ranges can also be added in the format `YYYY-YYYY`.

#### Edition name

The name of the digital edition project.

#### URL

The URL of the digital edition project.

#### Scholarly

Here the values yes or no should be used to say whether the edition is _scholarly_ in accordance with [Patrick Sahle](https://www.digitale-edition.de/exist/apps/editions-browser/about.html)'s definition of the term:
>An edition must be critical, must have critical components - a pure facsimile is not an edition, a digital library is not an edition.

#### Digital vs. Digitised

Here the values yes or no should be used to say whether the digital edition is _digital_ in accordance with [Patrick Sahle](https://www.digitale-edition.de/exist/apps/editions-browser/about.html)'s definition of the term:
>"A digitized print edition is not a "digital edition". If the paradigm of an edition is limited to the two-dimensional space of the "page" and to typographic means of information representation, then it's not a digital edition." (see: https://www.digitale-edition.de/exist/apps/editions-browser/about.html)

#### Edition

Here the values values yes and no should be used to say whether the digital edition is an _edition_ in accordance with [Patrick Sahle](https://www.digitale-edition.de/exist/apps/editions-browser/about.html)'s definition of the term:
>An edition must represent its material (usually as transcribed/edited text) - a catalog, an index, a descriptive database is not an edition.

#### Language

Here the values values yes and no should be used to say whether the digital edition is an _edition_ in accordance with [Patrick Sahle](https://www.digitale-edition.de/exist/apps/editions-browser/about.html)'s definition of the term:
>An edition must represent its material (usually as transcribed/edited text) - a catalog, an index, a descriptive database is not an edition.

#### Writing support

The nature of the source material (manuscript, letter, notebook, etc.). Use the singular form of the tag only (e.g. "Letter" even if the edition contains multiple) and capitalise the first letter. Separate multiple source materials with a semicolon.

#### Begin date

Year the project started. If not specified, use `not provided`.

#### End date

Year the project ended. If ongoing type `present`. If not specified, use `not provided`.

#### Manager

Name and surname of principal investigator/manager/coordinator.
If multiple, separate with a semicolon.

#### Participating institution(s)

Institution(s) involved in the project. If multiple, separate with a semicolon.
If not specified, use `not provided`.

#### Audience

The target audience of the digital edition project (scholars, students, general public, etc.).
If not specified, use `not provided`. If multiple, separate with a semicolon.

#### Philological statement

* `no`: No information on the editorial methods and practices nor on the source (digital or printed) of the text.
* `partly`: Some information about the source, and of the author, date and accuracy of the digital edition.
* `yes`: Complete information on the source of the text, as well as on the author, date and accuracy of the digital edition; (Digital Humanities) standards implemented, including modelling, markup language, data structure and software.

#### Account of textual variance

* `no`: No account of textual variance is given. The digital edition is a reproduction of a given print edition without any account of variants.
* `partly`: The digital edition is a reproduction of a given print scholarly edition and reproduces the selected textual variants extant in the apparatus criticus of that edition; or the edition does not follow a digital paradigm, in that the variants are not automatically computable the way they are encoded.
* `yes`: This edition is “based on full-text transcription of original texts into electronic form” 

#### Value of witnesses

* `N/A`: Not applicable, as no information about the source of the text is given, though it is easily assumable that the source is another digital or printed edition (possibly even a scholarly edition).
* `no`: The only witness modelled digitally is a printed non-scholarly edition used as a source for the digital edition.
* `partly`: Same as above, but the witness/source is a scholarly edition.
* `yes`: The witnesses are traditional philological primary sources (including manuscripts, inscriptions or papyri).

#### XML-TEI transcription

The source material is encoded in XML-TEI. Values:
* `no`: XML not used
* `partly`: XML but not TEI
* `yes`: XML-TEI is used

#### XML(-TEI) transcription is available to download

The source material is encoded in XML-TEI. Values:
* `no`
* `partly`
* `yes`

#### Images

The values `no`, `partly` or `yes` are used to specify if the edition comes with images. The value `not provided` is used for digital editions protected by access restrictions or paywalls whose homepage does not make clear whether images are provided.

#### Zoom images

The values `yes` or `no` are used to specify if the user can zoom in or out of images.

#### Image manipulation

The values `yes`or `no` are used to specify whether the user can manipulate the images (e.g. rotation, brightness, etc.).

#### Image manipulation

The values `yes` or `no` are used to tell us whether the transcription and the image are linked so that clicking on a word (or line) in the image brings up the corresponding word in the transcription and vice-versa.

#### Source text translation

The project provides a translation of the source material (not necessarily into English). If so, the corresponding [three-letter ISO codes](http://www.loc.gov/standards/iso639-2/php/code_list.php) should be used. If not, type `no`.

#### Website language

The project website is available in multiple languages. If so, the corresponding [three-letter ISO codes](http://www.loc.gov/standards/iso639-2/php/code_list.php) should be used. If not, simply type `no`.

#### Glossary

The values `yes` or `no` are used to specify if the digital edition provides a glossary.

#### Indices

The values `yes` or `no` are used to specify if the digital edition provides indices.

#### String matching search

The values `yes` or `no` are used to specify if the edition provides string matching (full text) search possibilities.


#### Advanced search

The values `yes` or `no` are used to specify if the digital edition provides advanced search functionality.

#### Creative Commons License

The values `yes`, `partially` or `no` are used to specify if the digital edition is protected by a Creative Commons License.

#### Open Source/Open Access

* `no`: Proprietary, all material is copyrighted. The source is closed and not reusable by other research projects. To access the material, users must pay a subscription fee.
* `partly`: Same as above but the subscription is free of charge.
* `yes`: Open Access. The texts may be accessed through specific software but the source is not accessible.
* `Open Access and Open Source (some data)`: Open Access and Open Source. Part of the data underlying the digital edition (e.g. text but not images) is freely available for access and reuse.
* `Open Access and Open Source (all data)`: Open Access and Open Source. All data underlying the digital edition is freely available for access and reuse.

#### Linked Open Data (LOD)

The values `yes` or `no` are used to specify if the digital edition makes use of [Linked Open Data](https://programminghistorian.org/lessons/intro-to-linked-data) (LOD) standards and if it is linked to other projects/data.

#### Application Programming Interface (API)

The values `yes` or `no` are used to specify if the digital edition comes with an API.

#### Crowdsourcing

The values `yes` or `no` are used to specify if the digital edition relies/relied on crowdsourced contributions.

#### Feedback

The values `yes` or `no` are used to specify if the digital edition provides a feedback space or contact information for users to make comments or suggestions.

#### Technological statement

This category assesses whether the digital edition provides complete information about technical aspects and practices.
* `no`: no information.
* `partly`: partial information.
* `yes`: complete information.

#### Technological statement

The values `yes` or `no` are used to specify if the digital edition provides links to external relevant resources.

#### OCR'd or keyed

The source text was digitised with Optical Character Recognition (OCR) software or manually Keyed in. Use `Keyed`, `OCR` or `Keyed; OCR

#### Mobile-friendly/application

The values `yes` or `no` are used to tell if the project is mobile friendly

#### Print-friendly view

The values `yes` or `no` are used to specify if the digital edition provides a print-friendly view of the text (e.g. PDF) or if the browser produces a suitable, printable version of the content.

#### Print facsimile (complementary output)

The values `yes` or `no` are used to specify if the digital project is complemented by a printed facsimile.

#### Repository of source material

The institution(s) that house the source text(s). `N/A` is used if the source is a new edition without a physical location, and `not provided` is used to indicate that the project website does not give clear information about the source's current repository.

#### Place of origin of source material

If known, the location from which the source text originated or where it was produced. `N/A` is used to indicate that the project does not have a physical provenance, and `not provided` is used to indicate that the project website does not give clear information about the source's provenance.

#### Sponsor/Funding body

The name of the funding agency. `N/A` is used if the project isn't supported by third-party funding.

#### Budget (rough)

How much the project cost. All currencies are supported and the numeric value should use commas as thousands separators (e.g. £10,000). The value `not provided` is used to indicate that the project website does not make this information known; `0` is used to indicate that the project specifies that it does not rely on funding.

#### Infrastructure

The technologies used to build the digital edition (Drupal, Omeka, MySQL, etc.). If multiple, please separate with a semicolon.

#### Current availability

Even if completed in the past, the digital edition is still viewable online today. The values `yes`(alive) and `no` (not available) are used.

#### Reviewed in RIDE

Was the edition reviewed in [RIDE](https://ride.i-d-e.de/), add the URL to the review or `no`

#### Sahle Catalog

Is the edition mentioned in [https://www.digitale-edition.de](https://www.digitale-edition.de) add the URL to the entry (e.g. https://digitale-edition.de/e862) or `no`

