
# https://developers.google.com/places/web-service/search?hl=ja
# https://developers.google.com/places/web-service/get-api-key?hl=ja

# 環境変数（ GOOGLE_PLACE_API_KEY ）に、APIKeyがあることを想定

# pip install requests
# http://www.yoheim.net/blog.php?q=20170802

import os
import requests

APIKEY_ENV_NAME = "GOOGLE_PLACE_API_KEY"

def execute():

    # APIKeyの取得
    API_KEY = os.environ.get(APIKEY_ENV_NAME)
    if not API_KEY:
        raise Exception("環境変数（{}）に、APIKeyが設定されていません".format(APIKEY_ENV_NAME))

    # 検索対象（イオンモール津田沼店）
    lat = "35.6904813"
    lng = "140.024784"

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key" : API_KEY,
        "location" : "{},{}".format(lat, lng),
        "radius" : 500
    }
    r = requests.get(url, params=params)
    print(r.text)

if __name__ == "__main__":
    execute()

"""
▼ 実行結果 ▼

{
   "html_attributions" : [],
   "next_page_token" : "CpQCDwEAAJjb3w0hMYN82FYs4q_AiqPuv1W2wNjk77BE_MYsLDxMIhDl1inzN8i1PsH9fVjCBDKvOCK_X8_132TvT32ZVi6nr_4bO4zuTyl9N69GHq5CU6bbvD08NR2Hp5GQ2VI1eDGZhIOV2NoNmV97tkaULkP1jFu-UcLUIpCfjHXEPczdx3zHLvb40m_a5216aY4B7V2sJHADZBs3SpNzPBHmgnq0gMzxI9UTDRxgEfLiRMl6uDJxwdRuDIh9XqdpvHmdDct6Eue67nHhxfw-8KhFFt3VaG1LjyDPAoKZgbjmmL_M3uXZ07eaxR0xkO5Xjm-e2s4bxT-5QqS_GkjBqDc-qF_yrmo1MNcY0DEUn_9OVkNwEhAP22XTWB4Vmf4n13zR8GZeGhQceeyUbYqUJIQL-3b0sDoi4hXqig",
   "results" : [
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6947058,
               "lng" : 139.982618
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.799553,
                  "lng" : 140.089632
               },
               "southwest" : {
                  "lat" : 35.6638363,
                  "lng" : 139.9388979
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png",
         "id" : "5d5c91c80801d251576cb6e1affc620f5cec2350",
         "name" : "Funabashi",
         "photos" : [
            {
               "height" : 1728,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/102084686430229311972/photos\"\u003e渡部敏広\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAjnY4W_s7GVOvWOomPiJ26HQavQYwK62W3Qh2janIO48m_GD8hfvwWDFR2wcfu42zuJfCKvo9mmyle_WvSMGH4zBWSbjdmLuFl00-zRq_kDuZWsH0AZ3E2QMesjcrkh7QEhCO9S52N_C1qDPh1RtFPxPlGhQoH24-dAfbTZKn8t6fMULxk8h2Tg",
               "width" : 3072
            }
         ],
         "place_id" : "ChIJt15MhSGAGGARCWuHCkC7KIE",
         "reference" : "CmRbAAAAyVixWJERsK1rBBKGpdSSvXRar0KpQQX58d_XcK4HuaUTq-GOX7nyQXn0padJ4YCUofhylCvKOJ2NSsOyQ1a9ZfbF5GdSYNR5KDFwicsIJ7wHbrZPh3ZiDD0SmMun4w9cEhBS8kPsLT5pCbMMIr5IBa6QGhQnRVp8kU_bS8hyp82NOwKFdvHXgw",
         "scope" : "GOOGLE",
         "types" : [ "locality", "political" ],
         "vicinity" : "Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.69302260000001,
               "lng" : 140.0228313
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6943715802915,
                  "lng" : 140.0241802802915
               },
               "southwest" : {
                  "lat" : 35.6916736197085,
                  "lng" : 140.0214823197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "e758af2ec8c8433d31c0b53c6af8e9fc723ef836",
         "name" : "ベティル(BELTIL)",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "place_id" : "ChIJjWnEQSGAImARobgCQvmUE2w",
         "rating" : 2.4,
         "reference" : "CmRRAAAAb68gBjS_A_nxfXhkVloMts0T77k1RWkLPJFk2ts4fP0q_ZnQFx46nLw2SDBPV1mgGNGdM2Rt3dCdB2pk17jA5JKjdqIMMw3GFKqLC0AMRTyn9PZqY9abKTt9ZYOkCu5JEhBYyXcnKnWrWfU91ff94yrHGhRT4p5-g8_a4PBS0ORNBoY2uBzk2Q",
         "scope" : "GOOGLE",
         "types" : [ "hair_care", "point_of_interest", "establishment" ],
         "vicinity" : "D-OMCビル, 3F, 2 Chome-21−7 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6922698,
               "lng" : 140.0276674
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69361878029149,
                  "lng" : 140.0290163802915
               },
               "southwest" : {
                  "lat" : 35.6909208197085,
                  "lng" : 140.0263184197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "e6dc1c764ae790f6727c982c17425ae1eed4fa42",
         "name" : "Masseria cafe",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 1153,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/101603042813505122994/photos\"\u003eMasseria\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAeRvKBYzJIBtnbyNtMl2TxT-ZYCXWzt2qxzL7DQ5hqlZKPHVNEHMhR3sguNYzgXXbBLvBEhDjBeaI73i_8DEf6AsLKDixHPL3HATP28WSJ_WbWA_AXwp2twI3Q0kwQUmJEhA71eYx3t4uAgIe1NmIb7MFGhT0CcliaRskk8BMlAyPiiMMz1AXpw",
               "width" : 2048
            }
         ],
         "place_id" : "ChIJh5d6wiSAImAR4IgikSHmZlQ",
         "price_level" : 2,
         "rating" : 3.7,
         "reference" : "CmRRAAAAUhy0qaBjdCTQVjcwCIdm3r_6Ect13px_rC5KpAuTzS6NNASe1BdTbUtqAt0MYC5FOqgXhnfnK7choBPv0qIzboE-nu9qqTmV44glEmALuAQifmNV9mEO6s2ywc9DiU0nEhDXNVGaFi4Ll1rgZCXUo6i7GhRhHK3YpYp2utNq5F0LZLOVelbc5Q",
         "scope" : "GOOGLE",
         "types" : [ "restaurant", "cafe", "food", "point_of_interest", "establishment" ],
         "vicinity" : "1 Chome-15-35 Maebarahigashi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.690309,
               "lng" : 140.022214
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6916579802915,
                  "lng" : 140.0235629802915
               },
               "southwest" : {
                  "lat" : 35.6889600197085,
                  "lng" : 140.0208650197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "d007c78620894869feb338eefe5f840525727982",
         "name" : "くいもの屋 わん 津田沼店",
         "opening_hours" : {
            "open_now" : false,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 311,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/106228478733871638048/photos\"\u003eくいもの屋 わん 津田沼店\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAMNNaohoOyIyxRyk_gK43BDdWHhLsxy1DfJm9v4B1aIxaThnPkuXbck03ffAEa3du0XJDWnv0Kbdk9aRotR-0VWyw1EMmLfT-j52ruKbx2auItgzbeF80K9y1rGpN6zmfEhAxHa7Ao8XPx-JfQs2WJOSNGhQex6Ye7qSDHAoscd6X4_YsG6Bvxg",
               "width" : 311
            }
         ],
         "place_id" : "ChIJYVUV6SaAImARPFZP2vOz6D0",
         "rating" : 2.7,
         "reference" : "CmRRAAAAnAFbpm81kHnN-FHcbSw3xpwfaoEV2OdYfmrLc84bD1JbEnl0ZNsu3w9hkdaZQgEtDVhHC9nHvwlPhj3coZRDNVRutgqrL7V6AtkASIQkkZBLO-GMnh7gwBQ4wlXCwOehEhBJVepN38H2UacjZQuBH9dqGhTgVRXbXjj_U4d9pvcqgDSAao4c7w",
         "scope" : "GOOGLE",
         "types" : [ "bar", "restaurant", "food", "point_of_interest", "establishment" ],
         "vicinity" : "1 Chome-2-1 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6928003,
               "lng" : 140.0212814
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69414928029151,
                  "lng" : 140.0226303802915
               },
               "southwest" : {
                  "lat" : 35.69145131970851,
                  "lng" : 140.0199324197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "39568d912c91cfa295b253a421f5307afbd9d55d",
         "name" : "Kin no Kura Jr.",
         "opening_hours" : {
            "open_now" : false,
            "weekday_text" : []
         },
         "place_id" : "ChIJHdzK4yCAImARROGBh0G9WWM",
         "price_level" : 2,
         "rating" : 2.5,
         "reference" : "CmRRAAAA5mcXnzzaJ-nmhEHTICpydzaHsc0pGlaf98quhiH-3W0eY81MwVyInhHTjXRYb6vtvRGX83vgluC-JaOFdPk_ND7dZI_NCfZehQ5rm1YWwsh5AgV5z8SeBc7E8UiR_s9fEhDWFO8COvjWk8dl5K5-3R8TGhTRuVfF5e4OZOYLKQOQTEaRvSSu7Q",
         "scope" : "GOOGLE",
         "types" : [ "restaurant", "food", "point_of_interest", "establishment" ],
         "vicinity" : "2 Chome-13-23 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.690481,
               "lng" : 140.024784
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6918299802915,
                  "lng" : 140.0261329802915
               },
               "southwest" : {
                  "lat" : 35.6891320197085,
                  "lng" : 140.0234350197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png",
         "id" : "d253d3666aa03d8c6f53ebf99835d91fd98e818c",
         "name" : "Talbots",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "place_id" : "ChIJTa0byyWAImARTUUpj4-9ChY",
         "price_level" : 2,
         "reference" : "CmRRAAAA6b6inSH1LtTGmTnnkEqYBHKu669bauaLaZf-5AsozLXatMMa56D556S6FlDuewXDz-fFz1Cji4QEHqx17WuAy4lPbysR69viVFj6gyIstQ8FaH1WdiRYjFt_kFFTEzHoEhBQp8BEfjldPI52P5WQcTXsGhSiUCNV3LrBqcg_RsWIUB772l1R2w",
         "scope" : "GOOGLE",
         "types" : [ "clothing_store", "store", "point_of_interest", "establishment" ],
         "vicinity" : "1−23−1 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6906554,
               "lng" : 140.0246852
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6920043802915,
                  "lng" : 140.0260341802915
               },
               "southwest" : {
                  "lat" : 35.6893064197085,
                  "lng" : 140.0233362197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "10b98c4ddc1fb18f0359dae8507573701ce6aca9",
         "name" : "フロプレステージュ 津田沼イオン店",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "place_id" : "ChIJLcLpLiSAImARA7yGzP-Si9Y",
         "price_level" : 2,
         "rating" : 4,
         "reference" : "CmRSAAAAof4-5yo03Y8AswGO5QBYQpQ8BGVqV8Hf5vyk3r7cEuoCveVvkzn-przHR7C5-EAbS8BnuKdl0Lwe_Le_NMZLTU1f-LNsZ6fMqGwjXUoCyg_CuYQ_NS3YNEMKm1oRmzT8EhBtEk4HYHvJ_xCR104HrwdnGhQ1vFOdxncDmFZ8_oOeMgfaBBX-pw",
         "scope" : "GOOGLE",
         "types" : [ "restaurant", "food", "store", "point_of_interest", "establishment" ],
         "vicinity" : "津田沼１丁目イオン津田沼店Ｂ１, 習志野市"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.69193639999999,
               "lng" : 140.0214928
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69328538029148,
                  "lng" : 140.0228417802915
               },
               "southwest" : {
                  "lat" : 35.69058741970849,
                  "lng" : 140.0201438197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png",
         "id" : "f43798a0c0177781d670dac04da5c284a4ca897f",
         "name" : "津田沼パルコ",
         "opening_hours" : {
            "open_now" : false,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 1920,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/110389526591474035726/photos\"\u003e麻生新\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAD3lKiP4cBVwv6VDhU69l8oysPGkOSBtm57DNiaIGbPB90idW45n7PApNMvIDD2lnDmpIoPegBbBq-GPRS22uwlgm95LKX6WI6l0l1BgxQZCZPJm5lrLJoSSvbrnVBohoEhCxPp293UfUTePGW2gE-CP3GhRrSg6_XxsKWQrMoP2drMksLHgBRg",
               "width" : 2560
            }
         ],
         "place_id" : "ChIJAeTJLSGAImARXM_rnTe8sKg",
         "rating" : 3.5,
         "reference" : "CmRSAAAAydVkxbtbCEhOyzMory7oS69AZwBV3dDKh_c9QCjQZDXOJyCsscGyqYZUeM0mdSWwBKDrQq38cFBTGgWSLuE1d8bfewRXaQGv7vGVtDNADUOP3ZcBpZiuYcOXb-iuzfgQEhCRj5dNUFoxrztVBSufJj00GhRp7ID2TacFzByM429NzACH2UXdvg",
         "scope" : "GOOGLE",
         "types" : [ "shopping_mall", "store", "point_of_interest", "establishment" ],
         "vicinity" : "2 Chome-18-1 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6930476,
               "lng" : 140.0223008
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6943965802915,
                  "lng" : 140.0236497802915
               },
               "southwest" : {
                  "lat" : 35.6916986197085,
                  "lng" : 140.0209518197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "902bc7657c3b534047c2e17aafee3fedc5cea75f",
         "name" : "アルボ(Arvo)",
         "place_id" : "ChIJB6QnFCGAImAR_FuC0XRd2cc",
         "reference" : "CmRSAAAAOgF7-knp7g9TsAZNLtbrdcvtOojZOWeIW0AQILma2IjFYnto1EFoy8ZNbeZXFiBvth1hO-w7BYgLVQhnrL3IEnSWDI_95lnm-SYeJPgNEvH8deCZAO_byFFXaEOZvf66EhCGEQS36WeQPhykJQnp-r1vGhRwTneJ0z3fQ5EvTf3S45QPSxO6Ag",
         "scope" : "GOOGLE",
         "types" : [ "hair_care", "point_of_interest", "establishment" ],
         "vicinity" : "鈴木生花ビル2F, 2 Chome-12−８ Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.69356979999999,
               "lng" : 140.0233035
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69491878029149,
                  "lng" : 140.0246524802915
               },
               "southwest" : {
                  "lat" : 35.6922208197085,
                  "lng" : 140.0219545197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "e9274b56147520c34b00c33e961e89b00cfe7568",
         "name" : "グリクロエ(guri croe)",
         "place_id" : "ChIJs-7kZSGAImARtkUM5i-jXi8",
         "rating" : 4,
         "reference" : "CmRRAAAAJx4RhhW3Eurz6lOeshANDb0-OVq0yRoQfde8ptW6xDioB2lqpjkzXXCFGmveLyHhM95wqK7WPWcF-eS0YyNeoOGvc7B5ZIydBVNgv1vysFKwJ0-j2zC0zjsbfUBw8S2vEhARS3jCtFrK1MFpTqANfWiAGhSDQGk5OFTPyEbmRCJ6Od9bdo8GDg",
         "scope" : "GOOGLE",
         "types" : [ "hair_care", "point_of_interest", "establishment" ],
         "vicinity" : "スクエアビル6F, 2 Chome-22−17 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6906062,
               "lng" : 140.0217954
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6919551802915,
                  "lng" : 140.0231443802915
               },
               "southwest" : {
                  "lat" : 35.6892572197085,
                  "lng" : 140.0204464197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "1621bd3ed011d9d097f9e14d02d6dc46315d7f76",
         "name" : "ピィディーシュシュ pd chou chou",
         "place_id" : "ChIJ51xj3CaAImARvCyadnIsP80",
         "rating" : 5,
         "reference" : "CmRSAAAAierUsOVdAv4O3Sc_X8WkWKuQnBykgbv55kCQP7zfMmZ25fb5vNyv3Gyc8EX5_oyOtraOFBUaNN5aMnzf5nlE3yfJ5EOn3wbFYtYCpVq2FURTNVfSvV2wtfd7ed45KAO4EhADGe86yTFM-kp0ZtF0WsZEGhRhcE71SGWDPX_ln4gt8H_fNxAqXA",
         "scope" : "GOOGLE",
         "types" : [ "point_of_interest", "establishment" ],
         "vicinity" : "はまゆうパスタビル5F, 1 Chome-2−8 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.688847,
               "lng" : 140.0213635
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69019598029149,
                  "lng" : 140.0227124802915
               },
               "southwest" : {
                  "lat" : 35.6874980197085,
                  "lng" : 140.0200145197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/school-71.png",
         "id" : "7e2fcb968d5ccad8c7d786618b86e1f19a5b1b5b",
         "name" : "Chiba Institute of Technology",
         "photos" : [
            {
               "height" : 3000,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/112346647569009984074/photos\"\u003e77 everlasting\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAiUujYBiUWOIJYeUnao_qcfO-BmVKyWpeCMRwtt2QoBLfsPLgZQLkIEY1Nm4FBPY2jYx5UifELmnc4VtUgK4sHtOaHjtl80BX8UoND_hL5zsIw4OsG8MjdQ8ndChIfk3vEhCeqkAizVzHZQg6PpDICg-TGhTOMmQ0laJ7VnUWK4N7nIgHah9r5Q",
               "width" : 4000
            }
         ],
         "place_id" : "ChIJgas4HCeAImARVrRb4XHtJps",
         "rating" : 4.1,
         "reference" : "CmRSAAAAzKNq_vC2vi5Gnmy1zw0WgJj4vkUqmNIu4M3Qk7iug9Rskv-tnjYMUmNwwJbFzX3ojdD7NjoPloZs-5S_zAfFs3E_xOdeJdl3ujYzqAP1qjJ4izVN01fEB7lAXL7LYKHLEhAs443cn5Pe7pwbom4jVSTOGhRL82NqeAPcuEJuOHxVKaIi4aJKZg",
         "scope" : "GOOGLE",
         "types" : [ "university", "point_of_interest", "establishment" ],
         "vicinity" : "2-17-1 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6918791,
               "lng" : 140.0213126
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6932280802915,
                  "lng" : 140.0226615802915
               },
               "southwest" : {
                  "lat" : 35.69053011970851,
                  "lng" : 140.0199636197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "377927b3f5fc697ce7d1e518ebeb137c1685edec",
         "name" : "本格カレーバイキングマンダラ 津田沼店",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 4032,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/113649682655274653862/photos\"\u003eYuuri S\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAhlFoLxs2PE5JG3r6Jp47AhCnfXAvlQiyy2v5DS0Une4JOrHmhJT-6AjUTlI1rhPEw9wgBrhVfVEeRd3e2gnAMV86A8CQtgG0Sw055tZjJMLLwa3-52_-fU-dWkIeWLGAEhC6saHRWnNiw8dxHQ3C3Xz0GhTcoD8vLWcMxQlL9KznVZKIvDVlzA",
               "width" : 3024
            }
         ],
         "place_id" : "ChIJ225dKSGAImARMTHT-Aa69YA",
         "price_level" : 1,
         "rating" : 1.8,
         "reference" : "CmRSAAAAT45ZFDFY-i2o3mpl630sT7wBUXAbC_WWu4Sz1-0MNxtmRow-jDisOCQnMgF6EDvARGIYJYikCpnIw0UtQI4LScCkpIoNm0airU6-bps4Im5pAvVj-HlsUEiUMu8sQRDtEhC3BZzdfUDynqxZAjsz6jDoGhS_nZjZY0o1cAvOJNbkBNW73CBWdg",
         "scope" : "GOOGLE",
         "types" : [ "restaurant", "food", "point_of_interest", "establishment" ],
         "vicinity" : "2 Chome-18-1 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.69356979999999,
               "lng" : 140.0233035
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.69491878029149,
                  "lng" : 140.0246524802915
               },
               "southwest" : {
                  "lat" : 35.6922208197085,
                  "lng" : 140.0219545197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "13aeb154bfa2010ad6b0151d81719a3a292147da",
         "name" : "ヘアーモッカ(hair mocca)",
         "place_id" : "ChIJs-7kZSGAImARRQVf0Rehabk",
         "reference" : "CmRSAAAAhfsGTaY7YkocNh37-LOJwsySZYMAu7IFdG5Fotkp3eOHGTPZVvYMbPTVXFvDtCyl4hRDtfL3aDsHHT-QB-C7w84K-Jj3InqJKUMhmdsEP4GFuqyG3n_ubgKti1bLC1WDEhCvpwCs82adTgqzMPxZeeASGhRyd-2q8_hOBGuJqlN2Jh_z08qQRw",
         "scope" : "GOOGLE",
         "types" : [ "hair_care", "point_of_interest", "establishment" ],
         "vicinity" : "2 Chome-22-17 Maebaranishi, Funabashi"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.691439,
               "lng" : 140.021835
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6927879802915,
                  "lng" : 140.0231839802915
               },
               "southwest" : {
                  "lat" : 35.6900900197085,
                  "lng" : 140.0204860197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "57b1bf5ba6e14c169262c96f6399527c1cf5448b",
         "name" : "マンボー津田沼店",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "place_id" : "ChIJE77B0iaAImARtuLgEdTw8OU",
         "rating" : 3.1,
         "reference" : "CmRSAAAA56caREUvqdtJztDhyKX2Fj7yFUHKW3ekXxMU6XffP6QBigXc4lMS_kgrawOON_Fv6NhbMtZ8AbdQ8SFbCRLkXXyGLAAjVDpNeU12OmQ4cYVqBPLAJynaQRE0cvugKcn4EhCkFmCuRtlQ8GTnzMkEQwqfGhT5kAOAl0G4j1Tr5CX8SLoRKo-2Fw",
         "scope" : "GOOGLE",
         "types" : [ "point_of_interest", "establishment" ],
         "vicinity" : "アイダビル3f, 1 Chome-11−4 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6910478,
               "lng" : 140.0202177
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6923967802915,
                  "lng" : 140.0215666802915
               },
               "southwest" : {
                  "lat" : 35.6896988197085,
                  "lng" : 140.0188687197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "536f0357b018f12f3bb7f2f284db374e69282afc",
         "name" : "デニッシュバー ディラ津田沼店",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "place_id" : "ChIJhYysyyCAImARAAlsbIpnR4E",
         "price_level" : 1,
         "rating" : 2,
         "reference" : "CmRSAAAAx4vRU8p4SPLs6RjIdAu7YQVlUpad2tQ-gx8o6IVhfBjybZdDQJjsSE_kLXbMocrDTb4MyINksGOi640fh-2yRQGK4R3gLkCjfq5zs86lJokIleY5U45m9_4biXg1CJM2EhBWpUhguDOy5dro4SLjOjMrGhTb4jDObdOF_xkyLhR4DXCkSDEEGA",
         "scope" : "GOOGLE",
         "types" : [ "food", "point_of_interest", "establishment" ],
         "vicinity" : "JR津田沼駅構内, 1 Chome-1−1 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6911312,
               "lng" : 140.0199439
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6924801802915,
                  "lng" : 140.0212928802915
               },
               "southwest" : {
                  "lat" : 35.6897822197085,
                  "lng" : 140.0185949197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "eba19ec7bc421d97020d8f7c919915a2b5212034",
         "name" : "ベッカーズ ホテルメッツ津田沼店",
         "opening_hours" : {
            "open_now" : true,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 1288,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/105475483656678217325/photos\"\u003e舘山文成\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAL56cgVg9R5b0NVu5_fdm6vR5Ckplq5x7zjliZAUPrO4hn1vpcaSgBgazV4d61NkyuMsrq6zwwlWLjMvYh44jD304Y_nGEaX368fij9ITLxRsKyCj7FR9bLbK3IWO8EXlEhATCU2VpLD-nDjv-07w9umgGhQTL74NCoqX7ctCX-vSgrsmzXHSMw",
               "width" : 1936
            }
         ],
         "place_id" : "ChIJYYLIziCAImARrSgbBemv6gU",
         "rating" : 3.3,
         "reference" : "CmRRAAAADg7YOe1PUqEtvjRBHX9cwAALc15MYZGwy64I1Jm3fPSkn2Lb6qZkhzoZzRMbvJgs-ndn_30zeg3kTSQKKtlEvMj22SH1qOrFX6ehKhHmdHf9nCk5zJwYw-MaY23qvRFPEhDhY5mFQ2OVx0zBBEc9Sw_SGhR9e7x9sP_X_qTiQMJdopPc0YOaug",
         "scope" : "GOOGLE",
         "types" : [ "restaurant", "food", "point_of_interest", "establishment" ],
         "vicinity" : "ホテルメッツ津田沼, 1F~2F, 1 Chome-1−1 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6942114,
               "lng" : 140.02497
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6955603802915,
                  "lng" : 140.0263189802915
               },
               "southwest" : {
                  "lat" : 35.6928624197085,
                  "lng" : 140.0236210197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "724dfd4448d54897383f4d311d6f74d39387bd97",
         "name" : "ヘアーサロン ノルテ(Hair Salon NORTE)",
         "place_id" : "ChIJi9vMxiOAImARa1JkJjsCPBo",
         "reference" : "CmRRAAAAgUJsQllj0GwWqS4NSxUMy0Ph5481jbeZTvePZrqG8Ljk6zzyAN9QyZU4WozNO1aaHIWfkx4g3pVoaiKgOI2M1JntQMb64-CSIvEXzPRAZbeKvWFi16JY1LbKS-LdQjYCEhCNqx7KaE-xAOdeM0oDoRdwGhT-ScAS6Nn5NSl7qeUOwskOZaIejw",
         "scope" : "GOOGLE",
         "types" : [ "hair_care", "health", "point_of_interest", "establishment" ],
         "vicinity" : "千葉県船橋市前原西2-25-6 2F"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.69053700000001,
               "lng" : 140.022693
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.6918859802915,
                  "lng" : 140.0240419802915
               },
               "southwest" : {
                  "lat" : 35.6891880197085,
                  "lng" : 140.0213440197085
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
         "id" : "45e330c3321ebbf703bf84eccf273e3dc1ecf2b7",
         "name" : "ザ・整体",
         "opening_hours" : {
            "open_now" : false,
            "weekday_text" : []
         },
         "photos" : [
            {
               "height" : 480,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/112374185892392037186/photos\"\u003eザ・整体\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAmK0t0qLOx_Jx-L0N1YWXleLjWi54RinNiYQZDmo_4oUeMB3H2cxjO6pGOcEMWPVGG6iGR1mk0cqucWbY_GU-CxLzo1EUR-PcftwEEw0ByORgyx70EUyflHuBWv6_F14xEhA5yepDAlCIJNUTwFmIpsyQGhTE_C0-kJARCrd_MCxn8ptZuHJrLA",
               "width" : 640
            }
         ],
         "place_id" : "ChIJ0U_dlCaAImAR08eE9UdUvIM",
         "rating" : 5,
         "reference" : "CmRSAAAAikw5IdB0tjixS3yE0tQcDk632MGCzemejjomNxBmi01ntBi636O0usrOE5EJbPQbRnnEFvOkX8RwNZwWJ5a1te0exMhmiAX1WPE4RnhjJ-8dQiux3kTRFo6XvzAXsIrTEhDZAKQf4gGdfLqQOPreYD7-GhSvoDpy0w9hsl7XFVVQp-PzsITdDQ",
         "scope" : "GOOGLE",
         "types" : [ "beauty_salon", "health", "point_of_interest", "establishment" ],
         "vicinity" : "津田沼十番街ビル702号, 1−10−41 Tsudanuma, Narashino"
      },
      {
         "geometry" : {
            "location" : {
               "lat" : 35.6830349,
               "lng" : 140.0243648
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 35.7082941,
                  "lng" : 140.0851601
               },
               "southwest" : {
                  "lat" : 35.652531,
                  "lng" : 139.9864994
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png",
         "id" : "5305bef486d8689d8f0191b467550f88fea3360f",
         "name" : "Narashino",
         "photos" : [
            {
               "height" : 1728,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/102084686430229311972/photos\"\u003e渡部敏広\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAq0Yu_Lqy7qHhD7JctJWua0bCif7lxReT0hWd75-tNjnx38PFcjY1k_dhMJuNGeX8a--IPhTDOzTHNt88-yMX8DkL0CKY7Bc5Xzd5QfmPcaIbQFbO6CnUERnmbQYrdYviEhBiQZAxPhzUR3jmgNaBzQtfGhRFFz5tNQRXOwX3TmSp6zlmHGfvwQ",
               "width" : 3072
            }
         ],
         "place_id" : "ChIJeeuzpMuBImARIcN5CQmfpeo",
         "reference" : "CmRbAAAANjCWyI9HmP9sguGPgRtPsOfD-iC993Lk46IoeDrHKSapkdnKE8PTvSsDxThfwWHnTKhiOmHsMFC9XWfIJlM1BGO5Mwms1XTcMajurTTrMwnVx6mG0zKwVsaxBCCicuFhEhCaIxj6-D76nBHFCqLoID7lGhT-L9NiTGApu0JUGBmu4gnhGrfRgA",
         "scope" : "GOOGLE",
         "types" : [ "locality", "political" ],
         "vicinity" : "Narashino"
      }
   ],
   "status" : "OK"
}
"""