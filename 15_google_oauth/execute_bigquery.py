# -*- coding: utf-8 -*-
#
# Using Google API via OAuth 2.0, which is under a embedded system.
# This program is a sample for Google Bigquery.
import os
from pprint import pprint
from oauth2client.client import flow_from_clientsecrets
from httplib2 import Http
from apiclient.discovery import build
from oauth2client.file import Storage

CREDENTIALS_FILE = "./secret/credentials"


# Get a credential.
if os.path.exists(CREDENTIALS_FILE) == False:
    import google_oauth
    credentials = google_oauth.get_credentials()

else:
    credentials = Storage(CREDENTIALS_FILE).get()


# Get API Service.
http_auth = credentials.authorize(Http())
service = build('bigquery', 'v2', http=http_auth)


# Execute a google bigquery.
query = "SELECT 1 AS dummy  FROM [patriot-999:adcross.view_banner_entry_all]  LIMIT 1"
# query = "SELECT 1 AS dummy  FROM [bigquery-public-data:hacker_news]  LIMIT 1"
# body = {
#     "kind": "bigquery#queryRequest", # The resource type of the request.
#     # "dryRun": True, # [Optional] If set to true, BigQuery doesn't run the job. Instead, if the query is valid, BigQuery returns statistics about the job such as how many bytes would be processed. If the query is invalid, an error returns. The default value is false.
#     # "useQueryCache": true, # [Optional] Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. The default value is true.
#     # "defaultDataset": { # [Optional] Specifies the default datasetId and projectId to assume for any unqualified table names in the query. If not set, all table names in the query string must be qualified in the format 'datasetId.tableId'.
#     #     "projectId": project_id, # [Optional] The ID of the project containing this dataset.
#     #     "datasetId": "patriot-999", # [Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.
#     # },
#     # "useLegacySql": True or False, # [Experimental] Specifies whether to use BigQuery's legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery's updated SQL dialect with improved standards compliance. When using BigQuery's updated SQL, the values of allowLargeResults and flattenResults are ignored. Queries with useLegacySql set to false will be run as if allowLargeResults is true and flattenResults is false.
#     # "maxResults": 42, # [Optional] The maximum number of rows of data to return per page of results. Setting this flag to a small value such as 1000 and then paging through results might improve reliability when the query result set is large. In addition to this limit, responses are also limited to 10 MB. By default, there is no maximum row count, and only the byte limit applies.
#     "query": query, # [Required] A query string, following the BigQuery query syntax, of the query to execute. Example: "SELECT count(f1) FROM [myProjectId:myDatasetId.myTableId]".
#     # "preserveNulls": True or False, # [Deprecated] This property is deprecated.
# }
body = {
    "kind": "bigquery#queryRequest",
    "query": query
}

# http://qiita.com/shibacow/items/b8f6445058b374291be5

project_id = "patriot-999"
# project_id = "bigquery-public-data"
result = service.jobs().query(projectId=project_id, body=body).execute(http_auth)
pprint(result)


"""
{'jobComplete': False,
 'jobReference': {'jobId': 'job_Lam-7fpXhX2_W46SM4OXrY5_B9U',
                  'projectId': 'patriot-999'},
 'kind': 'bigquery#queryResponse'}
 """
































