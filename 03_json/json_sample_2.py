# -*- coding: utf-8 -*-
# JSONモジュールを色々と使ってみるサンプル
# 参照：https://docs.python.org/2/library/json.html
import json


### JSON DUMP（Pythonオブジェクト -> 文字列）
# 基本
data = {
    "name": "fumufumu",
    "age": 22,
    "friends": ["miu", "miu2"]
}
jsonString = json.dumps(data)
print jsonString
# ソート
data = {
    "c": 1,
    "b": 2,
    "a": 3
}
print json.dumps(data, sort_keys=True)
# セパレーター指定（1つ目がカンマの代わり、2つ目がコロンの代わり）
print json.dumps(data, separators=("=", "*"))
# 整形
print json.dumps(data, indent=2)


print "================================"


### JSON DUMP（Pythonオブジェクト -> 文字列）
# 基本
jsonString = '''
{
    "name": "ようへい",
    "age": 29,
    "favorites": ["programming", "python"]
}
'''
print json.loads(jsonString)

# 値の操作
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
print json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)

import decimal
print json.loads("1.1", parse_float=decimal.Decimal)

# JSONエンコーダーの拡張
import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

print json.dumps(2 + 1j, cls=ComplexEncoder)
print ComplexEncoder().encode(2 + 1j)




# ファイルソースから読み込み
# import codecs
# inputfile = codecs.open('./user1.json', 'r', 'utf-8')
# for f in inputfile:
#     print f.encode('utf-8')


f = open("./user1.json")
# print f.read()
j = json.load(f)
print j["name"]

# ファイルへの書き出し
dict = {
    "name": "あああ",
    "age": 50
}
f = open("./user2.json", "w")
json.dump(dict, f, ensure_ascii=False)















