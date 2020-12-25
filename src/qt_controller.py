import requests
import os
import pathlib
from settings import secret_map, add_to_secrets


def get_user_account():
    if os.path.isfile('./src/tokens/qt_account_number.txt'):
        print("Existing Account Number Located... \U0001F44D")
        account_file = open('./src/tokens/qt_account_number.txt', 'r')
        account_number = account_file.readline()
    else:
        account_number = input("Enter the account number... \U0001F3E6 \n")
        pathlib.Path('./src/tokens').mkdir(parents=True, exist_ok=True)
        account_file = open('./src/tokens/qt_account_number.txt', 'w')
        account_file.write(account_number)
        account_file.close()

    accounts = get_accounts()
    for account in accounts:
        if account_number == account['number']:
            add_to_secrets('curr_account', account)
            return account

    print('Cannot find account! \U0001F622')
    raise


def get_accounts():
    endpoint = 'v1/accounts'
    url = secret_map['qt_server'] + endpoint
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {secret_map["qt_access"]}'
    }
    get = requests.get(url, headers=headers)
    get_json = get.json()
    return get_json['accounts']


def get_positions(account, simple=False):
    print('Fetching QuestTrade Position Data... \U0001F4C8 \n')
    account_number = account["number"]
    endpoint = f'v1/accounts/{account_number}/positions'
    url = secret_map['qt_server'] + endpoint
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {secret_map["qt_access"]}'
    }
    get = requests.get(url, headers=headers)
    get_json = get.json()

    if simple:
        position_info = {}
        total = 0
        for position in get_json['positions']:
            position_info[position['symbol']] = {
                'currentValue': position['currentMarketValue'],
            }
            total += position['currentMarketValue']
        return position_info, total
    else:
        return get_json['positions'], None

