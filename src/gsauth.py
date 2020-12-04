from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from settings import add_to_secrets

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def gs_auth():
    print('Authenticating Google Sheets... \U0001F512')
    if not os.path.isfile('./src/tokens/credentials.json'):
        print('Add credentials.json file! \U0001F4A1')
        raise

    creds = None
    if os.path.exists('./src/tokens/token.pickle'):
        with open('./src/tokens/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './src/tokens/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('./src/tokens/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    add_to_secrets('gs_service', service)
    print('Authenticated Google Sheets! \U0001F603 \n')
