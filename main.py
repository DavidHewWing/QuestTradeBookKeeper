import src.gsauth as gsauth
import src.qtauth as qtauth
import src.master_controller as master_controller
import src.settings as settings
import src.datastore_helper as datastore_helper

import os
import json
from google.cloud import datastore


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./src/tokens/credentials.json"

# # Authentication
settings.get_secrets()
account = datastore_helper.retrieve_account_by_api_key(settings.secret_map)
settings.add_to_secrets('account', account)
qtauth.qt_authentication(settings.secret_map)
gsauth.gs_auth()
print('Authentication Complete! \U0001F680 \n')

master_controller.run(settings.secret_map['account'])

def run(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Finished'