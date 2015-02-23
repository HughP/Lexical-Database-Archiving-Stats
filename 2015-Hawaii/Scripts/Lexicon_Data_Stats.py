#################### PURPOSE ##########################
#The Goal of this script is to give counts from the growing dataset related to archving lexical data sets. Started on 17. February 2015 by Hugh Paterson III. For archival purposes I need to indicate which version of python I am using (python 2.7.9 on OSX 10.9.5 via Homebrew), and what modules I call and use (pandas (0.15.2) matplotlib (1.4.2) basemap (1.0.7.))
#######################################################

############# STRUCTURE QUESTIONS #####################
#How should I name my variables? by project relevance or semantic relevance or arbitrary? - I am moving towards semantic relevance.
#Should I create a bunch of interrelated scripts or should I create a single script? - I am moving towards a single script.
#######################################################


import pandas
import scipy.stats as stats
#This line imports the CSV file to pandas and converts the CSV format to a dataframe. Pandas skips two other header rows which are in the dataset for other purposes.
df = pandas.read_csv('Master_Data.csv', skiprows=[1,2])
# All the data from the CSV is in a single dataframe. Now I can do something with that data if I want (such as filter and count tokens).


################ DATAFRAME NOTES #######################
#Every column in the data has a single word title without spaces. This was done by adding an extra header row in the dataset (pandas index 0). 

#ISO_639-3_code	Variety_Name	Timestamp	Application	FLEx_Version	LXDBSolution	Email	LXDBCreator	LXDBRecordProvider	ParticipantID	SILProject	Group	Split_help	Response_archive_status	Behavior	SC1	Institution	TAPS	SC2	WasObjectTrue	SC3	CorrectREAP	WasLXDB	SC4	GoodDescription	SC5	MisPerception	Response_comment	Print_status	entries_quantity	Last_update	Method_Received	Public_URL	Private_URL	Part2B	Part2T	Part1	Scope	Language_Type	Ref_Name	Comment	Graphic_Type	Latitude	Longitude	Language_Link	Language_Name	Apostrophe	leaflet_id	Radius	Color	EthStatus	Union	hex_color	Weight	Opacity	FillOpacity

#Column headings can not have dashes so I renamed the column to work in pandas/python.
df = df.rename(columns = {'ISO_639-3_code' : 'ISO639', })
#######################################################


############### THINGS TO COUNT #######################
#There are several things about the data set that I need to count.
# 1. TOTAL NUMBER OF RECORDS COLLECTED
# 2. TOTAL RECORDS BY COLLECTION METHOD
# 3. TOTAL RESPONSES
# 4. TOTAL RESPONDENTS
# 5. STOP CLASSES IN TREE
# 6. COMPUTE FISHER EXACT TEST
# 7. COMPUTE PERCENTAGES
#######################################################

######## TOTAL NUMBER OF RECORDS COLLECTED ############
#The first thing I need to count is the total number of records collected. Since every record should have a method attached to it about how I recived the record I will count the number of items in the column 'Method_Received'.
#Total number of records in the dataset based on the the premise that each record's counts will track how it was collected. 
Sum_Received = df.Method_Received.count() -1 ###!!! Currently this number is 1 too high. Is this counting including the index 0 row?
#print "Total number of records", Sum_Received, "\n"
######################################################


######## TOTAL RECORDS BY COLLECTION METHOD ##########
#Another thing I need to count is the total numger of records I have collected by collection method. So on the same column I need a count of the quantitiy of each unique value along with a list of each unique value.

#Total number of items in the dataset by method received
Totals_Received = df.Method_Received.value_counts()
######################################################

################# EDGE CASE METHODS ##################
#Total Records by Collection shows that there are two instances of edgecase collection methods. One of these is "personal question" This one happens to be non-SIL/Other.
Personal_Question = len(df.Group[df.Method_Received == 'Personal Question'])
Online_Search = Personal_Question = len(df.Group[df.Method_Received == 'Online Search']) 
######################################################



################### TOTAL RESPONSES ##################
#Total number of records from respondents.

#Total number of records created from Responses (Mailed in + Online survey)
Total_Responses = len(df.Group[df.Method_Received == 'Online Survey From']) + len(df.Group[df.Method_Received == 'Mailed in']) + Personal_Question # The +1 is for personal face to face question asking.

SIL_Responses = len(df.Group[df.Group == 1][df.Method_Received == 'Online Survey From']) + len(df.Group[df.Group == 1][df.Method_Received == 'Mailed in'])
Other_Responses = len(df.Group[df.Group == 2][df.Method_Received == 'Online Survey From']) + len(df.Group[df.Group == 2][df.Method_Received == 'Mailed in']) + Personal_Question

#print "Breakdown of how records were created:" "\n", Totals_Received
######################################################


#The next thing I need to count is the total number of responents. The column to look at is 'LXDBRecordProvider'. However, this column is optional in the Google Form. This means that some data may be NaN. Currently exsiting data has been hand curated to fix missing or NaN data. However, for ongoing data crunching this needs to be automated.  The way to solve this is to say: if the column is empty then add the value 'anonymous+ID' where the ID is a consecutive numeric.

#Following this I need to add a column with the value of the anonymized particiapnt in the form of 'ParticipantID'. This needs to be added in the column 'ParticipantID'. There needs to be a check to see if this ID already exists. Idealy the 'ParticipantID' column would be generated on the fly each time.

################### TOTAL RESPONDENTS ################
Total_Respondents = len(df.ParticipantID.value_counts()) - 1 # This counts all participants. However, the researcher is also one of the participants. Therefore to caculate all respondants, the total minus the researcher is caculated. The researcher is Hugh Paterson III.
Total_RecordProviders = len(df.LXDBRecordProvider.value_counts())
List_RecordProviders = df.LXDBRecordProvider.value_counts()
	
#SIL_Respondents = len(df.Group[df.SILProject == 'SIL']) #This line as it is written does not account for less than only one of eachkind in the ParticipantID
print "ABOUT RESPONDENTS""\n"
print "Total Respondents:", Total_Respondents, "\n"
print "Total Record Providers:", Total_RecordProviders, "\n"
print "List Total_RecordProviders:" "\n", List_RecordProviders, "\n" #Why does this list clip to the top and the bottom 12 each?
#print "SIL Respondents:", SIL_Respondents, "\n"
######################################################


############# COMPUTE CLASSES FOR WORLD MAP #############
#I need to count is the number in each class of the data on hand. This is for plotting purposes on the map. Note that variables j have not yet been implimented because they need to account for data which is not present and I am not sure how to do this yet.
SIL_Archived_Endangered = len(df.Group[df.Group == 1][df.Behavior == 1][df.EthStatus == 'Endangered'])
SIL_NotArchived_Endangered = len(df.Group[df.Group == 1][df.Behavior == 2][df.EthStatus == 'Endangered'])
Other_Archived_Endangered = len(df.Group[df.Group == 2][df.Behavior == 1][df.EthStatus == 'Endangered'])
Other_NotArchived_Endangered = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Endangered'])
SIL_Archived_Robust = len(df.Group[df.Group == 1][df.Behavior == 1][df.EthStatus == 'Robust'])
SIL_NotArchived_Robust = len(df.Group[df.Group == 1][df.Behavior == 2][df.EthStatus == 'Robust'])
Other_Archived_Robust = len(df.Group[df.Group == 2][df.Behavior == 1][df.EthStatus == 'Robust'])
Other_NotArchived_Robust = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust'])
#j = df.Group([EthStatus]).isnull().sum() # This needs to count the projects where there is no status on the ISO 639-3 code because the status is not carried over from the SIL.org data. The data is likely refrenceable directly via the Ethnologue, but the Coordinates are not avalible. 
Undetermined_languages = len(df.Group[df.ISO639 == 'und']) #This needs to search the column of the iso 639-3 code set and look for [und] and then count them

a_h_sum = SIL_Archived_Endangered + SIL_NotArchived_Endangered + Other_Archived_Endangered + Other_NotArchived_Endangered + SIL_Archived_Robust + SIL_NotArchived_Robust + Other_Archived_Robust + Other_NotArchived_Robust + Undetermined_languages #+ j

#Now I need to count and breakdown these items but only the ones which are from responses.
Response_SIL_Archived_Endangered = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.Behavior == 1][df.EthStatus == 'Endangered']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.Behavior == 1][df.EthStatus == 'Endangered'])
Response_SIL_NotArchived_Endangered = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.Behavior == 2][df.EthStatus == 'Endangered']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.Behavior == 2][df.EthStatus == 'Endangered'])
Response_Other_Archived_Endangered = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.Behavior == 1][df.EthStatus == 'Endangered']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.Behavior == 1][df.EthStatus == 'Endangered'])
Response_Other_NotArchived_Endangered = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.Behavior == 2][df.EthStatus == 'Endangered']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.Behavior == 2][df.EthStatus == 'Endangered'])
Response_SIL_Archived_Robust = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.Behavior == 1][df.EthStatus == 'Robust']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.Behavior == 1][df.EthStatus == 'Robust'])
Response_SIL_NotArchived_Robust = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.Behavior == 2][df.EthStatus == 'Robust']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.Behavior == 2][df.EthStatus == 'Robust'])
Response_Other_Archived_Robust = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.Behavior == 1][df.EthStatus == 'Robust']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.Behavior == 1][df.EthStatus == 'Robust'])
Response_Other_NotArchived_Robust = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust']) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust'])
#j = len(df.Group[df.Group == 2][df.Behavior == 2][df.EthStatus == 'Robust']) This needs to count the projects where there is no status on the ISO 639-3 code because the status is not carried over from the SIL.org data. The data is likely refrenceable directly via the Ethnologue, but the Coordinates are not avalible. 
Response_Undetermined_languages = len(df.Group[df.Method_Received == 'Online Survey From'][df.ISO639 == 'und']) + len(df.Group[df.Method_Received == 'Mailed in'][df.ISO639 == 'und'])

Response_a_h_sum = Response_SIL_Archived_Endangered + Response_SIL_NotArchived_Endangered + Response_Other_Archived_Endangered + Response_Other_NotArchived_Endangered + Response_SIL_Archived_Robust + Response_SIL_NotArchived_Robust + Response_Other_Archived_Robust + Response_Other_NotArchived_Robust + Response_Undetermined_languages # + j
######################################################


################ STOP CLASSES IN TREE ######################
#Where are we here?

#Stop Class 1

Claims_Responses_Archvied_2_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC1 == 2]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC1 == 2])
Claims_Responses_Archived_2_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC1 == 2]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC1 == 2])
Claims_Responses_Archived_2_Total = Claims_Responses_Archvied_2_SIL + Claims_Responses_Archived_2_Other

Claims_Responses_NotArchived_1_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC1 == 1]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC1 == 1])
Claims_Responses_NotArchived_1_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC1 == 1]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC1 == 1])
Claims_Responses_NotArchived_1_Total = Claims_Responses_NotArchived_1_SIL + Claims_Responses_NotArchived_1_Other

Claims_Responses_UnknownArchived_3_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC1 == 3]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC1 == 3])
Claims_Responses_UnknownArchived_3_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC1 == 3]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC1 == 3])
Claims_Responses_UnknownArchived_3_Total = Claims_Responses_UnknownArchived_3_SIL + Claims_Responses_UnknownArchived_3_Other
print "Responses marked 'Archived':", Claims_Responses_Archived_2_Total, "; of those", Claims_Responses_Archvied_2_SIL, "were from SIL, while", Claims_Responses_Archived_2_Other, "were from others."

#Stop Class 1 Totals

Claims_Archvied_2_SIL = len(df.Group[df.Group == 1][df.SC1 == 2])
Claims_Archived_2_Other = len(df.Group[df.Group == 2][df.SC1 == 2])
Claims_Archived_2_Total = Claims_Archvied_2_SIL + Claims_Archived_2_Other

Claims_NotArchived_1_SIL = len(df.Group[df.Group == 1][df.SC1 == 1])
Claims_NotArchived_1_Other = len(df.Group[df.Group == 2][df.SC1 == 1])
Claims_NotArchived_1_Total = Claims_NotArchived_1_SIL + Claims_NotArchived_1_Other

Claims_UnknownArchived_3_SIL = len(df.Group[df.Group == 1][df.SC1 == 3])
Claims_UnknownArchived_3_Other = len(df.Group[df.Group == 2][df.SC1 == 3])
Claims_UnknownArchived_3_Total = Claims_UnknownArchived_3_SIL + Claims_UnknownArchived_3_Other
print "Of all,", Sum_Received, "records in the dataset,", Claims_Archived_2_Total, "are marked 'Archived'; of those", Claims_Archvied_2_SIL, "were from SIL, while", Claims_Archived_2_Other, "were from others."
print "Of all,", Sum_Received, "records in the dataset,", Claims_NotArchived_1_Total, "are marked 'Not Archived'; of those", Claims_NotArchived_1_SIL, "were from SIL, while", Claims_NotArchived_1_Other, "were from others."
print "Of all,", Sum_Received, "records in the dataset,", Claims_UnknownArchived_3_Total, "are marked 'Unknown Archived'; of those", Claims_UnknownArchived_3_SIL, "were from SIL, while", Claims_UnknownArchived_3_Other, "were from others."

x = Claims_Archived_2_Total + Claims_NotArchived_1_Total + Claims_UnknownArchived_3_Total
print(x)


#Stop Class 2 (Formerly known as TAPS) SC2

Archive_Location_Responses_Yes_4_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC2 == 4]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC2 == 4])
Archive_Location_Responses_Yes_4_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC2 == 4]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC2 == 4])
Archive_Location_Responses_Yes_4_Total = Archive_Location_Responses_Yes_4_SIL + Archive_Location_Responses_Yes_4_Other

Archive_Location_Responses_No_5_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC2 == 5]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC2 == 5])
Archive_Location_Responses_No_5_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC2 == 5]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC2 == 5])
Archive_Location_Responses_No_5_Total = Archive_Location_Responses_No_5_SIL + Archive_Location_Responses_No_5_Other

#Stop Class 2 Totals (Formerly known as TAPS)

Archive_Location_Yes_4_SIL = len(df.Group[df.Group == 1][df.SC2 == 4])
Archive_Location_Yes_4_Other = len(df.Group[df.Group == 2][df.SC2 == 4])
Archive_Location_Yes_4_Total = Archive_Location_Yes_4_SIL + Archive_Location_Yes_4_Other

Archive_Location_No_5_SIL = len(df.Group[df.Group == 1][df.SC2 == 5])
Archive_Location_No_5_Other = len(df.Group[df.Group == 2][df.SC2 == 5])
Archive_Location_No_5_Total = Archive_Location_No_5_SIL + Archive_Location_No_5_Other


#Stop Class 3

Item_Existance_Verification_Responses_Yes_6_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC3 == 6]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC3 == 6])
Item_Existance_Verification_Responses_Yes_6_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC3 == 6]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC3 == 6])
Item_Existance_Verification_Responses_Yes_6_Total = Item_Existance_Verification_Responses_Yes_6_SIL + Item_Existance_Verification_Responses_Yes_6_Other

Item_Existance_Verification_Responses_No_7_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC3 == 7]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC3 == 7])
Item_Existance_Verification_Responses_No_7_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC3 == 7]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC3 == 7])
Item_Existance_Verification_Responses_No_7_Total = Item_Existance_Verification_Responses_No_7_SIL + Item_Existance_Verification_Responses_No_7_Other


#Stop Class 3 Totals

Item_Existance_Verification_Yes_6_SIL = len(df.Group[df.Group == 1][df.SC3 == 6])
Item_Existance_Verification_Yes_6_Other = len(df.Group[df.Group == 2][df.SC3 == 6])
Item_Existance_Verification_Yes_6_Total = Item_Existance_Verification_Yes_6_SIL + Item_Existance_Verification_Yes_6_Other

Item_Existance_Verification_No_7_SIL = len(df.Group[df.Group == 1][df.SC3 == 7])
Item_Existance_Verification_No_7_Other = len(df.Group[df.Group == 2][df.SC3 == 7])
Item_Existance_Verification_No_7_Total = Item_Existance_Verification_No_7_SIL + Item_Existance_Verification_No_7_Other

#Stop Class 4

Thingness_Lxdb_Responses_Yes_8_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC4 == 8]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC4 == 8])
Thingness_Lxdb_Responses_Yes_8_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC4 == 8]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC4 == 8])
Thingness_Lxdb_Responses_Yes_8_Total = Thingness_Lxdb_Responses_Yes_8_SIL + Thingness_Lxdb_Responses_Yes_8_Other

Thingness_Lxdb_Responses_No_9_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC4 == 9]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC4 == 9])
Thingness_Lxdb_Responses_No_9_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC4 == 9]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC4 == 9])
Thingness_Lxdb_Responses_No_9_Total = Thingness_Lxdb_Responses_No_9_SIL + Thingness_Lxdb_Responses_No_9_Other

#Stop Class 4 Totals

Thingness_Lxdb_Yes_8_SIL = len(df.Group[df.Group == 1][df.SC4 == 8])
Thingness_Lxdb_Yes_8_Other = len(df.Group[df.Group == 2][df.SC4 == 8])
Thingness_Lxdb_Yes_8_Total = Thingness_Lxdb_Yes_8_SIL + Thingness_Lxdb_Yes_8_Other

Thingness_Lxdb_No_9_SIL = len(df.Group[df.Group == 1][df.SC4 == 9])
Thingness_Lxdb_No_9_Other = len(df.Group[df.Group == 2][df.SC4 == 9])
Thingness_Lxdb_No_9_Total = Thingness_Lxdb_No_9_SIL + Thingness_Lxdb_No_9_Other

#Stop Class 5

Good_Description_Lxdb_Responses_Yes_10_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC5 == 10]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC5 == 10])
Good_Description_Lxdb_Responses_Yes_10_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC5 == 10]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC5 == 10])
Good_Description_Lxdb_Responses_Yes_10_Total = Good_Description_Lxdb_Responses_Yes_10_SIL + Good_Description_Lxdb_Responses_Yes_10_Other

Good_Description_Lxdb_Responses_No_11_SIL = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 1][df.SC5 == 11]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 1][df.SC5 == 11])
Good_Description_Lxdb_Responses_No_11_Other = len(df.Group[df.Method_Received == 'Online Survey From'][df.Group == 2][df.SC5 == 11]) + len(df.Group[df.Method_Received == 'Mailed in'][df.Group == 2][df.SC5 == 11])
Good_Description_Lxdb_Responses_No_11_Total = Good_Description_Lxdb_Responses_No_11_SIL + Good_Description_Lxdb_Responses_No_11_Other

#Stop Class 4 Totals

Good_Description_Lxdb_Yes_10_SIL = len(df.Group[df.Group == 1][df.SC5 == 10])
Good_Description_Lxdb_Yes_10_Other = len(df.Group[df.Group == 2][df.SC5 == 10])
Good_Description_Yes_10_Total = Good_Description_Lxdb_Yes_10_SIL + Good_Description_Lxdb_Yes_10_Other

Good_Description_Lxdb_No_11_SIL = len(df.Group[df.Group == 1][df.SC5 == 11])
Good_Description_Lxdb_No_11_Other = len(df.Group[df.Group == 2][df.SC5 == 11])
Good_Description_Lxdb_No_11_Total = Good_Description_Lxdb_No_11_SIL + Good_Description_Lxdb_No_11_Other

######################################################

############# COMPUTE FISHER EXACT TEST ###############
#Why --> V.s up down? http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.fisher_exact.html
pvalue = stats.fisher_exact([[8, 2], [1, 5]])
print("Fishers Exact p Value:", pvalue)

######################################################

############### COMPUTE PERCENTAGES ##################


######################################################

########## DATA SUMMARY FOR COMPARISON ###############

#	SIL Staff	Other	Totals
#Respondants	96	79	175
#Total lexical databses described by responses	203	168	371
#Number of lexical datasets from only respondents which were described as 'Archived'	63	38	101
#Additional records found via OLAC	4	18	22
#Additional records found via SIL Catalogue	81	2	83
#New total number of lexical databases found	288	188	476
######################################################

############### PRINT SECTION ON RESPONSES ##############
print "ABOUT RESPONSES""\n"
print "SIL Responses described:", SIL_Responses, "Lexical databases.", "\n"
print "Other Responses described:", Other_Responses, "Lexical databases.","\n"
print "Total Responses:", Total_Responses, "\n"
print "\n" "Total Responses Check:", (SIL_Responses+Other_Responses), "\n"
######################################################

############### PRINT SECTION ON RECORDS ##############

print "ABOUT RECORDS""\n"
print "Breakdown of how records were created:" "\n", Totals_Received
print "Total number of records", Sum_Received, "\n"
######################################################


############### PRINT SECTION COMPARISON ON ENDANGERED LANGUAGES ##############

#My print Statements are not working yet
print "\n" "A Summary of ALL the items found:" "\n"
print "SIL Staff Archived Endangered:", SIL_Archived_Endangered, "\n","SIL Staff Not-archived Endangered:", SIL_NotArchived_Endangered,"\n","Other Archived Endangered:", Other_Archived_Endangered,"\n", "Other Not-archived Endangered:", Other_NotArchived_Endangered,"\n", "SIL Staff Archived Robust:", SIL_Archived_Robust, "\n", "SIL Staff Not-archived Robust:", SIL_NotArchived_Robust,"\n", "Other Archived Robust:", Other_Archived_Robust, "\n", "Other Not-archived Robust:", Other_NotArchived_Robust, "\n", "Records not countable by language (no ISO code):", Undetermined_languages, "\n", "All quantities:", a_h_sum
#print "something", j
#Print only the items which are from resonses
print "\n" "A Summary of only the items returned via responses (Mailed in and Online survey):" "\n"
print "SIL Staff Archived Endangered:", Response_SIL_Archived_Endangered, "\n","SIL Staff Not-archived Endangered:", Response_SIL_NotArchived_Endangered,"\n","Other Archived Endangered:", Response_Other_Archived_Endangered,"\n", "Other Not-archived Endangered:", Response_Other_NotArchived_Endangered,"\n", "SIL Staff Archived Robust:", Response_SIL_Archived_Robust, "\n", "SIL Staff Not-archived Robust:", Response_SIL_NotArchived_Robust,"\n", "Other Archived Robust:", Response_Other_Archived_Robust, "\n", "Other Not-archived Robust:", Response_Other_NotArchived_Robust, "\n", "Records not countable by language (no ISO code):", Response_Undetermined_languages, "\n", "All quantities:", Response_a_h_sum
######################################################
#plt.legend(proxy,"range(1-2)",)
#print df.Group


########## CODE SNIPPETS FOR LATER USE ###############
#Sometimes I need to be able to return the entire row of a set of data based on a response to a column query.
#df.<column name>.value_counts() is the funtion which gives me the counts of a particualr items in column

#In the data file currently in use, the titles in the header row contain titles with spaces. This is evidently not allowed. Therefore the titles with spaces are retitled (for processing) with titles without spaces in the name.
#df = df.rename(columns = {'Ethnologue Status' : 'EthStatus', })
######################################################