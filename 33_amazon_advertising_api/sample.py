"""
    Amazon Advertising API の利用サンプル

    参考ドキュメント：
        https://images-na.ssl-images-amazon.com/images/G/09/associates/paapi/dg/index.html

    アカウントセットアップ：
        https://images-na.ssl-images-amazon.com/images/G/09/associates/paapi/dg/index.html
        https://affiliate.amazon.co.jp/assoc_credentials/home

    インストール：
        $ pip3 install --upgrade python-amazon-simple-product-api

    python-amazon-simple-product-apiについて：
        https://pypi.python.org/pypi/python-amazon-simple-product-api
        https://a-zumi.net/python-amazon-api-parent-category/
        https://github.com/yoavaviram/python-amazon-simple-product-api
"""
import os

from amazon.api import AmazonAPI

# アクセスキーとシークレットキーを取得（環境変数にあることを想定）
ACCESS_KEY = os.environ["AMAZON_ADVERTISING_API_ACCESS_KEY"]
SECRET = os.environ["AMAZON_ADVERTISING_API_SECRET"]

# アソシエイトタグ（環境変数にあることを想定）
ASSOCIATE_TAG = os.environ["AMAZON_ADVERTISING_API_ASSOCIATE"]

# 確認
print(ACCESS_KEY)
print(SECRET)
print(ASSOCIATE_TAG)

# 実装例（ItemLookUp）
amazon = AmazonAPI(ACCESS_KEY, SECRET, ASSOCIATE_TAG, region="JP")
product = amazon.lookup(ItemId="B00IESDRSW", Condition="All")
print(product)
print(product.title)
print(product.price_and_currency)
print(product.sales_rank)
# レスポンス構造
# https://github.com/yoavaviram/python-amazon-simple-product-api/blob/master/amazon/api.py#L663



