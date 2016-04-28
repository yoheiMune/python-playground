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



if os.path.exists(CREDENTIALS_FILE):
    credentials = Storage(CREDENTIALS_FILE).get()

else:


    SCOPE = 'https://www.googleapis.com/auth/bigquery.readonly'
    flow = flow_from_clientsecrets('secret/oauth2.json',
                                   scope=SCOPE,
                                   redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    print(flow)


    # STEP1
    auth_uri = flow.step1_get_authorize_url()
    print(auth_uri)

    # get code from STEP1
    code = "4/UgR2dMEPi4lY00QpMTIL8kQBaDTrlsyEc0TeoPJwL2Q"


    # STEP2
    credentials = flow.step2_exchange(code)
    print(credentials)

    # save
    Storage(CREDENTIALS_FILE).put(credentials)



# STEP3
http_auth = credentials.authorize(Http())
service = build('bigquery', 'v2', http=http_auth)


# STEP4
query = "SELECT 1 AS CheckBillableProject  FROM [patriot-999:adcross.view_banner_entry_all]  LIMIT 1"
body = {
    # "timeoutMs": 42, # [Optional] How long to wait for the query to complete, in milliseconds, before the request times out and returns. Note that this is only a timeout for the request, not the query. If the query takes longer to run than the timeout value, the call returns without any results and with the 'jobComplete' flag set to false. You can call GetQueryResults() to wait for the query to complete and read the results. The default value is 10000 milliseconds (10 seconds).
    "kind": "bigquery#queryRequest", # The resource type of the request.
    # "dryRun": True, # [Optional] If set to true, BigQuery doesn't run the job. Instead, if the query is valid, BigQuery returns statistics about the job such as how many bytes would be processed. If the query is invalid, an error returns. The default value is false.
    # "useQueryCache": true, # [Optional] Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. The default value is true.
    # "defaultDataset": { # [Optional] Specifies the default datasetId and projectId to assume for any unqualified table names in the query. If not set, all table names in the query string must be qualified in the format 'datasetId.tableId'.
    #     "projectId": project_id, # [Optional] The ID of the project containing this dataset.
    #     "datasetId": "patriot-999", # [Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.
    # },
    # "useLegacySql": True or False, # [Experimental] Specifies whether to use BigQuery's legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery's updated SQL dialect with improved standards compliance. When using BigQuery's updated SQL, the values of allowLargeResults and flattenResults are ignored. Queries with useLegacySql set to false will be run as if allowLargeResults is true and flattenResults is false.
    # "maxResults": 42, # [Optional] The maximum number of rows of data to return per page of results. Setting this flag to a small value such as 1000 and then paging through results might improve reliability when the query result set is large. In addition to this limit, responses are also limited to 10 MB. By default, there is no maximum row count, and only the byte limit applies.
    "query": query, # [Required] A query string, following the BigQuery query syntax, of the query to execute. Example: "SELECT count(f1) FROM [myProjectId:myDatasetId.myTableId]".
    # "preserveNulls": True or False, # [Deprecated] This property is deprecated.
}
pprint(body)

# http://qiita.com/shibacow/items/b8f6445058b374291be5

project_id = "patriot-999"
result = service.jobs().query(projectId=project_id, body=body).execute(http_auth)
pprint(result)


"""
<oauth2client.client.OAuth2WebServerFlow object at 0x1007b66a0>
https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fbigquery.readonly&response_type=code&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&access_type=offline&client_id=668560934470-9bcq0rmcfrfddtg6vjfhennj3b81ghf8.apps.googleusercontent.com
<oauth2client.client.OAuth2Credentials object at 0x103698080>
{'kind': 'bigquery#queryRequest',
 'query': 'SELECT 1 AS CheckBillableProject  FROM '
          '[patriot-999:adcross.view_banner_entry_all]  LIMIT 1'}
execute() takes at most 1 positional argument (2 given)
{'cacheHit': False,
 'jobComplete': True,
 'jobReference': {'jobId': 'job_F669WiYmY6rM3j9KGkCXqezOsWQ',
                  'projectId': 'patriot-999'},
 'kind': 'bigquery#queryResponse',
 'rows': [{'f': [{'v': '1'}]}],
 'schema': {'fields': [{'mode': 'NULLABLE',
                        'name': 'CheckBillableProject',
                        'type': 'INTEGER'}]},
 'totalBytesProcessed': '976036487',
 'totalRows': '1'}
 """
































