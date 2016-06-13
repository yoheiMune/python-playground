# パッケージ例
from weather import daily, weekly

print("今日の天気：", daily.forecast())

for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)