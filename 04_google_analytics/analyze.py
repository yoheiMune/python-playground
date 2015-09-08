# -*- coding: utf-8 -*-
# for Python 3
#
# Google Analytics API
import oauth2client
import apiclient
import httplib2

scope = ["https://www.googleapis.com/auth/analytics.readonly"]
service_account_email = "682828118526-b34hs263kbvvl22v06fj0m6ro1sds4k8@developer.gserviceaccount.com"

# キーのロード
key_file = "client_secret.p12"
with open(key_file, 'rb') as f:
    key = f.read()

# OAuth認証の準備
credentials = oauth2client.client.SignedJwtAssertionCredentials(service_account_email, key, scope=scope)
http = credentials.authorize(httplib2.Http())

# コネクション作成
service = apiclient.discovery.build("analytics", "v3", http=http)

# データ取得
results = service.data().ga().get(
    # ids="ga:100037984",
    ids="ga:75138417",
    start_date="2015-09-01",
    end_date="2015-09-07",
    metrics="ga:pageviews,ga:sessions,ga:users"
).execute()
row = results.get('rows')[0]

# PV
print("PV: %s" % row[0])

# セッション数
print("Session: %s" % row[1])

# ユーザー数
print("User: %s" % row[2])







