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

def execute1(api_key):

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "key" : api_key,
        "address" : "長野県諏訪郡下諏訪町南四王6133",
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


def reverse_geocoding(api_key):

  url = "https://maps.googleapis.com/maps/api/geocode/json"
  params = {
      "key" : api_key,
      # 〒393-0045 長野県諏訪郡下諏訪町南四王6133
      "latlng" : "36.066862,138.08763",
      "language" : 'ja'
  }
  r = requests.get(url, params=params)
  print(r.text)

  result = r.json()

  prefecture = ""
  city = ""
  for c in result["results"][0]["address_components"]:
    types = c["types"]
    name = c["long_name"]
    if "administrative_area_level_1" in types:
        prefecture = name
    elif "locality" in types:
        city = name
  print("prefecture:", prefecture)
  print("city:", city)



if __name__ == "__main__":

    # APIKeyの取得
    API_KEY = os.environ.get(APIKEY_ENV_NAME)
    if not API_KEY:
        raise Exception("環境変数（{}）に、APIKeyが設定されていません".format(APIKEY_ENV_NAME))

    # 住所からGeoLocation
    execute1(API_KEY)

    # GeoLocationから住所
    reverse_geocoding(API_KEY)

"""
▼ 実行結果（住所からGeoLocation） ▼

{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "１",
               "short_name" : "１",
               "types" : [ "political", "sublocality", "sublocality_level_4" ]
            },
            {
               "long_name" : "２３",
               "short_name" : "２３",
               "types" : [ "political", "sublocality", "sublocality_level_3" ]
            },
            {
               "long_name" : "１丁目",
               "short_name" : "１丁目",
               "types" : [ "political", "sublocality", "sublocality_level_2" ]
            },
            {
               "long_name" : "津田沼",
               "short_name" : "津田沼",
               "types" : [ "political", "sublocality", "sublocality_level_1" ]
            },
            {
               "long_name" : "習志野市",
               "short_name" : "習志野市",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "千葉県",
               "short_name" : "千葉県",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "日本",
               "short_name" : "JP",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "275-0016",
               "short_name" : "275-0016",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "日本、〒275-0016 千葉県習志野市津田沼１丁目２３−１",
         "geometry" : {
            "location" : {
               "lat" : 35.6904813,
               "lng" : 140.024784
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6918302802915,
                  "lng" : 140.0261329802915
               },
               "southwest" : {
                  "lat" : 35.6891323197085,
                  "lng" : 140.0234350197085
               }
            }
         },
         "place_id" : "ChIJG-BIJyOAImARjzeKi2JhEr4",
         "types" : [ "political", "sublocality", "sublocality_level_4" ]
      }
   ],
   "status" : "OK"
}

post_code: 275-0016
prefecture: 千葉県
city: 習志野市
latitude: 35.6904813
longitude: 140.024784
place_id: ChIJG-BIJyOAImARjzeKi2JhEr4
"""