#Data grid items and definitions used in the MasterList set of data
These are the columns and the reasons for their existence / how they are used. 
The **Source** column indicates where the data in the dataset came from. There are currently 5 possible values here: 
 1. Responses (direct content from email and questionnaires)
 2. ISO 639-3 tables
 3. SIL.org GIS data
 4. Computed values based on responses
 5. Researcher classified values based on qualitative responses from the questionnaires.
 
The **Field type** indicates which Python datatype is in the field. There are two values used here:
 1. String
 2. Integer

The **WordPress Field Name** is a field name that is parseable by WordPress so that I can look at the data in an interactive environment with mashup layers. The **Explanation** denotes why the field is necessary or how it came into being.


* **ISO 639-3 language code of the language you are analyzing/studying in your Lexical Database:**
 * _Source:_ This data comes from the questionnaire responses (or in this case also archive records).
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_subject_language
 * _Explanation:_ This is the ISO 639-3 code of the ISO 639-3 language code of the language you are analyzing/studying in your Lexical Database:
* **Variety Name or language name**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_language_variety_name
 * _Explanation:_ This is the varietal name, or sub-language name. The language name is the one from the ISO 639-3 table. However, this line is also needed because people keep lexicons of dialects or speech varieties which have not been given their own ISO 639-3 code.
* **Timestamp**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String (Though it is in a date format.)
 * _WordPress Field Name:_ post_date
 * _Explanation:_ This is the time and date that the response was received.
* **Application**
 * _Source:_ Computed
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_application
 * _Explanation:_ This is the application name of the lexical database solution. It is assumed that the answers in this list will form a basic taxonomy of the applications being used for creating the Lexical databases. In the multiple choice options several were suggested: FLEx, ToolBox, Lexus, TshwaneLex, etc 
* **FLEx Version**
 * _Source:_ Computed
 * _Field type:_ String (though this is digits in the form of 1.2.3)
 * _WordPress Field Name:_ None.
 * _Explanation:_ This is the version of FLEx that the respondent said that they were using at the time the response was received. The online form has a version number in the answer but this field separates the data returned in the questionnaire and only includes the version number.
* **What Lexical Database Solution do you use:**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This is the output of the form. Which is different than the input I am using for detailed analysis of users.
* **Email address**
 * _Source:_ This data comes from the questionnaire responses. 
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_email_address_of_data_provider
 * _Explanation:_ This is the email address of the record creator. It is personal information and should not be in the public version of the dataset. It was voluntarily provided, and optional in the web form. It was automatically provided when someone replied via email.
* **Lexical Database creator or contact person**
 * _Source:_ -
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This is the name of the individual who created the lexical database. It was voluntarily provided, and optional in the web form, from self reporters, it was in the archive record for those records found in archives or OLAC. It was automatically provided when someone replied via email.
* **Lexical Database record Provider**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_data_provider_name
 * _Explanation:_ This is the name of the individual who created the record. It was voluntarily provided, and optional in the web form. It was automatically provided when someone replied via email. While some of this data may be publicly available through archive records, not all of it is publicly available, therefore this column should not be included in the publicly available data.
* **Participant ID**
 * _Source:_ Computed
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This is a computed field so that participant quantities can be anonymously shared.
* **SIL Project**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_sil_project
 * _Explanation:_ The questionnaire respondents are asked if this is an SIL project. This is an optionally answered question. Responses via email are curated to fit.
* **Group**
 * _Source:_ Computed
 * _Field type:_ Interger
 * _WordPress Field Name:_ None.
 * _Explanation:_ Because the 'SIL Project' question is an open field is an open text field, a variety of answers are possible. This can include more than "Yes or No". This field becomes a binary representation of the 'SIL Project' field with a numerical value of '1' for 'SIL'/'Yes' and an numerical value of '2' for other answers. This field is computed in the following way: if the field 'SIL Project' as a string is "SIL" then a value of '1' is given, else '2'.
* **Did Hugh have to make a categorical decision based on the provided data, and what was that response?**
 * _Source:_ Researcher classified value
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Often in the comments researchers would indicate multiple lexical database projects. A second record was then added if needed. This was recorded with a value of 'Split Entry'. A second text item 'Need help' was also used to indicate that the response was complex and further negotiation of details with the researcher was required. This field was used for internal tracking. It also indicates that records generated were not actions of people adding multiple entires via the google form.
* **The respondent said that they archived their lexical database.**
 * _Source:_ Researcher classified value
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_archived_status
 * _Explanation:_ The questionnaire does not provide a binary value for a archived 'yes/no' distinction, because "no" is equally presented in the questionnaire with a variety of "yes" options. This field was manually curated, but might be possible to use Python to curate in the future. It uses two strings, "Yes" and "No. - Never Archived it."
* **Behavior**
 * _Source:_ Researcher classified value
 * _Field type:_ Interger
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is a binary summary of the responses. That is, the field contains a '1' when the respondent says they archived and a '2' when the respondent says they did not archive. This is done before any analysis about the archive solution the respondent says they interact with. It is binary for sorting purposes. With the use of Python this field may be unnecessary. The field is currently marked as 'Researcher classified value', but should likely be converted to values derived via Python and be converted to 'Computed". 
* **Stop Class1**
 * _Source:_ -
 * _Field type:_ Interger
 * _WordPress Field Name:_ -
 * _Explanation:_
* **The Institutional Archive at which the Lexical Database is allegedly archived**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_archive_name
 * _Explanation:_
* **TAPS Archive**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class2**
 * _Source:_ -
 * _Field type:_ Interger
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Was there anything found at the Archive?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class 3**
 * _Source:_ -
 * _Field type:_ Interger
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Items which should be in REAP found/not-found**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Was the thing a Lexical Database?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class 4**
 * _Source:_ -
 * _Field type:_ Interger
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Was the archive entry description clear that this was a lexical database/dataset?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class 5**
 * _Source:_ -
 * _Field type:_ Interger
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Thinks they have archived but have not**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Anything we should know?**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ -
 * _WordPress Field Name:_ String
 * _Explanation:_
* **If you are using FLEx or Toolbox have you produced a Print publication?**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_
* **Number of entries**
 * _Source:_ Researcher classified values
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_term_quantity
 * _Explanation:_ Some descriptions of lexical resources include a value for how many lexical entries are included in the resource. Some respondents provided this data as well. Coverage across the records is sporadic, but significant numbers of lexical databased comments included this data so it was included as its own field. The source is varied, sometimes it is from the responses, sometimes archive records, sometimes other.
* **Last Date updated**
 * _Source:_ Researcher classified values
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Sometimes Records have values for when a resource was last updated. I take it to mean that the version archived was not updated since the record was updated and include this kind of data in this table.
* **Method Received**
 * _Source:_ Researcher classified values
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_method_received_answer
 * _Explanation:_ This field exists to track how the entry record entered the databased. There are currently 4 possible values in this field: Responses via Google Docs, Responses via Email, Research via OLAC, and Research via Catalogues (mostly at the SIL Language and Culture Archive). In the data set these appear as the following strings: 'Online Survey From', 'Mailed in', 'Found on OLAC', 'Discovery'.
* **Online Accessible Archive Record**
 * _Source:_ Researcher classified values
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_url_to_archive_record
 * _Explanation:_ This field is the URL to the public archive record of the resource. Sometimes resources are embedded within collections and do not have their own URLs. This is problematic in general. For content which is not archived, URLs point to where the content is publicly accessible. 
* **Private URLs**
 * _Source:_ Researcher classified values
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Sometimes private URLs are accessible to the researcher. These are not public, and are not published with the dataset, but help in the classification and tracking of resources.
* **Part2B**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Part2T**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Part1**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Scope**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ language_scope
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Language_Type**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Ref_Name**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Comment**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Is a field in the ISO 639-3 code table. This field is best understood by consulting the ISO 639-3 registrar's own documentation.
* **Graphic Type**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _Explanation:_ This field comes from the data in the SIL list of endangered languages. It represents a shape on their map. The value is alway 'circle'. I left it in incase I use the same production method, though realistically this column should likely be dropped.
* **Latitude**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ Integer
 * _WordPress Field Name:_ language_latitude
 * _Explanation:_ This is the Latitude point value that the SIL.org data provides. The data is assumed to be on WGS84 datum. The data appears in the 0.00000 or -0.00000 format.
* **Longitude**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ Integer
 * _WordPress Field Name:_ language_longitude
 * _Explanation:_ This is the Longitude point value that the SIL.org data provides. The data is assumed to be on WGS84 datum. The data appears in the 0.00000 or -0.00000 format.
* **Language Link**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_language_link
 * _Explanation:_ This field is a HTML encoded link to the Ethnologue record for the language.
* **Language Name**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ language_name
 * _Explanation:_ SIL.org / ISO 639-3 language name. The general process here is to get the names from the ISO tables and then evaluate if any changes are needed.
* **Contains Apostrophe**
 * _Source:_ String
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ ISO 639-3 data is different than Ethnologue data in that ethnologue data itself does not use apostrophes where as ISO 639-3, and SIL.org do, so if a language name comes from the Ethnologue, then the data may not be the same as if it comes from SIL.org or the ISO 639-3 code table.
* **leaflet_id**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires a unique leaflet ID for each dot/datapoint for the production of dots on a mashup map.
* **Radius**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires a radius for the production of dots on a mashup map.
* **Color**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ Color of the circle. This field is unused. It is residue from the data merge with SIL.org data. Their script requires a an HTML color for the production of dots on a mashup map.
* **Ethnologue Status**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ ethnologue_17_status
 * _Explanation:_ This field is residue from the data merge with SIL.org data. It should be replaced with the EGIDS value of each language. The 'Union Status Key' computes based on the value of this field. This field has two values, *Robust* and *Endangered*. SIL.org claimed at the time the data was collected that the data was sourced from the Ethnologue 17th edition. The *Endangered languages* are languages classified in the Ethnologue with an EGIDS value of 6b-9, while *Robust languages* are classified as 0-6a on the EGIDS scale.
* **Union Status Key**
 * _Source:_ Computed
 * _Field type:_ Integer
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is a computed integer index of values from three columns creating 10 sets of data. This data is then used to create and plot the points on the global map. 
 1 = SIL Staff Archived Endangered, 2 = SIL Staff Not-archived Endangered, 3 = Other Archived Endangered, 4 = Other Not-archived Endangered, 5 = SIL Staff Archived Robust, 6 = SIL Staff Not-archived Robust, 7 = Other Archived Robust, 8 = Other Not-archived Robust, 9 = No available Coordinates, 10 = Lexical datasets with the code [und].
* **Hex Fill Color**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires an HTML color for the production of dots on a mashup map. I left it in incase I use the same production method, though realistically this column should likely be dropped.
* **Weight**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ Integer
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires a weight classification in the production of dots on a mashup map. I left it in incase I use the same production method, though realistically this column should likely be dropped.
* **Opacity**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ Integer
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires a opacity value in the production of dots on a mashup map. I left it in incase I use the same production method, though realistically this column should likely be dropped.
* **FillOpacity**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ Integer
 * _WordPress Field Name:_ None.
 * _Explanation:_ This field is unused. It is residue from the data merge with SIL.org data. Their script requires a fill opacity classification in the production of dots on a mashup map. I left it in incase I use the same production method, though realistically this column should likely be dropped.