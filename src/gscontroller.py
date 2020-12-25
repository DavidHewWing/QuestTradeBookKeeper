from __future__ import print_function
from settings import add_to_secrets
import os.path
import gspread


def get_headers(spreadsheet_id):
    gc = gspread.service_account(filename='./src/tokens/credentials.json')
    sheet = gc.open_by_key(spreadsheet_id)
    worksheet = sheet.get_worksheet(0)
    return worksheet.row_values(1)


def get_spreadsheet_id():
    if os.path.isfile('./src/tokens/spreadsheet_id.txt'):
        spreadsheet_file = open('./src/tokens/spreadsheet_id.txt', 'r')
        spreadsheet_id = spreadsheet_file.readline()
    else:
        spreadsheet_id = input('First time. Please input your spreadsheet id. \U0001F4C8 \n')
        spreadsheet_file = open('./src/tokens/spreadsheet_id.txt', 'w')
        spreadsheet_file.write(spreadsheet_id)
        spreadsheet_file.close()
    add_to_secrets('spreadsheet_id', spreadsheet_id)
    return spreadsheet_id
