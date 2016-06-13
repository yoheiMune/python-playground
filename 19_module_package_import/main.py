### モジュールとインポート

# import report
# weather = report.get_description()
# print("Today's weather:", weather)


# 別名でインポートする
# import report as rp
# weather = rp.get_description()
# print("Today's weather:", weather)

# 必要なものだけをインポートする
# from report import get_description
# weather = get_description()
# print("Today's weather:", weather)

# モジュールインポート先
import sys
from pprint import pprint
pprint(sys.path)

"""
[~/Desktop]$ cd ~/git/python-playground/
[~/git/python-playground][master]$ ll
total 8
drwxr-xr-x  6 munesadayohei  staff  204  7 25  2015 01_all
drwxr-xr-x  3 munesadayohei  staff  102  7 25  2015 02_list_sample
drwxr-xr-x  9 munesadayohei  staff  306  9  1  2015 03_json
drwxr-xr-x  5 munesadayohei  staff  170  3 29 10:54 04_google_analytics
drwxr-xr-x  2 munesadayohei  staff   68 10 23  2015 05_scikit_learn
drwxr-xr-x  5 munesadayohei  staff  170 11  3  2015 06_cookie
drwxr-xr-x  7 munesadayohei  staff  238 11  3  2015 06_cookie2
drwxr-xr-x  2 munesadayohei  staff   68 11 16  2015 07_django
drwxr-xr-x  5 munesadayohei  staff  170 11 17  2015 08_flask
drwxr-xr-x  4 munesadayohei  staff  136  2  2 13:13 09_wordnet
drwxr-xr-x  6 munesadayohei  staff  204  2 17 09:44 10_google_spreadsheet
drwxr-xr-x  6 munesadayohei  staff  204  2 17 11:52 11_chatwork
drwxr-xr-x  4 munesadayohei  staff  136  2 17 12:42 12_slack
drwxr-xr-x  3 munesadayohei  staff  102  4 18 20:39 13_dateutil
drwxr-xr-x  4 munesadayohei  staff  136  4 27 12:52 14_holiday
drwxr-xr-x  6 munesadayohei  staff  204  5  4 00:21 15_google_oauth
drwxr-xr-x  3 munesadayohei  staff  102  4 28 13:45 16_python_safari
drwxr-xr-x  3 munesadayohei  staff  102  5 21 22:47 17_argparse
drwxr-xr-x  3 munesadayohei  staff  102  6  2 09:48 18_coding_rule
-rw-r--r--  1 munesadayohei  staff   20  6 23  2015 README.md
-rw-r--r--  1 munesadayohei  staff    0  5 25 09:56 my-gitignore-target.txt
-rw-r--r--  1 munesadayohei  staff    0  5 27 00:32 my-global-gitignore-target.txt
[~/git/python-playground][master]$ 
[~/git/python-playground][master]$ mkdir 19_module_package_import
[~/git/python-playground][master]$ cd 19_module_package_import/
[~/git/python-playground/19_module_package_import][master]$ clear





[~/git/python-playground/19_module_package_import][master]$ touch main.py
[~/git/python-playground/19_module_package_import][master]$ touch module.py
[~/git/python-playground/19_module_package_import][master]$ mv module.py report.py
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    weather = report.get_description()
  File "/Users/munesadayohei/git/python-playground/19_module_package_import/report.py", line 7, in get_description
    return choice(wheters)
NameError: name 'wheters' is not defined
[~/git/python-playground/19_module_package_import][master]$ 

[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: rain
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: fog
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: snow
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: sun
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: who knows
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
  File "main.py", line 11
    from report as rp
                 ^
SyntaxError: invalid syntax
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: sun
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: who knows
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
Today's weather: fog
[~/git/python-playground/19_module_package_import][master]$ python3 main.py 
['/Users/munesadayohei/git/python-playground/19_module_package_import',
 '/Library/Frameworks/Python.framework/Versions/3.4/lib/python34.zip',
 '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4',
 '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin',
 '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages']
[~/git/python-playground/19_module_package_import][master]$ 
"""
















































