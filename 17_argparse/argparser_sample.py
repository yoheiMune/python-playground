# Sample of argparser module.
# ref: http://docs.python.jp/3.5/howto/argparse.html
import argparse

# 引数パーサーの起動
# parser = argparse.ArgumentParser()
# parser.parse_args()
"""
$ python3 argparser_sample.py

$ python3 argparser_sample.py -h
usage: argparser_sample.py [-h]

optional arguments:
  -h, --help  show this help message and exit

$ python3 argparser_sample.py --help
usage: argparser_sample.py [-h]

optional arguments:
  -h, --help  show this help message and exit
"""

# 位置引数の取得
# parser = argparse.ArgumentParser()
# parser.add_argument("date")
# args = parser.parse_args()
# print(args.date)
"""
$ python3 argparser_sample.py
usage: argparser_sample.py [-h] date
argparser_sample.py: error: the following arguments are required: date

$ python3 argparser_sample.py 2016-05-12
2016-05-12

$ python3 argparser_sample.py -h
usage: argparser_sample.py [-h] date

positional arguments:
  date

optional arguments:
  -h, --help  show this help message and exit
"""


# 位置引数の取得（説明付き）
# parser = argparse.ArgumentParser()
# parser.add_argument("date", help="the target date for summrizing data.")
# args = parser.parse_args()
# print(args.date)
"""
$ python3 argparser_sample.py -h
usage: argparser_sample.py [-h] date

positional arguments:
  date        the target date for summrizing data.

optional arguments:
  -h, --help  show this help message and exit
"""

# 位置引数（型チェック指定あり）
# parser = argparse.ArgumentParser()
# parser.add_argument("square", 
#                     help="display a square of a given value",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)
"""
$ python3 argparser_sample.py 4
16

$ python3 argparser_sample.py fourusage: argparser_sample.py [-h] square
argparser_sample.py: error: argument square: invalid int value: 'four'
"""


# Optional引数の導入
parser = argparse.ArgumentParser()
parser.add_argument("--date",
                    help="the date for summarizing date.")
args = parser.parse_args()
if args.date:
    print("args.date is defined. date = " , args.date)
else:
    print("args.date is undefined.")
"""
$ python3 argparser_sample.py --date 2016-05-12
args.date is defined. date =  2016-05-12

$ python3 argparser_sample.py
args.date is undefined.

$ python3 argparser_sample.py --date
usage: argparser_sample.py [-h] [--date DATE]
argparser_sample.py: error: argument --date: expected one argument

$ python3 argparser_sample.py -h
usage: argparser_sample.py [-h] [--date DATE]

optional arguments:
  -h, --help   show this help message and exit
  --date DATE  the date for summarizing date.
"""

# Optional引数の指定（値は指定せずオプションのみ指定）
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose",
#                     help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on.", args.verbose)
"""
$ python3 argparser_sample.py --verbose
verbosity turned on. True
"""


# 位置引数とOptionalの併用
# parser = argparse.ArgumentParser()
# parser.add_argument("date",
#                     help="the date for summarizing date.")
# parser.add_argument("--verbose",
#                     help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("the date specified is ", args.date)
# else:
#     print(args.date)
"""
$ python3 argparser_sample.py 2016-05-12 --verbose
the date specified is  2016-05-12

$ python3 argparser_sample.py 2016-05-12
2016-05-12
"""
























