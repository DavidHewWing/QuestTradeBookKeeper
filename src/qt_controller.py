import requests
import os
import pathlib
from .settings import secret_map, add_to_secrets


def get_user_account(account_name):
    accounts = get_accounts()
    for account in accounts:
        if account_name == account['number']:
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


def get_positions(account_number, simple=False):
    print('Fetching QuestTrade Position Data... \U0001F4C8 \n')
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
                'entryPrice': position['averageEntryPrice'],
                'totalEntryPrice': position['averageEntryPrice'] * position['openQuantity'],
            }
            total += position['currentMarketValue']
        return position_info, total
    else:
        return get_json['positions'], None


def get_balances(account_number):
    print('Fetching QuestTrade Balance Data... \U0001F4BC')
    endpoint = f'v1/accounts/{account_number}/balances'
    url = secret_map['qt_server'] + endpoint
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {secret_map["qt_access"]}'
    }
    get = requests.get(url, headers=headers)
    get_json = get.json()
    for balance in get_json['perCurrencyBalances']:
        if balance['currency'] == 'USD':
            print('Retrieved Balance Data... \U0001F40E \n')
            return balance
    return None
