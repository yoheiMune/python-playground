import urllib.request
import json
from pprint import pprint


url = "https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json"
with urllib.request.urlopen(url) as res:
    emojiList = json.loads(res.read().decode('utf-8'))

output = {}
for emoji in emojiList:
    if emoji["has_img_apple"] and emoji["has_img_google"] and emoji["category"]:

        # tmp
        if emoji["unified"].find("-") == -1:
            items = output.get(emoji["category"], [])
            items.append(emoji["unified"])
            output[emoji["category"]] = items

with open("emoji.json", "w") as f:
    json.dump(output, f, indent=2)