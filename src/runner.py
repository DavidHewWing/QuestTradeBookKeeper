from src import qtauth
from settings import get_secrets, secret_map

get_secrets()
qtauth.qt_authentication(secret_map)
