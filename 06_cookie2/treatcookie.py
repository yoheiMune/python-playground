# -*- coding: utf-8 -*-
# Cookieの扱い
# はてなブックマークにログインする
# 参考：http://d.hatena.ne.jp/yatt/20110503/1304403694
# 参考：http://matsulib.hatenablog.jp/entry/2015/03/06/161546
# 参考：http://www.atsuhiro-me.net/python/dev/cookie

from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import pprint

# Cookie利用
opener = build_opener(HTTPCookieProcessor(CookieJar()))


# name, pwd = '**your username**', '**your password**'
with open('ipass') as f:
    name, pwd = tuple(f.read().split(','))

post = {
    'name': name,
    'password': pwd
}
data = urlencode(post).encode('utf-8')


# ログインCookieを取得
res = opener.open('https://www.hatena.ne.jp/login', data)
pprint.pprint(res.getheaders())
# with open('out1.html', 'w', encoding='utf-8') as f:
#     f.write(res.read().decode('utf-8'))
# res.close()
print('***************')

# 認証が必要なページを開く
url = "http://d.hatena.ne.jp/%s/edit" % name
print(url)
res = opener.open(url)
pprint.pprint(res.getheaders())
with open('out2.html', 'wb') as f:
    f.write(res.read())
res.close()
