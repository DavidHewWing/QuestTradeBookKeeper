import webbrowser
import requests
import pathlib
import os
from settings import add_to_secrets


def qt_authentication(secret_map):
    print("Authenticating QuestTrade... \U0001F512")
    if os.path.isfile('./src/tokens/qt_refresh.txt'):
        print("Tokens exists. Grabbing refresh_token... \U0001F419	")
        token_file = open('./src/tokens/qt_refresh.txt', 'r')
        refresh_token = token_file.readline()
    else:
        print("Your first time. Please login... \U0001F409")
        redirect_uri = 'https://davidhewwing.github.io/QuestTradeBookKeeper/'
        url = f'https://login.questrade.com/oauth2/authorize?client_id=' \
              f'{secret_map["QT_API_KEY"]}' \
              f' &response_type=code&redirect_uri={redirect_uri}'
        webbrowser.open_new(url)
        code = input("Enter the code parameter... \U0001F4BB \n")
        refresh_token = get_refresh_token(secret_map, redirect_uri, code)
    url = f'https://login.questrade.com/oauth2/token?grant_type=refresh_token' \
          f'&refresh_token={refresh_token}'
    post = requests.post(url)
    post_json = post.json()
    update_refresh_token(post_json["refresh_token"])
    add_to_secrets('qt_access', post_json["access_token"])


# check if refresh tokens exists, if doesn't then create directory and file.
def get_refresh_token(secret_map, redirect_uri, code):
    url = f'https://login.questrade.com/oauth2/token?client_id={secret_map["QT_API_KEY"]}' \
          f'&code={code}' \
          f'&grant_type=authorization_code' \
          f'&redirect_uri={redirect_uri}'
    post = requests.post(url)
    post_json = post.json()
    update_refresh_token(post_json["refresh_token"])
    return post_json["refresh_token"]


def update_refresh_token(refresh_token):
    pathlib.Path('./src/tokens').mkdir(parents=True, exist_ok=True)
    token_file = open('./src/tokens/qt_refresh.txt', 'w')
    token_file.write(refresh_token)
    token_file.close()
