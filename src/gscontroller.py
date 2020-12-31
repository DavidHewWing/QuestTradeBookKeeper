from __future__ import print_function
from settings import add_to_secrets
from datetime import datetime
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


def update_headers(spreadsheet_id, column, symbol):
    gc = gspread.service_account(filename='./src/tokens/credentials.json')
    sheet = gc.open_by_key(spreadsheet_id)
    worksheet = sheet.get_worksheet(0)
    worksheet.add_cols(1)
    worksheet.update_cell(1, column, symbol)


def get_header_values(total, positions, balance):
    date = datetime.today().strftime('%Y-%m-%d')
    uninvested_cash = balance['cash']
    market_value = total
    buy_in_price = 0

    for position in positions:
        buy_in_price += positions[position]['totalEntryPrice']

    return {
        'Date': date,
        'Uninvested': uninvested_cash,
        'Buy-In Price': buy_in_price,
        'Market Value': market_value,
        'Increase': market_value - buy_in_price
    }


def append_row(spreadsheet_id, values):
    print('Appending Position Data in Google Sheets... \U0001F44D')
    gc = gspread.service_account(filename='./src/tokens/credentials.json')
    sheet = gc.open_by_key(spreadsheet_id)
    worksheet = sheet.get_worksheet(0)
    worksheet.append_row(values, 'USER_ENTERED')
    print('Finished! \U0001F496 \n')
