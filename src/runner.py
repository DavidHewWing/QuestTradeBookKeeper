from src.auth import gsauth, qtauth
from src import qt_controller
from src import gscontroller
from src import master_controller
from settings import get_secrets, secret_map

# Authentication
get_secrets()
qtauth.qt_authentication(secret_map)
gsauth.gs_auth()
print('Authentication Complete! \U0001F680 \n')

master_controller.run()
