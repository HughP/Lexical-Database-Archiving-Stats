#The Goal of this script is to give counts from the growing dataset related to archving lexical data sets. Started on 17. February 2015 by Hugh Paterson III. For archival purposes I need to indicate which version of python I am using (python 2.7.9 on OSX 10.9.5 via Homebrew), and what moduels I call and use (pandas (version) matplotlib (version) basemap 1.0.7.

#How should I name my variables? by project relevance or semantic relevance or arbitrary? Should I create a bunch of interrelated scripts or should I create a single script?


import pandas

#This line imports the CSV file to pandas and converts the CSV format to a dataframe
df = pandas.read_csv('datasets/language_plot.csv')

#In the data file currently in use, the titles in the header row contain titles with spaces. This is evidently not allowed. Therefore the titles with spaces are retitled (for processing) with titles without spaces in the name.
df = df.rename(columns = {'Ethnologue Status' : 'EthStatus'})

# All the data from the CSV is in a single dataframe. Now I can do something with that data if I want. (such as filter and count tokens).

#To effectivly move forward I need to give every column in my data a single word title without spaces. I then need an index of why each column was created or the kind of data used.

#There are several things about the data set that I need to count. 

#The first thing I need to count is the total number of records collected. Since every record should have a method attached to it about how I recived the record I will count the number of items in the column  ''.

#Another thing I need to count is the total numger of records I have collected by collection method. So on the same column I need a count of the quantitiy of each unique value along with a list of each unique value.

#The next thing I need to count is the total number of responents. I should be able to do this via the column ''. However, if the coumn is empty then I need to add the value 'anonymous+ID' where the ID is a consecutive numeric.

#Following this I need to add a column with the value of the anonymized particiapnt in the form of 'ParticipantID'. This needs to be added in the column ''. There needs to be a check to see if this ID already exists.


#Sometimes I need to be able to return the entire row of a set of data based on a response to a column query.

##df.<column name>.value_counts() is the funtion which gives me the counts of a particualr items in column


#I need to count is the number in each class of the data on hand. This is for plotting purposes on the map. Note that variables j & k have not yet been implimented because they need to account for data which is not present and I am not sure how to do this yet.
a = len(df.Group[df.Group == 1][df.Behavior == 1][df.EthStatus == 'Endangered'])
b = len(df.Group[df.Group == 1][df.Behavior == 2][df.EthStatus == 'Endangered'])
c = len(df.Group[df.Group == 2][df.Behavior == 1][df.EthStatus == 'Endangered'])
d = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Endangered'])
e = len(df.Group[df.Group == 1][df.Behavior == 1][df.EthStatus == 'Robust'])
f = len(df.Group[df.Group == 1][df.Behavior == 2][df.EthStatus == 'Robust'])
g = len(df.Group[df.Group == 2][df.Behavior == 1][df.EthStatus == 'Robust'])
h = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust'])
#j = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust']) This needs to count the projects where there is no status on the ISO 639-3 code because the status is not carried over from the SIL.org data. The data is likely refrenceable directly via the Ethnologue, but the Coordinates are not avalible. 
#k = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust']) This needs to search the column of the iso 639-3 code set and look for [und] and then count them

a_h_sum = a + b + c + d + e + f + g + h #+ j + k




	SIL Staff	Other	Totals
Respondants	96	79	175
Total lexical databses described by responses	203	168	371
Number of lexical datasets from only respondents which were described as 'Archvied'	63	38	101
Additional records found via OLAC	4	18	22
Additional records found via SIL Catalogue	81	2	83
New total number of lexical databases found	288	188	476



#My print Statements are not working yet
print('SIL Staff Archived Endangered:', a ,b,c)
#print("SIL Staff Archived Endangered" a '\n',"SIL Staff Not-archived Endangered" b '\n',"Other Archived Endangered" c '\n',"Other Not-archived Endangered" d '\n',"SIL Staff Archived Robust" e '\n',"SIL Staff Not-archived Robust" f '\n',"Other Archived Robust" g '\n',"Other Not-archived Robust" h '\n', "Total number of records", a_h_sum)

#plt.legend(proxy,"range(1-2)",)