# -*- coding: utf-8 -*-
#
# Sample chatwork api.
#
# ref:
#   http://developer.chatwork.com/ja/index.html
import urllib.request, urllib.parse, json
from pprint import pprint

# Base Url.
ENDPOINT = "https://api.chatwork.com/v1"


# Auth header.
with open("secret") as f:
    apikey = f.read()


# Room Id.
with open("secret2") as f:
    roomid = f.read()


# To memberid.
with open("secret3") as f:
    memberid = f.read()


# api.
def api (path, data=None):
    if data != None:
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8')
    headers = {"X-ChatWorkToken": apikey}
    req = urllib.request.Request(ENDPOINT + path, data=data, headers=headers)
    print(req.full_url)
    print(req.get_method())
    print(req.data)
    print(req.header_items())
    with urllib.request.urlopen(req) as res:
        result = json.loads(res.read().decode("utf-8"))
        info = dict(res.info())
        return (result, info)


# Get My Status.
# mystatus, info = api("/my/status")
# pprint(mystatus)
# """
# {
#   "unread_room_num": 2,
#   "mention_room_num": 1,
#   "mytask_room_num": 3,
#   "unread_num": 12,
#   "mention_num": 1,
#   "mytask_num": 8
# }
# """
# pprint(info)
# """
# HTTP/1.1 200 OK
# Content-Type: application/json
# X-RateLimit-Limit: 100
# X-RateLimit-Remaining: 44
# X-RateLimit-Reset: 1390941626
# """


# つぶやく
# path = "/rooms/%s/messages" % roomid
# data = {"body": "こんにちは、初めてのツイート!!!"}
# result, info = api(path, data)
# pprint(result)
# pprint(info)


# メンバー一覧
# result = api("/rooms/%s/members") % roomid
# pprint(result)


# To付きでつぶやく
path = "/rooms/%s/messages" % roomid
data = {"body": "[To:%s]こんにちは、初めてのツイート!!!" % memberid}
result, info = api(path, data)
pprint(result)
pprint(info)



























