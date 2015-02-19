#Data grid items and definitions
These are the columns and the reasons for their existence. The source column indicates where the data in the dataset came from. The Field type indicates which python datatype is in the field. The WordPress Field Name is a field name that is parseable by WordPress so that I can look at the data in an interactive environment with mashup layers. The explanation denotes why the field is necessary or how it came into being.
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
 * _Explanation:_ This is the application name of the lexical database solution. It is assumed that the answers in this list will form a basic taxonomy of the applications being used for creating the Lexical databases. In the multiple choice options several were suggested: FLEx, Toolbox, 
* **FLEx Version**
 * _Source:_ Computed
 * _Field type:_ String (though this is digits in the form of 1.2.3)
 * _WordPress Field Name:_ -
 * _Explanation:_ This is the version of FLEx that the respondent said that they were using at the time the response was received. The online form has a version number in the answer but this field separates the data returned in the questionnaire and only includes the version number.
* **What Lexical Database Solution do you use:**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_ This is the output of the form. Which is different than the input I am using for detailed analysis of users.
* **Email address**
 * _Source:_ This data comes from the questionnaire responses. 
 * _Field type:_ String
 * _WordPress Field Name:_ lxdb_email_address_of_data_provider
 * _Explanation:_ This is the email address of the record creator. It is personal information and should not be in the public version of the dataset. It was voluntarily provided, and optional in the web form. It was automatically provided when someone replied via email.
* **Lexical Database creator or contact person**
 * _Source:_ -
 * _Field type:_ String
 * _WordPress Field Name:_ -
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
 * _Explanation:_ Because the 'SIL Project' question is an open field is an open text field, a variety of answers are possible. This can include more than "Yes or No". This field becomes a binary representation of the 'SIL Project' field with a numerical value of 1 for SIL and an numerical value of 2 for other answers. This field is computed in the following way: if the field 'SIL Project' as a string is "SIL" then a value of '1' is given, else 2.
* **Did Hugh have to make a categorical decision based on the provided data, and what was that response?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **The respondent said that they archived their lexical database.**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ lxdb_archived_status
 * _Explanation:_
* **Behavior**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class1**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **The Institutional Archive at which the Lexical Database is allegedly archived**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ -
 * _WordPress Field Name:_ lxdb_archive_name
 * _Explanation:_
* **TAPS Archive**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class2**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Was there anything found at the Archive?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class 3**
 * _Source:_ -
 * _Field type:_ -
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
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Was the archive entry description clear that this was a lexical database/dataset?**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Stop Class 5**
 * _Source:_ -
 * _Field type:_ -
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
 * _WordPress Field Name:_ -
 * _Explanation:_
* **If you are using FLEx or Toolbox have you produced a Print publication?**
 * _Source:_ This data comes from the questionnaire responses, via online form or email.
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Number of entries**
 * _Source:_ Varied
 * _Field type:_ -
 * _WordPress Field Name:_ lxdb_term_quantity
 * _Explanation:_ Some descriptions of lexical resources include a value for how many lexical entries are included in the resource. Some respondents provided this data as well. Coverage across the records is sporadic, but significant numbers of lexical databased comments included this data so it was included as its own field. The source is varied, sometimes it is from the responses, sometimes archive records, sometimes other.
* **Last Date updated**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Method Received**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ lxdb_method_received_answer
 * _Explanation:_
* **Online Accessible Archive Record**
 * _Source:_ -
 * _Field type:_ -
 * _WordPress Field Name:_ lxdb_url_to_archive_record
 * _Explanation:_ This field is the URL to the public archive record of the resource. Sometimes resources are embedded within collections and do not have their own URLs. This is problematic and then the record does not have a URL. For content which is not archived, URLs point to where the content is publicly accessible. 
* **Private URLs**
 * _Source:_ Varied
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Part2B**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Part2T**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Part1**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Scope**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ language_scope
 * _Explanation:_
* **Language_Type**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Ref_Name**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Comment**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Graphic Type**
 * _Source:_ SIL.org GIS Data
 * _Field type: String_ -
 * _Explanation:_ This field comes from the data in the SIL list of endangered languages. It represents a shape on their map.
* **Latitude**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_ 
* **Longitude**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Language Link**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Language Name**
 * _Source:_ ISO 639-3 tables
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_ Ethnologue/ ISO 639-3 language name
* **Contains Apostrophe**
 * _Source:_ String
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_ ISO 639-3 data is different than Ethnologue data in that ethnologue data itself does not use apostrophes where as ISO 639-3 does.
* **leaflet_id**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Radius**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Color**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_ Color of the circle.
* **Ethnologue Status**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ ethnologue_17_status
 * _Explanation:_
* **Union Status Key**
 * _Source:_ Computed
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Hex Fill Color**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ String
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Weight**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **Opacity**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_
* **FillOpacity**
 * _Source:_ SIL.org GIS Data
 * _Field type:_ -
 * _WordPress Field Name:_ -
 * _Explanation:_