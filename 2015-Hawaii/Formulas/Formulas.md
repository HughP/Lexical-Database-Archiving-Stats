# Formulas

Stats are not my strong point. I consulted with three friends *A, M, & Z* to look at which formulas to use. Here is what I decided in prose.

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

To test these two groups for equivlencies in the archiving behavioral responses I used
##Chi Square
To do this I used the chi sqhare test in python as described here: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.chisquare.html

## Prop Test
as described here: http://stattrek.com/hypothesis-test/difference-in-proportions.aspx
