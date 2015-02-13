#Formulas used in the Hawai'i 2015 Poster/Presentation

Stats are not my strong point. I consulted with three friends *A, M, & Z* to look at which formulas to use. Here is what I decided in prose.

## The problem Statement
Paterson and Nordmoe (2013) made the following claim:
* SIL has nearly 80 years of history working with minority language communities. 
* About 1 million relevant non-digital objects are estimated to exists in SIL networks.
* About 50 million relevant digital objects are estimated to exist in SIL networks.

This claim was made solely on the bases of working with data in SIL International’s network of staff over the course of 4-5 years. An outstanding question remains: *Can the estimated ratio be applied more generally to all linguistic researchers, or is it subject to network constraints, and therefore limited to only SIL staff?*

I seek to answer the question: *is the volume of unarchived and endangered resources a localized behavioral attribute within a particular social network or is it a more general sociological phenomenon?*

Before asserting that the archiving behavior of linguists is dependent on specific factors such as project funding requirements, or social network affiliation (the Academy vs. NGO), an assessment needed to be made. My sampling methods attempted to included a cross-network sample of linguists and language program workers who may come from a variety of backgrounds including the Academy and a variety of NGOs. To test this hypothsis a single data type - the lexical dataset - was chose as “representative” of archive worthy documentary evidence. This follows argumentation in Woodbury 2003. [An online questionnaire was developed and a request for voluntary participation was sent to a variety of mailing lists](http://bit.ly/19QSPMb).

###Distribution of the respondants
**175 people responded**; indicating knowledge about **371 lexical data sets**, both archived and not archived. Of the respondents, **96 were SIL staff** and **79 were not affiliated with SIL**. Respondants were self selcted and therefore, I consider them random. An attempt was made to distribute the questionaire in places where people who belong to a variety of social networks would be given opportunity to respond, if they so chose ([see list](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/mailinglists.md)). While it is technically possible to track participant responses based on individual links sent to a wide variety of people, no such technological tracking was employed.

Some respondents work in multiple languages and have access to multible lexical datasets. In these cases a new record was created for each lexical dataset. This means that some respondents contributed to the creation of new records than others. A breakdown is as follows:

Number of lexical database records provided | 1 | 2 | 3 | 4 | 6 | 7 | 10 | 12 | 15 | 21 | 31 | 37 | *105*
 ------------ | ------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
Number of Respondants | 134 | 19 | 8 | 4 | 1 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | *1*
```Note 1: the final column with a count of 105 lexical database records representes the author's own investigation via OLAC and the SIL Language & Culture Archive catalogue.```

```Note 2: The difference between the numbers presented here veurses elsewhere (like Paterson 2014) is that these numbers include data collected in late 2014 and early 2015.```
##Discussion of the data
The collectted data is presented in the table below.

 | SIL Staff | Other | **Totals**
 ------------ | ------------ | ------------- | -------------
Respondants | 96 | 79 | 175
Total lexical databses described by responses | 203 | 168 | 371
Number of lexical datasets from only respondents which were described as 'Archvied' | 63 | 38 | 101
Additional records found via OLAC | 4 | 18 | 22
Additional records found via SIL Catalogue | 81 | 2 | 83
New total number of lexical databases found | 288 | 188 | 476

In the virst row we have the total number of respondants. In the second row we have the totals of the numbers of lexial databases each sub-segment of the total population of respondents provided data for, or about. The third row of the table describes how many of the total number of lexical databases mentioned were claimed to be *archived*.

However, a secondary question quicky arises. While the questionaire focuses on asking current (and living) respondents if they have archived, the questionaire fails to capture an assement of what has already been successfully archived, but is not accounted for in responses. I phrase the question as the following: *What if there is a lexical database in an archive but no-one responded about it?*

Uses cases where a linguist may have already archived lexical data sets, but were disinclined to responded directly to the questionnaire were attempted to be accounted for, but for the sake of clarity these numbers should be presented independently from responses to the questionaire. On account of this second kind of use case, three archives were contacted and given the opportunity to participate: 
* ELAR/SOAS
* PARADISEC
* SIL International's Language & Culture Archive

Each archive declined to provide information, citing either: *privacy concerns*, *lack of a detailed indexing procedures on curated archive holdings*, or *lack of staffing to sufficiently answer the question*. All three archives suggested that the best results might be achieved through searches at [OLAC - an aggregate records listing of participating language archives](http://search.language-archives.org/index.html). Some 22 records were found via OLAC and included in the results on row four in the table above. A manual tally of some 81 records of lexical databases in the SIL archive’s catalogue, not aggregated to OLAC, were also included. This brings the cumulative token count for lexical data sets to 476 tokens. However, there is cause for caution in the tabulation of the records discovered via the SIL Language & Culture Archive catalogue. The author does have access to this catalogue in ways that the author does not have access to catalogues at other institutions. And even though the SIL Archive staff delcined to formally assist, some manual work did yelid a significant token number of results. Therefore, it is possible that adding these additional tokens would unfairly present the situation as it more generally occurs, because the author has not been able equaly assess the contents of other well established and respected archvies such as ELAR, ALLIA, or TLA/DoBeS. The reasons for this inequality are discussed in a later section.

## Formula for network equivlency hypothesis
To return to the thesis and the open question on hand, *Can the estimated ratio be applied more generally to all linguistic researchers, or is it subject to network constraints, and therefore limited to only SIL staff?* we need to compare the two sub-populations by their respective responses. This should tell us if we should suspect similar behaviors, attitudes, and practices more generally across the whole population or if these atributes as culminating in the act of archiving are more prone to occurre in one of the two sub-sections of the population.

To acomplish the comparison statistical analysis I have applied two statsitical tests to only the responses recived and not the additional tokens discovered through OLAC and the Language & Culture Archive catalogue.

###Chi Square
To do this I used the chi sqhare test in python as described here: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.chisquare.html
This test was run on [Data File 1](https://github.com/HughP/Lexical-Database-Archiving-Stats/blob/master/2015-Hawaii/data/Anonymized%20Participant%20data%20-%20(about%20data%20file%201).md).

###Prop Test
as described here: http://stattrek.com/hypothesis-test/difference-in-proportions.aspx
