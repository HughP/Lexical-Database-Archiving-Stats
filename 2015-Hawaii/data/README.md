#Hawai'i Data Folder
There are several sets of data outlined as follows:

* **Questionnaire response data** - This data is collected via the Google form at the following link: http://bit.ly/19QSPMb This must be anonymized before release, as indicated in the terms of collection. One portion of this data is accessible via: [*Data File 1.csv*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/Anonymized%20Participant%20data%20-%20(about%20data%20file%201).md)

* **ISO 639-3 data** - This data is openly available from the [ISO 639-3 Registrar](http://www2.sil.org/iso639-3/default.asp), but is replicated in this repo for consistency across papers and presentations. The original documents are presented in a folder titled: [*iso-639-3_Code_Tables_20140320*](https://github.com/HughP/Lexical-Database-Archiving-Stats/tree/master/2015-Hawaii/data/iso-639-3_Code_Tables_20140320). Additionally, a CSV file titled:[*iso-639-3_20140320.csv*](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/iso-639-3_20140320.csv) is in the data folder and is an export of the table used to collate other data.

* **SIL.org data for GIS locations of languages**. This data was taken from SIL.org and was merged against ISO 639-3 tables.

A subset of the questionnaire data should be made public and included in this project. However, as indicated above, the data yet needs to be anonymized as much as is possible, to comply with the terms under which it was collected. It is well known in both the linguistics and big-data communities anonymized data can usually be reconstructed to some degree given access and comparison to tertiary data sets. So, even my efforts may not completely obscure retraceable facts.

#Data Management and Workflow Documentation

##FLEx Archiving responses (managed in GoogleDocs) (#1, #2, #3 etc.)

Documents discussed:
* FLEx Archiving responses: https://docs.google.com/spreadsheets/d/1ATDdKbtBjJfGH1Nk-3IVnEUD807QU1S74jwk1WIJosE/edit#gid=0
* Web form: https://docs.google.com/forms/d/101lf-QCLdt64s8e6KIsHluG1f4NGnng3y-U5WdDcjd0/edit
* FLEx Archiving responses #2: https://docs.google.com/spreadsheet/ccc?key=0AlihlYd_UNoWdERtTXFxcW9HX3ZvZWpXRWdVVVJQV0E&usp=drive_web&pli=1#gid=0 

FLEx Archiving responses is a Google Spreadsheet. It was the first spreadsheet that the Google form was attached to. It was detached from the online form and FLEx Archiving responses #2 was attached to the form. On 04. February 2015 Hugh manually compared the data and #2 had data which the #1 did not have, and #1 had data which the #2 did not have. It looks like number #1 is a copy from an earlier date and then items mailed in were merged into the #1, meanwhile #2 continued to receive new entries from the web form.

It was standard procedure to download these spreadsheets and to work on them in Apple Numbers. Prior to learning to use Python to manipulate data.

On 05. February 2015 all content from FLEx Archiving responses #2: was validated to be in the Numbers spreadsheet.
On 05. February 2015 all emailed entries were resolved.
On 05. February 2015 all content from FLEx Archiving responses was validated to be in the numbers spreadsheet.
On 08. February 2015 it was discovered that some respondents would reply some months later and respond to say that they had archived their lexical datasets. These records are generally consolidated in favor of the most recent record. 
On 12. February 2015 the live sheet was moved to https://docs.google.com/spreadsheets/d/1IVJ1xAbC0Kp4DNJBNmuEVlVMEsbjqmCvMMSWHuPwK14/edit?usp=sharing or Response sheet #3 in preparation for Hawaii 2015.

##Merge Data sets
Early in the project before Python skills were being developed, Google FusionTables was used to align various information about languages and lexical database records.
Data sets and documents discussed:

**iso-639-3_20140320**
Location: https://www.google.com/fusiontables/DataSource?docid=1RLu37yB_CygIGp0xegfVxcDRlFuS68WQgRYx6fyN 
On 14 May 2014 the ISO 639-3 code tables were downloaded from source and uploaded to a Google Fusion table document called iso-639-3_20140320.

**Location dots of languages from SIL.org**
Location: https://www.google.com/fusiontables/DataSource?docid=1gRLwL-sEnZOrdCwTmFpCxrVIM20gIelU4OETVb5o#rows:id=1
On 14 may 2014 Language dots (locations) were collected from SIL.org and condensed down to coordinates and ISO 639-3 codes. This was then put in a file called Location dots of languages from SIL.org.

**Merge of iso-639-3_20140320 and Location dots of languages from SIL.org**
Location: https://www.google.com/fusiontables/DataSource?docid=1v8P-bj-FnvJim5V6xRDvFCUEOZrnbZ1ESvzFz5EH
These first two documents, Location dots of languages from SIL.org and iso-639-3_20140320 were then merged along the ISO 639-3 code column. to create a new table called Merge of iso-639-3_20140320 and Location dots of languages from SIL.org

Content from the FLEx archiving responses was analyzed in Apple Numbers. Then exported as a .csv and uploaded to Google FusionTables.

**From Numbers**
This file is the export from Numbers to Google Fusion Table

**Merge of From Numbers and Merge of iso-639-3_20140320 and Location dots of languages from SIL.org**
A Merge of the previously combined ISO and SIL data was combined with the FLEx archiving data from numbers: 

#Specific files used in the projet
##MasterDataFile
This datafile is not currently publicly available due to confidentiality constraints.

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
