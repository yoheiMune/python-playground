"""
    Google Geocoding API の使用サンプル

    リファレンス：
        https://developers.google.com/maps/documentation/geocoding/intro?hl=ja
        https://developers.google.com/maps/documentation/geocoding/get-api-key?hl=ja

    メモ：
        ・環境変数（ GOOGLE_GEOCODING_API_KEY ）にAPIKeyが指定されていることを想定しています.

"""
import os
import requests


APIKEY_ENV_NAME = "GOOGLE_GEOCODING_API_KEY"

def execute():

    # APIKeyの取得
    API_KEY = os.environ.get(APIKEY_ENV_NAME)
    if not API_KEY:
        raise Exception("環境変数（{}）に、APIKeyが設定されていません".format(APIKEY_ENV_NAME))

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "key" : API_KEY,
        "address" : "千葉県習志野市津田沼1-23-1",
        "language" : 'ja'
    }
    r = requests.get(url, params=params)
    print(r.text)

    extract(r.json())

def extract(result):

    # 取得したいデータ
    post_code = ""
    prefecture = ""
    city = ""
    latitude = ""
    longitude = ""
    place_id = ""

    for c in result["results"][0]["address_components"]:
        types = c["types"]
        name = c["long_name"]
        if "postal_code" in types:
            post_code = name
        elif "administrative_area_level_1" in types:
            prefecture = name
        elif "locality" in types:
            city = name

    latitude = result["results"][0]["geometry"]["location"]["lat"]
    longitude = result["results"][0]["geometry"]["location"]["lng"]
    place_id = result["results"][0]["place_id"]

    print("post_code:", post_code)
    print("prefecture:", prefecture)
    print("city:", city)
    print("latitude:", latitude)
    print("longitude:", longitude)
    print("place_id:", place_id)



if __name__ == "__main__":
    execute()