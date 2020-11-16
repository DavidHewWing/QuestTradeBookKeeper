import webbrowser
from settings import secret_map, get_secrets

get_secrets()


def qt_authentication():
    url = f'https://login.questrade.com/oauth2/authorize?client_id=' \
          f'{secret_map["QT_API_KEY"]}' \
          f' &response_type=code&redirect_uri={secret_map["QT_REDIRECT"]}'
    print(url)
    webbrowser.open_new(url)

qt_authentication()
