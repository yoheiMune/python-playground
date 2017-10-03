"""
    CSVやTSVファイルの読み書きのサンプル（csvモジュールを利用）

    参照：
        https://docs.python.jp/3/library/csv.html
"""
import csv

# CSVの書き込み
with open("a.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["name", "age"])
    writer.writerow(["Yohei", 31])
    writer.writerow(["Junji", 32])
    writer.writerow(["Kami,Shin", 50])  # クオートでエスケープしてくれる
    writer.writerow(['Cha"Shu', 50])  # クオートでエスケープしてくれる
    writer.writerow(["AA\nBB", 21])  # 改行も対応

# CSVの読み込み
with open("a.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for row in reader:
        print(row[0], row[1])

# DictWriter
with open("b.csv", "w", newline="") as f:
    fieldnames = ["firstname", "lastname"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"')
    writer.writeheader()
    writer.writerow({ "firstname" : "AA", "lastname" : "BB" })
    writer.writerow({ "firstname" : "CC", "lastname" : "DD" })

# DictReader
with open("b.csv", newline="") as f:
    reader = csv.DictReader(f, delimiter=",", quotechar='"')
    for row in reader:
        print(type(row))  # <class 'collections.OrderedDict'>
        print(row["firstname"], row["lastname"])