"""
    importlibを用いて、動的インポートを行うサンプル.

    参照：
        https://docs.python.jp/3/library/importlib.html#importlib.import_module

    フォルダ構成：
        - sample_dynamic_import.py
        - jobs/
            - apple.py
            - orange.py

    利用イメージ：
        jobs/apple.py と jobs/orange.py を動的に読み込んで実行する
"""
from importlib import import_module

# importlib.import_module(name, package=None)

# appleを読み込む
module1 = import_module("jobs.apple")
module1.Worker.greeting()

# orangeを読み込む
module2 = import_module("jobs.orange")
module2.Worker.greeting()


# appleを読み込む（パッケージを指定した場合）
module1 = import_module(".apple", "jobs")
module1.Worker.greeting()
