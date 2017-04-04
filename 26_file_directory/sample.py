# -*- coding: utf-8 -*-
"""
    The sample of files and directories.

    refs:
        http://www.gesource.jp/programming/python/code/index.html
        http://www.geocities.jp/morchin33/effective_python/file_system.html
"""

# ファイルの読み書き
with open("a.txt", "w") as f:
    f.write("memomemo")
with open("a.txt", "a") as f:
    f.write("MEMOMEMO")
with open("a.txt") as f:
    text = f.read()

# ファイルへのtouch
from pathlib import Path
Path("b.txt").touch()

# ファイルの削除
import os
os.remove("b.txt")

# ディレクトリの作成（単一）
import os
os.mkdir("mydir")

# ディレクトリの作成（階層あり）
import shutil
os.makedirs("mydir2/aaa/bbb/ccc")
shutil.rmtree("mydir2")

# ディレクトリの削除（空っぽの場合）
import os
os.rmdir("mydir")

# ディレクトリの削除（中身がある場合）
import shutil
os.mkdir("mydir")
Path("mydir/a.txt").touch()
shutil.rmtree("mydir")

# ファイルやディレクトリの存在確認
import os
print(os.path.exists("a.txt"))
print(os.path.exists("mydir"))

# ファイルが存在するかを確認する
import os
print(os.path.isfile("a.txt"))

# ディレクトリが存在するかを確認する
import os
print(os.path.isdir("mydir"))

# パスの結合
print(os.path.join("aaa", "bbb", "ccc", "my.txt")) # aaa/bbb/ccc/my.txt

# ファイルの拡張子を取得する
root, ext = os.path.splitext("/var/log/myapp/aaaa.log")
print(root, ext) # /var/log/myapp/aaaa, log

# ファイル一覧を取得する
os.mkdir("mydir")
Path("mydir/aa.txt").touch()
Path("mydir/bb.log").touch()
Path("mydir/cc.txt").touch()
os.mkdir("mydir/sub")
Path("mydir/sub/ddd.txt").touch()
files = os.listdir("mydir")
print(files) # ['aa.txt', 'bb.log', 'cc.txt']

# ワイルドカードを利用
from glob import glob
files = glob("mydir/*.txt")
print(files) # ['mydir/aa.txt', 'mydir/cc.txt']

# 再帰的にファイルを収集する
for root, dirs, files in os.walk('./mydir'):
    for fname in files:
        print(os.path.join(root, fname))

# 絶対パスの取得
print(os.path.abspath(".")) # /Users/munesadayohei/git/python-playground/26_file_directory
# 絶対パスかの確認
print(os.path.isabs("/var/log"))

# ファイル名を返す
print(os.path.basename("mydir/sub/ddd.txt"))  # ddd.txt

# ディレクトリ名を返す
print(os.path.dirname("mydir/sub/ddd.txt"))  # mydir/sub

# 最終アクセス日
print(os.path.getatime("a.txt")) # 1490175670.0
# 最終更新日
print(os.path.getmtime("a.txt")) # 1490175670.0

# ファイルサイズ
print(os.path.getsize("a.txt")) # 8

# ファイルのコピー
shutil.copyfile("a.txt", "c.txt")

# ディレクトリのコピー
shutil.copytree("mydir", "mydir3")

# ファイルやディレクトリの移動
shutil.move("c.txt", "d.txt")
shutil.move("mydir3", "mydir4")


shutil.rmtree("mydir")
shutil.rmtree("mydir4")