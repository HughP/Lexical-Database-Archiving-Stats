# Formulas

Stats are not my strong point. I consulted with three friends *A, M, & Z* to look at which formulas to use. Here is what I decided in prose.

## The problem Statement
Paterson and Nordmoe (2013) made the following claim:
* SIL has nearly 80 years of history working with minority language communities. 
* About 1 million relevant non-digital objects are estimated to exists in SIL networks.
* About 50 million relevant digital objects are estimated to exist in SIL networks.

This claim was made solely on the bases of working with data in SIL International’s network of staff over the course of 4-5 years. An outstanding question remains: *Can the estimated ratio be applied more generally to all linguistic researchers, or is it subject to network constraints, and therefore limited to only SIL staff?*

I seek to answer the question: *is the volume of unarchived and endangered resources a localized behavioral attribute within a particular social network or is it a more general sociological phenomenon?*

Before asserting that the archiving behavior of linguists is dependent on specific factors such as project funding requirements, or social network affiliation (the Academy vs. NGO), an assessment needed to be made. My sampling methods attempted to included a cross-network sample of linguists and language program workers who may come from a variety of backgrounds including the Academy and a variety of NGOs. To test this hypothsis a single data type - the lexical dataset - was chose as “representative” of archive worthy documentary evidence. This follows argumentation in Woodbury 2003. [An online questionnaire was developed and a request for voluntary participation was sent to a variety of mailing lists](http://bit.ly/19QSPMb). **176 people responded**; indicating knowledge about **371 lexical data sets**. Of the respondents, **96 were SIL staff** and **80 were not affiliated with SIL**. Respondants were self selcted and therefore, I consider them random. An attempt was made to distribute the questionaire in places where people who belong to a variety of social networks would be given opportunity to respond, if they so chose. While it is technically possible to track participant responses based on individual links sent to a wide variety of people, no such technical tracking was employed.

Some respondents work in multiple languages and have access to multible lexical datasets. In these cases a new record was created for each lexical dataset. This means that some respondents contributed to the creation of new records than others. A breakdown is as follows:

Number of lexical database records provided | 1 | 2 | 3 | 4 | 6 | 7 | 10 | 12 | 15 | 21 | 31 | 37 | *105*
 ------------ | ------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
Number of Respondants | 135 | 18 | 8 | 4 | 1 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | *1*

## Formula for network equivlency hypothesis
Sent out a survey to several hundred people. On several mailing lists. Several hundred people (176) at last count, responded to several questions. 96 of these respondents were by SIL staff, while 80 respondents were by persons not affilitated with SIL.

 | SIL Staff | Other | **Totals**
 ------------ | ------------ | ------------- | -------------
Respondants | 96 | 80 | 176
Total lexical databses described by responses | 203 | 168 | 371
Number of lexical datasets from only respondents which were described as 'Archvied' | 63 | 38 | 101
Additional records found via OLAC | 4 | 18 | 22
Additional records found via SIL Catalogue | 81 | 2 | 83
New total number of lexical databases found | 288 | 188 | 476

##Discussion of the data

What if there is a lexical database in an archive but no-one responded about it?

Uses cases where a linguist may have already archived lexical data sets, but were disinclined to responded directly to the questionnaire were attempted to be included. On this account, three archives were contacted and given the opportunity to participate: ELAR/SOAS, PARADISEC, SIL International's Language & Culture Archive. Each archive declined to provide information, citing either: privacy concerns, lack of a detailed indexing procedures on curated archive holdings, or lack of staffing to sufficiently answer the question. All three archives suggested that the best results might be achieved through searches at OLAC - an aggregate records listing of participating language archives. Some 22 records were found via OLAC and included in the results. A manual tally of some 70 records of lexical databases in the SIL archive’s catalogue, not aggregated to OLAC, were also included. This bring the cumulative token count for lexical data sets to 476 tokens.


To test these two groups for equivlencies in the archiving behavioral responses I used
###Chi Square
To do this I used the chi sqhare test in python as described here: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.chisquare.html

###Prop Test
as described here: http://stattrek.com/hypothesis-test/difference-in-proportions.aspx
Comment: http://bit.ly/19QSPMb
