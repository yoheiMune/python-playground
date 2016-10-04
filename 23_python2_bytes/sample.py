# -*- coding: utf-8 -*-
# Python2

# 文字列をサンプルデータとして書き出す
content = u"abc123あいうえお"
data = content.encode("utf-8")
open("./data", "wb").write(data)

data = open("./data", "rb").read()
print("size:", len(data))
for i in range(len(data)):
    print(data[i].encode('hex'))