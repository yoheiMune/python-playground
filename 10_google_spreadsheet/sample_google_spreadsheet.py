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


# Open Workbook.
wb = gc.open("Python_API_ACCESS_SAMPLE")


# Get Sheet.
sh = wb.worksheet("Sheet1")


# Update a cell.
sh.update_acell('B2', "it's down there somewhere, let me take another look.")


# Fetch a cell range
cell_list = sh.range('A1:B7')
print(cell_list)



# Open Sheet, Workbook
#####################################
# You can open a spreadsheet by its title as it appears in Google Docs
wb = gc.open("Python_API_ACCESS_SAMPLE") # <-- Look ma, no keys!

# If you want to be specific, use a key (which can be extracted from
# the spreadsheet's url)
sht1 = gc.open_by_key('1VTHyBs-EmWh7WVhFG7WmcuImZUsIPtrjP3hpLqQQhCc')

# Or, if you feel really lazy to extract that key, paste the entire url
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1VTHyBs-EmWh7WVhFG7WmcuImZUsIPtrjP3hpLqQQhCc/edit#gid=0')



# Select a worksheet.
#####################################
# Select worksheet by index. Worksheet indexes start from zero
worksheet = wb.get_worksheet(0)

# By title
worksheet = wb.worksheet("私のシート")

# Most common case: Sheet1
worksheet = wb.sheet1

# Get a list of all worksheets
worksheet_list = wb.worksheets()




# Create a worksheet.
#####################################
worksheet = wb.add_worksheet(title="A worksheet", rows="100", cols="20")


# Delete a worksheet.
#####################################
wb.del_worksheet(worksheet)


# Get a cell value.
#####################################
# With label
val = sh.acell('B1').value
print(val)

# With coords
val = sh.cell(1, 2).value
print(val)


# Get all values in a row / column.
#####################################
# Get all values from the first row
values_list = sh.row_values(1)
print(values_list)

# Get all values from the first column
values_list = sh.col_values(1)
print(values_list)


# Get all values in a sheet.
#####################################
list_of_lists = sh.get_all_values()
print(list_of_lists)


# Find a cell.
#####################################
# Find a cell with exact string value
cell = sh.find("John")
print("Found something at R%sC%s" % (cell.row, cell.col))

# Find a cell matching a regular expression
amount_re = re.compile(r'(Big|Enormous) dough')
cell = sh.find(amount_re)
print(cell)



# Find all matched cells.
#####################################
# Find all cells with string value
cell_list = sh.findall("Rug store")
print(cell_list)

# Find all cells with regexp
criteria_re = re.compile(r'(Small|Room-tiering) rug')
cell_list = sh.findall(criteria_re)
print(cell_list)


# Cell Object.
######################################
sh.acell('A1')
value = cell.value
row_number = cell.row
column_number = cell.col



# Cell Object.
######################################
sh.update_acell('B1', 'Bingo!')
# Or
sh.update_cell(1, 2, 'Bingo!')

# Select a range
cell_list = sh.range('H3:K4')
for cell in cell_list:
    cell.value = 'O_o'

# Update in batch
sh.update_cells(cell_list)













