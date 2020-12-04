from __future__ import print_function
from settings import add_to_secrets
import os.path


def sample(gs_service, spreadsheet_id):
    sheet = gs_service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range='Bought vs. Market!A:B').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)


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
