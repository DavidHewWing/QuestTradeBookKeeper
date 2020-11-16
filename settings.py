import os
from dotenv import load_dotenv

load_dotenv()
secret_map = {}


def get_secrets():
    QT_API_KEY = os.getenv("QT_API_KEY")
    QT_REDIRECT = os.getenv("QT_REDIRECT")
    secret_map["QT_API_KEY"] = QT_API_KEY
    secret_map["QT_REDIRECT"] = QT_REDIRECT
