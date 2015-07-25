#! /usr/bin/python
# -*- coding: utf-8 -*-
print "python"
print "モジュールのロード"

if __name__ == "__main__":
    print "main module"

# コメントアウト（1行）
"""
コメントアウト（複数行：ダブルクォート）
"""
'''
コメントアウト（複数行：シングルクォート）
'''

# 文字列表現
print "python"
print 'python'
print """
aaa
bbb
ccc
"""

# 文字列連結
test_str = "python" + "-" + "fun"
test_str += "123"
print test_str
price = 100
print str(price) + "円"

#分割
test_str = "python-fun"
print test_str.split("-")

# ゼロ埋め
test_str = "1234"
print test_str.rjust(10, "0")
print test_str.rjust(10, "!")
print test_str.zfill(10)

# 文字列の検索
test_str = "python-fun"
print test_str.startswith("python")
print test_str.startswith("fun")
print "f" in test_str
print "z" in test_str

# 大文字・小文字変換
test_str = "Yoheim.NET"
print test_str.upper()
print test_str.lower()

# 先頭・末尾の削除
test_str = "    YoheiM.NET"
print test_str.lstrip()
print test_str.lstrip().lstrip("Yohei")
test_str = "www.yoheim.net      "
print test_str.rstrip() + "/"
print test_str.rstrip().rstrip(".net")

# 四則演算
test_int = 100
print test_int + 10
print test_int - 10
print test_int * 10
print test_int / 10

# 数値に変換
test_int = "100"
print int(test_int) + 100


# 日付
import datetime

today = datetime.date.today()
print today
print today.year
print today.month
print today.day

todaydetail = datetime.datetime.today()
print todaydetail
print todaydetail.hour
print todaydetail.minute
print todaydetail.second
print todaydetail.microsecond

# 日付フォーマット
print today.isoformat()
print todaydetail.strftime("%Y/%m/%d %H:%M:%S")

# 日付の計算
# 明日
print today + datetime.timedelta(days=1)
# 1月1日
newyear = datetime.datetime(2015,1,1)
print newyear
# 1週間後
print newyear + datetime.timedelta(days=7)
# 1月1日から今日までの日数
print (todaydetail - newyear).days

# タプル
value = (1, 2, 3, 4)
print value
print value[0]

# リスト
list1 = ['python', '-', 'fun', '.', 'com']
print list1
for i in list1:
    print i
# 値の追加
list1.append('/blog')
print list1
# 値の追加2
list1.insert(0, 'www')
list1.insert(1, '.')
print list1
# 値の削除
list1.remove('fun')
print list1
print list1.pop(2)
print list1
# 値を見つける
print list1.index('com')
# 出現回数、全削除
print list1.count('.')
print list1
for i in range(list1.count('.')):
    list1.remove('.')
print list1

# ディクショナリー
dict1 = {'year': 2015, 'month': '6', 'day': 24}
print dict1
for i in dict1:
    print i, dict1[i]
# 値の取得
print dict1['year']
print dict1.get('year')
#print dict1['years']
print dict1.get('years')
print dict1.get('years', 'NOT FOUND')
# 値の設定
dict2 = {}
print dict2
dict2['name'] = 'Yohei'
dict2['age'] = 29
print dict2
# 値の削除
del dict2['age']
print dict2
# キーのリスト化
dict3 = {'name': 'yoheiM', 'age': 25, 'favorite': 'food'}
print dict3.keys()
# キーの存在確認
print dict3.has_key('name')
print dict3.has_key('lastName')
print 'age' in dict3
print 'ageha' in dict3

# インクリメント（++演算子はpythonにはない）
num = 100
num += 1
print num

# デクリメント（--演算子もpythonにはない）
num = 100
num -= 1
print num

# コマンドライン引数
import sys
params = sys.argv
print params
# print params[0] # プログラム名
# print params[1] # 引数1
# print params[2] # 引数2


# プログラムの終了
# sys.exit()


# if文
value = 3
if value == 1:
    print "value is 1"
elif value == 2:
    print "value is 2"
else:
    print "value is more than 2"

value1 = "python"
value2 = "love"
if value1 == "python" and value2 == "love":
    print "python love"
if value1 == "python" or value1 == "ruby":
    print "you may like python or ruby"

if value1 == "ruby":
    pass                    # passは珍しい・・・
elif value1 == "python":
    print "Hello Python"

x = "yes"  if value1 == "python" else "no"
print x


# for文
someArray  = ["a", "b", "c", "d", "e"]
someArray2 = [1, 2, 3, 4, 5]
for char in someArray:
    print char

# http://www.pythonweb.jp/tutorial/for/index3.html
for str in "Hello":
    print str

for val in range(0, 10):
    print val

# https://sites.google.com/site/kuraitlab/programing-language/python/python-loops
for a in range(10):
    if a == 5:
        print "five"
        continue
    if a == 7:
        break
    print a

# http://kesin.hatenablog.com/entry/2013/05/12/004541
for c in range(len(someArray)):
    print c, someArray[c]

for c, val in enumerate(someArray):
    print c, val

for char in reversed(someArray):
    print char,

for char, num in zip(someArray, someArray2):
    print char, num


# while文
counter = 0
while counter < 10:
    counter += 1
    print counter


# switch文： Pythonにはない



# printのいろいろ
print "aaaa",

print "%d年目の%s" % (100, "python")

obj = open("test.txt", "w")
print >> obj, "python lover"


# 例外処理
value1 = 100
value2 = "200"
try:
    print value1 + value2
except:
    print "演算に失敗しました"
finally:
    print "演算終了"

try:
    raise
except:
    print "例外発生！！"
    # print "------------------------------------"
    # print traceback.format_exc(sys.exc_info()[2])
    # print "------------------------------------"


# importとfrom
import testmod
testclass1 = testmod.testclass()
testclass1.testmethod("1")

from testmod import testclass
testclass2 = testclass()
testclass2.testmethod("2")


# 関数の作成
def test1():
    print "call test"
test1()
def test2(name):
    print "Hello ", name
test2('Yohei')
test2(name='Yohei')
def test3(name="NoName"):
    print "Hello", name
test3()


# クラスの作成
class someClass:
    def __init__(self, code, name):
        self.code = code
        self.name = name

aList = []
aList.append(someClass(1, 'Yohei'))
aList.append(someClass(2, 'Munesada'))
for value in aList:
    print "====== class ======"
    print "code -> ", value.code
    print "name -> ", value.name

# クラスの継承
class TestExtends(list):

    def __init__(self):
        list.__init__(self)

    def append(self, value):
        list.append(self, value)
        print "値が追加されました:" + value

test = TestExtends()
test.append('python')
test.append(',')
test.append('lover')
for i in test:
    print i


# パッケージ
import module1.calc
print module1.calc.plusValue(1, 2)

from module1 import calc
print calc.plusValue(100, 200)

#ラムダ式
func = lambda num1, num2: num1 + num2
print func(10, 100)































