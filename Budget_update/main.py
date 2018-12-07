import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Gsheets-Budget-710900d21e8b.json', scope)
gc = gspread.authorize(credentials)

sh = gc.open('Budget_Test')
wks = sh.worksheet("Transactions")

# date
# discription
# amount
# category
# account


exampleFile = open('CSV/BOA/Test.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
# def update_row():
#     for 
#         wks.append_row([date, discription, amount, category, account])


#print(wks.get_all_records())
#wks.append_row(['Add 1', 'Add 2'])
#wks.delete_row(2)
# print(wks.acell('A4'))
# print(wks.cell(2,4)).value

# for cell in list_of_cell:
#     cell.value = "loop"
