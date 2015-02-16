#Hawai'i Data Folder
There are several sets of data outlined as follows:

* **Questionaire response data** - This data is collected via the google form at the following link: http://bit.ly/19QSPMb This must be anonymized before release, as indicated in the terms of collection. One portion of this data is accessible via: [*Data File 1.csv*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/Anonymized%20Participant%20data%20-%20(about%20data%20file%201).md)

* **ISO 639-3 data** - This data is openly avaible from the [ISO 639-3 Registrar](http://www2.sil.org/iso639-3/default.asp), but is replicated in this repo for consistency across papers and presentations. The orginal documents are presented in a folder titled: [*iso-639-3_Code_Tables_20140320*](https://github.com/HughP/Lexical-Database-Archiving-Stats/tree/master/2015-Hawaii/data/iso-639-3_Code_Tables_20140320). Additionally, a CSV file titled:[*iso-639-3_20140320.csv*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/iso-639-3_20140320.csv) is in the data folder and is an export of the table used to collate other data.

* **SIL.org data for GIS locations of languages**. This data was taken from SIL.org and was merged against ISO 639-3 tables.

A subset of the questionaire data should be made public and included in this project. However, as indicated above, the data yet needs to be anonymized as much as is possible, to comply with the terms under which it was collected. It is well known in both the linguistics and big-data communities anonomized data can usually be reconstructed to some degree given access and comparison to tertiary data sets. So, even my efforts may not completely obscure retraceable facts.

#Specific files
##Data File 1.csv

This is an anonymized list of participants and their answers. It has three columns:
* ParticipantID
* Group
* Behavior

ParticipantID is an anonymized version of the respondent's provided name or responseID, if no name was provided.
**Group** is either *SIL = 1*, or *other = 2*.
**Behavior** is either, the participant said they archived or not, with unknowns counting as not. Where *archived = 1* and *not archived = 2*. 
## iso-639-3_20140320.csv
This file is an export of the table used to collate other data. It is the ISO 639-3 Data which was current at the time of 2014/03/20.

##Map plot data
To plot the items on the map the union of several classes were formed. These unions were then each assigned a value 1-8 as is indicated in the following table. Due to the nature of the GIS data on hand, and the corespondences between the ISO and the SIL.org datasets, 17 lexical database records, which are identified by ISO language code are not represented on the map. Additionally, 12 Lexical datasets with the code [und] are not plotted. Non-plotted records are not indicated in the stats in the chart below.

Index Numeric | Quantitiy | Class
|----------|-----------|-----------|
1| 22 |SIL Archived Endangered
2| 24 |SIL not archived Endangered
3| 14 |Non-SIL Archived Endangered
4| 23 |Non-SIL Not Archived Endangered
5| 123 |SIL Archived Robust
6| 113 |SIL not archived Robust
7| 32 |Non-SIL Archived Robust
8| 94 |Non-SIL Not Archived Robust
