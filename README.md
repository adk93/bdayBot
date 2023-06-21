**Birthday Bot**
- Birthday Bot gets user data from  Gsheets,
- Finds people with birthday on a today's date
- Generates birthday wishes using OpenAI
- Sends birthday message to slack Channel

**.env file**
- OPENAI_API_KEY= *string key from openai*
- SLACK_TOKEN= *string token from slack app*
- service_account_json= *string json google serivce account*
- src_spreadsheet_id= *google spreadsheet id*
- sheet_name= *string google sheets sheet name*
- range= *string google sheets range to download*
- name_col_number= *col number with names*
- birthdate_col_number= *col number with birthday dates*
- slack_channel_name= *slack channel name starting with #*
- giphy_api_key = *giphy api key as string*