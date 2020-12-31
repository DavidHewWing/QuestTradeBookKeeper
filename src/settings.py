import os
from dotenv import load_dotenv
 
load_dotenv()
secret_map = {}


def get_secrets():
    QT_API_KEY = os.getenv("QT_API_KEY")
    secret_map["QT_API_KEY"] = QT_API_KEY


def add_to_secrets(key, value):
    secret_map[key] = value
