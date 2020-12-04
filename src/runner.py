from src import qtauth
from src import gsauth
from src import gscontroller
from settings import get_secrets, secret_map

# Authentication
get_secrets()
qtauth.qt_authentication(secret_map)
gsauth.gs_auth()
print('Authentication Complete! \U0001F680 \n')

# Get Spreadsheet Data
gscontroller.get_spreadsheet_id()
gscontroller.sample(secret_map['gs_service'], secret_map['spreadsheet_id'])
