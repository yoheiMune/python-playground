# -*- coding: utf-8 -*-
# for Python 3
#
# Google Analytics API
import oauth2client
import apiclient
import httplib2
import datetime

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

# データ取得 （基本データ）
#################################
# results = service.data().ga().get(
#     # ids="ga:100037984",
#     ids="ga:75138417",
#     start_date="2015-09-07",
#     end_date="2015-09-07",
#     metrics="ga:pageviews,ga:sessions,ga:users"
# ).execute()
# row = results.get('rows')[0]

# # PV
# print("PV: %s" % row[0])

# # セッション数
# print("Session: %s" % row[1])

# # ユーザー数
# print("User: %s" % row[2])


# 昨日のデータ
yesterday = (datetime.date.today() - datetime.timedelta(2)).strftime('%Y-%m-%d')
print(yesterday)


# データ取得 （フレッシュ枠 - click）
#################################
print("loading... fresh data click")
results = service.data().ga().get(
    ids="ga:75138417",
    start_date=yesterday,
    end_date=yesterday,
    dimensions="ga:eventAction,ga:eventLabel",
    metrics="ga:totalEvents",
    filters="ga:eventAction=~top-free-recommend-\d",
    max_results=300
).execute()
rows = results.get('rows')
# print(rows)

fresh_data = {}
for row in rows:
    # ['top-free-recommend-1', 'buy_100_ちはやふる（１）', '205']
    if row[1].startswith("buy") == False:
        continue
    id    = row[1].split("_")[1]
    type  = row[0].split("-")[3]
    title = row[1].split("_")[2]
    click = int(row[2])
    fresh_data[id] = {
        "type": type,
        "title": title,
        "click": click
    }
# print(fresh_data)


# データ取得 （フレッシュ枠 - imp）
#################################
print("loading... fresh data imp")
results = service.data().ga().get(
    ids="ga:75138417",
    start_date=yesterday,
    end_date=yesterday,
    dimensions="ga:eventAction,ga:eventLabel",
    metrics="ga:totalEvents",
    filters="ga:eventAction=~top-free-recommend-show",
    max_results=300
).execute()
rows = results.get('rows')
# print(rows)

for row in rows:
    # ['top-free-recommend-show', 'id_99', '16126']
    id  = row[1].split("_")[1]
    imp = int(row[2])
    if id in fresh_data:
        fresh_data[id]["imp"] = imp
print(fresh_data)























