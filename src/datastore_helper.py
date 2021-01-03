from google.cloud import datastore


def retrieve_account_by_api_key(secret_map):
  if secret_map['QT_API_KEY']:
    datastore_client = datastore.Client()
    print('Retrieving Client Info... \U0001F336 \n')
    key = datastore_client.key('account', secret_map['QT_API_KEY'])
    account = datastore_client.get(key)
    return account
  else:
    print('\033[93m' + 'You must add .env! Consult the README.md \U0001F6AB' + '\033[0m')
    raise

def insert_new_account(name, account):
  datastore_client = datastore.Client()
  kind = 'account'
  key = datastore_client.key(kind, name)
  new_account = datastore.Entity(key=key)
  new_account.update({
    'qt_refresh': account['qt_refresh'],
    'cash_invested': account['cash_invested'],
    'qt_account_number': account['qt_account_number'],
    'spreadsheet_id': account['spreadsheet_id'],
  })
  datastore_client.put(new_account)
  