{r}
rm(list=ls())
#Test of equal or given proportions for SIL archived projects
# SIL_unarchive<-141
# SIL_archive<-134
# nonSIL_unarchive<-130
# nonSIL_archive<-58

# Create data.frame
SIL<-c(134,141)
nonSIL<-c(58,130)
df<-data.frame(rbind(SIL,nonSIL))
df
colnames(df)[colnames(df)=="X1"] <- "Archived"
colnames(df)[colnames(df)=="X2"] <- "Not_Archived"

prop.test(df$Archived, df$Not_Archived, conf.level=0.95, correct=TRUE)


# A 2-sample test for equality of proportions tests shows a significant difference between the proportion of archived SIL projects and the proportion of archived non-SIL projects that were surveyed, 
# The 95% confidence interval estimate of the difference between the proportion of archived SIL projects the proportion of archived non-SIL projects is between 40.4% and 60.4%.

# http://courses.washington.edu/stat217/APAstyle.html
# http://stattrek.com/hypothesis-test/difference-in-proportions.aspx