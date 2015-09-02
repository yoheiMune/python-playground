# -*- coding: utf-8 -*-
# python3
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
print(jsonString)
# ソート
data = {
    "c": 1,
    "b": 2,
    "a": 3
}
print(json.dumps(data, sort_keys=True))
# セパレーター指定（1つ目がカンマの代わり、2つ目がコロンの代わり）
print(json.dumps(data, separators=("=", "*")))
# 整形
print(json.dumps(data, indent=2))


print("================================")


### JSON DUMP（Pythonオブジェクト -> 文字列）
# 基本
jsonString = '''
{
    "name": "yohei",
    "age": 29,
    "favorites": ["programming", "python"]
}
'''
print(json.loads(jsonString))

# 値の操作
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
print(json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex))

import decimal
print(json.loads("1.1", parse_float=decimal.Decimal))

# JSONエンコーダーの拡張
import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

print(json.dumps(2 + 1j, cls=ComplexEncoder))
print(ComplexEncoder().encode(2 + 1j))



# ファイルソースから読み込み
f = open("./user1.json")
print(json.load(f))

# ファイルへの書き出し
dict = {
    "name": "あああ",
    "age": 50
}
# f = open("./user2.json", "w")
# json.dump(dict, f, ensure_ascii=False)



jsonString = '''
{
    "name": "aaa",
    "age": 30
}
'''
data = json.loads(jsonString)
print(data)
print(data["name"])


# "user2.json"
# {
#     "name": "いいい",
#     "age": 20  
# }
f = open("user2.json")
data = json.load(f)
print(data)
print(data["name"])




# dumps
print("===============================")
dict = {
    "name": "aaa",
    "age": 30
}
jsonstring = json.dumps(dict)
print(jsonstring)

dict = {
    "name": "あああ",
    "age": 30
}
jsonstring = json.dumps(dict, ensure_ascii=False)
print(jsonstring) # {"age": 30, "name": "あああ"}


print("===============================")
dict = {
    "name": "aaa",
    "age": 30
}
f = open("output.json", "w")
json.dump(dict, f)

dict = {
    "name": "あああ",
    "age": 30
}
f = open("output2.json", "w")
json.dump(dict, f, ensure_ascii=False)


print("===============================")
dict = {
    "name": "aaa",
    "age": 30
}
jsonstring = json.dumps(dict, indent=2)
print(jsonstring)


dict = {
    "c": 1,
    "b": 2,
    "a": 3
}
print(json.dumps(dict, sort_keys=True, indent=2))



dict = {
    "a": 1,
    "b": 2
}
print(json.dumps(dict, separators=("*", "="), indent=2))





def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
jsonstring = '''
{
    "__complex__": true, 
    "real": 1, 
    "imag": 2
}
'''
print(json.loads(jsonstring, object_hook=as_complex))































