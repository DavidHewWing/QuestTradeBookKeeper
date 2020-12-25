from __future__ import print_function
import os.path

def gs_auth():
    print('Authenticating Google Sheets... \U0001F512')
    if not os.path.isfile('./src/tokens/credentials.json'):
        print('Add credentials.json file! Which should contain a service_account! \U0001F4A1')
        raise
    else:
        print('Service Account credentials found! \U0001F36D')
    print('Authenticated Google Sheets! \U0001F603 \n')
