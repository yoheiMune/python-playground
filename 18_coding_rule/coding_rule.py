# Coding rules for Python

# refs:
#   http://legacy.python.org/dev/peps/pep-0008/
#   http://pep8-ja.readthedocs.io/ja/latest/


### インデント
# 行を継続する場合は、折り返された要素を縦に揃える

# 開きカッコで揃える
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# この行とそれ以外を区別するために、インデントを深くする
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 突き出しインデントはインデントレベルを深くする
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# NG：折り返された要素を縦に揃えていない
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# NG：インデントが区別できない
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

## IF文の条件が長い場合には、以下のようにインデントを取る
# 追加のインデントをしない
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# 継続された行の条件をインデントする
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

## 行を継続して波カッコ/ブランケット/カッコを閉じる場合は、以下2種類のどちらか
my_list = [
    1, 2, 3,
    4, 5, 6
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f'
    )

my_list = [
    1, 2, 3,
    4, 5, 6
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f'
)

### 1行の長さ
# 最大79文字以内に制限
# docstringやコメントのように構造制限が少ないものは、72文字以内
# ただし、チームで合意できればそれより長くてもOK


# 2項演算子は前に揃える
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

### 空行
# トップレベルの関数やクラスは、2行ずつ空けて定義する
# クラス内部では、1行ずつ空けてメソッドを定義する
# 関連する関数のグループを分けるために、2行以上開けてもOK（ただし控えめに）


### import
## モジュールごとに行を分ける
# Good
import os
import sys
# 悪い
import os, sys

# しかし以下の場合はOK
from subprocess import Popen, PIPE

# 絶対importを推奨
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# しかし、絶対importを使うと不必要に冗長になる複雑なパッケージレイアウトの時は、
# 相対importもOK
from . import sibling
from .sibling import example

# ワイルドカードを使ったインポートは避けるべき
# どの名前が名前空間に存在しているかわかりにくく、
# 名前の上書きをしてしまった場合に、デバッグが非常にしづらい
# 悪い例：
from somemodule import *



### 式や文中の空白文字

# 余計な空白を使うのはダメ。
# カッコやブランケット、波かっこのはじめと直後、終わりの直前

# 良い
spam(ham[1], {eggs: 2})
# 悪い
spam( ham[ 1 ], { eggs: 2 } )

# カンマやセミコロン、コロンの直前

# 良い
if x == 4 print x, y; x, y = y, x
# 悪い
if x == 4 print x , y ; x , y = y , x

# しかし、スライスではコロンは二項演算子のように振る舞います。
# よって、両側に同じ数のスペースを置くべきです。
# また、拡張スライスでも、両側に同じスライスを置かなければなりません。
# 例外：スライスのパラメータが省略された場合には、スペースも省略できます

# 良い
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower:upper:step]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# 悪い
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

# 関数呼び出しの引数リストを始める開きかっこの直前は無駄な余白を入れない。
# 良い
spam(1)
# 悪い
spam (1)

# インデックスやスライスの開きかっこ直前も不要。
# 良い
dct["key"] = lst[index]
# 悪い
dct ["key"] = lst [index]

# 代入演算子を揃えるための、無駄な余白はダメ
# 良い
x = 1
y = 2
long_variable = 3

# 悪い
x             = 1
y             = 2
long_variable = 3


# 次の二項演算子は、両側に常に一つだけスペースを入れる
# 代入演算子（=）
# 拡張代入演算子（+=, -=）
# 比較演算子（ ==, <, >, !=, <>, <=, >=, in, not in, is, is not）
# ブール演算子（and, or, not）

# 優先順位が違う演算子を扱う場合、優先順位が一番低い演算子の両側に
# スペースを入れることを検討しましょう。入れるかどうかは任意ですが、
# 2つ以上のスペースは絶対に使わないこと。そして、二項演算子の両側には
# 常に同じ数の空白文字を入れる。

# 良い
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*x
c = (a+b) * (a-b)

# 悪い
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# キーワード引数やデフォルトパラメータであることを示すために使う
# =の両側にスペースは入れない

# 良い
def complet(real, imag=0.0):
    return magic(r=real, i=imag)

# 悪い
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# 関数アノテーションは、コロンに関する通常のルール（コロンの前には
# 余計なスペースを入れない）を守りつつ、->演算子がある場合は、その両側には
# 常にスペースを入れるようにする

# 良い
def munge(input: AnyStr): ...
def munge () -> AnyStr: ...

# 悪い
def munge(input:AnyStr): ...
def munge()->PosInt: ...


### 命名規則

# 前アンダースコア
# _single_leading_underscore：内部だけで使うことを示します。
# 例えば from M import * は、アンダースコアで始まる名前のオブジェクトをインポートしない。

# 後ろアンダースコア
# single_trailing_underscore_は、Pythonのキーワードと衝突するのを避ける
# ために使われます。例えば、以下のような使い方です。
Tkinter.Toplevel(master, class_="ClassName")

# __double_leading_underscoreは、クラスの属性に名前を付ける時に、
# 名前のマングリング機構を呼び出します（クラスFoobarの__booという名前は、
# _FooBar__booになります。
class FooBar:
    __boo = "aaa"

# モジュール名
# すべて小文字の短い名前。読みやすくするためにアンダースコアを使っても良い。
my_module

# パッケージ名
# すべて小文字の短い名前。アンダースコアの利用は推奨されていない。
mypackage

# クラス名
# CapWordsを利用する
MyClass

# 例外の名前
# 例外はクラスであるべきで、名前はCapWords形式を採用すべきです。
# ただしその例外が実際にエラーである場合には、末尾にErrorをつけます。
MyError

# 関数の名前
# すべて小文字を使い、読みやすくするために必要に応じてアンダースコアも利用出来る
my_function
# ただし、すでにmixedCaseがつかわれている場合は、互換性を保つためにmixedCaseを使うこともできます。
saySomething

# 関数の引数
# インスタンスメソッドの場合は、必ず最初はselfにします。
def my_function(self, xxx):
    pass
# クラスメソッドの場合は、必ずclsにします。
def my_class_function(cls, xxx) :
    pass
# 引数の変数名が予約語と被る場合は、末尾にアンダースコアをつけます。
def my_function(self, id_, dict_):
    pass

# 定数
# 全て大文字で書き、必要に応じてアンダースコアを利用することもできます
MY_CONSTS












































