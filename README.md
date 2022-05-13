# SorseleSwedenCemeteries

## Description
A Python script for extracting data from the Sorsele-Måla, Västerbotten parish cemetery records that are hosted on [Gravar.se](http://gravar.se/en/forsamling/mala-sorsele-pastorat). The raw, uncleaned data are saved to .csv files in the /Indexes folder. This repository also includes a Jupyter Notebook for analyzing the data from a given cemetery.

Sorsele-Måla parish has eight cemeteries whose approximate locations (to the best of my knowledge) can be viewed on this [Google Earth map](https://earth.google.com/earth/d/1QPZnbVRg0kruSzYW14yilgplwl3TCC4i?usp=sharing):
* Adak Kyrkogård
* Ammarnäs Kyrkogård
* Gargnäs Kyrkogård
* Malå Gamla
* Skogskyrkogården
* Sorsele Gamla Kyrkogård
* Sorsele Skogskyrkogård
* Viktoriakyrkans Kyrkogård

## Dependencies:
* `numpy`
* `matplotlib`
* `lxml`
* `requests`
* `pandas`
* `datetime`




## Future ideas:
- [ ] Use the FamilySearch API to check each name for a FS profile
- [ ] Sorting within a block
- [ ] Extract first/middle/last names. Consider:
  - [ ] Case insensitive
  - [ ] Maiden/married names
  - [ ] Nicknames (in quotes)
  - [ ] Children (underage)
- [ ] Most common first/last names - `wordcloud` package
- [ ] Sort by burial site and see if the order tells me anything
- [ ] A list of incomplete/incorrect data to return to the parish
