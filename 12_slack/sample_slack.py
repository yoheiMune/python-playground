# -*- coding: utf-8 -*-
"""
    Sample Slack Api Usage.

    ref:
        http://kazu22002.hatenablog.com/entry/2015/04/20/003345
        https://api.slack.com/methods
        https://api.slack.com/web#basics
"""
import urllib.request, urllib.parse, json
from pprint import pprint

END_POINT = "https://slack.com/api"
channel_id = "C0MLVSF1B"


# Load a token.
with open("secret") as f:
    token = f.read()


# api.
def api (path, data=None):
    url = END_POINT + path
    if data == None:
        data = {}
    data["token"] = token
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        ret  = json.loads(res.read().decode("utf-8"))
        return ret
        


# List of channels.
result = api("/channels.list")
pprint(result)
"""
{
    "ok": true,
    "channels": [
        {
            "id": "C024BE91L",
            "name": "fun",
            "created": 1360782804,
            "creator": "U024BE7LH",
            "is_archived": false,
            "is_member": false,
            "num_members": 6,
            "topic": {
                "value": "Fun times",
                "creator": "U024BE7LV",
                "last_set": 1369677212
            },
            "purpose": {
                "value": "This channel is for fun",
                "creator": "U024BE7LH",
                "last_set": 1360782804
            }
        },
        ....
    ]
}
"""


# Post a message.
# result = api("/chat.postMessage", {
#     'token':token,
#     'channel':channel_id,
#     'text': 'Hello from api'    
# })
# pprint(result)
# """
# {'channel': 'C0MLVSF1B',
#  'message': {'subtype': 'bot_message',
#              'text': 'Hello from api',
#              'ts': '1455681470.000006',
#              'type': 'message',
#              'username': 'bot'},
#  'ok': True,
#  'ts': '1455681470.000006'}
# """






















