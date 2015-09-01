# -*- coding: utf-8 -*-
#
# リストの利用についてまとめた
#

# https://docs.python.org/2/tutorial/datastructures.html


#### リストの基本機能
###############################################
# 生成
list01 = ["a", "a", "c", "c", 1, 1.4]
# 後ろに追加
list01.append("b")
# 前に追加
list01.insert(0, "z")
# 任意の場所に追加
list01.insert(2, "hoge")
# 配列に配列を追加
list01.extend([10, 20, 30, 10, 20, 30])
list02 = list01 + [1,2,3,4,5]
# 要素の削除（複数存在する場合は1つ目のみ）
list01.remove("c")
# 要素の削除（複数存在するものを全部）
list01 = [item for item in list01 if item is not "c"]
# または
list01 = filter(lambda a: a != "c", list01)
# indexを指定して削除
del list01[0]
del list01[1:2]
# del list01[:]
# 最後の要素を取得して同時に削除する
item = list01.pop()
# 指定した位置の要素を取得して同時に削除する
item = list01.pop(1)
# 指定した要素の位置を取得する
index = list01.index(1.4)
# 指定した要素の出現回数を取得する
count = list01.count(10)
# サイズを確認する
len(list01)

# 範囲指定で取り出す
print list01[0:1]
print list01[0:-1]
print list01[:3]
print list01[3:]

# 置換
print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
list02 = list("abcde")
list02[3] = "D"
list02[:3] = ["A", "B", "C"]
list02[-1:] = ["E", "F"]
print list02
#http://d.hatena.ne.jp/yumimue/20071205/1196839438



# ソートする（元のリスト自体をソートする）
list01.sort()
# ソートする（元のリストは変更しない）
list01 = sorted(list01)
# ソート条件を指定する（cmp）
list01.sort(cmp=lambda x,y: x<y)
list01 = sorted(list01, cmp=lambda x,y:x<y)
# ソートの前処理を指定する
["a", "AA" , "Ab", "ac"].sort(key=str.lower)
sorted(["a", "AA" , "Ab", "ac"], cmp=lambda x,y:x<y)
# 逆順にソートする（元のリスト自体をソートする）
list01.sort(reverse=True)
# または（元のリストは変更しない）
list01 = list(reversed(list01))
# または（トリッキー）
list01 = list01[::-1]

print list01


# Stuckとして利用する
stuck = [3,4,5]
stuck.append(6)
stuck.append(7)
print stuck.pop()
print stuck.pop()
print stuck


# キューとして利用する
# リストのappendとpop(0)で実現できるが、
# pop(0)を行うと全要素の位置を変更するため遅いとのこと
# 代わりに以下の実装を利用すると高速
from collections import deque
queue = deque(["A", "B", "C"])
queue.append("D")
print queue.popleft()
print queue


# 関数プログラミング（filter、map、reduce）
list01 = [1,2,3,4,5]
print filter(lambda x: x % 2 is 0, list01)
def isEven(x): return x % 2 is 0
print filter(isEven, list01)
print map(lambda x:x*2, list01)
def makeDouble(x): return x * 2
print map(makeDouble, list01)
print reduce(lambda x,y:x*y, list01)
def multiple(x,y): return x * y
print reduce(multiple, list01)


# リスト内包
print [i for i in range(10)]
print [i * 2 for i in range(10)]
print [i * 2 for i in range(10) if i % 2 is 1]
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# ループ処理（indexも一緒に取得したい）
for i, v in enumerate(["a","b","c"]):
    print i, v

# ループ処理（2つの配列を同時に処理する）
firstNames = ["a", "b", "c"]
lastNames  = ["A", "B", "C"]
for f, l in zip(firstNames, lastNames):
    print f, l

# ループ中に、ループ対象のリストを処理する
list01 = range(10)
for i in list01[:]:
    if i % 3 is 0:
        list01.append(i)
print list01


# 文字列からリストを作る
print list("12345")
print "1,2,3,4,5".split(",")

# 要素の存在確認
list01 = [1,2,3,4,5]
print 2 in list01
print 6 in list01

























