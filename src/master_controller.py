from src import qt_controller
from src import gscontroller
from settings import secret_map


def run():
    # questtrade data
    account = qt_controller.get_user_account()
    positions, total = qt_controller.get_positions(account, simple=True)
    print(positions)
    print(total)

    # googlesheets data
    spreadsheet_id = gscontroller.get_spreadsheet_id()
    headers = gscontroller.get_headers(spreadsheet_id)
    print(headers)

