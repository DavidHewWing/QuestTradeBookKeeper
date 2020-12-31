import gsauth
import qtauth
import master_controller
import settings


# Authentication
settings.get_secrets()
qtauth.qt_authentication(settings.secret_map)
gsauth.gs_auth()
print('Authentication Complete! \U0001F680 \n')

master_controller.run()

# def run(request):
#     request_json = request.get_json()
#     if request.args and 'message' in request.args:
#         return request.args.get('message')
#     elif request_json and 'message' in request_json:
#         return request_json['message']
#     else:
#         return f'Hello World!'
