import webbrowser
import requests
import pathlib
import os
import src.datastore_helper as datastore_helper
from .settings import add_to_secrets


def qt_authentication(secret_map):
    print("Authenticating QuestTrade... \U0001F512")
    account = secret_map['account']

    # If the account exists in the DB
    if account:

        print("Account info exists. Grabbing refresh_token... \U0001F419	")
        refresh_token = account['qt_refresh']
        datastore_helper.insert_new_account(secret_map['QT_API_KEY'], secret_map['account'])
        update_globals(secret_map['QT_API_KEY'], refresh_token, secret_map['account'])

    # if the account doesn't exist in the db then update
    else:
        # make a call to the API.
        print("Your first time. Please login... \U0001F409")
        redirect_uri = 'https://davidhewwing.github.io/QuestTradeBookKeeper/'
        url = f'https://login.questrade.com/oauth2/authorize?client_id=' \
              f'{secret_map["QT_API_KEY"]}' \
              f' &response_type=code&redirect_uri={redirect_uri}'
        webbrowser.open_new(url)
        code = input("Enter the code parameter... \U0001F4BB \n")

        # insert new account in DB
        refresh_token = get_refresh_token(secret_map['QT_API_KEY'], redirect_uri, code)
        new_account = new_account_script()
        new_account['qt_refresh'] = refresh_token
        datastore_helper.insert_new_account(secret_map['QT_API_KEY'], new_account)
        update_globals(secret_map['QT_API_KEY'], refresh_token, new_account)

    print('Authenticated QuestTrade! \U0001F603 \n')


def update_globals(name, refresh_token, account):
    url = f'https://login.questrade.com/oauth2/token?grant_type=refresh_token' \
          f'&refresh_token={refresh_token}'
    post = requests.post(url)
    post_json = post.json()
    add_to_secrets('account', account)
    add_to_secrets('qt_access', post_json["access_token"])
    add_to_secrets('qt_server', post_json["api_server"])

    account['qt_refresh'] = post_json['refresh_token']
    datastore_helper.insert_new_account(name, account)

# check if refresh tokens exists, if doesn't then create directory and file.
def get_refresh_token(key, redirect_uri, code):
    url = f'https://login.questrade.com/oauth2/token?client_id={key}' \
          f'&code={code}' \
          f'&grant_type=authorization_code' \
          f'&redirect_uri={redirect_uri}'
    post = requests.post(url)
    post_json = post.json()
    return post_json["refresh_token"]

def new_account_script():
    cash_invested = input('Enter the amount of cash invested. \U0001F4B0 \n')
    account_number = input('Enter your account number. \U0001F3E6 \n')
    spreadsheet_id = input('Enter the spreadsheet id. \U0001F4B9 \n')
    return {
        'cash_invested': cash_invested,
        'qt_account_number': account_number,
        'spreadsheet_id': spreadsheet_id
    }

