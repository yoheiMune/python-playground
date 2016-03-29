# -*- coding: utf-8 -*-
#
# Sample of Python for Google Spreadsheet.
#
# ref: 
#   https://github.com/burnash/gspread
#
# API Document:
#   http://gspread.readthedocs.org/en/latest/
import json, re
import gspread
import oauth2client.client


"""
pip install --upgrade pyopenssl, pycrypto


ERROR!!

AttributeError: 'module' object has no attribute 'SignedJwtAssertionCredentials'
pip3 install "oauth2client<2.0"
"""

# Authorize.
json_key = json.load(open('client_secret.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = oauth2client.client.SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)


# 基本的な操作
#####################################
# ワークブックを開く
# 引数にワークブック名を指定する
wb = gc.open("Python_API_ACCESS_SAMPLE")

# シートを取得する
# 引数にシート名を指定する
sh = wb.worksheet("Sheet1")

# 指定したセルの値を更新する
sh.update_acell('B2', "it's down there somewhere, let me take another look.")

# Rangeでセル一覧を取得する
cell_list = sh.range('A1:B7')
print(cell_list)


# 開く
#####################################
# ファイル名を指定してワークブックを開く
wb = gc.open("Python_API_ACCESS_SAMPLE")

# シートIDを指定してワークシートを開く
sht1 = gc.open_by_key('1VTHyBs-EmWh7WVhFG7WmcuImZUsIPtrjP3hpLqQQhCc')

# URLを指定してワークシートを開く
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1VTHyBs-EmWh7WVhFG7WmcuImZUsIPtrjP3hpLqQQhCc/edit#gid=0')


# ワークシートを選択する
#####################################
# インデックスを指定して開く
worksheet = wb.get_worksheet(0)

# シート名を指定して開く
worksheet = wb.worksheet("私のシート")

# シート1を開く
worksheet = wb.sheet1

# シート一覧を取得する
worksheet_list = wb.worksheets()


# ワークシートを作成する
#####################################
worksheet = wb.add_worksheet(title="A worksheet", rows="100", cols="20")


# ワークシートを削除する
#####################################
wb.del_worksheet(worksheet)


# セルの値を取得する
#####################################
# ラベルを指定する
val = sh.acell('B1').value
print(val)

# 行番号と列番号を指定する
val = sh.cell(1, 2).value
print(val)


# 指定した行/列の値を全て取得する
#####################################
# 指定した行の値を全て取得する
values_list = sh.row_values(1)
print(values_list)

# 指定した列の値を全て取得する
values_list = sh.col_values(1)
print(values_list)


# シートの全ての値を取得する
#####################################
list_of_lists = sh.get_all_values()
print(list_of_lists)


# セルを見つける
#####################################
# 文字列で探す
cell = sh.find("John")
print("Found something at R%sC%s" % (cell.row, cell.col))

# 正規表現で探す
amount_re = re.compile(r'(Big|Enormous) dough')
cell = sh.find(amount_re)
print(cell)


# 合致する全てのセルを取得する
#####################################
# 文字列で探す
cell_list = sh.findall("Rug store")
print(cell_list)

# 正規表現で探す
criteria_re = re.compile(r'(Small|Room-tiering) rug')
cell_list = sh.findall(criteria_re)
print(cell_list)


# Cellオブジェクト
######################################
cell = sh.acell('A1')
value = cell.value        # 値
row_number = cell.row     # 行番号
column_number = cell.col  # 列番号


# セルの更新
######################################
# 指定したセルの値を更新する
sh.update_acell('B1', 'Bingo!')
sh.update_cell(1, 2, 'Bingo!')

# セルを纏めて更新する（バッチ処理）
cell_list = sh.range('H3:K4')
for cell in cell_list:
    cell.value = 'O_o'
sh.update_cells(cell_list)














