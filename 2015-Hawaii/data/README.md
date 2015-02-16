#Data
There are several sets of data outlined as follows:
* **Archive specific data from SIL International** - This is corporation specific and confidential data and can not be released, but can be discussed in general terms. This data is only used in Paterson & Nordmoe.

* **Questionaire response data** - This data is collected via the google form at the following link: http://bit.ly/19QSPMb This must be anonymized before release, as indicated in the terms of collection. One portion of this data is accessible via: [*Data File 1*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/Anonymized%20Participant%20data%20-%20(about%20data%20file%201).md)

* **ISO 639-3 data** - This data is openly avaible from the [ISO 639-3 Registrar](http://www2.sil.org/iso639-3/default.asp), but is replicated in this repo for consistency across papers and presentations. The orginal documents are presented in a folder titled: [*iso-639-3_Code_Tables_20140320*](https://github.com/HughP/Lexical-Database-Archiving-Stats/tree/master/2015-Hawaii/data/iso-639-3_Code_Tables_20140320). Additionally, a CSV file titled:[*iso-639-3_20140320.csv*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/iso-639-3_20140320.csv) is in the data folder and is an export of the table used to collate other data.

* **SIL.org data for GIS locations of languages**. This data was taken from SIL.org and was merged against ISO 639-3 tables.

A subset of the questionaire data should be made public and included in this project. However, as indicated above, the data yet needs to be anonymized as much as is possible, to comply with the terms under which it was collected. It is well known in both the linguistics and big-data communities anonomized data can usually be reconstructed to some degree given access and comparison to tertiary data sets. So, even my efforts may not completely obscure retraceable facts.

#Specific files
##Data File 1

This is an anonymized list of paticiapnts and their answers. It has three columns:
* ParticipantID
* Group
* Behavior

ParticipantID is an anonymized version of the respondent's provided name or responseID, if no name was provided.
**Group** is either *SIL = 1*, or *other = 2*.
**Behavior** is either, the participant said they archived or not, with unknowns counting as not. Where *archived = 1* and *not archived = 2*. 
