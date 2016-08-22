# Yahooファイナンスから通過レートを取得するサンプル
# 
# YQL：
#   ドキュメント：https://developer.yahoo.com/yql/
#   テーブル定義：https://github.com/yql/yql-tables/blob/master/yahoo/finance/yahoo.finance.xchange.xml
# 
# 参考資料：
#   http://qiita.com/masato/items/6f81bdc89f81a7b6cc3a
#   http://stackoverflow.com/questions/3139879/how-do-i-get-currency-exchange-rates-via-an-api-such-as-google-finance
#
# サンプル：
#   https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDJPY%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys
#
import urllib.request
import urllib.parse
import json
from pprint import pprint

url = "https://query.yahooapis.com/v1/public/yql"
params = {
    "q": 'select * from yahoo.finance.xchange where pair in ("USDJPY")',
    "format": "json",
    "env": "store://datatables.org/alltableswithkeys"
}
url += "?" + urllib.parse.urlencode(params)

res = urllib.request.urlopen(url)
result = json.loads(res.read().decode('utf-8'))
pprint(result)
"""
{'query': {'count': 1,
           'created': '2016-08-22T02:57:07Z',
           'lang': 'en-US',
           'results': {'rate': {'Ask': '100.6850',
                                'Bid': '100.6380',
                                'Date': '8/21/2016',
                                'Name': 'USD/JPY',
                                'Rate': '100.6380',
                                'Time': '10:58pm',
                                'id': 'USDJPY'}}}}
"""
rate = result["query"]["results"]["rate"]["Rate"]
print('USD/JPY:', rate)
# USD/JPY: 100.6380